---
user-invocable: false
description: Factual claim verification — extract claims from changed content, verify in parallel against ground truth, and produce a tiered triage report
---

# Factual Claim Verification

This procedure catches *wrong information* in documentation: incorrect command output, hallucinated CLI flags, features described as existing when they don't, version claims, miscited APIs. It is the rigor enforcement that style checks alone cannot provide.

It is a shared primitive: the CI review pipeline invokes it via its domain files (when the PR carries the `fact-check:needed` label), and the interactive `/pr-review` skill invokes it as Step 5. It is also designed to be run standalone -- anywhere a set of changed content files needs to be verified for factual accuracy.

The procedure has six phases. They are listed in order, but the section names are descriptive rather than numbered so this reference can be reused outside of any specific calling workflow.

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
- **Per-claim evidence trail** -- the raw `{status, confidence, evidence, source, suggested_fix}` tuples, retained for re-entrant re-verification

### Minimum-viable caller (pseudocode)

```bash
# 1. Assemble the call
FILES=$(gh pr view "$PR" --json files -q '.files[].path')
SCRUTINY="heightened"  # domain files decide this; hardcoded here for illustration

# 2. Gate (see Gating section — optional for non-pr-review callers)
#    CI callers skip this and rely on the `fact-check:needed` label applied by triage.

# 3. Extract claims (see Claim extraction section)

# 4. Dispatch parallel verification subagents (see Parallel verification)

# 5. Collate into the tiered triage object

# 6. Hand the object to the caller for rendering
```

The skill is callable as a pure function of `(files, scrutiny)` → `(triage_object, author_questions, evidence_trail)`. Callers wire the output into their own review composition; fact-check does not render directly into a comment.

### Note on AI-suspect

AI-suspect detection (see [`pr-review:references:trust-and-scrutiny`](../pr-review/references/trust-and-scrutiny.md)) is a pr-review-skill concept. When that skill decides a PR is AI-suspect, it passes `scrutiny=heightened` to this file. The CI pipeline does not use the AI-suspect flag; CI callers pass `scrutiny` directly from the domain file's default (e.g., `review-blog.md` always passes `heightened`).

---

## Gating

Decide whether to run at all. This phase is relevant for pr-review-skill callers (which use the gate script below) and for standalone use; the CI pipeline gates via the `fact-check:needed` label applied by triage and does **not** invoke the gate script.

For pr-review and standalone callers:

```bash
bash .claude/commands/pr-review/scripts/should-fact-check.sh \
  <PR_NUMBER> "<CONTRIBUTOR_TYPE>" "<AI_SUSPECT>" "<RISK_TIER>"
```

Parse `FACT_CHECK=run|skip` from output. If `skip`, store `FACT_CHECK_REASON` for the calling workflow's report and exit. If `run`, continue to claim extraction.

The gate logic:

- `AI_SUSPECT=true` → always RUN (AI hallucinations show up everywhere, including non-content paths)
- `RISK_TIER=typo` → SKIP (nothing factual to check on a 5-line typo fix)
- bot/dependabot → SKIP unless content paths are touched
- any `content/{docs,blog,tutorials,learn,what-is}/` path in the diff → RUN

For CI callers: the gate lives upstream, in triage (`claude-triage.yml`). The domain file invokes fact-check only when the `fact-check:needed` label is present on the PR.

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
| Cross-reference | "see the X guide" -- the guide must exist |
| Numerical | pricing, limits, sizes |
| Quote/attribution | direct quotes, named sources |

**Skip** prose that is:

- Stylistic or opinion ("this approach is cleaner")
- Self-evidently context-only ("In this guide, we'll walk through...")
- Already cited and linked

### Scope

- Default (`scrutiny=standard`): extract claims from the diff only -- lines added or modified
- `scrutiny=heightened`: extract claims from the **full file**, not just the diff. AI hallucinates surrounding prose, not just changed lines.

### Claim extraction examples

Worked examples of correct extraction from real prose patterns. Each shows the paragraph, the extracted claims, and the reasoning.

**Example 1 -- simple single claim**

> "Pulumi ESC was released in 2024."

- Claim: "Pulumi ESC was released in 2024." (type: `version/availability`)
- Reasoning: one assertion about a single product-release fact.

**Example 2 -- composite claim**

> "Pulumi ESC supports AWS, Azure, and Vault."

- Claim 1: "Pulumi ESC supports AWS." (type: `feature existence`)
- Claim 2: "Pulumi ESC supports Azure." (type: `feature existence`)
- Claim 3: "Pulumi ESC supports Vault." (type: `feature existence`)
- Reasoning: each listed integration is separately verifiable. Combining them hides which one is wrong when only one is.

**Example 3 -- implicit comparison**

> "Unlike Terraform, Pulumi uses real programming languages."

- Claim 1: "Pulumi uses real programming languages." (type: `feature existence`)
- Claim 2 (implicit): "Terraform does not use real programming languages." (type: `feature existence`)
- Reasoning: "unlike X" asserts a property of X. Extract the implicit claim so it can be verified independently.

**Example 4 -- quantitative**

> "chardet is 41x faster at encoding detection than its predecessor."

- Claim: "chardet is 41x faster at encoding detection than its predecessor." (type: `numerical` / `benchmark`)
- Reasoning: any specific multiplier needs a source. The 🤔 intuition-check may also fire -- "41x" is unrounded and suspiciously specific.

**Example 5 -- temporal**

> "Recently, Pulumi added support for OpenTofu."

- Claim: "Pulumi added support for OpenTofu." (type: `feature existence`)
- Temporal flag: "recently" -- triggers the Temporal-claim handling rule below. Verify *and* record the date anchor.

**Example 6 -- negative**

> "Pulumi doesn't support ARM templates."

- Claim: "Pulumi doesn't support ARM templates." (type: `feature existence`, negative)
- Reasoning: harder to verify (proving a negative) -- requires reading the provider registry and confirming no matching package exists. Annotate as `verification_difficulty: high` so the subagent knows it may need extra evidence.

**Example 7 -- CLI with output**

> "Run `pulumi up` and you'll see `Performing changes:` in the output."

- Claim 1: "`pulumi up` is a valid CLI command." (type: `command behavior`)
- Claim 2: "`pulumi up` prints `Performing changes:`." (type: `output format`)
- Reasoning: the output claim is separately wrong-able from the command claim. (The current CLI prints `Updating (dev)`, not `Performing changes:` -- Claim 2 would be contradicted.)

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

The date anchor captures "verified true at this point in time." The caller may flag the claim for re-verification after N months (default: 6), since a "new in 2026" claim will read awkwardly in 2028.

When a temporal trigger word is **not warranted** -- e.g., "recently" describing a change from years ago -- flag as `contradicted: temporal misuse` with the suggested fix ("replace 'recently' with the actual timeframe, or drop the temporal qualifier").

### Intuition-check axis

Separate from verified/unverifiable: sometimes the *shape* of a claim is suspect even when evidence is absent or ambiguous. Flag these under 🤔 (distinct from ⚠️ unverifiable).

Shape-based flags:

- **Unrounded specific numbers.** "41x faster." "2,347 customers." "Reduced latency by 37.4%." Humans round; AI hallucinates precision. Unless the source is an authoritative benchmark, flag.
- **AI-pattern phrasing.** "Blazing-fast." "Seamlessly integrates." "World-class." "Battle-tested." "Revolutionary." Claims that *read like* marketing boilerplate usually don't hold up under source checking.
- **Specific but unsearchable.** "Used by 73% of Fortune 500 companies." "Deployed in over 40 countries." Specific, quotable, and -- often -- traceable to no source that anyone can find.

A 🤔 finding is NOT "this is probably wrong." It is "the shape of this claim suggests fabrication; author should cite a source regardless of what the verifier finds." If the author provides a source, the finding resolves. If not, it stays visible.

Distinction from other tiers:

- 🚨 Contradicted: evidence says the claim is wrong.
- 🚨 Unverifiable: no source found, but claim shape is plausible.
- 🤔 Intuition-check: claim shape is suspect independent of evidence.
- ⚠️ Low-confidence verified: evidence is partial / indirect.
- ✅ Verified: evidence matches claim.

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

#### 5. Notion + Slack (best-effort; pr-review / interactive use only)

Only if MCP tools are present in the runtime tool set. Use these to catch internal context that hasn't made it into a repo yet -- "we decided not to ship this," "this was renamed," "the CEO sketched this in a doc but it's not built."

```
mcp__claude_ai_Notion__notion-search
mcp__claude_ai_Slack__slack_search_public_and_private
```

Default search window: last 6 months. Absence of these tools must not fail the workflow -- annotate the evidence as "internal sources unavailable."

**CI fact-check never uses Notion or Slack.** The CI runner's tool set excludes these by design: fact-check output lands in a public PR comment, and internal sources create prompt-injection and leakage risks. See `docs-review-ci.md` §Hard rules.

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

### Subagent prompt template

Each subagent prompt is **self-contained** (the subagent has no access to the parent conversation):

```
You are verifying factual claims extracted from a Pulumi documentation change.

For each claim below, decide whether it is verified, unverifiable, or contradicted,
and return structured results.

Verification toolbox (use cheapest source first):
1. Local repo: Read/Grep within the working directory
2. gh CLI: prefer this over WebFetch for any Pulumi-related claim. Common patterns:
   - gh search code --owner pulumi "<term>"
   - gh api repos/pulumi/<repo>/contents/<path>
   - gh release view <tag> -R pulumi/pulumi
3. Live execution: pulumi --help, pulumi <cmd> --help, npm/go/python read-only.
   Require user confirmation before state-changing cloud operations.
4. WebFetch/WebSearch: only for non-Pulumi upstream sources (AWS, k8s, etc.)
5. Notion/Slack MCP: only if tools are present; best-effort. Never in CI.

Claims to verify:
{claim list with file/line/text/type/surrounding-paragraph}

For each claim, return JSON:
{
  "id": <claim id>,
  "status": "verified" | "unverifiable" | "contradicted",
  "confidence": "high" | "medium" | "low",
  "evidence": "<short quote, path:line, gh url, or command output>",
  "source": "repo" | "gh" | "exec" | "web" | "notion" | "slack",
  "suggested_fix": "<only if contradicted — concrete replacement text>"
}

Cap your full response under 250 words per claim group.
```

---

## Tiered triage

Build a structured triage object that the caller will render. The format:

```markdown
## 🔬 Fact-Check Results (14 claims, 3 files)

### 🚨 Needs your eyes (2)
- `content/docs/cli/logout.md:42` — **Contradicted**
  Claim: "pulumi logout removes credentials for all backends"
  Evidence: pulumi logout --help shows it only affects the current backend (exec)
  Suggested fix: "removes credentials for the current backend"

- `content/blog/esc-rotation.md:88` — **Unverifiable**
  Claim: "ESC supports automatic rotation for Vault secrets"
  Searched: registry docs, Notion (no decision found), Slack #esc (no mention)
  Action: ask author for source

### 🤔 Intuition-check (1)
- `content/blog/perf.md:14` — **Suspicious shape**
  Claim: "chardet is 41x faster at encoding detection"
  Reason: unrounded specific multiplier; author should cite a source regardless of verifier result

### ⚠️ Low-confidence verified (3)
- `content/docs/foo.md:12` — claim — source
  ...

<details>
### ✅ Verified (8)
- `content/docs/foo.md:18` — claim — source
- ...
</details>
```

### Tier rules

| Tier | Contents |
|---|---|
| 🚨 Needs your eyes | All `contradicted` claims (any confidence) + all `unverifiable` claims |
| 🤔 Intuition-check | Claims flagged by the intuition-check axis, regardless of verification result |
| ⚠️ Low-confidence verified | `verified` claims with `confidence: low` (and `medium` when scrutiny is heightened) |
| ✅ Verified | Everything else, collapsed under `<details>` |

A single claim can appear in both 🤔 (shape) and 🚨 / ✅ (evidence). When it does, render in 🚨 (the more actionable bucket) and cross-reference the shape concern in the evidence line.

### Why tiered

- **Top of view = only actionable items.** These are the only findings that gate approval.
- Verified claims are listed but visually subordinated so the audit trail exists without cognitive load.
- Each contradicted claim ships with a concrete suggested fix → caller can immediately apply the fix without re-reading the file.
- Counts in headers give a fast "is this 2 issues or 14?" gut check.

---

## Author-question buffer

For every `unverifiable` claim, add an entry to an author-question buffer:

```
- content/blog/esc-rotation.md:88 — Source for "ESC supports automatic rotation for Vault secrets"?
```

For every 🤔 intuition-check finding, add:

```
- content/blog/perf.md:14 — Cite a source for "chardet is 41x faster at encoding detection"?
```

The buffer is consumed by the calling workflow. In `/pr-review`, when the user picks **Request changes**, the buffer auto-populates the comment body with line-anchored questions per claim. Standalone callers can use it however they like -- print it, save it, ignore it.

---

## Assessment rules

The caller's overall assessment and confidence gauge use these rules:

| Finding | Effect on assessment |
|---|---|
| Any `contradicted` with `confidence: high` affecting code/CLI | Critical issues |
| Any other `contradicted` with `confidence: high` | Issues found |
| Only `unverifiable` claims | Minor issues + recommend asking author |
| Only 🤔 intuition-check findings | Minor issues + recommend asking author for sources |
| All verified | No impact |

| Finding | Effect on confidence gauge |
|---|---|
| Any high-confidence contradicted | Cap at LOW |
| Any unverifiable | Cap at MEDIUM |
| Any 🤔 intuition-check | Cap at MEDIUM |
| Heightened scrutiny | Cap at MEDIUM (always) |

When called from a PR review, preserve the PR-introduced vs. pre-existing distinction throughout: a contradiction in unchanged prose is pre-existing (surfaced but doesn't gate approval); a contradiction in the diff is PR-introduced and blocking.

---

## Heightened-scrutiny overrides

When the caller passes `scrutiny=heightened` (e.g., AI-suspect is set in `/pr-review`, or `review-blog.md` / `review-programs.md` sets it by default):

- Claim extraction runs over the **full file**, not just diff context
- Gating always returns RUN
- Web/`gh` verification runs by default on every claim
- Medium-confidence verified claims get promoted from collapsed `✅ Verified` to visible `⚠️ Low-confidence verified`
- The caller's confidence gauge prepends `🤖 AI-suspect` (pr-review only) and caps at MEDIUM
- Auto-trivial fixers should be disabled by the caller (the AI may have introduced subtly wrong "fixes" that look like typos but aren't)
- Pre-existing issue extraction runs per the rules below

### Pre-existing issue extraction

When `scrutiny=heightened`, the verifier reads the **full file** for claim extraction. Any substantive issue the verifier notices in unchanged prose renders in the 💡 Pre-existing bucket (owned by the caller's output format; see [`docs-review-core.md`](docs-review-core.md)):

- **Do extract:** broken links, wrong facts, code typos (missing imports, wrong method names), deprecated terminology, temporally-rotted claims.
- **Do NOT extract style nits** unless the domain file says to: heading case, list numbering, em-dash frequency, paragraph rhythm, trailing whitespace. Those are either linter territory or out of scope for fact-check.
- **Cap:** 15 findings per file. If the file has more substantive issues than that, the top 15 render; surplus is noted as "+N additional pre-existing findings" in the bucket.
- **Bucket:** substantive pre-existing findings render in 💡 alongside domain-file style nits (when the domain says to extract them). The domain file controls what counts as which; fact-check just surfaces what it finds.

For non-fact-check pre-existing extraction (style, structure), see the per-domain file's "Pre-existing issues" section.
