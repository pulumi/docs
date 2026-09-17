---
user-invocable: false
description: The closed set of dispositions for a review finding — what each means, when it's allowed, how to execute it, and how it's recorded.
---

# Dispositions

Every item on the worklist ends in exactly one of five states. There is no sixth state, and "we talked about it" is not one of them.

| Disposition | Means | Note required | Evidence that it happened |
|---|---|:---:|---|
| `fixed` | The diff changed; the finding no longer applies | no | The commit |
| `refuted` | Disputed with evidence; the model conceded | no | The `#update-review` mention + the ✅ Resolved `concede:` annotation |
| `deferred` | Real, but out of scope for this PR | **yes** | A filed issue, linked in the note |
| `accepted` | Knowingly shipping as-is | **yes** | The note (and, for a blocker, a PR comment) |
| `not-applicable` | The finding misreads the change; nothing to do and nothing to argue | **yes** | The note |

`fixed` and `refuted` evidence themselves. The other three are judgment calls someone has to own, so `review-worklist.py --require-clean` treats a missing note as an open item.

---

## `fixed`

The ordinary path. Make the change, keep it minimal, and keep it to what the finding actually asks for — a review fix is not an invitation to rewrite the section.

- Apply to the working tree during the walk; push once at the end (Step 5). A single small fix-push that lands only on flagged lines is what `auto-refresh-gate.py` recognizes, and it refreshes the review with no mention needed.
- For a `[style-blocker]` bullet in 🚨 (wrong product name, banned term, misspelling): fix it. These come from Vale's blocker allowlist, they are deterministic, and they are not worth disputing.
- For an inline ✏️ one-click suggestion: either the user clicks it in the Files-changed tab **or** you edit the line locally. Never both — the second one conflicts with the first.

## `refuted`

Use when the finding is wrong, not when it's inconvenient. Refuting well is a service: it tunes the pipeline. Refuting lazily poisons the outcome telemetry.

Dispute in the same `@claude #update-review` mention as the fixes, saying which finding and why. The update path classifies the dispute three ways, and what counts as evidence differs:

- **Domain-knowledge** ("this pattern is intentional; the team decided it") — the model defaults to conceding, and maintainer write access is itself sufficient evidence for design intent. Say plainly that it's a design decision.
- **Verifiable claim** ("that was added in v3.0", "the docs already say this elsewhere") — author authority proves nothing here. Bring the link, the file:line, or the command output, or the model will hold.
- **Reframing** ("you misread the sentence; the qualifier bounds it") — quote the sentence and the reading you intend.

Then check the outcome. A concede moves the finding to ✅ Resolved with a `concede: <reason>` annotation. **If the model holds** — a `🛡️ Disputed by … model held.` line — the item is *not* resolved. Take it back into the walk with the model's cited evidence in hand and pick a different disposition. Don't record `refuted` on a finding that was held.

## `deferred`

Real finding, wrong PR. Legitimate for a pre-existing problem the change merely brushed past, or a fix that would balloon the diff past what a reviewer can read.

- File the issue **now**, in the same session, and put its URL in the note. A deferral without an issue is an acceptance wearing a disguise.
- Give the issue enough context to act on cold: the finding text, the file, the line, and why it was out of scope here.
- Say it in the PR thread too, so the maintainer isn't left wondering. One line: "L88 heading case is pre-existing — filed #20456."

## `accepted`

Knowingly shipping with the finding standing. Always available, never free.

- The note must say *why*, in terms someone reading the PR later can evaluate: "house voice — we say 'simply' in tutorials deliberately", not "won't fix".
- For a 🚨 blocker, also post the reason as a PR comment. A blocker accepted silently reads to the scraper as `ignored_outstanding`, and to a maintainer as an oversight.
- This is the disposition to use when the user says "just merge it." Record it, with their reason, on each open item. That is the honest ledger entry, and it takes ten seconds.

## `not-applicable`

The finding is about something the change doesn't do — the reviewer matched the wrong line, or the finding describes code the PR deletes. Distinct from `refuted`: there's no factual dispute to adjudicate, just a mis-anchor.

- The note says what the finding actually points at and why nothing follows from it.
- If you find yourself reaching for this more than once or twice in a review, the review probably went stale against a newer head. Refresh it and re-read (skill Step 1) rather than dismissing item after item.

---

## Bucket-specific rules

- **🚨 Outstanding** — `fixed` or `refuted` are the expected outcomes. `deferred` and `accepted` are allowed but must be visible in the PR thread, not only in the local state file. Never leave one undecided.
- **⚠️ Low-confidence** — these don't block the PR and they still get a disposition. Most are author questions ("can you cite this?"); the answer is usually a one-line `fixed` or a `refuted` with the citation.
- **✏️ Style** — advisory. Apply, or `accepted` with a reason. Batch identical rewrites into one question; don't ask six times about "simply".
- **💡 Pre-existing** — optional by construction: not introduced by this PR and not the author's debt. Ask once whether to include them, default no, and `deferred` with an issue is the good outcome when the user says yes.

## Recording

State file, `.review-worklist-<PR>.json` at the repo root (gitignored):

```json
{
  "items": {
    "outstanding:L40": { "disposition": "fixed", "note": "" },
    "low:L12": { "disposition": "refuted", "note": "cited two paragraphs down; model conceded" },
    "style:content/docs/a.md:L91": { "disposition": "accepted", "note": "term of art on this page" }
  }
}
```

Write it as each decision is made, not at the end. The file is what makes `--resume` work after a lost session, and what `--require-clean` reads to answer the only question that matters at merge time: **is anything still undecided?**
