---
user-invocable: false
---

# Menu Updates Reference

How to detect and update menu frontmatter when moving files between documentation sections.

## Menu Structure in Pulumi Docs

Documentation uses Hugo menus for navigation. Each major section has its own menu identifier:

- **`iac`** - Infrastructure as Code documentation
- **`ai`** - AI-powered features (Neo, MCP server, etc.)
- **`esc`** - Environment, Secrets, and Configuration
- **`deployments`** - Pulumi Deployments
- **`insights`** - Pulumi Insights and Policy

## Frontmatter Menu Format

Menu configuration is defined in YAML frontmatter at the top of markdown files:

```yaml
---
title: Page Title
menu:
    <section>:
        name: Display Name
        parent: <parent-identifier>
        weight: <number>
---
```

**Fields**:
- **section** (`iac`, `ai`, etc.): Determines which menu this page appears in
- **name**: Display text in navigation
- **parent**: Identifier of parent menu item (defines hierarchy)
- **weight**: Numeric ordering within parent (lower = higher in list)

### Example

```yaml
---
title: MCP server
menu:
    iac:
        name: MCP server
        parent: iac-guides-ai-integration
        weight: 6
---
```

This page appears in the `iac` menu, under the parent `iac-guides-ai-integration`, with weight 6.

## When Menu Updates Are Needed

**Rule**: When a file moves between sections, the menu section must be updated to match the new location.

### Detection Logic

**Path-Based Section Detection**:
- `content/docs/iac/...` → Menu should use `iac`
- `content/docs/ai/...` → Menu should use `ai`
- `content/docs/esc/...` → Menu should use `esc`
- `content/docs/deployments/...` → Menu should use `deployments`
- `content/docs/insights/...` → Menu should use `insights`

**Update Required When**:
- Source path section ≠ Destination path section
- AND Menu section ≠ Destination path section

### Example: MCP Server Move

**Before** (`content/docs/iac/guides/ai-integration/mcp-server/index.md`):
```yaml
menu:
    iac:  # Matches path section
        name: MCP server
        parent: iac-guides-ai-integration
```

**After** (`content/docs/ai/mcp-server/index.md`):
```yaml
menu:
    ai:  # Updated to match new path section
        name: MCP server
        parent: ai-home  # Updated parent identifier
```

**Changes needed**:
1. Section: `iac` → `ai`
2. Parent: `iac-guides-ai-integration` → `ai-home`

## Finding the Correct Parent Identifier

Parent identifiers must match entries defined in `config/_default/menus.yml`.

### Strategy 1: Check menus.yml

Search for identifiers in the destination section:

```bash
grep -A 3 "^[[:space:]]*ai:" config/_default/menus.yml | grep "identifier:"
```

**Example output**:
```yaml
ai:
  - name: Get Started
    identifier: ai-get-started
  - name: Features
    identifier: ai-features
```

### Strategy 2: Check Destination Section's _index.md

Most section index files define their menu identifier:

```bash
grep "identifier:" content/docs/ai/_index.md
```

**Example output**:
```yaml
menu:
    ai:
        identifier: ai-home
```

### Strategy 3: Examine Sibling Files

Look at files already in the destination directory:

```bash
grep -A 3 "menu:" content/docs/ai/*/index.md | grep "parent:"
```

This shows what parent identifiers are commonly used in that section.

### Common Parent Patterns

**Root of section**:
- Format: `<section>-home`
- Examples: `ai-home`, `iac-home`, `esc-home`
- Used for top-level pages directly under `/docs/section/`

**Subsections**:
- Format: `<section>-<subsection>`
- Examples: `iac-guides-ai-integration`, `iac-using-pulumi`, `ai-features`
- Used for pages within subsections

**Deep nesting**:
- Format: `<section>-<subsection>-<subsubsection>`
- Example: `iac-guides-components-authoring`

## Menu Parent Discovery Algorithm

Automated algorithm to find the appropriate parent:

```python
def find_menu_parent(destination_file):
    """Find appropriate menu parent for destination file."""

    # Extract section from path
    section = extract_section_from_path(destination_file)

    # Parse destination path
    # Example: content/docs/ai/mcp-server/index.md
    #          → section='ai', depth=1 (mcp-server)
    dest_parts = destination_file.split('/')

    # If moving to section root (e.g., /docs/ai/page.md)
    # Use section-home as parent
    if len(dest_parts) == 4:  # content/docs/section/file.md
        return f"{section}-home"

    # If moving to subsection, find parent from directory structure
    dest_dir = os.path.dirname(destination_file)
    parent_index = os.path.join(dest_dir, "..", "_index.md")

    if os.path.exists(parent_index):
        # Read parent directory's _index.md for its menu identifier
        parent_id = extract_menu_identifier(parent_index)
        return parent_id

    # Check for sibling files and use their parent
    sibling_files = glob.glob(os.path.join(dest_dir, "*.md"))
    for sibling in sibling_files:
        sibling_parent = extract_menu_parent(sibling)
        if sibling_parent:
            return sibling_parent

    # Fallback: use section-home
    return f"{section}-home"
```

## Automated Update Procedure

The `analyze-menu.sh` script detects when updates are needed.

### Script Usage

```bash
bash .claude/commands/move-doc/scripts/analyze-menu.sh \
  "content/docs/iac/guides/ai-integration/mcp-server/index.md" \
  "content/docs/ai/mcp-server/index.md"
```

### Script Output

```json
{
  "sourceMenu": "iac",
  "sourcePathSection": "iac",
  "destPathSection": "ai",
  "needsUpdate": true,
  "recommendation": "Update menu from 'iac' to 'ai' to match new location"
}
```

### Update Process

If `needsUpdate: true`, offer user options:

1. **Update automatically** (recommended):
   - Detect appropriate parent identifier
   - Use Edit tool to update frontmatter
   - Show confirmation of changes

2. **Show manual instructions**:
   - Provide exact changes with line numbers
   - Let user edit manually

3. **Skip**:
   - Warn that file will appear in wrong navigation section
   - Continue without update

### Automatic Update Implementation

Using the Edit tool:

```markdown
**Before**:
```yaml
menu:
    iac:
        name: MCP server
        parent: iac-guides-ai-integration
        weight: 6
```

**After**:
```yaml
menu:
    ai:
        name: MCP server
        parent: ai-home
        weight: 6
```

**Edit tool call**:
```python
Edit(
  file_path="content/docs/ai/mcp-server/index.md",
  old_string="""menu:
    iac:
        name: MCP server
        parent: iac-guides-ai-integration
        weight: 6""",
  new_string="""menu:
    ai:
        name: MCP server
        parent: ai-home
        weight: 6"""
)
```

## Manual Update Process

If automatic update isn't suitable:

1. **Open destination file** in editor
2. **Locate menu section** in frontmatter (usually lines 8-12)
3. **Update section identifier**: Change `iac:` → `ai:` (or appropriate section)
4. **Update parent identifier**: Change to appropriate parent in new section
5. **Preserve other fields**: Keep `name` and `weight` unchanged
6. **Save file**
7. **Verify**: Run `make build` to catch errors

### Manual Update Example

**File**: `content/docs/ai/mcp-server/index.md`

**Find**:
```yaml
menu:
    iac:
        name: MCP server
        parent: iac-guides-ai-integration
        weight: 6
```

**Replace with**:
```yaml
menu:
    ai:
        name: MCP server
        parent: ai-home
        weight: 6
```

## Verification After Update

### 1. Build Site

Hugo will catch invalid menu identifiers:

```bash
make build
```

Look for errors about undefined menu identifiers.

### 2. Serve Locally

Verify navigation structure:

```bash
make serve
```

**Check**:
- Page appears in correct section navigation (e.g., AI section, not IaC)
- Navigation hierarchy is correct
- Breadcrumbs show proper path

### 3. Check Navigation Placement

Navigate to: `http://localhost:1313/docs/ai/mcp-server/`

**Verify**:
- Left sidebar shows page in AI section
- Page appears under correct parent
- Weight ordering is reasonable

### 4. Breadcrumb Trail

Check that breadcrumbs reflect new location:
```
Home > AI > MCP server
```

Not old location:
```
Home > IaC > Guides > AI Integration > MCP server
```

## Edge Cases

### No Menu Frontmatter

Some files don't have menu entries (child pages that appear in parent's subtree):

```yaml
---
title: Child Page
# No menu section
---
```

**Action**: Skip menu update step, no changes needed.

### Multiple Menu Entries

Some pages appear in multiple menus:

```yaml
menu:
    iac:
        name: Page Name
        parent: iac-home
    ai:
        name: Same Page
        parent: ai-home
```

**Action**: Update all menu sections that reference the old location.

### Moving Within Same Section

File moves from `content/docs/iac/old/` to `content/docs/iac/new/`:

**Action**: Parent may need updating, but section stays `iac`. Check parent validity.

### Unknown Destination Section

File moves to unrecognized path (e.g., `content/docs/tutorials/`):

**Action**: Warn user, request manual parent identifier input.

### Weight Conflicts

After move, weight might conflict with siblings:

**Original**: `weight: 6` in old location
**New location**: Siblings use weights 1, 2, 3, 4, 5

**Action**:
- Keep weight 6 initially (appears last)
- User can adjust later if desired
- Don't automatically renumber

### Malformed Menu YAML

Indentation or syntax errors in menu section:

```yaml
menu:
  iac:  # Wrong indentation (should be 4 spaces)
  name: Page
```

**Action**:
- Report parsing error
- Offer manual update guidance
- Don't attempt automatic fix (risk making it worse)

## Integration with Move Workflow

### Step 3.5: Analyze and Update Menu Frontmatter

After file moved (Step 3), before verification (Step 4):

1. **Run analysis script**:
   ```bash
   bash .claude/commands/move-doc/scripts/analyze-menu.sh "{source}" "{destination}"
   ```

2. **Parse JSON output** to check `needsUpdate`

3. **If no update needed**:
   - Display: "✓ Menu frontmatter matches destination section"
   - Continue to next step

4. **If update needed**:
   - Display recommendation and context
   - Offer options (automatic, manual, skip)
   - Execute chosen option
   - Display confirmation

5. **Store changes** for inclusion in final summary

## Common Mistakes

### Forgetting to Update Parent

**Wrong**:
```yaml
menu:
    ai:  # Updated section ✓
        parent: iac-guides-ai-integration  # Old parent ✗
```

**Right**:
```yaml
menu:
    ai:  # Updated section ✓
        parent: ai-home  # New parent ✓
```

### Using Non-Existent Parent

**Wrong**:
```yaml
menu:
    ai:
        parent: ai-mcp-server  # Doesn't exist in menus.yml ✗
```

**Right**:
```yaml
menu:
    ai:
        parent: ai-home  # Exists in menus.yml ✓
```

Verify parent exists: `grep "identifier: ai-home" config/_default/menus.yml`

### Changing Name Unnecessarily

**Wrong** (changing name during update):
```yaml
menu:
    ai:
        name: Model Context Protocol Server  # Changed ✗
```

**Right** (preserve name):
```yaml
menu:
    ai:
        name: MCP server  # Preserved ✓
```

Only update `section` and `parent`; keep `name` and `weight` unchanged unless explicitly requested.

## Best Practices

1. **Always run analysis script** when moving between sections
2. **Verify parent identifier** exists in menus.yml
3. **Test navigation** locally before committing
4. **Keep name and weight** unchanged during section moves
5. **Check breadcrumbs** to verify hierarchy
6. **Use automated update** when possible for consistency
7. **Document parent selection** in commit message if non-obvious

## Summary

Menu frontmatter updates ensure pages appear in correct navigation:

- **Detection**: Automated script identifies section boundary crossings
- **Parent discovery**: Algorithms find appropriate parent identifiers
- **Update options**: Automatic, manual, or skip with warnings
- **Verification**: Build site, test navigation, check breadcrumbs
- **Edge cases**: Handle no menu, multiple menus, malformed YAML

When moving files between sections, always update menu frontmatter to maintain navigation integrity.
