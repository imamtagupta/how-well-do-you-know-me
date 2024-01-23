from database import Base
from sqlalchemy import Column, INTEGER, String, DateTime, ForeignKey

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
    
    __tablename__ = 'question_option_association'
    
    id = Column(INTEGER, primary_key=True, unique=True) 
    qid = Column(INTEGER, ForeignKey("question.id"))
    oid = Column(INTEGER, ForeignKey("option.id"))
    
    
class Users(Base):
    
    __tablename__ = 'user'
    
    id = Column(INTEGER, primary_key=True, unique=True) 
    username = Column(String)
    created_at = Column(DateTime)
    
class UserAnswer(Base):
    
    __tablename__ = 'user_answer'
    
    id = Column(INTEGER, primary_key=True, unique=True) 
    uid = Column(INTEGER, ForeignKey("user.id"))
    qid = Column(INTEGER, ForeignKey("question.id"))
    oid = Column(INTEGER, ForeignKey("option.id"))
    
    
class FriendAnswer(Base):
    
    __tablename__ = 'friend_answer'
    
    id = Column(INTEGER, primary_key=True, unique=True) 
    uid = Column(INTEGER, ForeignKey("user.id"))
    qid = Column(INTEGER, ForeignKey("question.id"))
    oid = Column(INTEGER, ForeignKey("option.id"))
    fid = Column(INTEGER, ForeignKey("user.id"))