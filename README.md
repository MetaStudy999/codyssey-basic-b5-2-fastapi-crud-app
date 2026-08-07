# codyssey-basic-b5-2-fastapi-crud-app

글을 쓰고·보고·고치고·지울 수 있는 게시판형 FastAPI + Jinja2 + SQLite 웹 서비스입니다.

## 미션 범위

- 단일 `Memo` 모델
- Jinja2 SSR
- 목록 / 상세 / 등록 / 수정 / 삭제
- Router → Service → Repository → Model 계층 분리
- HTML Form + `Form()`
- 등록/수정/삭제 후 `303` PRG(Post-Redirect-Get)
- SQLite + SQLAlchemy ORM + `Depends` Session
- 존재하지 않는 ID 안내 화면
- 간단한 필수값 검증(보너스 범위)

인증/인가와 모델 간 관계는 B5-2 제약에 따라 구현하지 않습니다.

## 요구 환경

- Python 3.10 이상
- 외부 패키지는 미션에서 허용한 아래 5개만 사용합니다.
  - `fastapi`
  - `uvicorn`
  - `sqlalchemy`
  - `jinja2`
  - `python-multipart`

## 1. 가상환경 만들기

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2. 패키지 설치

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. 서버 실행

프로젝트 루트에서 실행합니다.

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

브라우저에서 다음 주소를 엽니다.

```text
http://localhost:8000
```

정상이라면 홈 화면에서 **메모 목록 보기**, **새 메모 작성** 링크를 확인할 수 있습니다.

## 화면 / 라우트

| Method | Path | 역할 |
|---|---|---|
| GET | `/` | 홈 |
| GET | `/memos` | 목록 |
| GET | `/memos/new` | 등록 폼 |
| POST | `/memos` | 등록 후 303 redirect |
| GET | `/memos/{id}` | 상세 |
| GET | `/memos/{id}/edit` | 수정 폼 |
| POST | `/memos/{id}/edit` | 수정 후 303 redirect |
| POST | `/memos/{id}/delete` | 삭제 후 303 redirect |

## 프로젝트 구조

```text
app/
├── main.py
├── database.py
├── models/          # SQLAlchemy ORM 모델
├── repositories/    # DB 접근
├── services/        # 비즈니스 규칙
├── routers/         # HTTP 요청/응답, 화면 전환
└── templates/       # Jinja2 SSR
scripts/
└── verify_db.py     # SQLite 직접 확인
tests/               # 표준 unittest 기반 자동 검증
docs/
└── LEARNING.md      # 평가 설명 항목 학습 가이드
```

## SQLite 데이터 직접 확인

서버를 한 번 실행하면 프로젝트 루트에 `database.db`가 생성됩니다. 메모를 등록한 뒤:

```bash
python scripts/verify_db.py
```

예상 형태:

```text
database: .../database.db
memo_count: 1
(1, '첫 메모', '내용', '2026-...')
```

실제 값은 사용자가 입력한 데이터에 따라 달라집니다.

## 자동 테스트

추가 테스트 라이브러리 없이 Python 표준 `unittest`를 사용합니다.

```bash
python -m unittest discover -s tests -v
```

HTTP 통합 테스트는 테스트용 임시 SQLite DB를 사용해 Uvicorn을 `127.0.0.1:8000`에 실행합니다. 해당 포트가 이미 사용 중이면 먼저 기존 서버를 종료한 뒤 테스트하세요.

## PRG 확인 방법

등록/수정/삭제 POST가 `303`을 반환하고 `Location`으로 GET 화면을 가리키는지 다음 자동 테스트로 확인할 수 있습니다.

```bash
python -m unittest tests.test_http_flow -v
```

## 문서

- [원본 미션](./b5-2-mission.md)
- [평가문항](./b5-2-evaluation.md)
- [Mission Work Packet](./MISSION-WORK-PACKET.md)
- [학습 가이드](./docs/LEARNING.md)
