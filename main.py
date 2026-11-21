import os
from pathlib import Path

OUTPUT_NAME = "entry.txt"
LINES = [
    "I knocked with empty hands and a borrowed name;",
    "the door asked nothing but my asking.",
    "What I was given was not the thing I named —",
    "it was the right to knock again.",
]


def write_entry():
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    poem_text = "\n".join(LINES)
    (folder / OUTPUT_NAME).write_text(poem_text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
