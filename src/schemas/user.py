# schemas/user.py
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    public_key: str = Field(..., min_length=10)
    email: EmailStr | None = None


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
