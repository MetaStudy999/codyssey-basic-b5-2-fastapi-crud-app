#!/usr/bin/env bash
set -euo pipefail

ROUND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="$ROUND_DIR/reference"

cd "$REF_DIR"

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

printf '[PASS] B5-2 virtual environment prepared at %s/.venv\n' "$REF_DIR"
printf '[INFO] Start server with: cd %s && source .venv/bin/activate && uvicorn app.main:app --reload\n' "$REF_DIR"
