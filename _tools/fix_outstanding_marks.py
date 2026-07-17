"""Repair table corruption from wrapping trailing text that included '|'."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "release-notes", "guide", "node_modules", ".gitbook", "_tools"}

OPEN = '<mark style="color:$danger;">'
CLOSE = "</mark>"
MARK_RE = re.compile(
    r'<mark style="color:\$danger;">(.*?)</mark>',
    re.DOTALL,
)


def repair_text(text: str) -> str:
    # Empty marks
    text = text.replace(f"{OPEN}{CLOSE}", "")

    def fix_mark(m: re.Match[str]) -> str:
        inner = m.group(1)
        if "|" not in inner:
            return m.group(0)
        before, after = inner.split("|", 1)
        before = before.rstrip()
        # Put table pipe back outside the mark
        if before == "":
            return "|" + after
        return f"{OPEN}{before}{CLOSE} |" + after

    text = MARK_RE.sub(fix_mark, text)

    # Ensure a space between adjacent marks when the second starts with word/content
    text = re.sub(
        rf"{re.escape(CLOSE)}{re.escape(OPEN)}(?=\*\*|[A-Za-z])",
        f"{CLOSE} {OPEN}",
        text,
    )

    # Collapse TODO mark + following mark that is only the description (keep both, with space)
    # Already handled by space insertion.

    return text


def main() -> None:
    changed = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            original = path.read_text(encoding="cp1252")
        updated = repair_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))
    print(f"Repaired {len(changed)} files")
    for c in sorted(changed):
        print(c)


if __name__ == "__main__":
    main()
