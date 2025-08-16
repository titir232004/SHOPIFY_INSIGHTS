import httpx
from typing import Optional, List, Dict
from pydantic import HttpUrl
from ..config import settings
from ..utils.url import normalize_base, join, COMMON_POLICY_PATHS, COMMON_FAQ_PATHS, COMMON_IMPORTANT_LINKS
from ..utils.parsing import get_meta_brand_name, find_product_cards
from ..models.brand import BrandContext, Product
from ..models.common import Policy, FAQItem, SocialHandles, ContactInfo, Link
from .extractors import (
    fetch_products_json, fetch_homepage, scan_known_paths,
    extract_social_handles, extract_contact_info, html_to_plain, find_faqs_from_html
)
from .normalizers import normalize_products

class InsightsFetcher:
    def __init__(self, base_url: str):
        self.base = normalize_base(base_url)
        self.headers = {"User-Agent": settings.USER_AGENT}

    async def run(self) -> BrandContext:
        limits = httpx.Limits(max_keepalive_connections=settings.HTTP_MAX_CONNECTIONS, max_connections=settings.HTTP_MAX_CONNECTIONS)
        async with httpx.AsyncClient(headers=self.headers, limits=limits, timeout=settings.HTTP_TIMEOUT, follow_redirects=True) as client:
            # 1) homepage
            home_html, home_tree = await fetch_homepage(client, self.base)
            if not home_html:
                # Treat as 401 per spec (website not found/unreachable)
                raise ValueError("WEBSITE_NOT_FOUND")

            # 2) brand name + socials
            brand_name = get_meta_brand_name(home_html)
            socials = extract_social_handles(home_html)

            # 3) products via products.json
            raw_products = await fetch_products_json(client, self.base)
            products = normalize_products(raw_products, self.base)

            # Fallback 1: /collections/all
            if not products:
                from .extractors import fetch_collection_products
                raw_products = await fetch_collection_products(client, self.base)
                products = normalize_products(raw_products, self.base)


            # 4) hero products (heuristic: product links found on homepage that match catalog handles/titles)
            hero_cards = find_product_cards(home_html)
            hero_map = {(h or "").strip().lower() for _,h in hero_cards if h}
            by_title = {p.title.strip().lower(): p for p in products if p.title}
            hero_products: List[Product] = []
            for t in hero_map:
                if t in by_title:
                    hero_products.append(by_title[t])

            # 5) policies / faq / important links
            policies_pages = await scan_known_paths(client, self.base, COMMON_POLICY_PATHS)
            faq_pages = await scan_known_paths(client, self.base, COMMON_FAQ_PATHS)
            links_pages = await scan_known_paths(client, self.base, COMMON_IMPORTANT_LINKS)

            policies: List[Policy] = []
            for path, html in policies_pages.items():
                content = html_to_plain(None)  # we return plain only when needed; keep content None to reduce bulk
                ptype = "privacy" if "privacy" in path else \
                        "refund" if "refund" in path else \
                        "return" if "return" in path else \
                        "shipping" if "shipping" in path else "policy"
                policies.append(Policy(type=ptype, title=ptype.capitalize(), url=join(self.base, path), content=None))

            faqs: List[FAQItem] = []
            for path, html in faq_pages.items():
                for item in find_faqs_from_html(html, join(self.base, path)):
                    faqs.append(FAQItem(**item))

            # 6) contacts (scan home + discovered pages)
            contacts = extract_contact_info({**policies_pages, **faq_pages, **links_pages}, home_html)

            # 7) important links
            important_links = [Link(title=None, url=join(self.base, p)) for p in set(list(policies_pages.keys()) + list(links_pages.keys()))]

            # 8) about (try common /pages/about, else og:description)
            about_html_map = await scan_known_paths(client, self.base, ["/pages/about", "/about"])
            about_text = None
            for _, ah in about_html_map.items():
                about_text = html_to_plain(None) or ""
            if not about_text and home_tree:
                # fallback to meta description
                meta_desc = home_tree.css_first("meta[name='description'], meta[property='og:description']")
                if meta_desc and meta_desc.attributes.get("content"):
                    about_text = meta_desc.attributes["content"]

            ctx = BrandContext(
                domain=self.base.split("//")[-1].strip("/"),
                base_url=self.base, brand_name=brand_name, about=about_text or None,
                product_catalog=products, hero_products=hero_products,
                policies=policies, faqs=faqs,
                social_handles=SocialHandles(**socials), contact=ContactInfo(**contacts),
                important_links=important_links,
                meta={}
            )
            return ctx
