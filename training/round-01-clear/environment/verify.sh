#!/usr/bin/env bash
set -u

ROUND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="$ROUND_DIR/reference"
APP_DIR="$REF_DIR/app"
PASS=0
FAIL=0

pass() {
  printf '[PASS] %s\n' "$1"
  PASS=$((PASS + 1))
}

fail() {
  printf '[FAIL] %s\n' "$1"
  FAIL=$((FAIL + 1))
}

check_file() {
  if [[ -f "$1" ]]; then
    pass "file exists: ${1#$ROUND_DIR/}"
  else
    fail "missing file: ${1#$ROUND_DIR/}"
  fi
}

printf '=== B5-2 Reference Verification ===\n'

for path in \
  "$REF_DIR/requirements.txt" \
  "$APP_DIR/main.py" \
  "$APP_DIR/database.py" \
  "$APP_DIR/routers/home.py" \
  "$APP_DIR/routers/memos.py" \
  "$APP_DIR/services/memo_service.py" \
  "$APP_DIR/repositories/memo_repository.py" \
  "$APP_DIR/models/memo.py" \
  "$APP_DIR/templates/home.html" \
  "$APP_DIR/templates/memos/list.html" \
  "$APP_DIR/templates/memos/detail.html" \
  "$APP_DIR/templates/memos/form.html" \
  "$APP_DIR/templates/not_found.html"
do
  check_file "$path"
done

if command -v python3 >/dev/null 2>&1; then
  if python3 -m compileall -q "$APP_DIR"; then
    pass "Python syntax compileall"
  else
    fail "Python syntax compileall"
  fi
else
  fail "python3 command available"
fi

if grep -q 'RedirectResponse' "$APP_DIR/routers/memos.py" \
  && grep -q 'status_code=303' "$APP_DIR/routers/memos.py"; then
  pass "PRG RedirectResponse 303 present"
else
  fail "PRG RedirectResponse 303 present"
fi

if grep -q 'Form(' "$APP_DIR/routers/memos.py"; then
  pass "FastAPI Form() input present"
else
  fail "FastAPI Form() input present"
fi

if grep -q 'Depends(get_db)' "$APP_DIR/routers/memos.py"; then
  pass "Depends(get_db) session injection present"
else
  fail "Depends(get_db) session injection present"
fi

if grep -q 'sqlite:///./database.db' "$APP_DIR/database.py"; then
  pass "SQLite database configuration present"
else
  fail "SQLite database configuration present"
fi

if grep -q 'db.query' "$APP_DIR/repositories/memo_repository.py" \
  && grep -q 'db.add' "$APP_DIR/repositories/memo_repository.py" \
  && grep -q 'db.commit' "$APP_DIR/repositories/memo_repository.py"; then
  pass "Repository CRUD persistence operations present"
else
  fail "Repository CRUD persistence operations present"
fi

printf 'Result: %d PASS / %d FAIL\n' "$PASS" "$FAIL"
[[ "$FAIL" -eq 0 ]]
