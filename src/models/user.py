from sqlmodel import Field, SQLModel
from datetime import datetime


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    public_key: str
    email: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    created_at: datetime = Field(default_factory=datetime.now(), alias="createdAt")
    updated_at: datetime = Field(default_factory=datetime.now(), alias="updatedAt")
