from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from src.models import *  # noqa: F403, E402
from src.database import init_db  # noqa: E402
from src.apis.v1 import router as v1_router   # noqa: E402


app = FastAPI()

app.include_router(v1_router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
async def root():
    return {"status": "ok", "message": "Service is running smoothly."}  
