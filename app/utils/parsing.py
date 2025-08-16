from bs4 import BeautifulSoup
from typing import List, Tuple

def get_meta_brand_name(html: str) -> str | None:
    soup = BeautifulSoup(html, "lxml")
    if (t := soup.find("meta", property="og:site_name")) and t.get("content"):
        return t["content"].strip()
    if soup.title and soup.title.text:
        return soup.title.text.strip()
    return None

def find_product_cards(html: str) -> List[Tuple[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    anchors = soup.select("a[href*='/products/']")
    out = []
    for a in anchors[:50]:
        href = a.get("href")
        title = a.get_text(strip=True) or a.get("aria-label") or ""
        if href:
            out.append((href, title))
    return out

def clean_text(s: str) -> str:
    return " ".join(s.split())
