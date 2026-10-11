# Indent Fixes Scripts

These scripts detect and fix incorrectly indented bullet lists in markdown files. This issue occurred during the content reorganization (PRs #16119, #16303) where bullet lists were inadvertently indented with 4 spaces, causing Hugo to render them as code blocks instead of proper lists.

## The Problem

In markdown, 4 spaces of indentation before a bullet point creates a code block instead of a list item:

```markdown
<!-- WRONG: Renders as code block -->
    - This is a bullet point
    - Another bullet point

<!-- CORRECT: Renders as list -->
- This is a bullet point
- Another bullet point
```

During the content reorganization, some bullet lists were accidentally indented with 4 spaces, breaking their rendering on the website.

## Usage

### Quick Start

From the repository root:

```bash
cd scripts/indent-fixes

# Step 1: Detect issues
python3 detect_indent_issues.py

# Step 2: Review the report, then fix all issues
python3 fix_indent_issues.py

# Step 3: Verify the changes
git diff content/docs/
```

### Step 1: Detection

Run the detection script to find all problematic indentations:

```bash
python3 detect_indent_issues.py
```

This will output:
- Summary count of files with issues
- Line-by-line listing of each problematic indentation
- Total count of issues found

**Example output:**
```
Found 14 files with potential indentation issues:

content/docs/iac/get-started/aws/next-steps.md: 5 issue(s)
  Line 22:     - Created a Pulumi new project.
  Line 23:     - Provisioned a new S3 bucket.
  Line 24:     - Turned it into a static website.
  Line 25:     - Created a website component for easy reuse.
  Line 26:     - Destroyed all of the resources you've provisioned.

Total: 66 potential issues across 14 files
```

### Step 2: Fix Issues

After reviewing the detection report, run the fix script:

```bash
python3 fix_indent_issues.py
```

This will:
- Process all markdown files in `content/docs/`
- Remove 4-space indentation from incorrectly indented bullet points
- Report the number of lines fixed per file

**Example output:**
```
Fixed 66 lines across 14 files:

  content/docs/iac/get-started/aws/next-steps.md: 5 line(s) fixed
  content/docs/iac/get-started/azure/destroy-stack.md: 5 line(s) fixed
  content/docs/iac/get-started/azure/next-steps.md: 3 line(s) fixed
  ...
```

### Step 3: Verify Changes

Review the changes made by the script:

```bash
# View summary of changes
git diff --stat content/docs/

# View detailed changes
git diff content/docs/

# Test the build
make build
```

## How It Works

### Detection Logic

The `detect_indent_issues.py` script intelligently identifies problematic indentations while avoiding false positives:

**What it detects:**
- Lines matching the pattern `^    - ` (4 spaces + dash + space)
- In markdown content sections (not frontmatter or code blocks)

**What it excludes:**
- **YAML frontmatter**: Indentation between `---` markers is correct YAML syntax
- **Code blocks**: Content within ` ``` ` fences is left untouched
- **Nested lists**: Legitimate 2nd-level list items (preceded by 2-space indented parent)
- **YAML-like structures**: Content that looks like YAML configuration blocks

### Fix Logic

The `fix_indent_issues.py` script:

1. Uses the same detection logic to identify problematic lines
2. Removes exactly 4 spaces from the beginning of each line
3. Writes the corrected content back to the file
4. Reports the number of changes made

**Safety features:**
- Only modifies lines that match the detection criteria
- Preserves all other formatting (newlines, trailing spaces, etc.)
- Non-destructive: Can be reviewed with `git diff` before committing

## When to Use These Scripts

- **After content reorganizations**: When files are moved/renamed, indentation issues may be introduced
- **When rendering issues occur**: If bullet lists appear as code blocks on the site
- **Periodic audits**: Run detection periodically to catch any new issues

## Workflow

1. Make content changes or complete a reorganization
2. Run `python3 detect_indent_issues.py` to check for issues
3. Review the detection report
4. Run `python3 fix_indent_issues.py` to apply fixes
5. **IMPORTANT** -- Review changes with `git diff`! There *will* be false positives!
6. Run `make build` to verify the site builds correctly
7. Commit the fixes

## Exit Codes

Both scripts return:
- **0** - Success (issues found and reported, or no issues found)
- **Non-zero** - Unexpected error occurred

## Related

- See `scripts/alias-verification/` for tools to verify file move aliases
- See `STYLE-GUIDE.md` for markdown formatting guidelines

## History

These scripts were created to fix issues introduced during:
- PR #16119: Major documentation reorganization
- PR #16303: Insights & Governance docs reorganization

The fixes were partially addressed in:
- PR #16427: Fixed get-started guides
- PR #16428: Fixed next-steps pages

This toolset completes the remediation and provides ongoing verification.
