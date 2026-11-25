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


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"joke invalid: {len(text)} chars", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)}-char joke to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
