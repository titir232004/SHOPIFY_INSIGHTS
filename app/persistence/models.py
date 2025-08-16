from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from typing import List

class Base(DeclarativeBase):
    pass

class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    domain: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    brand_name: Mapped[str] = mapped_column(String(255), nullable=True)
    about: Mapped[str] = mapped_column(String(2000), nullable=True)

    products: Mapped[List["Product"]] = relationship(back_populates="brand")

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    url: Mapped[str] = mapped_column(String(1024))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brands.id"))

    brand: Mapped["Brand"] = relationship(back_populates="products")
