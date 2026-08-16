# B5-2 Requirement → Implementation → Verification → Evidence

Source of Truth: `b5-2-mission.pdf` → `b5-2-mission.md` → `b5-2-evaluation.md`.

| ID | 공식 요구사항 | Reference 구현 | 검증 방법 | Phase C Evidence |
|---|---|---|---|---|
| R01 | `GET /` 홈 + 목적 설명 + 링크 2개 이상 | `reference/app/routers/home.py`, `templates/home.html` | 브라우저 `GET /` | 홈 화면 캡처 |
| R02 | 단일 모델 CRUD | Memo model/router/service/repository/templates | 등록→목록→상세→수정→삭제 | CRUD 전후 화면 |
| R03 | Jinja2 SSR / `TemplateResponse` | 모든 주요 GET 화면 템플릿 렌더링 | 브라우저 응답 확인 | 각 주요 화면 |
| R04 | 등록/수정 HTML Form + `Form()` + POST | `memos/form.html`, `routers/memos.py` | 폼 제출 | 등록/수정 요청 결과 |
| R05 | 등록/수정/삭제 후 PRG + `303` | `RedirectResponse(..., status_code=303)` | POST 후 Location/최종 GET 확인, 새로고침 | 개발자도구 또는 동작 기록 |
| R06 | routers/services/repositories/models 분리 | `reference/app/*` 디렉터리 | 구조/코드 검토 | 트리 출력 |
| R07 | SQLite + SQLAlchemy ORM | `database.py`, `Memo`, repository | 서버 기동 후 `database.db`, CRUD | DB 파일 + `inspect_db.py` 출력 |
| R08 | `Session` CRUD | `MemoRepository`의 query/add/commit/delete | DB 전후 확인 | DB 조회 출력 |
| R09 | `Depends` DB 세션 주입 | `Depends(get_db)` | 코드 및 요청 처리 | 코드/실행 근거 |
| R10 | 존재하지 않는 데이터 처리 | 404 `not_found.html` | `/memos/999999` | 404 안내 화면 |
| R11 | 상세 전체 필드 + 수정/삭제/목록 링크 | `memos/detail.html` | 상세 화면 | 상세 화면 캡처 |
| R12 | requirements 목록 | `reference/requirements.txt` | 파일 확인/설치 | 설치 로그 |
| R13 | localhost:8000 실행 | `uvicorn app.main:app --reload` | 실제 서버 기동 | 터미널 + 브라우저 |
| R14 | Python 3.10+ | Environment 문서/Phase C baseline | `python --version` | 버전 출력 |
| R15 | 외부 라이브러리 제한 | requirements 5종만 사용 | requirements 검토 | 파일 내용 |
| R16 | 인증/인가 미구현 | Reference 범위에서 제외 | 코드 검토 | 설명 |
| R17 | 모델 간 관계 미구현 | 단일 `Memo` 모델 | 코드 검토 | 설명 |
| R18 | README 실행 절차 | `reference/README.md`, Round Guide | 문서 따라 실행 | 실행 성공 기록 |

## 보너스

Reference는 필수 요구사항을 먼저 닫기 위해 제목/내용 공백 검증만 최소 추가했습니다. 검색 기능 등은 현재 CLEAR 필수 범위로 승격하지 않습니다.

## 상태 원칙

Reference 파일이 있다는 이유로 Runtime 항목을 PASS 처리하지 않습니다. 브라우저, 실제 DB, 303 Redirect, 새로고침 중복 방지 등은 Phase C에서 실제 실행 결과로만 Evidence를 확정합니다.
