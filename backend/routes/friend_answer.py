from database import get_db
from models import FriendAnswer
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schema import FriendAnswersRequest, FriendAnswersBase

router = APIRouter()


# CRUD operations for FriendAnswer model
@router.post("/friend-answers", response_model=FriendAnswersBase)
async def create_friend_answer(friend_answer_create: FriendAnswersRequest, db: Session = Depends(get_db)):
    db_friend_answer = FriendAnswer(**friend_answer_create.dict())
    db.add(db_friend_answer)
    db.commit()
    db.refresh(db_friend_answer)
    return db_friend_answer

@router.get("/friend-answers", response_model=list[FriendAnswersBase])
async def get_friend_answers(db: Session = Depends(get_db)):
    return db.query(FriendAnswer).all()

@router.get("/friend-answers/{friend_answer_id}", response_model=FriendAnswersBase)
async def get_friend_answer_by_id(friend_answer_id: int, db: Session = Depends(get_db)):
    return db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()

@router.put("/friend-answers/{friend_answer_id}", response_model=FriendAnswersBase)
async def update_friend_answer(friend_answer_id: int, friend_answer_update: FriendAnswersRequest, db: Session = Depends(get_db)):
    db_friend_answer = db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()
    if db_friend_answer:
        for key, value in friend_answer_update.dict().items():
            setattr(db_friend_answer, key, value)
        db.commit()
        db.refresh(db_friend_answer)
        return db_friend_answer
    raise HTTPException(status_code=404, detail="Friend Answer not found")

@router.delete("/friend-answers/{friend_answer_id}", response_model=FriendAnswersBase)
async def delete_friend_answer(friend_answer_id: int, db: Session = Depends(get_db)):
    db_friend_answer = db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()
    if db_friend_answer:
        db.delete(db_friend_answer)
        db.commit()
        return db_friend_answer
    raise HTTPException(status_code=404, detail="Friend Answer not found")
