#!/usr/bin/env python3
"""Real-Life Patch Notes — write one changelog line to entry.txt.

The bounty asks for a single-line software patch note, at most 160
characters, for a bug in real life or human biology, in the terse
register of a real release note. This program writes exactly that
line, and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

# The patch note, written for this bounty: a real-life bug (yawning
# betraying boredom in a meeting) reported in the flat, terse voice of
# a release note, with the version tag up front and the sting at the end.
LINE = (
    "v2.4.2: Fixed a bug where yawning in a meeting silently notified "
    "everyone in the room that you were bored."
)


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-160 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One line only, no
    # line breaks inside the line.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())