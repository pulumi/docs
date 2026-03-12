---
title_tag: Compostable AI | Case Studies
title: "Compostable AI: Building an AI Software Factory"
description: |
    Edinburgh-based AI platform company deploys from contract to production in one day, with two backend engineers managing infrastructure for 19 clients using AI agents and Pulumi.
meta_desc: Learn how Compostable AI built a software factory where AI agents write infrastructure code with Pulumi, deploying from contract to production in one day.

customer_name: Compostable AI
customer_logo: /logos/customers/compostable-ai.svg
customer_url: https://compostable.ai

quote_block:
    quote: |
        "The Pulumi policy packs are one element of the guardrails, and it's defense in depth. We have so many guardrails in place that are automatically enforced, and violations are automatically reported. And that's what allows us to be able to proceed with the velocity that we do."
    quote_attrib: Ewan Dawson, CTO, Compostable AI

exec_summary: |
    Compostable AI provides "sovereign intelligence layers" for enterprise customers: bespoke AI agent solutions built on their Clarity Platform. The company operates a single-tenant model, with each customer receiving dedicated AWS accounts for staging and production. With just two backend engineers, the team manages infrastructure for 15 solutions across 19 clients, deploying from contract signing to production in approximately one day.

    The company needed infrastructure-as-code that AI agents could generate, validate, and iterate on without human review. By adopting Pulumi's infrastructure as code, ESC for hierarchical configuration, and policy packs for automated compliance, Compostable AI built a software factory where AI agents handle the full development lifecycle. The team achieved ISO 27001 certification in six weeks and was recently onboarded as a supplier to a $1B revenue global enterprise.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenge
      anchor: the-challenge
    - label: Solution
      anchor: achieving-one-day-deployments-with-two-engineers
    - label: Software Factory
      anchor: the-software-factory-iteration-toward-correctness
    - label: Results
      anchor: results
    - label: Looking Forward
      anchor: looking-forward
---

## The challenge

Compostable AI provides "sovereign intelligence layers" for enterprise customers: bespoke AI agent solutions built on their Clarity Platform. The business model is single-tenant, with each customer receiving dedicated AWS accounts for staging and production.

The company achieved ISO 27001 certification in six weeks and was recently onboarded as a supplier to a $1B revenue global enterprise. They faced the challenge of scaling infrastructure deployments without proportional headcount growth.

Each client requires separate AWS accounts with consistent platform infrastructure but customer-specific configurations. The development philosophy centers on AI agents writing all code. "If we have to have engineers write or review code, that's an unacceptable bottleneck," Dawson says. Infrastructure tooling wasn't designed for this. The team needed infrastructure-as-code that agents could generate, validate, and iterate on without human review.

## Achieving one-day deployments with two engineers

Compostable AI selected Pulumi after evaluating infrastructure-as-code options through the lens of AI agent capabilities.

**Evolving the platform weekly without breaking production.** The team is building higher-level constructs for their platform layer, where infrastructure definitions are a codebase with abstractions, tests, and refactorings. "For us to be able to continually evolve our platform, we need to be able to reliably refactor the IaC code. This is easier in a strongly typed programming language."

TypeScript's type system proved critical for iterative development. Using TypeScript and leaning on the type system enables their iterative approach, where agents refine solutions through multiple passes. As Dawson explains, "it doesn't really matter how many iterations you have along the way" as long as the solution is correct.

**Fleet-wide configuration changes in minutes.** The team started with [Pulumi ESC](/product/secrets-management/) for secrets but found the real value in hierarchical configuration across their deployment fleet. "We can create composable blocks of configuration and use the Pulumi ESC's import functionality to dynamically build those in," Dawson explains. "When we have cross-cutting infrastructure configuration, we can change that in one place, and we know that all of the infrastructure is going to be updated."

The configuration hierarchy uses multiple layers (platform base, staging/prod, per-client, per-account), where each can override inherited settings. Configuration changes through ESC bypass the slower GitOps flow required for code changes, and the CLI interface enables agent automation across the fleet.

**Eliminating human review bottlenecks.** Compostable AI runs software development agents that take specifications from their issue tracker and use those specifications to build infrastructure. Rather than relying on a single general-purpose agent, the team delegates Pulumi-specific infrastructure work to [Neo](/blog/pulumi-neo/) through its MCP server.

"If you try to get one agent to do everything, it's a jack of all trades, master of none," Dawson explains. The team uses Claude Code, Gemini CLI, and Warp, AI coding assistants triggered through Linear tickets or Slack messages. When these agents encounter infrastructure tasks, instructions in the AGENTS.md file direct them to delegate to Neo via Pulumi's MCP server. Neo then executes Pulumi-specific work with direct integration to Pulumi Cloud.

Neo provides Pulumi-specific knowledge and tight integration with Pulumi Cloud and automatic credential management. "We use Pulumi Cloud deployments for all deployments rather than GitHub Actions, and Neo's really good at driving that itself."

## The software factory: iteration toward correctness

Compostable AI's development model operates on iterative refinement toward correct solutions. "We're just building a machine that just climbs towards that solution," Dawson says.

Software development agents expand initial specifications by examining the codebase, documentation, and previous deliverables. Other agents then assemble platform components or iterate on the platform itself. Multiple reviewing agents examine the prospective solution from different aspects: performance, functional correctness, and security. They provide feedback that triggers another development round until all agents are satisfied.

Once validated, the solution deploys to staging for manual user acceptance testing and security testing, including automated validation through Pulumi [policy packs](/docs/iac/packages-and-automation/crossguard/). The team uses the standard AWS best practices policy pack, deployed universally. The policy packs automate the implementation of best practices, validate conformance, and simplify the certification journey.

The blast radius is contained at the AWS account level. Agents have access only to staging accounts, and changes are limited to a single customer account for bespoke work.

## Results

Currently, it takes about 90 minutes to stand up a new AWS account and deploy the Clarity Platform. The rest of the one-day timeline is developing the initial MVP solution for review. The target is to reduce the full process to one hour. "The less it involves us as engineers sitting with our hands on keyboard, the higher throughput we've been getting."

With two backend engineers managing infrastructure for 15 solutions across 19 clients, the goal is non-linear scaling: serving 100 customers with the same team that serves 10 today.

The transformation for Dawson himself is philosophical. The 20-year software development veteran has fundamentally shifted his approach: "Back when I was a software developer, I used to think of my work as a craft. Then I spent 4 years in leadership positions, and stopped writing code. Since my return to startup life at the start of the agentic AI revolution 2 years ago, I've shipped more code than I did in the whole of the previous 15 years. And all of it in languages I wouldn't be able to write in by hand."

Achieving ISO 27001 certification in six weeks provides business credibility that's essential for a small startup operating in a space where the perception of risk is relatively high. "The Pulumi policy packs are one element of the guardrails, and it's defense in depth. We have so many guardrails in place that are automatically enforced, and violations are automatically reported. And that's what allows us to be able to proceed with the velocity that we do."

## Looking forward

Compostable AI continues to refine the software factory model. The platform will need to support the jump to 100-plus deployments while maintaining the current team structure.

Pulumi remains central to the strategy. "Pulumi is a key component of our strategy to pick the best tools that will help us grow on this agentic journey," Dawson says.

---

Ready to build your own AI-powered infrastructure workflow?

[Start Free](https://app.pulumi.com/signup) | [Talk with an Expert](/contact/?form=request-a-demo)
