# src/models/base.py
from datetime import datetime
from sqlmodel import SQLModel, Field

class TimeMixin(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.now,
        nullable=False,
        alias="createdAt"
    )
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
        nullable=False,
        alias="updatedAt"
    )

class BaseModel(TimeMixin, SQLModel):
    class Config:
        # Allows Pydantic to read ORM objects
        from_attributes = True
        # Converts field aliases (createdAt → created_at) in responses
        populate_by_name = True
