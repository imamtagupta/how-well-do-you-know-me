from database import Base
from sqlalchemy import Column, INTEGER, String

class Questions(Base):
    
    __tablename__ = 'question'

    id = Column(INTEGER, primary_key=True, unique=True) 
    title = Column(String)
    descriptions = Column(String)
    

class Options(Base):
    
    __tablename__ = 'option'

    id = Column(INTEGER, primary_key=True, unique=True) 
    type = Column(String)
    value = Column(String)
    
class QuestionOptionsAssociation(Base):
    pass