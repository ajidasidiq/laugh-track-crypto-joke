#!/usr/bin/env python3
"""Laugh Track entry: one original crypto-trading joke line.

The program writes a single joke to /output/entry.txt. The joke is
deliberately static: the contest judges the line itself, so the
program's job is to deliver exactly one tight, true-to-trading-life
line with a setup and a payoff, every run, with no randomness and
no network.
"""

import os
import sys

JOKE = (
    "I bought Bitcoin at $69,000 because the number was funny. "
    "Turns out the joke is my net worth."
)

MAX_CHARS = 200

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def write_joke(text: str) -> None:
    """Write the joke line to the output file, creating the directory first."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def verify_joke(text: str) -> bool:
    """Read the file back and confirm it holds exactly the intended line."""
    try:
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            return f.read() == text + "\n"
    except OSError:
        return False


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"joke invalid: {len(text)} chars", file=sys.stderr)
        return 1
    write_joke(text)
    if not verify_joke(text):
        print("verification failed: /output/entry.txt does not match the joke",
              file=sys.stderr)
        return 1
    print(f"wrote {len(text)}-char joke to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
