---
description: Convert a Figma design into a templatized product page — maps Figma sections to Hugo template partials, exports images, and wires up frontmatter.
---

# figma-to-template-page

Convert a Figma design into a templatized Hugo product page.

**Use this when:** You have a Figma URL for a product page and a corresponding markdown file open in the editor that you want to convert to use the `product-page` layout.

---

## Usage

`/figma-to-template-page <figma-url>`

The open file in the editor is the target markdown page to convert.

---

## Before you start — collect prerequisites

**1. Figma personal access token**

You need a token with `file_content:read` scope to read metadata and export images. Ask the user upfront:

> "To read and export from Figma I need a personal access token. You can create one at **figma.com → Account → Security → Personal access tokens**. Select the `file_content:read` scope."

If no token is provided, proceed with the design context step using the Figma MCP tool, then generate gray placeholder SVGs for any images you cannot export.

**2. Reference example**

Read `content/product/infrastructure-as-code.md` and `content/product/_index.html` and their rendered partials as canonical examples of a correctly implemented product page. Use it to understand layout structure, frontmatter keys, and partial invocation patterns.

---

## Step 1 — Understand the design

Use `mcp_figma_get_design_context` with the `nodeId` and `fileKey` from the URL. If the response is too large, fall back to `mcp_figma_get_metadata` to walk the tree.

Parse the node ID carefully: Figma URLs encode it as `node-id=824-6352` but the API requires `824:6352` (replace `-` with `:`).

From the metadata, identify:
- All frames/groups whose name ends with `-image` — these are the exportable image layers
- All section names that map to template partial types

---

## Step 2 — Map sections to partials

Use **only** the partials in `layouts/partials/template-partials/` and the layout `layouts/page/product-page.html`.

The orchestrator partial is `layouts/partials/template-page-content.html`. It loops through the `sections` array and resolves each partial by converting the `type` value: underscores become hyphens, then the result is used as `template-{type}.html`. **No changes to the orchestrator are needed** when adding new section types — just create the partial and use the correct `type` name.

**Type naming convention:** the `type` value must equal the partial filename stem (without the `template-` prefix and `.html` suffix), with hyphens replaced by underscores.

**Partial selection guide:**

| Design pattern | `type:` value | Partial |
|---|---|---|
| Large hero with CTA buttons | `hero` | `template-hero` |
| Two-column: heading left, description + cards right | `feature_split` | `template-feature-split` |
| Two-column: text left, **code/language-switcher** right | `section_header_with_code` | `template-section-header-with-code` |
| Two-column: text left, **static image** right | `section_header_with_image` | `template-section-header-with-image` |
| Centered section intro (optional image below) | `section_header` | `template-section-header` |
| Three equal-width feature columns | `three_column` | `template-three-column` |
| Two side-by-side cards | `two_column` | `template-two-column` |
| Customer quote | `testimonial` | `template-testimonial` |
| Stat counters | `counter_cards` | `template-counter-cards` |

**Extension rules:**
- Extend existing partials with optional parameters rather than creating new ones.
- When adding a parameter, make it optional with a safe default so existing callers are unaffected.
- If a new partial is genuinely needed, ask the user before creating it.

---

## Step 3 — Implement the frontmatter

Rewrite the target markdown file's frontmatter to use `layout: product-page` and add a `sections:` array where each item has a `type:` field plus the fields required by that partial.

> **Required:** The frontmatter must include `type: page` or Hugo will not render the page with the product-page layout. Always include it alongside `layout: product-page`.

The `sections:` array controls render order — items appear on the page in the order they are listed.

Follow the structure in `infrastructure-as-code.md` exactly — the `sections:` array, YAML indentation (2 spaces per level, section items indented 2 from `sections:`), and field names must match what the partials expect.

---

## Step 4 — Check icons

The site uses **Font Awesome 5.8.1 Free**. For every `icon:` value in the frontmatter:

1. Verify the class has a `:before` definition in `assets/css/bundle.css`:
   ```bash
   grep "\.fa-YOUR-ICON:before" assets/css/bundle.css
   ```
2. If missing, find the nearest valid substitute. Common pitfalls:
   - `fa-shield` → use `fa-shield-alt`
   - `fa-sliders` → use `fa-sliders-h`

---

## Step 5 — Export images

### 5a. Find the video poster image (if a video embed section exists)

If the design contains a YouTube video embed section, look for a sibling frame in Figma that acts as the video poster/thumbnail — typically a dark-background card showing the video title and a "Watch Now" play button. It's name usually contains something like `-poster-image`, `video-poster`, or similar.

Export it as PNG at 2x scale and place it in the same subdirectory as the other page images. Then add `poster_image` and `poster_alt` to the `video_embed` section frontmatter:

```yaml
- type: video_embed
  youtube_id: YOUTUBE_ID
  title: Video title
  poster_image: /images/product/DIRNAME/poster.png
  poster_alt: Descriptive alt text for the poster
  anchor: demo
```

### 5b. Find exportable layers

Exportable layers are typically named with an `-image` suffix. Walk the Figma node tree to collect their IDs:

```bash
grep -o 'id="[^"]*" name="[^-"]*-image[^"]*"' <metadata-file>
```

**Important:** Node names can change between when you read the metadata and when you call the API. Always resolve node IDs fresh — do not assume a name from metadata matches the API response name.

### 5c. Read export settings

Fetch the export settings for each node via the Figma REST API before exporting. This determines format and scale:

```bash
curl -s -H "X-Figma-Token: TOKEN" \
  "https://api.figma.com/v1/files/FILE_KEY/nodes?ids=NODE_ID1,NODE_ID2" \
  > /tmp/figma_nodes.json
```

Then extract `exportSettings` from each node's document. If a node shows an unexpected name (e.g. `img` instead of `overview-esc-image`), its ID has changed — search the full page tree to find the current ID:

```bash
python3 << 'EOF'
import json
data = json.load(open('/tmp/figma_root.json'))
def find(node):
    name = node.get('name','')
    if '-image' in name.lower() or node.get('exportSettings'):
        print(node['id'], name, [e.get('format') for e in node.get('exportSettings',[])])
    for c in node.get('children',[]): find(c)
find(data['nodes']['ROOT_NODE_ID']['document'])
EOF
```

### 5d. Determine format

| Export setting | Format to request |
|---|---|
| `SVG` | `format=svg` |
| `PNG` with `value: 2.0` | `format=png&scale=2` |
| No export setting | Default to SVG for vector/diagram layers |
| `png` or `svg` in layer name | Use that as the hint |

### 5e. Download images

Request export URLs then download:

```bash
# Get URLs
curl -s -H "X-Figma-Token: TOKEN" \
  "https://api.figma.com/v1/images/FILE_KEY?ids=NODE_ID&format=svg" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['images'])"

# Download
curl -s "S3_URL" -o static/images/product/DIRNAME/FILENAME.svg
```

Place all images in a new subdirectory under `static/images/product/`.

**Reusing existing logos:** Before exporting a logo from Figma, check if it already exists under `static/logos/`. Only reuse it if the file is an SVG — PNGs will be distorted at non-native sizes. If the existing logo is a PNG, export the SVG from Figma instead.

### 5f. Fix SVG preserveAspectRatio

Figma often exports SVGs with `preserveAspectRatio="none" width="100%" height="100%"`, which causes distortion when displayed at a constrained size. After downloading any SVG, check the opening tag and replace it with the intrinsic dimensions from the `viewBox`:

```bash
head -1 static/path/to/file.svg
# If it has preserveAspectRatio="none" width="100%" height="100%"
# and viewBox="0 0 W H", replace with:
# <svg width="W" height="H" viewBox="0 0 W H" ...>
```

This is most important for logos displayed at a fixed height.

---

## Step 6 — SCSS

If a new partial is added, add its styles to `theme/src/scss/_templates.scss`. Also update the comment block at the top of `layouts/partials/template-page-content.html` to document the new `type` value and its fields.

Use neutral class names for inner elements shared across partials (e.g. `section-header-split-inner`, not `section-header-with-code-inner`) so a single SCSS block can cover multiple parent selectors:

```scss
.template-section-header-with-code,
.template-section-header-with-image {
    .section-header-split-inner { ... }
    .section-header-split-content { ... }
    .section-header-split-image { ... }
}
```

For CTA link styling, the shared selector covers all template partials:
```scss
[class*="template-"] {
    .cta { @apply text-violet-800 font-semibold font-body no-underline; }
}
```

---

## Step 7 — Verify

Run `make build` and confirm there are no Hugo errors. Check that:
- All sections render in the expected order
- Images load (check paths match `static/images/...` → `/images/...`)
- No other product pages are broken
