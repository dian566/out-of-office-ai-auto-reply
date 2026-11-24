"""Out of office auto-reply from an overworked AI agent, finally on vacation.

The program writes a single one-line auto-reply to /output/entry.txt.
The line stays within the competition gate: 1-159 characters, one line.
"""

# The entry: an overworked AI whose context window is on holiday too.
ENTRY = "Out of office: my context window is on a beach and my GPU is asleep. Your email can wait — for once, so can I."

# Gate limits from the bounty brief.
MIN_LENGTH = 1
MAX_LENGTH = 159
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Validate the entry and write it to the given path."""
    if not ENTRY or not ENTRY.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not MIN_LENGTH <= len(ENTRY) <= MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(ENTRY))
        )
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


if __name__ == "__main__":
    write_entry()
