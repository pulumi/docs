---
title: "The Dark Factory Pattern for Infrastructure: Running Pulumi Lights-Out"
allow_long_title: true
date: 2026-05-03
draft: false
meta_desc: "What the dark factory pattern looks like when the factory floor is your Pulumi state graph, and where to start without burning down a prod account."
meta_image: meta.png
feature_image: feature.png
authors:
    - engin-diri
tags:
    - ai
    - ai-agents
    - automation
    - infrastructure-as-code
    - pulumi-neo
    - platform-engineering
social:
    twitter: |
        Stripe ships 1,300 AI-authored PRs a week. The pattern behind it has a name: the dark factory.

        What it looks like when the factory floor is your Pulumi state graph turns out to be a different problem than the application-code version.
    linkedin: |
        Manufacturing dark factories run with the lights off. No humans on the floor, just machines moving parts through the line.

        The same pattern is now showing up in software. Stripe is shipping 1,300 AI-authored pull requests a week. A HackerNoon writeup from February laid out a five-level autonomy ladder. BCG calls it the "dark software factory."

        Almost all of that material is about application code. Infrastructure is the harder problem: blast radius, drift, irreversible actions, multi-region state. The interesting question is what an end-to-end dark factory looks like when the factory floor is your stack state, and where the gates have to be tighter to keep a Saturday morning from becoming an incident.

        Here is where to start without burning down a prod account.
    bluesky: |
        Manufacturing dark factories run lights-out. Code dark factories are starting to.

        Infra is the hard one: blast radius, drift, irreversible actions. The interesting question is where the gates have to be tighter when the factory floor is your stack state.
---

The original dark factory was Fanuc's robotics plant in Japan, where the lights are off because nobody is on the floor. Robots build robots. Parts move through the line for weeks at a time without a person walking past them.

The same pattern is now showing up in software. Three engineers at StrongDM [shipped 32,000 lines of production code](https://www.strongdm.com/blog/the-strongdm-software-factory-building-software-with-ai) without writing or reviewing any of it. Stripe is reportedly generating over [1,300 AI-authored pull requests per week](https://www.mindstudio.ai/blog/what-is-a-dark-factory-ai-coding). In January, Dan Shapiro of Glowforge published [a five-level autonomy ladder](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/) that landed cleanly enough to become the shorthand most people now use, and BCG followed with a piece calling [the dark software factory](https://www.bcgplatinion.com/insights/the-dark-software-factory) the next phase of enterprise software delivery.

Almost every public writeup so far is about application code. The harder question is what this looks like for infrastructure.

<!--more-->

## What a dark factory actually is

Shapiro's ladder is the cleanest framing I've seen. He borrows it from the SAE's self-driving levels, and it fits surprisingly well:

| Level | What it is | Driving analogy |
| ----- | ---------- | --------------- |
| 0 | Spicy autocomplete | Stick shift; you do everything. |
| 1 | Coding intern (boilerplate) | Cruise control. |
| 2 | Junior developer (interactive pair) | One hand on the wheel. |
| 3 | AI writes the majority; you review every PR | Eyes still on the road. |
| 4 | Spec-driven; agent runs unattended for hours; you review later | Sleeping at the wheel, you can still wake up. |
| 5 | Dark factory; no human review of code before production | No steering wheel at all. |

Most teams are at level 2 or 3. A few of the more aggressive ones are at 4. Level 5 is the experiment. The interesting design question is what has to be true for level 5 to be safe, and that question gets sharper when the thing being shipped is infrastructure.

A dark factory is not a coding harness. A harness is the framework an agent runs inside; the dark factory is the surrounding system that makes a harness's output mergeable without a human reading the diff. Copilot and Cursor sit at the other end: interactive, the human stays in the loop on every keystroke. The dark factory takes the human out of the per-change loop entirely and puts them at the top, writing the spec and the acceptance criteria.

## The wall between generator and validator

Strip the dark factory down to its layers and there are four of them.

```mermaid
flowchart LR
    A[Inputs<br/>Humans] --> B[Code Generation<br/>Autonomous]
    B --> C[Validation<br/>Autonomous, isolated]
    C -->|pass| D[Merge & Deploy<br/>Autonomous + existing CI/CD]
    C -->|fail| B
    A -.->|holdout scenarios<br/>generator never sees these| C
```

The single most important rule is that Code Generation and Validation must be completely isolated. The generator never sees the acceptance scenarios. A separate evaluator does, and it judges the generator's output against scenarios the generator could not have memorized.

The reason is sycophancy. LLMs are too eager to agree with their own prior turns and too willing to declare victory on something they just produced. Without isolation, the same model that wrote the change is the one telling you it's fine. As StrongDM put it, a test that lives in the codebase can be lazily rewritten to match the code. It isn't malice; it's the agent doing exactly what it was asked, badly. The wall is what stops that.

StrongDM's pattern for this is **holdout scenarios**: plain-English BDD acceptance tests stored where the generator cannot reach them. Each scenario runs three times against an ephemeral deployment, two of three must pass, and the overall pass rate has to clear 90% before the change moves forward. If the generator fails, it gets a one-line failure message ("SQL Injection Detection failed: endpoint returned 500"), not the scenario text. It cannot game the test.

Without that wall, you don't have a quality gate. You have theater.

## Why infrastructure is the harder version

Application code factories can lean on tests, linters, and type checkers. Infrastructure adds blast radius, drift, secrets, irreversible actions, and multi-region state. A code dark factory shipping a broken UI causes a bad user experience. An infrastructure dark factory shipping a broken IAM policy ends in a postmortem.

A few things make this manageable on Pulumi specifically.

The orchestrator does not need to be invented. The [Pulumi Automation API](/automation/) is the engine as an SDK in Python, TypeScript, Go, .NET, Java, or YAML, which is the same surface a dark factory orchestrator runs on. Credentials don't have to be long-lived: [ESC and OIDC](/docs/esc/) issue short-lived ones per run, so the agent never sees a static secret. Policy doesn't have to be probabilistic: [CrossGuard](/docs/iac/using-pulumi/crossguard/) enforces deterministic rules at preview time. Execution doesn't have to happen on a laptop: [Pulumi Cloud Deployments](/docs/pulumi-cloud/deployments/) runs `pulumi up` inside a governed runner with audit logs and approval rules already wired. And the reasoning layer doesn't have to start from scratch: [Pulumi Neo](/product/neo/) is grounded in your state graph and ships with three modes (Auto, Balanced, Review) that line up cleanly with Shapiro's levels 5, 4, and 3.

That doesn't make Pulumi a dark factory by itself. It means the parts that an application-code factory has to build from scratch are pieces a Pulumi shop already has: a credential broker, a policy engine, a governed runner, a state-aware reasoning layer, an audit trail.

There's one more piece worth calling out, because it's the part nobody talks about. `pulumi preview` is structurally a holdout. It produces a deterministic diff that CrossGuard evaluates without ever seeing the conversation that produced the program. The diff is the holdout artifact, the policy pack is the validator, and they meet without context bleed. For infrastructure, half the wall is already built.

The interesting work is the part that nobody ships in a box.

## The interesting work

What no platform ships for you is the wall: the holdout scenarios for infrastructure, the isolated evaluator that runs them, and the agreement on which stacks are even allowed to run lights-out.

The orchestrator itself is small. It pulls a spec, runs `preview`, hands the preview to an isolated evaluator (with its own credentials and its own access to the cloud, no access to the generator's prompt or output), and branches on the verdict. Auto mode runs `up` immediately. Balanced mode submits a deployment that requires approval. Review mode opens a PR for a human. Every branch records a stack version traceable in the audit log. Twenty lines of glue, give or take.

The wall is the part that takes a week to get right. You write five plain-English scenarios for one stack ("after `pulumi up`, the bucket is private, has SSE-KMS, lives in eu-west-1, and is tagged `owner=team-x`") and a janky evaluator that runs `preview` and `up` against an ephemeral copy, queries the cloud, and asks a separate model whether the resulting state satisfies the scenario. Triple-run, 90% pass gate. Then you watch it for a few weeks before you let anything auto-apply.

## A four-phase rollout

This is the same path StrongDM walked for application code, with the gates tightened.

### Phase 1: better context, this afternoon

Write an `AGENTS.md` for your most active stack repo. Pulumi Neo [reads it natively](/blog/pulumi-neo-now-supports-agentsmd/), as do most coding agents. While you're there, look at your CrossGuard rules and rewrite the error messages as instructions. Not "S3 bucket has no encryption" but "S3 bucket has no encryption. Set `serverSideEncryptionConfiguration` with SSE-KMS to fix." That single change is the difference between an agent flailing and an agent fixing the policy violation on the first try. Wire `pulumi preview` as a build-before-push gate so PRs don't show up just to fail CI.

### Phase 2: spec-driven with holdouts, this week

Pick one stack with a small blast radius. A review-stack lifecycle is ideal. Write five plain-English holdout scenarios for it and the janky evaluator above. Humans still approve every PR. Don't auto-merge yet. You're earning the data, not declaring trust.

### Phase 3: take the human out of the merge

Only after StrongDM's three measurable gates hold over twenty PRs (scenario pass rate above 90%, false positive rate below 5%, human override rate below 10%) flip auto-apply on for that one stack. Add a weekly drift sweep that goes through the same scenario gate as everything else.

### Phase 4: lights out

Expand the auto-apply flag to every stack with strong scenario numbers. Wire your issue tracker so tickets tagged `infra:fix` flow through the pipeline. Mock the cloud APIs that are slow or flaky enough to make scenario evaluation expensive. At this point the orchestrator is configuration, not architecture.

## What could go wrong

The validator approves a bad change. This is the obvious one. The mitigation is the one StrongDM uses: triple-run with a 2-of-3 threshold, a 90% gate over the run set, a human audit of the first fifty auto-applied changes, and your existing policies still run after the validator says yes.

The agent gets a destroy permission it shouldn't have. There's a class of operations that should not sit in the autonomous loop yet: dropping a database, deleting a hosted zone, rotating a root key, anything that crosses a regulated data boundary. Scope what each agent identity can do at the credential layer, require human approval for anything destructive, and start every stack at Review mode. Tag changes, security-group adjustments, and instance resizes can run autonomously today. Release-branch cuts and config promotions can probably run by next quarter. The destructive class earns its way in over months.

You need all three of those layers. Approvals without policy means anything a human approves in a hurry ships. Policy without approvals means a sufficiently clever spec eventually finds the gap. Both without a human kill switch means an incident at 3 a.m. has nobody to escalate to.

Costs blow up. Cap retries at three per spec, alert on token spend per run, and remember that StrongDM reported roughly $1,000 per day per engineer-equivalent. That's still cheaper than a salary, but only if you put the cap in place before you find out.

## Where to start

Most of what a dark factory needs already exists in any reasonably mature platform. Whatever you have for state, policy, credentials, audit, and a deployment runner is the substrate. The interesting work is not building the factory. It's the wall: the holdout scenarios that make the gap between "the model says it's fine" and "the system is actually fine" mean something.

Write an `AGENTS.md` and five holdout scenarios for one stack this week. That's enough to get a real signal on whether the pattern fits your team. The rest is the same problem the application-code factories have already worked through, with the gates set tighter.
