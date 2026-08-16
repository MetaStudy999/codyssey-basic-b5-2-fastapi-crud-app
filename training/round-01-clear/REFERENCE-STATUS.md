# B5-2 R01 — Reference Status

## Phase A 준비 결과

- [x] Mission/Evaluation 분석
- [x] 단일 Memo 도메인 선정
- [x] FastAPI/Jinja2/SQLite/SQLAlchemy Reference 구조
- [x] routers/services/repositories/models 역할 분리
- [x] 홈/목록/상세/등록/수정/삭제 화면 흐름
- [x] HTML Form + FastAPI `Form()`
- [x] 등록/수정/삭제 `303` PRG 구현
- [x] `Depends(get_db)` 요청별 Session 주입
- [x] SQLAlchemy ORM CRUD Repository
- [x] 404 Not Found 안내 화면
- [x] 공식 허용 의존성 5종만 사용
- [x] 인증/인가 미구현 유지
- [x] 모델 간 관계 미구현 유지
- [x] 최소 서버사이드 필수값 검증
- [x] Reference 실행 가이드
- [x] offline `verify.sh` 준비
- [x] SQLite inspection helper
- [x] conservative reset helper
- [x] Requirement Mapping
- [x] Evaluation Q&A
- [x] Evidence Guide
- [x] Beginner Guide
- [x] 상세 Checklist
- [x] SQLite runtime 파일 Git ignore

## Phase C에서만 완료

- [ ] 실제 Python 3.10+ 확인
- [ ] 실제 가상환경/패키지 설치
- [ ] 실제 `verify.sh` 실행
- [ ] 실제 localhost:8000 서버 기동
- [ ] 홈 화면 브라우저 확인
- [ ] CRUD 전체 브라우저 흐름
- [ ] 실제 303 Redirect / F5 중복 방지
- [ ] 실제 `database.db` 생성
- [ ] 실제 DB 행 조회
- [ ] 실제 Not Found
- [ ] README 재현성 확인
- [ ] Runtime Evidence
- [ ] 사용자 자기 말 평가 설명
- [ ] BLOCKER/MAJOR 최종 Gate
- [ ] `✅ B5-2 CLEAR`

## 판정

**Reference 핵심 기준본 준비 완료 / Runtime 미시작 / CLEAR 아님**

Phase A 전체감사에서는 다른 미션과의 Python/DB/포트/의존성 정합성을 다시 확인합니다.
