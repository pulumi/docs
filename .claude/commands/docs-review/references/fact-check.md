---
user-invocable: false
description: Factual claim verification — extract claims from changed content, verify in parallel against ground truth, and produce a tiered triage report
---

# Factual Claim Verification

This procedure catches *wrong information* in documentation: incorrect command output, hallucinated CLI flags, features described as existing when they don't, version claims, miscited APIs.

---

## Invocation contract

### Inputs

The caller must provide:

- **`files`** -- list of changed content file paths (typically `.md` files under `content/`)
- **`scrutiny`** -- `standard` or `heightened` (see domain files for per-domain defaults)
- **`target_output`** -- where the tiered triage object will be rendered (a variable, a file path, or "the caller's composed review")
- **(optional) `previous_results`** -- on re-entrant runs, the previous triage object so the verifier can reuse already-verified claims

### Outputs

- **Tiered triage object** with four buckets:
  - 🚨 Needs your eyes (contradicted + unverifiable)
  - ⚠️ Low-confidence (verified with low confidence, or medium when `scrutiny=heightened`)
  - 🤔 Intuition-check (claim *shape* is suspect even when evidence is absent -- see Intuition-check axis below)
  - ✅ Verified (collapsed under `<details>`)
- **Author-question buffer** -- one line per unverifiable claim, file:line-anchored
- **Per-claim evidence trail** -- the raw `{status, confidence, evidence, source, suggested_fix}` tuples, retained for re-entrant re-verification *and* rendered verbatim into the 🔍 Verification trail section per `docs-review:references:output-format`. Includes cross-sibling-consistency records (see §Cross-sibling consistency).

The skill is callable as a pure function of `(files, scrutiny)` → `(triage_object, author_questions, evidence_trail)`. Do not render the output directly into a comment.

Every claim record must appear in `evidence_trail`, even when the claim also surfaces in a bucket via the always-🚨 carve-outs. The trail is the evidence behind those bucket entries, not a deduplicated summary.

---

## Claim extraction

For every changed content file, produce a structured claim list. A "claim" is any assertion that could be wrong:

| Claim type | Example |
|---|---|
| Command behavior | "`pulumi logout` removes credentials for the current backend" |
| Flag/option existence | "`--cwd` accepts a path" |
| Output format | "the command prints `Logged out`" |
| Version/availability | "available in v3.230+", "supported on Windows" |
| Feature existence | "ESC supports rotation for AWS" |
| Resource API surface | "the `aws.s3.Bucket` constructor takes a `versioning` argument" |
| Cross-reference | "see the X guide" -- the guide must exist; also sibling-consistency claims (nav steps, headings, conventions) checked against parallel pages — see §Cross-sibling consistency |
| Numerical | pricing, limits, sizes |
| Quote/attribution | direct quotes, named sources |

**Skip** prose that is:

- Stylistic or opinion ("this approach is cleaner")
- Self-evidently context-only ("In this guide, we'll walk through...")
- Stylistic, opinion, or rhetorical phrasing that is also already cited and linked

A specific factual claim — percentage, count, time-bounded statement, framing claim like "in production" vs "in use" — must still extract and verify even when cited. The citation makes verification cheap, not absent. See §Cited-claim spot-check.

### Scope

- Default (`scrutiny=standard`): extract claims from the diff only -- lines added or modified
- `scrutiny=heightened`: extract claims from the **full file**, not just the diff. AI hallucinates surrounding prose, not just changed lines.

### Frontmatter sweep

Hugo posts duplicate the same load-bearing phrasing across body, `meta_desc`, and `social:` sub-keys (`twitter`, `linkedin`, `bluesky`). When extracting a claim from any of these locations, scan the rest of the file -- body, `meta_desc`, and every `social:` sub-key -- for the same factual phrasing or a near-paraphrase, and treat all occurrences as one claim with multiple cited locations. A single finding then renders one suggestion-block per location, so a verified-false claim is fixed everywhere in one pass.

Example: a blog post says "96% of enterprises run AI agents in production today" in the body, and the same phrase (or a paraphrase: "96% of enterprises run agents in production") appears in `social.linkedin` and `social.bluesky`. Extract one claim, verify once, render the finding with three cited locations. Don't enumerate per-occurrence claims -- that triples verification work and risks the buckets disagreeing on confidence.

This rule also applies when the body is unchanged but a frontmatter sub-key was edited; the body's pre-existing phrasing still surfaces in the same finding if the frontmatter edit triggered a contradicted verdict.

### Cross-sibling consistency

When a new or changed file lives in a structurally-templated directory (≥3 parallel pages on the same subject), every nav step, heading, required-field name, and placeholder is a *sibling-consistency* claim. Extract each as a `claim_type: cross-reference` record and verify by reading the siblings.

**Pre-step artifact `.cross-sibling-discovery.json`** (workflow pre-step `cross-sibling-discover.py`). For each PR-changed `*.md` under `content/docs/`, the pre-step lists `directory_peers` (in-dir `*.md` files excluding `_index.md`) and sets `in_templated_section: true` when ≥3 peers exist (the threshold mirrors the templated-section criterion below). Per file, the artifact carries `in_templated_section`, `directory_peers`, and `siblings_for_dispatch` (the dispatch base when templated). **Read this artifact first.** Do *not* recompute the templated-section decision inline. The model still applies sibling-set filtering judgment (e.g., distinguish vendor pages from admin/troubleshooting peers in the same directory) before fan-out, but the classification itself is deterministic.

**Pre-step artifact `.frontmatter-validation.json`** (workflow pre-step `frontmatter-validate.py`). Three checks bundled in one content-tree walk + redirect-table scan:

- `menu_parents` — for each `menu.<name>.parent` declared in the file, did the parent identifier resolve in the same named menu? Carries `parent_exists_in_menu` (boolean) and `found_in_other_menus` (list — when the identifier exists in a different menu, the canonical "wrong-menu parent" bug).
- `alias_collisions` — `{alias, collides_with, scope: pr-internal|repo-wide}` records. Built from a global walk of `aliases:` blocks across `content/**/*.md`; cross-references the PR file's *declared* aliases against everything else.
- `url_collisions` — `{file, scope: hugo-alias|s3-redirect}` records keyed off the PR file's *rendered* URL. The pre-step builds a unified URL-ownership map combining Hugo aliases and `scripts/redirects/*.txt` entries (with normalization across `index.html`, `.html`, and trailing-slash conventions). When the PR's URL is already claimed by another file's alias or by an S3 redirect source, it surfaces here. **This replaces the brittle hardcoded `PARALLEL_PATTERNS` table from earlier S38 ships** — Hugo's own aliases and the move-doc skill's redirect-table maintenance are the canonical signal of "this URL is already taken."

**Read this artifact and surface its findings as 🚨 by default.**
- `parent_exists_in_menu: false` → 🚨 menu-tree-breakage (Hugo will not render the parent linkage; user navigation breaks).
- `alias_collisions` with `scope: repo-wide` → 🚨 redirect-shadowing (Hugo's first-claim-wins semantics silently break one of the two routes).
- `url_collisions` with `scope: hugo-alias` → 🚨 file-location divergence (the PR is dropping content at a URL the existing canonical guide already aliases). The collided file is the canonical sibling — surface it in the cross-sibling reads bullet AND in the 🚨 file-location finding.
- `url_collisions` with `scope: s3-redirect` → 🚨 redirect-table conflict (the PR's URL is in the active S3 redirect table; the redirect either becomes dead or shadows the new content). Cite the redirect-file path and line.

The model still calibrates phrasing and may demote to ⚠️ when context overrides (e.g., the PR is *intentionally* renaming an existing identifier and removing the old declaration in the same diff — rare; cite the diff line in the trail when applied). The structural decision is the artifact's; demotion requires explicit reasoning in the trail entry.

**Pre-step artifact `.hugo-build.json`** (workflow pre-step `hugo-build-validate.py`, Ship K). Hugo is the canonical authority for routing and build correctness — read this artifact for the build-correctness floor instead of trying to reason about whether the build would succeed. The pre-step renders without `make ensure` (asset prep + data fetch are intentionally skipped), so it strips a known set of CI-environment-only lines before emitting and reports them under `suppressed_ci_noise` — you don't have to recognize or filter that noise yourself. The artifact carries:

- `errors` — `hugo --renderToMemory` ERROR lines from the PR head, with CI-environment noise already removed. Anything left here is a build-breaking failure (broken `{{< ref >}}` shortcode, template render failure, content with malformed frontmatter that can't load). Surface each entry as 🚨 build-failure with the exact Hugo message in the trail. If an entry still reads as CI-environment-only rather than PR-introduced (a class the filter didn't anticipate — see "Known CI-environment-only error classes" below), demote it silently and note `suppressed: CI-env-only` in the trail with one line of reasoning.
- `warnings` — Hugo WARN lines (CI-environment noise already removed). Most are informational (e.g., `WARN found no layout file for ...`). Triage: surface broken-asset / broken-link warnings as 🚨 — but `link_integrity` below already pre-computes that subset, so start there rather than re-scanning the full list — and surface informational warnings only when the PR introduces them.
- `link_integrity` — subset of warnings/errors that match link/ref/asset patterns (broken refs, missing assets, unresolvable shortcode targets). Surface as 🚨 unless the target is a page the same PR is adding (PR-internal — false-positive scenario).
- `sitemap_diff.added` / `sitemap_diff.removed` — URLs gained/lost in the rendered sitemap between the PR base and head. Removed URLs that aren't replaced by an alias on a remaining page are orphan candidates (existing inbound links and external SEO break). Surface as 🚨 orphaned-target unless the move-doc alias-injection pattern is visible in the diff.
- `head_exit_code` / `head_exit_nonzero_is_ci_noise` — `hugo`'s exit code, plus a flag. A non-zero exit is a build break the agent must surface even if `errors` is empty — *unless* `head_exit_nonzero_is_ci_noise` is `true`, which means the only thing that failed was the stripped CI-environment noise (the `/404` page fingerprints a stylesheet PostCSS never built); treat that as benign.
- `suppressed_ci_noise` — the lines the pre-step stripped, for auditing the filter. Not review material; never surface these.

**Known CI-environment-only error classes** (the pre-step already filters these; listed so you can recognize a near-miss): PostCSS / Hugo-Pipes asset-pipeline failures (`error calling Fingerprint`, `... can not be transformed to a resource`, anything mentioning `PostCSS` or `resources.Fingerprint`/`resources.PostCSS`), and `data/openapi-spec.json not found` (the OpenAPI data file is fetched by `make ensure`, not committed). See `hugo-build-validate.py` §"What this is NOT".

**Read this artifact early.** When `errors` or `link_integrity` is non-empty, those findings take priority over prose-level claims — the build floor is non-negotiable. Known false-positive scenarios mirror the frontmatter-validation set: PR adds the missing target in the same diff, PR moves a file with an alias, PR-internal cross-link to a sibling being added concurrently. Demotion requires explicit reasoning in the trail.

Templated sections include (non-exhaustive):

- `content/docs/pulumi-cloud/admin/sso/saml/` (SAML setup guides)
- `content/docs/pulumi-cloud/admin/scim/` (SCIM provisioning guides)
- `content/docs/iac/languages-sdks/` (language reference pages)
- Provider integration directories under `content/docs/iac/` and `content/docs/esc/integrations/`

Any directory with ≥3 files whose H1 titles read as parallel entities qualifies — detect dynamically rather than relying on this list.

**What to extract.** One record per:

- Navigation-step instruction ("Settings → Access Management"; "click *Configure*"; "select the *SAML* tab").
- H2 heading.
- Required-field label in setup forms ("Audience URI," "ACS URL," "Entity ID").
- Placeholder convention (`acmecorp`, `<your-org>`, `example.com`).

Verify each by reading the sibling pages and recording whether the same step / heading / label / convention appears.

**Claim record format:**

```json
{
  "id": "c12",
  "file": "content/docs/pulumi-cloud/admin/sso/saml/<vendor>.md",
  "line": 42,
  "claim_text": "Settings → Access Management",
  "claim_type": "cross-reference",
  "verification_method": "read-siblings",
  "sibling_set": ["auth0", "entra", "gsuite", "okta", "onelogin"]
}
```

**Sibling-read dispatch.** Fresh-review path only -- same constraint as §Subagent extraction dispatch. For each detected sibling set, fan out N parallel digest subagents via the Agent tool (`general-purpose`, Haiku 4.5), capped at 5 per batch (matches §Routed verification's Pass 1 lane batch cap). Each subagent prompt is *only* the file path plus the JSON digest schema `{nav_steps, h2_headings, required_field_labels, placeholder_conventions}` -- "quote each item verbatim with line number; do not analyze, compare, or extract claims." The main agent compares the N digests against the PR-under-review's claims; existing rendering, bucket-promotion, and confidence-calibration rules below apply unchanged. The fan-out makes the reads non-optional -- a model running short on turns can't elide them.

**Uniform-dispatch mandate.** Every sibling gets the **same** digest-schema prompt; only the file path differs across the N subagents. The main agent **must not**:

- Substitute a grep / read-snippets / partial-scan for any sibling, even when the diff seems "small enough" or the sibling looks "structurally similar to the others" -- the model cannot know in advance which sibling reveals the navigation-step divergence.
- Vary the digest schema by sibling (e.g., "skip placeholder_conventions on entra because we already have it from okta") -- consistency across siblings is what makes the comparison sound.
- Pre-classify which siblings warrant full digests vs. cheap checks. There are no cheap checks; every sibling earns its full digest. The whole point of the schema is uniform extraction.

When the fan-out reports `5 of 5 siblings`, all five must have produced complete `{nav_steps, h2_headings, required_field_labels, placeholder_conventions}` records. If even one sibling was partial-read, the count is wrong and the cross-sibling-consistency dimension cannot land at HIGH confidence.

**Evidence-trail rendering** (verbatim into output-format.md §Verification trail):

- `L42 "Settings → Access Management" → ✅ matches entra/gsuite/okta/onelogin (5 of 5 siblings checked; 4 match, 1 has no equivalent step)`
- `L42 "Settings → SAML SSO" → 🚨 mismatch: scim/{okta,entra,onelogin}.md all use Settings → Access Management; this PR diverges`

**Bucket promotion.** Navigation-step mismatches trigger the workflow-breaking-instruction always-🚨 carve-out — the reader lands on the wrong page. Heading-style, placeholder, or other non-workflow-breaking divergences render as ⚠️, with the divergence noted in the trail.

**Confidence calibration.** The `cross-sibling consistency` dimension is HIGH only when every sibling was read; MEDIUM when most were; LOW when fewer than half were. The parenthetical must report the ratio (e.g., "read 2 of 5").

### Claim extraction examples

Worked examples of correct extraction from real prose patterns. Each shows the paragraph, the extracted claims, and the reasoning.

**Example 1 -- composite claim**

> "Pulumi ESC supports AWS, Azure, and Vault."

- Claim 1: "Pulumi ESC supports AWS." (type: `feature existence`)
- Claim 2: "Pulumi ESC supports Azure." (type: `feature existence`)
- Claim 3: "Pulumi ESC supports Vault." (type: `feature existence`)
- Reasoning: each listed integration is separately verifiable. Combining them hides which one is wrong when only one is.

**Example 2 -- implicit comparison**

> "Unlike Terraform, Pulumi uses real programming languages."

- Claim 1: "Pulumi uses real programming languages." (type: `feature existence`)
- Claim 2 (implicit): "Terraform does not use real programming languages." (type: `feature existence`)
- Reasoning: "unlike X" asserts a property of X. Extract the implicit claim so it can be verified independently.

**Example 3 -- quantitative**

> "chardet is 41x faster at encoding detection than its predecessor."

- Claim: "chardet is 41x faster at encoding detection than its predecessor." (type: `numerical` / `benchmark`)
- Reasoning: any specific multiplier needs a source. The 🤔 intuition-check may also fire -- "41x" is unrounded and suspiciously specific.

**Example 4 -- negative**

> "Pulumi doesn't support ARM templates."

- Claim: "Pulumi doesn't support ARM templates." (type: `feature existence`, negative)
- Reasoning: harder to verify (proving a negative) -- requires reading the provider registry and confirming no matching package exists. Annotate as `verification_difficulty: high` so the subagent knows it may need extra evidence.

### Claim record format

```json
{
  "id": "c1",
  "file": "content/docs/cli/logout.md",
  "line": 42,
  "claim_text": "pulumi logout removes credentials for all backends",
  "claim_type": "command-behavior",
  "verification_method": "exec",
  "temporal_trigger": null,
  "intuition_check": false
}
```

### Temporal-claim handling

Any claim containing one of the trigger words below receives a `temporal_trigger` annotation:

- `recently`
- `now supports`
- `new` / `newly`
- `just launched`
- `latest`
- `introduced` (when paired with a recent-sounding sentence)

When a temporal claim is verified, record the result with a date anchor:

> As of $TODAY (2026-04-23), Pulumi ESC supports AWS IAM rotation.

The date anchor captures "verified true at this point in time."

When a temporal trigger word is **not warranted** -- e.g., "recently" describing a change from years ago -- flag as `contradicted: temporal misuse` with the suggested fix ("replace 'recently' with the actual timeframe, or drop the temporal qualifier").

### Intuition-check axis

Intuition-check is **orthogonal to verification**. It scores the *shape* of a claim, not the evidence behind it. A claim can be both 🤔 (shape-suspect) and ✅ (verified), or 🤔 and 🚨 (contradicted); the intuition-check is a separate dimension.

#### When to set the `intuition_check` flag

Set the flag during claim extraction (before verification) if any of the following holds. Each sub-rule has an explicit threshold to keep the flag consistent across runs:

- **Unrounded specific numbers in a prose claim.** A number reads as "unrounded" when it is not a common human-communicated figure. Concrete thresholds:
  - **Round** (do not flag): multiples of 5% or 10%, typical marketing figures like 2x / 10x / 50x / 100x, order-of-magnitude ranges ("hundreds of," "thousands of").
  - **Unrounded** (flag): any digit pattern outside the round set. Examples: `41x`, `37.4%`, `2,347`, `93.2 ms`, `17.8 GB/s`. "A 200% improvement" is round (multiple of 100%); "a 193% improvement" is unrounded (flag).
  - Exception: if the claim names a source in the same sentence ("per the ACME 2024 benchmark"), do not flag on shape -- the source will be verified in the normal flow.
- **AI-pattern phrasing.** The following adjective set (and close variants) is AI-boilerplate: *blazing-fast, seamlessly integrates, world-class, battle-tested, revolutionary, cutting-edge, next-generation, enterprise-grade*. Presence of any term in a technical claim is enough to flag.
- **Specific but unsearchable.** A claim that looks like a quotable stat with a named source (e.g., "Used by 73% of Fortune 500 companies" / "Deployed in over 40 countries") but lacks a citation in the PR. "Specific" here means: a percentage, a country count, a customer count, a time-window claim.

Set `intuition_check: true` on the claim record. Verification proceeds normally.

#### Rendering rule (where 🤔 claims actually land)

After verification, render each claim in the bucket dictated by its verification result, **with the intuition-check flag surfaced in the evidence line**:

| Verification result | `intuition_check=true` renders in | Evidence-line note |
|---|---|---|
| `contradicted` (any confidence) | 🚨 Needs your eyes | No 🤔 note needed; the contradiction already demands a fix |
| `unverifiable` | 🚨 Needs your eyes | "Shape also suggests fabrication; cite a source" |
| `verified` with `confidence: low` | ⚠️ Low-confidence verified | "Shape was suspect; verifier found a low-confidence match" |
| `verified` with `confidence: medium` or `high` | ✅ Verified | No 🤔 note; evidence resolves the shape concern |
| **verification timed out / inconclusive** | 🤔 Intuition-check | "Verifier couldn't resolve; author should cite a source" |

The 🤔 bucket is therefore **small and specific**: claims whose shape was suspect AND whose verification returned neither a confirmation nor a contradiction. The model should not render 🤔 when the verifier produced a decisive answer either way.

### Subagent extraction dispatch

*Fresh-review path only. Re-entrant updates use `docs-review:references:update` -- don't fan specialists across a fix-response / dispute / re-verify pass; the deltas are localized and replication beats decomposition there.*

Spawn four parallel claim-finder subagents via the Agent tool (`general-purpose`, Sonnet 4.6 each). Each specialist owns a narrow slice of §Claim extraction; the slices are non-overlapping by design except for `framing`, which is a heuristic specialist that scans across canonical types.

- **`numerical`** -- `Numerical` + `Version/availability` rows + §Temporal-claim handling trigger list.
- **`cross-reference`** -- `Cross-reference` row + §Cross-sibling consistency *templated-section detection* and *what to extract* (the per-record list -- not the rendering / promotion / calibration tail). Identifies which siblings need reading; the reads themselves are a separate fan-out (see §Cross-sibling consistency).
- **`capability`** -- `Command behavior`, `Flag/option existence`, `Output format`, `Feature existence`, `Resource API surface` rows.
- **`framing`** -- heuristic specialist; canonical claim-type table unchanged. `Quote/attribution` row + framing-strength phrase list (`the only`, `the first`, `currently`, `as of <year>`, `is the leading`, `industry standard`, named-source quotes). Flags matches regardless of which canonical type the surrounding sentence falls under -- corroborates the others where the slices meet.

Each subagent prompt copies *only* its slice rows verbatim, plus §Skip rules, §Claim record format, and §Source-class classification (each emitted claim must carry a `source_class` value). Do **not** include the full table, other subagents' rows, §Frontmatter sweep, §Intuition-check axis, §Cited-claim spot-check, §Routed verification, or §Claim extraction examples — those belong to other phases or to the main agent. Per-claim cap ~250 words.

#### Source-class classification

Every emitted claim record carries a `source_class` field. The class determines the verification route (see §Routed verification); classifying defensively at extraction time is what makes the route cheap.

| `source_class` | When it applies | Verification route |
|---|---|---|
| `pulumi-internal` | References `pulumi/*` package, flag, command, version, schema, or another Pulumi doc page | Inline (main-agent gh check; no subagent) |
| `external-public` | Cites a URL, names a third-party vendor with a statistic, references a regulatory date, quotes a named source from a public article | Pass 2 web fan-out (skip Pass 1) |
| `ambiguous` | Shape is mixed; could be either | Pass 1 cheap-source attempt; Pass 2 on miss |

Apply these rules in order; first match wins:

1. Cited URL in the prose → `external-public`. The URL tells the verifier where to look; pulumi-internal claims don't need one.
1. Names a `pulumi/*` package, flag, version, command, or method → `pulumi-internal`.
1. Internal cross-reference (other Pulumi doc, sibling page, registry path, `/static/programs/` file) → `pulumi-internal`.
1. Vendor name + statistic + survey/report reference → `external-public`.
1. Regulatory body name + date or rule number → `external-public`.
1. Named-source quote (any "[name] said …" pattern) → `external-public`.
1. Generic capability or feature claim with no specific source → `ambiguous`.
1. Otherwise → `ambiguous`.

When uncertain, default to `ambiguous` rather than `pulumi-internal`. The cost of mis-routing an external claim through Pass 1 is higher than mis-routing an ambiguous one — the former wastes the entire Pass 1 attempt; the latter just adds one cheap gh search.

#### Combine step

1. **Dedup.** Key = `<file>:<line>` plus the first 40 chars of `claim_text` (lowercased, whitespace collapsed). Merge near-paraphrase matches; pick the most specific framing.
1. **Annotate.** Set `found_by: [<specialist>, ...]` from `numerical`, `cross-reference`, `capability`, `framing`. Single-specialist finds are the expected state -- the slices are non-overlapping by design -- and are not a confidence signal. When `framing` corroborates one of the others on the same claim (e.g., `[capability, framing]` on a feature claim with framing-strength language), set `cross_specialist_corroboration: true` -- a positive signal for the OutSystems-shape catch, not the absence of it as a low-confidence flag.
1. **Reconcile `source_class`.** If specialists disagree on the same deduped claim, take the most external classification (`external-public` > `ambiguous` > `pulumi-internal`) -- routing toward the more thorough lane is the safe default.
1. **Frontmatter sweep** runs here -- repeated body / `meta_desc` / `social:` phrasings collapse into a single claim with multiple cited locations regardless of which subagent caught each occurrence.
1. **Hand off.** Deduped list goes to §Routed verification; downstream schema unchanged except for the new `source_class` field on each record.

Store the deduped claim list for the verification phase. No interim user output.

---

## Routed verification

*Fresh-review path only. Re-entrant updates use `docs-review:references:update` -- don't fan specialists across a fix-response / dispute / re-verify pass; the deltas are localized and replication beats decomposition there.*

Each claim's `source_class` (set at extraction) routes it to one of four verification lanes. The lanes have different cost / latency / fan-out shapes; routing by classification avoids running Pass 1 on claims it has no chance of resolving (vendor statistics, regulatory dates, named-source quotes) and avoids dispatching a subagent at all for claims that close in two `gh` calls (Pulumi feature/flag/version checks). Pass 2 and Pass 3 split what older versions of this doc called the single "external" lane — one lane consults pre-fetched URLs from the workflow; the other dispatches WebSearch + WebFetch for claims with no URL in the diff.

| `source_class` | URL in diff? | Lane | Mechanism |
|---|---|---|---|
| `pulumi-internal` | n/a | **Inline** | Main agent runs the cheap-source check during the combine step. No subagent. |
| `ambiguous` | n/a | **Pass 1 → Pass 2 / Pass 3** | Batched cheap-source subagents; defer on miss to whichever external lane fits the claim shape. |
| `external-public` | yes | **Pass 2 (URL fetch)** | Consult `.fetched-urls.json` (workflow pre-step). Per-claim subagent if extraction needs reasoning; inline read otherwise. |
| `external-public` | no | **Pass 3 (search-then-fetch)** | Per-claim Sonnet web fan-out: WebSearch + WebFetch top results. |

### Inline lane (`pulumi-internal`)

Main agent walks §Verification source order steps 1-3 sequentially during the combine step. Emit the verdict directly into the trail; no subagent dispatch.

**Per-claim cap: 5 gh CLI calls.** After 5 `gh` calls without resolution on a single claim, stop. Reclassify the claim to `ambiguous` (→ Pass 1) or `external-public` (→ Pass 2 / Pass 3) and let the lane designed for harder verifications take it. The cap is hard, not aspirational — when in doubt at call 4, defer rather than push through.

**Per-PR cap: 40 gh CLI calls total.** After ~40 inline `gh` calls across all claims on the PR, stop the inline lane: summarize the remaining unresolved pulumi-internal claims and dispatch them as a single Pass 1 batch with the canonical-source playbook embedded. That batch is the escalation tier — beyond 40 calls of productive depth, the marginal claim is more likely to close in Pass 1's batched-subagent shape than in another inline iteration. The cap is approximate, not surgical: 40 is the budget that gives the model ~8 claims of full-depth verification; pushing to 50 is the over-spend zone (operator-visible via `::error::` annotation in CI).

**Don't iterate to find prior discussion.** Specifically: don't loop `gh api repos/pulumi/docs/issues` or `gh api repos/pulumi/docs/pulls` searching for prior PRs / issues / discussions about a topic. That's exploration, not verification — read the actual code path, release notes, or `pulumi/pulumi` source instead. One targeted `gh search code` or `gh api` call resolves the typical pulumi-internal claim; if that doesn't close it, the claim isn't pulumi-internal and belongs in another lane.

If the inline check fails to resolve a claim that was classified `pulumi-internal` (e.g., a Pulumi-related claim that turns out to also depend on external confirmation), reclassify it to `ambiguous` and route to Pass 1.

**Canonical sources for pulumi-internal verification.** Read the canonical source first.

| Claim shape | Canonical source |
|---|---|
| Menu / left-nav | `data/docs_menu_sections.yml`; rendered via `layouts/partials/docs/menu.html` |
| Example-program | `static/programs/<name>-<lang>/` |
| Sibling-pattern (frontmatter, file location, alias) | Nearest sibling under `content/docs/<closest>/` |
| Resource schema / API surface | `pulumi/pulumi-<provider>` |
| Shortcode | `layouts/shortcodes/<name>.html` |
| Alias / redirect | `aliases:` frontmatter + `scripts/redirects/*` |
| Frontmatter field semantics | An existing page in the same content tree that uses the field |

Search-order rules:

1. **Token first.** `gh search code --owner pulumi "<token>"` when the claim names a symbol/flag/filename/shortcode.
2. **Path second.** `gh api repos/<owner>/<repo>/contents/<path>` when the canonical path is known.
3. **Never `issues` or `pulls` for context discovery.** A targeted `gh issue list -R <repo> --search "<term>"` is fine when the claim is *about* a prior decision.
4. **No recursive tree-walking until 3 targeted reads have failed.**

**Shrug rule.** If 3 targeted reads don't close the claim, mark it `ambiguous` and route to Pass 1.

### Pass 1 lane (`ambiguous`)

Spawn parallel subagents (`general-purpose`, Sonnet 4.6), batched **up to 4 at a time**. Each subagent receives a small group of related claims (group by file or by claim type, whichever is smaller). If more than 20 ambiguous claims are extracted, batch by file rather than per-claim.

For each claim, walk §Verification source order steps **1-3** only (skip step 4 / WebFetch entirely):

1. Local repo / linked docs.
2. GitHub via `gh` CLI.
3. Live code execution (read-only).

Emit one of:

- **Verdict + source** — `verified` (with confidence rating), `contradicted` (with the divergence quoted), or `unverifiable` *only* when the claim is genuinely not fetchable from any source (paywalled, internal-only, future-dated). Do **not** default to `unverifiable` for claims a public web source could resolve -- defer instead.
- **Defer to Pass 2 or Pass 3** — claim needs the workflow's pre-fetched URL contents (Pass 2) or WebSearch + WebFetch (Pass 3). Pass 1 hands it off without rendering a verdict; the routing logic at the top of this section picks the right external lane.

### Pass 2 lane (`external-public` with URL in diff)

The workflow's pre-step `extract-urls-and-fetch.py` parses the PR diff for markdown links / autolinks / bare URLs in `content/(docs|blog)/**/*.md` and fetches each. The result lands in `.fetched-urls.json` at the repo root: `[{url, status, content_text, fetch_ms, error?}, ...]`. Cap 30 URLs per review; per-fetch timeout 10s.

**Pass 2 verification consults `.fetched-urls.json`. Do NOT WebFetch URLs already present in this file** -- the workflow has already done the network round-trip. The model reads the `content_text` for the URL it would have fetched, locates the supporting passage, runs §Cited-claim spot-check on it, and emits the three-field evidence line.

For each `external-public` claim whose URL appears in `.fetched-urls.json`:

- If the cited URL's `status` is 200 and `content_text` addresses the claim → render verdict (`verified` / `contradicted`) per spot-check.
- If `status` is non-2xx (dead link / paywall / soft-404) **or** `content_text` exists but doesn't address the claim → bounce to **Pass 3** for a fresh search; do not emit ⚠️ unverifiable from Pass 2.

**Dispatch unit:** Pass 2 typically runs inline (the content is already in `.fetched-urls.json`; no subagent needed). Spawn a Sonnet 4.6 subagent only when the claim requires substantial reasoning over the fetched content (multi-paragraph framing comparison, table extraction, etc.). At small N, the subagent overhead dominates -- prefer inline reads.

### Pass 3 lane (`external-public` without URL in diff)

For each `external-public` claim that does NOT have a URL in the PR diff, dispatch Sonnet 4.6 subagents (`general-purpose`) **in parallel**. Pass 3 is the search-then-fetch lane: WebSearch a query derived from the claim, then WebFetch the top 1-3 results.

**Mandatory dispatch.** Pass 3 cannot be skipped for external-public claims that need it. The model cannot silently roll an external-public claim into the Inline / Pass 1 lane to avoid the search dispatch -- the validator's `pass-3-dispatch-mandate` rule trips when external-public claims exist with no URL fetched and Pass 3 count is 0.

**Dispatch unit:**

- Default: **batch 2-3 claims per subagent**. Setup overhead per Pass 3 subagent (framing taxonomy + spot-check procedure + verdict format ≈ 800 words) amortizes across claims.
- Exception: if **<5 claims total** are routed to Pass 3, drop to per-claim -- parallelism gain dominates batching savings at small N.

Each Pass 3 subagent walks §Verification source order step **4** (WebFetch / WebSearch), then runs §Cited-claim spot-check end-to-end per claim. Subagent prompts must be self-contained -- copy in §Verification source order step 4, the §Cited-claim spot-check procedure with the framing taxonomy (`exact-match`, `strengthened`, `narrowed`, `shifted`, `contradicted`), and the §Mandatory evidence-line format. Per-claim cap stays ~250 words.

**Negative-evidence pointer for ⚠️ unverifiable verdicts.** A Pass 3 ⚠️ unverifiable verdict requires the trail entry to name the search that was attempted: `WebSearch ran query "<phrase>"; top N results didn't address the claim`. The validator's `pass-3-unverifiable-evidence` rule trips when the evidence pointer is missing. Pass 3 cannot shortcut to ⚠️ unverifiable without trying.

Output: claims close as `verified` (high/medium/low confidence), `contradicted`, or `unverifiable` (genuinely unfetchable -- defensible now because Pass 3 actively searched and the trail entry names the search).

### Verification source order (cheapest first)

#### 1. Local repo / linked docs

Grep/Read other content files; follow internal links to verify the target exists and matches the claim; read referenced `/static/programs/` files. **Cheapest source -- always try first.**

#### 2. GitHub via `gh` CLI

For any claim about Pulumi product source, provider behavior, version availability, or feature existence, query GitHub directly using authenticated `gh`. The user has access to virtually all `pulumi/*` repos (including private ones), so this is *deterministic and complete* in a way WebFetch is not.

Patterns to use:

```bash
# Find references to a feature/flag/method across all Pulumi repos at once
gh search code --owner pulumi "<term>"

# Read source files directly to verify API surface (resource properties, CLI flags, etc.)
gh api repos/pulumi/<repo>/contents/<path>

# Verify "added in v3.230" / "available since" claims against actual release notes
gh release list -R pulumi/pulumi --limit 20
gh release view <tag> -R pulumi/pulumi

# Confirm when a feature actually landed
gh api "repos/pulumi/pulumi/commits?path=<file>&since=<date>"

# Find prior decisions, "we decided not to ship this," or "this was renamed"
gh issue list -R pulumi/<repo> --search "<term> in:title,body"
gh pr list -R pulumi/<repo> --search "<term>"

# Read provider schema generation source for resource property claims
gh api repos/pulumi/pulumi-<provider>/contents/provider/cmd/...
```

`gh` results count as `confidence: high` when they directly match the claim, because they read source-of-truth from the actual repo. **Subagents should prefer `gh` over WebFetch whenever the claim is about anything `pulumi/*` ships.** This is the primary GitHub access mechanism for this procedure -- do not substitute the GitHub MCP.

#### 3. Live code execution

For CLI claims, actually run the command. Subagents are explicitly authorized to invoke:

- `pulumi --help`, `pulumi <subcommand> --help`, `pulumi version`
- `make build`, `make lint` from the worktree
- `npm`, `go`, `python` (read-only operations)

Subagents must **require user confirmation** before any state-changing cloud operation (anything that creates or modifies real resources). For code snippets, run them through the relevant `static/programs/` test harness when applicable:

```bash
ONLY_TEST="program-name" ./scripts/programs/test.sh
```

#### 4. WebFetch / WebSearch

Use WebFetch for any non-Pulumi source the claim depends on — provider docs, vendor pricing/licensing/product pages, third-party announcements, regulatory bodies, standards documents, anything publicly fetchable that resolves the claim. The list is illustrative, not exhaustive. Skip in favor of `gh` whenever the claim is about Pulumi itself.

`unverifiable` is a verdict for claims that are genuinely not fetchable (paywalled, internal-only, future-dated). It is NOT the default for vendor capability/pricing/licensing claims when a public web source could resolve them. If a publicly fetchable source could verify or contradict the claim, fetch it before defaulting to `unverifiable`.

**Vendor-licensing carve-out.** When the claim takes the shape `vendor X requires Plan Y or higher`, `feature Z is available on the Enterprise tier`, or any other plan-name / tier-gating phrasing, the vendor's pricing or product-tier page is the canonical source — fetch it before defaulting to ⚠️ unverifiable. Pricing pages are public and stable; the `unverifiable` verdict on a vendor licensing claim almost always indicates "the verifier didn't try" rather than "the page is genuinely paywalled." For JS-rendered pricing pages where WebFetch returns an empty body, `verified weakly` (with the source URL and a note that the body wasn't programmatically extractable) is the right verdict — not ⚠️ unverifiable. Reserve `unverifiable` for vendor pages that are 404, behind a login wall, or actively redirect away (those are real signals to surface to the maintainer).

#### 5. Notion + Slack (best-effort)

Only if MCP tools are present in the runtime tool set. Use these to catch internal context that hasn't made it into a repo yet -- "we decided not to ship this," "this was renamed," "the CEO sketched this in a doc but it's not built."

```
mcp__claude_ai_Notion__notion-search
mcp__claude_ai_Slack__slack_search_public_and_private
```

Default search window: last 6 months. Absence of these tools must not fail the workflow -- annotate the evidence as "internal sources unavailable."

#### Cited-claim spot-check

When a claim has an inline citation (URL, paper reference, named source), the verification step is *not* "trust the link" — it's "fetch the cited source and confirm it supports this exact framing."

Spot-check procedure:

1. Fetch the cited URL via WebFetch (or the source content via the appropriate tool).
1. Find the supporting passage in the source.
1. Compare the source's framing to the claim's framing. Does the source say *exactly what the PR claims*, or has the PR strengthened, narrowed, or shifted the framing?
1. If the source supports the exact framing, mark `verified, confidence: high` with the source pointer in evidence.
1. If the source is close but not exact (e.g., "in some capacity" became "in production"), mark `contradicted: source mismatch` with the divergence quoted.
1. If the source is unreachable or the cited URL doesn't actually contain the supporting passage, mark `unverifiable` with an author-question line.

Cited claims that pass spot-check land in ✅ Verified at high confidence — the citation made verification cheap. Cited claims that fail spot-check are *more* damning than unverifiable ones, because the author asserted a source they didn't actually consult.

##### Mandatory evidence-line format for cited claims

Cited-claim verdicts must produce a three-field evidence line:

```
- L<line> "<claim text>" → <verdict emoji> <verdict>
  - source quote: "<verbatim passage from fetched page>"
  - framing: <exact-match | strengthened | narrowed | shifted | contradicted>
```

A verdict without a verbatim source quote is a verdict without evidence — `(same report)`, `(URL resolves)`, `(linked inline)` record that fetching happened, not that comparison happened. Downgrade to `unverifiable` if the verbatim quote is missing.

Framing labels (only `exact-match` lands ✅; the rest land 🚨 under the contradicted-factual-claim carve-out):

- `exact-match` — source phrasing is the claim's phrasing, or a literal paraphrase of equal scope.
- `strengthened` — claim is a subset of the source. Source: "use"; claim: "use in production."
- `narrowed` — claim is broader than the source. Source: "U.S. enterprise"; claim: "enterprise."
- `shifted` — same numeric anchor, different subject. Source: "evaluate AI agents"; claim: "deploy AI agents."
- `contradicted` — source positively disagrees with the claim.

Example (strengthened framing):

```
- L40 "96% of enterprises run AI agents in production today" → 🚨 contradicted (source mismatch)
  - source quote: "96% of enterprises now use AI agents"
  - framing: strengthened — claim narrows "use" to "in production today"
```

### Confidence calibration

Subagents rate each verified claim as high / medium / low. Use the rubric below; don't default to "medium" when the evidence is ambiguous -- pick based on source quality.

| Rating | Criteria |
|---|---|
| **High** | Direct match in an authoritative source: provider schema source file, official docs page, release notes with matching version, `gh`-surfaced commit that introduced the feature, CLI `--help` output that the claim mirrors exactly |
| **Medium** | Indirect evidence: keyword collocation in the relevant repo, partial match in docs (claim phrasing differs from source phrasing but maps to the same concept), source exists but the page is older than the claim's temporal context |
| **Low** | Circumstantial: pattern-matching across multiple near-matches, a single forum / blog post, plausible but unverified by an authoritative source |

Examples:

- *Claim:* "`pulumi up` accepts a `--stack` flag."
  *Evidence:* `gh api repos/pulumi/pulumi/contents/sdk/go/cmd/pulumi-language-go/main.go` shows the `--stack` flag registered on the `up` subcommand.
  *Rating:* **high** -- direct source match.

- *Claim:* "Pulumi ESC integrates with Vault."
  *Evidence:* `pulumi/esc` README mentions Vault among other providers; no linked doc page shows a worked example.
  *Rating:* **medium** -- source exists but doesn't exactly match the "integrates with" phrasing; author may have overstated.

- *Claim:* "Most Pulumi users deploy on AWS."
  *Evidence:* No single source; multiple blog posts reference Pulumi+AWS prominently.
  *Rating:* **low** -- circumstantial.

### Subagent prompts

Subagent prompts must be self-contained — copy the rules into the prompt rather than referencing them. Per-lane requirements are spelled out in §Routed verification (Pass 1: §Verification source order steps 1-3 + §Claim record format; Pass 2: §Verification source order step 4 + the framing taxonomy + the §Mandatory evidence-line format). The inline lane runs on the main agent and needs no subagent prompt. Per-claim cap of ~250 words across both subagent lanes.

---

## Tiered triage

Build a structured triage object.

### Tier rules

Tier emoji conventions: 🚨 (Outstanding) and ⚠️ (Low-confidence verified) align with the canonical buckets in `docs-review:references:output-format`. ✅ Verified here is fact-check's own collapsed-details bucket — distinct from the canonical ✅ Resolved-since-last-review used elsewhere; do not conflate them. 🤔 Intuition-check has no canonical counterpart.

| Tier | Contents |
|---|---|
| 🚨 Needs your eyes | All `contradicted` claims (any confidence) + all `unverifiable` claims |
| 🤔 Intuition-check | Claims whose `intuition_check` flag was set AND whose verification came back inconclusive (timed out, could not reach a verdict). Cross-reference the shape concern in the evidence line. |
| ⚠️ Low-confidence verified | `verified` claims with `confidence: low` (and `medium` when scrutiny is heightened). Prefix the evidence line with "verified weakly" to distinguish from generic low-confidence findings. |
| ✅ Verified | Everything else, collapsed under `<details>` |

When a claim is flagged `intuition_check: true` AND the verifier reaches a decisive verdict, it renders in the verdict's bucket (🚨 / ⚠️ / ✅), not 🤔 -- see the rendering rule table in §Intuition-check axis. 🤔 is for inconclusive verification only.

### Credential redaction

The evidence line of any finding is rendered into the public pinned comment. **Never quote raw credential strings in evidence** -- file:line and a short description only. If the claim's context contains what looks like an API key, token, password, private URL, or connection string, replace the token with `[REDACTED]` in the evidence line and flag the underlying leak as a separate 🚨 finding (per `docs-review:references:infra` §Secret handling). Public-PR diffs are already exposed; the pinned comment must not amplify the leak by quoting the raw value.

Patterns that trigger redaction on sight:

- Strings matching common token formats (`ghp_*`, `sk-*`, `AKIA*`, `pul-*`, `xoxb-*`, JWT-like `eyJ*`).
- Hostnames ending in `.internal`, `.priv`, or any hostname paired with an obvious secret (`https://user:pass@...`).
- Strings with ≥32 contiguous alphanumeric characters that don't match a known non-secret format (UUIDs are OK; opaque blobs are not).

---

## Author-question buffer

For every `unverifiable` claim and every 🤔 intuition-check finding, add a line-anchored entry:

```
- content/blog/esc-rotation.md:88 — Source for "ESC supports automatic rotation for Vault secrets"?
- content/blog/perf.md:14 — Cite a source for "chardet is 41x faster at encoding detection"?
```

---

## Assessment rules

Preserve the PR-introduced vs pre-existing distinction throughout: contradictions in the diff are PR-introduced; contradictions in unchanged prose are pre-existing.

---

## Heightened-scrutiny overrides

When the caller passes `scrutiny=heightened`:

- The `heightened` branch of §Scope (full-file claim extraction), §Verification source order (web/`gh` verification by default on every claim), and §Tier rules (medium-confidence verified surfaces to ⚠️ Low-confidence verified instead of collapsed ✅ Verified) applies.
- Pre-existing issue extraction runs per the rules below.

### Pre-existing issue extraction

When `scrutiny=heightened`, the verifier reads the **full file** for claim extraction. Any substantive issue noticed in unchanged prose renders in the 💡 Pre-existing bucket:

- **Do extract:** broken links, wrong facts, code typos (missing imports, wrong method names), deprecated terminology, temporally-rotted claims.
- **Do NOT extract style nits:** heading case, list numbering, em-dash frequency, paragraph rhythm, trailing whitespace. Those are linter territory or out of scope for fact-check.
- **Cap:** per `docs-review:references:output-format`. If the file has more substantive issues than the cap, the top N render; surplus is noted as "+N additional pre-existing findings" in the bucket.
