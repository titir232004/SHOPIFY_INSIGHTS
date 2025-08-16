from sqlalchemy import Column, Integer, String
from app.persistence.database import Base

class ContactInfo(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(500), nullable=True)
    contact_page = Column(String(500), nullable=True)
