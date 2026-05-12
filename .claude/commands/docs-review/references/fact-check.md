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
  - 🚨 Needs your eyes (contradicted)
  - ⚠️ Low-confidence (verified with low confidence, or medium when `scrutiny=heightened`; plus unverifiable claims, each with an author-question line)
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

The full "what counts as a claim" definition — the enumerated taxonomy, the granularity / compound-decomposition rule, the explicit "what is NOT a claim" list (including the third-party-attribution flip), the framing/speech-act rule, and worked examples — lives in `docs-review:references:claim-extraction`, the single source of truth shared with the claim-extraction pre-step. Read it; this section is the table-of-contents, that file is the body.

### Pre-step artifact `.candidate-claims.json` (the claim floor) — read this first

Workflow pre-step: `extract-claims.py` (a deterministic regex floor — numbers, version pins, temporal words, source attributions, URLs, named-entity/spec claims, positioning/comparison trigger words) ∪ two redundant Sonnet passes `extract-claims-llm.py` (one atomic/per-sentence-framed, one holistic/paragraph-framed, both prompted with `docs-review:references:claim-extraction`) → unioned and deduped by `merge-claims.py` into `.candidate-claims.json` at the repo root: `{"claims": [{"file", "line_range", "text", "type", "source_hint"?, "confidence", "found_by": [...], "line_range_unverified"?}], "errors": [...], "meta": {...}}`.

**This list is the claim *floor*, not a ceiling.** The review **MUST** extract and verify every entry — surface a verdict for each one in the 🔍 Verification trail (the `candidate-claims-coverage` validator rule fails the review, soft-flooring loudly, if a candidate claim has no overlapping trail record). The review **MAY** add claims the artifact missed — the LLM passes are high-recall, not exhaustive, and the regex floor is shape-based. So: start from the artifact's `claims`, fold in anything else you spot in the diff, dedup, verify the union.

**Known false positives the artifact will contain** (the reviewer's contract is to triage each entry — see `docs-review:references:pre-computation` §"False-positive triage is a contractual responsibility"): the regex layer matches `text` shapes, not meaning, so it surfaces things like a `:latest` tag in a `Dockerfile` comment (a tag name, not a recency claim), a `/latest/` segment in a URL, a faithful description of the author's *own* design ("our pipeline runs three times…" — not a claim unless attributed to a third party), git metadata. When you triage a candidate claim down to "not actually a checkable claim", **record the demotion in the trail** anyway (`- L42 "<text>" → ➖ not-a-claim — <one-line reason>`) — that's what satisfies `candidate-claims-coverage` and traces the call. Demote, never silently drop. See `docs-review:references:claim-extraction` §"What is NOT a claim" for the full list.

**Degraded pre-step.** If `.candidate-claims.json` carries a non-empty `errors` array (an LLM pass failed, no `ANTHROPIC_API_KEY`, etc.), extraction was degraded — note "claim-extraction pre-step degraded; reverting to in-review extraction" in the trail, and run the in-review extraction (§Subagent extraction dispatch) yourself as a fallback. If the artifact is absent entirely (interactive `/docs-review`, or the workflow didn't run the pre-step), use the in-review extraction path as today — same fallback.

**Don't open this artifact when `.verified-claims.json` supersedes it.** On the normal CI path the verify-claims pre-step also ran and wrote `.verified-claims.json` whose `verdicts[]` carries one entry per candidate claim — `claim_id`, `file`, `line_range`, `text`, `type`, plus the verdict, `evidence`, and `source` — so it is a superset of `.candidate-claims.json` for everything the review needs. Read `.verified-claims.json` (§Routed verification) and treat *its* `verdicts[]` as the floor; don't also read `.candidate-claims.json` on that path. Read `.candidate-claims.json` directly only when `.verified-claims.json` is absent or its `verdicts[]` is empty (whole verify-claims-step crash) — then it's the floor and the in-review verification fallback applies.

`line_range_unverified: true` on a `.candidate-claims.json` entry means the LLM-asserted line range was out of bounds for the file and got clamped — trust the `text`, treat the line range as approximate when anchoring the trail entry.

### Scope

- Default (`scrutiny=standard`): extract claims from the diff only -- lines added or modified
- `scrutiny=heightened`: extract claims from the **full file**, not just the diff. AI hallucinates surrounding prose, not just changed lines.

### Frontmatter sweep

Hugo posts duplicate the same load-bearing phrasing across the body, `meta_desc`, and `social:` sub-keys (`twitter`, `linkedin`, `bluesky`). When extracting a claim from any of these locations, scan the rest of the file -- body plus every prose-bearing frontmatter key -- for the same factual phrasing or a near-paraphrase, and treat all occurrences as one claim with multiple cited locations. A single finding then renders one suggestion-block per location, so a verified-false claim is fixed everywhere in one pass.

**Pin the sweep scope to the pre-step artifact.** `.frontmatter-validation.json` (workflow pre-step `frontmatter-validate.py`) carries `frontmatter_keys` per file — the flat list of that file's frontmatter keys with one level of nesting expanded (`title`, `meta_desc`, `description`, `summary`, `social.twitter`, `social.linkedin`, `social.bluesky`, `menu.iac`, `aliases`, …). Sweep **exactly** `body` plus the prose-bearing keys in that list (`meta_desc`, `description`, `summary`, `title`, every `social.*` sub-key) — do **not** decide the scope ad hoc. Skip the structural keys (`menu.*`, `aliases`, `weight`, `date`, `draft`, `meta_image`, `authors`, `tags`). When you render the "Frontmatter sweep" investigation-log line, name the locations you actually swept (`ran on body + meta_desc + social.twitter + social.linkedin`); the validator checks that against `frontmatter_keys`. *(The failure mode this guards against: a sweep over `body + meta_desc` that silently omits the `social.*` sub-keys, dropping social/title framing-mismatch findings.)*

Example: a blog post says "96% of enterprises run AI agents in production today" in the body, and the same phrase (or a paraphrase: "96% of enterprises run agents in production") appears in `social.linkedin` and `social.bluesky` (both in the file's `frontmatter_keys`). Extract one claim, verify once, render the finding with three cited locations. Don't enumerate per-occurrence claims -- that triples verification work and risks the buckets disagreeing on confidence.

This rule also applies when the body is unchanged but a frontmatter sub-key was edited; the body's pre-existing phrasing still surfaces in the same finding if the frontmatter edit triggered a contradicted verdict.

### Cross-sibling consistency

When a new or changed file lives in a structurally-templated directory (≥3 parallel pages on the same subject), every nav step, heading, required-field name, and placeholder is a *sibling-consistency* claim. Extract each as a `claim_type: cross-reference` record and verify by reading the siblings.

**Pre-step artifact `.cross-sibling-discovery.json`** (workflow pre-step `cross-sibling-discover.py`). For each PR-changed `*.md` under `content/docs/`, the pre-step lists `directory_peers` (in-dir `*.md` files excluding `_index.md`) and sets `in_templated_section: true` when ≥3 peers exist (the threshold mirrors the templated-section criterion below). Per file, the artifact carries `in_templated_section`, `directory_peers`, and `siblings_for_dispatch` (the dispatch base when templated). **Read this artifact first.** Do *not* recompute the templated-section decision inline. The model still applies sibling-set filtering judgment (e.g., distinguish vendor pages from admin/troubleshooting peers in the same directory) before fan-out, but the classification itself is deterministic.

**Pre-step artifact `.frontmatter-validation.json`** (workflow pre-step `frontmatter-validate.py`). Three checks bundled in one content-tree walk + redirect-table scan:

- `menu_parents` — for each `menu.<name>.parent` declared in the file, did the parent identifier resolve in the same named menu? Carries `parent_exists_in_menu` (boolean) and `found_in_other_menus` (list — when the identifier exists in a different menu, the canonical "wrong-menu parent" bug).
- `alias_collisions` — `{alias, collides_with, scope: pr-internal|repo-wide}` records. Built from a global walk of `aliases:` blocks across `content/**/*.md`; cross-references the PR file's *declared* aliases against everything else.
- `url_collisions` — `{file, scope: hugo-alias|s3-redirect}` records keyed off the PR file's *rendered* URL. The pre-step builds a unified URL-ownership map combining Hugo aliases and `scripts/redirects/*.txt` entries (with normalization across `index.html`, `.html`, and trailing-slash conventions). When the PR's URL is already claimed by another file's alias or by an S3 redirect source, it surfaces here. Hugo's own aliases and the move-doc skill's redirect-table maintenance are the canonical signal of "this URL is already taken" — there is no hand-maintained pattern table to keep in sync.

**Read this artifact and surface its findings as 🚨 by default.**
- `parent_exists_in_menu: false` → 🚨 menu-tree-breakage (Hugo will not render the parent linkage; user navigation breaks).
- `alias_collisions` with `scope: repo-wide` → 🚨 redirect-shadowing (Hugo's first-claim-wins semantics silently break one of the two routes).
- `url_collisions` with `scope: hugo-alias` → 🚨 file-location divergence (the PR is dropping content at a URL the existing canonical guide already aliases). The collided file is the canonical sibling — surface it in the cross-sibling reads bullet AND in the 🚨 file-location finding.
- `url_collisions` with `scope: s3-redirect` → 🚨 redirect-table conflict (the PR's URL is in the active S3 redirect table; the redirect either becomes dead or shadows the new content). Cite the redirect-file path and line.

The model still calibrates phrasing and may demote to ⚠️ when context overrides (e.g., the PR is *intentionally* renaming an existing identifier and removing the old declaration in the same diff — rare; cite the diff line in the trail when applied). The structural decision is the artifact's; demotion requires explicit reasoning in the trail entry.

**Pre-step artifact `.hugo-build.json`** (workflow pre-step `hugo-build-validate.py`). Hugo is the canonical authority for routing and build correctness — read this artifact for the build-correctness floor instead of trying to reason about whether the build would succeed. The pre-step renders without `make ensure` (asset prep + data fetch are intentionally skipped), so it strips a known set of CI-environment-only lines before emitting — you never see them, and the count is in `stats.suppressed_ci_noise_count` for operator audit. The artifact carries:

- `errors` — `hugo --renderToMemory` ERROR lines from the PR head, with CI-environment noise already removed. Anything left here is a build-breaking failure (broken `{{< ref >}}` shortcode, template render failure, content with malformed frontmatter that can't load). Surface each entry as 🚨 build-failure with the exact Hugo message in the trail. If an entry still reads as CI-environment-only rather than PR-introduced (a class the filter didn't anticipate — see "Known CI-environment-only error classes" below), demote it silently and note `suppressed: CI-env-only` in the trail with one line of reasoning.
- `link_integrity` — the actionable subset of Hugo WARN/ERROR lines: broken refs, missing assets, unresolvable shortcode targets. This is your starting point for build-level findings — surface each entry as 🚨 unless the target is a page the same PR is adding (PR-internal — false-positive scenario). The full Hugo WARN list (mostly informational, e.g. `WARN found no layout file for ...`) is **not** in this artifact — it's operator-side only (count in `stats.warnings_count`; full lines in the `--verbose` operator artifact); work from `link_integrity` and `errors`.
- `sitemap_diff.added` / `sitemap_diff.removed` — URLs gained/lost in the rendered sitemap between the PR base and head. Removed URLs that aren't replaced by an alias on a remaining page are orphan candidates (existing inbound links and external SEO break). Surface as 🚨 orphaned-target unless the move-doc alias-injection pattern is visible in the diff.
- `head_exit_code` / `head_exit_nonzero_is_ci_noise` — `hugo`'s exit code, plus a flag. A non-zero exit is a build break the agent must surface even if `errors` is empty — *unless* `head_exit_nonzero_is_ci_noise` is `true`, which means the only thing that failed was the stripped CI-environment noise (the `/404` page fingerprints a stylesheet PostCSS never built); treat that as benign.
- `stats` — counts only: `errors_count`, `warnings_count` (the full WARN list is operator-only), `link_integrity_count`, `suppressed_ci_noise_count`, page counts, sitemap-diff counts. The non-zero `suppressed_ci_noise_count` / `warnings_count` are operator-audit signals, not review material.

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

- `L42 "Settings → Access Management" → 🤝 matches entra/gsuite/okta/onelogin (5 of 5 siblings checked; 4 match, 1 has no equivalent step)`
- `L42 "Settings → SAML SSO" → ⚔️ mismatch: scim/{okta,entra,onelogin}.md all use Settings → Access Management; this PR diverges`

**Bucket promotion.** Navigation-step mismatches trigger the workflow-breaking-instruction always-🚨 carve-out — the reader lands on the wrong page. Heading-style, placeholder, or other non-workflow-breaking divergences render as ⚠️, with the divergence noted in the trail.

**Confidence calibration.** The `cross-sibling consistency` dimension is HIGH only when every sibling was read; MEDIUM when most were; LOW when fewer than half were. The parenthetical must report the ratio (e.g., "read 2 of 5").

### Claim extraction examples

The canonical worked-example set — composite/split, implicit comparison, quantitative, negative, the third-party-attribution flip, and the hard run-to-run-disagreement shapes — lives in `docs-review:references:claim-extraction` §Worked examples (12 cases). Don't maintain a parallel copy here; the in-review fallback path reads that file.

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
| `unverifiable` | ⚠️ Low-confidence | "Shape also suggests fabrication; cite a source" (plus the author-question line) |
| `verified` with `confidence: low` | ⚠️ Low-confidence verified | "Shape was suspect; verifier found a low-confidence match" |
| `verified` with `confidence: medium` or `high` | ✅ Verified | No 🤔 note; evidence resolves the shape concern |
| **verification timed out / inconclusive** | 🤔 Intuition-check | "Verifier couldn't resolve; author should cite a source" |

The 🤔 bucket is therefore **small and specific**: claims whose shape was suspect AND whose verification returned neither a confirmation nor a contradiction. The model should not render 🤔 when the verifier produced a decisive answer either way.

### Subagent extraction dispatch

*Fresh-review path only. Re-entrant updates use `docs-review:references:update` -- don't fan specialists across a fix-response / dispute / re-verify pass; the deltas are localized and replication beats decomposition there.*

**When `.candidate-claims.json` provided the floor (the normal CI path — see §Pre-step artifact above), do NOT dispatch the four claim-finder subagents below.** The discovery they did inside the review's context — and the run-to-run variance in *which* claims they found — is exactly what the pre-step lifted out: on claims-heavy content, a single Opus run can miss a real blocking finding another run catches because the in-review discovery is model-judgment under attention pressure. Instead: take the pre-computed `claims` list, **classify** each entry — sort it into the four type-buckets below (`numerical` / `cross-reference` / `capability` / `framing`), set its `source_class` per §Source-class classification, set `cross_specialist_corroboration: true` when the `framing` heuristic also matches the entry's text — then fold in any additional claims you spot in the diff yourself, and run the §Combine step over the union. The four subagents are a **fallback**, run only when the artifact is absent or carries a non-empty `errors` array (degraded pre-step, or interactive `/docs-review`).

When the four subagents *do* run (fallback path): spawn four parallel claim-finder subagents via the Agent tool (`general-purpose`, Sonnet 4.6 each). Each specialist owns a narrow slice of §Claim extraction; the slices are non-overlapping by design except for `framing`, which is a heuristic specialist that scans across canonical types.

- **`numerical`** -- `Numerical` + `Version/availability` rows + §Temporal-claim handling trigger list.
- **`cross-reference`** -- `Cross-reference` row + §Cross-sibling consistency *templated-section detection* and *what to extract* (the per-record list -- not the rendering / promotion / calibration tail). Identifies which siblings need reading; the reads themselves are a separate fan-out (see §Cross-sibling consistency).
- **`capability`** -- `Command behavior`, `Flag/option existence`, `Output format`, `Feature existence`, `Resource API surface` rows.
- **`framing`** -- heuristic specialist; canonical claim-type table unchanged. `Quote/attribution` row + framing-strength phrase list (`the only`, `the first`, `currently`, `as of <year>`, `is the leading`, `industry standard`, named-source quotes). Flags matches regardless of which canonical type the surrounding sentence falls under -- corroborates the others where the slices meet.

Each subagent prompt copies *only* its slice rows verbatim, plus §Skip rules, §Claim record format, and §Source-class classification (each emitted claim must carry a `source_class` value). Do **not** include the full table, other subagents' rows, §Frontmatter sweep, §Intuition-check axis, §Cited-claim spot-check, §Routed verification, or §Claim extraction examples — those belong to other phases or to the main agent. Per-claim cap ~250 words.

**Cross-sibling note.** The four-way claim-finder dispatch retires (above) — but the *sibling-read* fan-out in §Cross-sibling consistency does **not**. That's a different shape of discovery (reading parallel *pages* to compare nav steps / headings / labels), it's fed by its own deterministic pre-step (`.cross-sibling-discovery.json`), and it stays. The `cross-reference` claim-type bucket still exists as a classification bucket for the candidate claims; it just isn't a dispatched finder on the normal path.

**Investigation-log rendering is unchanged.** Render the "External claim verification" bullet's `· N specialists (numerical, cross-reference, capability, framing); K cross-specialist corroborations` segment exactly as `docs-review:references:output-format` specifies (the validator's `external-claim-dispatch-metadata` rule enforces it verbatim). On the normal path the four "specialists" are the four type-buckets you sorted the candidate-claim floor into rather than four dispatched subagents — the *counts* still mean what they always meant (`K` = candidate claims the `framing` heuristic also flagged); the work moved from dispatch to classification, the rendered metadata didn't change.

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

Operates on the **union** of the `.candidate-claims.json` floor (normal path) — or the four subagents' output (fallback path) — and any additional claims the main agent spotted in the diff.

1. **Dedup.** Key = `<file>:<line>` plus the first 40 chars of `claim_text` (lowercased, whitespace collapsed). Merge near-paraphrase matches; pick the most specific framing. *(The candidate-claims floor is already deduped by `merge-claims.py`; this step folds in your in-review additions and re-collapses.)*
1. **Annotate.** Set `found_by: [<specialist>, ...]` from `numerical`, `cross-reference`, `capability`, `framing` (the type-buckets you sorted each claim into; on the fallback path, which subagent found it). When `framing` also matches a claim assigned another type-bucket (e.g., a feature claim with framing-strength language → `[capability, framing]`), set `cross_specialist_corroboration: true` -- a positive signal for the OutSystems-shape catch.
1. **Reconcile `source_class`.** *(Fallback-path only — on the normal CI path the routing is done deterministically by `verify-claims.py`'s `route_claim()`, not by a `source_class` label here.)* Take the most external classification (`external-public` > `ambiguous` > `pulumi-internal`) when in doubt -- routing toward the more thorough lane is the safe default. (Hint: the candidate claim's `source_hint` field — a URL or named source — is a strong `external-public` signal; a `pulumi/*` reference is `pulumi-internal`.)
1. **Frontmatter sweep** runs here -- collapse repeated phrasings across body and the prose-bearing frontmatter keys (`meta_desc`, `description`, `summary`, `title`, every `social.*` sub-key — pinned to `.frontmatter-validation.json`'s `frontmatter_keys`, see §Frontmatter sweep) into a single claim with multiple cited locations. (A candidate claim the LLM holistic pass already collapsed will arrive with multiple line ranges; re-collapse any the regex layer emitted as separate per-line records.)
1. **Hand off.** The floor's claims get their verdicts from `.verified-claims.json` (§Routed verification — read, don't re-verify); any claims you added beyond the floor go to §Routed verification fallback. On a degraded pre-step, the whole deduped list goes to the fallback.

Store the deduped claim list for the verification phase. No interim user output. The 🔍 Verification trail must carry a verdict for **every** entry — the `candidate-claims-coverage` validator rule checks the floor was honored, and `verified-claims-trail-faithful` checks the trail's verdicts match `.verified-claims.json`.

---

## Routed verification

*Fresh-review path only. Re-entrant updates use `docs-review:references:update` -- don't fan specialists across a fix-response / dispute / re-verify pass; the deltas are localized and replication beats decomposition there.*

**The review reads `.verified-claims.json`; it does not produce per-claim verdicts itself.** Workflow pre-step `verify-claims.py` (`.claude/commands/docs-review/scripts/verify-claims.py`) takes every entry in `.candidate-claims.json` (the floor), tries a deterministic pass-0 resolution (no model call — a `:latest` Docker tag → `not-a-claim`, a `static/programs/<dir>/` reference confirmed by a directory check → `verified`), routes the rest — Pass 1 (`pulumi-internal`: `gh` + local reads), Pass 2 (`external` with a fetched URL: consults `.fetched-urls.json`), Pass 3 (`external` with no fetched URL: server-side `web_search`) — fires parallel Sonnet 4.6 verifiers via direct `/v1/messages` with a forced `verify_claim` tool, and emits `.verified-claims.json` at the repo root:

```
{"schema_version": 1, "model": "claude-sonnet-4-6",
 "verdicts": [{"claim_id", "file", "line_range", "text", "type",
               "route": "pass0"|"pass1"|"pass2"|"pass3",
               "verdict": "verified"|"matches"|"not-a-claim"|"unverifiable"|"contradicted"|"mismatch",
               "confidence", "evidence", "source", "framing_note"?, "intuition_flag"?, "model_usage"}],
 "errors": [...], "meta": {"n_claims", "n_pass0", "n_pass1", "n_pass2", "n_pass3", ...}}
```

**This is the claim floor *and* the verdict source on the normal path** — `verdicts[]` carries one entry per candidate claim (it's a superset of `.candidate-claims.json`). Don't also open `.candidate-claims.json` when `.verified-claims.json` is present with a non-empty `verdicts[]` (see §Pre-step artifact `.candidate-claims.json`). **Read `.verified-claims.json` once. Do not re-verify.** For each verdict, render one line in §🔍 Verification trail using the verdict's `evidence` and `source` fields, with the per-verdict emoji from `docs-review:references:output-format` (✅ `verified` · 🤝 `matches` · ➖ `not-a-claim` · 🤷 `unverifiable` · ❌ `contradicted` · ⚔️ `mismatch`). The validator's `verified-claims-trail-faithful` rule fails the review when the trail's verdict word disagrees with the artifact's in the dangerous direction (the trail hiding a `contradicted`/`mismatch`/`unverifiable` the verifier recorded, or inventing a `contradicted`/`mismatch` it didn't find). The review's irreducible work is:

1. **Bucket promotion** — `contradicted`/`mismatch` → 🚨 Outstanding; an `unverifiable` *factual* claim → ⚠️ Low-confidence (file an author-question buffer line — see §Author-question buffer and `docs-review:references:output-format` §Bucket rules); a `verified` claim with low confidence (or medium under heightened scrutiny) → ⚠️ Low-confidence verified; `verified`/`matches`/`not-a-claim` otherwise → trail-only (no bucket). Trail verdict drives bucket placement; don't relitigate `contradicted`/`mismatch`/`unverifiable` via the two-question test (`unverifiable` still bypasses the two-question test — it just lands in ⚠️, not 🚨).
2. **Framing call** — on top of each verdict's `framing_note` (`strengthened`/`narrowed`/`shifted`): mirror it into the rendered bucket bullet.
3. **Intuition check** — on top of each verdict's `intuition_flag`: promote to 🤔 only when the verifier flagged it AND its verdict came back inconclusive (see §Intuition-check axis).
4. **Render the trail and the bucket findings** per `docs-review:references:output-format`. The investigation-log "External claim verification" line's routed-metadata segment maps `.verified-claims.json`'s `meta` directly: `routed: <meta.n_pass0> inline, <meta.n_pass1> Pass 1, <meta.n_pass2> Pass 2, <meta.n_pass3> Pass 3` — `n_pass0` is verify-claims.py's pass-0 lane (claims resolved deterministically with no model verifier dispatched, e.g. a `:latest` Docker tag demoted to `not-a-claim`, a `static/programs/<dir>/` reference confirmed by a directory check); those map to the `inline` counter. Add your in-review additions' routes (a claim you resolved without dispatching a verifier counts as `inline`). The per-lane `(verified V, contradicted C, unverifiable U)` parentheticals count the `pass2`- and `pass3`-routed verdicts by `verdict`; the leading `(N unverifiable, M contradicted)` parenthetical aggregates all verdicts.

**Claims you added beyond the floor** (claims the artifact missed — see §Combine step) have no verdict in `.verified-claims.json`; verify them in-review using the §Routed verification fallback below, fold their routes into the routed-metadata counts, and render their trail lines the same way.

**Degraded pre-step.** If `.verified-claims.json` is absent (interactive `/docs-review`, or the workflow's verify-claims step crashed), or carries a non-empty top-level `errors` array, or a particular verdict carries an error (the verifier crashed on that one claim), fall back to the §Routed verification fallback below for the affected claims — note "verify-claims pre-step degraded; in-review verification ran" in the trail. Cross-sibling-consistency checks (`matches` / `mismatch` against sibling pages) always run in-review via the sibling-read fan-out (§Cross-sibling consistency) — `verify-claims.py` does not do sibling comparison.

### Routed verification fallback (degraded / interactive path; also for claims added beyond the floor)

This path runs when `.verified-claims.json` is absent or degraded, on interactive `/docs-review`, and for any claims the review added that aren't in the floor. Each claim's `source_class` (set at extraction; see §Source-class classification) routes it to one of four lanes — the same routing `verify-claims.py` does deterministically, run by the model here:

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

Framing labels (only `exact-match` lands ✅ `verified`; the rest land ❌ `contradicted` — a 🚨-bucket verdict under the contradicted-factual-claim carve-out):

- `exact-match` — source phrasing is the claim's phrasing, or a literal paraphrase of equal scope.
- `strengthened` — claim is a subset of the source. Source: "use"; claim: "use in production."
- `narrowed` — claim is broader than the source. Source: "U.S. enterprise"; claim: "enterprise."
- `shifted` — same numeric anchor, different subject. Source: "evaluate AI agents"; claim: "deploy AI agents."
- `contradicted` — source positively disagrees with the claim.

Example (strengthened framing):

```
- L40 "96% of enterprises run AI agents in production today" → ❌ contradicted (source mismatch)
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

Calibration example: "`pulumi up` accepts a `--stack` flag" verified by `gh api .../pulumi-language-go/main.go` showing the flag registered → **high** (direct source match). A README that *mentions* a provider but no worked example → **medium**. "Most users deploy on AWS" backed only by blog-post collocation → **low**.

### Subagent prompts

Subagent prompts must be self-contained — copy the rules into the prompt rather than referencing them. Per-lane requirements are spelled out in §Routed verification (Pass 1: §Verification source order steps 1-3 + §Claim record format; Pass 2: §Verification source order step 4 + the framing taxonomy + the §Mandatory evidence-line format). The inline lane runs on the main agent and needs no subagent prompt. Per-claim cap of ~250 words across both subagent lanes.

---

## Tiered triage

Build a structured triage object.

### Tier rules

Tier emoji conventions: 🚨 (Outstanding) and ⚠️ (Low-confidence) align with the canonical buckets in `docs-review:references:output-format`. ✅ Verified here is fact-check's own collapsed-details bucket — distinct from the canonical ✅ Resolved-since-last-review used elsewhere; do not conflate them. 🤔 Intuition-check has no canonical counterpart.

| Tier | Contents |
|---|---|
| 🚨 Needs your eyes | All `contradicted` claims (any confidence) |
| 🤔 Intuition-check | Claims whose `intuition_check` flag was set AND whose verification came back inconclusive (timed out, could not reach a verdict). Cross-reference the shape concern in the evidence line. |
| ⚠️ Low-confidence | `verified` claims with `confidence: low` (and `medium` when scrutiny is heightened) — prefix the evidence line with "verified weakly" to distinguish from generic low-confidence findings; plus all `unverifiable` claims (the verifier couldn't confirm them) — each also gets an author-question line. |
| ✅ Verified | Everything else, collapsed under `<details>` |

When a claim is flagged `intuition_check: true` AND the verifier reaches a decisive verdict, it renders in the verdict's bucket (🚨 / ⚠️ / ✅), not 🤔 -- see the rendering rule table in §Intuition-check axis. 🤔 is for inconclusive verification only.

### Credential redaction

The evidence line of any finding is rendered into the public pinned comment. **Never quote raw credential strings in evidence** -- file:line and a short description only. If the claim's context contains what looks like an API key, token, password, private URL, or connection string, replace the token with `[REDACTED]` in the evidence line and flag the underlying leak as a separate 🚨 finding (per `docs-review:references:infra` §Secret handling). Public-PR diffs are already exposed; the pinned comment must not amplify the leak by quoting the raw value.

Patterns that trigger redaction on sight:

- Strings matching common token formats (`ghp_*`, `sk-*`, `AKIA*`, `pul-*`, `xoxb-*`, JWT-like `eyJ*`).
- Hostnames ending in `.internal`, `.priv`, or any hostname paired with an obvious secret (`https://user:pass@...`).
- Strings with ≥32 contiguous alphanumeric characters that don't match a known non-secret format (UUIDs are OK; opaque blobs are not).

`compose-review.py` runs this same pattern set as a deterministic backstop over every verdict's `text` / `evidence` / `source` before rendering them into `.review-draft.md` — a structural fact ("this string matches a token format") is exactly the kind of thing a pre-step does. That's belt-and-suspenders; the verifier should still redact at the source, and the reviewer must still flag the underlying leak as a separate 🚨 finding per `docs-review:references:infra` §Secret handling (the composer redacts the *quote*, not the *finding*).

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
