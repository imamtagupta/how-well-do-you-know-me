from database import Base
from sqlalchemy import Column, INTEGER, String

class Questions(Base):
    
    __tablename__ = 'question'

    id = Column(INTEGER, primary_key=True, unique=True) 
    title = Column(String)
    descriptions = Column(String)
    