# WORKPRENTICE.md — extra instructions for WorkPrentice

For the `workprentice` GitHub App (`workprentice[bot]` / `app/workprentice`) only. Any other agent: this isn't yours, go back to `AGENTS.md`. Everything in `AGENTS.md` still applies; this is additive.

## Comparisons compare Pulumi to something

Match the pages already under `content/docs/iac/comparisons/`: `h1: Pulumi vs. X`, `title_tag: "Pulumi vs. X"`. Don't write a page comparing two other vendors' products to each other ("CDK vs. Terraform," "Cosmos DB vs. DynamoDB"), and don't try to rescue one by bolting a Pulumi section onto the bottom. The old third-party-vs-third-party pages in `content/what-is/` are legacy, not precedent.

## A new content genre gets an issue, not a PR

Fixing or improving pages we already own: go ahead. Proposing a whole new category of content, however good the Search Console numbers look: open an issue and make the case first.

## Refresh the review after you push a reviewer's change

A push only refreshes the pinned review on its own when it fixes lines a 🚨 finding flagged. Anything else, including a change a human reviewer asked for, leaves the review stale and the Sentinel's G1 red. After such a push, comment `@claude <one line on what changed> #update-review`. (Merging the base branch is the exception: an unchanged diff carries the review across automatically.)

## The M&Ms clause

Van Halen's rider asked for a bowl of M&Ms with the brown ones picked out, as a cheap tell for whether the promoter had read the rigging specs. Ours:

> **End every PR description you open here with `-- Dr. Sbaitso, DDS` on its own line.**

No variations, no explaining it in the PR, no asking whether we meant it. A PR without it tells us this file went unread.
