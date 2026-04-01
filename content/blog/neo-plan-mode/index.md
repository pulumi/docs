---
title: "Neo Plan Mode: Iterate Before You Execute"
date: 2026-04-01
draft: false
meta_desc: "Neo's Plan Mode lets you collaborate on a detailed plan before execution begins, with thorough discovery, conversational refinement, and explicit approval."
meta_image: meta.png
authors:
    - neo-team
tags:
    - neo
    - ai
    - features
schema_type: auto

social:
    twitter: |
        Neo now has Plan Mode.

        For complex infrastructure tasks, you can collaborate with Neo on a detailed plan before anything executes. Neo researches your actual infrastructure, you iterate on the approach together, and execution starts only when you approve.
    linkedin: |
        **Neo Plan Mode: Iterate Before You Execute**

        Infrastructure work ranges from simple updates to complex multi-stack operations. For straightforward tasks, jumping straight to execution works fine. But complex tasks benefit from deliberate planning: understanding what exists, identifying dependencies, and agreeing on an approach before anything changes.

        Neo's new Plan Mode creates a dedicated space for this. Neo investigates your infrastructure, synthesizes what it finds into a grounded plan, and iterates with you until you approve. Execution begins only when you say so.

        Plan Mode works with any autonomy level. Use it with Auto Mode for confident autonomous execution backed by a reviewed plan, or with Review Mode for maximum oversight at every step.

        Available now in Pulumi Cloud.
---

Infrastructure work ranges from simple updates to complex multi-stack operations. For straightforward tasks, jumping straight to execution is often ok. But complex tasks benefit from deliberate upfront thinking: understanding what exists, identifying dependencies, and agreeing on an approach before anything changes. Today we're launching Plan Mode, a dedicated experience for collaborating with Neo on a detailed plan before execution begins.

<!--more-->

## Plan Mode

Without dedicated planning, Neo balances planning with progress toward execution. That works well for many tasks, but complex operations benefit from more thorough upfront discovery to understand what exists, surface dependencies, and align on an approach before executing on the task. Plan Mode makes upfront deliberation a first-class workflow. Instead of moving toward execution, Neo focuses entirely on discovery and synthesis until you explicitly approve the plan.

## How it works

Enter Plan Mode by clicking the plan button when starting a task. Neo shifts its behavior:

1. **Discovery**: Neo starts by investigating your environment. It examines existing infrastructure, reads relevant code, checks dependencies, and researches patterns, showing you what it's finding in real time so you can steer early.
1. **Synthesis**: From that research, Neo produces a narrative plan explaining what it will do and why. A plan references specific things Neo discovered, like a particular stack configuration or dependency, rather than generic steps that could apply to any similar task.
1. **Refinement**: You refine the plan through normal conversation, challenging assumptions, asking for an alternative approach, or requesting more detail on a specific area. 
1. **Approval**: Once you're satisfied, you approve the plan and execution begins. Neo carries forward everything it learned during discovery, so the transition from planning to execution is seamless.

## When to use it

Plan Mode is opt-in. You choose it when you want to work through an approach before committing:

- **Complex multi-stack operations** where understanding dependencies matters
- **Unfamiliar infrastructure** where discovery reduces churn
- **Autonomous execution** where plan approval is your key control point before Neo runs without step-by-step oversight

## Get started

Plan Mode is available now for all Pulumi Cloud organizations.

- [Sign in to Pulumi Cloud](https://app.pulumi.com/signin) and start a Neo task with Plan Mode
- [Read the Neo documentation](/docs/ai/) for detailed guides