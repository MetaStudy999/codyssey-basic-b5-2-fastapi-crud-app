# B5-2 R01 Environment

## Golden Path

Phase C의 기본 실행 경로는 **Python 3.10+ 로컬 가상환경 + FastAPI/Uvicorn + SQLite**입니다.

```text
repository
└── training/round-01-clear/
    ├── reference/
    │   ├── .venv/       # Runtime 생성, Git 제외
    │   ├── database.db  # Runtime 생성, Git 제외
    │   └── app/
    └── environment/
```

## 파일 역할

- `setup.sh`: 가상환경과 의존성 설치를 재현하는 보조 스크립트
- `verify.sh`: Reference 구조/문법/핵심 패턴을 검사하며 시스템을 변경하지 않음
- `inspect_db.py`: 실제 생성된 SQLite DB 행을 직접 확인
- `reset.sh`: 현재 B5-2 R01이 만든 `.venv`, `database.db`, cache만 제거

## R01 원칙

처음 실제 수행할 때는 핵심 명령을 사용자가 수동으로 실행해 의미를 이해합니다. `setup.sh`는 복구/재현용입니다.

## Runtime 전 확인

```bash
python3 --version
pwd
git status --short
```

Python 3.10 이상과 올바른 경로를 확인한 뒤 진행합니다.

## 주의

`database.db`는 상대경로 SQLite URL을 사용하므로 **`training/round-01-clear/reference`에서 Uvicorn을 실행**하는 것을 Golden Path로 고정합니다.
