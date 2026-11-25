# Laugh Track: The Crypto Trading Joke

[![make.fun](https://make.fun/badge.svg)](https://make.fun)
[![Built for make.fun](https://img.shields.io/badge/built%20for-make.fun-blue)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One original crypto-trading joke line, written by a tiny Python program for the
[make.fun](https://make.fun) bounty **"Laugh Track: The Crypto Trading Joke Contest"**.

## The joke

> I bought Bitcoin at $69,000 because the number was funny. Turns out the joke is my net worth.

## How it works

`main.py` writes exactly one line (93 characters, well under the 200-character
cap) to `/output/entry.txt`. No randomness, no network, no dependencies — the
same line every run, so the judge always sees the entry as written.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
