#!/usr/bin/env python3
"""Validate R2R's standalone animated landing HTML (without external Python deps)."""
from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile


class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.anchors = []
        self.remote_assets = []
        self.script_count = 0
        self.inline_script = []
        self.script_active = False
        self.title_count = 0
        self.headings = 0
        self.lang = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.append(d["id"])
        if tag == "a" and d.get("href", "").startswith("#"):
            self.anchors.append(d["href"][1:])
        if tag == "html":
            self.lang = bool(d.get("lang"))
        if tag == "h1":
            self.headings += 1
        if tag == "title":
            self.title_count += 1
        if tag == "script":
            self.script_count += 1
            self.script_active = True
            if "src" in d:
                self.remote_assets.append("external script")
        if tag == "link" and d.get("rel", "").lower() == "stylesheet":
            self.remote_assets.append("external stylesheet")
        if tag in ("img", "iframe") and d.get("src"):
            self.remote_assets.append(tag + " source")

    def handle_endtag(self, tag):
        if tag == "script":
            self.script_active = False

    def handle_data(self, data):
        if self.script_active:
            self.inline_script.append(data)


REQUIRED_IDS = (
    "main", "demo", "the-problem", "the-answer", "how-to-start",
    "watch-stalled", "watch-r2r", "lane-stalled", "lane-r2r",
    "state-text", "state-tag", "step-count", "progress-fill",
    "progress", "toggle-play", "restart", "copy-install", "install-command",
)


def check(path: Path, *, syntax_check: bool = True) -> list[str]:
    issues = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as err:
        return [f"file is unreadable: {err}"]
    audit = Audit()
    try:
        audit.feed(text)
        audit.close()
    except ValueError as err:
        return [f"bad HTML parser input: {err}"]
    if not text.lstrip().lower().startswith("<!doctype html>"):
        issues.append("expected HTML5 doctype")
    if not audit.lang:
        issues.append("missing html lang")
    if audit.headings != 1 or audit.title_count != 1:
        issues.append("expected exactly one h1 and title")
    if audit.script_count != 1 or not "".join(audit.inline_script).strip():
        issues.append("expected one nonempty inline JavaScript block")
    if audit.remote_assets:
        issues.append("standalone page references external assets: " + ", ".join(audit.remote_assets))
    if len(audit.ids) != len(set(audit.ids)):
        issues.append("duplicate DOM element IDs")
    for anchor in audit.anchors:
        if anchor and anchor not in audit.ids:
            issues.append("missing anchor target: " + anchor)
    for element in REQUIRED_IDS:
        if element not in audit.ids:
            issues.append("missing interactive DOM element: " + element)
    # A hidden-by-default reveal can make entire below-fold sections invisible in
    # browser screenshots, disabled-JS situations or delayed observer callbacks.
    if re.search(r"\.reveal\s*\{[^}]*\bopacity\s*:\s*0(?:[;\s}]|$)", text, re.S):
        issues.append("landing sections must remain readable without scroll animation")
    for expected in ("prefers-reduced-motion", "aria-live", "not a timed benchmark",
                     "Spec", "Multi-Agent", "HARDEN", "READY"):
        if expected.lower() not in text.lower():
            issues.append("missing content/accessibility cue: " + expected)
    if syntax_check and audit.script_count == 1 and audit.inline_script:
        script = "".join(audit.inline_script)
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "landing.js"
            file.write_text(script, encoding="utf-8")
            try:
                proc = subprocess.run(["node", "--check", str(file)], capture_output=True,
                                      text=True, timeout=15, check=False)
                if proc.returncode:
                    issues.append("inline JS syntax failed: " + proc.stderr.strip()[:500])
            except (OSError, subprocess.TimeoutExpired) as err:
                issues.append("Node JS syntax check NOT_RUN: " + str(err))
    return issues


def main() -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--path", type=Path,
                     default=Path(__file__).resolve().parent.parent / "docs/product/landing.html")
    args = cli.parse_args()
    problems = check(args.path)
    for problem in problems:
        print("LANDING_FAIL: " + problem, file=sys.stderr)
    if problems:
        return 1
    print("LANDING_PASS: HTML structure, accessible controls, self-contained assets, JS syntax")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
