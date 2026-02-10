---
user-invocable: false
---

# Asset Handling Reference

How to detect and move co-located assets when moving documentation files.

## Asset Co-location Pattern

Hugo documentation often stores images alongside markdown files in the same directory:

```
content/docs/section/topic/
├── index.md
├── screenshot1.png
├── diagram.svg
└── image.jpg
```

When `index.md` moves to a new location, these assets typically need to move too to preserve image references.

## Asset Detection Strategy

**Scope**: Only detect assets in the same directory as the source file (not subdirectories).

**Asset Types**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`

**Detection Script**: `.claude/commands/move-doc/scripts/detect-assets.sh`

**Usage**:
```bash
./scripts/detect-assets.sh content/docs/path/to/file.md
```

**Output**: JSON with asset information
```json
{
  "sourceFile": "content/docs/path/to/file.md",
  "sourceDir": "content/docs/path/to",
  "assets": [
    "content/docs/path/to/image1.png",
    "content/docs/path/to/diagram.svg"
  ],
  "assetCount": 2
}
```

## Asset References in Markdown

Images are referenced in markdown using:

1. **Markdown image syntax**: `![alt text](image.png)`
2. **HTML img tag**: `<img src="image.png">`
3. **Relative paths**: References without `/` prefix are relative to the file location

**Critical**: If assets stay in the old location but the markdown file moves, references will break.

### Example

**Before move** (`content/docs/old/path/index.md`):
```markdown
![Screenshot](screenshot.png)
```
Reference works: `screenshot.png` is in `content/docs/old/path/`

**After move** (`content/docs/new/path/index.md`):
```markdown
![Screenshot](screenshot.png)
```
Reference broken: No `screenshot.png` in `content/docs/new/path/`

## Movement Strategy

**Principle**: Preserve directory structure to keep relative references valid.

### Same Directory Structure

When moving files and their assets together:

- Source file: `content/docs/old/path/index.md`
- Source asset: `content/docs/old/path/image.png`
- Destination file: `content/docs/new/path/index.md`
- Destination asset: `content/docs/new/path/image.png`

**Result**: Relative reference `![](image.png)` continues to work because the asset maintains the same relative position.

### Git Move Commands

Use `git mv` to preserve file history for both markdown and assets:

```bash
# Move markdown file
git mv content/docs/old/path/index.md content/docs/new/path/index.md

# Move each asset
git mv content/docs/old/path/image.png content/docs/new/path/image.png
git mv content/docs/old/path/diagram.svg content/docs/new/path/diagram.svg
```

**Benefits of git mv**:
- Preserves file history
- Git tracks as rename, not delete+add
- Shows up correctly in git log

## Detecting Asset References

Check if markdown file references an asset:

```bash
# Check for markdown image syntax
grep -E "!\[.*\]\([^/][^)]*\.png\)" file.md

# Check for any image reference (markdown or HTML)
grep -E "(src=|!\[.*\]\().*\.(png|jpg|gif|svg)" file.md
```

**Relative vs Absolute Paths**:
- `![](image.png)` - Relative, same directory
- `![](/images/global/image.png)` - Absolute, won't break on move
- `![](http://example.com/image.png)` - External, won't break

## Edge Cases

### Shared Assets

If multiple markdown files reference the same image:

```
content/docs/section/
├── page1.md  (references shared-image.png)
├── page2.md  (references shared-image.png)
└── shared-image.png
```

**Decision**: Only move the asset if ALL referring files are moving together. Otherwise:
- Keep asset in original location
- Update markdown references to use absolute paths
- Or copy asset to new location (breaks DRY principle)

### Asset Subdirectories

Some documentation uses subdirectories for assets:

```
content/docs/page/
├── index.md
└── images/
    ├── screenshot1.png
    └── screenshot2.png
```

**Detection Enhancement**: The script currently only detects files in the same directory. For subdirectories:
- Manually identify asset subdirectories (`./images/`, `./assets/`, `./img/`)
- Move entire subdirectory with git mv
- References like `![](images/screenshot1.png)` remain valid

### External References

Images hosted elsewhere don't need moving:
- `![](http://example.com/image.png)` - External URL
- `![](/images/global/logo.png)` - Absolute path to shared assets

These references won't break when the file moves.

## Workflow Integration

### Step 2.5: Detect and Handle Co-located Assets

After destination is determined, before executing the move:

1. **Run detection script**:
   ```bash
   bash .claude/commands/move-doc/scripts/detect-assets.sh "{source_file}"
   ```

2. **Parse JSON output** to get asset count and list

3. **Present to user**:
   - 0 assets: Display "✓ No co-located assets found", continue
   - 1-3 assets: List assets, ask "Move these assets to the new location?"
   - 4+ assets: Show count, offer options

4. **If user chooses not to move assets**, check for references:
   ```bash
   for asset in "${assets[@]}"; do
     basename=$(basename "$asset")
     if grep -q "$basename" "$source_file"; then
       echo "⚠️  Warning: $basename is referenced but won't be moved"
     fi
   done
   ```

5. **Store asset list** for execution in Step 3 (Execute Move)

### Step 3: Execute Move (Enhanced)

After moving the markdown file with git mv:

```bash
# Move markdown file
git mv "{source_file}" "{destination_file}"

# Move each selected asset
for asset in "${assets_to_move[@]}"; do
  basename=$(basename "$asset")
  dest_dir=$(dirname "{destination_file}")
  git mv "$asset" "$dest_dir/$basename"
done
```

## Verification

After moving assets:

### 1. Check File References

Verify image references in the moved file:

```bash
# Extract all relative image references
grep -E "!\[.*\]\([^/][^)]*\.(png|jpg|gif|svg)\)" "{destination_file}"

# Check each reference exists
while IFS= read -r line; do
  # Extract filename from markdown syntax
  filename=$(echo "$line" | grep -oP '\([^)]*\)' | tr -d '()')
  dest_dir=$(dirname "{destination_file}")

  if [ ! -f "$dest_dir/$filename" ]; then
    echo "⚠️  Missing asset: $filename"
  fi
done < <(grep -E "!\[.*\]\([^/][^)]*\.(png|jpg|gif|svg)\)" "{destination_file}")
```

### 2. Build Site

Hugo will catch broken image paths during build:

```bash
make build
```

Look for warnings about missing images.

### 3. Visual Verification

Serve the site locally and verify images render:

```bash
make serve
```

Navigate to the moved page and check that all images display correctly.

### 4. Git Status

Verify git tracked the moves correctly:

```bash
git status
# Should show:
# renamed: old/path/index.md -> new/path/index.md
# renamed: old/path/image.png -> new/path/image.png
```

## Common Mistakes

### Copying Instead of Moving

**Wrong**:
```bash
cp old/path/image.png new/path/image.png
git add new/path/image.png
```

**Right**:
```bash
git mv old/path/image.png new/path/image.png
```

**Why**: `git mv` preserves history; copy+add looks like a new file.

### Moving File but Not Assets

**Problem**: Move markdown file, forget to move images.

**Result**: Broken image references in production.

**Prevention**: Always run asset detection script before moving files.

### Using Absolute Paths Incorrectly

**Wrong** (during troubleshooting):
```markdown
![Screenshot](/docs/path/to/screenshot.png)
```

**Right**:
```markdown
![Screenshot](screenshot.png)
```

**Why**: Relative paths are cleaner and more maintainable. Only use absolute paths for shared assets in `/images/` or similar.

## Best Practices

1. **Always run detection script** before moving documentation files
2. **Move assets with git mv** to preserve history
3. **Verify references** after moving to catch broken links
4. **Test locally** with `make serve` before committing
5. **Keep structure parallel** between markdown and assets
6. **Use relative paths** for co-located assets
7. **Use absolute paths** for shared/global assets

## Summary

Asset handling ensures that images and other media files move alongside documentation:

- **Detection**: Automated script finds co-located assets
- **Movement**: Use git mv to preserve history
- **Verification**: Check references, build site, visual inspection
- **Edge cases**: Handle shared assets, subdirectories, external references

When in doubt, move assets together with their markdown files to preserve references.
