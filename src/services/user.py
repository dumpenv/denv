# services/user_service.py
from sqlmodel import Session
from src.models.user import User
from src.schemas.user import UserCreate, UserRead


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def register_user(self, user_data: UserCreate) -> UserRead:
        user = User(
            name=user_data.name, public_key=user_data.public_key, email=user_data.email
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return UserRead.model_validate(user)
