from typing import Optional
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    title: str
    descriptions: str


class QuestionsBase(QuestionRequest):
    id: int

    
class OptionsRequest(BaseModel):
    type: str
    value: str
    
class OptionsBase(OptionsRequest):
    id: int


class QuestionOptionsAssociationRequest(BaseModel):
    qid: int
    oid: int

class QuestionOptionsAssociationBase(QuestionOptionsAssociationRequest):
    id: int
    

class UserAnswersRequest(BaseModel):
    uid: int
    qid: int
    oid: int
    
class UserAnswersBase(UserAnswersRequest):
    id: int


class FriendAnswersRequest(BaseModel):
    qid: int
    oid: int
    uid: int
    fid: int 

class FriendAnswersBase(FriendAnswersRequest):
    id: int