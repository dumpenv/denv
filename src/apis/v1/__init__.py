# __init__.py
from fastapi import APIRouter
from src.apis.v1.user import userRouter

router = APIRouter(prefix="/v1")
router.include_router(userRouter)
