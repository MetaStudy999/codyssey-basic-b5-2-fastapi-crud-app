import sqlite3
from pathlib import Path


DB_PATH = Path("database.db")

if not DB_PATH.exists():
    raise SystemExit("database.db가 없습니다. 먼저 서버를 실행하고 메모를 등록하세요.")

with sqlite3.connect(DB_PATH) as connection:
    rows = connection.execute(
        "SELECT id, title, content, created_at FROM memos ORDER BY id DESC"
    ).fetchall()

print(f"database: {DB_PATH.resolve()}")
print(f"memo_count: {len(rows)}")
for row in rows:
    print(row)
