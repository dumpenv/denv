from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.database.db import get_session
from src.schemas.user import UserCreate
from src.services.user import UserService


userRouter = APIRouter(prefix="/user", tags=["user"])


@userRouter.post("/register")
async def register_user(user_data: UserCreate, session: Session = Depends(get_session)):
    service = UserService(session)
    return await service.register_user(user_data)
