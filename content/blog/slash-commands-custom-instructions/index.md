---
title: "Bring Your Organization to Neo: Custom Instructions and Slash Commands"

date: 2025-12-10

draft: true

meta_desc: Custom Instructions teach Neo your organization's standards. Slash Commands turn proven prompts into shortcuts anyone can use. Both are available now.

meta_image: meta.png

authors:
    - neo-team

tags:
    - neo
    - agentic-ai

schema_type: auto

---

Every organization builds up knowledge over time: naming standards, compliance requirements, patterns your team has settled on, and proven approaches to common tasks. Until now, bringing this knowledge into Neo meant repeating it manually each time - specifying preferences, describing how your team works, and recreating prompts that someone already perfected.

Two new features change this. Custom Instructions teach Neo your standards so it applies them automatically. Slash Commands capture proven prompts so anyone on your team can use them with a keystroke.

<!--more-->

## Custom Instructions: Standards Applied Automatically

Custom Instructions let you define what Neo should know about your organization and how it should behave. This includes naming conventions, required tags and compliance requirements, technology preferences, and cost guidelines - but also actions Neo should take automatically, like including a rough cost estimate whenever it proposes new infrastructure. You configure them once in your organization settings, and Neo applies them to every task from that point forward.

Consider the difference. Before Custom Instructions, a simple request required loading context:

> "Neo, update our Lambda functions to Node 20. Remember, we use TypeScript exclusively, our naming convention is service-region-env, we always deploy to us-east-1 first for testing, and all resources need our standard compliance tags including CostCenter and DataClassification."

With those details captured in Custom Instructions, the same request becomes:

> "Neo, update our Lambda functions to Node 20."

Neo already knows how your team works, so you can focus on what you're trying to accomplish.

## Slash Commands: Capture What Works

Over time, your team figures out the right way to ask Neo for certain tasks. Maybe someone wrote the perfect prompt for checking policy violations, or discovered an approach to drift detection that catches issues others miss. That knowledge tends to live in someone's head or buried in a Slack thread.

Slash Commands turn these prompts into shortcuts anyone can use. When you type `/` in Neo, you'll see available commands, select one, and Neo receives the full prompt behind it.

Neo ships with built-in commands for common tasks:

| Command | What it does |
|---------|--------------|
| `/policy-issues-report` | Lists your most severe policy violations |
| `/get-started` | Learn what Neo can do and how to structure effective requests |
| `/component-version-report` | Lists components that are outdated in your private registry |
| `/provider-version-report` | Lists providers that are outdated |

You can also create your own. In Pulumi Cloud, you define the prompt and specify any parameters it should accept - no coding required. Once saved, your team can start using it immediately. If a command needs more information than what's provided, Neo will ask follow-up questions to fill in the gaps.

## Get Started

Custom Instructions and Slash Commands are available now. You can configure Custom Instructions in your organization settings. Slash Commands come with several built-in options, and you can create custom ones tailored to your workflow.
