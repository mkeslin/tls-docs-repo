#!/usr/bin/env python3
"""Fix UTF-8-as-Windows-1252 mojibake in markdown/mdc files."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Unicode codepoint -> cp1252 byte for the 0x80-0x9F window (and euro).
_CP1252_BYTE = {
    0x20AC: 0x80,  # €
    0x201A: 0x82,  # ‚
    0x0192: 0x83,  # ƒ
    0x201E: 0x84,  # „
    0x2026: 0x85,  # …
    0x2020: 0x86,  # †
    0x2021: 0x87,  # ‡
    0x02C6: 0x88,  # ˆ
    0x2030: 0x89,  # ‰
    0x0160: 0x8A,  # Š
    0x2039: 0x8B,  # ‹
    0x0152: 0x8C,  # Œ
    0x017D: 0x8E,  # Ž
    0x2018: 0x91,  # ‘
    0x2019: 0x92,  # ’
    0x201C: 0x93,  # “
    0x201D: 0x94,  # ”
    0x2022: 0x95,  # •
    0x2013: 0x96,  # –
    0x2014: 0x97,  # —
    0x02DC: 0x98,  # ˜
    0x2122: 0x99,  # ™
    0x0161: 0x9A,  # š
    0x203A: 0x9B,  # ›
    0x0153: 0x9C,  # œ
    0x017E: 0x9E,  # ž
    0x0178: 0x9F,  # Ÿ
}


def _to_cp1252_bytes(s: str) -> bytes:
    out = bytearray()
    for ch in s:
        o = ord(ch)
        if o < 0x80:
            out.append(o)
        elif 0xA0 <= o <= 0xFF:
            out.append(o)
        elif 0x80 <= o <= 0x9F:
            # C1 controls stored as themselves (undefined cp1252 slots)
            out.append(o)
        elif o in _CP1252_BYTE:
            out.append(_CP1252_BYTE[o])
        else:
            raise UnicodeEncodeError("cp1252", ch, 0, 1, "not in cp1252")
    return bytes(out)


def fix_cp1252_utf8_mojibake(text: str) -> str:
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == "\u00e2" and i + 2 < n:
            chunk = text[i : i + 3]
            try:
                fixed = _to_cp1252_bytes(chunk).decode("utf-8")
                out.append(fixed)
                i += 3
                continue
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        if ch in "\u00c2\u00c3" and i + 1 < n:
            chunk = text[i : i + 2]
            try:
                fixed = _to_cp1252_bytes(chunk).decode("utf-8")
                if fixed != chunk:
                    out.append(fixed)
                    i += 2
                    continue
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        out.append(ch)
        i += 1
    return "".join(out)


def fix_text(text: str) -> str:
    if text.startswith("\ufeff"):
        text = text.lstrip("\ufeff")
    text = text.replace("ï»¿", "")
    text = fix_cp1252_utf8_mojibake(text)
    text = text.replace("Â", "")
    return text


def main() -> int:
    paths = [
        p
        for p in ROOT.rglob("*")
        if p.is_file()
        and p.suffix.lower() in {".md", ".mdc"}
        and ".git" not in p.parts
        and "node_modules" not in p.parts
    ]
    changed = 0
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        fixed = fix_text(text)
        if fixed != text:
            path.write_text(fixed, encoding="utf-8", newline="\n")
            changed += 1
            print(f"fixed: {path.relative_to(ROOT)}")
    print(f"\nUpdated {changed} of {len(paths)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
