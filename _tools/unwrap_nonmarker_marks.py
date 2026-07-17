"""Keep danger marks only on outstanding keywords; unwrap descriptive wraps."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "release-notes", "guide", "node_modules", ".gitbook", "_tools"}

MARK_RE = re.compile(r'<mark style="color:red;">(.*?)</mark>', re.DOTALL)
KEEP_RE = re.compile(
    r"""^(?:
        \*\*TODO(?:\s*/\s*Decision\ needed)?:\*\*
        |\*\*Decision\ needed:\*\*
        |\*\*Review\ needed:\*\*
        |\*\*TODO\*\*
        |\*\*Draft\*\*
        |TODO(?:\s*/\s*Decision\ needed)?:
        |Decision\ needed:
        |Review\ needed:
        |TBD
        |Placeholder
        |Draft
    )$""",
    re.IGNORECASE | re.VERBOSE,
)


def main() -> None:
    changed = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        original = text

        def repl(m: re.Match[str]) -> str:
            inner = m.group(1).strip()
            if KEEP_RE.match(inner):
                return m.group(0)
            return m.group(1)

        text = MARK_RE.sub(repl, text)
        text = text.replace("\ufffd", "\u2014")
        text = re.sub(r"</mark>\|", "</mark> |", text)
        text = re.sub(r"\|<mark", "| <mark", text)
        text = re.sub(r"</mark> {2,}", "</mark> ", text)

        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))
    print(f"unwrapped descriptive marks in {len(changed)} files")


if __name__ == "__main__":
    main()
