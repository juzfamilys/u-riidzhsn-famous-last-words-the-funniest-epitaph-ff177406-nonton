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


def validate_entry(path: str, expected: str) -> None:
    """Guard: re-read the file back from disk and re-validate the exact
    bytes written, so a silent write failure can never pass quietly.

    Checks the raw bytes decode as valid UTF-8, contain exactly the
    expected single line (no trailing newline or extra bytes), and pass
    the same competition gate as the in-memory entry.
    """
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{path} is not valid UTF-8: {exc}") from exc
    if text != expected:
        raise ValueError(
            f"{path} on disk does not match the entry: "
            f"got {text!r}, expected {expected!r}"
        )
    validate(text)


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    validate_entry(OUTPUT_PATH, ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}: {ENTRY}")


if __name__ == "__main__":
    main()
