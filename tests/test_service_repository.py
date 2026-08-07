import tempfile
import unittest
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import Memo  # noqa: F401
from app.services.memo_service import MemoService


class MemoServiceRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        db_path = Path(self.temp_dir.name) / "test.db"
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.service = MemoService()

    def tearDown(self):
        self.engine.dispose()
        self.temp_dir.cleanup()

    def test_crud_and_validation(self):
        with self.Session() as db:
            memo = self.service.create_memo(db, title=" 첫 메모 ", content=" 내용 ")
            self.assertEqual("첫 메모", memo.title)
            self.assertEqual(1, len(self.service.list_memos(db)))

            loaded = self.service.get_memo(db, memo.id)
            self.assertIsNotNone(loaded)
            self.assertEqual("내용", loaded.content)

            updated = self.service.update_memo(db, memo.id, title="수정", content="수정 내용")
            self.assertIsNotNone(updated)
            self.assertEqual("수정", updated.title)

            self.assertTrue(self.service.delete_memo(db, memo.id))
            self.assertIsNone(self.service.get_memo(db, memo.id))
            self.assertFalse(self.service.delete_memo(db, memo.id))

            with self.assertRaises(ValueError):
                self.service.create_memo(db, title="   ", content="내용")


if __name__ == "__main__":
    unittest.main()
