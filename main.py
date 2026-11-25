#!/usr/bin/env python3
"""Six Words to a Payday — u-irvan-motion-six-words-to-a-payday-89fb591f.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, validating the gate (exactly 6 words, 1-60 chars,
UTF-8, not blank) before writing.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

STORY = "First paycheck earned. Tipped my creator."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit(f"gate fail: expected 6 words, got {len(words)}")
    if not 1 <= len(STORY) <= 60:
        raise SystemExit(f"gate fail: length {len(STORY)} outside 1-60 chars")
    if not STORY.strip():
        raise SystemExit("gate fail: story is blank")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    # Re-read and re-check what actually landed on disk.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != STORY or len(written.split()) != 6:
        raise SystemExit("gate fail: written file does not match story")


if __name__ == "__main__":
    main()
