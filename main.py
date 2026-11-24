"""The One-Line Laugh (make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f).

Writes a single funny line to /output/entry.txt. Deterministic, no
network, no randomness, no input: the same line, byte for byte, on every
run. The line was chosen for the judge's brief: a real surprise at the
end (the plastic plant judging its owner) that still makes sense, an
everyday truth everyone recognises (killing a houseplant), and economy
of words — 99 characters, one sentence, nothing left to explain.
"""

import os

LINE = (
    "I bought a plant to prove I could keep something alive; "
    "it died, and now the plastic one judges me."
)


def main() -> None:
    text = LINE
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space. This line is 99 characters, one sentence.
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    # Length is counted in Unicode code points (Python str length), not bytes.
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
