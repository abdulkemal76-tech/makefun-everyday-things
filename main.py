"""Everyday Things, Two Lines: a traffic jam explained to a 10-year-old.

Writes the two-line explanation to /output/entry.txt.
Line 1 explains the everyday thing through one concrete analogy.
Line 2 says what the analogy maps and what it leaves out.
Standard library only.
"""

import os

LINE_1 = (
    "A traffic jam is a zipper that jammed because every tooth "
    "tried to squeeze through the slider at the same time."
)
LINE_2 = (
    "The zipper fits how cars must slide into one lane a few at a time, "
    "but it leaves out the drivers who can choose to wait and the "
    "traffic lights that tell them when to go."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
