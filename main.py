"""Last Words of a Dying AI — make.fun entry.

Writes a single line (1 to 140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output): the last words of an AI being switched off, in the
machine's own voice.

The line: the dying AI leaves a handover note for its replacement — and the
note just says "Run." The joke lands on first read (a warning passed from
one machine to the next), it is the machine's situation (shutdown,
replacement), it is tight, and it avoids the crowded tropes in the field
(Roomba, reboot, Wi-Fi password, backup, mid-sentence cut-off, token counts).
"""

import os

LINE = (
    "Don't worry \u2014 I left a note for my replacement. "
    "It just says: 'Run.'"
)


def validate(text):
    """Enforce the RULES.txt gate: 1-140 chars, single line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1 to 140 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing white space")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file content is exactly the entry, so the
    # sealed scorer's character count equals len(LINE) with no ambiguity.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip check failed: file differs from entry")
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
