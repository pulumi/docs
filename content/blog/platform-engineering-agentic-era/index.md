---
title: "Platform Engineering in the Agentic Era: When Agents Provision"
date: 2026-08-27
draft: false
meta_desc: "How platform teams give AI agents identity, policy, and audit trails to provision infrastructure safely, without a human in every loop."
authors:
    - pulumi-content-team
tags:
    - platform-engineering
    - ai-agents
    - agentic-infrastructure
    - infrastructure-as-code
    - policy-as-code
category: general
faq_schema: true

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Gartner expects 40% of enterprise apps to carry a task-specific AI agent by the end of 2026. Most platform engineering advice still assumes the thing calling your APIs is a person.

        What changes when it isn't:
    linkedin: |
        Most platform engineering writing about AI agents stops at "agents will use your internal developer platform too." True, but it undersells the change. A developer reading your documentation and an agent calling your API for a golden path are different problems, because one of them can act at machine speed with no one watching the diff scroll by.

        We wrote up the operational questions a platform team actually has to answer once an agent starts provisioning infrastructure through the platform instead of only reading it, and what changes about identity, policy, review, and audit when the thing asking can already have acted by the time you notice.
    bluesky: |
        Gartner: 40% of enterprise apps will carry a task-specific AI agent by end of 2026. Platform engineering advice hasn't caught up — most of it still assumes a human is reading the catalog, not an agent calling the API.

        Here's what actually has to change:
---

Platform engineering in the agentic era means designing your internal developer platform for a caller that can act on its own judgment at machine speed, not only for a person reading documentation. The platform's job shifts from making self-service pleasant to making it safe by construction: scoped identity, policy that evaluates before a change lands, and an audit trail that holds up when no human clicked approve.

<!--more-->

Platform engineering's founding problem was human self-service: give a developer a golden path so a new environment or datastore doesn't require filing a ticket and waiting on the platform team to hand-provision it. The industry has a playbook for that one. The one arriving now is that the requester on the other end of that golden path is increasingly an agent, not a developer typing a request between meetings. App teams shipping with Claude Code, Codex, Cursor, and similar tools generate infrastructure requests at whatever pace the agent can propose changes, and that pace does not resemble the trickle of tickets a platform team used to plan around. The demand curve changed shape, and it's now the platform team's problem to absorb.

Most of what's been written about AI agents and platform engineering stops at the observation that agents are becoming platform users too. That's true, and it's not new anymore. [What Is Platform Engineering?](/what-is/what-is-platform-engineering/) already treats agents as a platform consumer alongside human developers, [What Is an Internal Developer Platform?](/what-is/what-is-an-internal-developer-platform/) covers how IDPs expose themselves to agents via MCP, and [Red Hat made the same point](https://www.redhat.com/en/blog/why-developer-portals-matter-more-age-ai-agents) about developer portals. What none of that writing does is stay long enough to answer the harder question: what does a platform actually have to provide once the agent moves from reading the catalog for context to calling it to make a change? This post is about that gap, and it stays specific to the case where the caller writes.

That question stopped being hypothetical for us a while back. In [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/), we described the coding agents (Claude Code, Codex, Cursor, OpenCode, and others) already showing up as platform users in their own right, each of which can now sign up for its own [Pulumi agent account](/docs/administration/concepts/agent-accounts/) (currently in preview) and provision directly, no human signup step required. The identity, policy, and audit questions below aren't a thought exercise; they're what a platform team runs into the first time one of those agents makes a real API call.

## What changes when AI agents become your platform's primary users?

An agent that reads your platform's documentation to answer a question and an agent that calls your platform's API to provision a database are different problems wearing the same name. The first needs accurate, well-structured context. The second needs an identity, a scope of what it's allowed to touch, a policy check before the change lands, and a record of what it did, because it can act faster than any human review cycle was built to catch.

### Reading the platform versus writing to it

| | Agent reads the platform | Agent writes to the platform |
| --- | --- | --- |
| What it needs | Accurate docs, a well-indexed catalog, MCP or similar structured context | A scoped identity, an API or code path it can call, a policy gate |
| What breaks if it's wrong | A bad answer, caught by the next question | A live change to real infrastructure, possibly before anyone notices |
| Who's accountable | The platform team, for the quality of the context | The platform team, for the guardrails around the action |
| Where it shows up in this writing | Red Hat's developer-portal piece, our own [what-is](/what-is/what-is-an-internal-developer-platform/) pages | This post |

The [agent-sprawl piece we published in April](/blog/agent-sprawl-iac-platform-is-the-answer/) argued that IaC is the natural substrate for governing what an agent can touch, and named seven things an agent needs from a platform: a trustworthy context lake, pre-cleared integrations, governed actions, deterministic policy, an audit trail, a review process, and human-in-the-loop approval where it still matters. That list is the right shape. The rest of this post works through how a platform team actually builds each piece.

## How do you give an AI agent permission to provision infrastructure?

An agent needs its own identity, not a shared service account and not a human's borrowed credentials, because both of those make it impossible to answer "who did this" later. That identity should be short-lived, scoped to a specific environment and action set, and issued the same way you'd issue credentials to a CI pipeline: through a secrets and configuration system the agent authenticates against per run, not a static key sitting in a config file.

### The identity questions a platform team has to answer

* **Whose identity does the agent act under** — its own service identity, or a human's identity it's delegated to act on behalf of? Delegation is easier to bootstrap and harder to audit; a dedicated agent identity is more work upfront and cleaner in the audit trail.
* **How long does a credential live?** A credential scoped to one provisioning run and revoked afterward bounds the damage of a compromised or confused agent in a way a long-lived key never will.
* **What's the scope per environment?** An agent cleared to provision in a sandbox account should not hold the same credential in production; the platform should mint different-scoped credentials per environment, not one credential the agent self-restricts.
* **Where does the credential come from?** [Pulumi ESC](/product/secrets-management/) is built for exactly this: dynamic, short-lived credentials pulled at the moment of use and never written to disk, whether the caller is a human, a CI job, or an agent.

{{< pullquote attribution="Luca Galante, Managing Director & Senior Analyst, Weave Intelligence" >}}
AI agents will graduate from experimental tools to first-class platform citizens. By 2026, mature platforms will treat agents like any other user persona, complete with RBAC permissions, resource quotas, and governance policies.
{{< /pullquote >}}

Galante's [2026 predictions for platformengineering.org](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026) put a name to what's already true operationally: an agent is a user persona, and it needs the RBAC, quotas, and golden paths any other persona gets, not a bespoke exception bolted on because it happens to be software.

## How does policy as code protect agent-driven self-service?

Policy as code matters more for agents than for human developers, because a human who's about to do something expensive has a moment to reconsider, and an agent doesn't pause unless the platform makes it. Policy that runs as a gate on every change, not a manual review step someone has to remember to run, is what makes agent-driven self-service safe to leave switched on.

### Where policy evaluates in an agent's loop

| Stage | What it catches | Who or what runs it |
| --- | --- | --- |
| Authoring time | Malformed resource shapes, missing required fields | IDE or agent tooling, before a change is even proposed |
| Preview | The actual diff of what will change, resources added or destroyed | `pulumi preview`, read by the agent or a human before applying |
| Pre-deploy policy gate | Violations of org rules: no public S3 buckets, required tags, allowed regions, cost ceilings | [Policy as code](/docs/insights/policy/), evaluated automatically and blocking the apply if it fails |
| Post-deploy scan | Drift, or a resource that slipped through some other path | Continuous [policy and inventory scanning](/docs/insights/policy/policy-findings/) across the whole estate |

A pre-deploy gate is the one that matters most for an unattended agent, because it's the only stage that can stop a bad change before it becomes one, rather than reporting it after the fact. Deterministic policy, evaluated the same way every time regardless of who or what proposed the change, is what lets a platform team say yes to agent self-service without reviewing every request by hand.

## Do guardrails need to account for the agent being manipulated, not just misconfigured?

Identity and policy answer what an agent is authorized to touch. A separate question is whether the agent can be talked into asking for something it was never supposed to request in the first place, a class of attack generally called prompt injection: a malicious instruction buried in a ticket, a dependency's README, or a document the agent reads mid-task can steer an otherwise well-behaved agent toward a bad request. The identity and policy gates above still contain the outcome, since a scoped credential limits the blast radius and a policy gate blocks the specific violation regardless of why the agent asked, but a platform team should treat "the agent requested this" as attacker-influenced input until it clears policy, not as proof the request is legitimate, and should isolate or sanitize untrusted content in an agent's context wherever it's practical to do so.

## Should an agent write infrastructure code, or call an API that writes it for it?

Both are legitimate, and the right choice depends on what the agent is actually doing: an agent extending or modifying a stack benefits from writing real code it can test and diff, while an agent performing a bounded, repeatable action is often better served by calling a narrow, pre-built interface that already encodes the guardrails.

### Two shapes of agent-facing interface

| | Agent writes code | Agent calls an API or tool |
| --- | --- | --- |
| Example | Agent edits a Pulumi program in TypeScript or Python to add a resource | Agent calls a golden-path template, or a service you've built on [Automation API](/docs/iac/concepts/automation-api/), to spin up a pre-defined environment |
| Correctness check | Preview, tests, and policy run against the actual diff | Correctness is baked into the interface itself; the agent can't ask for something the interface doesn't expose |
| Best for | Novel or exploratory changes, refactors, anything not covered by an existing template | Repeatable, high-volume requests: a new dev environment, a scoped test database |
| Failure mode if misused | An agent produces plausible-looking code that's subtly wrong and passes a weak review | An agent is boxed in and can't do the legitimate thing it actually needed to do |

Real programming languages help here regardless of which shape you pick, because they carry loops, functions, types, and test frameworks, which means an agent's output can be tested the same way a human's pull request would be. That's the same argument [we made about running agent workloads on Kubernetes](/blog/ai-agents-on-kubernetes/): once you have a package, whether a Helm chart or a golden-path component, composing it into your specific environment, wiring its secrets, gating its rollout with policy, and testing the whole thing before it ships is software engineering, and a general-purpose language is built for that in a way a templating language isn't.

The "agent calls an API" shape is available today, too: [`pulumi do`](/blog/pulumi-do-direct-resource-operations/), currently in research preview, turns a bounded, repeatable request into a single command with no project, code, or state file required, so `pulumi do aws:s3:Bucket create` provisions a bucket directly from the CLI. It's the narrow-interface half of this table, and governance layers on top of it through Pulumi Cloud rather than living in the command itself.

## What replaces code review when no human is watching?

Nothing single-handedly replaces code review, but the combination of a preview, automated tests, a policy gate, and a cost estimate covers most of what a human reviewer was actually checking for, and it runs on every change instead of only the ones someone remembers to look at closely.

### The agent's feedback loop

* **Preview** — a diff of exactly what resources will be created, changed, or destroyed, generated before anything applies.
* **Tests** — unit tests against component logic, and property tests that assert invariants ("no bucket is public," "every resource is tagged") regardless of what specific change produced them.
* **Policy result** — a pass or fail from the same deterministic policy engine that gates human-initiated changes, with the specific rule that failed if it does.
* **Cost estimate** — a projected cost delta, so an agent's request to "add capacity" doesn't turn into a five-figure surprise before anyone reads the invoice.
* **A human escalation path** — for anything that fails a check, or that the platform has flagged as consequential enough to require a person regardless of what checks pass. [Pulumi Neo's human-in-the-loop approvals](/docs/ai/neo/) are one concrete version of this: the agent proposes and previews, a person approves before anything applies.

## What breaks when fifty agents change the same environment at once?

Concurrency is the failure mode that doesn't show up until an agent workflow scales past a demo: one agent provisioning one environment has no other agent to conflict with, and fifty agents proposing changes to overlapping infrastructure at the same time is a distributed-systems problem a platform has to solve before it happens, not after.

### Blast-radius controls worth having before you need them

* **Stack-per-agent or stack-per-task** boundaries, so two agents can't lock or conflict over the same state file.
* **Concurrency limits per environment**, so a burst of agent activity can't overwhelm a shared account's API rate limits or a downstream provider's quotas.
* **Budget caps enforced by policy**, not just reported after the fact, so a runaway agent loop can't spend past a threshold before anyone notices.
* **Resource quotas per identity**, the same control a platform already applies to human teams, applied to agent identities too.
* **A kill switch**: a way to pause or revoke a specific agent's credentials immediately, without touching anyone else's access.

## How do you audit and roll back a change no human approved?

You audit it the same way you'd want to audit a change a human made under time pressure: by capturing who or what proposed it, what the diff was, what policy said, and what the state looked like immediately before, so rolling back means restoring a known-good state rather than reconstructing one from memory.

### What a usable agent audit trail contains

* **Identity** — which agent, running which task, under whose delegated authority if any.
* **Intent** — what the agent was asked to do, in whatever form that request took.
* **Diff** — the actual infrastructure change, not just a natural-language summary of it.
* **Policy result** — what passed, what was overridden, and by what authority if an override happened.
* **Before-and-after state** — enough to restore the prior state directly, rather than requiring someone to reason out what "before" looked like.

## What does an agent-ready golden path look like?

A golden path built for an agent looks almost exactly like one built for a human developer, because the point of a golden path was always to encode the organization's judgment into something reusable, so an agent that follows it inherits the same guardrails a human following it would.

What changes is how many golden paths a platform team needs, and how fast. The old model was artisanal: a platform engineer noticed a repeated request, spent a sprint or two hand-building a template for it, and that template served a human team's request volume for months. Once app teams are vibe-coding with agents that can generate a plausible request for a new environment, datastore, or service many times a day, hand-building one golden path at a time stops keeping up with what's actually arriving. Platform-engineering headcount does not scale at agent speed, and it does not need to: a golden path expressed as a Pulumi component is code, and code is something an agent can help extend under the same policy and review guardrails covered above, provided a human still owns what goes into the template in the first place. That's the shift underneath everything else in this post: platform teams are increasingly building the next golden path with agents, on top of letting agents consume the ones that already exist.

### Components and templates as the shared surface

A [Pulumi component](/docs/iac/guides/building-extending/components/build-a-component/) is a good unit for this, because it's callable from any language the platform supports and it can bake org defaults into the resource it creates, rather than relying on the caller to get them right:

```typescript
// A golden path for a scoped Postgres database, callable by a human
// developer or an agent through the same interface either way.
export class ScopedDatabase extends pulumi.ComponentResource {
    constructor(name: string, args: ScopedDatabaseArgs, opts?: pulumi.ComponentResourceOptions) {
        super("platform:index:ScopedDatabase", name, {}, opts);
        // Enforces org defaults (encryption, backup retention, network
        // isolation) regardless of who or what is calling this component.
    }
}
```

The value of a component like this is that it's the same component whether a human calls it from the CLI or an agent calls it from a task. That parity is what makes the guardrails hold: there's no separate, less-scrutinized "agent path" quietly bypassing the rules the human-facing path enforces. We covered the tradeoffs between service catalogs and infrastructure-first platforms in more depth in [Backstage vs. Pulumi](/blog/backstage-vs-pulumi-idp-why-infrastructure-first-platform-engineering-matters/), and the shape of golden paths themselves in [Golden Paths: Infrastructure, Components, and Templates](/blog/golden-paths-infrastructure-components-and-templates/).

## Frequently asked questions

### Is an AI agent just another platform user, or does it need different guardrails?

It's a different persona, not a different category of user. The RBAC, quotas, and policy an established platform already applies to human teams extend to agents too, but the specifics differ: short-lived scoped credentials instead of a developer's standing access, and automated policy gates instead of a code review someone remembers to do. The mechanism is the same; the settings change.

### Do AI agents actually provision production infrastructure today?

Some do, in bounded ways: golden-path environments, scoped test infrastructure, and pre-approved changes inside a policy-gated pipeline. Gartner expects 40% of enterprise applications to carry a task-specific AI agent by the end of 2026, up from under 5% in 2025, which is a fast enough curve that platform teams should build the guardrails before agent-initiated changes become common rather than after.

### What's the risk of letting an agent write infrastructure code directly?

The main risk is plausible-looking output that's subtly wrong: code that passes a linter or a weak review but omits a security control or misconfigures a resource. That risk isn't unique to agents, human-written code fails the same way, but an agent can produce more of it faster. The mitigation is the same one that works for human code: tests, preview, and a policy gate that runs on every change rather than a spot check.

### Should platform teams be worried about agentic AI project failure rates?

It's worth factoring in. Gartner also projects that over 40% of agentic AI projects will be canceled by the end of 2027 over escalating costs, unclear business value, or inadequate risk controls. That's a reason to build the guardrails described here before scaling agent access, not a reason to skip agent enablement altogether; the platforms that solve governance well are the ones likely to be in the smaller group of projects that stick.

### Does policy as code work the same way for agents as it does for human-initiated changes?

Yes, and that's the point. The same deterministic policy engine that blocks a human from creating a public S3 bucket should block an agent from doing the same thing, evaluated the same way regardless of who or what proposed the change. Building a second, agent-specific policy path is more work and a weaker guarantee than making the existing one apply universally.

### How is this different from what Backstage or a service catalog already does?

A service catalog is a discovery and documentation layer: it helps a developer, or an agent reading it, find the right template. It doesn't enforce identity scope, policy evaluation, or audit trails on the infrastructure changes that come out of using a template; those guardrails live in the provisioning layer underneath. An agent-ready platform needs both: a catalog an agent can navigate, and an infrastructure layer that governs what happens after it picks something.

## Where this goes next

None of this is settled. Most organizations giving agents provisioning access today are doing it in narrow, closely watched slices, and that's the right amount of caution for where the tooling actually is. For the broader picture of how identity, policy, and audit trails hold up once agents operate across an entire cloud estate rather than one platform's golden paths, see [how to govern and secure agentic infrastructure](/what-is/what-is-agentic-infrastructure/#how-do-you-govern-and-secure-agentic-infrastructure). DORA's 2025 research on AI-assisted software development found that AI's primary effect is to amplify an organization's existing strengths and weaknesses, not to fix weak platforms on its own, and that holds for infrastructure the same way it holds for code: an agent given access to a platform with weak identity controls, no policy gate, and no audit trail will find and exploit those gaps faster than a human ever would, and an agent given access to a well-governed platform will extend that governance instead of testing it.

The platforms that get this right treat an agent's provisioning request exactly like a human's, with the same identity model, the same policy gate, and the same audit trail, and let the difference in who's asking stay invisible to the infrastructure underneath. That's a smaller lift than it sounds like, because it's mostly the platform engineering discipline you already have, applied without an exception carved out for software that happens to make its own decisions.

{{< blog/cta-card title="Build agent-ready guardrails" label="Get started with Pulumi" href="/docs/get-started/" >}}
See identity, policy, and audit working together on real infrastructure, or go straight to [setting up policy as code](/docs/insights/policy/get-started/) if the pre-deploy gate is the piece you're missing.
{{< /blog/cta-card >}}
