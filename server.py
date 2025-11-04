from fastapi import FastAPI
from database import models
from database.db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok","service":"running"}