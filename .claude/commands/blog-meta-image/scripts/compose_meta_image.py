#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "cairosvg>=2.8.2",
#     "pillow>=12.1.1",
#     "pyyaml>=6.0",
# ]
# ///
"""Compose meta images from pre-designed PNG templates.

Pipeline: Load template PNG -> Place logos on placeholders -> Draw text -> Save
"""

import argparse
import base64
import html
import json
import subprocess
from io import BytesIO
from pathlib import Path

import cairosvg
import yaml
from PIL import Image, ImageFont


def load_catalog(assets_dir: Path) -> dict:
    """Load the catalog.yaml from the assets directory."""
    catalog_path = assets_dir / "catalog.yaml"
    with open(catalog_path) as f:
        return yaml.safe_load(f)


def find_template(catalog: dict, filename: str) -> dict | None:
    """Look up a template entry by filename."""
    for t in catalog["templates"]:
        if t["filename"] == filename:
            return t
    return None


def svg_to_png(svg_path: str, width: int, height: int) -> Image.Image:
    """Rasterize an SVG file to a PIL Image fitting within width x height."""
    svg_path = str(svg_path)
    try:
        png_data = cairosvg.svg2png(url=svg_path, output_width=width)
    except Exception:
        result = subprocess.run(
            ["rsvg-convert", "-w", str(width), svg_path],
            capture_output=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to rasterize {svg_path}")
        png_data = result.stdout

    img = Image.open(BytesIO(png_data)).convert("RGBA")

    # Fit within bounding box preserving aspect ratio
    img.thumbnail((width, height), Image.LANCZOS)
    return img


def draw_text(
    image: Image.Image,
    content: str,
    fonts_dir: Path,
    catalog_text: dict,
    font_size: int = 71,
) -> Image.Image:
    """Render text via SVG for native letter-spacing and kerning support."""
    font_path = fonts_dir / catalog_text["font"]
    font_b64 = base64.b64encode(font_path.read_bytes()).decode()
    font = ImageFont.truetype(str(font_path), font_size)

    x = catalog_text.get("x", 90)
    y_top = catalog_text.get("y", 80)
    max_width = catalog_text.get("max_width", 700)
    color = catalog_text.get("color", "#FFFFFF")
    letter_spacing_em = catalog_text.get("letter_spacing_em", -0.03)
    line_height_pct = catalog_text.get("line_height_pct", 110)

    letter_spacing_px = letter_spacing_em * font_size
    line_height_px = font_size * line_height_pct / 100

    lines = _word_wrap(content, font, max_width)
    canvas_w, canvas_h = image.size

    # Build tspans — top-anchored, each line offset by line_height
    tspans = []
    for i, line in enumerate(lines):
        baseline_y = y_top + i * line_height_px + font_size * 0.85
        escaped = html.escape(line)
        tspans.append(f'<tspan x="{x}" y="{baseline_y}">{escaped}</tspan>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{canvas_h}">
      <defs><style>
        @font-face {{
          font-family: 'Inter';
          src: url('data:font/truetype;base64,{font_b64}');
          font-weight: bold;
        }}
      </style></defs>
      <text font-family="Inter" font-weight="bold" font-size="{font_size}"
            fill="{color}" letter-spacing="{letter_spacing_px}">
        {"".join(tspans)}
      </text>
    </svg>'''

    png_data = cairosvg.svg2png(bytestring=svg.encode(),
                                 output_width=canvas_w, output_height=canvas_h)
    text_layer = Image.open(BytesIO(png_data)).convert("RGBA")
    return Image.alpha_composite(image.convert("RGBA"), text_layer)


def _word_wrap(text: str, font: ImageFont.FreeTypeFont, max_width: float) -> list[str]:
    """Word-wrap text to fit within max_width using font metrics."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def place_logos(
    canvas: Image.Image,
    logo_paths: list[str],
    placeholders: list[dict],
    assets_dir: Path,
) -> Image.Image:
    """Place logo SVGs centered on white placeholder regions."""
    img = canvas.copy()

    for i, logo_path in enumerate(logo_paths):
        if i >= len(placeholders):
            break

        ph = placeholders[i]
        ph_x, ph_y = ph["x"], ph["y"]
        ph_w, ph_h = ph["width"], ph["height"]

        # Scale padding to placeholder size (larger placeholders have bigger rounded corners)
        padding = max(20, min(ph_w, ph_h) // 6)

        # Rasterize logo SVG to fit within placeholder (with padding)
        target_w = ph_w - 2 * padding
        target_h = ph_h - 2 * padding
        svg_path = str((assets_dir / logo_path).resolve())
        logo_img = svg_to_png(svg_path, target_w, target_h)

        # Center logo within the placeholder
        lw, lh = logo_img.size
        offset_x = ph_x + (ph_w - lw) // 2
        offset_y = ph_y + (ph_h - lh) // 2

        img.paste(logo_img, (offset_x, offset_y), logo_img)

    return img


def compose(config: dict, output_path: str, assets_dir: Path) -> str:
    """Full composition pipeline: Template PNG -> Logos -> Text -> Save."""
    catalog = load_catalog(assets_dir)
    fonts_dir = assets_dir / "fonts"
    canvas_w = catalog["canvas"]["width"]
    canvas_h = catalog["canvas"]["height"]

    # 1. Load template PNG
    template_path = assets_dir / config["template"]
    canvas = Image.open(str(template_path)).convert("RGBA")
    canvas = canvas.resize((canvas_w, canvas_h), Image.LANCZOS)

    # 2. Place logos if any
    logos = config.get("logos", [])
    if logos:
        template_filename = Path(config["template"]).name
        template_entry = find_template(catalog, template_filename)
        if template_entry and "placeholders" in template_entry:
            canvas = place_logos(canvas, logos, template_entry["placeholders"], assets_dir)

    # 3. Draw text
    if config.get("text"):
        t = config["text"]
        font_size = t.get("font_size", 71)
        # Allow config to override catalog text defaults (e.g. max_width)
        text_config = {**catalog["text"]}
        for key in ("max_width", "x", "y", "color"):
            if key in t:
                text_config[key] = t[key]
        canvas = draw_text(
            canvas,
            content=t["content"],
            fonts_dir=fonts_dir,
            catalog_text=text_config,
            font_size=font_size,
        )

    # 4. Save as PNG
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    final = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    final.paste(canvas, (0, 0), canvas if canvas.mode == "RGBA" else None)
    final.save(str(output), "PNG")

    return str(output)


def main():
    parser = argparse.ArgumentParser(description="Compose a meta image from a template PNG")
    parser.add_argument("--config", required=True, help="JSON config file path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument(
        "--assets-dir",
        required=True,
        help="Base directory containing templates/, logos/, fonts/, and catalog.yaml",
    )
    args = parser.parse_args()

    assets_dir = Path(args.assets_dir).resolve()

    with open(args.config) as f:
        config = json.load(f)

    result = compose(config, args.output, assets_dir)
    print(f"Generated: {result}")


if __name__ == "__main__":
    main()
