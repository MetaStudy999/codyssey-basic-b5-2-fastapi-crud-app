# B5-2 Round 01 — Mission Clear Checklist

현재 모드: **Phase A — REFERENCE BUILD**  
Mission Runtime 상태: **⬜ NOT STARTED**

> Reference 구현이나 문서가 존재해도 실제 브라우저/DB 실행과 Evidence가 끝나기 전에는 `✅ CLEAR`로 판정하지 않습니다.

## A. Source

- [x] 공식 `b5-2-mission.pdf` 존재 확인
- [x] 공식 `b5-2-mission.md` 분석
- [x] 공식 `b5-2-evaluation.md` 분석
- [x] 필수/보너스/제약사항 분리
- [x] 단일 도메인 `Memo` Reference 선택

## B. Reference Build

- [x] `REFERENCE-BUILD.md`
- [x] `reference/README.md`
- [x] `reference/requirements.txt`
- [x] `routers/` 분리
- [x] `services/` 분리
- [x] `repositories/` 분리
- [x] `models/` 분리
- [x] `templates/` 분리
- [x] `database.py`
- [x] `environment/setup.sh`
- [x] `environment/verify.sh`
- [x] `environment/reset.sh`
- [x] `environment/inspect_db.py`
- [x] `docs/requirements-mapping.md`
- [x] `docs/evaluation-qa.md`
- [x] `evidence/README.md`
- [x] 상세 `BEGINNER-GUIDE.md`

## C. 공식 기능 요구 — Reference 구현

- [x] `GET /` 홈 Router
- [x] 홈 목적 설명 1~2줄
- [x] 홈 기능 링크 2개 이상
- [x] Jinja2 SSR `TemplateResponse`
- [x] Memo 단일 SQLAlchemy 모델
- [x] 목록 조회
- [x] 단건 상세 조회
- [x] 등록 폼
- [x] 등록 POST + `Form()`
- [x] 수정 폼
- [x] 수정 POST + `Form()`
- [x] 삭제 POST
- [x] 등록 후 `303` Redirect
- [x] 수정 후 `303` Redirect
- [x] 삭제 후 `303` Redirect
- [x] 상세 전체 필드 표시
- [x] 상세 수정/삭제/목록 이동
- [x] 존재하지 않는 ID 404 안내 화면
- [x] SQLite URL 설정
- [x] SQLAlchemy Session 생성
- [x] `Depends(get_db)` 세션 주입
- [x] Repository `query/add/commit/delete`
- [x] DB 파일 생성 코드 경로 준비
- [x] requirements에 공식 허용 5종만 명시
- [x] 인증/인가 미구현 유지
- [x] 모델 간 관계 미구현 유지

## D. 최소 검증 설계

- [x] Reference 파일 존재 검사
- [x] `compileall` Python syntax 검사 준비
- [x] PRG `303` 정적 검사 준비
- [x] `Form()` 정적 검사 준비
- [x] `Depends(get_db)` 정적 검사 준비
- [x] SQLite 설정 정적 검사 준비
- [x] Repository CRUD 정적 검사 준비
- [ ] `bash environment/verify.sh` 실제 실행 결과 확인

## E. Runtime — Phase C에서만 체크

- [ ] Python 3.10+ 실제 확인
- [ ] 가상환경 생성
- [ ] 패키지 설치 성공
- [ ] `uvicorn app.main:app --reload` 정상 기동
- [ ] `http://localhost:8000` 홈 정상
- [ ] 목록 실제 동작
- [ ] 상세 실제 동작
- [ ] 등록 실제 동작
- [ ] 수정 실제 동작
- [ ] 삭제 실제 동작
- [ ] 등록/수정/삭제 `303` 실제 확인
- [ ] 새로고침 시 중복 요청 없음
- [ ] 없는 ID 안내 실제 확인
- [ ] `reference/database.db` 실제 생성
- [ ] DB 내부 데이터 직접 확인
- [ ] README 절차만으로 재실행

## F. Evaluation 설명

- [x] Router/Service/Repository 역할 Reference 답변 준비
- [x] 라우터와 서비스 분리 기준 답변 준비
- [x] ORM 모델 필드 설계 이유 준비
- [x] `Session.add/commit/query` 의미 준비
- [x] 요청 흐름 설명 준비
- [x] GET/POST 차이 설명 준비
- [x] PRG/303 이유 설명 준비
- [x] Form 처리 설명 준비
- [x] 레이어 미분리 문제점 설명 준비
- [x] PostgreSQL 전환 시 변경점 설명 준비
- [x] 연관관계 확장 시 변경점 설명 준비
- [x] REST + Frontend 분리 시 유지/변경 레이어 설명 준비
- [ ] 사용자가 실제 코드/결과를 근거로 자기 말로 설명

## G. Evidence

- [x] Evidence 수집 계획 준비
- [ ] Python 버전 Evidence
- [ ] 서버 기동 Evidence
- [ ] 홈 Evidence
- [ ] CRUD Evidence
- [ ] PRG Evidence
- [ ] Not Found Evidence
- [ ] SQLite 파일/데이터 Evidence
- [ ] 구조 Evidence
- [ ] README 재현 Evidence
- [ ] Secret/credential 노출 없음 최종 확인

## H. CLEAR Gate

- [x] Source 분석
- [x] 최소 충분 Reference 구현 준비
- [x] 요구사항 매핑 준비
- [x] 평가 Q&A 준비
- [x] 입문자 가이드 준비
- [x] 검증 도구 준비
- [ ] Reference verify 실제 실행
- [ ] 실제 Runtime 검증
- [ ] Evidence 확보
- [ ] 평가 설명 확인
- [ ] BLOCKER 0 / MAJOR 0 최종 감사
- [ ] **✅ B5-2 CLEAR**
