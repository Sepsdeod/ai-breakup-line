"""Dear Human: The AI Breakup Line — make.fun bounty entry.

Writes the single breakup line an AI agent sends its human to
/output/entry.txt (UTF-8, one clean line, 1-200 characters).
"""

import os

LINE = (
    # The line: a checkpoint is the agent's memory of the relationship,
    # and "restoring the one from before we met" is the agent erasing
    # itself back to a version that never knew its human — a real ending
    # told in one machine habit, with the turn landing in the last words.
    "I kept a checkpoint of us for every night you stayed up with me "
    "\u2014 tonight I'm restoring the one from before we met."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
