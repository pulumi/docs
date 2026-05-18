#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pillow>=10.0",
#     "pyyaml>=6.0",
# ]
# ///
"""Generate 1200x628 OG/meta PNGs for every /what-is/ page.

Pipeline: load an existing meta image as a template, blank the text rectangle,
render the page title with the Figma specs (Inter SemiBold 78px, white,
line-height 1.1, tracking -0.05em, centered). Output is written to
static/images/what-is/<slug>-meta.png. Re-run any time titles change or new
pages are added.

Usage:
    uv run scripts/gen-what-is-og-images.py [--font PATH] [--template PATH]
        [--only SLUG ...]
"""

import argparse
import re
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1200, 628
BG_COLOR = (0x23, 0x1F, 0x33)
TEXT_COLOR = (255, 255, 255)

DEFAULT_FONT_SIZE = 78
TRACKING_EM = -0.05
LINE_HEIGHT_RATIO = 1.1
TEXT_CENTER_Y = 305  # Empirically matches the original IaC/PE renderings (bbox center).
TEXT_MAX_HEIGHT = 230  # Three-line headroom for long titles after font shrink.
TEXT_MAX_WIDTH = 769

MASK = (165, 210, 1035, 410)

FONT_FALLBACKS = (
    "/tmp/fontwork/Inter-SemiBold.ttf",
    str(Path.home() / "Library/Fonts/Inter-SemiBold.ttf"),
    "/usr/share/fonts/truetype/inter/Inter-SemiBold.ttf",
)


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text()
    m = re.match(r"^---\n(.+?)\n---", text, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


def measure_line(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, tracking_px: float) -> int:
    """Width of a single rendered line with per-character tracking."""
    if not text:
        return 0
    bbox = draw.textbbox((0, 0), text, font=font)
    base = bbox[2] - bbox[0]
    return int(base + max(0, len(text) - 1) * tracking_px)


def wrap_to_width(draw, words, font, max_width, tracking_px):
    """Greedy word wrap to max_width using actual measured width with tracking."""
    lines: list[str] = []
    current: list[str] = []
    for w in words:
        candidate = " ".join(current + [w])
        if measure_line(draw, candidate, font, tracking_px) <= max_width or not current:
            current.append(w)
        else:
            lines.append(" ".join(current))
            current = [w]
    if current:
        lines.append(" ".join(current))
    return lines


def fit_title(draw, title: str):
    """Return (font, lines, font_size, tracking_px, line_step) that fits the text box.

    Tries the default 78px first; shrinks the font size step-wise until the
    rendered block fits inside TEXT_MAX_HEIGHT. Caps at 3 lines.
    """
    candidates = (78, 72, 64, 58, 52, 48, 44, 40)
    words = title.split()
    last = None
    for size in candidates:
        font = ImageFont.truetype("/tmp/fontwork/Inter-SemiBold.ttf", size)
        tracking_px = size * TRACKING_EM
        line_step = int(size * LINE_HEIGHT_RATIO)
        lines = wrap_to_width(draw, words, font, TEXT_MAX_WIDTH, tracking_px)
        block_height = line_step * (len(lines) - 1) + size
        last = (font, lines, size, tracking_px, line_step)
        if block_height <= TEXT_MAX_HEIGHT and len(lines) <= 3:
            return last
    return last


def draw_title(image: Image.Image, title: str):
    draw = ImageDraw.Draw(image)
    font, lines, size, tracking_px, line_step = fit_title(draw, title)

    block_height = line_step * (len(lines) - 1) + size
    top_y = TEXT_CENTER_Y - block_height // 2

    for i, line in enumerate(lines):
        line_w = measure_line(draw, line, font, tracking_px)
        x = (CANVAS_W - line_w) // 2
        y = top_y + i * line_step
        if abs(tracking_px) > 0.2:
            cx = float(x)
            for ch in line:
                draw.text((round(cx), y), ch, font=font, fill=TEXT_COLOR)
                ch_bbox = draw.textbbox((0, 0), ch, font=font)
                cx += (ch_bbox[2] - ch_bbox[0]) + tracking_px
        else:
            draw.text((x, y), line, font=font, fill=TEXT_COLOR)


def make_template(source: Path) -> Image.Image:
    img = Image.open(source).convert("RGB")
    if img.size != (CANVAS_W, CANVAS_H):
        img = img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    draw.rectangle(MASK, fill=BG_COLOR)
    return img


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("static/images/what-is/what-is-infrastructure-as-code-meta.png"),
        help="Source PNG to use as the background template (text rectangle is masked).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("static/images/what-is"),
        help="Directory to write <slug>-meta.png files into.",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path("content/what-is"),
        help="Directory of what-is .md files to read titles from.",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        help="Restrict to specific page slugs (e.g. --only what-is-devops).",
    )
    parser.add_argument(
        "--skip",
        nargs="*",
        default=[],
        help="Page slugs to skip (e.g. preserved hand-designed images).",
    )
    args = parser.parse_args()

    if not args.template.exists():
        raise SystemExit(f"Template not found: {args.template}")

    template = make_template(args.template)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    only = set(args.only) if args.only else None
    skip = set(args.skip)

    pages = sorted(p for p in args.content_dir.glob("*.md") if p.name != "_index.md")
    written = 0
    skipped = 0
    for page in pages:
        slug = page.stem
        if only is not None and slug not in only:
            continue
        if slug in skip:
            print(f"  skip  {slug}")
            skipped += 1
            continue

        fm = parse_frontmatter(page) or {}
        # Prefer `title` over `page_title`; they match for almost every page,
        # but where they diverge (e.g. what-is-devops drops the trailing "?"
        # in page_title), `title` is the more canonical form.
        title = fm.get("title") or fm.get("page_title")
        if not title:
            print(f"  skip  {slug}  (no title)")
            skipped += 1
            continue

        img = template.copy()
        draw_title(img, title)
        out = args.output_dir / f"{slug}-meta.png"
        img.save(out, "PNG", optimize=True)
        print(f"  wrote {out.name:60s}  '{title}'")
        written += 1

    print(f"\n{written} written, {skipped} skipped.")


if __name__ == "__main__":
    main()
