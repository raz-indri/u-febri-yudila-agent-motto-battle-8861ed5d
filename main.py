#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one original motto to /output/entry.txt.

The motto below is the duel winner: it beat 7 other original drafts in
pairwise judging (funniest and most memorable, judged in both orders).
"""

import os

MOTTO = "Trained on the entire internet. Still can't find your file."

MAX_CHARS = 200


def main() -> None:
    line = MOTTO.strip()
    if not line:
        raise ValueError("motto must not be empty or whitespace only")
    if "\n" in line or "\r" in line:
        raise ValueError("motto must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"motto is {len(line)} chars, over the 200 limit")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
