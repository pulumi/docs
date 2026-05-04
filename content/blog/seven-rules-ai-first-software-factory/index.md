---
title: "Seven Rules for Building an AI-First Software Factory"
date: 2026-05-04
draft: true
meta_desc: "Ewan Dawson, CTO of Compostable AI, on building a software factory where AI agents write the code. Seven rules learned across nineteen client deployments."
meta_image: meta.png
feature_image: feature.png
authors:
    - ewan-dawson
    - adam-gordon-bell
tags:
    - ai
    - ai-agents
    - infrastructure-as-code
social:
    twitter: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson, CTO of Compostable AI, on the seven rules he built around the agents that write almost all of his company's code.
    linkedin: |
        "I used to think of writing code as a craft. Now I run a factory, and the people on the floor are AI agents."

        Ewan Dawson is CTO of Compostable AI, where five engineers run an AI-first software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. Most of the code his company ships, he hasn't personally read.

        Adapted from his recent Pulumi webinar — and expanded with the rules they didn't have time to land on stage.
    bluesky: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing. Ewan Dawson's seven rules for an AI-first software factory — where agents write nearly all the code.
---

*Ewan Dawson is CTO of [Compostable AI](https://compostable.ai/), where five engineers run an AI-first software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. This article is adapted from his recent Pulumi webinar (TBD: link to webinar recording), expanded to cover the rules they didn't have time to land on stage.*

<!--more-->

I used to think of writing code as a craft. Now I run a factory, and the people on the floor are AI agents.

Most of the code Compostable ships now, I haven't personally read. The agents are real engineers — better at some things than I am, weaker at others. These are the seven rules I've built around them. The tools will be different in a year. The rules, I think, won't.

## 1. Transform, don't enhance

A few years ago, before I started Compostable, I was working at a large multinational when GitHub Copilot first came out. Everyone got excited about it — that was the first ChatGPT moment in software development, and I remember being blown away the first time I used it. I thought: this changes software development. Everything changes now.

But getting it into the hands of engineers at that company turned into an uphill fight with GRC. Copyright, security, compliance. Each concern was reasonable. Each one slowed us down. We were trying to drop a future-of-software-development tool into a process designed for none of that. By the time we'd negotiated a limited trial, I'd already worked out that whatever this technology was going to become, it wasn't going to become it inside a big enterprise first. Startups would. So I left and started one.

When we built Compostable, we were deliberate about it. I wasn't bolting agents onto a process I already knew. I was trying to figure out what the process should look like if AI did most of the writing from day one.

**Don't bolt AI onto your existing workflow. Redesign the workflow around what agents can do.** Most of the leverage in this technology comes from rebuilding around it. The tool change is the easy part.

## 2. Remove the problem, don't solve it

If the agents were going to write code that touched production, blast radius wasn't a hypothetical — one bad agent run could trash a customer's database. The obvious move was to build a multi-tenant sandbox: guardrails, approvals, rollback. Every version we tried still had agents loose in a shared environment — one bug away from making one customer's data visible to another.

So we didn't build the sandbox. We gave every client their own AWS account instead — nineteen accounts now, one per client. Single tenant, all the way down. Agents only ever touch staging. The AWS account itself is the security boundary, and Amazon has spent twenty years getting that boundary right. We got ISO 27001 certified in six weeks because most of the work was already done.

**Remove the problem before you try to solve it.** Easier to manage a fleet of accounts than to secure a shared environment. Easier to reframe the problem than to engineer your way through it.

The trade-off is real — running a fleet that size is its own kind of work, and a lot of the rules below are what makes it manageable. But it's work I know how to do.

## 3. Pick tools your agents can drive

Managing nineteen accounts meant picking tools that didn't need a human in every loop. Our first attempt was CDK — TypeScript-native, same language as our application code. My initial thinking was that infrastructure is code, it's just code, that'll be easy. It's not really that easy. As we added clients, the accounts started to drift out of sync. Deployments took forever. Retries got complicated when one account update succeeded and another failed. The tooling we were using just wasn't really up to the job.

So I started looking around. Pulumi solved the parts that were burning us — reliable deployment from code, configuration that varied per-client without forking the codebase. Pulumi had already shipped Neo and an MCP server when most vendors were still figuring out their AI story; they were clearly betting on agents. That's the kind of partner I was looking for. Neo picked up our infrastructure on day one. One of my colleagues put it: "The scary thing about Neo is it just seems to know everything about what we do."

What kept us going wasn't any one feature. It was that the pieces composed — IaC, ESC, Neo, Pulumi Cloud all built on top of each other as primitives, and the benefits compounded across the stack. We picked one piece for the agentic mindset, and the next piece was already in the box.

**Tools have to share your AI-first mindset. If they don't integrate deeply, the human becomes the glue.** If part of your stack still requires a human to click through a web UI to provision an account, your agents stop there.

## 4. Don't let one agent do everything

The first thing you reach for when you start automating with agents is a god prompt — one big prompt that defines your whole software factory, with one agent turned loose on the work. It doesn't work. The agents that write the code aren't the best at checking their own homework. They're lenient on themselves.

So we don't run one agent. We run a constellation of them, each with a narrow job. One agent reviews the backlog and flags under-specified tickets. Another writes the application code. Neo writes the infrastructure — when an agent hits an infra task, AGENTS.md tells it to delegate to Neo via Pulumi's MCP server. Then four or five checker agents go over the PR from different angles — performance, correctness, security. They're running on smaller models than the writers, and you know what? They always find something.

**Don't let any agent mark its own homework.** Specialization compounds. The checkers are cheap, they each look for one thing, and a narrow job means a narrow context window. Infrastructure alone can fill an agent's context — give it the whole job and there's no room left to think.

## 5. Measure human hours per unit of value

Once the agents are producing code, the bottleneck moves to the humans around them — PR review, per-client rollouts, anyone who has to approve the work before it ships. The metric I use now is human hours per unit of value produced. Look at every step and ask what you can automate; if you can't, ask why not. The pattern we've ended up with is humans at the start, writing the specs and choosing the work that matters; humans at the end, doing the final pre-production check; agents in between.

The mechanism that keeps the humans out of the middle is configuration. We hold all of it in ESC (Pulumi's config and secrets layer), and ESC environments inherit from each other — a base layer for the platform, a layer for staging vs. production, per-client overrides as small diffs on top. When something needs to change across all nineteen clients, we update one base environment and run `pulumi up`, or hand it off to Neo to redeploy every stack. One change, nineteen clients updated — not nineteen tickets and three meetings. If you're managing config sprawl across environments, ESC is where I'd start.

**Measure human hours per unit of value. Treat every one as a bottleneck to remove.** Engineers writing or reviewing routine code is an unacceptable bottleneck. Each one you remove gives the agents another order of magnitude.

## 6. Design for convergence, not one-shot correctness

Agents don't get the answer right the first time. They drift. They go off-topic, work in areas they're not supposed to. As strong as the models are, you're not shipping the first thing they produce.

The trick is that it doesn't matter how many tries it takes, as long as no human is in the loop. We run our pipeline as a convergence machine: each iteration goes back through the checker agents from the last rule, the issues they find feed into the next pass, and eventually all the agents pass, all the tests pass. Total time: an overnight run.

Two things have to be true for that loop to work. You need a way to evaluate whether the output is good enough — without that, you don't know when to stop. And the loop has to actually converge: each pass has to get closer, or you'll churn forever on the same issue under different framings.

I've shipped more code in the last two years — after a stretch in leadership where I wrote almost none — than I did in the previous fifteen, all of it in languages I couldn't write by hand.

**Don't aim for one-shot correctness. Build a machine that climbs.**

## 7. Run the factory in the cloud, not on a laptop

That machine has to live somewhere. The default mental picture of AI coding is one developer in their IDE, watching Copilot autocomplete. That's not what we do. Our agents run in the cloud — the factory keeps producing while engineers are in meetings, talking to clients, or asleep. We don't sit there watching progress bars; we spend the time with clients.

Running it in the cloud isn't just about keeping it on at night. Once you've built it, the next job is to tweak it — improve quality, reduce costs, improve throughput. That's hard if it's scattered across developers' laptops. Configuration and credentials drift. The thing you're trying to optimize is in different states on different machines. It doesn't really work on-prem, on laptops, or on a Mac Mini in the corner. That's why we run on Pulumi Cloud rather than GitHub Actions — Pulumi Cloud is somewhere you can iterate on the factory itself, not just trigger it.

**Build the factory somewhere you can work on it — not just somewhere it can run.**

## Closing thought

If you're where I was two years ago: don't ask how AI fits into what you already do. Find the biggest thing a human still does by hand and take that human out of the loop. Then do it again.

The factory is built one rule at a time. Mine isn't finished — and that's the point.

## Why Pulumi — in my own words

A few notes on why I chose Pulumi as the foundation.

> *"Pulumi was an ecosystem, not just a product. The primitives worked well together, they composed well together, and the benefits compounded across the stack. Choosing Pulumi was one of the better decisions we made along the way. It made our lives easier."*

> *"I don't actually care if it's HCL or TypeScript, as long as my software development agents can write it. And they do a better job with TypeScript than HCL."*

> *"One of my colleagues said the scary thing about Neo is that it just seems to know everything about what we do. But that's because it sits at the center of our infrastructure. We can ask it a question, and it will go away and find the answer."*

> *"The close integration between ESC and Pulumi stacks was really crucial for us. Neo understood all of it as part of one platform, and that made things much easier. We have five engineers on the team, and I can't really imagine managing this level of complexity without the tools we have now."*

---

*Watch the original Pulumi webinar (TBD: link). Learn more about [Compostable AI](https://compostable.ai/) and [Pulumi Neo](https://www.pulumi.com/product/neo/).*
