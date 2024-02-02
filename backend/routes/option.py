from database import get_db
from models import Options
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schema import OptionsRequest, OptionsBase

router = APIRouter()

@router.post("/options", response_model=OptionsBase)
async def create_option(option_create: OptionsRequest, db: Session = Depends(get_db)):
    db_option = Options(**option_create.dict())
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

@router.get("/options", response_model=list[OptionsBase])
async def get_options(db: Session = Depends(get_db)):
    return db.query(Options).all()

@router.get("/options/{option_id}", response_model=OptionsBase)
async def get_option_by_id(option_id: int, db: Session = Depends(get_db)):
    return db.query(Options).filter(Options.id == option_id).first()

@router.put("/options/{option_id}", response_model=OptionsBase)
async def update_option(option_id: int, option_update: OptionsRequest, db: Session = Depends(get_db)):
    db_option = db.query(Options).filter(Options.id == option_id).first()
    if db_option:
        for key, value in option_update.dict().items():
            setattr(db_option, key, value)
        db.commit()
        db.refresh(db_option)
        return db_option
    raise HTTPException(status_code=404, detail="Option not found")

@router.delete("/options/{option_id}", response_model=OptionsBase)
async def delete_option(option_id: int, db: Session = Depends(get_db)):
    db_option = db.query(Options).filter(Options.id == option_id).first()
    if db_option:
        db.delete(db_option)
        db.commit()
        return db_option
    raise HTTPException(status_code=404, detail="Option not found")
