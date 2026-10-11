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
3. **Detects co-located assets** - Finds images and assets that should move with the file
4. **Moves file and assets safely** - Uses `git mv` to preserve history and injects Hugo alias
5. **Updates menu frontmatter** - Adjusts menu section when crossing section boundaries
6. **Verifies aliases** - Runs repository alias verification scripts
7. **Updates internal links** - Updates references in docs/ and product/ directories
8. **Provides summary** - Shows comprehensive checklist and next steps, including orphaned menu detection

## 8-Step Workflow

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
[Step 1/8] Determine Source File

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

### Step 3: Detect and Handle Co-located Assets

**Goal**: Identify and optionally move images and other assets co-located with the source file.

**Display**:

```
[Step 3/8] Detect Co-located Assets

Checking for images and assets in source directory...
```

**Action**:

Run asset detection script:

```bash
bash .claude/commands/move-doc/scripts/detect-assets.sh "{source_file}"
```

**Parse JSON output**:

- `assetCount` - Number of assets found
- `assets[]` - Array of asset file paths
- `sourceDir` - Source directory path

**Decision tree based on asset count**:

**0 assets**:
```
✓ No co-located assets found
```
Continue to Step 4.

**1-3 assets**:
```
Found {count} asset(s) in {sourceDir}:
  - filename1.png
  - filename2.svg
  - filename3.jpg

Move these assets to the new location?
```

Use AskUserQuestion with options:
- Yes - Move all assets (recommended)
- No - Keep assets at current location
- Review individually - Select which assets to move

**4+ assets**:
```
Found {count} assets in {sourceDir}

Would you like to move these assets with the file?
```

Use AskUserQuestion with options:
- Move all assets (recommended)
- Review and select specific assets
- Skip asset movement

**Asset reference detection**:

If user chooses not to move assets, check if markdown file references them:

```bash
for asset in "${skipped_assets[@]}"; do
  basename=$(basename "$asset")
  if grep -q "$basename" "{source_file}"; then
    # Found reference
  fi
done
```

If references found, display warning:
```
⚠️  Warning: Source file references assets that won't be moved:
  - image.png (referenced in markdown)
  - diagram.svg (referenced in markdown)

These image references will break unless you update them manually.
Consider moving these assets or updating the references to absolute paths.
```

**Store asset move list**: Keep track of which assets to move for execution in Step 4.

**Error handling**:

- Script execution fails → Warn, continue without asset detection
- Permission errors reading directory → Warn, continue without asset detection
- Very large number of assets (20+) → Offer batch operations, don't list all individually

See `move-doc:references:asset-handling` for detailed asset co-location patterns and verification strategies.

### Step 4: Execute Move and Add Alias

**Goal**: Move file and selected assets with git, then inject Hugo alias.

**Display**:

```
[Step 4/8] Execute Move and Add Alias

Moving file and assets with git...
```

**Actions**:

**3a. Create parent directory if needed**:

```bash
mkdir -p "$(dirname "{destination_file}")"
```

**3b. Execute git mv for markdown file**:

```bash
git mv "{source_file}" "{destination_file}"
```

**3b-assets. Execute git mv for selected assets** (if any from Step 3):

```bash
dest_dir=$(dirname "{destination_file}")

for asset in "${assets_to_move[@]}"; do
  asset_basename=$(basename "$asset")
  git mv "$asset" "$dest_dir/$asset_basename"
done
```

**3c. Calculate old URL** using algorithm from `move-doc:references:path-conversion`

**3d. Inject alias into frontmatter** using Edit tool for string replacement. See `move-doc:references:alias-injection` for frontmatter manipulation strategies.

**Display results**:

```
✅ File moved: {source_file} → {destination_file}
✅ Assets moved: {asset_count} file(s)
✅ Git history preserved (used git mv)
✅ Alias added: {old_url}
```

**Error handling**:

- `git mv` fails → Report error (uncommitted changes, conflicts, permissions), rollback not needed as no changes made
- Asset move fails → Report which assets failed, continue with markdown file
- Alias injection fails → Warn user, provide manual instructions, continue with verification
- Duplicate alias exists → Report success (already correct)

### Step 5: Analyze and Update Menu Frontmatter

**Goal**: Detect and update menu frontmatter when moving between documentation sections.

**Display**:

```
[Step 5/8] Analyze Menu Frontmatter

Checking if menu updates are needed...
```

**Action**:

Run menu analysis script:

```bash
bash .claude/commands/move-doc/scripts/analyze-menu.sh "{source_file}" "{destination_file}"
```

**Parse JSON output**:

- `needsUpdate` - Boolean indicating if update needed
- `sourceMenu` - Current menu section (e.g., "iac")
- `destPathSection` - Destination section based on path (e.g., "ai")
- `recommendation` - Human-readable recommendation

**Decision tree**:

**needsUpdate = false**:
```
✓ Menu frontmatter matches destination section
```
Continue to Step 6.

**needsUpdate = true**:

Display context:
```
ℹ️  Menu Section Change Detected

Current menu section: {sourceMenu}
Destination path: /docs/{destPathSection}/...

The file is moving between sections and menu frontmatter needs updating.
```

Use AskUserQuestion with options:
- Update menu automatically (recommended)
- Show me what to change (manual instructions)
- Skip (file will appear in wrong navigation section)

**If automatic update chosen**:

1. **Find appropriate parent identifier** for destination section:
   - Check destination section's `_index.md` for menu identifier
   - Look at sibling files in destination directory for common parent
   - Fallback to `{section}-home` pattern

2. **Read current frontmatter** to extract menu block:
   ```bash
   grep -A 5 "menu:" "{destination_file}"
   ```

3. **Use Edit tool** to update menu section and parent:

   Example:
   ```yaml
   # Before
   menu:
       iac:
           name: MCP server
           parent: iac-guides-ai-integration
           weight: 6

   # After
   menu:
       ai:
           name: MCP server
           parent: ai-home
           weight: 6
   ```

4. **Display confirmation**:
   ```
   ✅ Updated menu frontmatter:
     Section: {sourceMenu} → {destPathSection}
     Parent: {old_parent} → {new_parent}
   ```

**If manual instructions chosen**:

Display exact changes needed:
```
Update menu frontmatter in {destination_file}:

Lines X-Y:
  Change: menu.iac → menu.ai
  Change: parent: iac-guides-ai-integration → parent: ai-home

Command to edit:
  code {destination_file}:X
```

**If skip chosen**:

Display warning:
```
⚠️  Warning: Menu frontmatter not updated

The file will appear in the '{sourceMenu}' navigation section instead of '{destPathSection}'.
This may cause confusion for users navigating the documentation.

To fix later, manually update the menu section in the frontmatter.
```

**Error handling**:

- No menu frontmatter found → Skip this step, display info message
- Malformed YAML in menu section → Offer manual update guidance, don't attempt automatic fix
- Cannot determine parent identifier → Ask user for parent identifier input
- File staying in same section → Skip update, display info message

See `move-doc:references:menu-updates` for detailed menu structure, parent discovery algorithms, and verification procedures.

### Step 6: Run Alias Verification

**Goal**: Verify alias correctness using repository scripts.

**Display**:

```
[Step 6/8] Run Alias Verification

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

### Step 7: Update Internal Links

**Goal**: Update references in `docs/` and `product/` (skip `blog/` and `tutorials/` per AGENTS.md).

**Display**:

```
[Step 7/8] Update Internal Links

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

**Additional check: References in `.github/workflows/` and `scripts/`**

Hugo aliases redirect URLs at request time — they do **not** rewrite filesystem paths or hard-coded URL strings in CI workflows or repository scripts. If automation reads or writes the moved file by its old path (e.g. a `sed -i ./content/...` line in a workflow), the move silently breaks that automation at the next scheduled run.

**Real example**: PR #19137 moved `content/docs/get-started/download-install/versions.md` to `content/docs/install/versions.md`. The Hugo alias kept all user-facing URLs working, but `.github/workflows/pulumi-cli-docs.yml` had `sed -i ./content/docs/get-started/download-install/versions.md` hard-coded, and the next scheduled CLI docs run failed with `sed: can't read ...: No such file or directory`.

Search both the old URL and the old filesystem path:

```bash
# Combine URL and filesystem-path searches; trim leading ./ from path
old_path_trimmed="${source_file#./}"
grep -rn "{old_url}\|${old_path_trimmed}" .github/workflows/ scripts/ 2>/dev/null
```

**Do not auto-update these matches.** Workflow and script references appear inside shell strings, regex, JS, YAML literals, JSON, etc., where a blind `sed` substitution can corrupt surrounding syntax or the meaning of adjacent code. Surface matches as a manual-review warning instead.

**On matches found**, display:

```
⚠️  External references that this skill will NOT auto-update:

  .github/workflows/foo.yml:42 — old URL
  scripts/bar.sh:9 — old filesystem path

Hugo aliases do not redirect filesystem writes or URL constants inside CI.
Review each match and update by hand if the surrounding code still expects
the old location. Common offenders:

  - sed -i / cat / cp commands writing to the moved file
  - Lighthouse / link-checker URL lists
  - Algolia ranking rules keyed on the old canonical URL
  - Redirect destinations in scripts/redirects/*.txt
```

Add a "Manual review: external references" line to the Step 8 summary if any matches were found, listing the file:line locations so the user can act on them in the same PR as the move.

**On no matches**: silently continue — no message needed unless the user has asked for verbose output.

### Step 8: Summary and Next Steps

**Goal**: Provide comprehensive summary with orphaned menu detection and actionable next steps.

**Display**:

```
[Step 8/8] Summary and Next Steps

═══════════════════════════════════════════════════════════
📋 Move Summary
═══════════════════════════════════════════════════════════

File Move:
✅ Moved: {old_url} → {new_url}
✅ Git history preserved (used git mv)

Assets:
{asset_status}

Menu Frontmatter:
{menu_status}

Aliases:
{alias_status}

Internal Links:
{link_update_status}

═══════════════════════════════════════════════════════════
```

**Additional Check: Orphaned Menu Entries**

Run orphaned menu detection:

```bash
bash .claude/commands/move-doc/scripts/check-orphaned-menus.sh "{old_url}"
```

**Parse JSON output**:

- `found` - Whether a menu entry was found
- `isOrphaned` - Whether entry has no remaining references
- `identifier` - Menu identifier checked
- `lineNumber` - Line in menus.yml
- `referenceCount` - Number of files still referencing this identifier

**If orphaned entry found** (`found: true` and `isOrphaned: true`):

Display warning in summary:

```
⚠️  Orphaned Menu Entry Detected

The menu entry in config/_default/menus.yml may be orphaned:
  Identifier: {identifier}
  Location: config/_default/menus.yml:{lineNumber}
  References: 0 files

Consider removing this entry from menus.yml if no other pages use it.
Manual verification recommended before removal.
```

Add to next steps:

```markdown
6. Review orphaned menus (if detected):
   - Open config/_default/menus.yml:{lineNumber}
   - Verify no other pages reference '{identifier}'
   - Search: grep -r "parent: {identifier}" content/docs/
   - If confirmed unused, remove the menu entry
   - Test: make serve (verify navigation still works)
   - Commit: git commit -m "docs: remove orphaned menu entry for {identifier}"
```

**If entry still referenced** (`found: true` and `isOrphaned: false`):

Display info message:

```
ℹ️  Menu entry '{identifier}' still in use by {referenceCount} file(s). No cleanup needed.
```

**If no entry found** (`found: false`):

No additional message needed (old location didn't have corresponding menu entry).

**Complete next steps display**:

```
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
   {asset_verification_note}

4. Commit:
   git add -A
   git commit -m "docs: move {filename} from {old_dir} to {new_dir}"

5. Consider updating:
   - Navigation menu weights (if order affected)
   - External docs pointing to old URL
   - Related content links

{orphaned_menu_steps}

═══════════════════════════════════════════════════════════
```

**Status templates**:

- **Assets**:
  - Moved: "✅ Moved {count} asset(s) with file"
  - Skipped: "ℹ️ {count} asset(s) not moved (verify references)"
  - None: "✅ No co-located assets"

- **Menu**:
  - Updated: "✅ Updated menu section: {old} → {new}"
  - Updated parent: "✅ Updated menu parent: {old_parent} → {new_parent}"
  - No update needed: "✅ Menu frontmatter matches destination"
  - Skipped: "⚠️ Menu frontmatter not updated (manual update needed)"
  - No menu: "ℹ️ No menu frontmatter in file"

- **Aliases**:
  - Success: "✅ Added alias: {old_url}" + "✅ Alias verification: PASSED"
  - Warning: "⚠️ Added alias: {old_url}" + "⚠️ Alias verification: FAILED"

- **Links**:
  - Updated: "✅ Updated {count} reference(s)" + note about skipped blog/tutorials
  - Skipped: "ℹ️ {count} reference(s) not updated (manual update needed)"
  - None: "✅ No internal links to update"

**Optional commit assistance**: Offer to create commit with message following repository conventions.

## Reference Files

This skill uses detailed reference documentation:

- `move-doc:references:path-conversion` - Hugo URL path calculation algorithm
- `move-doc:references:alias-injection` - Frontmatter manipulation patterns
- `move-doc:references:asset-handling` - Asset co-location patterns and movement strategies
- `move-doc:references:menu-updates` - Menu structure and frontmatter update procedures
- `move-doc:references:orphaned-menus` - Orphaned menu detection and cleanup guidance
- `move-doc:references:link-updates` - Internal link update patterns and edge cases
- `move-doc:references:verification` - Alias verification script usage

## Critical Requirements

**From AGENTS.md (lines 72-98)**:

1. **Always use `git mv`** to preserve file history
2. **Always add aliases** to moved files (Hugo content)
3. **Always verify aliases** with repository scripts
4. **Update links in `docs/` and `product/`** only (skip `blog/` and `tutorials/`)
5. **Never break existing URLs** - aliases must redirect properly
6. **Always scan `.github/workflows/` and `scripts/`** for references to the old URL or filesystem path — Hugo aliases do not redirect filesystem writes or URL constants embedded in CI/automation

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
