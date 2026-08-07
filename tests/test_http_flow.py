import http.client
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
HOST = "127.0.0.1"
PORT = 8000


class HttpFlowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.db_path = Path(cls.temp_dir.name) / "http-flow.db"
        cls.env = os.environ.copy()
        cls.env["DATABASE_URL"] = f"sqlite:///{cls.db_path}"
        cls.process = cls._start_server()
        cls._wait_for_server()

    @classmethod
    def tearDownClass(cls):
        cls._stop_server()
        cls.temp_dir.cleanup()

    @classmethod
    def _start_server(cls):
        return subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "app.main:app", "--host", HOST, "--port", str(PORT)],
            cwd=ROOT,
            env=cls.env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            text=True,
        )

    @classmethod
    def _stop_server(cls):
        if getattr(cls, "process", None) and cls.process.poll() is None:
            cls.process.terminate()
            try:
                cls.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                cls.process.kill()
                cls.process.wait(timeout=5)

    @classmethod
    def _wait_for_server(cls):
        deadline = time.time() + 10
        last_error = None
        while time.time() < deadline:
            try:
                status, _, _ = cls.request("GET", "/")
                if status == 200:
                    return
            except OSError as exc:
                last_error = exc
            time.sleep(0.1)
        raise RuntimeError(f"server did not start: {last_error}")

    @staticmethod
    def request(method: str, path: str, data: dict[str, str] | None = None):
        body = None
        headers = {}
        if data is not None:
            body = urlencode(data)
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            headers["Content-Length"] = str(len(body.encode("utf-8")))
        connection = http.client.HTTPConnection(HOST, PORT, timeout=5)
        try:
            connection.request(method, path, body=body, headers=headers)
            response = connection.getresponse()
            response_body = response.read().decode("utf-8")
            normalized_headers = {key.lower(): value for key, value in response.getheaders()}
            return response.status, normalized_headers, response_body
        finally:
            connection.close()

    def test_complete_prg_crud_and_restart_persistence(self):
        status, _, home = self.request("GET", "/")
        self.assertEqual(200, status)
        self.assertIn("메모 목록 보기", home)
        self.assertIn("새 메모 작성", home)

        status, _, _ = self.request("GET", "/memos")
        self.assertEqual(200, status)

        status, headers, _ = self.request(
            "POST", "/memos", {"title": "HTTP 메모", "content": "처음 내용"}
        )
        self.assertEqual(303, status)
        self.assertEqual("/memos/1", headers.get("location"))

        status, _, detail = self.request("GET", "/memos/1")
        self.assertEqual(200, status)
        self.assertIn("HTTP 메모", detail)
        self.assertIn("처음 내용", detail)

        status, _, form = self.request("GET", "/memos/1/edit")
        self.assertEqual(200, status)
        self.assertIn("메모 수정", form)

        status, headers, _ = self.request(
            "POST", "/memos/1/edit", {"title": "수정된 메모", "content": "수정 내용"}
        )
        self.assertEqual(303, status)
        self.assertEqual("/memos/1", headers.get("location"))

        with sqlite3.connect(self.db_path) as connection:
            row = connection.execute("SELECT title, content FROM memos WHERE id = 1").fetchone()
        self.assertEqual(("수정된 메모", "수정 내용"), row)

        self._stop_server()
        self.__class__.process = self._start_server()
        self._wait_for_server()

        status, _, detail_after_restart = self.request("GET", "/memos/1")
        self.assertEqual(200, status)
        self.assertIn("수정된 메모", detail_after_restart)

        status, headers, _ = self.request("POST", "/memos/1/delete", {})
        self.assertEqual(303, status)
        self.assertEqual("/memos", headers.get("location"))

        status, _, missing = self.request("GET", "/memos/1")
        self.assertEqual(404, status)
        self.assertIn("해당 데이터를 찾을 수 없습니다", missing)

    def test_blank_form_is_rejected(self):
        status, _, body = self.request("POST", "/memos", {"title": " ", "content": "내용"})
        self.assertEqual(400, status)
        self.assertIn("제목과 내용은 비워 둘 수 없습니다", body)


if __name__ == "__main__":
    unittest.main()
