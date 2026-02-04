---
description: Automates moving documentation files with git history preservation, automatic alias injection, verification, and internal link updates.
---

# /move-doc Skill

## Invocation

```
/move-doc [source-file]
```

**Parameters**:

- `source-file` (optional): Path to file to move (e.g., `content/docs/old/path/file.md`)

**Examples**:

```
/move-doc content/docs/guides/old-name.md
/move-doc
```

## What This Skill Does

1. **Determines source file** - Identifies file to move from argument, context, or prompts user
2. **Gets destination** - Interactive destination selection with validation and preview
3. **Moves file safely** - Uses `git mv` to preserve history and injects Hugo alias
4. **Verifies aliases** - Runs repository alias verification scripts
5. **Updates internal links** - Updates references in docs/ and product/ directories
6. **Provides summary** - Shows comprehensive checklist and next steps

## 6-Step Workflow

### Step 1: Determine Source File

**Goal**: Identify the file to move with minimal friction.

**Detection Strategy** (priority order):

1. **Command argument**: `/move-doc content/docs/foo/bar.md`
2. **Recent context**: Check last 5 messages for Read/Edit operations on `.md` files under `content/`
3. **Ask user**: Present AskUserQuestion with suggestions from recent context (up to 4 recent files)

**Validation**:

- File exists
- Is markdown (`.md` extension)
- Under `content/` directory
- Get absolute path

**File type detection**: Hugo content files (`content/**/*.md`) use Hugo aliases. Non-content files require S3 redirects (not supported by this skill).

**Display**:

```
[Step 1/6] Determine Source File

📄 Moving: content/docs/old/path/file.md
   Type: Hugo content file
   Current URL: /docs/old/path/file/
```

**Error handling**:

- File doesn't exist → Error, stop
- Not markdown → Error, stop
- Not under `content/` → Warn, ask confirmation to continue
- Non-Hugo content → Warn about S3 redirects, stop

### Step 2: Determine Destination

**Goal**: Get validated destination with preview.

**User interaction**:

Use AskUserQuestion to determine move type:

```
How would you like to move this file?
```

**Options**:

1. **Rename in same directory** - Extract current directory, ask for new filename, validate kebab-case
2. **Move to different directory** - Navigate directories similar to `/new-doc`, optionally rename
3. **Enter full destination path** - Prompt for complete path and validate

**Validation for all options**:

- Parent directory exists (or offer to create)
- Destination file doesn't exist
- Under `content/` directory (if Hugo content)
- Kebab-case filename (unless `_index.md`)
- Different from source path

**Calculate URL changes** using algorithm from `move-doc:references:path-conversion`. Preview source, destination, old URL, new URL, and alias that will be added. Confirm with user before proceeding.

**Error handling**:

- Parent directory doesn't exist → Offer to create it
- Destination exists → Error, ask for different destination
- Same as source → Error, ask for different destination
- Invalid filename format → Explain kebab-case, ask again

### Step 3: Execute Move and Add Alias

**Goal**: Move file with git and inject Hugo alias.

**Display**:

```
[Step 3/6] Execute Move and Add Alias

Moving file with git...
```

**Actions**:

**3a. Create parent directory if needed**:

```bash
mkdir -p "$(dirname "{destination_file}")"
```

**3b. Execute git mv**:

```bash
git mv "{source_file}" "{destination_file}"
```

**3c. Calculate old URL** using algorithm from `move-doc:references:path-conversion`

**3d. Inject alias into frontmatter** using Edit tool for string replacement. See `move-doc:references:alias-injection` for frontmatter manipulation strategies.

**Display results**:

```
✅ File moved: {source_file} → {destination_file}
✅ Git history preserved (used git mv)
✅ Alias added: {old_url}
```

**Error handling**:

- `git mv` fails → Report error (uncommitted changes, conflicts, permissions), rollback not needed as no changes made
- Alias injection fails → Warn user, provide manual instructions, continue with verification
- Duplicate alias exists → Report success (already correct)

### Step 4: Run Alias Verification

**Goal**: Verify alias correctness using repository scripts.

**Display**:

```
[Step 4/6] Run Alias Verification

Running alias verification scripts...
```

**Commands**:

```bash
cd scripts/alias-verification
./extract-renames.sh
python3 verify-aliases.py
```

**Parse results**:

- Exit code 0 = Success
- Exit code 1 = Failures detected

**On success**:

```
✅ Alias verification passed
✅ Old URL {old_url} will redirect to new location
```

**On failure**:

```
⚠️ Alias verification failed
```

Read `scripts/alias-verification/aliases-missing.txt` to get details:

```python
with open('scripts/alias-verification/aliases-missing.txt', 'r') as f:
    failures = f.read()
```

**Parse failure** from `aliases-missing.txt` and display expected alias and file path.

**Recovery options** (ask user):

- Re-inject alias (re-read, re-inject, re-verify)
- Show file contents and expected format
- Continue without fix (warn about broken redirects, note in summary)
- Abort and rollback (`git mv` back to source)

**Error handling**:

- Scripts not found → Critical error, ensure in repository root
- Script execution fails → Warn, suggest manual verification at localhost

See `move-doc:references:verification` for detailed script usage and error handling.

### Step 5: Update Internal Links

**Goal**: Update references in `docs/` and `product/` (skip `blog/` and `tutorials/` per AGENTS.md).

**Display**:

```
[Step 5/6] Update Internal Links

Searching for internal references...
```

**Search for references** using `grep -rl "{old_url}" content/docs/ content/product/ --include="*.md"` and count results.

**Decision tree based on count**:

- **0 references**: Report no links to update
- **1-19 references**: List files, offer "Update all", "Show changes first", or "Skip"
- **20+ references**: Show count only, offer "Update all" or "Skip"

**Update command**: `find content/docs content/product -name "*.md" -exec sed -i 's|{old_url}|{new_url}|g' {} +`

**Show changes** (if count < 20): Display grep context for first 3-5 files, ask to proceed

**Skip**: Provide list of files and manual update command

**Error handling**:

- `sed` fails → List failed files, offer continue or rollback
- Many files modified → Remind to review with `git diff`, provide revert command if needed

**Important**: Always skip `blog/` and `tutorials/` per AGENTS.md. See `move-doc:references:link-updates` for patterns and edge cases.

### Step 6: Summary and Next Steps

**Goal**: Provide comprehensive summary and actionable next steps.

**Display**:

```
[Step 6/6] Summary and Next Steps

═══════════════════════════════════════════════════════════
📋 Move Summary
═══════════════════════════════════════════════════════════

File Move:
✅ Moved: {old_url} → {new_url}
✅ Git history preserved (used git mv)

Aliases:
{alias_status}

Internal Links:
{link_update_status}

═══════════════════════════════════════════════════════════
📝 Next Steps
═══════════════════════════════════════════════════════════

1. Review changes:
   git status
   git diff

2. Test build:
   make build

3. Test locally:
   make serve
   Visit: http://localhost:1313{new_url}
   Old URL: http://localhost:1313{old_url} (should redirect)

4. Commit:
   git add -A
   git commit -m "docs: move {filename} from {old_dir} to {new_dir}"

5. Consider updating:
   - Navigation menu weights (if order affected)
   - External docs pointing to old URL
   - Related content links

═══════════════════════════════════════════════════════════
```

**Status templates**:

- Alias success: "✅ Added alias: {old_url}" + "✅ Alias verification: PASSED"
- Alias warning: "⚠️ Added alias: {old_url}" + "⚠️ Alias verification: FAILED"
- Links updated: "✅ Updated {count} reference(s)" + note about skipped blog/tutorials
- Links skipped: "ℹ️ {count} reference(s) not updated (manual update needed)"
- No links: "✅ No internal links to update"

**Optional commit assistance**: Offer to create commit with message following repository conventions.

## Reference Files

This skill uses detailed reference documentation:

- `move-doc:references:path-conversion` - Hugo URL path calculation algorithm
- `move-doc:references:alias-injection` - Frontmatter manipulation patterns
- `move-doc:references:link-updates` - Internal link update patterns and edge cases
- `move-doc:references:verification` - Alias verification script usage

## Critical Requirements

**From AGENTS.md (lines 72-98)**:

1. **Always use `git mv`** to preserve file history
2. **Always add aliases** to moved files (Hugo content)
3. **Always verify aliases** with repository scripts
4. **Update links in `docs/` and `product/`** only (skip `blog/` and `tutorials/`)
5. **Never break existing URLs** - aliases must redirect properly

## Error Recovery

**Full rollback** (if major failure occurs):

```bash
# Undo file move
git mv "{destination_file}" "{source_file}"

# Undo link updates
git restore content/docs/ content/product/

# Verify clean state
git status
```

**Partial rollback options**:

- Undo file move only: `git mv "{destination}" "{source}"`
- Undo link updates only: `git restore content/docs/ content/product/`
- Undo alias injection: Manual edit or restore from git history
