---
description: Create a new changelog entry for the Pulumi releases log, with the correct date-prefixed filename and frontmatter.
---

# /new-changelog Command

**Use this when:** You're adding an entry to the Pulumi releases changelog — the individual, dated items that appear (grouped by month) on `/releases/` and render at `/releases/changelog/<slug>/`.

Creates a new changelog entry under `content/releases/changelog/` with the required date-prefixed filename (`YYYY-MM-DD-slug.md`), valid frontmatter, and a starter body. Uses the Hugo `changelog` archetype so the title and date stay derived from the filename.

## Background

- Each entry is a single markdown file in `content/releases/changelog/` (not a leaf bundle). Shared images and videos live in the `images/` and `videos/` subfolders and are referenced by absolute path (e.g. `/releases/changelog/images/foo.png`).
- **Filenames must be `YYYY-MM-DD-slug.md`**, and the date prefix must match the frontmatter `date:`. `make lint` enforces both (see `scripts/lint/lint-markdown.js`, `checkChangelogFilename`).
- The section `_index.md` sets `cascade.type: changelog` (routes entries to `layouts/changelog/single.html`) and `build.render: never` (no list page for the folder itself). Don't touch it when adding an entry.
- These are short announcements — a paragraph or two that lead with what the reader can now do, then link to the announcement blog post and/or docs. There are no authors, tags, categories, feature images, or social copy (unlike blog posts).

## Instructions for Claude

**CRITICAL**: Complete all 5 steps in sequence. Display progress as **[Step X/5]** before each step. Even when skipping a step, display it with a one-line explanation.

**Minimize open-ended questions**: use AskUserQuestion with prepopulated, context-derived suggestions wherever possible.

### 1. Gather information

Ask the user for the following using AskUserQuestion, seeding smart defaults:

- **Title**: The entry headline (Sentence case). If they only have a topic, suggest a headline and let them refine it.
- **Date**: The publish/announcement date, used for display and month grouping. Options:
  1. label: "Today ({current-date}) (Recommended)" / description: "Use today's date"
  2. label: "Enter a specific date" / description: "You'll provide YYYY-MM-DD"
  - Replace `{current-date}` with the actual current date in `YYYY-MM-DD`. Validate any custom date matches `YYYY-MM-DD`.
- **Summary (`meta_desc`)**: Suggest a concise one- or two-sentence summary (max 160 characters) based on the title. Required — the linter fails without it.
- **Tier badge (optional)**: Ask whether the release applies only to a particular Pulumi product tier. Options are Team, Enterprise, and Business Critical. Default is none. Only add the `tier:` field if the user specifies one.

If the user already provided the announcement details or a link to a blog post, use them to draft the body in Step 4 instead of asking again.

### 2. Generate the filename

1. **Slug**: lowercase the title, replace spaces with hyphens, strip everything except `[a-z0-9-]`, and collapse repeated hyphens.
2. **Filename**: prefix with the date: `content/releases/changelog/{YYYY-MM-DD}-{slug}.md`.
3. If a file with that name already exists, tell the user and suggest an alternative slug.

### 3. Create the file from the archetype

Prefer the Hugo archetype so title/date derive from the filename:

```bash
hugo new --kind changelog content/releases/changelog/{YYYY-MM-DD}-{slug}.md
```

If Hugo isn't available or errors, write the file directly with this frontmatter instead:

```markdown
---
title: "Title in Title Case"
date: YYYY-MM-DD
meta_desc: "One- or two-sentence summary (<= 160 chars)"
# tier: public preview   # optional — remove if no badge
---
```

### 4. Fill in the entry

1. Remove the archetype's instructional comments from the frontmatter.
2. Set `title`, `date`, and `meta_desc` to the gathered values (the archetype pre-fills `title`/`date` from the filename — verify and tidy the title).
3. Add the `tier:` field only if the user specified one; otherwise omit it.
4. Replace the placeholder body with the announcement: a short paragraph or two that lead with the reader benefit, then link out to the blog post (`/blog/...`) and/or docs (`/docs/...`). Follow `STYLE-GUIDE.md` (H1 = Title Case, H2+ = Sentence case; sentence-case running prose; lowercase common nouns like "stack").
5. If the entry needs an image or video, place it in `content/releases/changelog/images/` or `.../videos/` **with a date-prefixed, lowercase-hyphenated filename** (`YYYY-MM-DD-slug.ext`, using this entry's date — e.g. `2026-07-11-command-palette.mp4`), and reference it by absolute path (e.g. `/releases/changelog/images/2026-07-11-foo.png`). `make lint` enforces the asset naming too. Markdown must end with a trailing newline.

### 5. Validate and provide next steps

Validate:

- Filename is `YYYY-MM-DD-slug.md` and the date prefix matches frontmatter `date:`.
- Any images/videos added under `images/`/`videos/` are date-prefixed (`YYYY-MM-DD-slug.ext`) and their references updated to match.
- `title` and `meta_desc` are present; `meta_desc` is <= 160 characters.
- The file ends with a newline.
- The user is not committing directly to `master` (warn if so).

Run the linter on the new file to confirm:

```bash
node scripts/lint/lint-markdown.js content/releases/changelog/{YYYY-MM-DD}-{slug}.md
```

Then tell the user:

1. **Location** of the new entry.
2. **Preview locally**: `make serve`, then visit `/releases/` (the entry appears in its month group and opens in a modal) and `/releases/changelog/{YYYY-MM-DD}-{slug}/` for the standalone page.
3. **Recommended**: run `/docs-review` on the entry before committing, and `make lint` to confirm.

## Notes

- Follow the writing style (tone, voice, pespective) and CTA conventions of existing changelog posts.  
- Keep entries short and link-forward; the full story belongs in the linked blog post or docs.
