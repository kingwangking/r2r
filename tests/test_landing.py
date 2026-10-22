"""Source-only negative tests for standalone R2R HTML checker."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("r2r_landing", ROOT / "scripts/check_landing.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class LandingTests(unittest.TestCase):
    def test_actual_landing_structure(self):
        self.assertEqual(mod.check(ROOT / "docs/product/landing.html"), [])

    def test_missing_anchor_is_detected(self):
        src = (ROOT / "docs/product/landing.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.html"
            p.write_text(src.replace('href="#demo"', 'href="#missing-page-section"'), encoding="utf-8")
            self.assertTrue(any("missing anchor target" in s for s in mod.check(p, syntax_check=False)))

    def test_invisible_by_default_sections_are_rejected(self):
        src = (ROOT / "docs/product/landing.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "invisible.html"
            p.write_text(src.replace(
                ".reveal { opacity: 1; transform: none;",
                ".reveal { opacity: 0; transform: none;"
            ), encoding="utf-8")
            self.assertTrue(any("remain readable" in s for s in mod.check(p, syntax_check=False)))

    def test_external_script_is_detected(self):
        src = (ROOT / "docs/product/landing.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "remote.html"
            p.write_text(src.replace("</head>", '<script src="https://cdn.example.invalid/x.js"></script></head>'),
                         encoding="utf-8")
            self.assertTrue(any("external" in s for s in mod.check(p, syntax_check=False)))


if __name__ == "__main__":
    unittest.main()
