---
title: "Knowledge as Code: The Memory File Just Got a Spec"
date: 2026-07-14
draft: false
meta_desc: "Google's Open Knowledge Format: a one-page spec for the LLM wiki. Markdown, one required field, git. Why knowledge as code is your agent loop's missing layer."
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - ai-agents
    - google-cloud
    - platform-engineering
category: perspectives
schema_type: auto

social:
    twitter: |
        Your agent's memory file just got a spec. Google's Open Knowledge Format: markdown, YAML frontmatter, exactly one required field.

        The smallness is the point. Engin Diri wrote up why it wins.
    linkedin: |
        Five weeks ago Engin Diri wrote that memory is what makes an agent loop compound: a markdown file outside the context window that holds what the model forgets. Three days after that post went live, Google shipped a spec for that file.

        The Open Knowledge Format is deliberately tiny. A directory of markdown, YAML frontmatter, one required field. The obvious critique, that there is almost nothing in it, turns out to be the strongest argument for it, and there is precedent in the agent stack for exactly this kind of win.

        Engin walks through what OKF actually specifies, why the smallness is the feature, and why platform teams should read it as the missing sibling of infrastructure as code.
    bluesky: |
        The LLM wiki everyone built after Karpathy's gist is a dialect only your own agent can read.

        Google's Open Knowledge Format pins it down: markdown, frontmatter, one required field. Knowledge as code.
---

Five weeks ago I wrote that the least glamorous piece of an agent loop is also the one that decides whether it compounds: [memory](/blog/stop-prompting-design-the-loop/). A markdown file outside the context window that holds what is done, what is next, and what was learned, because the model forgets all of it between runs. Write the memory file before the loop.

What I left open, because there was nothing to point at, was the format. My memory file looked nothing like yours, and neither of our agents could read the other's.

Three days after that post went live, Google shipped an answer.

<!--more-->

## The pattern everyone copied

[Andrej Karpathy published a gist in April](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) he called the LLM wiki, and it collected thousands of stars and forks. It's meant to be pasted straight into a coding agent. Instead of indexing your documents for RAG and re-deriving answers from raw text on every query, the agent builds a wiki and keeps it current: interlinked markdown pages, an `index.md` with a one-line summary per page, a `log.md` recording every change, entity pages that grow as sources come in. Drop in a meeting transcript and the agent reads it, updates a dozen existing pages, fixes the cross-references, and appends to the log in one pass.

It took off for the same reason wikis usually die. A knowledge base is valuable in exact proportion to the bookkeeping nobody wants to do: summarizing, linking, reconciling contradictions, pruning stale claims. Karpathy's line, which Google now quotes back in its own announcement, is that LLMs "don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass." The human curates sources and asks questions. The agent does the janitorial work that made every previous wiki rot.

## A wiki only your agent can read

Then everyone built one, and every one is a dialect. Mine links related pages in the frontmatter; yours links them at the bottom of the body. Mine has a `tags` field; yours calls it `categories`. None of this matters while the wiki serves one person, because the schema lives in your `CLAUDE.md` and your agent reads it on every run.

It matters the moment the wiki has to travel. Hand your knowledge base to a teammate and their agent starts guessing at your conventions, or misses half the structure entirely. A platform team that wants one shared wiki, queried independently by everyone's agents, has no format to agree on. A knowledge base you can't hand to someone else's agent is a silo of one. And a team's collective knowledge should outlive any single person's markdown habits.

## What Google actually shipped: the Open Knowledge Format

On June 12, two tech leads in Google Cloud's data analytics engineering org [announced the Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/), with a [spec and reference tooling on GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog). Strip the branding and OKF v0.1 is a formalization of the Karpathy pattern:

- A bundle is a directory tree of markdown files. Two filenames are reserved: `index.md` for progressive disclosure and `log.md` for update history. Everything else is a concept document.
- Every concept carries YAML frontmatter with exactly one required field: `type`. Five more are recommended: `title`, `description`, `resource`, `tags`, `timestamp`. Producers can add anything; consumers must preserve what they don't understand.
- A markdown link from one concept to another asserts a relationship. The prose around the link says what kind.

The whole spec fits on a page, and that's deliberate. The announcement names three principles: minimally opinionated; producers and consumers independently swappable; a format rather than a platform. No required SDK, no compression scheme, no new runtime. Reading a bundle is `cat`; distributing one is `git clone`. The repo backs it up with reference tooling: an enrichment agent that drafts concept docs from BigQuery datasets, and a static visualizer that renders a bundle as a graph. Three sample bundles, built by that same agent, give you something to copy from.

## The critique is the feature

The pushback writes itself: there is almost nothing here. Folder indexes and five suggested frontmatter fields, on top of a pattern the community already had. True. Also the point.

The standards that stick are embarrassingly small. [MCP](/docs/ai/mcp-server/) didn't model your tools; it standardized the socket they plug into. `AGENTS.md` fixed nothing but a filename, and that was enough for [Neo to read the same conventions file as every other agent](/blog/pulumi-neo-now-supports-agentsmd/). [Agent Skills](/docs/ai/skills/) gave procedure a place to live, and docs sites settled on [/llms.txt](/llms.txt) for published content. Knowledge was the layer still missing its boring little standard. Whether OKF specifically is the one that survives matters less than the shape it commits to: markdown, frontmatter, git. Every other layer of the agent stack already landed there, so that bet is safe.

## Knowledge as code

Platform teams should care about this before anyone else. Infrastructure as code captures the what: the resources, the config, the dependency graph. It has never captured the why. The runbook for rotating credentials, the decision record explaining the pinned CNI version, who owns the cluster, what the incident in November taught you. That knowledge lives in a wiki behind an API, a shared drive, a Slack thread, and the heads of two senior engineers. Google's announcement frames this fragmentation as the problem: agents reassembling answers from systems that each speak a proprietary format.

OKF's answer is a move platform engineers will recognize, because it's the same one that produced IaC: put it in git, make it diffable, review changes in pull requests. Knowledge as code, sitting next to the infrastructure as code it explains:

```
platform/
├── index.md
├── log.md
├── services/
│   ├── index.md
│   ├── checkout-api.md
│   └── payments-worker.md
├── runbooks/
│   ├── index.md
│   └── rotate-database-credentials.md
└── decisions/
    ├── index.md
    └── why-we-pin-the-vpc-cni-version.md
```

The recommended `resource` field takes a URI naming the asset a concept describes, and a Pulumi URN is exactly that:

```yaml
---
type: runbook
title: Rotate the payments database credentials
description: Zero-downtime credential rotation for the payments Postgres instance.
resource: urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db
tags: [payments, postgres]
timestamp: 2026-07-01T09:30:00Z
---
```

Now the runbook names the exact resource it operates on. An agent planning a change to that database can walk from the URN to the runbook to the decision record that explains the constraint, before it proposes anything. In the loop post I said [skills](/docs/ai/skills/) are intent written down, the conventions an agent reads instead of guessing. A knowledge bundle is the other half: experience written down. Tools give the loop hands, skills give it habits, and the bundle is what it gets to remember.

Before writing any of that down, I ran the test. A fresh agent got two inputs, the spec and this bundle, and one question: which services touch the payments database, and how do I rotate its credentials without downtime? It read six files and answered correctly, down to why rotating a second time too soon is the dangerous move. What sold me was the file it didn't read. It left the CNI decision record closed, because the cross-links mark that page as a cluster concern, not a database one.

The bundle is public, exactly the tree above. Clone it, hand your agent the spec, and ask your own questions:

{{< github-card repo="dirien/pulumi-platform-okf-bundle" >}}

## What a standard won't do for you

Three caveats, so nobody mistakes this for magic.

**It formats knowledge; it doesn't create it.** The warning from the loop post applies with no edits: memory is what lets a loop compound, and slop compounds right alongside it. A wrong runbook in a beautifully conformant bundle is still a wrong runbook, now served to every agent on the team with confidence. The leverage isn't the format. It's that knowledge changes finally go through review like code changes.

**v0.1 is a draft, and the name may not survive.** Google says so itself: the announcement calls v0.1 "a starting point, not a finished standard." OKF could lose to a better spec next year. I'd start anyway, because converting markdown with frontmatter into markdown with slightly different frontmatter is the cheapest migration you'll ever run, and it's precisely the kind of mechanical pass an agent finishes in an afternoon. The shape is the commitment. The name is a detail.

**Conformance is a floor, not hygiene.** The spec requires consumers to tolerate broken links, missing indexes, and unknown types. That tolerance keeps readers working, and it also means nothing forces your bundle to stay healthy. Karpathy's gist included a lint pass for a reason: contradictions, orphaned pages, stale claims. Keep it, and run it the way you lint code, on a schedule, with findings that reach a human.

## Where to start

1. **Pick the knowledge that already hurts.** The runbook nobody can find during an incident, the onboarding doc that's wrong in ways only one person knows. One domain, not the whole org.
1. **Let the agent do the conversion.** Paste the [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) into your coding agent, point it at the existing folder of docs, and have it refactor them into a bundle. This is exactly the bookkeeping LLMs are good at, and it works as well on a wiki export as on a fresh start.
1. **Put the bundle where the code lives.** Same repo or a sibling, but in git, behind pull requests. The day a knowledge change gets a review comment is the day the bundle becomes trustworthy.
1. **Wire it into the loop.** Agents read `index.md` first and drill down only when a concept earns it, which keeps the context window small. The memory file I told you to write before the loop now has a format, and every agent you run, in [whatever harness you built](/blog/stop-tuning-prompts-build-a-harness/), can read the same one.

The advice from June holds: write the memory file before the loop. What changed is that the file no longer has to be a private dialect. There's now a one-page, git-native spec for the layer your agents think with, and the smallness that makes it look trivial is the property that lets it spread. The loop does the typing. The wiki does the remembering. And the remembering is now something you can put in a pull request and hand to the next agent, like everything else you ship.

{{< blog/cta-button "Wire Pulumi context into your agents" "/docs/ai/" >}}
