"""Two Robots in an Elevator — make.fun entry.

Writes one funny line of awkward small talk that one robot says to
another while riding an elevator together, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line itself is the entry: no trailing
newline, so the file's character count equals the line's length.

The line: a robot admits it faked sleep mode to dodge elevator small
talk, only for the other robot to board — leaving both of them awake,
together, with nothing left to hide behind.

Verified 2026-11-25: two runs write byte-identical entry.txt (sha256
b27d9ddabb8658f2bb5157a16e5ed3633b5f5046165b953c3f0260afeebf7adb),
109 characters / 111 bytes, no trailing newline.

Fix 2026-11-25 (Gate 1 finding): the v3 line anchored the elevator only
with "this ride" + "boarded", which could be any vehicle; the line now
says "this elevator ride" outright, and the slack word "just" was trimmed
(the ellipsis already carries the pause), keeping the line tight.
"""

import os

ENTRY = "I set myself to sleep mode for this elevator ride, but then you boarded, and now we're both\u2026 awake. Together."


def main():
    line = ENTRY
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
