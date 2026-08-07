from fastapi import FastAPI

from app.database import Base, engine
from app.models import Memo  # noqa: F401 - registers the table with SQLAlchemy metadata
from app.routers import home, memos


Base.metadata.create_all(bind=engine)

app = FastAPI(title="B5-2 Memo Board")
app.include_router(home.router)
app.include_router(memos.router)
