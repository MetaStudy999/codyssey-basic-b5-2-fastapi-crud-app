import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StructureTest(unittest.TestCase):
    def test_required_directories_and_templates_exist(self):
        required = [
            "app/routers",
            "app/services",
            "app/repositories",
            "app/models",
            "app/templates",
        ]
        for relative in required:
            self.assertTrue((ROOT / relative).is_dir(), relative)

    def test_only_allowed_dependencies_are_declared(self):
        declared = {
            line.strip().lower()
            for line in (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
        allowed = {"fastapi", "uvicorn", "sqlalchemy", "jinja2", "python-multipart"}
        self.assertEqual(allowed, declared)

    def test_router_uses_depends_form_and_303(self):
        source = (ROOT / "app/routers/memos.py").read_text(encoding="utf-8")
        self.assertIn("Depends(get_db)", source)
        self.assertIn("Form(...)", source)
        self.assertIn("status_code=303", source)


if __name__ == "__main__":
    unittest.main()
