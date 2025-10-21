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
python3 verify-aliases.py
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

## Fixing Issues

If the verification script finds MISSING or SUSPICIOUS files:

```bash
# Generate fixes for all issues
python3 generate-fixes.py

# Review the sample fixes shown, then apply
python3 apply-fixes.py

# Re-verify to confirm 100% correct
python3 verify-aliases.py
```

## Workflow

1. Make file renames/moves in your branch
2. Run `./extract-renames.sh`
3. Run `python3 verify-aliases.py`
4. If issues found, use `generate-fixes.py` and `apply-fixes.py`
5. Re-run `python3 verify-aliases.py` until it passes (exit 0)
6. Merge your PR with confidence!

---

## Comprehensive Historical Verification

The scripts above check **branch-level changes** (current branch vs master). However, they can miss **pre-reorg moves** - files that were moved on master before your branch was created, or multi-hop moves (A→B→C where only B is aliased).

### When to Use Historical Verification

Use these scripts when:
- You've completed a major documentation reorganization
- You want to ensure ALL historical paths have aliases (not just recent branch changes)
- You're investigating reports of missing aliases that the branch verification missed

### Comprehensive Verification Workflow

#### Step 1: Verify All Historical Aliases

```bash
cd scripts/alias-verification
python3 verify-all-historical-aliases.py
```

This script:
- Checks the **complete git history** of every file (limited to past 6 months)
- Uses `git log --follow -M30% origin/master` to track all historical paths
- **Only checks master branch** - ignores development branches that were never merged/published
- **30% similarity detection** catches files that were significantly rewritten during moves (e.g., documentation revamps)
- Checks both frontmatter aliases AND S3 redirect files (`scripts/redirects/*.txt`)
- Identifies files missing any historical alias

Output files:
- `historical-aliases-missing.txt` - Files with missing historical aliases ❌
- `historical-aliases-correct.txt` - Files with complete coverage ✓
- `historical-aliases-report.txt` - Detailed analysis with git history

#### Step 2: Generate Fixes

```bash
python3 generate-historical-fixes.py
```

This script:
- Parses the missing aliases log
- Reads current aliases from each file
- Generates a combined list of all aliases (existing + missing)
- Outputs `historical-fixes.json` with the complete fix data

#### Step 3: Apply Fixes

```bash
python3 apply-historical-fixes.py
```

This script:
- Reads `historical-fixes.json`
- Updates each file's frontmatter to add missing aliases
- Prompts for confirmation before modifying files
- Reports success/failure for each file

**⚠️ WARNING**: This modifies files in place. Make sure to commit any important changes first!

#### Step 3.5: Review for False Positives (IMPORTANT)

Before committing the changes, **you must review them for false positives**. The 30% similarity detection can occasionally match unrelated files that happen to have similar content patterns.

```bash
git diff
```

**Common false positive patterns to watch for:**

1. **Unrelated file replacements**: Files with similar names but completely different purposes
   - Example: `doppler.md` matched with historical path `infisical.md` (different products)
   - Example: CLI commands that were never actually renamed (e.g., `pulumi_project` ← `pulumi_env_init`)

2. **Content rewrites that aren't renames**: Files that were deleted and recreated with new content
   - Low similarity can match files that share some boilerplate but are fundamentally different

3. **Development-only paths**: Should be rare now that we only check master, but verify paths make sense

**How to remove false positive aliases:**

If you find an incorrect alias, simply edit the file and remove it from the `aliases:` list in the frontmatter.

**Example of removing a false positive:**

```yaml
# Before (with false positive)
aliases:
  - /docs/esc/integrations/dynamic-login-credentials/infisical-login/  # ← FALSE POSITIVE
  - /docs/esc/providers/doppler-login/

# After (false positive removed)
aliases:
  - /docs/esc/providers/doppler-login/
```

After removing false positives, re-run the apply script if needed, or proceed to verification.

#### Step 4: Re-verify

```bash
python3 verify-all-historical-aliases.py
```

Run the comprehensive verification again to confirm all aliases are now present.

### Example Output

```
================================================================================
=== VERIFICATION SUMMARY ===
================================================================================
Total markdown files scanned:        699
Files with historical moves:         353
Files with complete aliases:         ✓ 271
Files with missing aliases:          ❌ 82
Total missing aliases:               ❌ 82
```

### What Gets Checked

The comprehensive verification checks:
1. **Git History**: All paths a file has had in the past 6 months on the master branch
1. **Frontmatter Aliases**: The `aliases:` field in markdown frontmatter
1. **S3 Redirects**: Redirect mappings in `scripts/redirects/*.txt` files
1. **Multi-hop Moves**: Files moved multiple times (A→B→C)
1. **Pre-reorg Moves**: Files moved on master before your branch existed
1. **Low-Similarity Renames**: Files that were significantly rewritten during moves using git's 30% similarity detection (catches delete+add operations that are actually content revamps)

**Note**: The script only checks `origin/master` history, not development branches. This prevents false positives from paths that only existed during development and were never published.

### Differences from Branch Verification

| Feature | Branch Verification | Historical Verification |
|---------|-------------------|------------------------|
| Scope | Current branch vs master | Complete git history |
| Time Range | Branch lifetime | Past 6 months |
| Catches pre-reorg moves | ❌ No | ✓ Yes |
| Catches multi-hop moves | ❌ No | ✓ Yes |
| Checks S3 redirects | ❌ No | ✓ Yes |
| When to use | Every PR with file moves | After major reorgs |
