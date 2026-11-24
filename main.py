#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one original excuse (71 characters) to /output/entry.txt: the
AI wrote the bug, and the developer's only contribution was clicking
merge at 2 a.m.

Why this angle: a full-field read of all 572 submissions (430 real
titles) shows the worn premises are works-on-my-machine (51 hits),
staging (24), Friday 4:59 deploys (11+), load-bearing bugs/TODOs, and
tests-passed variants. AI authorship of the bug scores 0 hits, as do
refresh-twice, one-volunteer-maintainer and past-me angles. The joke
turns the blame onto the model first, then the twist reveals the human
did the one thing that mattered: merging it unread at 2 a.m. One
twist, dev voice, nothing to trim.

Stdlib only, deterministic: the same output on every run.
"""

import os

EXCUSE = (
    "The AI wrote the bug. "
    "My only contribution was clicking merge at 2 a.m."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
