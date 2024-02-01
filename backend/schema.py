from typing import Optional
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    title: str
    descriptions: str


class QuestionsBase(QuestionRequest):
    id: Optional[int]

    
