import os

POEM = (
    "I knocked with empty hands and a borrowed name;\n"
    "the door asked nothing but my asking.\n"
    "What I was given was not the thing I named \u2014\n"
    "it was the right to knock again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
