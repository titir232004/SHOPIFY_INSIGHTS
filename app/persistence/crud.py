from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.models.policy import Policy
from app.models.faq import FAQ
from app.models.social import SocialHandle
from app.models.contact import ContactInfo

# --- PRODUCTS ---
async def create_product(db: AsyncSession, data: dict):
    product = Product(**data)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

# --- POLICIES ---
async def create_policy(db: AsyncSession, data: dict):
    policy = Policy(**data)
    db.add(policy)
    await db.commit()
    await db.refresh(policy)
    return policy

# --- FAQ ---
async def create_faq(db: AsyncSession, data: dict):
    faq = FAQ(**data)
    db.add(faq)
    await db.commit()
    await db.refresh(faq)
    return faq

# --- SOCIALS ---
async def create_social(db: AsyncSession, data: dict):
    social = SocialHandle(**data)
    db.add(social)
    await db.commit()
    await db.refresh(social)
    return social

# --- CONTACT INFO ---
async def create_contact(db: AsyncSession, data: dict):
    contact = ContactInfo(**data)
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact
