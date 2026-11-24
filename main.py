#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line office joke (89 characters) to /output/entry.txt.

The joke: a fake "as discussed" email about something nobody ever discussed,
and three colleagues replying "agreed" anyway. Specific office detail
(the "as discussed" email convention), a turn that pays off in the very
last word, and tight enough to read in one pass.

Standard library only. Deterministic: same bytes on every run. No network,
no randomness, no clock, no input files.
"""

import os

JOKE = "I wrote 'as discussed' about something we never discussed. Three people replied 'agreed'."


def main() -> None:
    # Gate self-check, mirroring RULES: 1-200 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the gate"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the joke, one line, 89 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
