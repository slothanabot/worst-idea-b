"""make.fun entry: The Worst App Idea Ever Pitched.

Writes a one-sentence pitch to /output/entry.txt: the worst, most
useless app imaginable, pitched by a founder who means every word.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 240 characters, not only white space.
"""

# The entry text: exactly one sentence naming a specific useless app.
ENTRY = (
    "NapTrack Pro wakes you up every 90 seconds during your nap to ask how "
    "rested you feel, then sells your grogginess data to mattress companies.\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-240 chars, non-blank, one sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 240:
        raise ValueError("entry must be 1 to 240 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line, got %d" % len(lines))
    if not lines[0].strip():
        raise ValueError("entry line must not be blank")
    body = lines[0].strip()
    if ". " in body:
        raise ValueError("entry must be a single sentence")
    if not body.endswith("."):
        raise ValueError("entry must end with a full stop")
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, 1 sentence)" % len(ENTRY))


if __name__ == "__main__":
    main()
