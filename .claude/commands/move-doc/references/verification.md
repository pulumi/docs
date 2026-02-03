# Alias Verification Reference

How to use repository scripts to verify Hugo aliases are correct after moving files.

## Overview

The repository includes scripts in `scripts/alias-verification/` to ensure moved files have proper aliases. These scripts:

1. Extract git renames from commit history
2. Verify each renamed file has correct alias in frontmatter
3. Report missing or incorrect aliases

## Script Locations

```
scripts/alias-verification/
├── extract-renames.sh       # Extract renames from git log
├── verify-aliases.py        # Verify aliases in frontmatter
├── generate-fixes.py        # Generate alias fix commands
├── apply-fixes.py           # Apply generated fixes
└── README.md                # Detailed usage instructions
```

## Basic Workflow

### Step 1: Extract Renames

```bash
cd scripts/alias-verification
./extract-renames.sh
```

**What it does**:

- Scans git log for renamed markdown files in `content/`
- Writes results to `renames.txt`
- Format: `old_path|new_path` (one per line)

**Output file**: `renames.txt`

**Example**:

```
content/docs/old/path.md|content/docs/new/path.md
content/docs/foo/_index.md|content/docs/bar/_index.md
```

**Exit codes**:

- `0`: Success (renames found and extracted)
- `0`: Success (no renames found - empty file)

### Step 2: Verify Aliases

```bash
python3 verify-aliases.py
```

**What it does**:

- Reads `renames.txt`
- For each rename:
  - Calculates expected alias URL from old path
  - Reads new file's frontmatter
  - Checks if expected alias is present
- Reports missing or incorrect aliases

**Output files**:

- `aliases-missing.txt` - Files with missing aliases
- `aliases-ok.txt` - Files with correct aliases (if verbose)

**Exit codes**:

- `0`: All aliases correct
- `1`: Missing or incorrect aliases found

**Console output**:

```
Checking aliases for 3 renames...
✓ content/docs/new/path1.md has correct alias
✗ content/docs/new/path2.md missing alias: /docs/old/path2/
✓ content/docs/new/path3.md has correct alias

Results: 2 OK, 1 missing
```

### Step 3: Review Failures

If exit code is `1`, read `aliases-missing.txt`:

```bash
cat aliases-missing.txt
```

**Format**:

```
Missing alias for: content/docs/old/path.md -> content/docs/new/path.md
Expected alias: /docs/old/path/
File: content/docs/new/path.md
```

## Integration with /move-doc

The `/move-doc` skill uses these scripts in **Step 4**:

```bash
cd scripts/alias-verification
./extract-renames.sh
python3 verify-aliases.py
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo "✅ Alias verification passed"
else
    echo "⚠️ Alias verification failed"
    cat aliases-missing.txt
fi
```

## URL Calculation Algorithm

See `references/path-conversion.md` for the algorithm used by verification scripts to convert file paths to URLs.

## Error Handling

**Script not found**: Ensure in `scripts/alias-verification/` directory

**Python dependencies**: Install with `pip3 install pyyaml`

**No renames found**: OK - verification will pass trivially

**Malformed frontmatter**: Manually fix YAML syntax in file

## Manual Verification Alternative

If scripts fail:

1. Start Hugo server: `make serve`
2. Test old URL redirect: `curl -I http://localhost:1313/docs/old/path/`
3. Test new URL loads: `curl -I http://localhost:1313/docs/new/path/`
4. Check frontmatter: `head -20 content/docs/new/path.md`

## Common Issues

**Verification fails but alias looks correct**: Missing trailing slash - add `/` at end

**Multiple aliases accumulate**: Correct behavior when file moved multiple times - all previous URLs should redirect

**Script hangs**: Large git history - wait or limit scope with `git log --since="2024-01-01"`
