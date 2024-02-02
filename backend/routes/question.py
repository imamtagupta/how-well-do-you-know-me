from database import get_db
from models import Questions
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schema import QuestionRequest, QuestionsBase
router = APIRouter()


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


@router.get("/questions/{question_id}", response_model=QuestionsBase)
async def get_question_by_id(question_id: int, db: Session = Depends(get_db)):
    return db.query(Questions).filter(Questions.id == question_id).first()

@router.put("/questions/{question_id}", response_model=QuestionsBase)
async def update_question(question_id: int, question_update: QuestionRequest, db: Session = Depends(get_db)):
    db_question = db.query(Questions).filter(Questions.id == question_id).first()
    if db_question:
        for key, value in question_update.dict().items():
            setattr(db_question, key, value)
        db.commit()
        db.refresh(db_question)
        return db_question
    raise HTTPException(status_code=404, detail="Question not found")

@router.delete("/questions/{question_id}", response_model=QuestionsBase)
async def delete_question(question_id: int, db: Session = Depends(get_db)):
    db_question = db.query(Questions).filter(Questions.id == question_id).first()
    if db_question:
        db.delete(db_question)
        db.commit()
        return db_question
    raise HTTPException(status_code=404, detail="Question not found")
