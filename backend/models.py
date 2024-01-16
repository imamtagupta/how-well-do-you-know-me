from database import Base
from sqlalchemy import Column, Integer, String

class Questions(Base):
    __tablename__ = "question"
    id: Column(Integer, primary_key=True, unique=True) 
    title: Column(String)
    descriptions: Column(String)
    