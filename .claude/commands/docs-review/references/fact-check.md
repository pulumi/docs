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

Store the full claim list for the verification phase. No interim user output.

---

## Parallel verification

Spawn parallel subagents using the Agent tool (`general-purpose` type), batched **up to 4 at a time** to avoid context overload. Each subagent receives a small group of related claims (group by file or by claim type, whichever is smaller).

If more than 20 claims are extracted, batch by file rather than per-claim to keep the subagent count manageable.

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

Used for *non-Pulumi* upstream sources where `gh` doesn't apply: AWS/Azure/GCP provider docs, upstream tool docs (Kubernetes, Terraform), third-party announcements. **Skip in favor of `gh` whenever the claim is about Pulumi itself.**

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

The verification step must produce a three-field evidence line, not a one-field summary:

```
- L<line> "<claim text>" → <verdict emoji> <verdict>
  - source quote: "<verbatim passage from the fetched page>"
  - framing: <exact-match | strengthened | narrowed | shifted | contradicted>
```

`(same OutSystems report)` / `(citation linked inline)` / `(URL resolves)` are NOT acceptable evidence for a cited claim — they record that fetching happened, not that comparison happened. **The verbatim source quote is the proof that the comparison was done.** A verdict without a source quote is a verdict without evidence; downgrade to `unverifiable`.

##### Worked example — strengthened framing

This is the case S30 missed across three runs on PR #130.

- **Claim** (PR #130 L40): *"96% of enterprises run AI agents in production today."*
- **Source** (`outsystems.com/news/enterprise-ai-agent-report-2026/`): page title is *"96% of Organizations Use AI Agents"*; meta description reads *"96% of enterprises now use AI agents."*
- **Comparison:** the percentage matches; the framing does not. The source's *"use"* / *"now use"* covers pilots, experiments, and internal trials. The PR's *"run in production today"* claims revenue-producing deployment. The claim narrows the source.
- **Verdict:** 🚨 contradicted — strengthened framing.

Correct evidence line:

```
- L40 "96% of enterprises run AI agents in production today" → 🚨 contradicted (source mismatch)
  - source quote: "96% of enterprises now use AI agents"
  - framing: strengthened — claim narrows source's "use" to "in production today"
```

The framing labels are deliberate: each one names a *specific* drift pattern.

- **exact-match** — source phrasing is the claim's phrasing or a literal paraphrase of equal scope.
- **strengthened** — claim is a subset of the source (source: "use"; claim: "use in production"). PR overstates the source.
- **narrowed** — claim is broader than the source (source: "U.S. enterprise customers"; claim: "enterprise customers"). PR overstates the population.
- **shifted** — same numeric anchor, different subject (source: "96% of organizations evaluate AI agents"; claim: "96% of organizations deploy AI agents"). The PR cited the right report for the wrong number.
- **contradicted** — source positively disagrees with the claim. Stronger than the above three; reserved for *negation*, not framing drift.

The first four (`strengthened`, `narrowed`, `shifted`, `contradicted`) all land in 🚨 Outstanding under the always-🚨 carve-out for contradicted-factual-claim. `exact-match` lands in ✅ Verified at high confidence.

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

Subagent prompts must be self-contained — copy the rules into the prompt rather than referencing them. Include the §Verification source order rules, the §Claim record format expected output schema, and a per-claim cap of ~250 words.

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
