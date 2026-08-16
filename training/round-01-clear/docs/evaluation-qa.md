# B5-2 Evaluation Q&A

평가 답변은 Reference 코드 구조를 근거로 설명하는 연습용입니다. Phase C에서는 실제 실행 결과를 함께 제시합니다.

## 1. 라우터 / 서비스 / 저장소를 왜 나누었나요?

- **라우터**: URL, HTTP 메서드, `Form()`, `Depends()`, `TemplateResponse`, Redirect처럼 웹 요청/응답을 다룹니다.
- **서비스**: 제목/내용 검증처럼 도메인 규칙을 다룹니다.
- **저장소**: SQLAlchemy `Session`으로 조회·추가·수정·삭제하는 DB 접근을 다룹니다.

이렇게 나누면 요청 방식이 바뀌거나 DB가 바뀌어도 한 레이어의 변경이 다른 레이어로 과도하게 번지는 것을 줄일 수 있습니다.

## 2. 브라우저 요청 흐름은 어떻게 되나요?

`브라우저 → Router → Service → Repository → SQLite` 순으로 저장/조회하고, 조회된 결과는 다시 `Repository → Service → Router → Jinja2 Template → 브라우저`로 전달됩니다.

## 3. GET과 POST는 왜 나눕니까?

GET은 화면이나 데이터를 조회하는 요청에 사용하고, POST는 등록·수정·삭제처럼 서버 상태를 변경하는 요청에 사용했습니다. 이 구분 덕분에 URL/메서드만 보아도 요청 의도를 이해하기 쉬워집니다.

## 4. PRG(Post-Redirect-Get)는 왜 적용합니까?

POST 처리 직후 HTML을 직접 렌더링하면 사용자가 새로고침할 때 브라우저가 같은 POST를 다시 전송할 수 있습니다. Reference는 성공 후 `RedirectResponse(status_code=303)`로 GET 화면에 이동시켜, 새로고침이 등록·수정·삭제를 반복하지 않도록 합니다.

## 5. 왜 303인가요?

POST 처리 결과 이후 브라우저가 리다이렉트 대상에 GET을 수행하도록 의도를 명확히 하기 위해 사용합니다. Reference의 등록/수정/삭제 성공 경로가 모두 303 Redirect입니다.

## 6. `Form()`은 무슨 역할인가요?

HTML `<form>`이 전송한 `application/x-www-form-urlencoded` 또는 multipart 형식의 필드 값을 FastAPI 함수 파라미터 `title`, `content`로 받도록 합니다. `python-multipart`가 필요한 이유도 폼 데이터 처리와 관련됩니다.

## 7. `Depends(get_db)`는 왜 사용하나요?

요청마다 SQLAlchemy `Session`을 하나 제공하고, 요청이 끝나면 `finally`에서 닫도록 DB 세션 생명주기를 중앙화합니다. 라우터마다 직접 세션을 만들고 닫는 중복을 줄입니다.

## 8. `Session.add`, `commit`, `query`는 어떤 SQL 동작과 연결되나요?

- `add()`는 새 ORM 객체를 세션의 작업 대상으로 등록합니다.
- `commit()`은 트랜잭션을 확정하며 필요한 INSERT/UPDATE/DELETE를 DB에 반영합니다.
- `query()`는 SELECT를 구성해 데이터를 조회하는 데 사용합니다.

Reference의 실제 SQLAlchemy 동작은 Phase C에서 DB 파일 전후를 확인하며 설명합니다.

## 9. 왜 ORM 모델 필드를 이렇게 구성했나요?

`id`는 각 메모를 구분하는 PK, `title`과 `content`는 실제 도메인 데이터, `created_at`/`updated_at`은 생성·수정 시점을 확인하기 위한 필드입니다. 단일 모델의 3~6개 권장 범위에 맞춘 단순한 구조입니다.

## 10. 라우터에 모든 로직을 넣으면 어떤 문제가 생기나요?

HTTP 처리, 검증, SQL 코드가 한 함수에 섞여 함수가 길어지고 수정 영향 범위를 파악하기 어려워집니다. 테스트와 재사용도 어려워집니다. Reference는 역할을 분리해 이 문제를 피합니다.

## 11. SQLite를 PostgreSQL로 바꾸면 어디가 바뀌나요?

주로 `database.py`의 DB URL/engine 설정과 해당 DB 드라이버 의존성이 바뀝니다. 서비스의 비즈니스 규칙과 대부분의 라우터는 유지할 수 있습니다. 실제 외부 DB 전환은 B5-2 필수 범위가 아닙니다.

## 12. 모델 간 관계가 필요해지면 어떻게 합니까?

현재 미션은 관계 구현을 금지합니다. 이후 확장한다면 모델에 FK/`relationship`을 추가하고, Repository 조회/저장과 Service 규칙, 화면 표시를 함께 변경합니다. 이 작업은 다음 미션 범위로 남깁니다.

## 13. REST API + 별도 Frontend로 바꾸면 무엇이 유지되나요?

Jinja2 `TemplateResponse`와 HTML 폼 중심 Router는 JSON 요청/응답 Router로 크게 바뀝니다. 반면 Service의 비즈니스 규칙, Repository의 DB 접근, ORM Model은 상당 부분 유지할 수 있습니다.

## 14. 존재하지 않는 ID는 어떻게 처리하나요?

Service/Repository 조회 결과가 `None`이면 Router가 `not_found.html`을 HTTP 404로 렌더링합니다. 평가의 '안내 화면 또는 목록 이동' 요구 중 안내 화면 방식을 선택했습니다.
