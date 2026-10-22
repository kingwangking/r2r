"""Isolated tests of the portable Skill source/package checker (stdlib only)."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("skill_release", ROOT / "scripts" / "skill_release.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class SkillReleaseTests(unittest.TestCase):
    def make_skill(self, folder: Path):
        root = folder / "r2r"
        (root / "assets").mkdir(parents=True)
        (root / "references").mkdir()
        (root / "SKILL.md").write_text(
            "---\nname: r2r\ndescription: A test skill.\n---\n\n"
            "[asset](assets/R2R.md) [guide](references/operating-guide.md)\n",
            encoding="utf-8",
        )
        (root / "LICENSE").write_text("MIT\n", encoding="utf-8")
        (root / "assets/R2R.md").write_text("# Template\n", encoding="utf-8")
        (root / "references/operating-guide.md").write_text("# Guide\n", encoding="utf-8")
        return root

    def test_valid_source_and_deterministic_zip(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            root = self.make_skill(folder)
            paths, links = checker.check_skill(root)
            self.assertEqual(len(paths), 4)
            self.assertEqual(links, 2)
            a, b = folder / "a.zip", folder / "b.zip"
            first = checker.pack_skill(root, a)
            second = checker.pack_skill(root, b)
            self.assertEqual(first, second)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with zipfile.ZipFile(a) as zf:
                self.assertEqual(sorted(zf.namelist()), [
                    "r2r/LICENSE", "r2r/SKILL.md", "r2r/assets/R2R.md", "r2r/references/operating-guide.md"
                ])

    def test_missing_license_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.make_skill(Path(d))
            (root / "LICENSE").unlink()
            with self.assertRaises(checker.SkillCheckError):
                checker.check_skill(root)

    def test_mismatched_name_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.make_skill(Path(d))
            f = root / "SKILL.md"
            f.write_text(f.read_text().replace("name: r2r", "name: not-r2r"), encoding="utf-8")
            with self.assertRaises(checker.SkillCheckError):
                checker.check_skill(root)

    def test_missing_reference_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.make_skill(Path(d))
            f = root / "SKILL.md"
            f.write_text(f.read_text() + "[missing](references/no.md)\n", encoding="utf-8")
            with self.assertRaises(checker.SkillCheckError):
                checker.check_skill(root)

    def test_package_escape_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.make_skill(Path(d))
            f = root / "SKILL.md"
            f.write_text(f.read_text() + "[bad](../../outside.md)\n", encoding="utf-8")
            with self.assertRaises(checker.SkillCheckError):
                checker.check_skill(root)

    def test_duplicate_frontmatter_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = self.make_skill(Path(d))
            f = root / "SKILL.md"
            f.write_text(f.read_text().replace("name: r2r", "name: r2r\nname: r2r"), encoding="utf-8")
            with self.assertRaises(checker.SkillCheckError):
                checker.check_skill(root)


if __name__ == "__main__":
    unittest.main()
