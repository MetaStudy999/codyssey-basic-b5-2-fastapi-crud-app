# G5 Runtime Notes

## Executed runtime

A real Uvicorn process was started on `127.0.0.1:8000` with the implemented FastAPI application. The runtime flow exercised actual HTTP requests and an actual SQLite file, not mocked responses.

Verified at runtime:

- server startup completed successfully
- `GET /` returned 200 and rendered the home content/links
- `GET /memos/new` rendered the create form
- `POST /memos` created a row and returned 303
- `GET /memos` rendered the created memo
- `GET /memos/1` rendered detail data
- `GET /memos/1/edit` rendered the edit form
- update POST returned 303
- missing ID returned a guidance page with 404
- blank required value was rejected with a visible validation message
- the Uvicorn process was stopped and restarted
- the previously updated memo was still available after restart
- SQLite was queried directly with `sqlite3` from Python and contained the expected row

See:

- `server-log.txt`
- `http-flow.txt`
- `db-verification.txt`
- `test-results.txt`
- `runtime-environment.txt`

## Human browser runtime

`NOT_REQUIRED` for the current acceptance gate. The Mission makes major-screen screenshots optional, and the required server/CRUD/PRG/SQLite behavior has executable HTTP/runtime evidence. A human browser smoke check can still be performed as optional presentation evidence, but it does not block B5-2 completion.
