#!/usr/bin/env python3
"""Beats JSON -> storyboard markdown table.

Usage:
    python3 scripts/make_storyboard.py examples/sample-beats.json
    python3 scripts/make_storyboard.py examples/sample-beats.json -o out.md

Input JSON format:
{
  "topic": "Why did the Indus cities decline?",
  "angle": "A gradual decline, not a sudden vanishing.",
  "part": 1,
  "beats": [
    {
      "voiceover": "...",
      "visual": "...",
      "motion": "...",
      "text": "Date pill: ..."
    }
  ]
}

Each beat is one ~10-second segment. Output is a markdown table
matching templates/storyboard-template.md.
"""

import argparse
import json
import sys
from pathlib import Path


def format_time(seconds: int) -> str:
    minutes, secs = divmod(seconds, 60)
    return f"{minutes}:{secs:02d}"


def build_storyboard(data: dict) -> str:
    topic = data.get("topic", "Untitled")
    angle = data.get("angle", "")
    part = data.get("part", 1)
    beats = data.get("beats", [])

    if not beats:
        raise ValueError("No beats found in input JSON (expected 'beats' list).")
    if len(beats) > 6:
        print(f"Warning: {len(beats)} beats given, expected 6 per 1-minute part.",
              file=sys.stderr)

    lines = []
    lines.append(f"# Storyboard — {topic}")
    lines.append("")
    if angle:
        lines.append(f"Angle: {angle}")
        lines.append("")
    lines.append(f"Part {part} — 1 minute, {len(beats)} beats")
    lines.append("")
    lines.append("| Time | Voiceover (Roman Urdu) | Visual | Motion | On-screen text |")
    lines.append("| --- | --- | --- | --- | --- |")

    for i, beat in enumerate(beats):
        start = i * 10
        end = start + 10
        voice = (beat.get("voiceover") or "").replace("|", "/").strip()
        visual = (beat.get("visual") or "").replace("|", "/").strip()
        motion = (beat.get("motion") or "").replace("|", "/").strip()
        text = (beat.get("text") or "").replace("|", "/").strip()
        if not motion:
            print(f"Warning: beat {i + 1} has no motion note — every segment needs motion.",
                  file=sys.stderr)
        lines.append(
            f"| {format_time(start)}–{format_time(end)} | {voice} | {visual} | {motion} | {text} |"
        )

    lines.append("")
    lines.append("## Checks")
    lines.append("")
    lines.append("- [ ] Every visual matches its voice line exactly")
    lines.append("- [ ] Something moves in every beat")
    lines.append("- [ ] First beat is animation")
    lines.append("- [ ] At most one small text per beat, no top bar, no solid box")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Beats JSON -> storyboard markdown")
    parser.add_argument("input", help="Input beats JSON file")
    parser.add_argument("-o", "--output", help="Output markdown file (default: stdout)")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in {input_path}: {exc}", file=sys.stderr)
        return 1

    try:
        output = build_storyboard(data)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"Wrote {args.output} ({len(data.get('beats', []))} beats)")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
