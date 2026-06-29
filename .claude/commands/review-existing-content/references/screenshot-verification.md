---
description: Screenshot and UI verification pass for the automated existing-content review. Compares article screenshots against curated reference images and, where accessible, product source code. Flag-only — never regenerates or deletes images.
---

# Screenshot Verification

Base image criteria (alt text, borders, format, size, brand-asset compliance) come from
`docs-review:references:image-review` — apply those first. This reference
adds the **currency** checks: is the UI an article's screenshots show still
the UI the product ships?

This pass is **flag-only**. You report stale screenshots in the PR
description's Screenshot check section; you never retake, edit, or delete an
image, and you never reword prose to match a screenshot.

## Lane 1 — reference-image comparison (always available)

Curated reference images live in `.claude/commands/_common/images/`
(shared with `/glow-up`), indexed by `manifest.yaml` there.

For each image the article references:

1. Read the article image with the Read tool. If it doesn't depict Pulumi
   product UI or branding (e.g. an architecture diagram, a terminal capture,
   a third-party console), record it as `n/a — not Pulumi UI` and move on.
2. Read the matching reference image(s) from the manifest (`area:
   console-overview` for Pulumi Cloud Console UI, `branding` for logos). For
   branding, the manifest PNG is a cached convenience; the canonical logo is
   the brand asset API (see the Branding bullet).
3. Compare deliberately, not impressionistically:
   - **Left navigation** — section names, order, presence/absence of
     products. This is the highest-signal staleness indicator.
   - **Terminology** — product names and labels visible in the UI vs. what
     the article's prose calls them.
   - **Branding** — compare any Pulumi logo against the *canonical* mark, not
     just the cached `branding` PNG (which can lag). Fetch the current logo and
     Read it:
     `curl -sL "https://brand.pulumi.com/api/logo?lockup=horizontal&background=white&format=png&width=1200" -o /tmp/pulumi-logo.png`.
     Then apply the brand-asset compliance checks from
     `docs-review:references:image-review` (logo misuse, AI-generated imagery,
     deprecated Pulumipus).
   - **Structure** — header layout, major panels.
4. Record a verdict per image: `current`, `stale` (name the specific
   differences — "left nav shows 'Pulumi Insights' where current UI has
   'Insights & Governance'"), or `unverifiable` (UI area not covered by any
   reference — say which area a new reference would need to cover).

Also check the manifest's `captured` dates: if a reference you used is older
than 180 days, add an aging note to the Screenshot check section ("reference
`pulumi-cloud-console-current.png` captured YYYY-MM-DD — refresh needed; owner:
docs-team"). Keep flagging it on every run until the reference is refreshed.

## Lane 2 — product source verification (when accessible)

Mirrors the fact-check Pass 1 lane (Pulumi-internal verification via `gh`).
Use it to verify **UI strings the prose asserts** — button labels, menu
names, setting names — against the Pulumi Cloud Console source.

1. **Feasibility gate, once per run:** `gh repo view pulumi/console`
   (the console repo may be private to the workflow token). If it fails,
   skip lane 2 for the whole run and mark prose UI claims `unverifiable —
   needs human check` instead. Never guess.
2. When accessible, search for the literal UI string:
   `gh search code --repo pulumi/console "<label>"` or
   `gh api` on likely paths. A hit verifies the label; a confident miss
   (searched variants, found the surrounding component with a different
   label) is evidence of staleness — quote what the source says instead.
3. Source-verified corrections to **prose** (a renamed button, a moved menu
   item) meet the high-confidence bar and may be applied as fixes, citing
   the console file path as the source. Screenshot pixels remain flag-only
   regardless of what lane 2 proves.

## Output

One Screenshot check entry per image (and per prose UI claim checked via
lane 2):

```
- static/images/docs/stacks-list.png — stale: left nav lacks "Insights & Governance"
  (added 2025); reference: pulumi-cloud-console-current.png (captured 2026-05-29)
- static/images/docs/arch-diagram.png — n/a, not Pulumi UI
- prose L42 "click **New Project**" — verified (console: src/routes/projects/new.tsx)
```
