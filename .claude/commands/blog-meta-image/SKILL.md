---
name: blog-meta-image
description: "Generate a meta image (Open Graph / social share) for a blog post. Reads the blog post title, selects a pre-composed template (dark/light, mascot/logos), and renders a 1200x628 PNG. Use when the user types /blog-meta-image or asks to create, generate, or regenerate a blog post's meta image, social card, or Open Graph image. Accepts optional arguments like theme, mascot style, or logo names."
---

# `/blog-meta-image` — Generate Blog Meta Image

You are generating a meta image for a Pulumi blog post. Follow these steps precisely.

**Skill directory**: `.claude/commands/blog-meta-image/` — all paths below are relative to the project root unless noted.

## [Step 1/4] Find the Blog Post

Locate the blog post that needs a meta image:

1. If `$ARGUMENTS` contains a file path, use that directly.
2. Otherwise, run `git status` and `git diff --name-only` to find modified/untracked `content/blog/*/index.md` files.
3. If multiple blog posts are found, use `AskUserQuestion` to ask which one.
4. If no blog post is found, ask the user to specify a path.

Read the full blog post file (frontmatter + body).

## [Step 2/4] Parse Blog Content & User Requests

### From the blog post, extract:
- **Title**: the `title:` field from YAML frontmatter — this becomes the text on the image
- **Tags**: the `tags:` array from frontmatter
- **Topics**: scan the body for key signals — cloud providers (AWS, Azure, GCP), languages (Go, Python, TypeScript), technologies (Kubernetes, Terraform, Docker), features (ESC, secrets, OIDC, policy), concepts (AI, ML, platform engineering, IDP)

### From `$ARGUMENTS`, parse user preferences:
- **Theme**: "dark" or "light"
- **Style**: "mascot", "flying", "closeup", "wireframe", "shield", or logo names like "aws kubernetes"
- **Title override**: if the user explicitly provides different text in quotes, use that instead of the blog title

If `$ARGUMENTS` fully specifies the template (e.g., `/blog-meta-image dark flying`), skip the interactive questions and go straight to Step 3's rendering. If partially specified, only ask about the unspecified parts.

## [Step 3/4] Select Template & Render

Read the asset catalog reference at `.claude/commands/blog-meta-image/references/asset-catalog.md` for the full template list and logo inventory.

### Interactive Selection (3 progressive questions)

Ask the following questions **progressively** (one at a time) using `AskUserQuestion`. Skip any question that was already answered via `$ARGUMENTS`.

---

### Question 1: Theme

```
header: "Theme"
question: "Dark or light background?"
options:
  - label: "Dark"
    description: "Deep purple gradient with grid lines"
  - label: "Light"
    description: "Lighter purple gradient with grid lines"
```

---

### Question 2: Style

```
header: "Style"
question: "Feature a Pulumipus mascot or product logos?"
options:
  - label: "Pulumipus mascot"
    description: "One of 4 Pulumipus character poses on the right side"
  - label: "Product logos"
    description: "1-3 product/technology logo SVGs on white placeholder shapes"
```

---

### Question 3a (if Pulumipus mascot): Which mascot?

```
header: "Mascot"
question: "Which Pulumipus style?"
options:
  - label: "Flying"
    description: "3D Pulumipus flying with wings spread and sunglasses"
  - label: "Closeup"
    description: "3D teal Pulumipus head closeup with big sunglasses"
  - label: "Wireframe"
    description: "Purple line-art wireframe outline of Pulumipus"
  - label: "Shield"
    description: "3D Pulumipus holding a shield with sunglasses"
```

The selected mascot + theme determines the template file. For example: dark + flying = `templates/dark-flying.png`.

---

### Question 3b (if Product logos): Which logos?

```
header: "Logos"
question: "Which product/technology logos? (select 1-3)"
multiSelect: true
```

Based on technologies detected in the blog post (AWS, Kubernetes, TypeScript, Docker, etc.), present up to 4 relevant logos from the catalog. Example:
- "AWS" — `logos/aws.svg`
- "Kubernetes" — `logos/kubernetes.svg`
- "Docker" — `logos/docker.svg`
- "TypeScript" — `logos/typescript.svg`

The number of selected logos (1, 2, or 3) determines which template to use (`logo-1`, `logo-2`, or `logo-3`). If more than 3 are selected, ask the user to narrow down to 3.

**Logo lookup**: Check `assets/logos/` first. If a needed logo isn't found locally:
1. Try [simple-icons](https://github.com/simple-icons/simple-icons/tree/develop/icons) first — clean vector SVGs for 3000+ brands. Download from `https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg` and add a `fill` attribute with the brand color to `<path>` elements.
2. Otherwise use `WebSearch` to find the official SVG (`"<technology> logo SVG site:github.com"`)
3. Use `WebFetch` to download the SVG content
4. Save it to `.claude/commands/blog-meta-image/assets/logos/<name>.svg`

---

### Template Resolution

Combine theme + style to determine the template file:

| Theme | Style | Template |
|-------|-------|----------|
| dark | flying | `templates/dark-flying.png` |
| dark | closeup | `templates/dark-closeup.png` |
| dark | wireframe | `templates/dark-wireframe.png` |
| dark | shield | `templates/dark-shield.png` |
| dark | 1 logo | `templates/dark-logo-1.png` |
| dark | 2 logos | `templates/dark-logo-2.png` |
| dark | 3 logos | `templates/dark-logo-3.png` |
| light | flying | `templates/light-flying.png` |
| light | closeup | `templates/light-closeup.png` |
| light | wireframe | `templates/light-wireframe.png` |
| light | shield | `templates/light-shield.png` |
| light | 1 logo | `templates/light-logo-1.png` |
| light | 2 logos | `templates/light-logo-2.png` |
| light | 3 logos | `templates/light-logo-3.png` |

### Build Composition Config

Build a JSON config. For mascot templates:

```json
{
  "template": "templates/dark-flying.png",
  "text": {
    "content": "Blog Post Title Here",
    "font_size": 71
  },
  "logos": []
}
```

For logo templates (use `max_width: 520` to avoid overlapping logo placeholders):

```json
{
  "template": "templates/dark-logo-2.png",
  "text": {
    "content": "Blog Post Title Here",
    "font_size": 71,
    "max_width": 520
  },
  "logos": [
    "logos/aws.svg",
    "logos/kubernetes.svg"
  ]
}
```

**Font size guidelines:**
- Short titles (1-3 words): `font_size: 80`
- Medium titles (4-8 words): `font_size: 71`
- Long titles (9+ words): `font_size: 56`
- Very long titles (15+ words): `font_size: 44`

**Important**: Paths in the JSON config are relative to the `--assets-dir` directory.

### Environment Setup (first time only)

Before rendering, ensure `uv` is installed:

```bash
which uv
```
If not found, install it:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

No `uv sync` is needed — the script has inline PEP 723 metadata declaring its own dependencies (`cairosvg`, `pillow`, `pyyaml`), so `uv run` handles installation automatically.

### Rendering

1. Write the JSON config to a temporary file named after the blog post slug (e.g., `/tmp/meta-<slug>.json`, where `<slug>` is the blog directory name like `my-post`)
2. Determine the blog post directory (e.g., `content/blog/my-post/`)
3. The composition script is at `.claude/commands/blog-meta-image/scripts/compose_meta_image.py`
4. The assets directory is at `.claude/commands/blog-meta-image/assets/`
5. Run with `uv run`:
   ```bash
   uv run .claude/commands/blog-meta-image/scripts/compose_meta_image.py \
     --config /tmp/meta-<slug>.json \
     --assets-dir .claude/commands/blog-meta-image/assets \
     --output <blog-dir>/meta.png
   ```

## [Step 4/4] Confirm & Update Frontmatter

1. Verify the PNG was created successfully at the expected path
2. Check the blog post's frontmatter for `meta_image:` — if missing or set to something else, update it:
   ```yaml
   meta_image: meta.png
   ```
3. Report to the user:
   - Which blog post was used
   - What template was selected (theme + style) and why
   - What logos were placed (if any)
   - Where the meta.png was saved
   - Remind them to preview the image to make sure it looks good

## Error Handling

- If `compose_meta_image.py` fails, read the error output and try to fix the config (common issues: invalid SVG path, missing template file)
- If a requested logo name doesn't match anything in the catalog, suggest the closest matches and ask the user
- If the blog post has no title, ask the user for one
