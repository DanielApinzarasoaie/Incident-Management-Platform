from fastapi import FastAPI
from app.database.base import Base
from app.database.database import engine
from app.routers.incidents import router as incidents_router
  

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "Incident Management Platform",
    version = "1.0.0"
)

app.include_router(incidents_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Incident Management Platform"}   






