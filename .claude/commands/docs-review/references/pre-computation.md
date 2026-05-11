# Pre-computation reference

Architectural pattern for atomizing deterministic checks into workflow pre-step artifacts the reviewer agent reads. Codifies the principle that emerged across S38 (Ship G + Ship H): structural facts go to scripts, editorial judgment stays with the agent.

## Principle

**Scripts find structural facts. The agent makes editorial judgments.**

Determinism (single right answer, no context needed): pre-step. Probabilistic judgment (relevance, severity, framing accuracy, voice, prose-vs-prose comparison): agent. Mixed cases: pre-step computes the fact, the agent applies severity / suppression / consolidation.

The agent is **not** a parrot for script output. Each artifact entry is an input to a decision, not the decision itself. The agent reads the artifact, applies context (PR scope, author trust, surrounding diff, intent signals), and decides whether each finding surfaces, at what severity, consolidated with which other findings, and in what voice.

## Why atomize

S37 → S38 evidence: the model **skips deterministic checks under attention pressure**. Cross-sibling-reads classification was inconsistent across runs (1 of 4 captures caught the structural triplet on pr18568). Encoding the same logic as a deterministic pre-step (Ship G) produced reliable discovery at 47% lower cost and freed the agent's attention budget for the judgment work that actually needs it. The reviewer's value increased — sharper findings, better phrasing — because we removed the rote lookup work crowding it out.

## Bundle architecture

Pre-steps cluster by **what they read**. Bundle by reading pattern, not by topic, to amortize file IO + parse cost.

| Bundle | Script | Artifact | Reads |
|---|---|---|---|
| URL fetch | `extract-urls-and-fetch.py` | `.fetched-urls.json` | PR diff + external URL fetches |
| Editorial balance (Tier 1) | `editorial-balance-detect.py` | `.editorial-balance.json` | `content/blog/**/*.md` body |
| Vale lint | `vale-findings-filter.py` | `.vale-findings.json` | All changed `*.md` |
| Cross-sibling discovery (Ship F/G) | `cross-sibling-discover.py` | `.cross-sibling-discovery.json` | `content/docs/**/*.md` directory tree |
| Frontmatter validation (Ship H) | `frontmatter-validate.py` | `.frontmatter-validation.json` | All `content/**/*.md` frontmatter + redirect tables |
| Hugo build (Ship K, S39) | `hugo-build-validate.py` | `.hugo-build.json` | `hugo --renderToMemory` at HEAD + `hugo list all` at HEAD and BASE |

The originally-queued `docs-reference-graph` bundle is subsumed by Ship K: Hugo's render emits broken-link / broken-shortcode / missing-asset warnings as part of the build, and the sitemap-diff covers added/removed-page detection. Resurrect a separate reference-graph script only if a specific bug class slips through Hugo's checks.

**Next candidates** (priority order, no committed timeline — see `s39-runs/notes/script-candidates.md` in the rebenchmark scratch dir):

1. `markdown-link-validate.py` — flags dangling plain markdown-style internal links (`[x](/docs/...)`) that Hugo silently accepts; closes the one residual gap Ship K's build floor doesn't cover.
1. `image-validate.py` — file size, format-vs-extension mismatch, 1px-gray-border check, placeholder `meta_image` SHA detection, generic alt-text strings.
1. Editorial-balance Tier 2 extension — compute entity-mention counts + recommendation-steering counts deterministically (the patterns are already enumerated as regex in the blog criteria).

These were tracked as "Queued" bundles (`markdown-body-scan.py`, `pulumi-lookups.py`) in earlier sessions; S39's audit reprioritized — `markdown-link-validate.py` is the higher-value next step than a general markdown-mechanics scan.

Each pre-step is independent. Each writes a self-contained artifact. The reviewer agent reads what's relevant to its current task.

## False-positive triage is a contractual responsibility

Scripts WILL produce false positives. Examples already observed or anticipated:

- `placeholder-scan` finds `TODO` in a code block that's an intentional placeholder for the reader.
- `image-asset-check` flags decorative images that legitimately don't need alt text.
- `internal-link-existence` flags links to pages the *same PR* is adding (target doesn't exist YET).
- `menu-parent-validate` flags a parent identifier the PR is *creating* in the same diff.
- `alias-collision` flags a deliberate rename (PR removes the old declaration, adds the new — net change is alias migration, not collision).
- `acronym-detect` flags `import re` and `cd /tmp` in code blocks.

The reviewer's contract: **for each artifact entry, decide whether it's real, important, and worth surfacing**. Triage is not optional. If the agent passes script output through unfiltered, the system has moved overhead from the model to the reader, not eliminated it.

Each pre-step's spec (in `references/fact-check.md` or domain-specific docs) must list known false-positive scenarios so the agent knows when to suppress. Demotion or suppression must be traced in the verification trail with explicit reasoning ("L11 menu-parent collision suppressed: PR-internal — the parent is being added at L42 of `data/docs_menu_sections.yml` in the same diff").

## What does NOT belong in a pre-step

- "Is this paragraph well-written?" — judgment.
- "Does this claim accurately represent its source?" — prose-vs-prose comparison.
- "Is this finding important enough to surface as 🚨?" — context-dependent severity.
- "Does this read as marketing voice or docs voice?" — judgment.
- "Should these N similar findings consolidate into one?" — judgment.
- "Is this acronym defined elsewhere in the repo?" — Vale handles this with appropriate context awareness; don't reinvent linting.
- "Does this finding LOOK structurally wrong but is intentional?" — context-dependent.

Anything that requires reading two prose passages and judging their relationship: agent. Anything that needs to know "is this PR sloppy or careful overall": agent. Anything where the right answer depends on PR scope, author trust, or surrounding diff intent: agent.

## How to add a new pre-step

1. **Confirm atomization criteria.** The check must have a single right answer that doesn't require context, AND be observed (or anticipated) to get skipped under attention pressure. If both don't hold, leave it model-driven or give it to Vale.
2. **Pick the bundle.** Match by reading pattern (frontmatter? body? reference graph? batched API lookups?). Don't fork a new script if an existing bundle reads the same input.
3. **Write the script.** Mirror the shape of `cross-sibling-discover.py` or `frontmatter-validate.py`. Single-purpose, deterministic, fast (sub-3-second on full repo walk), no LLM calls.
4. **Wire the workflow YAML.** Add a step in `.github/workflows/claude-code-review.yml` after the existing pre-steps, with `continue-on-error: true` and a stub-fallback `||` clause that writes an empty artifact.
5. **Update the spec.** Add a "Pre-step artifact `<name>.json`" paragraph in the relevant `references/*.md` section. Spec what the artifact contains, mandate "read this first," surface the structural floor, and call out known false-positive scenarios.
6. **Optionally add a validator rule.** If the artifact carries findings the reviewer must surface, `validate-pinned.py` can flag drift (artifact says X, rendered review doesn't include X) — same pattern as `editorial-balance-counts-faithful`.
7. **Self-test on representative fixtures.** Run on PRs that should trip + PRs that should pass. False-positive rate should be near zero.
8. **Spike-test in CI.** Fire `@claude #new-review` on the test PR and confirm the artifact reaches the agent (model should cite the artifact name in the trail).

## When to consider per-step agents (not pre-steps)

The pre-computation pattern keeps the reviewer as a single Opus pass with richer input. If we ever need actual per-step agents (multiple model calls, intermediate prompts, agent-to-agent handoffs), the trigger conditions are:

- A check requires LLM judgment AND is currently being skipped (e.g., a specialized cross-document semantic check the main reviewer can't fit in attention).
- The check's prompt would be substantially different from the main reviewer's (e.g., a fact-check sub-agent that only does prose-vs-prose claim comparison).
- The cost of running it as a separate Sonnet call is less than the attention cost it imposes on the main reviewer.

Pass 2 / Pass 3 verification subagents already meet these criteria. Adding more requires the same justification — not "it would be cleaner architecturally," but "this specific failure mode requires a separate model call to fix."
