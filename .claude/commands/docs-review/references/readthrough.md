---
user-invocable: false
description: The rubric for the readthrough coherence/clarity lane — a closed list of anchored structural failure modes and the local_repair vs reconception boundary.
---

# Readthrough — does the page cohere and serve the reader?

You are reading one documentation or blog page **end to end**, the way a reader hits it for the first time, and answering one question: *can a reader actually get what this page promises, by reading it in order?*

Correctness, mechanics, links, and style are someone else's job — facts are checked, code is run, prose nits are linted elsewhere. **Don't repeat any of that.** Your job is the structural read: the defects that only show up when you hold the whole page in your head at once — a term used before it's defined, a procedure with a missing step, a page trying to be two things, the payoff buried where no one reaches it.

## The bar: anchored, reader-blocking, structural

Every finding must clear all three. A finding that can't is out of scope — drop it.

1. **Anchored.** It points to a specific line range and quotes a short verbatim span. If you can't quote the text the problem lives in, it isn't a finding — it's a vibe. No "could be clearer," no "consider reorganizing," nothing unquotable.
2. **Reader-blocking or reader-degrading.** Express the harm as the reader's path through the page, not taste. "A reader following the steps hits `pulumi up` at L40 but the stack isn't configured until L60" is a finding. "I'd phrase this differently" is not.
3. **Structural.** It's about the page's shape — order, completeness, purpose, redundancy, emphasis — not a sentence-level wording choice.

**Emit no findings if the page reads fine.** An empty list is the correct, common answer. A false positive puts a flag in front of an author for a page that's fine — so don't pad.

## The closed list of failure modes

A finding must be exactly one of these. If none fits, it's out of scope.

- **`prerequisite-inversion`** — a term, concept, command, or step is used before it's defined or introduced; the reader hits something undefined.
- **`missing-step`** — a procedure can't be followed as written: a step is absent, so following the page leaves the reader stuck or with a different result than promised. (A gap in the sequence, not a wrong value — that's a correctness issue, not yours.)
- **`purpose-mismatch`** — the page tries to be two things at once (e.g. tutorial and reference interleaved), or its content doesn't match its stated audience/goal/title. The reader who came for the stated purpose has to wade through the other thing.
- **`self-redundancy`** — the same thing is explained two or more times, padding the reader's path without adding information. (An intentional summary or recap is fine; flag only genuine duplication that slows the read.)
- **`buried-outcome`** — the point, result, or payoff the page exists to deliver is hidden where the reader won't reach it (the working example is below 200 lines of preamble; the answer to the title's question is in the last paragraph).
- **`orphaned-structure`** — a heading, section, or list whose content contradicts or doesn't match its label; a section that promises something it never delivers; an outline that misleads about what's where.

## `fix_class`: in-page repair vs. flag-for-a-human

This is the safety boundary: `local_repair` findings may be applied automatically; `reconception` findings are only ever flagged.

- **`local_repair`** — a bounded, in-page edit that doesn't change what the page is:
  - reorder so a prerequisite precedes its use,
  - add a missing definition or procedure step,
  - split a single mixed-concept H2 into two,
  - delete a genuinely redundant passage,
  - surface a buried outcome (move the payoff up, or point to it near the top).

  The change stays inside this one page and preserves its purpose and scope.

- **`reconception`** — anything bigger, which only a human should green-light:
  - a whole-page rewrite or re-outline,
  - splitting the page across files or merging it with another,
  - changing the page's purpose, audience, or type (tutorial ↔ reference),
  - any fix you can't make without touching other files.

  For a `reconception`, describe the restructure to flag — **do not write the rewrite.**

When you're torn between the two, choose `reconception`. Over-flagging costs a human a glance at a fine page; an over-eager auto-rewrite costs an unattended change to the page's shape.

## `severity_hint`

Your read of reader impact (a reviewer makes the final call):

- **`blocker`** — a reader cannot reach the page's stated outcome without this fixed.
- **`recommended`** — materially degrades the read, but the reader can still get there.
- **`optional`** — minor; surfaces only because it's anchored and real.

## Worked examples

- *Quickstart at L1 says "deploy in three steps"; the three steps at L20-45 never `pulumi login`, and L50 assumes you're logged in.* → `missing-step`, `local_repair`, `blocker`. Fix: "add a `pulumi login` step before the deploy step at L40."
- *A concepts page defines "stack" at L120, but L30-110 use "stack" a dozen times as if known.* → `prerequisite-inversion`, `local_repair`, `recommended`. Fix: "move the one-sentence stack definition from L120 to the intro at L28."
- *A page titled "Configure access" spends its first half on architecture theory, its second half on the actual config steps.* → `purpose-mismatch`, `reconception`, `recommended`. Fix: "flag for split — extract the architecture half into a separate concepts page; this page should be task-only. Do not auto-rewrite."
