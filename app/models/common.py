from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional, Dict

class Link(BaseModel):
    title: Optional[str] = None
    url: HttpUrl

class Policy(BaseModel):
    type: str
    title: Optional[str] = None
    url: Optional[HttpUrl] = None
    content: Optional[str] = None

class FAQItem(BaseModel):
    question: str
    answer: str
    url: Optional[HttpUrl] = None

class ContactInfo(BaseModel):
    emails: List[str] = Field(default_factory=list)
    phones: List[str] = Field(default_factory=list)
    address_blocks: List[str] = Field(default_factory=list)
    contact_page: Optional[HttpUrl] = None

class SocialHandles(BaseModel):
    instagram: Optional[HttpUrl] = None
    facebook: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None
    tiktok: Optional[HttpUrl] = None
    youtube: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    others: Dict[str, HttpUrl] = Field(default_factory=dict)
