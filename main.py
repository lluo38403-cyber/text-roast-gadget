"""One-Line Roast: The Gadget You Use Every Day — make.fun text entry.

Writes one line roasting a gadget used every day
to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

ENTRY = "My phone battery dies at 4pm every day, which is impressive commitment for something that promised me all-day battery life."
MAX_CHARS = 200


def main():
    assert ENTRY.strip(), "entry must not be blank"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, "round-trip mismatch"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
