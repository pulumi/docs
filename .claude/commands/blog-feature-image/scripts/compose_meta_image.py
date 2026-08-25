#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "cairosvg>=2.8.2",
#     "numpy>=1.24",
#     "pillow>=12.1.1",
#     "pyyaml>=6.0",
# ]
# ///
"""Compose a blog feature image from a pre-designed PNG template.

Pipeline: Load template PNG -> Place logos (or a phosphor icon) on the
template's placeholders -> Save.

The OpenGraph/social meta card is no longer composited here — it is generated
on-brand at build time from the post title + this feature image
(scripts/meta-images/blog.mjs via scripts/generate-meta-images.mjs).
"""

import argparse
import colorsys
import json
import subprocess
from io import BytesIO
from pathlib import Path


def _ensure_cairo():
    """Make the native libcairo discoverable before importing cairosvg.

    cairosvg (via cairocffi) dlopen()s the system libcairo *by leaf name*, which
    Homebrew installs outside the default dylib search path on macOS — so a bare
    `uv run` fails with a cryptic 'no library called "cairo" was found'. dyld
    only reads DYLD_FALLBACK_LIBRARY_PATH at process launch, so if cairo isn't
    already discoverable we set that var to the Homebrew lib dir and re-exec once
    (guarded against a loop). Callers no longer need to set it themselves.
    """
    import ctypes.util
    import glob
    import os
    import sys

    if ctypes.util.find_library("cairo") or os.environ.get("_CAIRO_REEXEC"):
        return
    if sys.platform != "darwin":
        return  # Linux/Windows rely on the normal loader search paths

    libdirs = []
    for pat in (
        "/opt/homebrew/lib/libcairo.2.dylib",
        "/usr/local/lib/libcairo.2.dylib",
        "/opt/homebrew/Cellar/cairo/*/lib/libcairo.2.dylib",
        "/usr/local/Cellar/cairo/*/lib/libcairo.2.dylib",
    ):
        for f in glob.glob(pat):
            libdirs.append(os.path.dirname(f))
    if not libdirs:
        return  # nothing to add; let the import fail with its own message

    existing = os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = os.pathsep.join(
        dict.fromkeys([*libdirs, *(p for p in existing.split(os.pathsep) if p)])
    )
    os.environ["_CAIRO_REEXEC"] = "1"
    os.execv(sys.executable, [sys.executable, *sys.argv])


_ensure_cairo()

import cairosvg
import numpy as np
import yaml
from PIL import Image, PngImagePlugin


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


def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]:
    """Convert a hex color string like #231F33 to an RGBA tuple."""
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255


def _rgb_to_hls_np(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Vectorized RGB → HLS matching Python colorsys conventions.

    arr: shape (H, W, 3), float32 in [0, 1].
    Returns (h, l, s) each shape (H, W), float32 in [0, 1].
    """
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    cmax = arr.max(axis=2)
    cmin = arr.min(axis=2)
    delta = cmax - cmin
    l = (cmax + cmin) / 2.0

    denom_low = np.maximum(cmax + cmin, 1e-10)
    denom_high = np.maximum(2.0 - cmax - cmin, 1e-10)
    s = np.where(
        delta < 1e-10,
        0.0,
        np.where(l <= 0.5, delta / denom_low, delta / denom_high),
    )

    safe_delta = np.where(delta < 1e-10, 1.0, delta)
    rc = (cmax - r) / safe_delta
    gc = (cmax - g) / safe_delta
    bc = (cmax - b) / safe_delta
    h = np.where(
        cmax == r, bc - gc,
        np.where(cmax == g, 2.0 + rc - bc, 4.0 + gc - rc),
    )
    h = np.where(delta < 1e-10, 0.0, (h / 6.0) % 1.0)
    return h, l, s


def _hls_to_rgb_np(h: np.ndarray, l: np.ndarray, s: np.ndarray) -> np.ndarray:
    """Vectorized HLS → RGB matching Python colorsys conventions.

    h, l, s: shape (H, W), float32 in [0, 1].
    Returns arr shape (H, W, 3), float32 in [0, 1].
    """
    m2 = np.where(l <= 0.5, l * (1.0 + s), l + s - l * s)
    m1 = 2.0 * l - m2

    def _v(hue: np.ndarray) -> np.ndarray:
        hue = hue % 1.0
        return np.where(
            hue < 1.0 / 6.0, m1 + (m2 - m1) * hue * 6.0,
            np.where(
                hue < 0.5, m2,
                np.where(
                    hue < 2.0 / 3.0, m1 + (m2 - m1) * (2.0 / 3.0 - hue) * 6.0,
                    m1,
                ),
            ),
        )

    achromatic = s < 1e-10
    r_out = np.where(achromatic, l, _v(h + 1.0 / 3.0))
    g_out = np.where(achromatic, l, _v(h))
    b_out = np.where(achromatic, l, _v(h - 1.0 / 3.0))
    return np.clip(np.stack([r_out, g_out, b_out], axis=2), 0.0, 1.0)


def tint_image(img: Image.Image, hex_color: str, mode: str = "overlay") -> Image.Image:
    """Apply a color tint to an image, preserving its alpha.

    mode="overlay" (default): replaces all pixel colors with a flat tint while
    keeping the original alpha mask — opaque areas become a solid shape of the
    tint color. Best for logos that are already single-color cutouts.

    mode="color": CSS color blend — takes H and S from the tint color and the
    Lightness from each logo pixel. Every pixel is recolored to the tint hue
    and saturation while preserving the logo's internal brightness distribution.
    Use with #C3BDFF to shift logos into Pulumi's lavender accent palette while
    keeping internal contrast.
    """
    r, g, b, _ = hex_to_rgba(hex_color)
    img = img.convert("RGBA")
    _, _, _, alpha = img.split()
    if mode == "color":
        blend_h, _, blend_s = colorsys.rgb_to_hls(
            r / 255, g / 255, b / 255)
        # Scale saturation down so darker logo pixels don't appear more vivid
        # than the tint color itself (which sits at lightness ~0.68).
        blend_s *= 0.7
        arr = np.array(img.convert("RGB"), dtype=np.float32) / 255.0
        h_px, l_px, s_px = _rgb_to_hls_np(arr)
        # Remap lightness so dark pixels are pushed up to a visible floor.
        # Maps L=0 → l_floor and L=1 → 1.0, preserving relative contrast.
        l_floor = 0.45
        l_px = l_floor + l_px * (1.0 - l_floor)
        out = _hls_to_rgb_np(
            np.full_like(h_px, blend_h),
            l_px,
            np.full_like(s_px, blend_s),
        )
        result = Image.fromarray(
            (out * 255).astype(np.uint8), "RGB").convert("RGBA")
        result.putalpha(alpha)
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
    padding: int | None = None,
) -> Image.Image:
    """Place logo SVGs centered on placeholder regions, with optional color tint."""
    img = canvas.copy()

    for i, logo_path in enumerate(logo_paths):
        if i >= len(placeholders):
            break

        ph = placeholders[i]
        ph_x, ph_y = ph["x"], ph["y"]
        ph_w, ph_h = ph["width"], ph["height"]

        if padding is None:
            # Scale padding to placeholder size (larger placeholders have bigger rounded corners)
            pad = max(20, min(ph_w, ph_h) // 6)
        else:
            pad = padding

        # Rasterize logo SVG to fit within placeholder (with padding)
        target_w = ph_w - 2 * pad
        target_h = ph_h - 2 * pad
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


def compose(config: dict, output_path: str, assets_dir: Path) -> str:
    """Feature-image composition: template PNG → logos on placeholders → save."""
    catalog = load_catalog(assets_dir)

    # 1. Load the template PNG at its natural size
    template_path = assets_dir / config["template"]
    canvas = Image.open(str(template_path)).convert("RGBA")
    canvas_w, canvas_h = canvas.size

    # 2. Place logos or a phosphor icon on the template's placeholders
    logos = config.get("logos", [])
    icon = config.get("icon")
    if logos and icon:
        raise ValueError(
            "Config sets both 'logos' and 'icon' — a template centerpiece is one or the other")
    if logos or icon:
        template_filename = Path(config["template"]).name
        template_entry = find_template(catalog, template_filename)
        if template_entry and "placeholders" in template_entry:
            if icon:
                # Solid phosphor icon, flat-tinted violet-primary (dark), rendered
                # at ~85% of the clear space (340px placeholder -> 290px icon).
                canvas = place_logos(
                    canvas, [icon], template_entry["placeholders"], assets_dir,
                    logo_tint=config.get("icon_tint", "#C3BDFF"),
                    logo_tint_mode="overlay",
                    padding=25,
                )
            else:
                canvas = place_logos(
                    canvas, logos, template_entry["placeholders"], assets_dir,
                    logo_tint=config.get("logo_tint", "#C3BDFF"),
                    logo_tint_mode=config.get("logo_tint_mode", "overlay"),
                )

    # 3. Save as PNG
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    final = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    final.paste(canvas, (0, 0), canvas if canvas.mode == "RGBA" else None)

    # Stamp a PNG Software tag so the render is positively identifiable as our
    # pipeline's output. The lint allowlist in scripts/lint/lint-markdown.js
    # accepts only this string and "Figma" — an untagged PNG is a lint failure,
    # so dropping this stamp would fail every image this script renders. Keep
    # FEATURE_IMAGE_SOFTWARE there in sync if this value changes.
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Software", "pulumi-blog-feature-image")
    final.save(str(output), "PNG", pnginfo=meta)

    return str(output)


def main():
    parser = argparse.ArgumentParser(
        description="Compose a blog feature image from a template PNG")
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
