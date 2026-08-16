# B5-2 Runtime Evidence Guide

이 디렉터리는 **Phase C 실제 실행 결과**만 기록합니다. 예상 출력이나 Reference 문서 존재만으로 PASS 처리하지 않습니다.

## 필수 Evidence 세트

1. `python --version` — Python 3.10 이상 확인
2. 패키지 설치/서버 기동 — `uvicorn app.main:app --reload` 정상 로그
3. 홈 — `http://localhost:8000` 목적 문구와 목록/등록 링크
4. 등록 — 폼 입력 후 상세 화면으로 이동
5. 목록 — 등록 데이터 노출
6. 상세 — 전체 필드 + 수정/삭제/목록 이동
7. 수정 — 수정 후 상세 결과 확인
8. 삭제 — 삭제 후 목록으로 이동, 데이터 제거 확인
9. PRG — 등록/수정/삭제 POST가 `303`, 새로고침 시 중복 동작 없음
10. Not Found — 존재하지 않는 ID에서 적절한 404 안내
11. SQLite — `reference/database.db` 생성
12. DB 직접 확인 — `python ../environment/inspect_db.py` 출력 또는 DB Browser 화면
13. 구조 — `routers/services/repositories/models/templates` 분리 확인
14. README 절차 — 문서만 보고 재실행 가능함을 확인

## Evidence 이름 권장

```text
01-python-version.txt
02-server-start.txt
03-home.png
04-create.png
05-list.png
06-detail.png
07-update.png
08-delete.png
09-prg.txt
10-not-found.png
11-db-file.txt
12-db-inspection.txt
13-project-tree.txt
14-runtime-notes.md
```

스크린샷 이름은 실제 상황에 맞게 달라도 됩니다.

## 금지

- Password / Token / API Key / Private Key를 Evidence에 저장하지 않습니다.
- 실제로 실행하지 않은 결과를 만들어 넣지 않습니다.
- Reference 예상 결과를 실제 출력처럼 기록하지 않습니다.
