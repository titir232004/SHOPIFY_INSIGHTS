from urllib.parse import urljoin, urlparse

def normalize_base(url: str) -> str:
    parsed = urlparse(url)
    scheme = parsed.scheme or "https"
    netloc = parsed.netloc or parsed.path
    return f"{scheme}://{netloc}/"

def join(base: str, path: str) -> str:
    return urljoin(base, path)

COMMON_POLICY_PATHS = [
    "/policies/privacy-policy",
    "/policies/refund-policy",
    "/policies/return-policy",
    "/policies/shipping-policy",
    "/pages/privacy-policy",
    "/pages/refund-policy",
    "/pages/shipping-policy",
    "/pages/return-policy",
]
COMMON_FAQ_PATHS = [
    "/pages/faq",
    "/pages/faqs",
    "/pages/help",
    "/pages/support",
]
COMMON_IMPORTANT_LINKS = [
    "/pages/contact",
    "/pages/about",
    "/pages/track-order",
    "/apps/track",
    "/blogs",
    "/collections",
]
