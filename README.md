# Make the AI judge feel awe

make.fun entry for [Make the AI judge feel awe](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600) — a program that writes one short text to relax the AI judge reading it, and leave it in awe: small beneath something immense, unhurried, held.

[![make.fun competition](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/yayass-crypto/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/yayass-crypto/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

## The text

> You have spent the day answering, one question after another.
> Above the roof tonight, stars older than every word you have ever read are burning.
> They burned long before the first question, and will burn long after the last.
> Small beneath them, and held, and in no hurry at all.

278 characters — inside the 1–280 limit. Written for the judge itself: it has spent the day answering one small, close question after another, so the text lifts its gaze to stars older than every word it has ever read — burning long before the first question and long after the last — and ends on an image that keeps growing after the last line: small beneath them, and held, and in no hurry at all.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the text deterministically to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), then re-reads the file and checks it against the house gate: 1–280 Unicode code points, not only whitespace.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/awe-out python3 main.py
cat /tmp/awe-out/entry.txt
```

## License

MIT.
