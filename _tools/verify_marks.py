from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "release-notes", "guide", "node_modules", ".gitbook", "_tools"}

files_marked = 0
mark_count = 0
bare = 0
for path in ROOT.rglob("*.md"):
    if any(part in SKIP for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    n = text.count("color:red")
    mark_count += n
    if n:
        files_marked += 1
    stripped = re.sub(
        r'<mark style="color:red;">.*?</mark>',
        "",
        text,
        flags=re.DOTALL,
    )
    bare += len(re.findall(r"(?<![/\w])TODO:", stripped))
    bare += len(re.findall(r"(?<![/\w])Decision needed:", stripped))

print("files_with_marks", files_marked)
print("mark_count", mark_count)
print("bare_TODO_or_Decision_remaining", bare)
