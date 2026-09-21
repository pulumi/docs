---
user-invocable: false
description: The closed set of dispositions for a review finding — what each means, when it's allowed, how to execute it, and how it's recorded.
---

# Dispositions

Every item on the worklist ends in exactly one of five states. "We talked about it" is not one of them.

| Disposition | Means | Note required | Evidence that it happened |
|---|---|:---:|---|
| `fixed` | The diff changed; the finding no longer applies | no | The commit |
| `refuted` | Disputed with evidence; the model conceded | no | The `#update-review` mention + the concede annotation |
| `deferred` | Real, but out of scope for this PR | **yes** | A filed issue, linked in the note |
| `accepted` | Knowingly shipping as-is | **yes** | The note (and, for a blocker, a PR comment) |
| `not-applicable` | The finding misreads the change; nothing to do and nothing to argue | **yes** | The note |

`fixed` and `refuted` evidence themselves. The other three are judgment calls someone has to own, so `review-worklist.py --require-clean` treats a missing note as an open item — and `/resolve` rejects them outright without a reason.

There is a sixth value in the data, `author-accepted`, but **nobody types it**. See [When you are the author](#when-you-are-the-author).

---

## Where a disposition lives

On the v3 surface the ledger is the `<!-- REVIEW_STATE … -->` block on the author card. It is the PR's own record: the Sentinel reads it to score G2, the reviewer brief renders it in the **Waiting on the author** list, and `review-worklist.py` seeds from it. A finding id absent from that block is **open**, whatever any comment says.

Two lanes write it, and the choice matters:

- **`/resolve F<n> <disposition>[: reason]`** — deterministic, zero model cost, agent-facing plumbing. Use it to *record* a decision the user has already made. `/resolve all <disposition>: <reason>` dispositions every open finding at once and always needs a reason. It requires the PR author or a write/maintain/admin collaborator and fails closed on an unreadable permission; comments from bot accounts are ignored entirely.
- **`@claude <reasoning> #update-review`** — the model lane. Use it whenever the finding needs *adjudicating* rather than recording: a dispute, a fix the auto-refresh gate didn't catch, an answer to an ❓ question. It is the only lane that can change the review's mind.

On the legacy v2 surface there is no `REVIEW_STATE` and no `/resolve`; `#update-review` and the local state file are all you have.

`.review-worklist-<PR>.json` at the repo root (gitignored) stays useful either way — it's where style items (which carry no `F<n>`) and your in-progress notes live:

```json
{
  "items": {
    "F1": { "disposition": "fixed", "note": "" },
    "F3": { "disposition": "refuted", "note": "cited two paragraphs down; model conceded" },
    "style:content/docs/a.md:L91": { "disposition": "accepted", "note": "term of art on this page" }
  }
}
```

Write it as each decision is made, not at the end. On v3 it is a cache the enumerator will re-seed from `REVIEW_STATE`; on v2 it is the only ledger there is.

---

## When you are the author

If the PR author dispositions their own finding as anything other than `fixed`, the handler records it as **`author-accepted`**, preserving what they typed as `original_disposition`.

This is deliberate, not a bug: self-adjudication shouldn't read as independent adjudication. The Sentinel counts the item as answered — the author *did* answer — while the brief keeps the row in front of the human approver, labelled with both values (`author-accepted (refuted)`).

What follows from it:

- **Tell the user before they pick.** "Refuting your own finding records as author-accepted and stays visible to your reviewer" is a fifteen-word heads-up that prevents a surprise in review.
- **A refutation you want *weighed* goes through `#update-review`,** not `/resolve`. The model can concede, which clears the finding on its own merits; `/resolve refuted` on your own PR just files your opinion.
- **`fixed` is never collapsed.** A real code change is evidence, not an opinion.

---

## `fixed`

The ordinary path. Make the change, keep it minimal, and keep it to what the finding actually asks for — a review fix is not an invitation to rewrite the section.

- Apply to the working tree during the walk; push once at the end (Step 5). A single small fix-push that lands only on the lines a 🚨 or ❓ finding anchors is what `auto-refresh-gate.py` recognizes: the card shows a 🔄 banner within a minute and refreshes itself with no mention needed. Only those two buckets anchor it, so a push that also fixes a ⚠️ or ✏️ item is declined as a whole and needs `#update-review` — worth knowing before you batch an advisory fix into a blocker's push.
- The v3 card usually writes the fix for you. Each blocking finding carries an `F<n> · Do this` block with the verbatim line, why it's wrong, and a replacement — often with an **If you'd rather keep it** alternative. Confirm the line still matches the file, then apply it.
- For a `[style-blocker]` bullet in 🚨 (wrong product name, banned term, misspelling): fix it. These come from Vale's blocker allowlist, they are deterministic, and they are not worth disputing.
- For an inline ✏️ one-click suggestion: either the user clicks it in the Files-changed tab **or** you edit the line locally. Never both — the second one conflicts with the first.

## `refuted`

Use when the finding is wrong, not when it's inconvenient. Refuting well is a service: it tunes the pipeline. Refuting lazily poisons the outcome telemetry.

Dispute in the same `@claude #update-review` mention as the fixes, naming the finding by its id and saying why. The update path classifies the dispute three ways, and what counts as evidence differs:

- **Domain-knowledge** ("this pattern is intentional; the team decided it") — the model defaults to conceding, and maintainer write access is itself sufficient evidence for design intent. Say plainly that it's a design decision.
- **Verifiable claim** ("that was added in 3.261", "the docs already say this elsewhere") — author authority proves nothing here. Bring the link, the file:line, or the command output, or the model will hold.
- **Reframing** ("you misread the sentence; the qualifier bounds it") — quote the sentence and the reading you intend.

Then check the outcome. A concede clears the finding. **If the model holds** — a 🛡️ note beside the finding — the item is *not* resolved; it stops blocking merge, but it stays visible to the human approver with the model's reasoning attached. Take it back into the walk and pick a different disposition rather than recording `refuted` on a finding that was held.

## `deferred`

Real finding, wrong PR. Legitimate for a pre-existing problem the change merely brushed past, or a fix that would balloon the diff past what a reviewer can read.

- File the issue **now**, in the same session, and put its URL in the note. A deferral without an issue is an acceptance wearing a disguise.
- Give the issue enough context to act on cold: the finding text, the file, the line, and why it was out of scope here.
- Say it in the PR thread too, so the maintainer isn't left wondering. One line: "F4's heading case is pre-existing — filed #20456."

## `accepted`

Knowingly shipping with the finding standing. Always available, never free.

- The note must say *why*, in terms someone reading the PR later can evaluate: "house voice — we say 'simply' in tutorials deliberately", not "won't fix".
- For a 🚨 blocker, also post the reason as a PR comment. A blocker accepted silently reads to the scraper as `ignored_outstanding`, and to a maintainer as an oversight.
- This is the disposition to use when the user says "just merge it." `/resolve all accepted: <their reason>` records it across every open finding in one comment. That is the honest ledger entry, and it takes ten seconds.

## `not-applicable`

The finding is about something the change doesn't do — the reviewer matched the wrong line, or the finding describes code the PR deletes. Distinct from `refuted`: there's no factual dispute to adjudicate, just a mis-anchor.

- The note says what the finding actually points at and why nothing follows from it.
- If you find yourself reaching for this more than once or twice in a review, the review probably went stale against a newer head. Refresh it and re-read (skill Step 1) rather than dismissing item after item.

---

## Bucket-specific rules

- **🚨 Outstanding** (v3 "Fix or disagree") — blocks merge. `fixed` or `refuted` are the expected outcomes. `deferred` and `accepted` are allowed but must be visible in the PR thread, not only in the ledger. Never leave one undecided.
- **❓ Author-answer** (v3 "Questions for you") — blocks merge, and it is addressed to you specifically: the reviewer is told not to police it. These are the items only the author can settle ("where does this figure come from?"). Usually a one-line `fixed` or a `refuted` with the citation, and answering is what unblocks it — a question left unanswered blocks just as hard as a 🚨.
- **⚠️ Reviewer-check** (v3, on the brief) — advisory, and written *for the approver*, not for you. It still gets a disposition, because an item someone is told to check is an item someone has to answer, but it never blocks and it batches well.
- **⚠️ Low-confidence** (legacy v2 only) — doesn't block, still gets a disposition. Most are author questions; the answer is usually a one-line `fixed` or a `refuted` with the citation.
- **✏️ Style** — advisory. Apply, or `accepted` with a reason. Batch identical rewrites into one question; don't ask six times about "simply". These carry no `F<n>`, so they live in the local state file only.
- **💡 Pre-existing** — optional by construction: not introduced by this PR and not the author's debt. Ask once whether to include them, default no, and `deferred` with an issue is the good outcome when the user says yes. **Only v2 puts these in the worklist** (the one bucket carrying `optional: True`); on v3 the brief gives a count and the evidence page the detail, so there is no row to disposition and nothing for `--require-clean` to skip. Note that what you leave open here is banked: `build-glowup-backlog.py` reads still-open and accepted findings off a content-review PR as page debt for the glow-up lane.
