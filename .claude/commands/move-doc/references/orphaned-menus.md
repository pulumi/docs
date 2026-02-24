---
user-invocable: false
---

# Orphaned Menu Cleanup Reference

How to detect and clean up orphaned menu entries in menus.yml when moving files.

## Menu Entry Lifecycle

When files move between sections, menu entries can become orphaned:

1. **File with menu frontmatter** exists at old location
   - Frontmatter references a parent identifier in `config/_default/menus.yml`
   - Entry in menus.yml provides navigation structure

2. **File moves** to new section
   - Frontmatter updated to new section (Step 3.5 of move-doc)
   - File no longer references old parent identifier

3. **Menu entry orphaned**
   - Entry remains in menus.yml
   - No files reference it as `parent`
   - Serves no navigation purpose

## What is an Orphaned Menu Entry?

An entry in `config/_default/menus.yml` that:
- Defines a menu identifier
- No longer has any files referencing it as a `parent`
- Was used by files that have since moved away

### Example from MCP Server Move

**Before move** - Entry used by files:
```yaml
# config/_default/menus.yml (lines 13-16)
iac:
  - name: AI Integration
    parent: iac-using-pulumi
    identifier: iac-guides-ai-integration  # Used as parent
    weight: 60
```

Referenced by:
```yaml
# content/docs/iac/guides/ai-integration/mcp-server/index.md
menu:
    iac:
        parent: iac-guides-ai-integration  # References this identifier
```

**After move** - Entry orphaned:
```yaml
# config/_default/menus.yml (lines 13-16)
iac:
  - name: AI Integration
    parent: iac-using-pulumi
    identifier: iac-guides-ai-integration  # No longer referenced
    weight: 60
```

File moved to `/docs/ai/` and updated:
```yaml
# content/docs/ai/mcp-server/index.md
menu:
    ai:
        parent: ai-home  # No longer references iac-guides-ai-integration
```

**Result**: `iac-guides-ai-integration` is orphaned - no files reference it.

## Detection Strategy

### Automated Script

**Script**: `.claude/commands/move-doc/scripts/check-orphaned-menus.sh`

**Purpose**: Detect potentially orphaned menu entries after file moves.

**Usage**:
```bash
bash .claude/commands/move-doc/scripts/check-orphaned-menus.sh "/docs/iac/guides/ai-integration/"
```

**Algorithm**:

1. Convert old URL to likely identifier format:
   - `/docs/iac/guides/ai-integration/` → `iac-guides-ai-integration`

2. Search menus.yml for this identifier:
   ```bash
   grep -n "identifier: iac-guides-ai-integration" config/_default/menus.yml
   ```

3. If found, count files referencing it as parent:
   ```bash
   grep -r "parent: iac-guides-ai-integration" content/docs/ --include="*.md"
   ```

4. If reference count = 0, entry is orphaned

### Script Output

```json
{
  "found": true,
  "identifier": "iac-guides-ai-integration",
  "lineNumber": "15",
  "context": "  - name: AI Integration\n    parent: iac-using-pulumi\n    identifier: iac-guides-ai-integration",
  "referenceCount": 0,
  "isOrphaned": true,
  "menusFile": "config/_default/menus.yml"
}
```

**Fields**:
- `found`: Whether menu entry was found in menus.yml
- `identifier`: Menu identifier checked
- `lineNumber`: Line in menus.yml where identifier appears
- `context`: Surrounding lines showing the menu entry
- `referenceCount`: Number of markdown files referencing this as parent
- `isOrphaned`: True if referenceCount = 0
- `menusFile`: Path to menus.yml

## Manual Verification

Before removing an orphaned entry, verify manually:

### 1. Check Git History

Confirm files recently moved away:

```bash
git log --all --full-history -- "content/docs/iac/guides/ai-integration/"
```

Look for commit messages about moving files from this directory.

### 2. Search for References

Comprehensive search across all content:

```bash
# Search markdown files
grep -r "iac-guides-ai-integration" content/ --include="*.md"

# Search config files
grep -r "iac-guides-ai-integration" config/

# Search other menus.yml entries (used as parent by other entries)
grep "parent: iac-guides-ai-integration" config/_default/menus.yml
```

**Zero results** = Confirmed orphaned

### 3. Check Menu Structure

Understand the menu hierarchy:

```yaml
iac:
  - name: Guides
    identifier: iac-using-pulumi  # Parent of orphaned entry
  - name: AI Integration
    parent: iac-using-pulumi
    identifier: iac-guides-ai-integration  # Orphaned entry
```

Verify this isn't a structural element still needed for navigation.

## Cleanup Process

### Safe Removal Steps

1. **Locate entry** in menus.yml using line number from script

2. **Verify it's truly orphaned** using manual verification steps above

3. **Remove entry block** from menus.yml:

   **Before**:
   ```yaml
   iac:
     - name: Guides
       parent: iac-home
       identifier: iac-using-pulumi
       weight: 20
     - name: AI Integration
       parent: iac-using-pulumi
       identifier: iac-guides-ai-integration
       weight: 60
     - name: Components
       parent: iac-guides-building-extending
       identifier: iac-guides-components
       weight: 1
   ```

   **After**:
   ```yaml
   iac:
     - name: Guides
       parent: iac-home
       identifier: iac-using-pulumi
       weight: 20
     - name: Components
       parent: iac-guides-building-extending
       identifier: iac-guides-components
       weight: 1
   ```

   **Removed lines**:
   ```yaml
     - name: AI Integration
       parent: iac-using-pulumi
       identifier: iac-guides-ai-integration
       weight: 60
   ```

4. **Verify YAML syntax**:
   ```bash
   make build
   ```

   Look for YAML parsing errors in menus.yml.

5. **Test navigation**:
   ```bash
   make serve
   ```

   Navigate to IaC section, verify no broken navigation links.

6. **Commit change**:
   ```bash
   git add config/_default/menus.yml
   git commit -m "docs: remove orphaned menu entry for iac-guides-ai-integration

   This menu entry was orphaned when MCP server docs moved from
   /docs/iac/guides/ai-integration/ to /docs/ai/. No files now
   reference this identifier as a parent."
   ```

## Edge Cases

### Shared Identifiers

Some identifiers may be referenced by:

1. **Multiple files** (not orphaned):
   ```bash
   grep -r "parent: iac-guides-ai-integration" content/docs/
   # Returns multiple files
   ```
   **Action**: Keep the entry, it's still in use

2. **Other menu entries as parent** (not orphaned):
   ```yaml
   - name: Child Section
     parent: iac-guides-ai-integration  # Uses orphaned entry as parent
   ```
   **Action**: Keep the entry, it's used for menu hierarchy

3. **Navigation templates**:
   ```html
   <!-- themes/.../navigation.html -->
   {{ if eq .Identifier "iac-guides-ai-integration" }}
   ```
   **Action**: Keep the entry, it's referenced in theme code

### Section Headers

Some menu entries are pure navigation organization:

```yaml
- name: Guides
  parent: iac-home
  identifier: iac-using-pulumi  # Section header
  weight: 20
```

**Characteristics**:
- `referenceCount` may be 0 (no files directly use as parent)
- BUT: Other menu entries use it as `parent`
- Provides structural organization in sidebar

**Detection**:
```bash
# Check if other menu entries use this as parent
grep "parent: iac-using-pulumi" config/_default/menus.yml
```

**Action**: Do NOT remove section headers, even if no files directly reference them.

### Placeholders for Upcoming Content

Some entries may be intentional placeholders:

```yaml
- name: Advanced Topics
  parent: iac-home
  identifier: iac-advanced  # Future content
  weight: 100
```

**Action**: Verify with team before removing. May be intentional.

### False Positives

Script may flag entries that shouldn't be removed:

1. **Recent commit**: Files just moved, but not yet deployed
2. **Branch differences**: Files exist on other branches
3. **External references**: Used by tools or scripts outside repo

**Always verify manually** before removal.

## When to Skip Cleanup

Don't remove menu entries that:

1. **Are section headers** organizing other menu items
2. **Are placeholders** for upcoming content
3. **Are used by other menu entries** as `parent`
4. **Have referenceCount > 0** (still referenced by files)
5. **Are part of theme logic** (referenced in templates)
6. **Are uncertain** - when in doubt, ask team

## Integration with Move Workflow

Orphaned menu detection runs in **Step 6: Summary** as a passive check.

### Workflow Integration

1. **Run detection script** during final summary:
   ```bash
   bash .claude/commands/move-doc/scripts/check-orphaned-menus.sh "{old_url}"
   ```

2. **Parse JSON output** to determine status

3. **If orphaned** (`found: true` and `isOrphaned: true`):
   - Display warning with identifier and line number
   - Add cleanup guidance to "Next Steps"
   - Do NOT automatically remove (too risky)

4. **If still in use** (`found: true` and `isOrphaned: false`):
   - Display info: "Menu entry still in use by {count} file(s)"
   - No action needed

5. **If not found** (`found: false`):
   - No message needed
   - Old location didn't have menu entry

### Example Warning

```
⚠️  Orphaned Menu Entry Detected

The menu entry in config/_default/menus.yml may be orphaned:
  Identifier: iac-guides-ai-integration
  Location: config/_default/menus.yml:15
  References: 0 files

Consider removing this entry from menus.yml if no other pages use it.
Manual verification recommended before removal.
```

### Next Steps Guidance

Added to summary:

```markdown
6. Review orphaned menus (if detected):
   - Open config/_default/menus.yml:15
   - Verify no other pages reference 'iac-guides-ai-integration'
   - Remove orphaned entry if confirmed unused
   - Test navigation with `make serve`
   - Commit: "docs: remove orphaned menu entry for iac-guides-ai-integration"
```

## Why Not Automatic Removal?

**Rationale for manual verification**:

1. **Menu structure is complex** - automated removal could break navigation
2. **Section headers may have referenceCount = 0** but are still needed
3. **False positives** could delete intentional placeholders
4. **High impact** - broken navigation affects entire site
5. **Low frequency** - orphaned entries are rare, manual cleanup is acceptable

**Trade-off**: Safety over automation. Detection provides value; removal requires judgment.

## Verification After Cleanup

After removing an orphaned entry:

### 1. Build Site

Check for errors:
```bash
make build
```

Look for:
- YAML syntax errors in menus.yml
- Undefined menu identifier warnings
- Navigation build errors

### 2. Test Navigation

Serve site locally:
```bash
make serve
```

**Verify**:
- All sections load correctly
- Sidebar navigation works
- No broken links in menu
- Section structure intact

### 3. Check Breadcrumbs

Navigate to pages in the affected section:
```
http://localhost:1313/docs/iac/guides/...
```

Verify breadcrumbs don't reference removed entry.

### 4. Review Git Diff

Before committing:
```bash
git diff config/_default/menus.yml
```

**Verify**:
- Only orphaned entry removed
- No accidental removals
- YAML indentation correct
- No trailing spaces

## Common Mistakes

### Removing Section Headers

**Wrong** (removing structural element):
```yaml
# Removed - MISTAKE
# - name: Guides
#   identifier: iac-using-pulumi
```

**Check**: Does another entry use this as `parent`?
```bash
grep "parent: iac-using-pulumi" config/_default/menus.yml
```

If yes, it's a section header, not orphaned.

### Batch Removal Without Verification

**Wrong**:
```bash
# Remove all with referenceCount=0
# DANGEROUS - may remove section headers
```

**Right**:
```bash
# Verify each individually
# Check git history, references, menu structure
```

### Ignoring Edge Cases

**Wrong** (assuming script is always correct):
```
Script says orphaned → Remove immediately
```

**Right**:
```
Script says orphaned → Verify manually → Then remove if confirmed
```

## Best Practices

1. **Always run detection script** after moving files
2. **Verify manually** before removal (check history, references, structure)
3. **Understand menu hierarchy** before removing entries
4. **Test navigation** after cleanup
5. **Document removal reason** in commit message
6. **Keep section headers** even if referenceCount = 0
7. **When uncertain, ask** - don't guess

## Summary

Orphaned menu cleanup ensures menus.yml stays clean:

- **Detection**: Automated script identifies potential orphans
- **Verification**: Manual checks confirm it's safe to remove
- **Cleanup**: Remove entry, test navigation, commit with message
- **Edge cases**: Section headers, placeholders, false positives
- **Integration**: Passive check in move workflow, not automatic removal

When in doubt, keep the entry - orphaned entries don't break anything, but removing needed entries breaks navigation.
