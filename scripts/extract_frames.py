#!/usr/bin/env python3
"""Extract frames from a video every N seconds, using ffmpeg.

Usage:
  python3 scripts/extract_frames.py input.mp4 -o frames/ --interval 5
  python3 scripts/extract_frames.py input.mp4 -o frames/ --interval 2

Output:
  frames/frame_0000.jpg, frame_0001.jpg, ...
  frames/frames.csv  (time, file)

Requires ffmpeg on PATH. No frames are invented — only frames ffmpeg
actually extracts from the input file are written.
"""
import argparse
import csv
import subprocess
import sys
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description="Extract video frames every N seconds with ffmpeg.")
    p.add_argument("input", help="Input video file")
    p.add_argument("-o", "--output", default="frames", help="Output folder for frames")
    p.add_argument("--interval", type=float, default=5, help="Seconds between frames (default 5)")
    args = p.parse_args()

    inp = Path(args.input)
    out = Path(args.output)
    if not inp.exists():
        print(f"Input not found: {inp}", file=sys.stderr)
        return 1
    if args.interval <= 0:
        print("Interval must be > 0", file=sys.stderr)
        return 1
    out.mkdir(parents=True, exist_ok=True)

    # fps=1/interval extracts one frame every `interval` seconds.
    cmd = [
        "ffmpeg", "-y", "-i", str(inp),
        "-vf", f"fps=1/{args.interval}",
        str(out / "frame_%04d.jpg"),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:], file=sys.stderr)
        return r.returncode

    frames = sorted(out.glob("frame_*.jpg"))
    with open(out / "frames.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["time_sec", "file"])
        for i, fp in enumerate(frames):
            w.writerow([round(i * args.interval, 2), fp.name])
    print(f"Wrote {len(frames)} frames to {out}/ (interval {args.interval}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
