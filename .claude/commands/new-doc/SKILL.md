---
name: new-doc
description: |
  Create Pulumi documentation with proper frontmatter and menu structure. 

  Use when Claude needs to: (1) Create a new documentation page, (2) Set up an index page (_index.md) with sections, (3) Add
  pages to the Hugo menu system with proper weights and identifiers, (4) Generate SEO-optimized metadata.
---

# new-doc

Create documentation pages with proper frontmatter, menu structure, and SEO optimization.

## Core Principles

**CRITICAL**: Complete all 7 steps in sequence. Display progress as **[Step X/7]** before each step.

**Important**:

- **Always display all 7 steps**: Even when skipping a step, display it with an explanation (e.g., "[Step 2/7] Skipped - using suggested location from Step 1")
- **Minimize open-ended questions**: Use AskUserQuestion with prepopulated suggestions for nearly all inputs. Always provide smart defaults based on context.
- **Store decisions**: Track choices to avoid re-asking
- **Check for existing docs first**: Prevent duplication

## Workflow Overview

1. **[Step 1/7]** Gather context, check existing docs, suggest page type/location
2. **[Step 2/7]** Confirm suggestions or navigate manually
3. **[Step 3/7]** Interactive directory navigation (if needed)
4. **[Step 4/7]** Gather content details (title, meta_desc, etc.)
5. **[Step 5/7]** Calculate menu weight
6. **[Step 6/7]** Generate menu metadata (identifier, parent, meta_image)
7. **[Step 7/7]** Create file and validate

## Steps

### [Step 1/7] Gather Context and Check Existing Docs

**Ask**: What are you documenting?

**Check for existing docs** using Grep with key terms from user's description:

```bash
# Extract 2-3 key terms from user's description and search
grep -ri "key_terms" /workspaces/src/pulumi/docs/content/docs/ --include="*.md" | head -10
```

**If existing docs found:**

Analyze the results and categorize:

- **Nearly identical topic**: Existing page covers the same concept
- **Related but distinct**: Existing pages cover adjacent/related topics

Then use AskUserQuestion:

```text
# If nearly identical:
Question: "I found existing documentation on this topic at {path}. What would you like to do?"
Options:
- "Update existing page (Recommended)"
- "Create new page anyway"

# If related but distinct:
Question: "I found related documentation at {path1}, {path2}. What would you like to do?"
Options:
- "Create new page (Recommended)"
- "Update one of the existing pages"
```

**Actions based on response:**

- If update: Use Read to open the existing file, present to user, exit workflow
- If create: Continue with new page creation

**If not found**: Display "No existing documentation found. Proceeding with new page creation." and continue.

**Suggest based on keywords** (see [directory-hints.md](references/directory-hints.md) for complete mapping):

Common patterns:

- **Concepts** (iac/concepts): "what is", "understanding", "overview"
- **Guides** (iac/guides): "how to", "guide", "tutorial"
- **Clouds** (iac/clouds/[provider]): AWS, Azure, GCP, Kubernetes
- **Languages** (iac/languages-sdks/[lang]): TypeScript, Python, Go, .NET, Java, YAML

**Present suggestions via AskUserQuestion:**

```text
Question: "I've analyzed your description. How would you like to proceed?"
Options:
- "Use suggested location (Recommended)"
- "Choose different location"
- "Let me refine my description"
```

Store choice. If "Use suggested location", skip to Step 4. Don't re-ask page type.

### [Step 2/7] Confirm or Navigate

**Always display this step**, even if skipping.

Based on the user's response to the Step 1 question:

- **"Use suggested location"**:
  - Display: "[Step 2/7] Confirmed - using suggested location: /docs/{path}"
  - Display: "[Step 3/7] Skipped - location already determined"
  - Store the suggested path and page type
  - Skip to Step 4 to gather content details

- **"Choose different location"**:
  - Display: "[Step 2/7] User chose different location, proceeding to interactive navigation"
  - Proceed to Step 3 for interactive navigation

- **"Let me refine my description"**:
  - Display: "[Step 2/7] User refining description"
  - Ask user for clarification, then re-run Step 1 analysis

**Important**: Page type (regular vs index) is already determined by this point. Don't ask again.

### [Step 3/7] Interactive Navigation (if needed)

**CRITICAL**: Display locations by menu weight (NOT alphabetically) to match left-nav order.

```bash
# For each subdirectory, extract title and weight
for dir in $(ls -1 {path}/ | grep -v "^_" | grep -v "^\."); do
  index_file="{path}/$dir/_index.md"
  if [ -f "$index_file" ]; then
    title=$(grep -m1 "^title:" "$index_file" | sed 's/title: *//' | tr -d '"')
    weight=$(grep -A10 "^menu:" "$index_file" | grep -m1 "weight:" | grep -oE '[0-9]+')
    echo "${weight:-999}|${title:-$dir}|$dir"
  else
    echo "999|$dir|$dir"
  fi
done | sort -n -t'|' -k1 | nl -w1 -s'. '
```

**Display format:**

```text
Current location: docs > Infrastructure as Code

Available subsections:
1. Get Started (get-started)
2. Guides (guides)
3. Concepts (concepts)
...
```

**Then ask via AskUserQuestion:**

```text
Question: "Where should this page be placed?"
Options:
- "1. Get Started (get-started)"
- "2. Guides (guides)"
- "3. Concepts (concepts)"
- "Place it here in current directory"
- "Enter path manually"
- "Go up one level"
```

**Navigation flow:**

- If number selected: Navigate into that subdirectory, repeat
- If "Place it here": Stop navigation
  - Regular pages: Create `{slug}.md` in current directory
  - Index pages: Create `_index.md` if it doesn't exist
- If "Enter path manually": Prompt for full path, validate, and use it
- If "Go up": Move to parent directory, repeat (handle root gracefully)

Continue navigation until placement is determined.

### [Step 4/7] Gather Content Details

Gather all required metadata using AskUserQuestion with smart suggestions.

**For regular pages**, follow all patterns in [questions-regular.md](references/questions-regular.md):

1. Title (with Title Case suggestion)
2. Title tag (with "| Pulumi Docs" format)
3. Meta description (50-160 chars validation)
4. Filename (kebab-case validation)

**For index pages**, follow patterns in [questions-index.md](references/questions-index.md):

- Part 1: Basic metadata (8 fields with smart suggestions)
  - Title, Link title, H1, Meta description, Description HTML
  - Primary button (label + link)
  - Secondary button (optional)
- Part 2: Sections array (iterative builder with card patterns)
  - Section type, heading, cards
  - Button cards, logo label cards, or flat text
  - Continue loop for multiple sections

**Ask about content generation (regular pages only):**

```text
Question: "Should I generate a rough draft of the content?"
Options:
- "No, just create a stub with instructions (Recommended)"
- "Yes, generate a rough draft"
```

Store the choice. If "Yes", prepare to generate content in Step 7. If "No", use default stub template.

Then proceed to Step 4b for index pages, or Step 5 for regular pages.

### [Step 4b/7] Build Sections Array (Index Pages)

For index pages only, build the sections array iteratively following the complete patterns in [questions-index.md - Part 2](references/questions-index.md#part-2-sections-array-builder).

**For each section:**

1. Select section type (button-cards, cards-logo-label-link, or flat)
2. Gather section heading
3. If button-cards or cards-logo-label-link:
   - Determine card count (2-4 typical)
   - For each card: gather emoji/icon, heading, description, link
4. If flat: gather description paragraph
5. Ask if user wants to add another section

**Validation**: Ensure at least one section exists before proceeding to Step 5.

### [Step 5/7] Calculate Menu Weight

**Display**: "[Step 5/7] Calculating menu weight..."

Find the maximum weight in the target directory:

```bash
# Find max weight in target directory
find {path} -name "*.md" -maxdepth 1 -exec grep -h "weight:" {} \; 2>/dev/null | grep -oE '[0-9]+' | sort -n | tail -1
```

**Logic:**

- No pages: suggest 10
- Pages exist: max weight rounded up to next multiple of 10
- Index pages: top-level suggest 1, subsection suggest 10+

**Display result**: "Calculated weight: {weight}"

### [Step 6/7] Generate Menu Metadata

**Display**: "[Step 6/7] Generating menu metadata..."

**Identifier**: `{section}-{subsection}-{slug}` or `{section}-{subsection}-home` for index pages

**Check uniqueness:**

```bash
grep -rh "identifier:" /workspaces/src/pulumi/docs/content/docs/{section}/ | grep "{identifier}"
```

If conflict, append `-2`, `-3`, etc.

**Parent**:

- Regular pages: identifier of _index.md in same directory
- Top-level index: no parent
- Subsection index: identifier of parent directory's _index.md

**Meta image**: Use cloud-specific images for AWS, Azure, GCP, Kubernetes paths, default for others.

**For complete mapping**: See [meta-images.md](references/meta-images.md)

**Display result**: "Menu identifier: {identifier}, Parent: {parent}, Meta image: {meta_image}"

### [Step 7/7] Create File and Validate

**Display**: "[Step 7/7] Creating file and validating..."

Run validation checks from [validation.md](references/validation.md):

- File doesn't exist
- Parent identifier exists
- Menu identifier unique
- Weight reasonable (0 < w < 1000)
- All required frontmatter present
- YAML valid
- Kebab-case filename (regular pages)
- Meta desc 50-160 chars
- Links valid (start with `/docs/` or external)

Create file using templates from [frontmatter.md](references/frontmatter.md):

- **Regular pages**: Use regular page template with title, title_tag, meta_desc, menu structure
  - **If rough draft requested**: Generate initial content sections based on the user's description and context
  - **If stub only** (default): Use this template after frontmatter:

    ```markdown

    ## Overview

    <!-- TODO: Add overview of this topic -->

    ## Prerequisites

    <!-- TODO: List any prerequisites or requirements -->

    ## Next steps

    <!-- TODO: Add links to related documentation or next steps -->
    ```

- **Index pages**: Use index page template with sections array, link_buttons, docs_home flags (no additional content needed)

Display success output as defined in [validation.md](references/validation.md):

```text
✅ Created at /docs/{path}/{filename}.md
✅ Identifier: {identifier} (unique)
✅ Parent: {parent} (validated)
✅ Weight: {weight}
✅ Meta desc: {length} chars

Preview: http://localhost:1313/docs/{path}/
Next: Write content, run /docs-review, run make lint
```

## Error Handling

For complete error handling strategies, see [validation.md - Error Handling](references/validation.md#error-handling).

Common scenarios:

- File exists: Suggest alternatives or ask to overwrite
- Invalid filename: Auto-suggest kebab-case correction
- Missing parent: Warn about navigation issues, offer to create
- Duplicate identifier: Auto-append `-2`, `-3` until unique
- Empty sections (index pages): Require at least one section before proceeding

## Repository-Specific Notes

- H1 = Title Case, H2+ = Sentence case (per STYLE-GUIDE.md)
- Aliases only for moved files, not new pages
- Weight spacing: multiples of 10 for easy insertion
- Index pages need: `docs_home: true`, `notitle: true`, `norightnav: true`
- Menu section = first directory under `/docs/` (e.g., `/docs/iac/...` → section: `iac`)
