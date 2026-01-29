---
description: Add 1px grey borders to PNG images in a documentation file.
---

# Usage

`/add-borders <doc-file-path>`

Analyze PNG images referenced in the specified markdown file at {{arg}} and add 1px #999999 (medium grey) borders to any images that don't already have them. This improves visual clarity and consistency of screenshots and diagrams in documentation.

---

## Process

### 1. Verify prerequisites

Before running the border tool, ensure dependencies are installed:

```bash
cd scripts/image-borders && pipenv install
```

If this is the first run or if Pillow is not yet installed, the installation will complete automatically.

### 2. Run the border addition tool

Execute the Python script with the provided documentation file:

```bash
pipenv run python scripts/image-borders/add_borders.py {{arg}}
```

The script will:

- Parse the markdown file to find all PNG image references
- Check each image's edge pixels to detect existing borders
- Add a 1px #999999 border to images that don't have one
- Skip images that already have a grey border (within tolerance)
- Display a summary of modified and skipped images

### 3. Review the results

The script outputs:

- **Modified**: Images that received new borders
- **Skipped**: Images that already had borders

Example output:

```output
Found 3 PNG image(s)

✓ Added border: content/docs/esc/assets/create-environment.png
✓ Added border: content/docs/esc/assets/editor-before-save.png
⊘ Skipped (has border): content/docs/esc/assets/editor-after-save.png

Summary:
  Modified: 2
  Skipped: 1
```

### 4. Verify the changes

After borders are added:

1. View the modified images to ensure borders look correct
2. Check that border width and color (#CCCCCC) are appropriate
3. Verify the images still display correctly in the documentation

You can preview the documentation locally:

```bash
make serve
```

Then navigate to the affected page at http://localhost:1313

### 5. Commit the changes (if appropriate)

If the borders improve the documentation quality, commit the modified images:

```bash
git add <image-files>
git commit -m "Add 1px borders to documentation images for visual clarity"
```

---

## Options

The script supports additional options:

- `--dry-run` - Show what would be done without making changes
- `--repo-root <path>` - Specify repository root (auto-detected by default)

Example with dry run:

```bash
pipenv run python scripts/image-borders/add_borders.py {{arg}} --dry-run
```

---

## Notes

- Do not apply borders to `meta.png` images used for social sharing
- The script uses edge pixel analysis to detect existing borders with 80% confidence threshold
- Handles RGBA images (preserves transparency)
- Uses #999999 (medium grey) for visibility on both white and light backgrounds
- Only processes PNG files (ignores JPG, GIF, SVG, etc.)
- Modifies images in place (use git to revert if needed)
