# B5-2 R01 — Reference Build

## Source of Truth

1. `b5-2-mission.pdf`
2. `b5-2-mission.md`
3. `b5-2-evaluation.md`

## Reference 주제

단일 도메인 **Memo(메모)** 관리 웹 애플리케이션.

공식 미션 범위를 벗어나지 않도록 인증/인가와 모델 간 연관관계는 구현하지 않습니다.

## Reference Complete 구조

```text
training/round-01-clear/
├── README.md
├── REFERENCE-BUILD.md
├── REFERENCE-STATUS.md
├── BEGINNER-GUIDE.md
├── CHECKLIST.md
├── reference/
│   ├── README.md
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── database.py
│       ├── routers/
│       │   ├── home.py
│       │   └── memos.py
│       ├── services/
│       │   └── memo_service.py
│       ├── repositories/
│       │   └── memo_repository.py
│       ├── models/
│       │   └── memo.py
│       └── templates/
│           ├── base.html
│           ├── home.html
│           ├── not_found.html
│           └── memos/
│               ├── list.html
│               ├── detail.html
│               └── form.html
├── environment/
│   ├── setup.sh
│   ├── verify.sh
│   ├── reset.sh
│   └── inspect_db.py
├── docs/
│   ├── requirements-mapping.md
│   └── evaluation-qa.md
└── evidence/
    └── README.md
```

## 구현 선택

### 1. 라우팅

- 홈 `GET /`
- 목록 `GET /memos/`
- 등록 폼 `GET /memos/new`
- 등록 `POST /memos`
- 상세 `GET /memos/{id}`
- 수정 폼 `GET /memos/{id}/edit`
- 수정 `POST /memos/{id}/edit`
- 삭제 `POST /memos/{id}/delete`

### 2. PRG

등록/수정/삭제 성공 시 모두 `303` Redirect를 사용합니다.

### 3. 데이터

SQLite `database.db` + SQLAlchemy ORM `Memo` 단일 모델을 사용합니다.

### 4. 레이어

- Router: HTTP/SSR/Redirect
- Service: 입력 검증/비즈니스 규칙
- Repository: DB 접근
- Model: ORM 구조

### 5. 오류 처리

존재하지 않는 메모는 HTTP 404 + 안내 템플릿으로 처리합니다.

### 6. 최소 검증

`environment/verify.sh`는 파일 구조, Python syntax, PRG 303, Form, Depends, SQLite 설정, Repository CRUD 코드 존재를 오프라인으로 검사합니다.

실제 브라우저/DB/Redirect 동작은 Phase C Runtime에서만 PASS 처리합니다.

## 의도적으로 하지 않는 것

- 인증/인가
- 사용자 모델
- FK/relationship
- REST JSON API 분리
- 별도 JavaScript frontend
- Docker/Cloud 배포
- 공식 요구에 없는 외부 라이브러리

이들은 B5-2 CLEAR에 필요한 항목이 아니며 이후 미션 또는 고도화 범위입니다.
