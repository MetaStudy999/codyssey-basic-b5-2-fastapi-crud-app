import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "reference" / "database.db"

if not DB_PATH.exists():
    raise SystemExit(f"[FAIL] database not found: {DB_PATH}")

with sqlite3.connect(DB_PATH) as connection:
    rows = connection.execute(
        "SELECT id, title, content, created_at, updated_at FROM memos ORDER BY id DESC"
    ).fetchall()

print(f"[PASS] database: {DB_PATH}")
print(f"[PASS] memo rows: {len(rows)}")
for row in rows[:10]:
    print(row)
