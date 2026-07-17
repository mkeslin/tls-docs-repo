"""Wrap outstanding doc markers in GitBook danger-colored <mark> tags."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "release-notes", "guide", "node_modules", ".gitbook", "_tools"}

MARK_RE = re.compile(r'<mark\s+style="color:\$danger;">.*?</mark>', re.DOTALL)
OPEN = '<mark style="color:$danger;">'
CLOSE = "</mark>"


def protect_marks(text: str) -> tuple[str, list[str]]:
    parts: list[str] = []
    out: list[str] = []
    i = 0
    while True:
        m = MARK_RE.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i : m.start()])
        token = f"@@MARK{len(parts)}@@"
        parts.append(m.group(0))
        out.append(token)
        i = m.end()
    return "".join(out), parts


def restore_marks(text: str, parts: list[str]) -> str:
    for idx, part in enumerate(parts):
        text = text.replace(f"@@MARK{idx}@@", part)
    return text


def process_text(original: str) -> str:
    # Fix previously mangled compound markers first (outside protect)
    text = original.replace(
        '**TODO / <mark style="color:$danger;">**Decision needed:**</mark>**',
        f"{OPEN}**TODO / Decision needed:**{CLOSE}",
    )
    text = text.replace(
        f'{OPEN}**TODO:**{CLOSE} {OPEN}{CLOSE}{OPEN}',
        f"{OPEN}**TODO:** ",
    )
    # If we opened a combined wrap above that left a trailing CLOSE from the third mark,
    # normalize common AOP pattern to a single mark for the whole clause.
    text = re.sub(
        rf'{re.escape(OPEN)}\*\*TODO:\*\* ([^{CLOSE}<]+){re.escape(CLOSE)}',
        rf"{OPEN}**TODO:** \1{CLOSE}",
        text,
    )

    text, parts = protect_marks(text)

    # Compound outstanding markers
    text = re.sub(
        r"\*\*TODO / Decision needed:\*\*",
        f"{OPEN}**TODO / Decision needed:**{CLOSE}",
        text,
    )
    text = re.sub(
        r"(?<![*\w$])TODO / Decision needed:",
        f"{OPEN}**TODO / Decision needed:**{CLOSE}",
        text,
    )

    text = re.sub(
        r"\*\*Decision needed:\*\*",
        f"{OPEN}**Decision needed:**{CLOSE}",
        text,
    )
    text = re.sub(
        r"(?<![*\w$])Decision needed:",
        f"{OPEN}**Decision needed:**{CLOSE}",
        text,
    )

    text = re.sub(r"\*\*TODO:\*\*", f"{OPEN}**TODO:**{CLOSE}", text)
    text = re.sub(r"(?<![*\w/$])TODO:", f"{OPEN}**TODO:**{CLOSE}", text)
    text = re.sub(r"\*\*TODO\*\*(?!:)", f"{OPEN}**TODO**{CLOSE}", text)

    text = re.sub(
        r"(\*\*Status:\*\*\s*)Placeholder\b",
        rf"\1{OPEN}Placeholder{CLOSE}",
        text,
    )
    text = re.sub(
        r"(\|\s*)Placeholder(\s*\|)",
        rf"\1{OPEN}Placeholder{CLOSE}\2",
        text,
    )
    text = re.sub(
        r"(Status \| )Placeholder\b",
        rf"\1{OPEN}Placeholder{CLOSE}",
        text,
    )

    text = re.sub(
        r"(?<![A-Za-z@])TBD(?![A-Za-z])",
        f"{OPEN}TBD{CLOSE}",
        text,
    )

    text = re.sub(
        r"\*\*Review needed:\*\*",
        f"{OPEN}**Review needed:**{CLOSE}",
        text,
    )
    text = re.sub(
        r"(?<![*\w])Review needed:",
        f"{OPEN}**Review needed:**{CLOSE}",
        text,
    )

    text = re.sub(
        r"(\*\*Status:\*\*\s*)Draft\b",
        rf"\1{OPEN}Draft{CLOSE}",
        text,
    )
    text = re.sub(
        r"Status:\s*\*\*Draft\*\*",
        f"Status: {OPEN}**Draft**{CLOSE}",
        text,
    )
    # Table cell starting with Draft —
    text = re.sub(
        r"(\| )Draft( — )",
        rf"\1{OPEN}Draft{CLOSE}\2",
        text,
    )

    # Only color the outstanding *markers* (not the rest of the line/table cell).
    # Wrapping trailing prose breaks Markdown tables when cells contain '|'.
    return restore_marks(text, parts)


def main() -> None:
    changed: list[str] = []
    scanned = 0
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        scanned += 1
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            original = path.read_text(encoding="cp1252")
        updated = process_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))

    print(f"Scanned {scanned}, changed {len(changed)}")
    for rel in sorted(changed):
        print(rel)


if __name__ == "__main__":
    main()
