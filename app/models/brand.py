from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict
from .common import Policy, FAQItem, ContactInfo, SocialHandles, Link

class Product(BaseModel):
    id: Optional[int] = None
    title: str
    handle: Optional[str] = None
    url: Optional[HttpUrl] = None
    vendor: Optional[str] = None
    product_type: Optional[str] = None
    tags: List[str] = []
    images: List[HttpUrl] = []
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    available: Optional[bool] = None

class BrandContext(BaseModel):
    domain: str
    base_url: HttpUrl
    brand_name: Optional[str] = None
    about: Optional[str] = None

    product_catalog: List[Product] = []
    hero_products: List[Product] = []

    policies: List[Policy] = []
    faqs: List[FAQItem] = []

    social_handles: SocialHandles = SocialHandles()
    contact: ContactInfo = ContactInfo()
    important_links: List[Link] = []

    meta: Dict[str, str] = {}
