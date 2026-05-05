---
title: "Seven Rules for Building an AI-First Software Factory"
date: 2026-05-04
draft: true
meta_desc: "Ewan Dawson, CTO of Compostable AI, on building a software factory where AI agents write the code. Seven rules learned across nineteen client deployments."
meta_image: meta.png
feature_image: feature.png
youtube_id: oHNdlWlsR-w
authors:
    - ewan-dawson
    - adam-gordon-bell
tags:
    - ai
    - ai-agents
    - infrastructure-as-code
    - pulumi-neo
    - pulumi-esc
social:
    twitter: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson, CTO of Compostable AI, on the seven rules he built around the agents that write almost all of his company's code.
    linkedin: |
        Ewan Dawson used to think of writing code as a craft. Now he runs a factory — and the people on the floor are AI agents.

        Ewan is CTO of Compostable AI, where five engineers run an AI-first software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. Most of the code his company ships, he hasn't personally read.

        Adapted from his recent Pulumi webinar — and expanded with the rules they didn't have time to land on stage.
    bluesky: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson's seven rules for an AI-first software factory — where agents write nearly all the code.
---

*Ewan Dawson is CTO of [Compostable AI](https://compostable.ai/), where five engineers run an AI-first software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. This article is adapted from his recent Pulumi webinar, and covers rules in more depth then we had time for on stage.*

<!--more-->

I used to think of writing code as a craft. Now I run a factory, and the people on the floor are AI agents.

Most of the code Compostable ships now, I haven't personally read. The agents are real engineers — better at some things than I am, weaker at others. These are the seven rules I've built around them. The tools will be different in a year. The rules, I think, won't.

## 1. Transform, don't enhance

A few years ago, before I started Compostable, I was working at a large multinational when [GitHub Copilot](https://github.com/features/copilot) first came out. Everyone got excited about it — that was the first ChatGPT moment in software development, and I remember being blown away the first time I used it. I thought: this changes software development. Everything changes now.

But getting it into the hands of engineers at that company turned into an uphill fight with the Governance, Risk, and Compliance team. Copyright, security, compliance. Each concern was reasonable. Each one slowed us down. We were trying to drop a future-of-software-development tool into a process designed for none of that. By the time we'd negotiated a limited trial, I'd already worked out that whatever this technology was going to become, it wasn't going to become it inside a big enterprise first. Startups would. So I left and started one.

When we built Compostable, we were deliberate about it. I wasn't bolting agents onto a process I already knew. I was trying to figure out what the process should look like if AI did most of the writing from day one.

{{< notes type="tip" >}}
**Don't bolt AI onto your existing workflow. Redesign the workflow around what agents can do.** Most of the leverage in this technology comes from rebuilding around it. The tool change is the small part.
{{< /notes >}}

## 2. Remove the problem, don't solve it

As we were building Compostable, one of the first problems was a version of the same risk I'd faced at my previous company. Our buyers are large enterprises in regulated industries — the perception of risk around AI is high, and "we share a sandbox with the other clients" is not something anyone wants to hear.

If the agents were going to write code that touched production, blast radius wasn't a hypothetical: one bad agent run could trash a customer's database, or leak one client's data into another's. The obvious move was to build a multi-tenant sandbox: guardrails, approvals, rollback. Every version we tried still had agents loose in a shared environment, one bug away from making one customer's data visible to another.

So we didn't build the sandbox. We gave every client their own AWS account instead — nineteen accounts now, one per client, each paired with a digital-twin staging environment. Agents iterate on staging until the work is verified, and only then does it ship to production. The AWS account itself is the security boundary, and Amazon has spent twenty years getting that boundary right. Automated guardrails layer on top — defense in depth — and we got ISO 27001 certified in six weeks because most of the work was already done.

We didn't make the multi-tenant problem go away. We *shifted* it: instead of securing a shared environment, we now manage a fleet of accounts. That's a problem with twenty years of well-trodden answers.

{{< notes type="tip" >}}
**Remove the problem before you try to solve it.** Easier to manage a fleet of accounts than to secure a shared environment. Easier to reframe the problem than to engineer your way through it.
{{< /notes >}}

The trade-off is real — running a fleet that size is its own kind of work, and a lot of the rules below are what makes it manageable. But it's work I know how to do.

## 3. Pick tools your agents can drive

Managing nineteen accounts meant picking tools that didn't need a human in every loop. Our first attempt was [CDK](https://aws.amazon.com/cdk/) — TypeScript-native, same language as our application code. My initial thinking was that infrastructure is code, it's just code, that'd be straightforward. It wasn't. As we added clients, the accounts started to drift out of sync. Deployments took forever. Retries got complicated when one account update succeeded and another failed. The tooling we were using wasn't up to the job.

I went looking for something better. Pulumi solved the parts that were burning us: reliable deployment from code, configuration that varied per-client without forking the codebase. Pulumi had already shipped [Neo](/product/neo/) and an MCP server when most vendors were still figuring out their AI story; they were clearly betting on agents. That's the kind of partner I was looking for. Neo picked up our infrastructure on day one. One of my colleagues put it: "The scary thing about Neo is it just seems to know everything about what we do."

> *"I don't actually care if it's HCL or TypeScript, as long as my software development agents can write it. And they do a better job with TypeScript than HCL."*
>
> *— Ewan Dawson*

What kept us going wasn't any one feature. It was that the pieces composed — Pulumi IaC, [Pulumi ESC](/docs/pulumi-cloud/esc/), Neo, and [Pulumi Cloud](/docs/pulumi-cloud/) all built on top of each other as primitives, and the benefits compounded across the stack. We picked one piece for the agentic mindset, and the next piece was already in the box.

{{< notes type="tip" >}}
**Tools have to share your AI-first mindset. If they don't integrate deeply, the human becomes the glue.** If part of your stack still requires a human to click through a web UI to provision an account, your agents stop there.
{{< /notes >}}

## 4. Don't let one agent do everything

Early on, when we first wired agents into the development flow, the move I reached for was a god prompt — one big system prompt that defined the whole software factory, with one agent turned loose on the work. It didn't work. The agents that write the code aren't the best at checking their own homework. They're lenient on themselves.

So we don't run one agent. We run a constellation of them, each with a narrow job. One agent reviews the backlog and flags under-specified tickets. Another writes the application code. Neo writes the infrastructure. When an agent hits an infra task, [AGENTS.md](https://agents.md/) tells it to delegate to Neo via Pulumi's MCP server. Then four or five checker agents go over the PR from different angles — performance, correctness, security. They're running on smaller models than the writers, and you know what? They always find something.

{{< notes type="tip" >}}
**Don't let any agent mark its own homework.** Specialization compounds. The checkers are cheap, they each look for one thing, and a narrow job means a narrow context window. Infrastructure alone can fill an agent's context. Give it the whole job and there's no room left to think.
{{< /notes >}}

## 5. Measure human hours per unit of value

Once the agents were reliably producing code, throughput went up — but not by the order of magnitude we'd hoped. Every PR still queued behind a human reviewer. Every rollout still went through a person. The bottleneck had moved: agents were producing the code; humans had become the slow path on either side of them.

The metric I use now is human hours per unit of value produced. Look at every step and ask what you can automate; if you can't, ask why not. The pattern we've ended up with is humans at the start, writing the specs and choosing the work that matters; humans at the end, doing the final pre-production check; agents in between.

The mechanism that keeps the humans out of the middle is configuration. We hold all of it in ESC, and ESC environments inherit from each other: a base layer for the platform, a layer for staging vs. production, per-client overrides as small diffs on top. When something needs to change across all nineteen clients, we update one base environment and run `pulumi up`, or hand it off to Neo to redeploy every stack. One change, nineteen clients updated — not nineteen tickets and three meetings. If you're managing config sprawl across environments, ESC is where I'd start.

{{< notes type="tip" >}}
**Measure human hours per unit of value. Treat every one as a bottleneck to remove.** Engineers writing or reviewing routine code is an unacceptable bottleneck. Each one you remove gives the agents another order of magnitude.
{{< /notes >}}

## 6. Design for convergence, not one-shot correctness

Even after the constellation was running, the first pass was rarely the keeper. Agents drift. They go off-topic, work in areas they're not supposed to. As strong as the models are, you're not shipping the first thing they produce.

The trick is that it doesn't matter how many tries it takes, as long as no human is in the loop. We run our pipeline as a convergence machine: each iteration goes back through the checker agents from the last rule, the issues they find feed into the next pass, and eventually all the agents pass, all the tests pass. Total time: an overnight run.

Concretely: a backlog ticket goes in. One agent expands the ticket — checks it's well-specified, injects context if it's missing. A coding agent works it. The PR comes back through four or five checker agents who comment from their own angle. Their comments feed the next round; the coding agent picks them up and revises. Round and round until every checker is satisfied, every test passes, every guardrail fires green. End-to-end: ticket to merged PR, no human in the middle.

Two things have to be true for that loop to work. You need a way to evaluate whether the output is good enough. Without that, you don't know when to stop. And the loop has to actually converge: each pass has to get closer, or you'll churn forever on the same issue under different framings.

Once that's working, the work shifts. The question is no longer *will it finish* but *how cheap can we make it* — fewer iterations, smaller models on the checker side, better prompts so the coding agent lands closer on the first try. The climbing machine is the floor; everything after is making the climb cheap.

I've shipped more code in the last two years — after a stretch in leadership where I wrote almost none — than I did in the previous fifteen, all of it in languages I couldn't write by hand.

{{< notes type="tip" >}}
**Don't aim for one-shot correctness. Build a machine that climbs.**
{{< /notes >}}

## 7. Run the factory in the cloud, not on a laptop

That machine has to live somewhere. Once it does, the question becomes where you can actually work on it. The default mental picture of AI coding is one developer in their IDE, watching Copilot autocomplete. That's not what we do. Our agents run in the cloud. The factory keeps producing while engineers are in meetings, talking to clients, or asleep. We don't sit there watching progress bars. We don't sit there waiting for the next checker pass to finish. Our engineers spend their time with clients.

What "time with clients" means in practice is the part of the job that's gotten *more* important since the agents arrived. Engineers spend less time at keyboards and more time understanding the business — talking to customers about what they actually need, writing it down in language the agents can act on, reviewing the spec before any code starts. Given/when/then, BDD-style. The factory runs while the engineers do the part of the job a model still can't do for you.

Running it in the cloud isn't just about keeping it on at night. Once you've built it, the next job is to tweak it: improve quality, reduce costs, improve throughput. That's hard if the factory is scattered across developers' laptops. Configuration and credentials drift between machines. The same prompts run against different model versions; the same env vars get half-set. The thing you're trying to optimize lives in different states across the team. It doesn't work on-prem, on laptops, or on a Mac Mini in the corner. That's why we run on Pulumi Cloud rather than [GitHub Actions](https://github.com/features/actions) — Pulumi Cloud is somewhere you can iterate on the factory itself, not just trigger it.

{{< notes type="tip" >}}
**Build the factory somewhere you can work on it — not just somewhere it can run.**
{{< /notes >}}

## Closing thought

If you're where I was two years ago: don't ask how AI fits into what you already do. Find the biggest thing a human still does by hand and take that human out of the loop. Then do it again.

The factory is built one rule at a time. Mine isn't finished — and that's the point.

---

*Watch the [original Pulumi webinar](https://www.youtube.com/watch?v=oHNdlWlsR-w). Learn more about [Compostable AI](https://compostable.ai/) and [Pulumi Neo](https://www.pulumi.com/product/neo/).*
