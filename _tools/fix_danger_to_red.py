from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "release-notes", "guide", "node_modules", ".gitbook"}
SUFFIXES = {".md", ".mdc", ".py"}

changed = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in SUFFIXES:
        continue
    if any(part in SKIP for part in path.parts):
        continue
    text = path.read_text(encoding="utf-8")
    # GitBook Git Sync does not resolve $danger as CSS; use a real color.
    new = text.replace("color:red", "color:red")
    if new != text:
        path.write_text(new, encoding="utf-8", newline="\n")
        changed.append(str(path.relative_to(ROOT)))

print(f"updated {len(changed)} files")
for c in sorted(changed)[:30]:
    print(c)
if len(changed) > 30:
    print(f"... +{len(changed) - 30} more")

sample = (ROOT / "internal/sops/deliver/legacy-system-migration.md").read_text(
    encoding="utf-8"
)
needle = "Rank which items belong"
i = sample.find(needle)
print("sample:", repr(sample[max(0, i - 70) : i + 20]))
