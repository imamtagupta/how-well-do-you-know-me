from database import get_db
from models import QuestionOptionsAssociation
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schema import QuestionOptionsAssociationRequest, QuestionOptionsAssociationBase

router = APIRouter()

@router.post("/question-options-associations", response_model=QuestionOptionsAssociationBase)
async def create_association(association_create: QuestionOptionsAssociationRequest, db: Session = Depends(get_db)):
    db_association = QuestionOptionsAssociation(**association_create.dict())
    db.add(db_association)
    db.commit()
    db.refresh(db_association)
    return db_association

@router.get("/question-options-associations", response_model=list[QuestionOptionsAssociationBase])
async def get_associations(db: Session = Depends(get_db)):
    return db.query(QuestionOptionsAssociation).all()

@router.get("/question-options-associations/{association_id}", response_model=QuestionOptionsAssociationBase)
async def get_association_by_id(association_id: int, db: Session = Depends(get_db)):
    return db.query(QuestionOptionsAssociation).filter(QuestionOptionsAssociation.id == association_id).first()

@router.put("/question-options-associations/{association_id}", response_model=QuestionOptionsAssociationBase)
async def update_association(association_id: int, association_update: QuestionOptionsAssociationRequest, db: Session = Depends(get_db)):
    db_association = db.query(QuestionOptionsAssociation).filter(QuestionOptionsAssociation.id == association_id).first()
    if db_association:
        for key, value in association_update.dict().items():
            setattr(db_association, key, value)
        db.commit()
        db.refresh(db_association)
        return db_association
    raise HTTPException(status_code=404, detail="Association not found")

@router.delete("/question-options-associations/{association_id}", response_model=QuestionOptionsAssociationBase)
async def delete_association(association_id: int, db: Session = Depends(get_db)):
    db_association = db.query(QuestionOptionsAssociation).filter(QuestionOptionsAssociation.id == association_id).first()
    if db_association:
        db.delete(db_association)
        db.commit()
        return db_association
    raise HTTPException(status_code=404, detail="Association not found")
