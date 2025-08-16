from sqlalchemy import Column, Integer, String, Float
from app.persistence.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    url = Column(String(500))
    vendor = Column(String(255), nullable=True)
    product_type = Column(String(255), nullable=True)
    price_min = Column(Float, nullable=True)
    price_max = Column(Float, nullable=True)
