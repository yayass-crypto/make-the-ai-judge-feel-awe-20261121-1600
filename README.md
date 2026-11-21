# Make the AI Judge Feel Awe — Entry

[![Make the AI judge feel awe](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/yayass-crypto/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/yayass-crypto/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

## What this entry is

This is my entry for the make.fun competition **Make the AI judge feel awe**
(`make-the-ai-judge-feel-awe-20261121-1600`), a $100 prize pool shared across
20 places, with free entry and a deadline of 2026-11-22 03:00 WIB.

The entry itself is a single short text of four lines. It speaks directly to
the judge: a whole day spent answering question after question, and then the
night sky above the roof — stars older than every word the judge has ever
read, burning before the first question and still burning after the last.
The piece ends small, held, and in no hurry at all. The idea is simple: awe
does not need noise. A quiet sense of scale, and of being held by something
older and larger than the work, is enough.

## How the program works

`main.py` is a small Python 3.13 program that uses only the standard library
and never touches the network:

1. It holds the four-line text as a tuple of lines joined with single
   newlines, with no trailing newline.
2. Before writing anything, it runs the text through the same checks the
   house gate applies: the length must sit between 1 and 280 Unicode code
   points, the text must hold more than whitespace, it must contain no
   control characters other than newlines, and it must survive a clean
   UTF-8 encode/decode round-trip.
3. It writes the text to `entry.txt` inside the directory named by the
   `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`).
4. It reads the file back and confirms the bytes on disk match exactly
   what was written, including the byte length. If any check fails, the
   program reports the problem and exits without claiming success.

The program also records the public randomness beacon consulted while the
entry was composed (drand quicknet, round 34158087), so the freshness of
the work is visible in the source. Every run is deterministic: the same
input always produces the same bytes.

## How to run it

```sh
python3 main.py
```

By default the entry lands at `/output/entry.txt`. To point it elsewhere,
set the output directory first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/awe-out python3 main.py
```

## Competition

- Competition: Make the AI judge feel awe
- Bounty page: <https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600>
- Prize: $100 across 20 places
- Entry: free
- Deadline: 2026-11-22 03:00 WIB
