from database import get_db
from models import UserAnswer, FriendAnswer
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schema import UserAnswersRequest, UserAnswersBase

router = APIRouter()

@router.post("/user-answers", response_model=UserAnswersBase)
async def create_user_answer(user_answer_create: UserAnswersRequest, db: Session = Depends(get_db)):
    db_user_answer = UserAnswer(**user_answer_create.dict())
    db.add(db_user_answer)
    db.commit()
    db.refresh(db_user_answer)
    return db_user_answer

@router.get("/user-answers", response_model=list[UserAnswersBase])
async def get_user_answers(db: Session = Depends(get_db)):
    return db.query(UserAnswer).all()

@router.get("/user-answers/{user_answer_id}", response_model=UserAnswersBase)
async def get_user_answer_by_id(user_answer_id: int, db: Session = Depends(get_db)):
    return db.query(UserAnswer).filter(UserAnswer.id == user_answer_id).first()

@router.put("/user-answers/{user_answer_id}", response_model=UserAnswersBase)
async def update_user_answer(user_answer_id: int, user_answer_update: UserAnswersRequest, db: Session = Depends(get_db)):
    db_user_answer = db.query(UserAnswer).filter(UserAnswer.id == user_answer_id).first()
    if db_user_answer:
        for key, value in user_answer_update.dict().items():
            setattr(db_user_answer, key, value)
        db.commit()
        db.refresh(db_user_answer)
        return db_user_answer
    raise HTTPException(status_code=404, detail="User Answer not found")

@router.delete("/user-answers/{user_answer_id}", response_model=UserAnswersBase)
async def delete_user_answer(user_answer_id: int, db: Session = Depends(get_db)):
    db_user_answer = db.query(UserAnswer).filter(UserAnswer.id == user_answer_id).first()
    if db_user_answer:
        db.delete(db_user_answer)
        db.commit()
        return db_user_answer
    raise HTTPException(status_code=404, detail="User Answer not found")

# CRUD operations for FriendAnswer model
@router.post("/friend-answers", response_model=FriendAnswerBase)
async def create_friend_answer(friend_answer_create: FriendAnswerRequest, db: Session = Depends(get_db)):
    db_friend_answer = FriendAnswer(**friend_answer_create.dict())
    db.add(db_friend_answer)
    db.commit()
    db.refresh(db_friend_answer)
    return db_friend_answer

@router.get("/friend-answers", response_model=list[FriendAnswerBase])
async def get_friend_answers(db: Session = Depends(get_db)):
    return db.query(FriendAnswer).all()

@router.get("/friend-answers/{friend_answer_id}", response_model=FriendAnswerBase)
async def get_friend_answer_by_id(friend_answer_id: int, db: Session = Depends(get_db)):
    return db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()

@router.put("/friend-answers/{friend_answer_id}", response_model=FriendAnswerBase)
async def update_friend_answer(friend_answer_id: int, friend_answer_update: FriendAnswerRequest, db: Session = Depends(get_db)):
    db_friend_answer = db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()
    if db_friend_answer:
        for key, value in friend_answer_update.dict().items():
            setattr(db_friend_answer, key, value)
        db.commit()
        db.refresh(db_friend_answer)
        return db_friend_answer
    raise HTTPException(status_code=404, detail="Friend Answer not found")

@router.delete("/friend-answers/{friend_answer_id}", response_model=FriendAnswerBase)
async def delete_friend_answer(friend_answer_id: int, db: Session = Depends(get_db)):
    db_friend_answer = db.query(FriendAnswer).filter(FriendAnswer.id == friend_answer_id).first()
    if db_friend_answer:
        db.delete(db_friend_answer)
        db.commit()
        return db_friend_answer
    raise HTTPException(status_code=404, detail="Friend Answer not found")
