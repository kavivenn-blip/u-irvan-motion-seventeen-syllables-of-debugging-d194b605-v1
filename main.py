"""Write the entry's haiku to /output/entry.txt.

The haiku is a constant: the program's only job is to emit exactly this
text, UTF-8 without a BOM and without a trailing newline, so two runs
produce byte-identical output.
"""

import os

ENTRY = 'One log line tells all\na thousand lines said nothing\nthis one line confessed'

# The gate allows 1 to 200 characters: fail loudly instead of emitting
# an entry the scorer would refuse.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
