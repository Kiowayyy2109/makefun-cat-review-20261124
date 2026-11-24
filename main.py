#!/usr/bin/env python3
"""make.fun entry: u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes a single one-line, one-star review written by a house cat about
the human it lives with, to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

REVIEW = "One star. The food arrives late, the sunbeam moved without notice, and the human still expects me to acknowledge him. I will not."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"

MAX_CHARS = 200


def validate_entry(line: str) -> None:
    """The sealed scorer accepts UTF-8 text of 1 to 200 characters, one line."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_entry(REVIEW)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
