import os

from sqlmodel import create_engine, SQLModel, Session


DATABASE_CONNECTION_STRING = os.environ.get("DATABASE_CONNECTION_STRING")

if not DATABASE_CONNECTION_STRING or DATABASE_CONNECTION_STRING == "":
    raise ValueError("DATABASE_CONNECTION_STRING not found in environment variables.")

engine = create_engine(DATABASE_CONNECTION_STRING, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
