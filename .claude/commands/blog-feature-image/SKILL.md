---
name: blog-feature-image
description: "Render the feature image (1884x1256) for a blog post — the in-body hero art. Reads the blog post, selects a feature template (neo, platform, rocket, shield, lightbulb, a 1-3 logo variant, or a shape template — circle, square, diamond, hexagon, lock, shield, speech-bubble, sync-diamond — with a centered solid phosphor icon or single small logo), renders feature.png, and sets feature_image in frontmatter. The OpenGraph/social meta image is no longer produced here — it is generated on-brand at build time from the title + feature image (scripts/meta-images/blog.mjs). Use when the user types /blog-feature-image (formerly /blog-meta-image) or asks to create, generate, or regenerate a blog post's feature image, hero image, or social card. Accepts optional arguments like a feature template name, logo names, or a phosphor icon name."
---

# `/blog-feature-image` — Render a Blog Feature Image

> Formerly `/blog-meta-image`. This skill now produces **only** the feature image. The 1200×628 OpenGraph/social card is generated at build time by `scripts/meta-images/blog.mjs` (via `scripts/generate-meta-images.mjs`) from the post title and this feature image — do not composite or commit a `meta.png`.

You are rendering the **feature image** (1884×1256) for a Pulumi blog post — the hero art shown at the top of the post and in the blog listing. Follow these steps precisely.

> ## ⛔ Hard rule: never create the image yourself
>
> There are exactly **two** valid ways `feature.png` may be produced, and no others:
>
> 1. **`compose_meta_image.py` renders one of the built-in templates** in `assets/templates/` (the normal path — Steps 2–3).
> 2. **You copy a file the user explicitly gave you a path to**, and that file is a **human/designer-supplied image** (e.g. from the design team, `needs-design`).
>
> You must **NEVER** create, draw, paint, illustrate, synthesize, or otherwise author original image content for `feature.png`, and you must **NEVER** use any image-generation tool/model (or ask another agent to) to produce it. An **AI-generated image is never an acceptable feature image** — no matter how well it fits the post, how much better it might look, or how the "custom image" option is phrased below. If no template fits and no designer-supplied file exists, pick the closest template or stop and ask the user — do **not** invent one.

**Skill directory**: `.claude/commands/blog-feature-image/` — all paths below are relative to the project root unless noted.

## [Step 1/4] Find the Blog Post

Locate the blog post that needs a feature image:

1. If `$ARGUMENTS` contains a file path, use that directly.
2. Otherwise, run `git status` and `git diff --name-only` to find modified/untracked `content/blog/*/index.md` files.
3. If multiple blog posts are found, use `AskUserQuestion` to ask which one.
4. If no blog post is found, ask the user to specify a path.

Read the full blog post file (frontmatter + body).

## [Step 2/4] Parse Blog Content & User Requests

### From the blog post, extract:
- **Title**: the `title:` field from YAML frontmatter (used to choose an on-theme template)
- **Tags**: the `tags:` array from frontmatter
- **Topics**: scan the body for key signals — cloud providers (AWS, Azure, GCP), languages (Go, Python, TypeScript), technologies (Kubernetes, Terraform, Docker), features (ESC, secrets, OIDC, policy), concepts (AI, ML, platform engineering, IDP)

### From `$ARGUMENTS`, parse user preferences:
- **Feature template**: name of a feature template (e.g., "neo", "platform", "rocket", "shield", "lightbulb"), a shape template (e.g., "shape-lock", "shape-circle"), or logo names like "aws kubernetes"
- **Phosphor icon**: an icon name for a shape template's centerpiece (e.g., "shape-sync-diamond git-branch")

### Fast-path: existing feature image

If a `feature.png` already exists in the blog post's directory, skip all interactive questions — just make sure `feature_image: feature.png` is set in frontmatter (Step 4) and report. (New posts scaffold with a blank `feature_image` and no image file, so any `feature.png` present is a real one.)

If `$ARGUMENTS` fully specifies the feature template (e.g., `/blog-feature-image rocket`), skip the interactive question and go straight to Step 3's rendering. If partially specified, only ask about the unspecified parts.

## [Step 3/4] Select Feature Template & Render

Read the asset catalog reference at `.claude/commands/blog-feature-image/references/asset-catalog.md` for the full template list and logo inventory.

### Interactive Selection

Ask questions **progressively** (one at a time) using `AskUserQuestion`. Skip any question already answered via `$ARGUMENTS`.

---

### Question 1: Custom or template?

```
header: "Feature Image Source"
question: "Use a designer-supplied custom image, or a built-in template? (To request a custom image from the design team, label your PR with `needs-design`. If you can't get one fast enough, continue with templates.)"
options:
  - label: "I have a designer-supplied image"
    description: "Provide a path to a human/designer-made feature image file (never an AI-generated one)"
  - label: "Use a template"
    description: "Choose from the built-in Pulumi feature image templates"
```

The "custom image" option is only for a **designer-supplied file** (a designer, the `needs-design` team, or the author) — never an AI-generated stand-in. If the user doesn't already have one, use a template instead.

If **I have a designer-supplied image** is selected:
1. First, check whether `feature.png` already exists in the blog post's directory.
   - If it does, use that file without asking — skip straight to Step 4.
   - If it does not exist, ask the user for the file path to their designer-supplied image.
2. If a path was provided, copy it into the blog post directory and rename it to `feature.png`:
   ```bash
   cp "<provided-path>" "<blog-dir>/feature.png"
   ```
3. Skip straight to Step 4.

> **`make lint` only accepts two PNG `Software` tags**: `Figma` (a designer's Figma export) and `pulumi-blog-feature-image` (this skill's renderer). An **untagged** PNG now fails, because that's what every ad-hoc image writer produces by default. So a designer-supplied file that isn't a straight Figma export — re-saved from another tool, or run through an optimizer that strips metadata — will fail lint even though it's legitimate. **Do not "fix" that by writing a tag onto the file.** Report the failure to the user and ask them for the original Figma export.

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
  - label: "Shape + icon or single logo"
    description: "Outline shape (circle, square, diamond, hexagon, lock, shield, speech bubble, sync diamond) with a centered solid phosphor icon or a single small logo"
```

If **Shape + icon or single logo** is selected, go to Question 2a. If **Logo variant** is selected, ask which logos (Question 3):

---

### Question 2a: Which shape?

_Only ask if the shape family was chosen. Recommend a shape based on the post's topic._

```
header: "Shape Template"
question: "Which shape template?"
options:
  - label: "Lock"
    description: "Security, secrets, encryption, access control"
  - label: "Shield"
    description: "Security posture, compliance, policy, protection"
  - label: "Speech bubble"
    description: "Community, Q&A, announcements, AI chat and agents"
  - label: "Sync diamond"
    description: "CI/CD, automation, deployments, drift detection"
  - label: "Hexagon"
    description: "Kubernetes-adjacent, modules, packages, components"
  - label: "Circle / Square / Diamond"
    description: "General-purpose abstract — pick by icon silhouette fit"
```

(Present at most 4 options per `AskUserQuestion` call — lead with the topical best fits for this post; the free-form "Other" covers the rest.)

### Question 2b: Icon or logo in the center?

```
header: "Shape Centerpiece"
question: "What goes in the center of the shape?"
options:
  - label: "Phosphor icon (recommended)"
    description: "A solid (fill-weight) Phosphor icon, tinted violet (#C3BDFF)"
  - label: "Single logo"
    description: "One product/technology logo, rendered small"
```

If **Phosphor icon**: suggest 3–4 topical icon names from [Phosphor Icons](https://phosphoricons.com) based on the post content (e.g. `rocket-launch`, `shield-check`, `database`, `git-branch`, `robot`, `stack`), then fetch per the icon-lookup rule below. Pick an icon whose silhouette complements the shape (e.g. a wide icon fights the tall lock).

If **Single logo**: continue with Question 3 (exactly 1 logo) and Question 4 as usual — the monochrome-preferred overlay rule applies unchanged.

---

**Icon lookup (phosphor)**: Check `assets/icons/<name>-fill.svg` first. If missing, download the **fill** weight from phosphor-icons/core and cache it in the skill assets (commit it — the cache grows like the logo library):

```bash
curl -fsSL "https://raw.githubusercontent.com/phosphor-icons/core/main/assets/fill/<name>-fill.svg" \
  -o .claude/commands/blog-feature-image/assets/icons/<name>-fill.svg
```

On a 404, the slug is wrong — search phosphoricons.com for the correct kebab-case name and retry. Always use the fill weight (solid), never regular/bold/duotone.

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

**Recommend `Overlay` almost every time.** It's the default and the right choice for the vast majority of posts — it keeps the logos on-brand in Pulumi's lavender and reads cleanest against the template background. This is *especially* true when a monochrome variant of the logo is available (see the mandatory-monochrome rule below), since a clean single-color cutout tints perfectly.

`Color` is a **backup for when overlay doesn't work** — not a stylistic preference. Reach for it only when a flat lavender tint destroys the logo's legibility: specifically when the logo is a **solid filled shape with no internal cutouts**, so overlay collapses it into a featureless lavender blob and the recognizable shape is lost. In that case `Color` preserves the internal brightness contrast that keeps the mark readable. When the logo has cutouts/negative space that survive a flat tint (most icons and monochrome variants do), stay on `Overlay`. When in doubt, render `Overlay` first and only switch to `Color` if the shape is genuinely unreadable.

```
header: "Logo Tint Style"
question: "How should the tint color be applied to the logos?"
options:
  - label: "Overlay (default)"
    description: "Replace all logo colors with a flat tint — best for single-color cutout logos."
  - label: "Color"
    description: "Backup for when overlay flattens a solid, cutout-less logo into an unreadable blob — recolors in light-purple while preserving internal brightness contrast to keep the shape legible."
```

Set `logo_tint_mode` in the feature config to `"overlay"` or `"color"` accordingly. Default is `"overlay"`.

**⚠️ Overlay tint MUST use the monochrome variant when one exists.** For `overlay` mode, always prefer a `<name>-monochrome.svg` over the plain `<name>.svg` — check `assets/logos/` for a monochrome-suffixed version of each selected logo and use it if present (e.g. `kubernetes-monochrome.svg`, not `kubernetes.svg`). The flat tint reads cleanest off a clean single-color cutout; multicolor source SVGs can produce muddy or uneven fills. Only fall back to the plain SVG when no monochrome variant exists. (For `color` mode, use the plain full-color SVG.)

---

**Logo lookup**: Check `assets/logos/` first. If tint style is `Overlay` and there is a version of the logo suffixed with `monochrome`, use that (see the overlay rule above — monochrome is mandatory when available). If a needed logo isn't found locally:
1. Try [simple-icons](https://github.com/simple-icons/simple-icons/tree/develop/icons) first — clean vector SVGs for 3000+ brands. Download from `https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg` and add a `fill` attribute with the brand color to `<path>` elements.
2. Otherwise use `WebSearch` to find the official SVG (`"<technology> logo SVG site:github.com"`)
3. Use `WebFetch` to download the SVG content
4. Save it to `.claude/commands/blog-feature-image/assets/logos/<name>.svg`

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
| Shape: circle | `templates/feature-shape-circle.png` |
| Shape: square | `templates/feature-shape-square.png` |
| Shape: diamond | `templates/feature-shape-diamond.png` |
| Shape: hexagon | `templates/feature-shape-hexagon.png` |
| Shape: lock | `templates/feature-shape-lock.png` |
| Shape: shield | `templates/feature-shape-shield.png` |
| Shape: speech bubble | `templates/feature-shape-speech-bubble.png` |
| Shape: sync diamond | `templates/feature-shape-sync-diamond.png` |
| Custom | _(provided path, skip feature render)_ |

### Build Composition Config

Build **one** JSON config for `feature.png` (1884×1256).

**Feature config** — for static templates (no logos):

```json
{
  "template": "templates/feature-neo.png",
  "logos": []
}
```

**Feature config** — for logo variants (logos composited onto circular placeholders):

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

**Feature config** — for a shape template with a phosphor icon centerpiece (icon is always flat-tinted `#C3BDFF`, rendered at ~85% of the clear space):

```json
{
  "template": "templates/feature-shape-lock.png",
  "icon": "icons/shield-check-fill.svg"
}
```

**Feature config** — for a shape template with a single small logo (same logo rules as the logo variants, including the monochrome-preferred overlay rule):

```json
{
  "template": "templates/feature-shape-circle.png",
  "logos": ["logos/aws.svg"],
  "logo_tint_mode": "overlay"
}
```

`icon` and `logos` are mutually exclusive — set one or the other.

**Important**: All paths in the config are relative to `--assets-dir`.

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

`cairosvg` rasterizes the logo SVGs and needs the **native `libcairo`** library (a system package, not a pip dep). The script auto-locates Homebrew's copy on macOS, so a plain `uv run` normally just works. If you still see `no library called "cairo" was found`, install it:

```bash
brew install cairo        # macOS
# apt-get install libcairo2 # Debian/Ubuntu
```

### Rendering

Render the feature image. Skip if the user provided a custom image.

1. Determine the blog post directory (e.g., `content/blog/my-post/`) and use its name as `<slug>`
2. Write the feature JSON config to `/tmp/feature-<slug>.json`
3. Run:
   ```bash
   uv run .claude/commands/blog-feature-image/scripts/compose_meta_image.py \
     --config /tmp/feature-<slug>.json \
     --assets-dir .claude/commands/blog-feature-image/assets \
     --output <blog-dir>/feature.png
   ```

## [Step 4/4] Confirm & Update Frontmatter

1. Verify `feature.png` was created at its expected path (a template render, or the designer-supplied file the user handed you — never an AI-generated image)
2. Update the blog post's frontmatter — add or update the feature image field only:
   ```yaml
   feature_image: feature.png
   ```
   Do **not** add a `meta_image` field — the social/OpenGraph card is generated at build time from the title + this feature image.
3. Report to the user:
   - Which blog post was used
   - What feature template was selected and why
   - What logos were placed (if any)
   - Where `feature.png` was saved
   - That the OpenGraph social card is generated at build time (preview it with `make meta-images` then check `assets/images/generated/blog/<slug>/index.png`)
   - Remind them to preview `feature.png` to make sure it looks good

## Error Handling

- If `compose_meta_image.py` fails, read the error output and try to fix the config (common issues: invalid SVG path, missing template file)
- If a requested logo name doesn't match anything in the catalog, suggest the closest matches and ask the user
- If the blog post has no title, ask the user for one
