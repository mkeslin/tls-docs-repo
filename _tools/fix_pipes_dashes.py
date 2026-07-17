from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "release-notes", "guide", "node_modules", ".gitbook", "_tools"}

REPLACEMENT = "\ufffd"  # Unicode replacement character


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
        text = text.replace(REPLACEMENT, "\u2014")
        text = re.sub(r"</mark>\|", "</mark> |", text)
        text = re.sub(r"\|<mark", "| <mark", text)
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))
    print(f"fixed {len(changed)}")
    for c in sorted(changed):
        print(c)


if __name__ == "__main__":
    main()
