from sqlalchemy.orm import Session

from app.models.memo import Memo
from app.repositories.memo_repository import MemoRepository


class MemoService:
    def __init__(self, repository: MemoRepository | None = None):
        self.repository = repository or MemoRepository()

    def list_memos(self, db: Session) -> list[Memo]:
        return self.repository.list_all(db)

    def get_memo(self, db: Session, memo_id: int) -> Memo | None:
        return self.repository.get_by_id(db, memo_id)

    def create_memo(self, db: Session, *, title: str, content: str) -> Memo:
        clean_title, clean_content = self._validate(title, content)
        return self.repository.create(db, title=clean_title, content=clean_content)

    def update_memo(self, db: Session, memo_id: int, *, title: str, content: str) -> Memo | None:
        memo = self.repository.get_by_id(db, memo_id)
        if memo is None:
            return None
        clean_title, clean_content = self._validate(title, content)
        return self.repository.update(db, memo, title=clean_title, content=clean_content)

    def delete_memo(self, db: Session, memo_id: int) -> bool:
        memo = self.repository.get_by_id(db, memo_id)
        if memo is None:
            return False
        self.repository.delete(db, memo)
        return True

    @staticmethod
    def _validate(title: str, content: str) -> tuple[str, str]:
        clean_title = title.strip()
        clean_content = content.strip()
        if not clean_title or not clean_content:
            raise ValueError("제목과 내용은 비워 둘 수 없습니다.")
        return clean_title, clean_content
