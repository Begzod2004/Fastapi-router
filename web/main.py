from fastapi import FastAPI
from . import models
from .routes import router
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def home():
  return "Welcome"

app.include_router(router, prefix="/cotigory", tags=["cotigory"])
