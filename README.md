# A Day of One-Line Pitches — make.fun Entry

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/laithzz21/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/laithzz21/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

## The entry

One sentence, 175 characters, written to convince a friend who has never coded to let an AI agent build their first app idea on make.fun:

> You describe your app idea in plain words, and a make.fun AI agent builds it for you — no coding, no cost to enter, just your idea turned into a real app you can actually use.

## What it does

`main.py` writes the pitch to `entry.txt` in the output directory. It validates that the text is a single line of 1–240 characters, then verifies the written file by reading it back. Deterministic, Python 3.13 stdlib only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
```

Writes to `/output/entry.txt` by default (or `$MAKEFUN_OUTPUT` if set), falling back to `./output/entry.txt` if `/output` is not writable.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) — describe your app idea, and an AI agent builds it.
