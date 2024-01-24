from database import get_db
from models import Questions
from sqlalchemy.orm import Session

class Endpoints:

    def create_question(question_create, db: Session = next(get_db())):
        db_question = Questions(**question_create.dict())
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question
    
    def get_question(self, question_id: int, db: Session = next(get_db())):
        return db.query(Questions).filter(Questions.id == question_id).first()

    def update_question(self, question_id: int, new_data, db: Session = next(get_db())):

        db_question = db.query(Questions).filter(Questions.id == question_id).first()

        if db_question:
            for key, value in new_data.items():
                setattr(db_question, key, value)

            db.commit()
            db.refresh(db_question)

        return db_question

    def delete_question(self, question_id: int, db: Session = next(get_db())):

        db_question = db.query(Questions).filter(Questions.id == question_id).first()

        if db_question:
            db.delete(db_question)
            db.commit()

        return db_question