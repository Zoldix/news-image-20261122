#!/usr/bin/env python3
"""Entry for make.fun news-image-20261122: copy the front page to /output.

The image (entry.png, 1024x1024, hand-drawn with Pillow by the builder)
sums up the world's news of Sunday 22 November 2026: 32 dated stories
across 7 regions, led by the COP31 deal taking shape in Antalya.
Standard library only; deterministic: the same bytes every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(SRC, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_SIGNATURE):
        print("entry.png: bad PNG signature", file=sys.stderr)
        return 1
    if len(data) > 1048576:
        print("entry.png: over 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
