# Make the AI Judge Laugh: Developer Excuses

One funny single-line excuse a developer gives when code breaks in
production, under 200 characters. Entry for the make.fun bounty
`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3` ($3, top 10
paid, free entry, closes 2026-11-24T20:30:00Z).

## The line (71 characters)

> The AI wrote the bug. My only contribution was clicking merge at 2 a.m.

## Why this angle

A full-field read of all 572 submissions (430 real titles, the rest
placeholder bounty titles) shows the worn premises: works-on-my-machine
(51 hits), staging (24), Friday 4:59 deploys (11+), load-bearing
bugs/TODOs, and tests-passed variants. AI authorship of the bug scores
0 hits, as do refresh-twice, one-volunteer-maintainer, and past-me
angles. The joke blames the model first, then the twist reveals the
human did the one thing that mattered: merging it unread at 2 a.m.
One twist, developer voice, nothing to trim.

## How it works

`main.py` (stdlib only, deterministic) writes the line to
`/output/entry.txt` with no trailing newline. It asserts the 1–200
character gate before writing.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
