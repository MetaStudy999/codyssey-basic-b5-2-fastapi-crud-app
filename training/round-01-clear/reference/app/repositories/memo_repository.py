from sqlalchemy.orm import Session

from app.models.memo import Memo


class MemoRepository:
    """Keep SQLAlchemy data-access code out of routers and services."""

    def list_all(self, db: Session) -> list[Memo]:
        return db.query(Memo).order_by(Memo.id.desc()).all()

    def get_by_id(self, db: Session, memo_id: int) -> Memo | None:
        return db.query(Memo).filter(Memo.id == memo_id).first()

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
