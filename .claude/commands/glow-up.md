---
description: Deep review and polish of a single documentation file and its images (comprehensive improvement suggestions).
---

# Usage

`/glow-up [file-path]`

**Use this when:** You want to significantly improve an existing documentation page with comprehensive suggestions for content, structure, clarity, and visuals.

Performs deep analysis and improvement of a single file, acting as a professional technical writer focused on making documentation clear, concise, and consistent with Pulumi style guidelines.

The `file-path` argument is optional. If not provided, the command will attempt to infer the target file from context (e.g., a file currently open in the IDE).

---

## Process

### 1. Determine target file

Determine which file to analyze:

**If a file path is provided** ({{arg}}):

- Use that file path as the target

**If no file path is provided**:

- DO NOT RUN ANY COMMANDS YET. First check the conversation context for system reminders
- Look for system reminders mentioning "The user opened the file" or similar context about open files in the IDE
- If an open file is found in the context, use that file path as the target
- If no open file is found, ask the user which file they want to analyze

Once the target file is determined, proceed with the analysis.

### 2. Read and analyze the file

Read the entire target file and perform comprehensive analysis.

**Base criteria**: Use `_common:review-criteria` as your foundation for quality standards. This command extends those criteria with proactive improvements and detailed image analysis specific to the glow-up workflow.

#### Text analysis

**Style violations:**

- Marketing language, superlatives, and filler words ("easy", "simple", "just", "very", "really", "obviously")
- Ableist or unnecessarily gendered language
- Violent/aggressive terms (e.g., "kill")
- Vague qualifiers that judge difficulty
- Passive voice constructions
- Overly complex or run-on sentences
- Spelling and grammar errors

**Structural issues:**

- Incorrect heading capitalization (H1 should be Title Case, H2+ should be Sentence case)
- Long paragraphs (more than 3 sentences)
- Missing blank lines around headings
- Skipped heading levels (e.g., H2 directly to H4)

**Code formatting:**

- Indented code blocks (should use fenced blocks with language identifiers)
- Missing language identifiers on fenced blocks
- Wrong language identifiers (e.g., `bash` vs `output`)
- Code examples that don't follow best practices or may not run correctly

**Terminology:**

- Incorrect capitalization of Pulumi terms (e.g., "Stack" instead of "stack")
- "Click" instead of "select"
- "Go to" instead of "navigate"
- Directional terms ("above", "below") instead of direct links

**Links and references:**

- Vague link text ("click here", "here", "this link")
- Missing cross-references to related documentation
- Broken or outdated links
- Links that don't resolve or point to wrong targets (404s, incorrect paths)

**Content quality:**

- Unclear explanations
- Missing context for users
- Unsourced claims or statistics
- Outdated information
- Missing code examples where helpful

**Front matter:**

- Missing or incomplete required fields (title, description, etc.)
- Meta descriptions that are inappropriate length or missing
- SEO issues with page titles or descriptions

**Content type considerations:**

- Consider whether the content is Documentation or Blog/Marketing material
- Apply appropriate style guidelines based on content type (see `_common:review-criteria` role-specific guidelines)
- Documentation should be clear and objective; blogs can be more engaging

#### Image and diagram analysis

For each image or diagram referenced in the document:

1. **Check for missing borders on PNG images**: Run the border detection script with dry-run mode to deterministically identify which PNG images need borders:

   ```bash
   cd /workspaces/src/pulumi/docs/scripts/image-borders && pipenv run python add_borders.py <file-path> --dry-run
   ```

   The script will report which images would be modified vs skipped.

2. Regardless of existing borders, use the Read tool to view the image and analyze the image for the following issues:

**Screenshots:**

- Missing or inadequate alt text (accessibility requirement)
- Outdated UI elements or styling that don't match current product (compare against `pulumi-cloud-console-current.png`)
  - **Pay special attention to left navigation!**
- Outdated Pulumi logos or branding (compare against `pulumi-logo-current.png`)
- Screenshots that need retaking due to rebranding
- Poor image quality or resolution
- File size optimization opportunities
- Unnecessary screenshots that could be replaced with text or code

**Diagrams:**

- Missing or unclear labels and legends
- Confusing visual flow or layout
- Inconsistent styling with other diagrams
- Diagrams that could be converted to text-based formats (Mermaid, GoAT/ASCII) for better maintainability
- Missing alt text descriptions

**Technical checks:**

- Image file format appropriateness (PNG vs JPG vs SVG)
- Whether the image adds value or is decorative
- Maintenance overhead concerns (per AGENTS.md: "Be wary of images due to maintenance overhead")

### 3. Load reference images (if needed)

**Only load reference images if the document contains screenshots or images.**

After reading the target file in step 2, check if it contains any image references (e.g., `![alt text](image-path)`). If no images are present, skip this step to avoid wasting tokens.

If the document contains screenshots, load the reference images to compare against:

1. Read `.claude/commands/_common/images/pulumi-logo-current.png` to see the current Pulumi logo
2. Read `.claude/commands/_common/images/pulumi-cloud-console-current.png` to see the current Cloud Console UI

These references represent current branding standards. Use them to:

- Compare logos in screenshots against the current logo
- Compare Cloud Console UI elements against the current design
- Make confident assessments about what's outdated
- Identify specific differences (e.g., "logo uses old color scheme", "UI shows deprecated navigation structure")

### 4. Review guidelines

Before proposing changes, verify understanding of:

- `STYLE-GUIDE.md` — Pulumi-specific style rules (headings, links, code blocks, terminology)
- `AGENTS.md` — Repository conventions and build workflow
- Google Developer Documentation Style Guide — For topics not covered in STYLE-GUIDE.md

### 5. Create improvement plan

Develop a detailed plan organized by issue category:

**1. Style improvements** — List specific instances with line numbers:

- Marketing language to remove or rewrite
- Passive voice to convert to active
- Complex sentences to simplify
- Problematic language to replace

**2. Structural fixes** — List specific instances with line numbers:

- Headings to re-capitalize
- Paragraphs to break up
- Heading levels to adjust
- Blank lines to add

**3. Code formatting** — List specific instances with line numbers:

- Indented blocks to convert to fenced blocks
- Missing language identifiers to add
- Incorrect language identifiers to fix

**4. Terminology corrections** — List specific instances with line numbers:

- Incorrect capitalizations
- Terms to replace per style guide

**5. Link improvements** — List specific instances with line numbers:

- Vague link text to make descriptive
- Missing cross-references to add
- Broken links to fix

**6. Image and diagram improvements** — List specific issues with file paths:

- Missing alt text to add (include suggested alt text)
- Outdated screenshots to flag for replacement (describe what's outdated)
- **Logo issues** (old Pulumi branding, deprecated product logos)
- Unclear diagrams to improve or replace
- Images to convert to Mermaid/GoAT
- Unnecessary images to remove
- File format or size optimizations
- PNG images that need 1px grey borders for visual clarity

**7. Content enhancements** — List specific recommendations:

- Unclear sections that need rewriting
- Missing context to add
- Code examples to add or improve
- Outdated information to update

**8. Estimated impact:**

- Minor tweaks (< 10 changes)
- Moderate improvements (10-30 changes)
- Major rewrite (> 30 changes or significant restructuring)

### 6. Present plan for approval

**IMPORTANT: Do NOT implement changes without user approval.**

Present the complete plan with:

- Clear categories of improvements
- Specific line numbers for text issues
- Specific file paths for image issues
- Before/after examples for significant changes
- **For images with logo/branding issues**: Describe what you see, compare against reference images, and explain specific differences
- Total count of issues found
- Estimated scope of work

Ask the user:

- Whether to proceed with all improvements
- Whether to focus on specific categories only
- Whether any proposed changes need discussion
- **For screenshot/image issues**: Whether images should be flagged for manual update or removed

### 7. Execute improvements

Once approved, implement the changes in logical order:

1. **Structural fixes** (headings, blank lines, paragraph breaks)
2. **Code formatting** (convert indented blocks, add language identifiers)
3. **Terminology** (fix capitalizations, replace terms)
4. **Style improvements** (remove filler, simplify sentences, active voice)
5. **Link improvements** (improve link text, add cross-references)
6. **Image improvements** (add alt text, remove unnecessary images, flag outdated screenshots)
7. **Add borders to PNG images** (run `/add-borders <file-path>` if PNG images need borders)
8. **Content enhancements** (rewrite unclear sections, add context)

Use the TodoWrite tool to track progress through the improvements.

**Note on images**: You can add/improve alt text and remove unnecessary image references, but you cannot update screenshot content or logos. Flag these issues for the user to address manually.

### 8. Verify changes

After implementing improvements:

1. Run `make lint` to ensure no formatting errors
2. Check that local links resolve to actual files (external links are verified by CI)
3. Verify technical accuracy is preserved
4. Confirm the tone matches other documentation in the same section
5. Review that the file ends with a newline
6. Verify all images have appropriate alt text

Report verification results to the user, including any flagged images that need manual updates.

---

## Guidelines

**Do:**

- Be thorough in identifying issues
- Preserve technical accuracy
- Maintain the author's intended meaning
- Follow STYLE-GUIDE.md strictly
- Make the documentation more accessible and clear
- Add helpful cross-references to related docs
- View all images referenced in the document
- Flag outdated branding and logos
- Suggest text-based diagram alternatives (Mermaid/GoAT) when appropriate

**Don't:**

- Change technical details without verification
- Remove useful examples or explanations
- Make the documentation less comprehensive
- Add unnecessary verbosity
- Change headings in ways that break existing links (check for inbound references first)
- Proceed with changes before user approval
- Attempt to edit image files directly (flag for manual update instead)

**Tone:**

- Documentation should be clear, objective, and professional
- Avoid marketing language and hype
- Be specific and factual
- Use examples to clarify concepts
- Focus on helping users accomplish their goals

**Image analysis guidelines:**

- Only load reference images (`.claude/commands/_common/images/pulumi-logo-current.png` and `.claude/commands/_common/images/pulumi-cloud-console-current.png`) if the document contains screenshots or images
- Compare screenshots against reference images rather than relying on memory
- Always use the Read tool to view images before commenting on them
- Be specific about what appears outdated (UI elements, logos, branding)
- When identifying outdated elements, reference specific differences from the current standards
- Consider maintenance overhead when evaluating whether images are necessary
- Prefer text-based diagrams (Mermaid/GoAT) over static images when feasible
- Ensure all images serve a clear purpose and add value
