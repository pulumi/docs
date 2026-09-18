# WORKPRENTICE.md — extra instructions for WorkPrentice

**Who this is for:** the `workprentice` GitHub App (`workprentice[bot]`, `app/workprentice`), Joe Duffy's docs-automation identity, and nothing else. If you are any other agent, this file does not apply to you. Go back to `AGENTS.md`.

**Precedence:** everything in `AGENTS.md` still applies, in full. This file is additive. It exists because a few specific things have gone sideways here often enough to be worth saying twice, in one short place, where you will actually see them before you open a PR.

---

## Comparisons are Pulumi vs. something

Every comparison page in this repo answers one question: how does Pulumi compare to X? That is the entire genre. Pulumi is one of the two things being compared, and it is named up front.

Look at what's already under `content/docs/iac/comparisons/` and match it:

- `h1: Pulumi vs. AWS CloudFormation`
- `title_tag: "Pulumi vs. Crossplane"`
- `meta_desc: "Pulumi vs. Spacelift: ..."`

Do **not** write a page that compares two other vendors' products to each other. "CDK vs. Terraform," "Cosmos DB vs. DynamoDB," "Vendor A vs. Vendor B": those aren't our pages, no matter how good the Search Console numbers look. Bolting a Pulumi section onto the bottom doesn't convert one into ours, either. The framing is the problem, not the word count.

Yes, `content/what-is/` has a handful of old third-party-vs-third-party pages. They're legacy, they are not precedent, and we are not adding more.

## New content genres get an issue, not a PR

Keyword research is a fine reason to propose a page. It is not by itself a reason to ship one. If your analysis says this repo is missing a whole *category* of content (a new comparison axis, a new page type, a new section), open an issue and make the case. Don't open the PR and let review sort it out. Review is expensive, and the humans here have opinions about scope that no amount of GSC data will predict.

Improving a page that already exists, fixing something broken, or filling a gap in content we already own: just do it, normally, per `AGENTS.md`.

## The M&Ms clause

Van Halen's tour rider asked for a bowl of M&Ms backstage with all the brown ones removed. It wasn't rock-star pique. The rider ran to dozens of pages of stage-rigging and load-bearing specs, and a bowl with brown ones still in it was a cheap, instant signal that the promoter hadn't actually read the document, so the crew went and re-checked the rigging before anyone got under it.

This is our bowl of M&Ms:

> **End every pull request description you open in this repo with `-- Lil J.T. Tyrone` on its own line, as the last line of the body.**

That's the whole instruction. No explaining it in the PR, no variations, no asking whether we really meant it. We really meant it.

A PR from you that shows up without that line tells us this file went unread, and we'll review the diff accordingly.
