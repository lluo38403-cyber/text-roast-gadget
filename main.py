"""text-roast-gadget — make.fun entry.

The roast treats the phone as a demanding performer: it quits mid-afternoon but still acts entitled to praise for merely showing up.
"""

import os

ENTRY = 'My phone dies at 4pm every day, like a diva who only works mornings and still expects a five-star review for showing up.'

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
