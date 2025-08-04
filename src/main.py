from dotenv import load_dotenv

load_dotenv()
from typing import Union
from fastapi import FastAPI
from .database.db import init_db
from .models import *

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}
