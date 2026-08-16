from sqlalchemy.orm import Session

from app.models.memo import Memo
from app.repositories.memo_repository import MemoRepository


class ValidationError(ValueError):
    """Raised when a memo form contains invalid data."""


class MemoService:
    """Own business rules; repository owns persistence details."""

    def __init__(self, repository: MemoRepository | None = None) -> None:
        self.repository = repository or MemoRepository()

    def list_memos(self, db: Session) -> list[Memo]:
        return self.repository.list_all(db)

    def get_memo(self, db: Session, memo_id: int) -> Memo | None:
        return self.repository.get_by_id(db, memo_id)

    def create_memo(self, db: Session, *, title: str, content: str) -> Memo:
        clean_title, clean_content = self._validate(title, content)
        return self.repository.create(db, title=clean_title, content=clean_content)

    def update_memo(self, db: Session, memo: Memo, *, title: str, content: str) -> Memo:
        clean_title, clean_content = self._validate(title, content)
        return self.repository.update(db, memo, title=clean_title, content=clean_content)

    def delete_memo(self, db: Session, memo: Memo) -> None:
        self.repository.delete(db, memo)

    @staticmethod
    def _validate(title: str, content: str) -> tuple[str, str]:
        clean_title = title.strip()
        clean_content = content.strip()

        if not clean_title:
            raise ValidationError("제목을 입력해 주세요.")
        if not clean_content:
            raise ValidationError("내용을 입력해 주세요.")
        if len(clean_title) > 120:
            raise ValidationError("제목은 120자 이하로 입력해 주세요.")

        return clean_title, clean_content
