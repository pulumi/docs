---
name: meta
description: "Generate a meta image (Open Graph / social share) for a blog post. Reads the blog post title, selects backgrounds/mascots/patterns from the asset library, and renders a 1200x600 PNG. Use when the user types /meta or asks to create, generate, or regenerate a blog post's meta image, social card, or Open Graph image. Accepts optional arguments for specific mascots, background colors, patterns, or styles."
---

# `/meta` — Generate Blog Meta Image

You are generating a meta image for a Pulumi blog post. Follow these steps precisely.

**Skill directory**: `.claude/commands/meta/` — all paths below are relative to the project root unless noted.

## [Step 1/5] Find the Blog Post

Locate the blog post that needs a meta image:

1. If `$ARGUMENTS` contains a file path, use that directly.
2. Otherwise, run `git status` and `git diff --name-only` to find modified/untracked `content/blog/*/index.md` files.
3. If multiple blog posts are found, use `AskUserQuestion` to ask which one.
4. If no blog post is found, ask the user to specify a path.

Read the full blog post file (frontmatter + body).

## [Step 2/5] Parse Blog Content & User Requests

### From the blog post, extract:
- **Title**: the `title:` field from YAML frontmatter — this becomes the text on the image
- **Tags**: the `tags:` array from frontmatter
- **Topics**: scan the body for key signals — cloud providers (AWS, Azure, GCP), languages (Go, Python, TypeScript), technologies (Kubernetes, Terraform, Docker), features (ESC, secrets, OIDC, policy), concepts (AI, ML, platform engineering, IDP)

### From `$ARGUMENTS`, parse user preferences:
- **Mascot names**: fuzzy-match against catalog (e.g., "einstein" -> `einsteinypus.svg`, "wizard" -> `wizard.svg`, "rocket" -> `rocket.svg`, "detective" -> `detectypus.svg`)
- **Background color**: "purple", "dark blue", "salmon", "rose", etc.
- **Background style**: "gradient", "flat", "dark"
- **Pattern**: "hexagons", "stars", "circuits", "dots", etc.
- **Layout requests**: "two mascots", "no pattern", "no mascot", etc.
- **Title override**: if the user explicitly provides different text in quotes, use that instead of the blog title

If the user provides no `$ARGUMENTS`, proceed to the interactive asset selection in Step 3 (all 5 questions will be asked). If `$ARGUMENTS` specifies some assets, only the unspecified categories will be asked interactively.

## [Step 3/5] Select Assets (Interactive)

Read the asset catalog reference at `.claude/commands/meta/references/asset-catalog.md` for the full asset list and topic-to-asset mapping table.

Use your topic analysis from Step 2 to **curate the best 4 options** for each question below. Present options that match the blog's themes, mixing variety (e.g., dark/light, gradient/flat) so the user has meaningful choices.

**Arguments override**: If the user provided explicit assets in `$ARGUMENTS` (e.g., `/meta wizard dark-purple circuits`), **skip the interactive question for that category** and use the specified asset directly. Only ask about categories the user didn't specify.

Ask the following questions **progressively** (one at a time) using `AskUserQuestion`. Each question should have exactly 4 options (the "Other" escape hatch is provided automatically by the tool).

---

### Question 1: Background Color

```
header: "Background"
question: "Which background color fits this post?"
```

Present 4 backgrounds from the catalog based on topic analysis. Mix gradient/flat and dark/light for variety. Example options for an AI post:
- "Dark purple gradient" — `horizontal-gradient-dark-purple.svg`
- "Violet-blue gradient" — `horizontal-gradient-violet-blue.svg`
- "Lavender gradient" — `horizontal-gradient-lavender.svg`
- "Flat dark blue" — `flat-dark-blue.svg`

Use descriptive labels (color + style). Put the description as the filename so the user can confirm. **Skip if `$ARGUMENTS` specified a background.**

---

### Question 2: Pattern Overlay

```
header: "Pattern"
question: "Which pattern overlay should we use?"
```

Present 3 content-matched patterns + 1 "None (clean look)" option. Example for a cloud post:
- "Clouds" — `clouds.svg`
- "Circuits" — `circuits.svg`
- "Stars" — `stars.svg`
- "None (clean look)" — no pattern

**Skip if `$ARGUMENTS` specified a pattern or "no pattern".**

---

### Question 3: Mascot

```
header: "Mascot"
question: "Which Pulumipus mascot should appear?"
```

Present 4 topic-matched mascots from the catalog. Example for a fun AI post:
- "Chill Hoodie" — `chill-hoodie.svg`
- "AI Code" — `pulumipus_ai-code.svg`
- "Wizard" — `wizard.svg`
- "Flying Sparkles" — `flying-sparkles.svg`

**Skip if `$ARGUMENTS` specified a mascot or "no mascot".**

---

### Question 4: Decorative Stamp

```
header: "Stamp"
question: "Add a decorative stamp accent?"
```

Present 3 thematic stamps + 1 "None" option:
- "Sparkles" — `sparkles-stamp.svg`
- "Lightning" — `lightning-stamp.svg`
- "Cloud" — `cloud-stamp.svg`
- "None"

**Skip if `$ARGUMENTS` specified a stamp or "no stamp".**

---

### Question 5: Product / Technology Logo

```
header: "Logo"
question: "Add a product or technology logo?"
```

Based on technologies detected in the blog post (AWS, Kubernetes, TypeScript, Docker, etc.), present up to 3 relevant logos + 1 "None" option. Example for a Kubernetes-on-AWS post:
- "AWS logo"
- "Kubernetes logo"
- "Docker logo"
- "None"

If the user picks a logo:
1. Check if the SVG already exists in `assets/logos/` (e.g., `aws.svg`, `kubernetes.svg`)
2. If not found locally, use `WebSearch` to find the official SVG (search for `"<technology> logo SVG site:github.com"` or `"<technology> brand guidelines SVG"`)
3. Use `WebFetch` to download the SVG content from the official source
4. Save it to `.claude/commands/meta/assets/logos/<name>.svg`
5. Add it as an overlay in the composition config (position it as a small accent, 80-120px, typically in the top-right area or near the mascot, avoiding text overlap)

**Skip if `$ARGUMENTS` specified a logo or "no logo".**

---

### Handling "Other" responses

If the user selects "Other" and types a custom value for any question, fuzzy-match their input against the full asset catalog. If no close match is found, ask for clarification.

### Text color logic (automatic, not interactive)

After the background is selected:
- Dark backgrounds (`is_dark: true` in the catalog) → white text `#FFFFFF`
- Light backgrounds (`is_dark: false` in the catalog) → dark text `#1B1B1B`

## [Step 4/5] Generate Composition JSON & Render

Build a JSON config file and run the composition engine. The config schema:

```json
{
  "background": "backgrounds/<filename>.svg",
  "pattern": "patterns/<filename>.svg",
  "text": {
    "content": "The Blog Post Title Goes Here",
    "x": 80,
    "y": 180,
    "font_size": 46,
    "font_weight": "bold",
    "color": "#FFFFFF",
    "max_width": 620
  },
  "overlays": [
    {
      "svg_path": "mascots/<filename>.svg",
      "width": 420,
      "height": 420,
      "x": 740,
      "y": 180
    }
  ]
}
```

**Important**: Paths in the JSON config are relative to the `--assets-dir` directory. Use paths like `backgrounds/flat-blue.svg`, `mascots/wizard.svg` — do NOT prefix with `assets/`.

### Layout guidelines:

**Text positioning:**
- `x`: always 80
- `y`: 160-220 depending on title length (shorter title -> lower y for vertical centering)
- `font_size`: 44-48 (use 44 for very long titles, 48 for short ones)
- `max_width`: 580-650 (leave room for mascot on right; use 580 if mascot is large)

**Mascot positioning (single mascot):**
- Typically placed right side: `x` = 700-850, depending on mascot width
- Bottom-aligned: calculate `y` so mascot bottom edge is near y=600
  - Formula: `y = 600 - mascot_height` (adjust slightly so mascot isn't clipped)
- Scale mascot to fit: `width` and `height` should be 350-500px, maintaining aspect ratio
- The mascot dimensions from the catalog are the *native* SVG dimensions — scale proportionally to fit within your target bounding box

**Multiple mascots (only if user requests):**
- First mascot: x=650, bottom-aligned
- Second mascot: x=900, bottom-aligned, slightly smaller
- Stagger y positions for visual interest

**Stamps/icons (optional accent):**
- Place stamps in decorative positions: top-right corner, or near the mascot
- Keep small: 80-150px
- Don't overlap text

**Pattern:**
- Set `"pattern"` key at the top level (not in overlays)
- If no pattern desired, omit the `"pattern"` key entirely

### Environment Setup (first time only)

Before rendering, ensure `uv` is installed:

```bash
which uv
```
If not found, install it:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No `uv sync` is needed — the script has inline PEP 723 metadata declaring its own dependencies (`cairosvg`, `pillow`), so `uv run` handles installation automatically regardless of which project directory you're in.

### Rendering:

1. Write the JSON config to a temporary file (e.g., `/tmp/meta-config.json`)
2. Determine the blog post directory (e.g., `content/blog/my-post/`)
3. The composition script is at `.claude/commands/meta/scripts/compose_meta_image.py`
4. The assets directory is at `.claude/commands/meta/assets/`
5. Run with `uv run` (handles venv activation automatically):
   ```bash
   uv run .claude/commands/meta/scripts/compose_meta_image.py \
     --config /tmp/meta-config.json \
     --assets-dir .claude/commands/meta/assets \
     --output <blog-dir>/meta.png
   ```
   If `uv run` fails, check that `uv` is installed and that the script's inline metadata is intact.

## [Step 5/5] Confirm & Update Frontmatter

1. Verify the PNG was created successfully at the expected path
2. Check the blog post's frontmatter for `meta_image:` — if missing or set to something else, update it:
   ```yaml
   meta_image: meta.png
   ```
3. Report to the user:
   - Which blog post was used
   - What assets were selected (background, pattern, mascot, stamps) and why
   - Where the meta.png was saved
   - Remind them to preview the image to make sure it looks good

## Error Handling

- If `compose_meta_image.py` fails, read the error output and try to fix the config (common issues: invalid SVG path, mascot positioned off-canvas)
- If a requested asset name doesn't match anything in the catalog, suggest the closest matches and ask the user
- If the blog post has no title, ask the user for one
