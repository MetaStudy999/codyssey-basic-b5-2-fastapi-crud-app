# B5-2 학습 가이드 — 구현을 설명할 수 있게 만들기

## 1. 요청이 이동하는 길

브라우저 요청은 이 저장소에서 다음 순서로 이동한다.

```text
Browser
  → app/routers/memos.py          (HTTP 요청/응답, 화면 전환)
  → app/services/memo_service.py  (검증과 비즈니스 규칙)
  → app/repositories/memo_repository.py (DB CRUD)
  → app/models/memo.py            (memos 테이블 매핑)
  → SQLite database.db
  → Jinja2 template
  → Browser
```

라우터가 SQLAlchemy 쿼리를 직접 수행하지 않는 이유는 HTTP 처리와 DB 접근 책임을 섞지 않기 위해서다. 서비스는 "제목/내용은 비어 있으면 안 된다" 같은 규칙을 가지고, 저장소는 `select`, `db.get`, `add`, `commit`, `delete` 같은 데이터 접근만 담당한다.

## 2. GET과 POST

- `GET`은 화면이나 데이터를 조회할 때 사용한다. 이 앱의 `/`, `/memos`, `/memos/{id}`, `/memos/new`, `/memos/{id}/edit`가 예다.
- `POST`는 서버 상태를 바꾸는 등록/수정/삭제에 사용한다.

조회와 변경을 분리하면 브라우저·서버·사용자가 요청의 의도를 명확히 구분할 수 있다.

## 3. Form()이 하는 일

HTML `<form method="post">`가 폼 데이터를 전송한다. `app/routers/memos.py`의 `title: str = Form(...)`, `content: str = Form(...)`가 그 값을 함수 인자로 받는다. 그래서 `python-multipart`가 의존성에 포함된다.

## 4. PRG(Post-Redirect-Get)

등록/수정/삭제 POST 요청이 성공하면 HTML을 바로 반환하지 않고 `RedirectResponse(..., status_code=303)`을 반환한다. 브라우저는 `Location`으로 새 GET 요청을 보낸다.

```text
POST /memos
  → DB 저장
  → 303 Location: /memos/1
  → GET /memos/1
```

이 구조에서는 사용자가 결과 페이지에서 F5를 눌러도 마지막 요청은 GET이므로 같은 POST가 다시 제출되는 문제를 줄일 수 있다.

## 5. SQLAlchemy ORM과 SQL

`Memo` 클래스는 `memos` 테이블을 객체로 표현한다.

- `db.add(memo)` → 새 ORM 객체를 Session의 작업 대상으로 등록한다.
- `db.commit()` → 트랜잭션을 커밋하며 INSERT/UPDATE/DELETE가 DB에 반영된다.
- `db.get(Memo, id)` → 기본키 기준 단건 SELECT에 대응한다.
- `select(Memo)` + `db.scalars(...)` → 현재 코드의 목록 SELECT 방식이다.
- `Session.query(...)` → SQLAlchemy의 전통적인 ORM 조회 API로, 개념적으로 SELECT 조회에 대응한다. 현재 구현은 SQLAlchemy 2.x 스타일의 `select()`를 사용한다.
- `db.delete(memo)` + `commit()` → DELETE에 대응한다.

Session은 DB 작업 단위를 관리하는 객체다.

## 6. Depends로 Session을 주입하는 이유

`get_db()`는 요청마다 Session을 열고, 라우터 처리가 끝나면 `finally`에서 닫는다. 라우터는 `db: Session = Depends(get_db)`로 Session을 받는다. 이렇게 하면 세션 생성/종료 코드가 각 라우트에 반복되지 않는다.

## 7. SQLite를 PostgreSQL로 바꾼다면

핵심 변경 지점은 `app/database.py`의 연결 URL과 DB 드라이버 설정이다. 현재 모델/서비스/저장소가 SQLAlchemy 추상화를 사용하므로 비즈니스 규칙과 대부분의 CRUD 코드는 유지할 수 있다. 단, 실제 PostgreSQL을 쓰려면 그 DB용 드라이버 패키지가 필요하므로 현재 B5-2의 "외부 라이브러리 추가 금지" 제약 안에서는 구현하지 않는다.

## 8. 모델 관계가 필요해진다면

현재 미션은 단일 모델만 요구하고 관계 구현을 제외한다. 다음 단계에서 카테고리를 추가한다면 `models/`에 새 모델과 FK/relationship을 추가하고, repository/service에서 관계 조회 및 규칙을 확장하며, template에서 관계 데이터를 표시하게 된다.

## 9. REST API + 별도 프론트엔드로 바꾼다면

유지 가능한 부분:
- `models/`
- `repositories/`
- 대부분의 `services/`

크게 바뀌는 부분:
- `routers/`가 Jinja2 `TemplateResponse` 대신 JSON 응답을 반환
- `templates/`는 제거되고 별도 프론트엔드가 API를 호출

레이어 분리를 해두면 UI 방식이 바뀌어도 DB/비즈니스 계층 전체를 다시 작성할 필요가 줄어든다.

## 10. 직접 설명 연습 질문

1. 등록 버튼을 누른 뒤 브라우저 → 라우터 → 서비스 → 저장소 → DB → 상세 화면까지 어떤 순서로 움직이는가?
2. 등록 직후 200 HTML이 아니라 303을 반환하는 이유는 무엇인가?
3. `Session.add`, `commit`, `query/select`, `delete`가 각각 어떤 SQL 동작과 연결되는가?
4. `Depends(get_db)`를 모든 라우트에 직접 `SessionLocal()`을 쓰는 방식과 비교하면 무엇이 좋은가?
5. 라우터에 SQL과 검증 코드를 모두 넣으면 테스트와 유지보수가 왜 어려워지는가?
