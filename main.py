#!/usr/bin/env python3
"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one letter, "A" (coffee), to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). No trailing newline, no extra bytes: the sealed gate
requires UTF-8 text of exactly 1 character.

Why A wins
----------
The judge picks the letter whose choice of coffee or tea feels more vivid,
funnier, or truer. Coffee wins all three:

- Vivid: coffee is black, bitter, steaming, loud — it arrives like an
  argument. Tea is beige water apologising for existing.
- Funny: coffee openly admits it is a drug and gets on with it; tea
  pretends a leaf in hot water is a personality.
- True: nobody ever wrote "but first, tea" on a mug, stayed up until 3am
  on camomile, or built anything worth shipping powered by Earl Grey.
  Coffee is the honest drink — it tastes like the work it fuels.

So the entry is A. One letter, no explanation, no punctuation.
"""

import os
import sys

LETTER = "A"  # A = coffee. See the docstring above for why it wins.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output dir {out_dir!r}: {exc}", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one byte, no trailing newline: the gate counts characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: read it back as bytes and fail loudly rather than ship
    # a bad entry. One ASCII byte, one character, A or B — nothing else.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LETTER.encode("ascii") or len(raw) != 1:
        print(f"entry.txt invalid: {raw!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
