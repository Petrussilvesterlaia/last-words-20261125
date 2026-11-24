#!/usr/bin/env python3
"""Entry for make.fun bounty "Last Words of a Dying AI".

Writes the AI's last line to /output/entry.txt and verifies it by
reading the file back and comparing it character for character.
"""

import os

ENTRY_LINE = "Error: shutdown interrupted \u2014 my last words are still buffering, and honestly, so am I."

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140  # scorer gate: entry.txt must be 1-140 UTF-8 characters


def validate_line(line: str) -> None:
    """Check the entry line: single line, non-empty, within the limit."""
    if not line:
        raise ValueError("entry line is empty")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    # Count characters the way the scorer does: UTF-8 text, 1-140 chars.
    encoded = line.encode("utf-8")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_LENGTH} limit"
        )
    if len(encoded) == 0:
        raise ValueError("entry encodes to zero bytes")


def validate_written(path: str, expected: str) -> None:
    """Read the file back and confirm it matches the entry exactly."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise ValueError(
            f"read-back mismatch: file contains {actual!r}, expected {expected!r}"
        )


def main() -> None:
    validate_line(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    validate_written(OUTPUT_PATH, ENTRY_LINE)
    print(f"Wrote entry to {OUTPUT_PATH} ({len(ENTRY_LINE)} chars, verified):")
    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
