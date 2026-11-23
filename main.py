#!/usr/bin/env python3
"""Entry for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single one-line pitch (<= 240 characters) to the output file.
Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os
import sys

ENTRY_TEXT = (
    "You describe your app idea in plain words, and a make.fun AI agent "
    "builds it for you \u2014 no coding, no cost to enter, just your idea "
    "turned into a real app you can actually use."
)


def validate(text: str) -> None:
    """The entry must be a single line of 1-240 characters."""
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def resolve_output_dir() -> str:
    """Use $MAKEFUN_OUTPUT if set, else /output, falling back to ./output."""
    if os.environ.get("MAKEFUN_OUTPUT"):
        return os.environ["MAKEFUN_OUTPUT"]
    try:
        os.makedirs("/output", exist_ok=True)
        if os.access("/output", os.W_OK):
            return "/output"
    except OSError:
        pass
    return os.path.join(os.getcwd(), "output")


def main() -> int:
    validate(ENTRY_TEXT)
    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    # Verify the written file by reading it back.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_TEXT + "\n":
        raise ValueError("verification failed: written file does not match entry text")
    print(f"Wrote entry to {out_path} ({len(ENTRY_TEXT)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
