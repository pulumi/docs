---
title: "Seven Rules for Building an AI-First Software Factory"
date: 2026-05-07
draft: true
meta_desc: "Ewan Dawson, CTO of Compostable AI, on building a software factory where AI agents write the code. Seven rules learned across nineteen client deployments."
meta_image: meta.png
feature_image: feature.png
youtube_id: oHNdlWlsR-w
authors:
    - ewan-dawson
    - adam-gordon-bell
author_roles:
    adam-gordon-bell: "as told to"
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
        Ewan Dawson runs a five-person software factory at Compostable AI. Most of the code it ships, he hasn't read.

        The agents do the writing. The team handles what the agents can't: defining the work, talking to the customers, deciding what gets built. The factory keeps producing whether the engineers are at their desks or not.

        In a recent Pulumi webinar, Ewan walked through the rules in brief. The blog post is the expanded version. For anyone trying to figure out how to set their team up for what's happening in software now.
    bluesky: |
        Five engineers. Nineteen clients. Custom code shipped within a day of signing.

        Ewan Dawson's seven rules for an AI-first software factory — where agents write nearly all the code.
---

*Ewan Dawson is CTO of [Compostable AI](https://compostable.ai/), where five engineers run an AI-first software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. This article is adapted from his recent Pulumi webinar, and covers rules in more depth then we had time for on stage.*

<!--more-->

I used to think writing code was the main job. Now most of my job is managing the system that writes the code.

Most of the code Compostable ships now, I haven't personally read. The agents are not just autocomplete anymore. They take tickets, write code, and make mistakes that need review. These are the seven rules I've built around them. The tools keep changing, but these are the rules we keep coming back to.

## 1. Transform, don't enhance

A few years ago, before I started Compostable, I was working at a large multinational when [GitHub Copilot](https://github.com/features/copilot) first came out. Everyone got excited. It was a ChatGPT moment for software development, and the first time I tried it, I was blown away. This is going to change things, I thought.

But getting it into the hands of engineers at that company turned into an uphill fight with the Governance, Risk, and Compliance team. Copyright, security, compliance. The concerns were reasonable. They also added up. We were trying to drop a future-of-software-development tool into a process designed for none of that. By the time we'd negotiated a limited trial, I'd already worked out that whatever this technology was going to become, it wasn't going to become it inside a big enterprise first. Startups would. So I left and started one.

When we built Compostable, we were deliberate about it. I wasn't bolting agents onto a process I already knew. I was trying to figure out what the process should look like if AI did most of the writing from day one.

{{< notes type="tip" >}}
**Don't bolt AI onto your existing workflow. Redesign the workflow around what agents can do.**

Most of the leverage in this technology comes from rebuilding around it. The tool change is the small part.
{{< /notes >}}

## 2. Remove the problem, don't solve it

As we were building Compostable, one of the first problems was a version of the same risk I'd faced at my previous company. Our buyers are large enterprises in regulated industries. They worry about AI risk a lot. "We share a sandbox with the other clients" is not something anyone wants to hear.

If the agents were going to write code that touched production, blast radius wasn't a hypothetical: one bad agent run could trash a customer's database, or leak one client's data into another's. The obvious move was to build a multi-tenant sandbox: guardrails, approvals, rollback. Every version we tried still had agents loose in a shared environment, one bug away from making one customer's data visible to another.

So we didn't build the sandbox. We gave every client their own AWS account instead. Nineteen accounts now, one per client, each with its own digital-twin staging environment. Agents iterate on staging until the work is verified, and only then does it ship to production. The AWS account itself is the security boundary, and Amazon has spent twenty years getting that boundary right. We layered automated guardrails on top, and got ISO 27001 certified in six weeks because most of the work was already done.

We didn't make the multi-tenant problem go away. We *shifted* it: instead of securing a shared environment, we now manage a fleet of accounts. That's a problem with twenty years of well-trodden answers.

{{< notes type="tip" >}}
**Remove the problem before you try to solve it.**

Easier to manage a fleet of accounts than to secure a shared environment. Easier to reframe the problem than to engineer your way through it.
{{< /notes >}}

## 3. Pick tools your agents can drive

Our first attempt at running the fleet was [CDK](https://aws.amazon.com/cdk/), TypeScript-native, the same language as our application code. My initial thinking was that infrastructure is code, it's just code, that'd be straightforward. It wasn't. As we added clients, the accounts started to drift out of sync. Deployments took forever. Retries got complicated when one account update succeeded and another failed. The tooling we were using wasn't up to the job. We needed something that didn't put a human in every deploy loop.

I went looking for something better. Pulumi solved the parts that were burning us: reliable deployment from code, configuration that varied per-client without forking the codebase. Pulumi had already shipped [Neo](/product/neo/) and an MCP server when most vendors were still figuring out their AI story. They were clearly betting on agents. That's the kind of partner I was looking for. Neo picked up our infrastructure on day one. One of my colleagues put it: "The scary thing about Neo is it just seems to know everything about what we do."

> *"I don't actually care if it's HCL or TypeScript, as long as my software development agents can write it. And they do a better job with TypeScript than HCL."*
>
> *— Ewan Dawson*

What kept us going wasn't any one feature. It was that the pieces fit together. Pulumi IaC, [Pulumi ESC](/docs/pulumi-cloud/esc/), Neo, and [Pulumi Cloud](/docs/pulumi-cloud/) all built on top of each other, and we got benefits across the stack. We picked Pulumi because it fit our agents. The other pieces, the ESC, Neo, the Cloud, came along with it.

{{< notes type="tip" >}}
**Tools have to share your AI-first mindset. If they don't integrate deeply, the human becomes the glue.**

If part of your stack still requires a human to click through a web UI to provision an account, your agents stop there.
{{< /notes >}}

## 4. Don't let one agent do everything

Earlier, before the infrastructure story was sorted, we'd been wiring agents into the rest of the development flow. The move I reached for was a god prompt: one big system prompt that defined the whole software factory, with one agent turned loose on the work. It didn't work. The agents that write the code aren't the best at checking their own homework. They're lenient on themselves.

So we don't run one agent. We run a constellation of them, each with a narrow job. One agent reviews the backlog and flags under-specified tickets, adding context the original ticket missed. Another writes the application code. Neo writes the infrastructure. When an agent hits an infra task, [AGENTS.md](https://agents.md/) tells it to delegate to Neo via Pulumi's MCP server. Once a PR is up, four or five checkers go at it. One looks at correctness, another at performance, another at security. One walks the tests, looking for paths the writer skipped. They're running on smaller models than the writer, and you know what? They always find something.

{{< notes type="tip" >}}
**Don't let any agent mark its own homework. Specialize by job — a narrow job means a narrow context window.**

The checkers are cheap, they each look for one thing, and the writers don't have to leave room for self-criticism. Infrastructure alone can fill an agent's context. Give one agent the whole job and there's no room left to think.
{{< /notes >}}

## 5. Measure human hours per unit of value

Once we had agents writing and agents reviewing, throughput went up. Not by the order of magnitude we'd hoped, though. The bottleneck had moved past the PR (which the constellation now handled) to the work surrounding it. Configuration changes that needed to land across nineteen clients. Approvals before anything could ship to production. Per-client rollouts. All of those still ran through a person, and they added up.

The metric I use now is human hours per unit of value produced. Look at every step. Anything that doesn't have to go through a person, automate. Humans write the specs at the start, and do the final pre-production check. Agents do the rest.

The mechanism that keeps the humans out of the middle is configuration. We hold all of it in ESC, and ESC environments inherit from each other: a base layer for the platform, a layer for staging vs. production, per-client overrides as small diffs on top. When something needs to change across all nineteen clients, we update one base environment and run `pulumi up`, or hand it off to Neo to redeploy every stack. One base change updates all nineteen. It used to be a ticket per client and three meetings. If you're managing config sprawl across environments, ESC is where I'd start.

{{< notes type="tip" >}}
**Measure human hours per unit of value. Treat every one as a bottleneck to remove.**

Engineers writing or reviewing routine code is a bottleneck you can't afford. Every one you remove gives the agents more room to run.
{{< /notes >}}

## 6. Design for convergence, not one-shot correctness

Even with multiple agents writing and reviewing each other's work, the first pass was rarely the keeper. Agents drift. They go off-topic, work in areas they're not supposed to. As strong as the models are, you're not shipping the first thing they produce.

The trick is that it doesn't matter how many tries it takes, as long as no human is in the loop. The pipeline iterates on its own. Each pass goes back through the checker agents from the last rule, the issues they find feed the next pass, and the loop only stops when the checks all pass. Total time: an overnight run.

What that looks like: the constellation from the last rule runs the cycle. The checkers' comments feed the next round, the coding agent picks them up and revises. It keeps going until the checks pass, the tests pass, and the guardrails are green. By the end, you've gone from ticket to merged PR with no human in the middle.

Two things have to be true for that loop to work. You need a way to evaluate whether the output is good enough. Without that, you don't know when to stop. And the loop has to actually converge. Each pass has to get closer. A checker that fails every PR for a different reason isn't helping. It just keeps the work going in circles. The coding agent has to be able to act on the feedback, and the feedback has to be specific enough that "fix this" narrows the search rather than widening it.

Once it converges, the question moves on: how cheap can we make it? Fewer iterations. Smaller models on the checker side. Better prompts so the coding agent lands closer on the first try. The optimization never really ends.

{{< notes type="tip" >}}
**Don't aim for one-shot correctness. Design for convergence.**

It doesn't matter how many tries it takes, as long as the loop closes without a human in it. Get convergence first. The optimization comes after.
{{< /notes >}}

## 7. Run the factory in the cloud, not on a laptop

A factory like this has to live somewhere. Once it does, the question becomes where you can actually work on it. When people picture AI coding, they picture one developer in their IDE, watching Copilot autocomplete. That's not what we do. Our agents run in the cloud. The factory keeps producing whether engineers are in meetings, talking to clients, or asleep. Nobody on the team is watching progress bars. The engineers spend that time with clients.

What does "time with clients" actually mean? It's the part of the job that's become more important since the agents arrived. Engineers spend less time at keyboards and more time understanding what customers need. Writing the requirements down in language the agents can act on. Reviewing the spec before any code starts. Given/when/then, BDD-style. The factory runs while the engineers do the work a model still can't do for them.

Running it in the cloud isn't just about keeping it on at night. Once you've built it, the next job is to tweak it: improve quality, reduce costs, improve throughput. That's hard if the factory is scattered across developers' laptops. Configuration and credentials drift between machines. The same prompts run against different model versions. The same env vars get half-set on half the laptops. The thing you're trying to optimize lives in different states across the team.

We keep everything in the cloud. AWS, Pulumi Cloud, GitHub, and so on. But the specific stacks matter less than the principle. On-prem, on laptops, or on a Mac Mini in the corner. Those work fine for running it. They don't work for a team trying to improve it.

{{< notes type="tip" >}}
**Build the factory somewhere you can work on it — not just somewhere it can run.**

Cloud isn't just about keeping it on at night. It's about having one place where a whole team can iterate on the factory together.
{{< /notes >}}

## Closing thought

I've shipped more code in the last two years than I did in the fifteen before that. Most of it in languages I couldn't write by hand. And that's after a stretch in leadership where I wrote almost none.

If you're where I was two years ago: don't ask how AI fits into what you already do. Find the biggest thing a human still does by hand and take that human out of the loop. Then do it again.

The factory is built one rule at a time. Mine isn't finished. That's the point.

---

*Watch the [original Pulumi webinar](https://www.youtube.com/watch?v=oHNdlWlsR-w). Learn more about [Compostable AI](https://compostable.ai/) and [Pulumi Neo](https://www.pulumi.com/product/neo/).*
