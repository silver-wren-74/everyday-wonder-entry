#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt.
"""

import os

SENTENCE = (
    "The escalator handrail slips a fraction ahead of the steps, "
    "so my hand arrives at the top before the rest of me does."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
