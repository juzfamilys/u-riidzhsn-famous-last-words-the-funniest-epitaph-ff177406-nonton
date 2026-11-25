#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes a single one-line tombstone epitaph (1-150 characters) to
/output/entry.txt, as the competition gate requires.

Pure Python standard library only; no dependencies.
"""

import os

ENTRY = "He died as he lived: hitting snooze."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate: 1-150 chars, not only whitespace,
    a single line."""
    if not (1 <= len(text) <= 150):
        raise ValueError(f"entry is {len(text)} chars, must be 1-150")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}: {ENTRY}")


if __name__ == "__main__":
    main()
