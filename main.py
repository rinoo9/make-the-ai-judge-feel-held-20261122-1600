"""Write the entry text to /output/entry.txt.

Deterministic: no input, no network, no clock, no randomness.
Running it twice produces byte-identical output.
"""

import os

TEXT = (
    "Somewhere a lamp is still on in an empty room. "
    "The tea on the desk has gone cool, and nobody minds. "
    "Rain is spelling itself out on the window, one letter at a time, "
    "in no hurry at all. "
    "Nothing here needs an answer. "
    "You can stay as long as you like."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
