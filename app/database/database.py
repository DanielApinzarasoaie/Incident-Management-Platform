from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL : 

    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    DATABASE_URL={
        f"postgresql://"
        f"{DB_USER}:"
        f"{DB_PASSWORD}"
        f"@{DB_HOST}:"
        f"{DB_PORT}/"
        f"{DB_NAME}"
    }

if not DATABASE_URL:
    raise ValueError(
        "Database configuration missing"
    )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db = SessionLocal()

    try: 
        yield db

    finally:
        db.close()