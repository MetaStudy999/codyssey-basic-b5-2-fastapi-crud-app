# Codyssey Basic B5-2

## 구분
- 선택 미션 (OPTIONAL)
- 현재 훈련 체계: Round 01 — CLEAR
- 현재 작업 모드: Phase A — REFERENCE BUILD

## 시작 위치
`training/round-01-clear/BEGINNER-GUIDE.md`부터 진행합니다.

## 공식 원본
- `b5-2-mission.pdf`
- `b5-2-mission.md`
- `b5-2-evaluation.md`

공식 원본은 수정하지 않습니다. 훈련 결과는 `training/` 아래에서 차수별로 독립 관리합니다.

## Round 01 Reference Build

현재 `training/round-01-clear/reference/`에 Memo 단일 도메인의 FastAPI/Jinja2/SQLAlchemy/SQLite CRUD 기준본을 준비했습니다.

주요 준비물:
- 홈/목록/상세/등록/수정/삭제 SSR 흐름
- `303` PRG
- Router / Service / Repository / Model 분리
- `Depends(get_db)` DB Session 주입
- SQLite 직접 확인 도구
- Reference verify/setup/reset
- Requirements Mapping / Evaluation Q&A / Evidence Guide
- Beginner Guide / Checklist

## 상태

**Reference 핵심 기준본 준비 완료 / Runtime 미시작 / `✅ CLEAR` 아님**

실제 localhost:8000, CRUD, 303 Redirect, SQLite 데이터, Not Found, Evidence는 Phase C에서 사용자 환경에서 검증합니다.
