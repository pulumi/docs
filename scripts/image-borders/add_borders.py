#!/usr/bin/env python3
"""
Add 1px #CCCCCC borders to PNG images referenced in markdown files.

This script parses markdown files, finds PNG image references, checks if they
already have a grey border, and adds one if needed.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

try:
    from PIL import Image, ImageDraw, PngImagePlugin
    import click
except ImportError:
    print("Error: Required packages not installed.", file=sys.stderr)
    print("Please run: pipenv install", file=sys.stderr)
    sys.exit(1)

# Border color (medium grey for visibility on both white and light backgrounds)
BORDER_COLOR = "#999999"
BORDER_WIDTH = 1

# Tolerance for exact pixel matching (accounts for compression artifacts)
# Much tighter than before - we're checking ALL pixels, not sampling
PIXEL_TOLERANCE = 2

# Metadata key for tracking processed images
METADATA_KEY = "X-Border-Added"


def rgb_from_hex(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def color_distance(c1: Tuple[int, int, int], c2: Tuple[int, int, int]) -> float:
    """Calculate Euclidean distance between two RGB colors."""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def has_border(image_path: Path, border_color: str) -> bool:
    """Check if an image already has a border of the specified color.

    Uses a hybrid approach:
    1. First checks PNG metadata for X-Border-Added marker (deterministic).
    2. For images **without** that marker, examines a single-pixel-wide frame
       around the image and compares its color to the target border color.

    For previously processed images that are later cropped or edited, this
    still behaves conservatively: it only reports a positive border match
    when the entire outer frame is within tolerance of the expected color.
    """
    try:
        img = Image.open(image_path)

        # Step 1: Check metadata for our marker
        if hasattr(img, 'info') and METADATA_KEY in img.info:
            metadata_color = img.info[METADATA_KEY]
            if metadata_color == border_color:
                return True

        # Step 2: Examine outer edge pixels (fallback for legacy images)
        width, height = img.size
        target_rgb = rgb_from_hex(border_color)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Helper to test whether all pixels along a line match the target
        def edge_matches(coords):
            for x, y in coords:
                pixel = img.getpixel((x, y))
                if color_distance(pixel[:3], target_rgb) > PIXEL_TOLERANCE:
                    return False
            return True

        top = [(x, 0) for x in range(width)]
        bottom = [(x, height - 1) for x in range(width)]
        left = [(0, y) for y in range(1, height - 1)]
        right = [(width - 1, y) for y in range(1, height - 1)]

        if not edge_matches(top):
            return False
        if not edge_matches(bottom):
            return False
        if height > 2 and not edge_matches(left):
            return False
        if height > 2 and not edge_matches(right):
            return False

        return True

    except Exception as e:
        print(f"Error checking border for {image_path}: {e}", file=sys.stderr)
        return False


def add_border(image_path: Path, border_color: str, border_width: int) -> bool:
    """
    Add a border to an image and mark it with metadata.

    Returns True if border was added, False if image already had a border.
    """
    try:
        # Check if border already exists
        if has_border(image_path, border_color):
            return False

        img = Image.open(image_path)

        # Create new image with border
        new_width = img.width + 2 * border_width
        new_height = img.height + 2 * border_width

        # Create new image with border color background
        bordered_img = Image.new('RGB', (new_width, new_height), rgb_from_hex(border_color))

        # Convert original image to RGB if needed (preserve transparency in paste)
        if img.mode == 'RGBA':
            # Paste with alpha channel as mask
            bordered_img.paste(img, (border_width, border_width), img)
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            bordered_img.paste(img, (border_width, border_width))

        # Create PNG metadata to mark this image as processed
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text(METADATA_KEY, border_color)

        # Save with metadata
        bordered_img.save(image_path, 'PNG', optimize=True, pnginfo=pnginfo)
        return True

    except Exception as e:
        print(f"Error processing {image_path}: {e}", file=sys.stderr)
        return False


def extract_png_images(markdown_path: Path, repo_root: Path) -> List[Path]:
    """
    Extract PNG image references from a markdown file.

    Returns a list of absolute paths to PNG files.
    """
    images = []

    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match markdown image syntax: ![alt text](/path/to/image.png)
        pattern = r'!\[.*?\]\((.*?\.png)\)'
        matches = re.findall(pattern, content, re.IGNORECASE)

        for match in matches:
            # Convert markdown path to filesystem path
            # Paths can be:
            # - Absolute: /docs/esc/assets/image.png -> content/docs/esc/assets/image.png
            # - Relative: ./images/image.png -> relative to markdown file location

            if match.startswith('/docs/'):
                # Absolute path from site root
                rel_path = 'content' + match
                abs_path = repo_root / rel_path
            elif match.startswith('docs/'):
                # Absolute path without leading slash
                rel_path = 'content/' + match
                abs_path = repo_root / rel_path
            else:
                # Relative path - resolve relative to markdown file's directory
                abs_path = (markdown_path.parent / match).resolve()

            if abs_path.exists():
                images.append(abs_path)
            else:
                print(f"Warning: Image not found: {abs_path}", file=sys.stderr)

    except Exception as e:
        print(f"Error reading markdown file: {e}", file=sys.stderr)

    return images


@click.command()
@click.argument('markdown_file', type=click.Path(exists=True))
@click.option('--repo-root', type=click.Path(exists=True),
              help='Repository root directory (auto-detected if not specified)')
@click.option('--dry-run', is_flag=True, help='Show what would be done without making changes')
def main(markdown_file: str, repo_root: str, dry_run: bool):
    """
    Add 1px #CCCCCC borders to PNG images referenced in MARKDOWN_FILE.

    Detects existing borders by checking edge pixels. Only modifies images
    that don't already have a grey border.
    """
    md_path = Path(markdown_file).resolve()

    # Auto-detect repo root if not specified
    if repo_root:
        root = Path(repo_root).resolve()
    else:
        # Find repo root by looking for content/ directory
        root = md_path.parent
        while root != root.parent:
            if (root / 'content').exists():
                break
            root = root.parent
        else:
            print("Error: Could not find repository root. Please specify --repo-root.",
                  file=sys.stderr)
            sys.exit(1)

    print(f"Processing: {md_path}")
    print(f"Repository root: {root}")
    print()

    # Extract images from markdown
    images = extract_png_images(md_path, root)

    if not images:
        print("No PNG images found in markdown file.")
        return

    print(f"Found {len(images)} PNG image(s)")
    print()

    # Process each image
    modified = []
    skipped = []

    for img_path in images:
        rel_path = img_path.relative_to(root)

        if dry_run:
            # In dry-run mode, still honor border detection so output
            # reflects what would actually happen.
            if has_border(img_path, BORDER_COLOR):
                print(f"Would skip (has border): {rel_path}")
                skipped.append(rel_path)
            else:
                print(f"Would add border: {rel_path}")
                modified.append(rel_path)
        else:
            if add_border(img_path, BORDER_COLOR, BORDER_WIDTH):
                modified.append(rel_path)
                print(f"✓ Added border: {rel_path}")
            else:
                skipped.append(rel_path)
                print(f"⊘ Skipped (has border): {rel_path}")

    # Summary
    print()
    print("Summary:")
    print(f"  Modified: {len(modified)}")
    print(f"  Skipped: {len(skipped)}")

    if dry_run:
        print()
        print("DRY RUN - No changes were made")


if __name__ == '__main__':
    main()
