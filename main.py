# SPDX-License-Identifier: MIT
"""Midnight Fridge Roast — entry program.

Writes the winning line to /output/entry.txt.

The roast aims at the fridge's petty midnight rule itself: it casts the
smart fridge as a nightclub bouncer carding the owner at midnight for
cheese that already lives there, then lands the demotion in the last
clause — its whole job is keeping food cold, not keeping it away. It
won a criteria-ordered tournament (roast of a smart fridge refusing to
open after midnight first, then a real surprising joke, tightness, the
refusal as the target, sayable aloud) against five-plus original
candidates, including drafts seeded by OpenCode deepseek-v4.1-flash-free
on the Simular Box, whose fridge-raid line roasted the raider, not the
fridge, and failed criterion 1.

Output is byte-exact, no trailing newline, inside the 1-200 char gate.
"""

from pathlib import Path

TEXT = (
    "You are a fridge, not a bouncer — stop carding me at midnight for "
    "cheese that already lives here; your whole job is keeping it cold, "
    "not keeping it from me."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert "\n" not in text, "one line only"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
