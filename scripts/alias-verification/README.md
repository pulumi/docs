# Alias Verification Scripts

These scripts verify that all renamed files have proper `aliases` fields in their frontmatter pointing to their old locations on `master`. This is critical for SEO and preventing broken links.

## Usage

### Step 1: Extract Renames

First, extract the list of renamed files from the current branch compared to master:

```bash
cd scripts/alias-verification
./extract-renames.sh
```

This creates:
- `renames.txt` - All renamed files (R status)
- `deletes.txt` - All deleted files (D status)

### Step 2: Verify Aliases

Run the verification script to check all renamed content files:

```bash
./verify-aliases.sh
```

This will output:
- Summary statistics
- Three log files:
  - `aliases-correct.txt` - Files with correct aliases ✓
  - `aliases-missing.txt` - Files missing the required alias ❌
  - `aliases-suspicious.txt` - Files with aliases but maybe wrong ⚠️

### Exit Codes

- **0** - All aliases verified correctly
- **1** - Issues found (check log files)

## How It Works

### Path to URL Conversion

The script converts file paths to Hugo URLs:

- `content/docs/foo/bar.md` → `/docs/foo/bar/`
- `content/docs/foo/_index.md` → `/docs/foo/`

### Alias Checking

For each renamed file, the script:
1. Reads the frontmatter
2. Extracts the `aliases` array
3. Checks if the old URL path is present
4. Categorizes as CORRECT, MISSING, or SUSPICIOUS

## Example Output

```
=== VERIFICATION SUMMARY ===
Total content files renamed: 341

✓ CORRECT:    320
❌ MISSING:    15
⚠️  SUSPICIOUS: 6

❌ ISSUES FOUND - Details in:
  ✓ aliases-correct.txt
  ❌ aliases-missing.txt
  ⚠️  aliases-suspicious.txt
```

## Workflow

1. Make file renames/moves in your branch
2. Run `./extract-renames.sh`
3. Run `./verify-aliases.sh`
4. Fix any MISSING or SUSPICIOUS files
5. Re-run `./verify-aliases.sh` until it passes (exit 0)
6. Merge your PR with confidence!
