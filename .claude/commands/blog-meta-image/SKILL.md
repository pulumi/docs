---
name: blog-meta-image
description: "Generate a feature image (1884x1256) and OpenGraph meta image (1200x628) for a blog post. Reads the blog post title, selects a feature template (neo, platform, rocket, shield, lightbulb, or logo variant), renders feature.png, then composites it with title text onto meta.png. Use when the user types /blog-meta-image or asks to create, generate, or regenerate a blog post's feature image, meta image, social card, or Open Graph image. Accepts optional arguments like feature template name or logo names."
---

# `/blog-meta-image` — Generate Blog Feature & Meta Images

You are generating two images for a Pulumi blog post: a **feature image** (1884×1256) and a **meta/OpenGraph image** (1200×628). Follow these steps precisely.

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
- **Feature template**: name of a feature template (e.g., "neo", "platform", "rocket", "shield", "lightbulb") or logo names like "aws kubernetes"
- **Title override**: if the user explicitly provides different text in quotes, use that instead of the blog title

### Fast-path: existing feature image with no frontmatter declaration

Check whether `feature.png` exists in the blog post's directory **and** the frontmatter does **not** already have a `feature_image:` field set (i.e., it is absent or still the placeholder `feature.png` value but the file is a real rendered image, not the placeholder).

If a real `feature.png` is present and `feature_image` is not yet committed in frontmatter:
- **Skip all interactive questions entirely**
- Use the existing `feature.png` as the feature image source for the meta render
- Jump directly to the meta render portion of Step 3 (build meta config, render `meta.png`)
- Still update frontmatter with both `feature_image: feature.png` and `meta_image: meta.png` in Step 4

If `$ARGUMENTS` fully specifies the feature template (e.g., `/blog-meta-image rocket`), skip the interactive question and go straight to Step 3's rendering. If partially specified, only ask about the unspecified parts.

## [Step 3/4] Select Feature Template & Render

Read the asset catalog reference at `.claude/commands/blog-meta-image/references/asset-catalog.md` for the full template list and logo inventory.

### Interactive Selection

Ask questions **progressively** (one at a time) using `AskUserQuestion`. Skip any question already answered via `$ARGUMENTS`.

---

### Question 1: Custom or template?

```
header: "Feature Image Source"
question: "Provide a custom feature image, or use a built-in template? (Reach out in #marketing Slack to get a custom image. If you can't get one fast enough, continue with templates.)"
options:
  - label: "I have a custom image"
    description: "Provide a path to your own feature image file"
  - label: "Use a template"
    description: "Choose from the built-in Pulumi feature image templates"
```

If **I have a custom image** is selected:
1. First, check whether `feature.png` already exists in the blog post's directory.
   - If it does, use that file as the custom image without asking — skip straight to the meta render step.
   - If it does not exist, ask the user for the file path.
2. If a path was provided (i.e., the file is not already `feature.png` in the blog directory), copy it into the blog post directory and rename it to `feature.png`:
   ```bash
   cp "<provided-path>" "<blog-dir>/feature.png"
   ```
3. Use `<blog-dir>/feature.png` as the `feature_image` in the meta config, then skip straight to the meta render step.

---

### Question 2: Feature template

```
header: "Feature Image"
question: "Choose a feature template for this blog post:"
options:
  - label: "Platform"
    description: "Default, platform engineering, DevOps, Pulumi news and events"
  - label: "Neo"
    description: "For usage on Neo specific posts only"
  - label: "Rocket"
    description: "Releases, new features, and announcements"
  - label: "Shield"
    description: "Security, secrets, compliance, and policy"
  - label: "Lightbulb"
    description: "Tutorials, how-tos, best practices, and guest posts"
  - label: "Logo variant (1-3 logos)"
    description: "Cloud provider or technology-specific content — places provider/tech logos in circular placeholders"
```

If **Logo variant** is selected, ask which logos (Question 3):

---

### Question 3: Which logos?

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

The number of selected logos (1, 2, or 3) determines which template to use (`feature-logo-1`, `feature-logo-2`, or `feature-logo-3`). If more than 3 are selected, ask the user to narrow down to 3.

---

### Question 4: Logo tint style

_Only ask if logos were selected in Question 3._

```
header: "Logo Tint Style"
question: "How should the tint color be applied to the logos?"
options:
  - label: "Overlay (default)"
    description: "Replace all logo colors with a flat tint — best for single-color cutout logos"
  - label: "Colorize"
    description: "Preserve internal contrast: bright areas stay bright, dark areas stay dark, all tinted — better for multi-color logos"
```

Set `logo_tint_mode` in the feature config to `"overlay"` or `"colorize"` accordingly. Default is `"overlay"`.

---

**Logo lookup**: Check `assets/logos/` first. If a needed logo isn't found locally:
1. Try [simple-icons](https://github.com/simple-icons/simple-icons/tree/develop/icons) first — clean vector SVGs for 3000+ brands. Download from `https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg` and add a `fill` attribute with the brand color to `<path>` elements.
2. Otherwise use `WebSearch` to find the official SVG (`"<technology> logo SVG site:github.com"`)
3. Use `WebFetch` to download the SVG content
4. Save it to `.claude/commands/blog-meta-image/assets/logos/<name>.svg`

---

### Template Resolution

| Selection | Feature Template |
|-----------|-----------------|
| Neo | `templates/feature-neo.png` |
| Platform | `templates/feature-platform.png` |
| Rocket | `templates/feature-rocket.png` |
| Shield | `templates/feature-shield.png` |
| Lightbulb | `templates/feature-lightbulb.png` |
| 1 logo | `templates/feature-logo-1.png` |
| 2 logos | `templates/feature-logo-2.png` |
| 3 logos | `templates/feature-logo-3.png` |
| Custom | _(provided path, skip feature render)_ |

### Build Composition Configs

Build **two** JSON configs: one for `feature.png` (1884×1256) and one for `meta.png` (1200×628).

**Feature config** — for mascot/static templates (no text, no logos):

```json
{
  "template": "templates/feature-neo.png",
  "logos": []
}
```

**Feature config** — for logo variants (logos composited onto circular placeholders, no text):

```json
{
  "template": "templates/feature-logo-2.png",
  "logos": [
    "logos/aws.svg",
    "logos/kubernetes.svg"
  ],
  "logo_tint_mode": "overlay"
}
```

**Meta config** — no template; starts from a `#20054E` background, composites the feature image offset to the right, applies the overlay and logo, then draws the title text:

```json
{
  "background_color": "#20054E",
  "feature_image": "<absolute-path-to-blog-dir>/feature.png",
  "overlay": "templates/meta-overlay.png",
  "logo": "templates/meta-logo.png",
  "text": {
    "content": "Blog Post Title Here",
    "font_size": 88
  }
}
```

**Font size guidelines:**
- Short titles (1-3 words): `font_size: 96`
- Medium titles (4-8 words): `font_size: 84`
- Long titles (9+ words): `font_size: 72`
- Very long titles (15+ words): `font_size: 60`

**Important**: In the feature config, all paths are relative to `--assets-dir`. In the meta config, `feature_image` must be an **absolute path** to the rendered (or custom) feature image.

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

Generate **two images** by running the composition script twice.

**Step A — Feature image (1884×1256):** Skip if the user provided a custom image.

1. Determine the blog post directory (e.g., `content/blog/my-post/`) and use its name as `<slug>`
2. Write the feature JSON config to `/tmp/feature-<slug>.json`
3. Run:
   ```bash
   uv run .claude/commands/blog-meta-image/scripts/compose_meta_image.py \
     --config /tmp/feature-<slug>.json \
     --assets-dir .claude/commands/blog-meta-image/assets \
     --output <blog-dir>/feature.png
   ```

**Step B — Meta image (1200×628):**

1. Write the meta JSON config to `/tmp/meta-<slug>.json`
   - Set `feature_image` to the **absolute path** of the feature image (either just rendered or the custom path provided by the user)
2. Run:
   ```bash
   uv run .claude/commands/blog-meta-image/scripts/compose_meta_image.py \
     --config /tmp/meta-<slug>.json \
     --assets-dir .claude/commands/blog-meta-image/assets \
     --output <blog-dir>/meta.png
   ```

## [Step 4/4] Confirm & Update Frontmatter

1. Verify both PNGs were created successfully at their expected paths
2. Update the blog post's frontmatter — add or update both image fields:
   ```yaml
   meta_image: meta.png
   feature_image: feature.png
   ```
3. Report to the user:
   - Which blog post was used
   - What feature template was selected and why
   - What logos were placed (if any)
   - Where `feature.png` and `meta.png` were saved
   - Remind them to preview both images to make sure they look good

## Error Handling

- If `compose_meta_image.py` fails, read the error output and try to fix the config (common issues: invalid SVG path, missing template file)
- If a requested logo name doesn't match anything in the catalog, suggest the closest matches and ask the user
- If the blog post has no title, ask the user for one
