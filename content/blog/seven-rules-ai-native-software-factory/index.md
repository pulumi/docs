---
title: "Seven Rules for Building an AI-Native Software Factory"
date: 2026-05-07
draft: false
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

        Ewan Dawson's seven rules for an AI-native software factory — where agents write nearly all the code.
---

*Ewan Dawson is CTO of [Compostable AI](https://compostable.ai/), where five engineers run an AI-native software factory: nineteen clients, custom AWS deployments, most of them shipped within a day of contract signing. This article is adapted from his recent Pulumi webinar, and covers rules in more depth than we had time for on stage.*

<!--more-->

For the past twenty years, I've viewed software development as a craft. The best engineers drew on decades of experience to get every function right.

But two years into the agentic AI revolution, I realised software is going to look more like a factory than a craft. The economics have changed. We can't treat code as bespoke anymore. To scale, we have to think industrial — use the tools to ship more value with fewer engineers.

I joined Compostable AI soon after it was founded 2.5 years ago, and I built the engineering org AI-native from day one. The technology has come a long way since then, and so has my understanding of what AI-native actually means. Here are seven rules I keep coming back to.

## 1. Transform, don't enhance

<img src="rule-1-chrysalis.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Going AI-native isn't an upgrade to your existing process. If you treat AI as a way to hand your developers smarter tools, you leave most of the value on the table. You get the leverage by rebuilding how you write software — and the culture and processes around it.

I know that's a tall order for a large, mature engineering org. My advice: start small. Pick one team or one business area and run it as a fully AI-native function. Take what you learn and roll it out from there. And do the political work early, especially with your Governance, Risk, and Compliance function. Get GRC on your side early. Otherwise AI becomes a compliance fight instead of a structural advantage.

{{< notes type="tip" size="large" >}}
**Don't bolt AI onto your existing workflow. Redesign the workflow around what agents can do.**

Most of the leverage in this technology comes from rebuilding around it. The tool change is the small part.
{{< /notes >}}

## 2. Remove the problem, don't solve it

<img src="rule-2-knot.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

Going AI-native flips which problems are hard and which are easy. The right move often isn't to engineer a solution. It's to reframe the problem so it goes away.

Here's an example. Serving multiple clients with agents writing the code, blast radius wasn't a hypothetical. One bad agent run could trash a customer's database, or leak one client's data into another's. Our instinct was to build a secure multi-tenant sandbox with guardrails, approvals, rollback. But every version we tried still had agents loose in a shared environment, one bug away from making one customer's data visible to another's. So we removed the problem: every client gets two dedicated AWS accounts, one for production and one "digital twin" staging account. Agents iterate on staging until the work checks out. Only then does it ship to production. We have nineteen accounts now, one per client.

Managing nineteen AWS accounts with five engineers used to be an administrative nightmare. When code is cheap, infrastructure-as-code tools like AWS Control Tower and Pulumi make it the easier path.

{{< notes type="tip" size="large" >}}
**Remove the problem before you try to solve it.**

It's cheaper to reframe the problem than to engineer your way through it.
{{< /notes >}}

## 3. Pick tools your agents can drive

<img src="rule-3-wrench.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Removing problems is the process side. The other side is tooling. If you want an automated factory, your tech stack has to be something agents can drive. This overlaps a lot with tools that have great developer experience. If a tool has a robust API plus a clean CLI, agents can drive it. If it's heavy click-ops around a web UI, agents stop there.

We didn't get there first try. Our first IaC tool worked fine when we had a couple of clients. As we added more, accounts drifted, deployments slowed, retries got complicated. We needed something built for where we were heading.

I went looking, and [Pulumi](/) fit. We express infrastructure as type-safe code — TypeScript, in our case, rather than HCL — and agents are good at writing it. Pair that with [Pulumi Neo](/product/neo/) — pre-loaded with domain-specific Pulumi skills — and we ship infrastructure that follows best practices. One of my colleagues put it: "The scary thing about Neo is it just seems to know everything about what we do." Pulumi IaC plus [Pulumi ESC](/docs/pulumi-cloud/esc/) for configuration beats stitching tools together. And TypeScript lets us build higher-level abstractions that keep the AWS account fleet tractable.

{{< pullquote >}}
"I don't actually care if it's HCL or TypeScript, as long as my software development agents can write it. And they do a better job with TypeScript than HCL."
{{< /pullquote >}}

{{< notes type="tip" size="large" >}}
**Tools have to share your AI-native mindset. If they don't integrate deeply, the human becomes the glue.**

If part of your stack still requires a human to click through a web UI to provision an account, your agents stop there.
{{< /notes >}}

## 4. Don't let one agent do everything

<img src="rule-4-constellation.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

When I first started with agents, I reached for a god prompt: one massive system prompt meant to guide a single agent through the whole software lifecycle. It didn't work. Agents struggle when you give them multiple goals. The writer is lenient on its own work — it won't catch what it just shipped. You don't want it reviewing the code, checking for security flaws, or hunting bugs.

We get better results from a constellation of specialized agents, each handling one part of the line. Pulumi Neo handles infrastructure. Alongside it sit agents specialized in:

* Code implementation
* Code review and testing
* Security auditing
* Internal standards compliance
* Documentation updates

Tasks pass down the line. Clean code comes out the other end, with almost no human involved.

{{< notes type="tip" size="large" >}}
**Don't let any agent mark its own homework. Specialize by job.**

Treat agents the way you'd treat a team. The one who writes the code shouldn't be the one signing it off.
{{< /notes >}}

## 5. Measure human hours per unit of value

<img src="rule-5-hourglass.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Once we had agents writing and agents reviewing, throughput went up — but the bottleneck moved past the PR. Engineering hours were still the most expensive thing in the building, so my core metric is human hours per unit of value produced. Minimize that.

That means hunting for every step that still goes through a person — especially the mid-pipeline steps between ideation and production. Automate the human touchpoints along that line, and the factory runs 24/7.

Pushing automation this hard also forces good engineering. A chaotic, undocumented process is impossible to automate. Good engineering is still good engineering, AI or not. Agents won't fix a weak process.

{{< notes type="tip" size="large" >}}
**Measure human hours per unit of value. Treat every one as a bottleneck to remove.**

You can't automate what you can't describe. Every human in the pipeline marks a piece that hasn't been described yet.
{{< /notes >}}

## 6. Design for convergence, not one-shot correctness

<img src="rule-6-spiral.png" alt="" class="float-left w-32 mr-4 mb-2 mt-1 rounded-lg sm:w-40 sm:mr-6 lg:w-44">

Even with the human touchpoints removed, the agents don't ship right the first try. Once you embrace the factory pipeline, you stop needing them to. We design for convergence instead — a system that lands on the right answer through automated iteration.

The loop we run looks like this:

1. **Refinement:** agents iterate on the Product Requirements Document until the problem is clear.
2. **Planning:** agents draft multiple technical approaches, and evaluation agents pick the best one.
3. **Implementation:** coding agents write the software.
4. **Review:** specialized checking agents look for bugs, API misuse, and security flaws.

If the checkers find a problem, they hand it back to the implementation agent. The loop repeats until the tests pass and the agents agree on a clean PR. Once it converges, we merge and deploy to staging.

Two things have to be true. You need a way to evaluate the output. Without that, you don't know when to stop. And the loop has to converge — each pass has to get closer. A checker that fails every PR for a different reason isn't helping — it just keeps the work going in circles. The feedback has to narrow the search, not widen it.

Once it converges, the question moves on. How cheap can we make it? Lower the time to PR, reduce token count, drop the overall cost. The optimization never really ends.

{{< notes type="tip" size="large" >}}
**Don't aim for one-shot correctness. Design for convergence.**

It doesn't matter how many tries it takes, as long as the loop closes without a human in it. Get convergence first. The optimization comes after.
{{< /notes >}}

## 7. Run the factory in the cloud, not on a laptop

<img src="rule-7-cloud.png" alt="" class="float-right w-32 ml-4 mb-2 mt-1 rounded-lg sm:w-40 sm:ml-6 lg:w-44">

Even a converged factory has to live somewhere. Try running a fully automated factory on individual developers' laptops, and it falls apart. Laptops are highly trusted machines. Put autonomous agents on them and your security posture drops, fast. And the factory has to run 24/7. Events come from elsewhere — PR comments, Slack threads, errors in test environments.

Cloud also kills configuration drift across a dozen developer machines. The same prompts run against different model versions, and env vars sit half-set on half the laptops. The thing you're trying to optimize lives in different states across the team. Cloud isn't just where the factory runs; it's the only place a team can iterate on it together. Keep everything in one place — AWS, Pulumi Cloud, GitHub. The specific stack matters less than the principle of one place.

And the part that matters most: the factory keeps running, testing, and deploying long after we've closed our laptops and gone to sleep.

{{< notes type="tip" size="large" >}}
**Build the factory somewhere you can work on it — not just somewhere it can run.**

A factory scattered across laptops can't be improved as a system. Cloud keeps it in one shape, 24/7, and lets the team iterate together.
{{< /notes >}}

## Closing thought

I've shipped more code in the last two years than I did in the fifteen before that. Most of it in languages I couldn't write by hand. And that's after a stretch in leadership where I wrote almost none.

If you're where I was two years ago: don't ask how AI fits into what you already do. The factory is built one rule at a time, and it's not a template — it's the practice of finding where you're taking advantage of the new economics and where you're not, where your practices still need an update. The leverage is in finding these places and improving them.

---

*Watch the [original Pulumi webinar](https://www.youtube.com/watch?v=oHNdlWlsR-w). Learn more about [Compostable AI](https://compostable.ai/) and [Pulumi Neo](/product/neo/).*
