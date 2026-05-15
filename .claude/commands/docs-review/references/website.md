---
user-invocable: false
description: Review criteria for marketing, pricing, legal, and competitive landing pages under content/ that aren't blog or docs.
---

# Review — Website

Applied to `content/**.md` paths *not* under `blog/`, `case-studies/`, `docs/`, `learn/`, `tutorials/`, or `what-is/` — pricing, legal, `vs/`, `why-pulumi/`, `about/`, `careers/`, etc. These pages carry claims with potential revenue, legal, and FTC consequences if wrong. Fact-check is on for every change.

**Stance.** Authors of these pages typically have non-public data and domain expertise the reviewer doesn't. Surface claims as **verification asks** ("worth a double-check before merge"), not assertions of error. Default tier is ⚠️. Reserve 🚨 for (a) legal semantic changes and (b) claims a public source positively contradicts. Inability to verify is itself worth surfacing — but as "please confirm," not "this is wrong."

---

## Scope

- Diff-only. Pre-existing issues off. Fact-check on, heightened.

## Criteria

`docs-review:references:shared-criteria` applies (links, images, spelling, generic prose).

### Pricing claims

When the diff touches a dollar amount, tier name (`Team`, `Enterprise`, etc.), feature inclusion, or pricing condition, surface for author double-check against the canonical pricing source. ⚠️ — cheap verification before a wrong number ships.

### Date-sensitive language

Absolute claims (`the only`, `the first`, `the latest`, `currently`, `as of <year>`) without a dated qualifier in the same sentence — these go stale silently when not auto-republished. ⚠️ with a suggested dated qualifier; author can dismiss if intentional.

### Competitive claims (`content/vs/**`)

Surface claims about a competitor's *missing* features for author re-verification — competitors ship features and the claim becomes false. ⚠️ as a verification ask. **Escalate to 🚨** when public sources show the competitor *does* support the feature today (libel/FTC exposure).

### Legal text (`content/legal/**`)

- **Semantic edits → 🚨**, route to legal team review before merge. Wording changes affecting rights, obligations, scope, or dating.
- **`last_updated` integrity → ⚠️**: bumping the date without semantic changes, or changing semantic content without bumping the date.
- **Cosmetic edits** (typos, format) → silent.

### Customer attributions

When the diff touches a named-person quote or attribution (`"<quote>" — Jane Smith, CTO at AcmeCorp`), surface for author confirmation the person is still in role at the named company. ⚠️ — author likely knows. Skip when the quote is unchanged context around an unrelated edit.

## Fact-check

Invoke `docs-review:references:fact-check` with:

- **Files:** changed `content/**.md`
- **Scrutiny:** heightened, verification-ask-framed (see Stance)
- **Sources:** public only; surface unverifiable claims as "please confirm" rather than dropping them

## Do not flag

- **Marketing-speak.** "Simple," "powerful," "the modern way" are appropriate here even though docs flags them.
- **Cited superlatives.** "Fastest IaC tool" with a benchmark link is a claim, not a finding.
- **AGENTS.md canonical-link rule.** That rule applies to `/docs/` paths only.
- **AEO H2 patterns.** Marketing H2s are conversion-driven; AEO applies to docs/blog only.
- **Phrasings that come across as "you got this wrong."** Re-frame as "worth a double-check before merge" unless you have positive contradicting evidence.
