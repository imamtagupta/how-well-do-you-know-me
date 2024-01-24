from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/demo"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
print(f"settings.SQLALCHEMY_DATABASE_URI {settings.SQLALCHEMY_DATABASE_URI}")
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
Base = declarative_base()
metadata = Base.metadata
