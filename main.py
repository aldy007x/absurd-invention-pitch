#!/usr/bin/env python3
"""One-sentence pitch for make.fun's "One-Sentence Absurd Invention Pitch" bounty.

The whole entry is a single sentence (at most 220 characters) pitching a
ridiculous invention that fixes a tiny everyday annoyance. This program writes
that sentence to /output/entry.txt, where the sealed scorer and the house
judge read it.

The pitch, chosen after weighing the judge's brief (funny invention first,
then a clever fix, originality, tightness):
- the annoyance is tiny and universal: someone always squeezes the
  toothpaste tube from the middle;
- the invention is absurd but weirdly plausible: a tube that squeezes itself
  from the bottom, correctly, every time;
- the laugh comes from the invention itself: instead of a complaint, it
  leaves a one-star review of the offender on the bathroom mirror, so the
  tube acts as both housekeeper and critic;
- the name carries the joke: the Tube Tribunal passes judgement on the
  bathroom's oldest cold war.
"""

PITCH = (
    "Meet the Tube Tribunal: a toothpaste tube that squeezes itself from the "
    "bottom and leaves a one-star review of whoever squeezed the middle on "
    "the bathroom mirror, ending the bathroom\u2019s oldest cold war."
)

MAX_CHARS = 220


def main() -> None:
    text = PITCH.strip()
    if not text:
        raise SystemExit("pitch is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(text)} chars, over the 220 limit")
    # Exactly one sentence: a single terminal period and no other
    # sentence-ending punctuation.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    if "?" in text or "!" in text:
        raise SystemExit("pitch must be exactly one sentence")
    if text != text.strip() or "\n" in text:
        raise SystemExit("pitch must be a single line with no extra whitespace")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)}-char pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
