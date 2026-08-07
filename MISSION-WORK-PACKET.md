# B5-2 Mission Work Packet

## 1. Identity

- Mission: `B5-2`
- Title: 글을 쓰고·보고·고치고·지울 수 있는 게시판형 웹 서비스 만들기
- Repository: `MetaStudy999/codyssey-basic-b5-2-fastapi-crud-app`
- Work branch: `mission/b5-2`
- Control Tower: `MetaStudy999/codyssey-basic` (READ ONLY)
- Control Tower frozen baseline: `0d1581b3e82366988f57e1d76da311c028b8e15e`
- Mission repository baseline: `12e1630c0391e86c912df8a74c9e5afe59c15273`

## 2. Source Inventory

| Source | Path | State | Notes |
|---|---|---|---|
| Mission PDF | `b5-2-mission.pdf` | VALID | 6 rendered pages; substantive mission, requirements, constraints and examples |
| Mission Markdown | `b5-2-mission.md` | DUPLICATE / VALID | Markdown transcription of the Mission PDF; no implementation-changing conflict found |
| Evaluation Markdown | `b5-2-evaluation.md` | VALID | Four evaluation sections with functional, architecture and explanation criteria |
| Evaluation PDF | none found | MISSING | No evaluation PDF is present in the repository baseline |
| Official operations | Control Tower frozen Governance | VALID | Read-only execution rules and Source protocol |

- Source Mode: `FULL SOURCE`
- Source Confidence: `HIGH`
- Source Gaps: Evaluation PDF is absent, but the official Evaluation Markdown is substantive and sufficient for evaluation mapping.
- Source Conflicts: none found.

## 3. Dependency / Drift Check

- B5-1 relationship: `RECOMMENDED` conceptually, not an official build prerequisite.
- B5-2 Mission does not require reuse of B5-1 artifacts.
- B5-2 explicitly limits scope to one model and excludes model relationships, authentication and authorization.
- Control Tower drift affecting this workcell: none identified at start; frozen Governance remains the execution basis.

## 4. Repository Baseline Inventory

At `12e1630c0391e86c912df8a74c9e5afe59c15273` the repository contains only:

- `README.md`
- `b5-2-mission.pdf`
- `b5-2-mission.md`
- `b5-2-evaluation.md`

No FastAPI entry point, `routers/`, `services/`, `repositories/`, `models/`, `templates/`, SQLite database, dependency file or tests exist. Therefore all application implementation items start as `TODO`.

## 5. Mission Contract

The minimum sufficient implementation will use one `Memo` domain model with four fields (`id`, `title`, `content`, `created_at`) and will provide:

1. Python 3.10+ compatible FastAPI app on `http://localhost:8000`.
2. Dependencies limited to `fastapi`, `uvicorn`, `sqlalchemy`, `jinja2`, `python-multipart`.
3. `routers/`, `services/`, `repositories/`, `models/`, `templates/` role separation.
4. Jinja2 SSR via `TemplateResponse` for all main screens.
5. Home page with purpose text and at least two links.
6. Memo list/detail/create/edit/delete flow.
7. HTML `Form()` handling for create/update and POST for create/update/delete.
8. `RedirectResponse(status_code=303)` after create/update/delete (PRG).
9. Not-found guidance for missing memo IDs.
10. SQLite + SQLAlchemy ORM persistence, `Session`, and FastAPI `Depends` session injection.
11. Direct DB verification script.
12. README with venv, install and server run steps.

### Non-scope

- Authentication / authorization / login
- Multi-model relationships
- External libraries beyond the five allowed packages
- Cloud deployment

### Optional but low-cost enhancement

- Server-side required-field validation for title/content with an inline error message. This is a Mission bonus and must not alter the core scope.

## 6. Requirement Traceability

| ID | Requirement | Source | Acceptance / Evidence |
|---|---|---|---|
| REQ-B5-2-001 | Server runs on localhost:8000 | Mission §4.1, Eval item 1 | boot log + HTTP 200 `/` |
| REQ-B5-2-002 | Allowed dependencies only | Mission §4.1, §7 | `requirements.txt` |
| REQ-B5-2-003 | Layer directories separated | Mission §4.2, §4.8, Eval item 2 | tree + import/responsibility inspection |
| REQ-B5-2-004 | Jinja2 SSR main screens | Mission §4.3 | route/template inspection + HTTP pages |
| REQ-B5-2-005 | Home purpose + 2 links | Mission §4.4 | HTTP body check |
| REQ-B5-2-006 | Single-model CRUD | Mission §4.5, Eval item 1 | HTTP CRUD flow + DB query |
| REQ-B5-2-007 | Form + POST + Form() | Mission §4.6 | route inspection + HTTP form submission |
| REQ-B5-2-008 | PRG with 303 | Mission §4.7, Eval items 1/3 | POST response headers/status |
| REQ-B5-2-009 | Not-found UX | Mission §4.5, Eval item 1 | missing ID HTTP page |
| REQ-B5-2-010 | SQLite + ORM Session + Depends | Mission §4.9, Eval items 1/2/3 | DB file + code inspection + persistence test |
| REQ-B5-2-011 | README run procedure | Mission §4.10, Eval item 1 | README inspection |
| REQ-B5-2-012 | Learner can explain request/CRUD/design decisions | Mission §3, Eval items 2-4 | `docs/LEARNING.md` aligned with implementation |

## 7. Evaluation Mapping

- Item 1 — Functional execution: automated HTTP/DB integration checks plus human browser runtime where useful.
- Item 2 — Structure/ORM understanding: static responsibility checks and learning notes tied to exact code.
- Item 3 — Request flow/CRUD principles: learning notes + route/service/repository/model trace.
- Item 4 — Extension/design judgement: learning notes only; no out-of-scope implementation will be added.

## 8. Mission-specific TOC

```text
B5-2
├── Source / Evaluation Discovery
├── Environment / Dependencies
├── FastAPI Entry Point
├── Layered Structure
│   ├── Router
│   ├── Service
│   ├── Repository
│   └── Model
├── SQLite / SQLAlchemy / Depends
├── Jinja2 SSR
├── Home
├── CRUD
│   ├── List
│   ├── Detail
│   ├── Create
│   ├── Update
│   └── Delete
├── Form Validation
├── PRG / 303 Redirect
├── Not Found UX
├── DB Verification
├── Automated Tests
├── Runtime / Evidence
├── Learning
└── Handoff
```

## 9. Agent Routing

- ChatGPT: orchestrator, source fusion, primary implementation, test design, review.
- Independent agent: use only after the baseline implementation/tests are complete, focused on BLOCKER/MAJOR, missing requirements, false PASS, secret exposure.
- Human: browser acceptance only if needed after automated HTTP checks.

## 10. Test Plan

1. Python compile/import smoke check.
2. Repository/service CRUD with temporary SQLite database.
3. Start Uvicorn on port 8000 and use Python standard-library HTTP client to verify:
   - `GET /`
   - `GET /memos`
   - create form and POST create → 303
   - detail
   - edit form and POST update → 303
   - POST delete → 303
   - missing ID guidance
4. Query SQLite directly and compare stored values.
5. Restart server and confirm data persists.
6. Check dependencies and layer boundaries.

No additional test-only external package is required.

## 11. Runtime Plan

Automated HTTP runtime will be performed first. Human browser confirmation, if requested, will be limited to opening the home/list/detail/create/edit screens and confirming the visible flow.

## 12. Evidence Plan

- `evidence/test-results.txt`
- `evidence/http-flow.txt`
- `evidence/db-verification.txt`
- `evidence/runtime-notes.md`
- optional human screenshots under `evidence/screenshots/`

Only actual executed results may be marked PASS.

## 13. G1-G8 Checklist

- [x] G1 SOURCE — source candidates, states, mode, confidence, gaps, dependency and repository baseline determined
- [ ] G2 BUILD — minimum sufficient implementation complete
- [ ] G3 TEST — automated tests complete
- [ ] G4 REVIEW — BLOCKER=0 / MAJOR=0
- [ ] G5 RUNTIME — runtime verification complete or explicit NEEDS-RUNTIME
- [ ] G6 EVIDENCE — required evidence stored
- [ ] G7 LEARN — implementation-aligned beginner learning material complete
- [ ] G8 MERGE — PR merged and handoff/result recorded

## 14. STOP Rule

Stop when confirmed Mission/Evaluation requirements are satisfied, required tests/evidence are complete, BLOCKER=0 and MAJOR=0. Optional refactoring, extra frameworks, authentication, relationships, deployment and other enhancements remain backlog.

## 15. Handoff Contract

Final repository must include `HANDOFF.md` and `mission-result.yaml` with source mode/confidence/gaps, G1-G8 results, final commit/PR/merge status, tests, runtime, evidence, BLOCKER/MAJOR counts and remaining backlog. The Control Tower repository remains untouched by this workcell.
