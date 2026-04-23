---
user-invocable: false
description: Factual claim verification — extract claims from changed content, verify in parallel against ground truth, and produce a tiered triage report
---

# Factual Claim Verification

This procedure catches *wrong information* in documentation: incorrect command output, hallucinated CLI flags, features described as existing when they don't, version claims, miscited APIs. It is the rigor enforcement that style checks alone cannot provide.

It is a shared primitive: the CI review pipeline invokes it via its domain files (when the PR carries the `fact-check:needed` label), and the interactive `/pr-review` skill invokes it as Step 5. It is also designed to be run standalone — anywhere a set of changed content files needs to be verified for factual accuracy.

The procedure has six phases. They are listed in order, but the section names are descriptive rather than numbered so this reference can be reused outside of any specific calling workflow.

---

## Inputs

The caller must provide:

- A list of changed content file paths (typically `.md` files under `content/`)
- A scrutiny level: `standard` or `heightened`
- A target output: where the tiered triage object will be rendered

When called from `/pr-review`, the scrutiny level comes from `CONTENT_SCRUTINY` (which is `heightened` whenever `AI_SUSPECT=true`). When called standalone, the caller decides.

See `pr-review:references:trust-and-scrutiny` for the trust model and how AI-suspect changes behavior.

---

## Gating

Decide whether to run at all. This phase is most relevant when called from a PR-review workflow; standalone callers may skip it.

Run `should-fact-check.sh` with the contributor type, AI-suspect flag, and risk tier:

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
| Cross-reference | "see the X guide" — the guide must exist |
| Numerical | pricing, limits, sizes |
| Quote/attribution | direct quotes, named sources |

**Skip** prose that is:

- Stylistic or opinion ("this approach is cleaner")
- Self-evidently context-only ("In this guide, we'll walk through...")
- Already cited and linked

### Scope

- Default (`scrutiny=standard`): extract claims from the diff only — lines added or modified
- `scrutiny=heightened`: extract claims from the **full file**, not just the diff. AI hallucinates surrounding prose, not just changed lines.

### Claim record format

```json
{
  "id": "c1",
  "file": "content/docs/cli/logout.md",
  "line": 42,
  "claim_text": "pulumi logout removes credentials for all backends",
  "claim_type": "command-behavior",
  "verification_method": "exec"
}
```

Store the full claim list for the verification phase. No interim user output.

---

## Parallel verification

Spawn parallel subagents using the Agent tool (`general-purpose` type), batched **up to 4 at a time** to avoid context overload. Each subagent receives a small group of related claims (group by file or by claim type, whichever is smaller).

If more than 20 claims are extracted, batch by file rather than per-claim to keep the subagent count manageable.

### Verification source order (cheapest first)

#### 1. Local repo / linked docs

Grep/Read other content files; follow internal links to verify the target exists and matches the claim; read referenced `/static/programs/` files. **Cheapest source — always try first.**

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

`gh` results count as `confidence: high` when they directly match the claim, because they read source-of-truth from the actual repo. **Subagents should prefer `gh` over WebFetch whenever the claim is about anything `pulumi/*` ships.**

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

Only if MCP tools are present in the runtime tool set. Use these to catch internal context that hasn't made it into a repo yet — "we decided not to ship this," "this was renamed," "the CEO sketched this in a doc but it's not built."

```
mcp__claude_ai_Notion__notion-search
mcp__claude_ai_Slack__slack_search_public_and_private
```

Default search window: last 6 months. Absence of these tools must not fail the workflow — annotate the evidence as "internal sources unavailable."

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
5. Notion/Slack MCP: only if tools are present; best-effort.

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

### ⚠️ Low-confidence verified (3)
- `content/docs/foo.md:12` — claim — source
  ...

<details>
### ✅ Verified (9)
- `content/docs/foo.md:18` — claim — source
- ...
</details>
```

### Tier rules

| Tier | Contents |
|---|---|
| 🚨 Needs your eyes | All `contradicted` claims (any confidence) + all `unverifiable` claims |
| ⚠️ Low-confidence verified | `verified` claims with `confidence: low` (and `medium` when scrutiny is heightened) |
| ✅ Verified | Everything else, collapsed under `<details>` |

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

The buffer is consumed by the calling workflow. In `/pr-review`, when the user picks **Request changes**, the buffer auto-populates the comment body with line-anchored questions per claim. Standalone callers can use it however they like — print it, save it, ignore it.

---

## Assessment rules

The caller's overall assessment and confidence gauge use these rules:

| Finding | Effect on assessment |
|---|---|
| Any `contradicted` with `confidence: high` affecting code/CLI | Critical issues |
| Any other `contradicted` with `confidence: high` | Issues found |
| Only `unverifiable` claims | Minor issues + recommend asking author |
| All verified | No impact |

| Finding | Effect on confidence gauge |
|---|---|
| Any high-confidence contradicted | Cap at LOW |
| Any unverifiable | Cap at MEDIUM |
| Heightened scrutiny | Cap at MEDIUM (always) |

When called from a PR review, preserve the PR-introduced vs. pre-existing distinction throughout: a contradiction in unchanged prose is pre-existing (surfaced but doesn't gate approval); a contradiction in the diff is PR-introduced and blocking.

---

## Heightened-scrutiny overrides

When the caller passes `scrutiny=heightened` (e.g., AI-suspect is set in `/pr-review`):

- Claim extraction runs over the **full file**, not just diff context
- Gating always returns RUN
- Web/`gh` verification runs by default on every claim
- Medium-confidence verified claims get promoted from collapsed `✅ Verified` to visible `⚠️ Low-confidence verified`
- The caller's confidence gauge prepends `🤖 AI-suspect` and caps at MEDIUM
- Auto-trivial fixers should be disabled by the caller (the AI may have introduced subtly wrong "fixes" that look like typos but aren't)
