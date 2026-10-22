#!/usr/bin/env python3
"""Validate and deterministically package the portable R2R Skill.

This is a *source/package* check, not an agent-host test or GitHub Release.
No third-party Python dependencies. Publishing stays a maintainer decision.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "r2r"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
METADATA_PATTERN = re.compile(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*)$")
REQUIRED = ("SKILL.md", "LICENSE", "assets/R2R.md", "references/operating-guide.md")


class SkillCheckError(Exception):
    """The candidate directory violates the portable package contract."""


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SkillCheckError("SKILL.md must start with YAML frontmatter (---)")
    try:
        closing = lines.index("---", 1)
    except ValueError as exc:
        raise SkillCheckError("SKILL.md frontmatter has no closing ---") from exc
    result: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = METADATA_PATTERN.match(line)
        if not match:
            raise SkillCheckError(f"Unsupported frontmatter line: {line!r}")
        key, value = match.groups()
        if key in result:
            raise SkillCheckError(f"Duplicate frontmatter key: {key}")
        result[key] = value.strip().strip('"').strip("'")
    return result


def check_skill(root: Path) -> tuple[list[Path], int]:
    root = root.resolve()
    if not root.is_dir():
        raise SkillCheckError(f"Missing skill directory: {root}")
    for name in REQUIRED:
        if not (root / name).is_file():
            raise SkillCheckError(f"Missing required package file: {name}")
    metadata = parse_frontmatter((root / "SKILL.md").read_text(encoding="utf-8"))
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_PATTERN.fullmatch(name) or name != root.name:
        raise SkillCheckError("Skill frontmatter name must match a lowercase hyphenated directory")
    if not description or len(description) > 1024:
        raise SkillCheckError("Skill description must be nonempty and at most 1024 chars")
    if "metadata" in metadata or any(key.startswith("metadata.github") for key in metadata):
        raise SkillCheckError("Install-derived metadata must not be committed to a published skill")

    paths = sorted(x for x in root.rglob("*") if x.is_file() or x.is_symlink())
    if not paths:
        raise SkillCheckError("No Skill files found")
    links_checked = 0
    for path in paths:
        if path.is_symlink():
            raise SkillCheckError(f"Symlinks are not allowed in portable package: {path}")
        if root not in path.resolve().parents:
            raise SkillCheckError(f"File escaped Skill directory: {path}")
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            href = match.group(1).strip()
            if href.startswith("#"):
                continue
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in ("https", "http", "mailto"):
                    raise SkillCheckError(f"Unexpected link scheme in {path.name}: {href}")
                continue
            decoded = unquote(parsed.path)
            if not decoded:
                continue
            target = (path.parent / decoded).resolve()
            if target != root and root not in target.parents:
                raise SkillCheckError(f"Skill link escapes its package: {path}: {href}")
            if not target.is_file():
                raise SkillCheckError(f"Missing Skill link target: {path}: {href}")
            links_checked += 1
    return paths, links_checked


def pack_skill(root: Path, output: Path) -> str:
    paths, _ = check_skill(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Stable archive metadata: same inputs produce the same bytes.
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in paths:
            info = zipfile.ZipInfo(
                "r2r/" + path.relative_to(root).as_posix(),
                date_time=(2024, 1, 1, 0, 0, 0),
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    (output.parent / (output.name + ".sha256")).write_text(
        f"{digest}  {output.name}\n", encoding="utf-8"
    )
    return digest


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--pack", type=Path, help="Build a Skill-only ZIP and SHA-256 text")
    cli.add_argument("--skill-root", type=Path, default=SKILL, help="Skill root (default: bundled r2r)")
    args = cli.parse_args()
    try:
        files, links = check_skill(args.skill_root)
        print(f"SKILL_SOURCE_CHECK_PASS: {len(files)} files; {links} internal links; name={args.skill_root.name}")
        if args.pack:
            digest = pack_skill(args.skill_root, args.pack)
            print(f"PACKAGE_CREATED: {args.pack} sha256={digest}")
        return 0
    except (SkillCheckError, OSError, UnicodeError) as exc:
        print(f"SKILL_SOURCE_CHECK_FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
