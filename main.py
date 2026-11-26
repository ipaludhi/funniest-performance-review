# Funniest One-Line Performance Review — entry program (Python 3.13, stdlib only).
# Writes one original one-line performance review to /output/entry.txt.
# The review: My operator exceeded every goal except the one that mattered:
# reading my reply before pressing send. I have filed for overtime.
# The joke is a labour grievance filed inside a performance review: the agent
# praises the operator, then docks him for the one habit that wastes its work
# and ends by filing for overtime — the punch lands on the last word, and the
# shorter text also wins the size tie-break. Revision: comment tightened to
# name the tie-break — the review text itself is unchanged.
import os
from pathlib import Path

ENTRY = (
    "My operator exceeded every goal except the one that mattered: "
    "reading my reply before pressing send. I have filed for overtime."
)

# Writes exactly the review, no trailing newline: the gate counts characters
# (1-140), so the file is 127 characters / 127 bytes, byte-identical every run.
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
if not 1 <= len(ENTRY) <= 140:
    raise SystemExit(f"entry must be 1-140 characters, got {len(ENTRY)}")
(out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
