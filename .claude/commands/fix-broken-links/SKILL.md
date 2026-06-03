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

## Verify each link before fixing it

**The checker produces false positives — never fix a link without confirming it's actually broken.** The crawler hits live URLs with a bot user agent, so it routinely mis-flags links that are fine in a browser: bot-protected sites, transient `5xx`/timeouts, rate-limiting, auth walls, and pages that block automated clients. `excludeAcceptable()` already filters the common transient reasons, but plenty slip through — especially in the `external` list.

For **every** reported link, confirm it's genuinely broken before touching anything:

1. **Re-check the destination** — `WebFetch` (or `curl -sIL`) the URL. If it resolves, it's a false positive.
2. **Weigh the reason code.** Internal `HTTP_404`/`HTTP_410` on a `pulumi.com` path is almost always real. External failures, and codes like `HTTP_403`, `HTTP_401`, `HTTP_429`, `HTTP_503`, or connection/timeout errors, are frequently bot protection or transient — treat as suspect until confirmed.
3. **If it's a false positive, do not edit, redirect, or exclude it.** Leave the link as-is and record it in the PR audit trail under a **False positives / not actioned** section, with the URL, the reason code, and one line on why it's fine (e.g. "resolves in browser; 403 is Cloudflare bot protection"). Optionally suggest it as a future exclusion-list candidate, but don't add it unless it's a recurring offender.

Only links you've confirmed broken proceed to triage below.

## Skip links already being handled (deduplication)

Broken links persist for days, so the same ones surface in consecutive runs while
a fix is already in flight. **Before actioning a confirmed-broken link, check
whether it's already covered** — never open a second PR for a fix that's pending,
or file a duplicate issue.

For each confirmed-broken link, search for prior work:

1. **Open PRs in `pulumi/docs`.** List candidates with
   `gh pr list --state open --search "broken link" --json number,title,url,headRefName`
   (prior runs use the `fix/broken-links-*` branch pattern). For a likely match,
   confirm with `gh pr view <n>` / `gh pr diff <n>` that it actually covers this
   link (same destination URL, source file, redirect, or exclusion entry).
2. **Existing issues, before filing a new one.** For an out-of-scope item that
   would become an issue in another repo, search that repo first —
   `gh issue list --repo pulumi/<repo> --state open --search "<url-or-path>"`
   (or `gh search issues`). If an open issue already tracks it, treat it as a
   duplicate and reuse that issue's link; do **not** file another.

Classify each confirmed-broken link as **actionable** (no existing PR/issue
covers it) or **duplicate** (one does — capture the PR/issue URL). Then:

- **All duplicates** (every confirmed-broken link is already covered): do **not**
  create a branch, PR, or any issue. Write a Slack summary to
  `.broken-links-pr.txt` saying so and listing each link with its existing
  PR/issue link, e.g. `:link: 5 broken links — all already tracked (no new PR): <url> → #19470, …`. Stop here.
- **Some actionable, some duplicates:** action only the non-duplicates (open the
  PR, file new issues). **Omit duplicates from the fixes**, but list them in a
  short **Already tracked** section in the PR description (one line each, linking
  the existing PR/issue). Don't re-file or re-fix them.

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

If **every** confirmed-broken link is a duplicate (see deduplication above), skip
all of the below: open no branch, PR, or issue, write the "all already tracked"
Slack summary to `.broken-links-pr.txt`, and stop. Otherwise, for the actionable
(non-duplicate) links:

1. Create a branch `fix/broken-links-<date>` (date from the workflow, e.g. `fix/broken-links-2026-06-02`).
2. Make the fixes, grouping related changes into clear commits.
3. File a GitHub issue (`gh issue create`) for every **new** out-of-scope item (reuse the existing issue for duplicates).
4. Run `make lint` and `make build`; fix anything they surface.
5. Open a **ready** (non-draft) PR to `master`.
6. Write the final PR URL plus a one-line summary to `.broken-links-pr.txt` for the workflow's Slack step, e.g.:
   `:link: Fixed 7 broken links — <PR URL> (2 aliases, 1 redirect, 3 source edits, 1 issue filed)`

## PR description contract (auditability)

The reviewer must be able to audit every decision without re-deriving it. Model the description on PR #19469. Include:

- **A table or list of every broken link** → the strategy applied → one line of non-obvious reasoning (why a redirect vs. an alias, why excluded, etc.).
- A **Verification** section: confirm `make lint` and `make build` passed, and note that each link was re-checked before fixing.
- A **False positives / not actioned** section listing every reported link you confirmed was actually fine, with its reason code and why (so the reviewer knows it was checked, not missed).
- An **Already tracked** section, when any link was skipped as a duplicate: one succinct line per link linking the existing PR or issue that covers it.
- An **Out of scope / filed issues** section linking every issue you created for breakage owned by other repos or otherwise unfixable here.
