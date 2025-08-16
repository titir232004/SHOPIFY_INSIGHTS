from sqlalchemy import Column, Integer, String
from app.persistence.database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=True)
    url = Column(String(500))
    content = Column(String, nullable=True)
