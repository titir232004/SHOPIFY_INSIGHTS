import re

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{3,4}\)?[\s-]?)?\d{3}[\s-]?\d{4,}")
SOCIAL_MAP = {
    "instagram": "instagram.com",
    "facebook": "facebook.com",
    "twitter": "twitter.com",
    "tiktok": "tiktok.com",
    "youtube": "youtube.com",
    "linkedin": "linkedin.com",
}

def extract_emails(text: str):
    return sorted(set(EMAIL_RE.findall(text)))

def extract_phones(text: str):
    return sorted(set(p.strip() for p in PHONE_RE.findall(text) if len(p.strip()) >= 8))
