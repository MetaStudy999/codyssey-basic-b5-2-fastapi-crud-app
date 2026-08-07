# B5-2 Independent Review Contract

## Source of Truth

1. `b5-2-mission.pdf`
2. `b5-2-mission.md`
3. `b5-2-evaluation.md`
4. `MISSION-WORK-PACKET.md`
5. code/tests/evidence

Control Tower Governance is frozen at `0d1581b3e82366988f57e1d76da311c028b8e15e` and the Control Tower repository is READ ONLY.

## Review Scope

Report only:

- BLOCKER
- MAJOR
- clear Mission/Evaluation requirement omissions
- failing tests
- false PASS/evidence claims
- secret/credential exposure
- clear code/document contradictions that can cause evaluation failure

Do not redesign the application, add authentication/relationships/deployment, add libraries, perform broad refactors, or turn optional improvements into required work.

## Beginner Learning Preservation

`docs/LEARNING.md` must remain aligned with the actual implementation and should explain the current simple structure rather than introduce enterprise abstractions.

## Status Definitions

- TODO: not implemented/executed
- IMPLEMENTED: written but not executed
- TESTED: reliable test executed
- PASS: implementation + required verification/evidence complete
- NEEDS-RUNTIME: human/runtime verification still required
- BLOCKED: external dependency prevents progress

## Test Commands

```bash
python -m compileall app scripts tests
python -m unittest discover -s tests -v
```

## Exit Condition

Stop the independent review when `BLOCKER=0` and `MAJOR=0`. MINOR and improvement suggestions do not delay mission completion.
