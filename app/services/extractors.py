import httpx
from typing import List, Dict, Optional
from selectolax.parser import HTMLParser
from ..utils.url import join, COMMON_POLICY_PATHS, COMMON_FAQ_PATHS, COMMON_IMPORTANT_LINKS
from ..utils.text import extract_emails, extract_phones, SOCIAL_MAP
from ..utils.parsing import clean_text

HEADERS_TEMPLATE = lambda ua: {"User-Agent": ua, "Accept": "text/html,application/json;q=0.9"}


async def get(client: httpx.AsyncClient, url: str) -> Optional[httpx.Response]:
    try:
        r = await client.get(url, timeout=None, follow_redirects=True)
        if r.status_code < 400:
            return r
    except Exception:
        return None
    return None


async def fetch_products_json(client: httpx.AsyncClient, base: str) -> List[Dict]:
    # Standard Shopify feed
    r = await get(client, join(base, "/products.json?limit=250"))
    if not r:
        return []
    try:
        data = r.json()
        return data.get("products", []) if isinstance(data, dict) else []
    except Exception:
        return []


async def fetch_homepage(client: httpx.AsyncClient, base: str) -> tuple[str, HTMLParser | None]:
    r = await get(client, base)
    if not r:
        return "", None
    html = r.text
    return html, HTMLParser(html)


async def scan_known_paths(client: httpx.AsyncClient, base: str, paths: list[str]) -> Dict[str, str]:
    out = {}
    for p in paths:
        r = await get(client, join(base, p))
        if r:
            out[p] = r.text
    return out


def extract_social_handles(html: str) -> Dict[str, str]:
    out = {}
    tree = HTMLParser(html)
    for a in tree.css("a"):
        href = a.attributes.get("href", "")
        for key, host in SOCIAL_MAP.items():
            if host in href:
                out.setdefault(key, href)
    return out


def extract_contact_info(pages: Dict[str, str] | None, home_html: str) -> dict:
    text_blobs = [home_html] + list((pages or {}).values())
    emails = set()
    phones = set()
    contact_page = None
    for html in text_blobs:
        tree = HTMLParser(html)
        text = tree.text(separator=" ")
        for e in extract_emails(text):
            emails.add(e)
        for p in extract_phones(text):
            phones.add(p)
        # crude contact page URL discovery
        for a in tree.css("a"):
            href = a.attributes.get("href", "")
            label = (a.text() or "").lower()
            if "contact" in href or "contact" in label:
                contact_page = href if href.startswith("http") else contact_page
    return {"emails": sorted(emails), "phones": sorted(phones), "contact_page": contact_page}


def html_to_plain(tree: HTMLParser | None) -> str | None:
    if not tree:
        return None
    return clean_text(tree.text(separator=" "))


def find_faqs_from_html(html: str, url: str) -> list[dict]:
    tree = HTMLParser(html)
    faqs = []
    for details in tree.css("details"):
        summary = details.css_first("summary")
        if summary:
            q = summary.text(strip=True)
            a = details.text(separator=" ").replace(q, "", 1).strip()
            if q and a:
                faqs.append({"question": q, "answer": a, "url": url})
    for h in tree.css("h2,h3,h4"):
        if "faq" in (h.text() or "").lower():
            section_text = tree.text(separator=" ")
            # Could improve here: parse Q&A sections
            break
    return faqs


async def fetch_collection_products(client: httpx.AsyncClient, base: str) -> list[dict]:
    """
    Fallback: fetch products from /collections/all page.
    """
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    url = join(base, "/collections/all")
    r = await get(client, url)
    if not r:
        return []

    soup = BeautifulSoup(r.text, "lxml")
    products = []
    seen = set()

    for a in soup.select("a[href*='/products/']"):
        href = a.get("href")
        title = a.get_text(strip=True) or a.get("aria-label") or ""
        if not href or href in seen:
            continue
        seen.add(href)

        products.append({
            "title": title,
            "handle": href.split("/")[-1],
            "url": urljoin(base, href),
            "vendor": None,
            "product_type": None,
            "tags": [],
            "images": [],
            "price_min": None,
            "price_max": None,
            "available": None
        })

    return products
