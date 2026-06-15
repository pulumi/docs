---
title: "Neo Plan Mode: Iterate Before You Execute"
date: 2026-04-01
draft: false
meta_desc: "Neo's Plan Mode lets you collaborate on a detailed plan before execution begins, with thorough discovery, conversational refinement, and explicit approval."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - pulumi-neo
    - ai
    - features
categories:
    - agentic-infrastructure
schema_type: auto

social:
    twitter: |
        Neo now has Plan Mode.

        For complex infrastructure tasks, you can collaborate with Neo on a detailed plan before anything executes. Neo researches your actual infrastructure, you iterate on the approach together, and execution starts only when you approve.
    linkedin: |
        **Neo Plan Mode: Iterate Before You Execute**

        For straightforward infrastructure tasks, jumping straight to execution works fine. But complex operations benefit from deliberate planning, understanding what exists, identifying dependencies, and agreeing on an approach before anything changes.

        Neo's new Plan Mode creates a dedicated space for exactly this kind of upfront thinking. When you enable it, Neo investigates your actual infrastructure and synthesizes what it finds into a grounded plan that you refine together through conversation. Execution begins only when you approve.

        Because Plan Mode works with any autonomy level, you can review the approach thoroughly up front and then let Neo execute without stopping, or keep full oversight at every step. The planning phase and execution phase have independent controls.

        Available now in Pulumi Cloud.
    bluesky: |
        Neo now has Plan Mode. For complex tasks, collaborate with Neo on a detailed plan before anything executes. It researches your infrastructure, you iterate together, and execution starts only when you approve.
---

Infrastructure work ranges from simple updates to complex multi-stack operations. For straightforward tasks, jumping straight to execution is often fine. But complex tasks benefit from deliberate upfront thinking: understanding what exists, identifying dependencies, and agreeing on an approach before anything changes. Today we're launching Plan Mode, a dedicated experience for collaborating with Neo on a detailed plan before execution begins.

<!--more-->

## Plan Mode

Without dedicated planning, Neo balances planning with progress toward execution. That works well for many tasks, but complex operations benefit from more thorough upfront discovery. Plan Mode now makes upfront deliberation a first-class workflow, where instead of focusing on getting to execution, Neo focuses entirely on discovery and synthesis until you explicitly approve the plan.

## How it works

Enter Plan Mode by selecting the plan button when starting a task. Neo shifts its behavior:

1. **Discovery**: Neo investigates your environment — examining existing infrastructure, reading relevant code, checking dependencies, and researching patterns.
1. **Synthesis**: From that research, Neo produces a plan explaining what it will do and why. The plan references specific things Neo discovered, like a particular stack configuration or dependency.
1. **Refinement**: You refine the plan through normal conversation, challenging assumptions, asking for an alternative approach, or requesting more detail on a specific area.
1. **Approval**: Once you're satisfied, you approve the plan and execution begins. Neo carries forward everything it learned during discovery, so the transition from planning to execution is seamless.

## When to use it

Plan Mode is opt-in. You choose it when you want to work through an approach before committing:

- **Complex multi-stack operations** where understanding dependencies matters
- **Unfamiliar infrastructure** where discovery reduces churn
- **Autonomous execution** where plan approval is your key control point before Neo runs without step-by-step oversight

## Get started

Plan Mode is available now for all Pulumi Cloud organizations. It works with any [task mode](/docs/ai/tasks/#task-modes), so you can pair thorough upfront planning with whatever level of execution autonomy fits the situation.

To try it, [open Neo in Pulumi Cloud](https://app.pulumi.com/neo). For more details, see the [Plan Mode documentation](/docs/ai/tasks/#plan-mode).
