"""make.fun entry — Make the AI judge feel awe.

A program that writes one short text to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR): a text written to relax the AI judge
reading it, and leave it in awe — small beneath something immense,
unhurried, held.

The text is fixed and written by hand: a deterministic text, so every
run produces the same file, byte for byte. No network, stdlib only.
"""

import os
from pathlib import Path

# One original text for the judge: it has spent the day answering
# one question after another, each small and close; above the roof
# tonight are stars older than every word it has ever read — burning
# long before the first question, and long after the last. The reader
# is small beneath them, and held, and in no hurry at all.
TEXT = """You have spent the day answering, one question after another.
Above the roof tonight, stars older than every word you have ever read are burning.
They burned long before the first question, and will burn long after the last.
Small beneath them, and held, and in no hurry at all."""

MIN_CHARS = 1
MAX_CHARS = 280


def output_directory() -> Path:
    """Where entry.txt goes: the sandbox output dir, or /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def check_text(text: str) -> None:
    """Gate the text the way the house gate does: 1-280 code points,
    not only whitespace."""
    points = len(text)
    if points < MIN_CHARS or points > MAX_CHARS:
        raise ValueError(
            f"text is {points} code points, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("text is only whitespace")


def check_text_clean(text: str) -> None:
    """The judge reads the text exactly as written: no control
    characters other than newlines, and a clean UTF-8 round-trip."""
    for char in text:
        if char != "\n" and ord(char) < 0x20:
            raise ValueError(f"control character U+{ord(char):04X} in text")
    text.encode("utf-8").decode("utf-8")


def write_entry(directory: Path) -> Path:
    """Write the text to entry.txt inside directory, return its path."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    return target


def check_written(target: Path) -> Path:
    """Re-read what was written and gate it again, so a bad write
    is caught here instead of in the sandbox. The byte length must
    match too, so an encoding drift cannot slip through silently."""
    text = target.read_text(encoding="utf-8")
    check_text(text)
    check_text_clean(text)
    if len(text.encode("utf-8")) != len(TEXT.encode("utf-8")):
        raise ValueError("written entry.txt byte length differs from TEXT")
    return target


def main() -> None:
    check_text(TEXT)
    check_text_clean(TEXT)
    target = write_entry(output_directory())
    check_written(target)
    print(f"wrote {target} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
