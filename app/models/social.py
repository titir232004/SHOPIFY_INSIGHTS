from sqlalchemy import Column, Integer, String
from app.persistence.database import Base

class SocialHandle(Base):
    __tablename__ = "social_handles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    platform = Column(String(50), nullable=False)
    url = Column(String(500), nullable=False)
