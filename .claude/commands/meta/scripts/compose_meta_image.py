#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "cairosvg>=2.8.2",
#     "pillow>=12.1.1",
# ]
# ///
"""Compose meta images from SVG assets.

Layer stack (bottom->top): Background -> Pattern -> Overlays (z-order) -> Text
"""

import argparse
import json
import os
import subprocess
import textwrap
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600


def svg_to_png(svg_path: str, width: int, height: int) -> Image.Image:
    """Rasterize an SVG file to a PIL Image at the given dimensions.

    Renders at the target width, then crops/resizes to exact height to avoid
    aspect-ratio letterboxing (e.g. 1200x628 SVGs rendered to 1200x600).
    """
    svg_path = str(svg_path)
    try:
        # Render at target width only -- let height be natural
        png_data = cairosvg.svg2png(url=svg_path, output_width=width)
    except Exception:
        result = subprocess.run(
            ["rsvg-convert", "-w", str(width), svg_path],
            capture_output=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to rasterize {svg_path}")
        png_data = result.stdout

    from io import BytesIO
    img = Image.open(BytesIO(png_data)).convert("RGBA")

    # Crop to exact target dimensions (top-aligned crop for backgrounds)
    if img.size != (width, height):
        img = img.crop((0, 0, width, height))

    return img


def apply_pattern(bg_svg_path: str, pattern_svg_path: str) -> Image.Image:
    """Compose background + pattern as a combined SVG to preserve CSS blend modes.

    Creates an intermediate SVG that embeds both as <image> elements,
    letting the SVG renderer handle mix-blend-mode natively.
    """
    import base64

    bg_data = Path(bg_svg_path).read_bytes()
    pat_data = Path(pattern_svg_path).read_bytes()
    bg_b64 = base64.b64encode(bg_data).decode()
    pat_b64 = base64.b64encode(pat_data).decode()

    combined_svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
     viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}">
  <image width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
         preserveAspectRatio="none"
         href="data:image/svg+xml;base64,{bg_b64}"/>
  <image width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}"
         preserveAspectRatio="none"
         href="data:image/svg+xml;base64,{pat_b64}"/>
</svg>"""

    from io import BytesIO
    png_data = cairosvg.svg2png(
        bytestring=combined_svg.encode(),
        output_width=CANVAS_WIDTH,
        output_height=CANVAS_HEIGHT,
    )
    return Image.open(BytesIO(png_data)).convert("RGBA")


def draw_text(
    image: Image.Image,
    content: str,
    fonts_dir: Path,
    x: int = 80,
    y: int = 200,
    font_size: int = 48,
    font_weight: str = "bold",
    color: str = "#FFFFFF",
    max_width: int = 650,
    line_spacing: int = 8,
) -> Image.Image:
    """Render text onto the image with word-wrapping."""
    img = image.copy()
    draw = ImageDraw.Draw(img)

    font_file = "Inter-Bold.ttf" if font_weight == "bold" else "Inter-Regular.ttf"
    font_path = fonts_dir / font_file
    font = ImageFont.truetype(str(font_path), font_size)

    # Word-wrap: measure words and break lines to fit max_width
    words = content.split()
    lines = []
    current_line = ""
    for word in words:
        test = f"{current_line} {word}".strip()
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    # Draw each line
    cy = y
    for line in lines:
        draw.text((x, cy), line, fill=color, font=font)
        bbox = font.getbbox(line)
        line_height = bbox[3] - bbox[1]
        cy += line_height + line_spacing

    return img


def compose(config: dict, output_path: str, assets_dir: Path) -> str:
    """Full composition pipeline: BG -> pattern -> overlays -> text -> save."""
    fonts_dir = assets_dir / "fonts"

    # 1. Background (with optional pattern)
    bg_path = str((assets_dir / config["background"]).resolve())

    if config.get("pattern"):
        pat_path = str((assets_dir / config["pattern"]).resolve())
        canvas = apply_pattern(bg_path, pat_path)
    else:
        canvas = svg_to_png(bg_path, CANVAS_WIDTH, CANVAS_HEIGHT)

    # 2. Overlays in z-order (behind first, front last)
    for overlay in config.get("overlays", []):
        svg_path = str((assets_dir / overlay["svg_path"]).resolve())
        ov_w = overlay.get("width", 300)
        ov_h = overlay.get("height", 300)

        ov_img = svg_to_png(svg_path, ov_w, ov_h)

        # Preserve aspect ratio: fit within the bounding box
        ov_img.thumbnail((ov_w, ov_h), Image.LANCZOS)

        ox = overlay.get("x", 0)
        oy = overlay.get("y", 0)
        canvas.paste(ov_img, (ox, oy), ov_img)

    # 3. Text
    if config.get("text"):
        t = config["text"]
        canvas = draw_text(
            canvas,
            content=t["content"],
            fonts_dir=fonts_dir,
            x=t.get("x", 80),
            y=t.get("y", 200),
            font_size=t.get("font_size", 48),
            font_weight=t.get("font_weight", "bold"),
            color=t.get("color", "#FFFFFF"),
            max_width=t.get("max_width", 650),
        )

    # 4. Save as PNG (flatten alpha onto white if needed, then save RGB)
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    # Flatten to RGB for final PNG
    final = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), (255, 255, 255))
    final.paste(canvas, (0, 0), canvas if canvas.mode == "RGBA" else None)
    final.save(str(output), "PNG")

    return str(output)


def main():
    parser = argparse.ArgumentParser(description="Compose a meta image from SVG assets")
    parser.add_argument("--config", required=True, help="JSON config file path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument(
        "--assets-dir",
        required=True,
        help="Base directory containing assets/ subdirs (backgrounds, patterns, mascots, icons) and fonts/",
    )
    args = parser.parse_args()

    assets_dir = Path(args.assets_dir).resolve()

    with open(args.config) as f:
        config = json.load(f)

    result = compose(config, args.output, assets_dir)
    print(f"Generated: {result}")


if __name__ == "__main__":
    main()
