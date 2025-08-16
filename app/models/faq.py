from sqlalchemy import Column, Integer, String
from app.persistence.database import Base

class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(String(500), nullable=False)
    answer = Column(String, nullable=True)
    url = Column(String(500), nullable=True)
