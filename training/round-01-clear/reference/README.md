# B5-2 Reference — Memo CRUD

공식 B5-2 Mission/Evaluation을 충족하도록 설계한 **Reference 기준본**입니다. 실제 Runtime PASS/Evidence는 Phase C에서 사용자 환경에서 검증합니다.

## 무엇을 만드는가

단일 도메인 `Memo`를 대상으로 다음 SSR 화면 흐름을 구현합니다.

- `GET /` 홈
- `GET /memos/` 목록
- `GET /memos/new` 등록 폼
- `POST /memos` 등록 → `303` Redirect
- `GET /memos/{id}` 상세
- `GET /memos/{id}/edit` 수정 폼
- `POST /memos/{id}/edit` 수정 → `303` Redirect
- `POST /memos/{id}/delete` 삭제 → `303` Redirect

## 구조

```text
reference/
├── requirements.txt
├── README.md
└── app/
    ├── main.py
    ├── database.py
    ├── routers/
    │   ├── home.py
    │   └── memos.py
    ├── services/
    │   └── memo_service.py
    ├── repositories/
    │   └── memo_repository.py
    ├── models/
    │   └── memo.py
    └── templates/
        ├── base.html
        ├── home.html
        ├── not_found.html
        └── memos/
            ├── list.html
            ├── detail.html
            └── form.html
```

## 역할 분리

- `routers`: HTTP 요청, `Form()`, `Depends()`, 화면/Redirect 응답
- `services`: 입력 검증과 비즈니스 규칙
- `repositories`: SQLAlchemy `Session`을 통한 CRUD 데이터 접근
- `models`: SQLAlchemy ORM 모델
- `templates`: Jinja2 SSR 화면

## 로컬 실행 — Phase C

아래 명령은 `training/round-01-clear/reference`에서 실행합니다.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

브라우저에서 `http://localhost:8000`에 접속합니다.

> Windows PowerShell의 가상환경 활성화는 `.venv\Scripts\Activate.ps1`입니다.

## DB 확인

서버가 최초 기동되면 현재 디렉터리에 `database.db`가 생성됩니다. Runtime 검증 시 `environment/inspect_db.py`로 저장 결과를 직접 확인합니다.

## PRG

등록·수정·삭제 성공 후 `RedirectResponse(..., status_code=303)`으로 GET 화면으로 이동합니다. 따라서 새로고침이 직전 POST 요청을 반복하지 않습니다.

## 범위 제한

공식 제약에 맞춰 로그인/인증/인가, 모델 간 연관관계는 구현하지 않습니다. 외부 런타임 의존성도 `fastapi`, `uvicorn`, `sqlalchemy`, `jinja2`, `python-multipart` 범위로 제한합니다.
