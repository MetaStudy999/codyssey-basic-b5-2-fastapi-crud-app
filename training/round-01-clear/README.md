# B5-2 Round 01 — CLEAR

구분: **선택 미션 (OPTIONAL)**  
현재 작업 모드: **Phase A — REFERENCE BUILD**  
Runtime Mission 상태: **⬜ NOT STARTED**

## 현재 판정

B5-2의 FastAPI CRUD **Reference 핵심 기준본은 준비 완료**했습니다. 실제 브라우저/DB Runtime과 Evidence는 Phase C에서 수행하므로 아직 `✅ CLEAR`가 아닙니다.

## 핵심 문서

- `REFERENCE-BUILD.md`: 기준 구현 설계와 범위
- `REFERENCE-STATUS.md`: Phase A / Phase C 구분
- `BEGINNER-GUIDE.md`: 입문자 처음부터 끝까지 학습 경로
- `CHECKLIST.md`: 공식 Mission/Evaluation CLEAR Gate
- `docs/requirements-mapping.md`: 요구사항→구현→검증→증빙
- `docs/evaluation-qa.md`: 평가 예상 Q&A
- `evidence/README.md`: 실제 Evidence 수집 기준

## 기준 구현

`reference/` 아래에 Memo 단일 도메인 FastAPI/Jinja2/SQLAlchemy/SQLite CRUD 앱을 구성했습니다.

## 환경/검증

`environment/` 아래에 `setup.sh`, `verify.sh`, `reset.sh`, `inspect_db.py`가 있습니다.

Reference 파일이 존재한다는 이유만으로 Runtime PASS를 표시하지 않습니다.
