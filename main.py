from fastapi import FastAPI
from app.router import *
from app.utills.db import db_init,Base

Base.metadata.create_all(db_init)

app=FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"massage": "okk."}
