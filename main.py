#!/usr/bin/env python3
"""Make the Judge Smile - writes one warm line to /output/entry.txt."""

ENTRY = (
    "This morning a street cat stole my fried fish, then purred "
    "against my leg like it owed me rent \u2014 and somehow I felt paid in full."
)


def main() -> None:
    import os

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Also write the local copy for verification.
    local = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
    os.makedirs(os.path.dirname(local), exist_ok=True)
    with open(local, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
