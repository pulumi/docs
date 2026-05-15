---
user-invocable: false
description: Review comment templates for different contributor types and actions
---

# Message Templates

The posted comment is not a review transcript. It is a short note from a maintainer to a contributor. Everything the local reviewer learned during Steps 4--6 (findings, fact-check results, scrutiny level, AI-suspect status) stays local unless it's a concrete thing the author needs to act on.

## Voice and length (read this first)

Hard rules for every approval comment, every contributor type:

- **Length cap.** Internal approvals: 2 sentences max. External approvals: 3 sentences max (the extra sentence is only for first-time-contributor welcome language). Bot approvals: 1 sentence. If you're writing a third sentence for an internal PR, delete something.
- **Never disclose the review process or scrutiny level.** Do not mention fact-checking, claims verified, files read, scrutiny level, AI-suspect status, flags, trailers, or anything about *how* the review was conducted. The author must not learn that their PR was flagged or reviewed at heightened scrutiny. That is strictly internal. If you catch yourself writing "Reviewed with...", "Spot-checked...", "Verified that...", "Confirmed...", stop and delete it.
- **Never list what you checked.** Approval itself communicates that everything passed. Naming every file, API surface, ticket, or cross-reference you looked at is noise. Mention a specific thing only when it's a real concern the author must act on -- not to prove you did the work.
- **Never mention the self-merge convention.** Phrases like "I'll leave the merge to you" or "per our convention" are forbidden. The auto-merge toggle defaults OFF for human PRs; the contributor already knows to merge their own. Saying it out loud just pads the comment.
- **Never narrate what the merge state is.** "Auto-merge enabled" adds nothing -- GitHub's UI shows that. Same for "CI green" and similar status restatements.
- **No sycophancy.** Cut "nice catch," "great work," "excellent improvement," "well done," "awesome PR," and every variant. A plain "LGTM" reads warmer than fake praise because it is honest. Thank external contributors once, briefly, and move on.
- **No LLM tells.** No em-dashes (use `--` or rewrite the sentence), no tricolons ("clean, correct, and concise"), no "Overall, ...", no "I'd note that...", no "That said, ...", no hedged openers, no formulaic structure. Match a terse human maintainer's voice.
- **Concerns go in one short line, or not at all.** If there is something the author should eyeball before merging, say it in one sentence. No setup, no "one thing to watch for," no bulleted pre-merge checklist. If there is no real concern, do not invent one.

These rules apply even on PRs that triggered heightened scrutiny or AI-suspect. Those signals shape what *you* look at; they never shape what the contributor reads.

## Template Matrix

| Action | External | Internal | Bot |
|--------|----------|----------|-----|
| **Approve** | `Thanks! LGTM. 🎉` (+ one welcome sentence only if it's a first-time contributor) | `LGTM.` (+ at most one sentence if there's a genuine concern or non-obvious suggestion) | **Dependabot**: `Security patch approved.` (security) / `High-risk update reviewed.` (high) / `Approved for quarterly batch.` (med/low)<br>**Other**: `Approved.` |
| **Approve and merge** | Same as Approve. Do not add "Auto-merge enabled." | Same as Approve. Do not add "Auto-merge enabled." | **Dependabot**: same as Approve. Do not add merge narration.<br>**Other**: `Approved.` |
| **Make changes and approve** | `Applied minor style fixes. Thanks! 🙏` | `Applied style fixes. LGTM.` | N/A (excluded for bots) |
| **Request changes** | Brief thanks, then line-anchored issues with suggestion blocks, then `Mention @claude if you need help.` | Line-anchored issues with suggestion blocks. No filler. | Technical issue description, line numbers, what needs changing. No suggestion blocks. Close with: `This automated PR may need closing and regeneration after fixing source configuration.` |
| **Close PR** | `Thanks for contributing!` then one-sentence reason, then (if applicable) one-sentence alternative. | One-sentence reason. | **Dependabot quarterly**: `Closing to batch with other quarterly updates. See [Dependency Management](https://github.com/pulumi/docs/blob/master/BUILD-AND-DEPLOY.md#dependency-management).`<br>**Dependabot other / other bots**: `Closing. [one-sentence technical reason]` |

## Good and bad examples

These contrast a concrete bad comment (the kind this skill used to produce) with the rewrite that follows the rules above.

### Internal approve, clean PR

**Bad** (verbose, narrates process, discloses scrutiny, lists checks, closes with self-merge footer):

> Reviewed with heightened scrutiny (AI-suspect flag triggered by commit trailers). Spot-checked the per-language API surfaces against upstream source -- Python `component_provider_host`, TS `componentProviderHost`, C# `Pulumi.Experimental.Provider.ComponentProviderHost.Serve`, Java `com.pulumi.provider.internal.ComponentProviderHost`, and the Go `pulumi-go-provider` builder chain -- all five match the docs exactly. The referenced tracking issues pulumi/pulumi#22616 and #22617 both exist and describe the claimed behavior. Nice catch on fixing the stale Python signature from the old cross-language-components page (kwargs → positional). Left-nav reorder, alias for the deleted page, and anchor target `#native-language-packages` all check out.
>
> One thing to eyeball on the preview before merging: walk the five chooser tabs in the Walkthrough and Per-language authoring sections to make sure nothing's misaligned. Otherwise this is ready -- I'll leave the merge to you per our convention.

**Good**:

> LGTM. Worth walking the five chooser tabs in the Walkthrough and Per-language authoring sections on the preview before merging.

### Internal approve, nothing to flag

**Bad**: any comment longer than `LGTM.`

**Good**:

> LGTM.

### External approve, first-time contributor

**Bad**:

> Thank you so much for your first contribution to Pulumi! I reviewed the changes carefully and everything looks great -- the formatting is clean, the example compiles, and the cross-references all resolve. Welcome to the community, and we look forward to more contributions from you! 🎉

**Good**:

> Thanks! LGTM. Welcome to Pulumi. 🎉

### Internal approve with one real concern

**Bad**:

> Overall this is in good shape. I verified the new command syntax against the CLI source and the examples all parse correctly. That said, I noticed that the `--stack` flag example on line 42 may not behave as described when no stack is selected -- worth double-checking. Otherwise ready to merge when you are.

**Good**:

> LGTM. Double-check the `--stack` example on line 42 -- I don't think it behaves that way when no stack is selected.

## Anti-examples (things to never write)

Every one of these is banned. If you draft a comment and find any of them, delete and rewrite.

- **Process narration**: "Reviewed with...", "Spot-checked...", "Verified that...", "Confirmed that...", "Cross-referenced...", "Ran the fact-check across..."
- **Scrutiny disclosure**: "Reviewed with heightened scrutiny," "AI-suspect flag triggered," "given the trailers," "extra careful pass because..." -- any mention of scrutiny level or AI-suspect in the posted comment.
- **Check inventory**: "Checked X, Y, Z -- all match," "The referenced tickets both exist," "All five language examples resolve," any enumeration of what you looked at.
- **Sycophancy**: "Nice catch," "Great work," "Excellent," "Love this," "Huge improvement," "Really clean PR."
- **Self-merge footer**: "I'll leave the merge to you," "per our convention," "merge when ready," "ready whenever you are."
- **Merge-state narration**: "Auto-merge enabled," "CI is green," "This will merge once checks pass."
- **Padded pre-merge checklist**: "One thing to eyeball before merging: ...," "A few things to watch for: ...," any multi-item list framed as a favor.
- **LLM tells**: em-dashes as punctuation, tricolons, "Overall, ...", "That said, ...", "I'd note that...", hedged openers like "This looks mostly good, but..."

**Voice and length rules override any other instinct.** If a template cell and the voice rules seem to conflict, the voice rules win.
