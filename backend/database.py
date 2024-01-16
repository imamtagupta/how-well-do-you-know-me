from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/demo"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()