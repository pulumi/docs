# Event page reference — content/events/<slug>/index.md

Contents: frontmatter fields · slug rules · sortable_date recipe · tags vocabulary · presenters · registration form IDs · multi-session events · validation fallback · update mode.

The single source of truth for the schema is `archetypes/event/index.md` (its comments are authoritative and kept current). This file adds the operational details the archetype can't carry.

## Frontmatter fields (beyond the archetype comments)

| Field | Rule |
|---|---|
| `title` | ≤ 60 characters, sentence case. Hard limit from the marketing template; trim with the user rather than truncating silently. |
| `meta_desc` | 50–160 characters, one sentence — it's the card text on /events/ and the search snippet. |
| `meta_image` / `meta_image_square` | Leave **blank** by default: the build auto-generates an on-brand card (landscape + square) from frontmatter. Set only when event-meta-image renders an enriched card into the bundle (`/events/<slug>/meta.png`, `/events/<slug>/meta-square.png`). |
| `gated` | `true` renders the registration form (needs `form.hubspot_form_id`). Pulumi-hosted workshops/webinars default gated. |
| `external` | `true` → `url_slug` becomes the external URL and `block_external_search_index: true` is required. No form. |
| `url_slug` | Must equal the bundle directory name (internal events). |
| `event_type` | `workshop` \| `webinar` \| `talk`. Also the default card overline (uppercased). |
| `sortable_date` | ISO 8601 with milliseconds and the offset valid **on that date** — see recipe. Sorts the list, dates schema.org, stamps the card. |
| `youtube_url` | Leave empty until the event has run. Setting it flips the page to the on-demand layout (no form, out of "Upcoming"). Multi-session: only after the **last** session. |
| `featured` / `unlisted` | Default `false`. |

## Slug rules

Lowercase the title; spaces → hyphens; strip everything but `[a-z0-9-]`. Keep it readable and stable — it's the URL. On collision with a *different* event, suffix with the year (`-2026`) or month. Renaming an existing event's slug changes its URL → needs an `aliases:` entry for the old path (same SEO rule as any content move).

## sortable_date recipe (DST-proof)

Never hand-write the UTC offset — PT is `-07:00` in July and `-08:00` in January. Compute it from the IANA timezone:

```bash
python3 -c "from zoneinfo import ZoneInfo; from datetime import datetime; \
print(datetime(2026, 9, 24, 11, 0, tzinfo=ZoneInfo('America/Los_Angeles')).isoformat(timespec='milliseconds'))"
# → 2026-09-24T11:00:00.000-07:00
```

Common zones: PT `America/Los_Angeles` · ET `America/New_York` · CET/CEST `Europe/Berlin` · UK `Europe/London` · IST `Asia/Kolkata`. Stdlib-only, works on macOS and Linux.

## Tags vocabulary (case-sensitive — reuse, don't mint)

Harvested from existing `content/events/*/index.md`; these drive the /events/ filters, so a near-duplicate spelling creates a broken filter bucket.

- `level` (exactly one): `Beginner` · `Intermediate` · `Advanced`
- `topics`: Kubernetes · AI · Platform Engineering · DevOps · Docker · DevSecOps · Security · Secrets Management · Pulumi ESC · Automation · Infrastructure as Code · Pulumi Features · Developer Productivity · CI/CD
- `clouds`: AWS · Azure · Google Cloud · Oracle
- `languages`: TypeScript · Python · Golang · C# · Java · YAML

Empty arrays are fine — most events set only `topics` and maybe one cloud. Before minting a new value, grep: `grep -rh "topics:" content/events/*/index.md | sort -u`.

## Presenters

```yaml
presenters:
    - name: Engin Diri
      role: Principal Solutions Architect, Pulumi
      photo: /images/team/engin-diri.jpg
```

- **Pulumi people**: id = kebab name → role from `data/team/team/<id>.toml` (`title` + ", Pulumi" — the TOML is fresher than copying an old event), photo `static/images/team/<id>.jpg` (verify the file exists; referenced as `/images/team/<id>.jpg`).
- **External people**: role = `Title, Company`. Photo via the event-meta-image resolution ladder; a sourced photo is committed to `static/images/people/<kebab-name>.jpg`. Unresolvable → `photo: ""` (the page tolerates it; the card renderer skips it with a warning).

## Registration form IDs

`form.hubspot_form_id` (UUID) and `form.salesforce_campaign_id` (`701…`, 18 chars) are **created by marketing after the tracking issue is filed** and typically arrive as a comment on that issue. Sequencing:

1. Issue filed → marketing builds the HubSpot form + SF campaign → posts IDs on the issue.
2. Until then a gated page carries empty strings with a `# TODO: wire in from pulumi/marketing#<n>` comment, and the PR body flags it.
3. When the IDs land, rerun `/create-event <issue-url>` — update mode wires them in.

Extraction regexes (scan issue comments): HubSpot `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` · Salesforce `\b701[A-Za-z0-9]{15}\b`.

## Multi-session events (`sessions:`)

One event on several dates (Americas + EMEA) is **one page** with a `sessions:` array — never two bundles. The archetype documents the shape; `make lint` (`checkEventSessions`) enforces:

1. Top-level `sortable_date` = the **earliest** session's date.
2. No top-level `form:` — each session carries its own (`hubspot_form_id` required per session when gated; don't reuse one form ID across sessions).
3. `sessions` is a non-empty array or absent entirely.

And the un-lintable rule: no `youtube_url` until every session has run.

## Validation fallback (when `make lint` can't run)

Fresh clones/worktrees may lack node deps. Best effort, in order: try `make lint`; on missing deps run this checklist manually:

1. Frontmatter parses: `python3 -c "import yaml; yaml.safe_load(open('content/events/<slug>/index.md').read().split('---')[1])"`
2. `title` ≤ 60 chars; `meta_desc` 50–160 chars.
3. `event_type` ∈ {workshop, webinar, talk}; `tags.level` ∈ {Beginner, Intermediate, Advanced}.
4. `url_slug` == directory name (or external URL + `block_external_search_index: true`).
5. `sortable_date` matches `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}[+-]\d{2}:\d{2}` and the offset came from the recipe.
6. Sessions rules above, when present.
7. No trailing whitespace; file ends with a newline.

Report which validator ran. A fallback pass is not a substitute: note that `make lint` must pass in CI.

## Update mode

When the bundle already exists: touch only what the spec explicitly provides (usually form IDs), preserve everything else, and never regress a filled field to a default. If there's no gap at all, say so and change nothing.
