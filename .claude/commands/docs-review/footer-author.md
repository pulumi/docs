<!-- CLAUDE_REVIEW_FOOTER -->

---

**How to answer a finding** — every 🚨 and ❓ item above needs one of these before merge:

1. **Fix it** — push the change; the review refreshes and marks it fixed.
1. **Refute or accept it** — reply on this PR with one line per finding:
   `/resolve F3 refuted: the flag does exist in 3.261`
   Dispositions: `fixed` · `refuted` · `deferred` · `accepted` · `not-applicable` (the last three need a reason after `:`).
1. **Accept everything at once** — `/resolve all accepted: <why>` — you own the PR; saying so is a valid answer.
1. **Argue it out** — comment `@claude #update-review` with your reasoning and the review will re-adjudicate (it may concede, or hold with a 🛡️ note for your reviewer).

Pushing new commits refreshes this review automatically when the changes line up with the findings above; otherwise mention `@claude #update-review`. `@claude #new-review` starts over from scratch. Please don't edit, hide, or delete this comment — it is the review's record. Full mechanics: CONTRIBUTING.md §AI-assisted contributions.
