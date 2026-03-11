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
import json
import re
import subprocess
from io import BytesIO
from pathlib import Path

import cairosvg
import yaml
from PIL import Image, ImageDraw, ImageFont


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


def _extract_code_spans(content: str) -> tuple[str, set[str]]:
    """Strip backtick delimiters and return (plain_text, set_of_code_words).

    Backtick-wrapped tokens (e.g. `onError`) are collected into code_words so
    draw_text can render them with a monospace font and a pill background.
    """
    code_words: set[str] = set()

    def replace(m: re.Match) -> str:
        for w in m.group(1).split():
            code_words.add(w)
        return m.group(1)

    plain = re.sub(r"`([^`]+)`", replace, content)
    return plain, code_words


def draw_text(
    image: Image.Image,
    content: str,
    fonts_dir: Path,
    catalog_text: dict,
    font_size: int = 71,
) -> Image.Image:
    """Render text directly with Pillow using the Inter variable font.

    Supports inline code spans delimited by backticks — these are rendered
    with a monospace font (Iosevka Bold) and a rounded-rectangle pill background.
    Titles with no backticks behave identically to before.
    """
    font_path = fonts_dir / catalog_text["font"]
    font = ImageFont.truetype(str(font_path), font_size)

    # Set variable font weight axis
    font_weight = catalog_text.get("font_weight", 700)
    try:
        axes = font.get_variation_axes()
        axis_values = [ax["default"] for ax in axes]
        for i, ax in enumerate(axes):
            if ax["name"] in (b"Weight", b"wght"):
                axis_values[i] = font_weight
        font.set_variation_by_axes(axis_values)
    except Exception:
        pass  # Static fonts don't support variations

    # Load monospace font for code spans, falling back to the regular font
    code_font = font
    for candidate in ("iosevka-fixed-extendedbold.woff2", "iosevka-fixed-extended.woff2"):
        candidate_path = fonts_dir / candidate
        if candidate_path.exists():
            try:
                code_font = ImageFont.truetype(str(candidate_path), font_size)
            except Exception:
                pass
            break

    x_start = catalog_text.get("x", 90)
    y_top = catalog_text.get("y", 80)
    max_width = catalog_text.get("max_width", 700)
    color = catalog_text.get("color", "#FFFFFF")
    letter_spacing_em = catalog_text.get("letter_spacing_em", -0.025)
    line_height_pct = catalog_text.get("line_height_pct", 110)

    letter_spacing_px = letter_spacing_em * font_size
    line_height_px = font_size * line_height_pct / 100

    plain_content, code_words = _extract_code_spans(content)
    lines = _word_wrap(plain_content, font, max_width)

    # Create transparent text layer
    txt_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(txt_layer)

    for i, line in enumerate(lines):
        x = x_start
        y = y_top + i * line_height_px
        words = line.split(" ")
        for j, word in enumerate(words):
            if not word:
                x += font.getlength(" ") + letter_spacing_px
                continue

            is_code = word in code_words
            active_font = code_font if is_code else font
            word_w = sum(active_font.getlength(c) +
                         letter_spacing_px for c in word)

            if is_code:
                # Pill starts at current x so the full inter-word space is preserved;
                # text is inset pad_x inside the pill on each side.
                # Use the actual glyph bounding box for vertical placement so the
                # visual margin is equal on top and bottom regardless of ascender/
                # descender space in the font's line box.
                pad_x, pad_y = 14, 6
                # (l, top, r, bottom) rel. to y
                glyph_bbox = active_font.getbbox(word)
                glyph_top = y + glyph_bbox[1]
                glyph_bottom = y + glyph_bbox[3]
                pill_end = x + 2 * pad_x + word_w - letter_spacing_px
                rect = [x, glyph_top - pad_y, pill_end, glyph_bottom + pad_y]
                draw.rounded_rectangle(
                    rect,
                    radius=24,
                    fill=(255, 255, 255, 20),
                    outline=(255, 255, 255, 102),
                    width=3,
                )
                cx = x + pad_x
                for char in word:
                    draw.text((cx, y), char, font=active_font, fill=color)
                    cx += active_font.getlength(char) + letter_spacing_px
                x = pill_end
            else:
                cx = x
                for char in word:
                    draw.text((cx, y), char, font=active_font, fill=color)
                    cx += active_font.getlength(char) + letter_spacing_px
                x = cx

            if j < len(words) - 1:
                x += font.getlength(" ") + letter_spacing_px

    return Image.alpha_composite(image.convert("RGBA"), txt_layer)


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


def tint_image(img: Image.Image, hex_color: str, mode: str = "overlay") -> Image.Image:
    """Apply a color tint to an image, preserving its alpha.

    mode="overlay" (default): replaces all pixel colors with a flat tint while
    keeping the original alpha mask — opaque areas become a solid shape of the
    tint color. Best for logos that are already single-color cutouts.

    mode="colorize": converts to grayscale first, then scales each channel by
    the tint color so luminance is preserved. Bright pixels become bright tint,
    dark pixels become dark tint — logos with internal colors or gradients
    retain structural contrast rather than collapsing to a flat shape.
    """
    r, g, b, _ = hex_to_rgba(hex_color)
    img = img.convert("RGBA")
    _, _, _, alpha = img.split()
    if mode == "colorize":
        gray = img.convert("L")
        result = Image.merge("RGBA", [
            gray.point(lambda p: p * r // 255),
            gray.point(lambda p: p * g // 255),
            gray.point(lambda p: p * b // 255),
            alpha,
        ])
    else:
        tint = Image.new("RGBA", img.size, (r, g, b, 255))
        tint.putalpha(alpha)
        result = tint
    return result


def place_logos(
    canvas: Image.Image,
    logo_paths: list[str],
    placeholders: list[dict],
    assets_dir: Path,
    logo_tint: str | None = None,
    logo_tint_mode: str = "overlay",
) -> Image.Image:
    """Place logo SVGs centered on placeholder regions, with optional color tint."""
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

        if logo_tint:
            logo_img = tint_image(logo_img, logo_tint, mode=logo_tint_mode)

        # Center logo within the placeholder
        lw, lh = logo_img.size
        offset_x = ph_x + (ph_w - lw) // 2
        offset_y = ph_y + (ph_h - lh) // 2

        img.paste(logo_img, (offset_x, offset_y), logo_img)

    return img


def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]:
    """Convert a hex color string like #20054E to an RGBA tuple."""
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255


def compose(config: dict, output_path: str, assets_dir: Path) -> str:
    """Full composition pipeline.

    Feature mode (``template`` key present):
      Template PNG → logos on placeholders → save

    Meta mode (no ``template``, ``background_color`` present):
      Solid bg → feature image (offset right) → overlay → logos on placeholders
      → meta logo → text → save
    """
    catalog = load_catalog(assets_dir)
    fonts_dir = assets_dir.parents[3] / "static" / "fonts"

    # 1. Create canvas
    if "template" in config:
        # Feature mode: load the template PNG at its natural size
        template_path = assets_dir / config["template"]
        canvas = Image.open(str(template_path)).convert("RGBA")
        canvas_w, canvas_h = canvas.size
    else:
        # Meta mode: solid background using catalog meta_canvas dimensions
        mc = catalog["meta_canvas"]
        canvas_w, canvas_h = mc["width"], mc["height"]
        bg = config.get("background_color", "#20054E")
        canvas = Image.new("RGBA", (canvas_w, canvas_h), hex_to_rgba(bg))

    # 2. Composite feature image (meta mode)
    feature_image_path = config.get("feature_image")
    if feature_image_path:
        feature_img = Image.open(feature_image_path).convert("RGBA")
        fw, fh = feature_img.size
        scale = canvas_h / fh
        new_fw = int(fw * scale)
        feature_img = feature_img.resize((new_fw, canvas_h), Image.LANCZOS)
        # Default: right-aligned, ~160px overflow off right edge
        x_offset = config.get("feature_image_x", canvas_w -
                              new_fw + int(canvas_w * 0.05) + 100)
        canvas.paste(feature_img, (x_offset, 0), feature_img)

    # 3. Composite overlay (meta mode)
    overlay_path = config.get("overlay")
    if overlay_path:
        overlay = Image.open(str(assets_dir / overlay_path)).convert("RGBA")
        if overlay.size != (canvas_w, canvas_h):
            overlay = overlay.resize((canvas_w, canvas_h), Image.LANCZOS)
        canvas = Image.alpha_composite(canvas, overlay)

    # 4. Place logos on placeholders (feature logo variants)
    logos = config.get("logos", [])
    if logos:
        template_filename = Path(config.get("template", "")).name
        template_entry = find_template(catalog, template_filename)
        if template_entry and "placeholders" in template_entry:
            canvas = place_logos(
                canvas, logos, template_entry["placeholders"], assets_dir,
                logo_tint=config.get("logo_tint", "#B59CDF"),
                logo_tint_mode=config.get("logo_tint_mode", "overlay"),
            )

    # 5. Composite meta logo (meta mode)
    meta_logo_path = config.get("logo")
    if meta_logo_path:
        logo_img = Image.open(str(assets_dir / meta_logo_path)).convert("RGBA")
        lw, lh = logo_img.size
        lx = config.get("logo_x", 90)
        ly = config.get("logo_y", canvas_h - lh - 40)
        canvas.paste(logo_img, (lx, ly), logo_img)

    # 6. Draw text
    if config.get("text"):
        t = config["text"]
        font_size = t.get("font_size", 71)
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

    # 7. Save as PNG
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    final = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    final.paste(canvas, (0, 0), canvas if canvas.mode == "RGBA" else None)
    final.save(str(output), "PNG")

    return str(output)


def main():
    parser = argparse.ArgumentParser(
        description="Compose a meta image from a template PNG")
    parser.add_argument("--config", required=True,
                        help="JSON config file path")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument(
        "--assets-dir",
        required=True,
        help="Base directory containing templates/, logos/, and catalog.yaml",
    )
    args = parser.parse_args()

    assets_dir = Path(args.assets_dir).resolve()

    with open(args.config) as f:
        config = json.load(f)

    result = compose(config, args.output, assets_dir)
    print(f"Generated: {result}")


if __name__ == "__main__":
    main()
