from database import get_db
from models import Questions
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schema import QuestionRequest, QuestionsBase
router = APIRouter()


# class Endpoints:

@router.post("/questions", response_model=QuestionsBase)
async def create_question(question_create: QuestionRequest, db: Session = Depends(get_db)):
    db_question = Questions(**question_create.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

@router.get("/questions", response_model=list[QuestionsBase])
async def get_question(db: Session = Depends(get_db)):
    return db.query(Questions).all()

# @router.patch("/questions")
# async def update_question(self, question_id: int, new_data, db: Session = next(get_db())):
#     db_question = db.query(Questions).filter(Questions.id == question_id).first()
#     if db_question:
#         for key, value in new_data.items():
#             setattr(db_question, key, value)
#         db.commit()
#         db.refresh(db_question)
#     return db_question

# def delete_question(self, question_id: int, db: Session = next(get_db())):
#     db_question = db.query(Questions).filter(Questions.id == question_id).first()
#     if db_question:
#         db.delete(db_question)
#         db.commit()
#     return db_question