from sqlmodel import Field
from src.models.base import BaseModel


class User(BaseModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    public_key: str
    email: str | None = None
    is_active: bool = True
    is_superuser: bool = False

