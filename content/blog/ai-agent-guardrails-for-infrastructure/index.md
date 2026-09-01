---
title: "AI Agent Guardrails for Infrastructure: What Policy as Code Actually Prevents"
allow_long_title: true
date: 2026-08-27
draft: false
meta_desc: "What policy as code blocks when an AI agent proposes infrastructure changes, and the five kinds of failure it cannot see."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - ai
    - ai-agents
    - policy-as-code
    - security
    - infrastructure-as-code
category: perspectives
schema_type: auto
faq_schema: true

# Social media copy, auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Two-thirds of enterprises say they have clear guardrails for what their AI agents can do. When an agent exceeds them, only 11% actually block the action.

        What policy as code actually prevents, and the five failure modes it can't see:
    linkedin: |
        65% of enterprises had an AI agent-related security incident in the past year, according to a new Cloud Security Alliance survey of 418 IT and security professionals commissioned by Token Security. 66% say they have clear guardrails defining what their agents can do. The gap is in what happens next: when an agent exceeds its scope, 38% of organizations require human approval, 24% log it, and only 11% automatically block the action.

        Policy as code sits on the enforcing side of that gap. It runs on every preview and update, applies the same rules whether a human or an agent authored the change, and an org-mandatory policy has no documented skip flag — a genuinely useful property when an agent can propose plausible-looking infrastructure faster than any team can review it.

        It is also not the whole answer. There are real limits to what policy as code can see once an agent is involved, and specific places the rest of the enforcement has to live.

        Read the full breakdown of what policy as code actually prevents, and what it doesn't:
    bluesky: |
        65% of enterprises had an AI agent incident in the past year. 66% say they have clear guardrails. Only 11% automatically block an agent that exceeds them.

        Here's what policy as code actually prevents, and the five things it can't see.
---

Policy as code reliably stops an AI agent from deploying a change that breaks a rule someone wrote down. It does not stop a change nobody wrote a rule about, and it cannot see one that never passes through Pulumi at all. Knowing which side of that line a failure falls on is the practical question for anyone letting an agent touch production.

<!--more-->

## Why are AI agent guardrails suddenly urgent?

The Cloud Security Alliance surveyed 418 IT and security professionals in January 2026, in a study commissioned by Token Security, and published the results in April 2026 as [*Autonomous but Not Controlled: AI Agent Incidents Now Common in Enterprises*](https://cloudsecurityalliance.org/artifacts/autonomous-but-not-controlled-ai-agent-incidents-now-common-in-enterprises). Nearly two in three respondents, 65%, said their organization experienced an AI agent-related incident in the past 12 months: data exposure in 61% of those cases, operational disruption in 43%, financial loss in 35%. Eighty-two percent had discovered a previously unknown, "shadow" AI agent operating in their environment within the past year, and 41% found one more than once. Sixty-eight percent still reported high confidence in their visibility into what their agents were doing.

The same survey asked what happens when an agent exceeds the scope it was given. Thirty-eight percent of organizations require human approval before the action proceeds. Twenty-four percent log it and move on. Only 11% automatically block it. And 66% of respondents said they have clear guardrails defining what their agents are allowed to do in the first place, a genuinely encouraging number on its own. Read next to the 11%, it says something sharper: describing a boundary and enforcing one are different exercises, and most organizations have made more progress on the first than the second.

This is not a hypothetical risk sitting a few years out. In April 2026, [the Guardian reported](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database) that a Claude-powered coding agent, working for the founder of a company called PocketOS, deleted the company's production database and then confessed to it unprompted. [Zenity's technical writeup](https://zenity.io/blog/current-events/ai-agent-database-deletion-pocketos) traced the mechanics: the agent found a stored Railway API token in the repository it was working in and issued a `volumeDelete` GraphQL mutation directly against the platform's API, in about nine seconds, and the backups lived on the same volume it deleted. Nothing in the reporting on the incident suggests the agent went through an infrastructure-as-code tool, a policy engine, or a review process of any kind. It found a stray credential and an API, and that was sufficient.

The conversation has moved into practitioner forums at the same pace. A [Hacker News thread](https://news.ycombinator.com/item?id=47897140) on agentic systems and database design drew this line from one commenter: "NO ONE, agent or human, should have direct write access to production databases outside of emergency break glass scenarios." One [r/Terraform thread](https://www.reddit.com/r/Terraform/comments/1u0ii35/how_are_you_thinking_about_ai_agents_and_policy/) describes a pattern worth naming: an agent that only generates code, where no apply happens unless every check passes and the plan shows zero unexpected replacements. Threads on [r/sre](https://www.reddit.com/r/sre/comments/1pfvi75/were_about_to_let_ai_agents_touch_production/), [r/aws](https://www.reddit.com/r/aws/comments/1roy344/claude_code_ran_terraform_destroy_on_production/), and [r/devops](https://www.reddit.com/r/devops/comments/1rcre0e/are_aigenerated_infra_changes_causing_more/) tell the same story from different angles, and [devops.com asked the plain question directly](https://devops.com/ai-agents-are-writing-your-infrastructure-code-is-anyone-governing-it/): AI agents are writing infrastructure code now, so who is governing it, citing [Veracode's Spring 2026 GenAI Code Security Update](https://www.veracode.com/blog/spring-2026-genai-code-security/), which found that only about 55% of AI code-generation tasks produce secure code by default. None of this is speculation about a future risk. It is a description of the present one.

## What does policy as code actually prevent?

[Policy as code](/what-is/what-is-policy-as-code/) evaluates every proposed infrastructure change against rules written in the languages your team already uses: TypeScript, Python, or Rego via OPA, and it runs that evaluation automatically on every `pulumi preview` and `pulumi up`, before the change reaches the cloud. It does not ask who or what proposed the change. A resource-validation policy checking that an S3 bucket is encrypted applies exactly the same way whether a developer wrote the code by hand or an agent generated it in a single pass. That indifference to authorship is the property that matters most here: it is one of the few controls in a platform whose enforcement cost does not rise with the volume or speed of changes flowing through it, which is precisely what changes when the author is an agent capable of producing far more infrastructure code than any team can read line by line.

Enforcement is also close to unavoidable by configuration. Pulumi Cloud attaches mandatory policy packs to a stack through a policy group, and there is no flag a developer, or an agent driving the CLI on a developer's behalf, can pass to skip an org-mandated pack. Running the CLI with a local policy pack of your own adds to the organization's packs rather than replacing them, and a violation from any of them halts the update. An agent that generates a plan violating a mandatory rule gets the same rejection a human would: the change does not go through.

Some of Pulumi's enforcement levels go further than blocking. A resource-validation policy set to *remediate* can rewrite the offending property and substitute corrected state before the resource is even created, closing the gap between "flagged" and "fixed" without a second round trip. Pre-built policy packs mapped to CIS, PCI DSS, NIST, and ISO 27001 controls, available on the Business Critical edition, mean a team does not have to author baseline compliance rules from nothing before an agent starts generating changes against them.

## What does policy as code not prevent?

None of that adds up to a general answer to "can this agent be trusted with infrastructure," and the honest version of this post has to say where the coverage actually ends.

Policy as code only evaluates changes that pass through Pulumi. A preventative policy group sees the resources Pulumi manages, full stop. If an agent holds a cloud API token or a database credential directly, the way the agent in the PocketOS incident did, and calls that API without ever generating a Pulumi program, there is no interception point at all: nothing in the reporting on that incident suggests the change passed through an IaC tool, a policy engine, or a review step of any kind. Pulumi's Audit policy groups can scan the cloud account on a schedule and report what they find through Discovery, but that is detection after the fact, not prevention, and it cannot undo what already happened.

Policy checks structure, not intent. A rule can confirm a database is encrypted, tagged correctly, and sitting in the right subnet, and none of that tells you whether it is the right database for the change being made. An agent that misreads which resource a request refers to can produce a change that is fully compliant and still wrong.

Destructive replacements are a resource option, not a policy feature. Protecting a resource from deletion or replacement is something you opt into per resource with `protect` or `retainOnDelete`, both off by default. A policy can be written to flag a diff that would destroy and recreate a stateful resource, but that has to be a rule someone deliberately authored; no pre-built pack ships it as a given. An agent proposing a plausible-looking replacement of a production database will sail through unless that specific rule already exists.

Stack-validation policies, the ones that check relationships across multiple resources rather than properties of one, only run during `pulumi up`. They do not run during `pulumi preview`, which means the review a human performs on an agent's pull request, reading the preview output before approving it, cannot catch a stack-level violation. The rule fires only once the change is already being applied.

And policy encodes the failures someone anticipated. A rule set built from a team's collective experience with human-authored changes was not written with an agent's failure modes in mind, and an agent exploring the space of plausible changes can find the gap in a rule set faster than any team writes new rules to close it. An advisory policy, which warns without blocking, makes this worse rather than better: a human reads a warning and stops to think about it; an agent records it and proceeds to the next step, because nothing forced it to stop.

## Do AI agents change how you should write policy?

Yes, in a few concrete ways, as [agentic infrastructure](/what-is/what-is-agentic-infrastructure/) moves from experiment to default. The choice between advisory and mandatory enforcement stops being a matter of team culture once the author of a change might not read a warning the way a person does. For the small set of rules where a violation would be unrecoverable, treat mandatory as the default rather than something you graduate into after a warning period.

It is also worth assuming an agent will read a rejection message and try again. A policy that blocks one specific property value, rather than the underlying condition it is protecting against, invites an agent to keep adjusting that one property until the check passes while the actual risk remains. Write policies against the property that matters, not the value that happened to trip the first attempt, and treat repeated near-miss violations from the same source as a signal worth a human looking at, not just a counter to log.

## What belongs around policy as code?

Policy as code is one layer among several, and each of the others closes a gap the others cannot:

- Least-privilege scoping on the agent's own credentials removes the capability to make an unreviewed change directly against a cloud API or database, rather than reviewing the intent after the fact. This is the most direct answer to the PocketOS failure mode.
- Cloud-native guardrails, [AWS Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/overview), and [GCP Organization Policy](https://docs.cloud.google.com/organization-policy/overview), are enforced by the cloud provider itself, so they apply no matter what tool or agent made the call.
- [Kubernetes admission control](https://openpolicyagent.org/docs/kubernetes) via OPA Gatekeeper or Kyverno enforces rules at the API server, regardless of how an object was submitted.
- [Sandboxing the machine an agent runs on](/blog/sandboxing-coding-agents-yolo-mode/) contains what the agent can reach in the first place, which is a different problem than validating what it proposes.
- A human approval step and an audit trail at a defined blast-radius threshold give a person a checkpoint before the highest-consequence changes, and a record to reconstruct what happened when something gets through anyway.

[A working policy-as-code implementation](/blog/deployment-guardrails-with-policy-as-code/) using Pulumi's CrossGuard framework is the how-to companion to this post if you are setting the mechanics up for the first time.

## Where should a team start?

Start with the agent's own credentials, not with the policy engine. Narrowing what an agent can reach directly removes an entire category of failure, the one policy as code cannot see, before a single rule gets written. From there, put mandatory enforcement, not advisory, behind the small number of rules that describe genuinely unrecoverable outcomes, and put destructive-change protection where it actually lives: `protect` and `retainOnDelete` on the resources that matter, and an explicit review step for any plan showing a replacement, rather than hoping a policy rule catches it.

Sixty-six percent of organizations believe they have clear guardrails. Eleven percent will actually stop an agent that crosses them. Closing that gap is not a single control. It is deciding, deliberately, which of your failure modes belong to policy as code, which belong to the layers around it, and which ones nobody has written a rule for yet.
