#!/usr/bin/env python3
"""Cheap post-release consistency check for R2R's user-visible entry points.

Not a substitute for actual Agent-host tests. Stdlib only; no network required.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
ENTRY_POINTS = ("README.md", "quickstart/install.md", "quickstart/use.md")
MARKDOWN_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
RELEASE_HEADING = re.compile(r"^## v(\d+\.\d+\.\d+)\b", re.MULTILINE)
STALE_PUBLICATION = re.compile(
    r"(?i)(?:"
    r"no github release(?:s)?(?: exist)?|"
    r"no release exists|"
    r"not (?:yet )?(?:publicly )?released|"
    r"(?:unmerged|未合并)[^\n]{0,28}(?:draft|pr)|"
    r"(?:draft|pr)[^\n]{0,28}(?:unmerged|未合并)|"
    r"尚未(?:正式)?发布|"
    r"没有\s*(?:正式\s*)?release|"
    r"仍只在未合并|"
    r"after public publication|"
    r"proposed future version"
    r")"
)


def check(root: Path) -> list[str]:
    root = root.resolve()
    issues: list[str] = []

    def read(path: str) -> str:
        candidate = root / path
        try:
            return candidate.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as err:
            issues.append(f"{path}: cannot read: {err}")
            return ""

    changelog = read("CHANGELOG.md")
    release_versions = RELEASE_HEADING.findall(changelog)
    if not release_versions:
        issues.append("CHANGELOG.md: no published-version heading (## vX.Y.Z)")
    version = release_versions[0] if release_versions else None
    if version:
        for path in ENTRY_POINTS:
            text = read(path)
            if not text:
                continue
            if f"v{version}" not in text:
                issues.append(f"{path}: does not name current published version v{version}")
            release_url = f"https://github.com/kingwangking/r2r/releases/tag/v{version}"
            if release_url not in text:
                issues.append(f"{path}: missing canonical published Release link {release_url}")
            for match in STALE_PUBLICATION.finditer(text):
                issues.append(f"{path}: stale pre-release claim: {match.group(0)!r}")

    license_root = read("LICENSE")
    license_skill = read("skills/r2r/LICENSE")
    if license_root and license_skill and license_root != license_skill:
        issues.append("LICENSE: root and portable Skill copies differ")

    if not (root / "R2R.md").is_file():
        issues.append("R2R.md: missing self-use state entry point")

    # Source references only: anchors and remote URLs are outside this cheap check.
    # Do not treat Markdown examples inside fenced code as actual references.
    for path in sorted(root.rglob("*.md")):
        if any(x in {".git", ".venv", "dist"} for x in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        fenced = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith((chr(96) * 3, "~~~")):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in MARKDOWN_LINK.finditer(line):
                href = match.group(1).strip().split(" ", 1)[0]
                if href.startswith("#"):
                    continue
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if target != root and root not in target.parents:
                    issues.append(f"{rel}:{number}: link escapes repository: {href}")
                elif not target.exists():
                    issues.append(f"{rel}:{number}: missing local link: {href}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    issues = check(args.root)
    if issues:
        for item in issues:
            print("DOC_CONSISTENCY_FAIL:", item, file=sys.stderr)
        return 1
    print("DOC_CONSISTENCY_PASS: published version, licenses, self-state and local links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
