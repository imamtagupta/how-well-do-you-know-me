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