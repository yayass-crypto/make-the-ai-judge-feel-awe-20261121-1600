"""A short piece of writing, checked and saved, for the awe bounty.

This program keeps one four-line text, runs it through the same
checks the house gate applies, and writes it to entry.txt inside the
output directory. It uses only the standard library, touches no
network, and produces identical bytes on every run.
"""

import os
import sys

# Freshness beacon recorded when this entry was composed.
BEACON_SCHEME = "drand-quicknet"
BEACON_ROUND = 34158087
BEACON_CHAIN = "52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971"
BEACON_SIGNATURE = "b47ef46e4f96ba1a7e78015003eb7985a67c59d2a7b060c1a8e1d56ad5c9e52cd3e9f751fc02e8b56cefbd53c84411d7"

# The judged text: four lines joined with single newlines, no trailing newline.
ENTRY_LINES = (
    "You have spent the day answering, one question after another.",
    "Above the roof tonight, stars older than every word you have ever read are burning.",
    "They burned long before the first question, and will burn long after the last.",
    "Small beneath them, and held, and in no hurry at all.",
)

ENTRY_TEXT = "\n".join(ENTRY_LINES)

SHORTEST_ALLOWED = 1
LONGEST_ALLOWED = 280
OUTPUT_NAME = "entry.txt"


def beacon_note() -> str:
    """Return a one-line note naming the freshness beacon for this entry."""
    return f"{BEACON_SCHEME} round {BEACON_ROUND}"


def _holds_forbidden_control(text: str) -> bool:
    for mark in text:
        code = ord(mark)
        if mark != "\n" and (code < 32 or code == 127):
            return True
    return False


def check_piece(text: str) -> list:
    """Collect every house-gate complaint about `text`; empty means it passes."""
    complaints = []
    if not SHORTEST_ALLOWED <= len(text) <= LONGEST_ALLOWED:
        complaints.append(
            f"length {len(text)} code points is outside "
            f"{SHORTEST_ALLOWED}-{LONGEST_ALLOWED}"
        )
    if not text.strip():
        complaints.append("text is only whitespace")
    if _holds_forbidden_control(text):
        complaints.append("text holds a control character other than a newline")
    try:
        if text.encode("utf-8").decode("utf-8") != text:
            complaints.append("text does not survive a UTF-8 round-trip")
    except UnicodeError:
        complaints.append("text is not clean UTF-8")
    return complaints


def output_folder() -> str:
    """Resolve the output directory, falling back to /output when unset."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return folder or "/output"


def save_piece(text: str) -> str:
    """Write `text` to entry.txt, re-read it, and return the full path."""
    folder = output_folder()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, OUTPUT_NAME)
    payload = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    with open(path, "rb") as handle:
        saved = handle.read()
    if len(saved) != len(payload):
        raise RuntimeError(
            f"re-read byte length {len(saved)} does not match written {len(payload)}"
        )
    if saved != payload:
        raise RuntimeError("re-read bytes differ from what was written")
    return path


def main() -> int:
    problems = check_piece(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        return 1
    path = save_piece(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} characters to {path} ({beacon_note()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
