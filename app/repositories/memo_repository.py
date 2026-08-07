from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.memo import Memo


class MemoRepository:
    def list_all(self, db: Session) -> list[Memo]:
        statement = select(Memo).order_by(Memo.id.desc())
        return list(db.scalars(statement).all())

    def get_by_id(self, db: Session, memo_id: int) -> Memo | None:
        return db.get(Memo, memo_id)

    def create(self, db: Session, *, title: str, content: str) -> Memo:
        memo = Memo(title=title, content=content)
        db.add(memo)
        db.commit()
        db.refresh(memo)
        return memo

    def update(self, db: Session, memo: Memo, *, title: str, content: str) -> Memo:
        memo.title = title
        memo.content = content
        db.commit()
        db.refresh(memo)
        return memo

    def delete(self, db: Session, memo: Memo) -> None:
        db.delete(memo)
        db.commit()
