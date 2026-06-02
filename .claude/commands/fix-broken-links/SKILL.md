---
name: fix-broken-links
description: Fix broken links reported by the daily link checker. Reads .broken-links.json, triages each link to a fix strategy (alias, S3 redirect, source edit, exclusion, or out-of-scope issue), and opens an auditable PR. Invoked by the check-links workflow; not user-invocable.
user-invocable: false
---

# Fix Broken Links

You are fixing the broken links found by the daily link checker (`scripts/link-checker/check-links.js`, run against `https://www.pulumi.com`). Work through every reported link, pick the right strategy for each, open one auditable PR, and file issues for anything that can't be fixed in this repo.

## Input

Read `.broken-links.json` from the repo root. Shape:

```json
{
  "generated": "2026-06-02T15:00:00.000Z",
  "internal": [{ "source": "...", "destination": "...", "reason": "HTTP_404" }],
  "external": [{ "source": "...", "destination": "...", "reason": "HTTP_404" }]
}
```

- `source` — the live page the broken link was found **on**.
- `destination` — the URL that failed.
- `reason` — BLC reason code (`HTTP_404`, `HTTP_410`, `ERRNO_ENOTFOUND`, …).
- `internal` — `destination` is on `pulumi.com`; `external` — third-party.

If both lists are empty, do nothing (the workflow won't invoke you in that case, but be defensive).

## Mapping a live URL back to its source file

`source` and `destination` are live `https://www.pulumi.com/...` URLs. To edit or redirect them you must find the file that produces them:

1. Strip the origin to get the path, e.g. `/docs/iac/concepts/stacks/`.
2. Hugo content lives under `content/`. A path like `/docs/iac/concepts/stacks/` is produced by `content/docs/iac/concepts/stacks/_index.md` or `.../stacks.md`. Use **Glob**/**Grep** under `content/` to locate it.
3. To find *which* file emits a broken **destination** link, Grep for the link text under `content/`, `data/`, `layouts/`, and `static/` — it may come from a data file, a shortcode, or a template, not prose.
4. Registry, API-docs, and other generated paths have **no** source file in this repo (see "Out of scope" below).

## Per-link triage

Apply the first row that matches.

| Situation | Strategy | Mechanism |
|---|---|---|
| Internal link points at a moved/renamed path, but the destination page still exists at a new path | **Hugo alias** | Add the old path to `aliases:` on the destination page's frontmatter |
| Internal link to a page that was deleted/restructured, or a non-Hugo path (registry, generated docs) | **S3 redirect** | Add a redirect line to the topic-appropriate file in `scripts/redirects/` |
| Broken link living in **editable** content (`content/docs`, `content/product`, `content/tutorials`) | **Edit at source** | Fix the link in place; use the full root-relative path (`/docs/...`), never `../` |
| Broken link in a **blog** post **and** an equivalent replacement exists (same content, or close enough that the post's meaning is unchanged) | **Edit at source + stamp `lastmod`** | Swap the link; add/update `lastmod:` in that post's frontmatter (leave `date:` alone) |
| Broken link in a **blog** post with **no** equivalent replacement | **Route around the prose** | Add an alias/redirect so it resolves; if it's a dead external link, add it to the exclusion list. **Do not reword blog prose** |
| Dead / transient / bot-protected **external** link | **Exclusion list** | Add the URL to `getDefaultExcludedKeywords()` in `check-links.js` with an inline `//` comment naming the reason + blog post/issue. If the page mattered, prefer swapping to a Wayback snapshot |
| Redirect **loop** or malformed alias YAML | **Repair** | Remove the stale redirect / fix the alias indentation |
| Breakage owned by **another repo** (e.g. registry `logoUrl`, generated SDK docs) or otherwise unfixable here | **Out of scope** | File a GitHub issue and document it in the PR description — do not hack around it |

### Mechanics

**Hugo alias.** Add the old path under `aliases:` in the destination page's frontmatter (root-relative, trailing slash):

```yaml
aliases:
- /docs/old/path/
```

Full mechanics and edge cases: `move-doc:references:alias-injection`.

**S3 redirect.** Append one line to the topic-appropriate file in `scripts/redirects/` (e.g. `cicd-redirects.txt`, `iac-cli-redirects.txt`, `general-broken-links-redirects.txt` when nothing more specific fits). Format is `source-path|destination-url`, one per line. The source is the path **without** a leading slash and usually ends in `/index.html`; the destination is root-relative (`/docs/.../`) or a full URL for off-site targets:

```
docs/old/path/index.html|/docs/iac/new/path/
```

**Edit at source.** Replace the broken link with the correct one. Internal docs links use the full canonical root-relative path (`/docs/iac/concepts/stacks/`); never `../`. This is the only strategy that touches prose, and for blog posts it's limited to equivalent-content link swaps.

**Blog `lastmod`.** Any blog edit must add or update `lastmod:` (ISO date, today) in that post's frontmatter so the change is reflected, while the original `date:`/publish date stays put so post ordering doesn't shift.

**Exclusion list.** Add the URL to the array returned by `getDefaultExcludedKeywords()` in `scripts/link-checker/check-links.js`, grouped with similar entries, with an inline comment naming the reason and the post/issue, matching the existing style:

```js
"https://example.com/gone",  // blog/<post>: 404, no replacement (#<issue>)
```

## Editing guardrails

- **Tutorials are editable** like docs — fix their links at the source.
- **Blog prose is editable only** to substitute a broken link for an equivalent-content replacement, and every such edit stamps `lastmod`. Blog links with no equivalent replacement are routed around with an alias/redirect/exclusion, never reworded.
- Internal links use full root-relative paths, never `../`.
- `make lint` and `make build` must both pass before you open the PR.

## Output

1. Create a branch `fix/broken-links-<date>` (date from the workflow, e.g. `fix/broken-links-2026-06-02`).
2. Make the fixes, grouping related changes into clear commits.
3. File a GitHub issue (`gh issue create`) for every out-of-scope item.
4. Run `make lint` and `make build`; fix anything they surface.
5. Open a **ready** (non-draft) PR to `master`.
6. Write the final PR URL plus a one-line summary to `.broken-links-pr.txt` for the workflow's Slack step, e.g.:
   `:link: Fixed 7 broken links — <PR URL> (2 aliases, 1 redirect, 3 source edits, 1 issue filed)`

## PR description contract (auditability)

The reviewer must be able to audit every decision without re-deriving it. Model the description on PR #19469. Include:

- **A table or list of every broken link** → the strategy applied → one line of non-obvious reasoning (why a redirect vs. an alias, why excluded, etc.).
- A **Verification** section: confirm `make lint` and `make build` passed, and note any spot-checks.
- An **Out of scope / filed issues** section linking every issue you created for breakage owned by other repos or otherwise unfixable here.