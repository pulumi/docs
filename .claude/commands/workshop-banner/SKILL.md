---
name: workshop-banner
description: "Generate a workshop/event banner image. Auto-detects the event from arguments or git status, reads frontmatter for title, event type, and presenters, then renders a 1368x768 PNG saved into the event directory with frontmatter updated. Use when the user types /workshop-banner or asks to create, generate, or regenerate a workshop banner, event banner, or social image for an event. Accepts optional arguments like an event slug, file path, or overrides."
---

# `/workshop-banner` — Generate Workshop/Event Banner

You are generating a banner image for a Pulumi workshop or event. Follow these steps precisely.

**Skill directory**: `.claude/commands/workshop-banner/` — all paths below are relative to the project root unless noted.

## [Step 1/4] Find the workshop/event

Locate the event that needs a banner:

1. If `$ARGUMENTS` contains a file path (e.g., `content/events/foo/index.md`), use that directly.
2. If `$ARGUMENTS` contains a bare slug (e.g., `designing-reusable-infrastructure-as-code`), resolve it to `content/events/<slug>/index.md`.
3. Otherwise, run `git status` and `git diff --name-only` to find modified/untracked `content/events/*/index.md` files.
4. If multiple events are found, use `AskUserQuestion` to ask which one.
5. If no event is found, ask the user to specify a path or slug.

Read the full event file (frontmatter + body).

## [Step 2/4] Parse event frontmatter & user requests

### From the event frontmatter, extract:

| Config key | Frontmatter source | Parsing notes |
|---|---|---|
| `title` | `main.title` (fall back to top-level `title`) | Use as-is |
| `event_type` | `main.event_type` | Usually `"workshop"` or `"event"` |
| `speaker_name` | `main.presenters[].name` | See presenter selection in Step 3 |
| `speaker_title` | `main.presenters[].role` — portion **before** the last comma | e.g., `"Senior Solutions Architect, Pulumi"` → `"Senior Solutions Architect"` |
| `speaker_company` | `main.presenters[].role` — portion **after** the last comma | → `"Pulumi"`. If no comma in role, treat entire string as `speaker_title`, leave `speaker_company` empty |
| `speaker_photo` | `main.presenters[].photo` | Convert site-root path to absolute filesystem path: prepend `<project_root>/static`. E.g., `/images/team/engin-diri.jpg` → `<project_root>/static/images/team/engin-diri.jpg` |

### From `$ARGUMENTS`, parse user preferences:

- **CTA text**: e.g., `"Sign Up"`, `"Join Now"`
- **Title override**: if the user explicitly provides different text in quotes, use that instead of the frontmatter title
- **Presenter name**: if a specific presenter name is mentioned, pre-select that presenter

If `$ARGUMENTS` fully specifies everything needed (event path + any overrides) and the event has exactly one presenter, skip the interactive questions and go straight to Step 3's rendering section.

## [Step 3/4] Progressive questions & render

### Interactive selection (up to 4 progressive questions)

Ask the following questions **progressively** (one at a time) using `AskUserQuestion`. Skip any question that was already answered via `$ARGUMENTS` or is not applicable.

---

### Question 1: Featured speaker (only if multiple presenters)

If `main.presenters` contains more than one presenter, ask which one to feature. If there is exactly one presenter (or zero), skip this question and use that presenter automatically.

```
header: "Featured Speaker"
question: "Which presenter should be featured on the banner?"
options:
  - label: "<presenter1.name>"
    description: "<presenter1.role>"
  - label: "<presenter2.name>"
    description: "<presenter2.role>"
  ...
```

Build options dynamically from `main.presenters[]`.

---

### Question 2: CTA button text

Skip if already provided via `$ARGUMENTS`.

```
header: "CTA Button"
question: "What text for the call-to-action button?"
options:
  - label: "Register"
    description: "Default CTA for workshops"
  - label: "Sign Up"
    description: "Alternative registration CTA"
  - label: "Join Now"
    description: "For live events"
  - label: "Watch Now"
    description: "For replays (event has a youtube_url)"
  - label: "Custom"
    description: "Enter your own CTA text"
```

If the event has a `youtube_url` set, suggest "Watch Now" as the default. Otherwise default is "Register". If the user selects "Custom", follow up by asking for their text.

---

### Company logo (hard-coded)

Always use the Pulumi logo at `static/logos/brand/logo-on-black.png`. Convert to absolute path for the config: `<project_root>/static/logos/brand/logo-on-black.png`. Do **not** ask the user about this — it is always included.

---

### Question 4: Partner logos (optional)

Only ask this if `main.tags.clouds` or `main.tags.topics` suggest a partner context (e.g., clouds contains `"AWS"`, `"Azure"`, `"Google Cloud"`).

```
header: "Partner Logos"
question: "Add partner/technology logos to the bottom-right?"
options:
  - label: "Skip"
    description: "No partner logos"
  - label: "Add logos"
    description: "Provide paths to partner logo files"
```

If the user selects "Add logos", ask for:
1. Paths to logo files (absolute paths)
2. Optional `partner_text` (e.g., `"powered by"`)
3. Whether logos go before or after the text

Suggest relevant logos based on tags — e.g., if `clouds: ["AWS"]`, mention the user could provide an AWS logo.

---

### Build config and render

**Build the JSON config** with all collected values:

```json
{
  "event_type": "<from main.event_type>",
  "title": "<from main.title or override>",
  "cta_text": "<from question or default 'Register'>",
  "speaker_photo": "<absolute path: project_root/static + frontmatter photo>",
  "speaker_name": "<from selected presenter>",
  "speaker_title": "<parsed from role, before last comma>",
  "speaker_company": "<parsed from role, after last comma>",
  "company_logo": "<absolute path or empty>",
  "partner_logos": ["<absolute paths>"],
  "partner_text": "<if provided>",
  "partner_logos_after_text": ["<absolute paths>"]
}
```

Write the config to `/tmp/banner_config_<event-slug>.json`.

**Determine output path**: `content/events/<event-slug>/meta.png` — saves the banner alongside the event's `index.md`.

**Render** using the HTML renderer (requires Playwright):

```bash
python3 <skill_dir>/scripts/render_banner_html.py \
  --config /tmp/banner_config_<event-slug>.json \
  --output content/events/<event-slug>/meta.png
```

Read the output PNG to show the result to the user.

## [Step 4/4] Confirm & update frontmatter

1. Verify the PNG was created successfully at the expected path.
2. Check the event's frontmatter for `meta_image:` — if missing or set to something else, update it:
   ```yaml
   meta_image: /events/<event-slug>/meta.png
   ```
   This is the Hugo site-root-relative path (no `content/` prefix).
3. Report to the user:
   - Which event was used (path and title)
   - Which presenter was featured
   - What config was applied (event type, CTA, logos)
   - Where `meta.png` was saved
   - That `meta_image` was updated in frontmatter
   - Remind them to preview the image to make sure it looks good
4. Ask if any adjustments are needed (text, layout, speaker choice, etc.).

## Layout reference

- **Left white card** (~52% width): badge (top-left), title (vertically centered), CTA button (bottom-left)
- **Right purple panel** (~48% width): company logo (top-right), circular speaker photo with glow ring (center), speaker name/title (below photo), partner logos (bottom-right)
- **Accent shapes**: coral/pink diagonal stripes at top-left and bottom corners

## Notes

- The HTML renderer uses Google Fonts (Outfit, DM Sans) and CSS gradients/shadows for a polished look.
- Title auto-sizes based on text length.
- Speaker photo is displayed in a circle with a glowing ring effect; a placeholder icon shows when no photo is provided.
- Images are embedded as base64 data URIs — all paths must be absolute filesystem paths.
- Requires `playwright` Python package (`pip install playwright && playwright install chromium`).

## Error handling

- If `render_banner_html.py` fails, read the error output and try to fix the config (common issues: invalid photo path, missing file).
- If a presenter has no `photo` field, the renderer will show a placeholder silhouette — this is fine.
- If the event has no presenters at all, skip the speaker fields entirely (the banner will show a placeholder).
- If the frontmatter title is very long (>80 characters), mention to the user that they can provide a shorter override for better visual results.
