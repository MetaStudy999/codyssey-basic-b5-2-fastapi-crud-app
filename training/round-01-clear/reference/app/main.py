from fastapi import FastAPI

from app.database import Base, engine
from app.models.memo import Memo  # noqa: F401 - registers the ORM table metadata
from app.routers import home, memos

app = FastAPI(title="B5-2 Memo CRUD Reference")

# Round 01 Reference keeps schema creation explicit and beginner-friendly.
Base.metadata.create_all(bind=engine)

app.include_router(home.router)
app.include_router(memos.router)
