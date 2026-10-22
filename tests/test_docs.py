"""The documentation check should catch regressions in published user entry points."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parent.parent / "scripts" / "check_docs.py"
SPEC = importlib.util.spec_from_file_location("r2r_check_docs", SOURCE)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class DocCheckTests(unittest.TestCase):
    def fixture(self, root: Path):
        (root / "quickstart").mkdir()
        (root / "skills/r2r").mkdir(parents=True)
        (root / "R2R.md").write_text("# Program\n", encoding="utf-8")
        (root / "CHANGELOG.md").write_text("# History\n\n## v0.1.0 — Initial\n", encoding="utf-8")
        (root / "LICENSE").write_text("MIT\n", encoding="utf-8")
        (root / "skills/r2r/LICENSE").write_text("MIT\n", encoding="utf-8")
        link = "https://github.com/kingwangking/r2r/releases/tag/v0.1.0"
        (root / "README.md").write_text(f"R2R v0.1.0 [Release]({link}) [Use](quickstart/use.md)\n", encoding="utf-8")
        (root / "quickstart/install.md").write_text(f"Install v0.1.0 [Release]({link})\n", encoding="utf-8")
        (root / "quickstart/use.md").write_text(f"Use v0.1.0 [Release]({link})\n", encoding="utf-8")

    def test_current_release_fixture_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            self.assertEqual(mod.check(root), [])

    def test_stale_unreleased_claim_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            f = root / "quickstart/use.md"
            f.write_text(f.read_text(encoding="utf-8") + "\nThe PR is still in an unmerged Draft.\n", encoding="utf-8")
            self.assertTrue(any("stale pre-release" in x for x in mod.check(root)))

    def test_secondary_entry_staleness_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            (root / "skills/README.md").write_text(
                "This package is still in an unmerged Draft PR.\n", encoding="utf-8"
            )
            self.assertTrue(any("skills/README.md" in x and "stale" in x for x in mod.check(root)))

    def test_version_mismatch_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            f = root / "README.md"
            f.write_text("Only v0.0.1 is available.\n", encoding="utf-8")
            self.assertTrue(any("does not name" in x for x in mod.check(root)))

    def test_broken_relative_link_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            f = root / "README.md"
            f.write_text(f.read_text(encoding="utf-8") + "[Broken](missing.md)\n", encoding="utf-8")
            self.assertTrue(any("missing local link" in x for x in mod.check(root)))

    def test_license_divergence_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(root)
            (root / "skills/r2r/LICENSE").write_text("not the same\n", encoding="utf-8")
            self.assertTrue(any("copies differ" in x for x in mod.check(root)))


if __name__ == "__main__":
    unittest.main()
