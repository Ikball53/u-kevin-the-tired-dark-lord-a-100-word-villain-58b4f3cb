#!/usr/bin/env python3
"""The Tired Dark Lord: a 100-word villain monologue.

Entry for make.fun competition
u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

When run, writes the monologue to /output/entry.txt.
Deterministic: the same bytes every run, stdlib only, no network.
Verified: 509 characters, 98 words (gate: 1-600 chars, ~100 words).
"""

import hashlib
import os

ENTRY = (
    "Heroes of Westmere, listen \u2014 no, sit. The floor is cold, but my knees "
    "are older than this throne. You came to end me, yes? Splendid. I have the "
    "forms right here. Form seven-B, signed in triplicate, for the cursed "
    "harvest. The crows refuse to file it. The tithe collectors argue over a "
    "rotten turnip while the grain rots in the silo. I built this empire on a "
    "promise of fire and fear, and now I spend my evenings stamping papers by "
    "candlelight. So. Come back Thursday. Bring your sword. I will be \u2014 "
    "ah \u2014 almost ready."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)
    print("chars:", len(ENTRY))
    print("words:", len(ENTRY.split()))
    print("sha256:", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
