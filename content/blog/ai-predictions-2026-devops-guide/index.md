---
title: "AI Predictions for 2026: A DevOps Engineer's Guide"
date: 2025-12-11
meta_image: meta.png
meta_desc: "AI predictions for 2026 and what they mean for DevOps engineers. From agent orchestration to local AI breakthroughs, here's how to prepare your infrastructure."
authors:
    - engin-diri
tags:
    - ai
    - devops
    - platform-engineering
    - automation
    - aws
    - pulumi-neo

social:
    twitter: "AI Predictions for 2026: What DevOps Engineers Need to Know. From IDE evolution to agent orchestration, local AI breakthroughs to machine-to-machine payments. Here's how to prepare for the AI-driven future."
    linkedin: |
        AI Predictions for 2026: A DevOps Engineer's Preparation Guide

        The AI landscape is shifting dramatically. Here's what's coming:

        - IDEs evolving into agent orchestration platforms
        - LLM providers specializing (Anthropic for coding, Google as generalist)
        - Local AI breakthroughs with new edge hardware
        - Code execution replacing traditional tool calling
        - Agent-to-agent protocols going mainstream
        - Machine-to-machine payments via crypto

        For DevOps engineers, this means rethinking how we build, deploy, and manage infrastructure. The engineers who thrive won't be those who resist these changes, but those who build the infrastructure to enable them.

        Read my full analysis on preparing for the AI-driven future.

        #AI #DevOps #PlatformEngineering #CloudNative #Automation
---

The IDE is dying, and so is tool calling. OpenAI is not going to win. And next year, you're going to be shipping code that you've never reviewed before, even as an experienced engineer.

These are bold claims, but the way we use AI in 2026 for coding and agents is going to look completely different. In this post, I want to cover my predictions and why they matter right now for DevOps engineers. Some of these are definitely hot takes, but that's what makes this conversation worth having.

<!--more-->

## IDEs are dead (at least as we know them)

Traditional IDEs where the code is the focus of the interface are simply going to become irrelevant. We're moving toward agent manager interfaces where we can kick off agents in parallel to work on different features in a codebase or even work on different projects at the exact same time.

We're already seeing this transition. [Google Antigravity](https://developers.googleblog.com/en/build-with-google-antigravity-our-new-agentic-development-platform/) combines a familiar AI-powered coding experience with a new agent-first interface. You can deploy agents that autonomously plan, execute, and verify complex tasks across your editor, terminal, and browser. [Cursor 2.0](https://cursor.com/changelog/2-0) lets you run up to eight agents in parallel on a single prompt, using git worktrees or remote machines to prevent file conflicts. Each agent operates in its own isolated copy of your codebase.

AWS validated this direction at [re:Invent 2025](https://aws.amazon.com/blogs/aws/top-announcements-of-aws-reinvent-2025/) by announcing "frontier agents" including Kiro for autonomous coding, along with dedicated security and DevOps agents. These agents maintain state, log actions, operate with policy guardrails, and integrate directly with CI/CD pipelines.

For infrastructure specifically, [Pulumi Neo](/docs/ai/) represents this same shift. Instead of writing code or running CLI commands for every operation, you describe what you need in natural language and Neo handles the implementation. It works across your entire infrastructure, understanding dependencies and creating execution plans that go through pull requests for review.

For DevOps engineers, this means your pipelines need to accommodate AI-generated code at scale. Multiple agents working simultaneously need isolated, reproducible environments. More generated code means more artifacts to track, version, and deploy.

## The different paths to AI dominance

A lot of people think that in the future a single large language model is going to have a monopoly and be the best at absolutely everything. But what's really going to happen is different providers will specialize and focus on being the best at different things.

Google is going down the generalist play with Gemini, aiming to be the jack of all trades. Anthropic is focusing on being the best for coding. You can see this in the benchmarks: when Opus 4.5 came out, the first benchmark they highlighted was for software engineering, because that's what Anthropic is focusing on.

Amazon is carving out its own niche with the [Nova model family](https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models), announced at re:Invent 2025. The Nova 2 lineup includes specialized models: Pro for complex reasoning, Sonic for real-time voice conversations, and Omni for simultaneous text, audio, and video processing. With [Nova Forge](https://www.aboutamazon.com/news/aws/aws-re-invent-2025-ai-news-updates), organizations can build custom frontier models by combining their proprietary data with AWS open weight models. The re:Invent message was clear: leveraging your first-party data is now fundamental to going beyond generic AI. We're talking about 30-40% increases in accuracy when you bring your own data into the equation.

But here's the hot take: I don't think OpenAI is going to come out on top with any kind of specialization. They've [disappointed time and time again](https://garymarcus.substack.com/p/gpt-5-overdue-overhyped-and-underwhelming) with GPT-5 and GPT-4.5. With 4.5, they seemed to try to be the creative specialist, but it just didn't work. The [GPT-5 launch in August 2025](https://www.axios.com/2025/08/12/gpt-5-bumpy-launch-openai) was described as "barely better than last month's flavor of the month" and on some metrics it's actually worse than earlier models.

For DevOps teams, this specialization means you'll need infrastructure that's model-agnostic and supports multiple AI backends. Plan for secrets management across multiple LLM providers and design your systems to swap models based on the task at hand.

## The local AI breakthrough

2026 is going to be the year of local AI. We didn't see that much this year besides DeepSeek at the start of 2025, which was a big deal. We had a couple of new models like Qwen 3, but nothing that fundamentally changed the game. Now we're starting to see new hardware that makes it obvious we're going to be able to run very large models on smaller devices.

There's new AI chips that can run upwards of 120 billion parameter large language models on the edge, which would be a complete game-changer. Right now, hardware requirements are one of the biggest problems when it comes to scaling local AI. If we can solve the hardware problem, we get 100% data privacy and zero-millisecond latency for our agents.

AWS is addressing this with [Trainium3 UltraServers](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/), their 3nm AI chips delivering 4.4x more compute than the previous generation. More significantly, [AWS AI Factories](https://www.geekwire.com/2025/amazon-unveils-frontier-agents-new-chips-and-private-ai-factories-in-aws-reinvent-rollout/) allow organizations to deploy racks of Trainium chips and NVIDIA GPUs directly into their own data centers, addressing data sovereignty concerns while keeping AI inference close to the data.

For DevOps, this opens possibilities for zero-latency inference in CI/CD pipelines, complete data privacy for sensitive codebases, and reduced cloud costs for AI-heavy workloads.

## Engineers as system architects

We're finally going to get to the point where we're not the coders. We delegate that entirely to our coding agents and we become the system architects. This mirrors the evolution of other engineering disciplines. Civil engineers don't fabricate the steel beams; they design the structure and verify the integrity.

I think of this as a three-step process:

1. **Define**: Set your objectives and the system that your agents will operate under
1. **Orchestrate**: Delegate the coding to your agents
1. **Validate**: Ensure the quality of the outputs and the overall system

We're still in the loop. We are the final say in whatever is created, but we're delegating the grunt work to our coding agents.

This is exactly the model that [Pulumi Neo](/docs/ai/tasks/) implements for infrastructure. When you give Neo a complex request, it creates a task plan outlining the steps it will take to accomplish your goal. This plan provides transparency into Neo's approach and gives you the opportunity to adjust the strategy before execution begins. Neo operates in different modes: Review mode where everything requires approval, Balanced mode where only deployments need sign-off, or Auto mode for full autonomy. You define the boundaries, Neo orchestrates the work, and you validate through pull requests and previews.

For DevOps engineers, this shift means building robust validation infrastructure becomes critical. When AI writes the code, you need automated testing pipelines, security scanning, and verification systems that can operate at the speed of AI-generated changes.

## Code execution is replacing tool calling

Here's a key insight that kept coming up at re:Invent: models are no longer the bottleneck. Context is. Our agents are going to change a lot next year because code execution is starting to replace tool calling. The problem with tool calling right now is that all the capabilities you give an agent take up context upfront. When you try to give a lot of different tools to an agent, you completely overwhelm it.

[Anthropic's research on code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) addresses exactly this problem. Code execution is a massive token reduction, faster, and more flexible. You're giving the agent the ability to generate its own capabilities at runtime by writing code to interact with APIs. A workflow that previously consumed about 150,000 tokens when tools were passed directly through the model was reimplemented with code execution and used only about 2,000 tokens. That's a 98.7% reduction.

AWS embraced this pattern with [Amazon Bedrock AgentCore](https://www.aboutamazon.com/news/aws/amazon-sagemaker-ai-amazon-bedrock-aws-ai-agents), which now includes code interpretation capabilities. AgentCore supports any agent framework (CrewAI, LangGraph, OpenAI SDK) and provides memory, browser tools, and observability features that make code execution practical at enterprise scale.

For DevOps, this means you need sandboxed, secure execution environments for AI-generated code. Running agent-generated code requires appropriate isolation, resource limits, and monitoring.

## Progressive disclosure and composable skills

The best part about code execution flexibility is it unlocks progressive disclosure. All I mean by that is: you have a lot of capabilities for an agent, but you don't actually give all of them upfront. Instead, you allow the agent to discover capabilities and then leverage them in a more flexible way.

For each capability, you just have a bit of metadata or description that loads upfront. When the agent decides to leverage that capability, then you load the full instructions. Now you can practically scale to infinity because all capabilities don't have to be loaded at runtime.

[Claude Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) is a good example of this pattern. Skills are organized folders of instructions, scripts, and resources that agents can discover and load dynamically. At session start, the agent scans available skills and populates the system prompt with just a brief name and description (around 100 tokens). The full skill prompt loads only after Claude selects it, preventing context bloat while maintaining discoverability.

[Kiro Powers](https://kiro.dev/powers/) addresses the same problem. Connecting five MCP servers can consume over 50,000 tokens, roughly 40% of an AI model's context window, before you even type your first request. Powers bundle MCP servers, steering files, and hooks into units that load dynamically based on conversation context. Mention "payment" and the Stripe power activates. [Datadog, Figma, and others](https://venturebeat.com/ai/aws-launches-kiro-powers-with-stripe-figma-and-datadog-integrations-for-ai) have powers available.

For DevOps, this translates to modular infrastructure definitions, on-demand capability loading, and efficient resource utilization. Think about how you can apply this pattern to your own automation.

## Agent-to-agent protocols are finally happening

Agent-to-agent protocols are where AI agents operate in a peer network, discover each other's capabilities in real time, and interact autonomously. When Google released their [A2A protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) earlier this year, there was a ton of buzz. A lot of people thought it was going to be the next big standard, like the next MCP. But then it kind of fell to the wayside.

The big reason is the chicken-and-egg problem. In order for A2A to be useful, you need a lot of people to adopt it at the same time. Otherwise, if you build an A2A-compatible agent, it has no other agents to talk to. The whole value proposition is lost unless you already have a big network to attach to.

But that's finally changing. The [Linux Foundation launched the A2A project](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) in June 2025, and adoption is accelerating. Adobe, Microsoft, SAP, ServiceNow, and S&P Global are all implementing A2A. In July 2025, Google released [version 0.3 of the A2A protocol](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) with a more stable interface critical to accelerating enterprise adoption.

## Machines paying machines

My next big prediction is that machines paying machines is going to become a very big thing. [Coinbase released the x402 protocol](https://www.coinbase.com/developer-platform/discover/launches/x402) for exactly this: building AI agents that you expose over the internet but require payment whenever someone else interacts with them.

This goes really well with agent-to-agent protocols. You can create a peer network where you monetize your agents. They all leverage each other but make payments whenever they take advantage of another agent's capabilities. Cryptocurrency is the perfect solution for this kind of machine-to-machine network because you need a currency where it's easy to do micropayments quickly and globally.

The x402 protocol has achieved [156,000 weekly transactions with 492% growth](https://www.coingecko.com/learn/x402-autonomous-ai-agent-payment-coinbase) since launching in May 2025. It's now integrated with [Anthropic's MCP Protocol](https://docs.cdp.coinbase.com/x402/welcome), Google Gemini, OpenAI Codex, and other platforms. Stablecoins like USDC make it possible to charge per request, per service, or per second of usage with near-zero transaction costs, enabling payments as low as $0.001 per request.

## Artifact reviews instead of diff reviews

When we want to do a rigorous code review traditionally, we look line by line at all the changes. But coding agents are getting to the point where they can prove their code works through artifacts. Instead of reviewing line by line, we can look at browser recordings, full working demos of a backend API, and other artifacts.

[Google Antigravity](https://developers.googleblog.com/en/build-with-google-antigravity-our-new-agentic-development-platform/) is a perfect example. As part of its coding process, it can autonomously spin up your website, visit it, scroll through it, take screenshots, and record everything. Agents generate artifacts, including tangible deliverables like task lists, implementation plans, screenshots, and browser recordings. You can verify the agent's logic at a glance.

[Amazon Nova Act](https://aws.amazon.com/blogs/aws/build-reliable-ai-agents-for-ui-workflow-automation-with-amazon-nova-act-now-generally-available/) takes this further. It enables AI agents to automate browser-based tasks like form filling, QA testing, and workflow validation with over 90% reliability. The service includes built-in observability through live viewing, CloudTrail logging, and session replay, making it possible to review what an agent actually did rather than parsing through code changes.

## Shipping code you've never read

For the last prediction, we're tying everything together. We've talked about reviewing artifacts instead of diffs, creating systems instead of coding, and the new capabilities for agents with code execution.

We're going to get to the point very quickly where we're shipping code that we have never read before. And I'm not talking about people who vibe code. Even experienced engineers are going to trust their systems so much that they have the ability to review the code but they're not going to. We're just going to ship to production after reviewing the artifacts.

I presented on this exact topic at [the Tel Aviv Pulumi User Group meetup at Qodo HQ](https://www.meetup.com/tel-aviv-pulumi-user-group/events/310498800/) back in October, where I demonstrated how Pulumi Neo's autonomous decision-making capabilities can handle infrastructure tasks that we traditionally managed manually. [Qodo](https://www.qodo.ai/) is doing fascinating work in this space with their agentic development tools, building systems that let you trust the output without necessarily reviewing every line.

I'm not saying we're taking the human completely out of the loop. I'm saying we're going to have a lot of trust in our systems and a validation process that includes us, but that doesn't necessarily have to be us actually looking at the code. Tools like Pulumi Neo create pull requests with clear documentation of changes, run previews to validate infrastructure modifications, and provide the transparency needed to ship with confidence.

## The path forward

The predictions I've outlined point to a fundamental shift in how software gets built and deployed. For DevOps engineers, this isn't a threat but an opportunity to become more strategic and less operational. We're entering the battle of the agentic frameworks, where the winners will be those who can build faster, cheaper agentic applications through their platforms.

The immediate reality is that your CI/CD pipelines need to accommodate AI-generated code at scale, your secrets management needs to handle multiple LLM providers, and your execution environments need proper sandboxing for agent-generated code. These aren't future concerns; they're requirements for working effectively with the AI tools available today.

Looking further out, the engineers who thrive will be those who embrace the system architect role. Define clear objectives and constraints for your AI agents. Build validation frameworks that can verify outcomes without requiring line-by-line code review. Design infrastructure that's modular enough to load capabilities on demand.

The technology to make this happen already exists. Agent orchestration platforms are shipping. Code execution is replacing tool calling. Progressive disclosure patterns are proven. The question isn't whether these changes are coming; it's whether you'll be ready when they arrive.

## Start building for the AI-driven future today

If you want to experience what this future looks like right now, [Pulumi Neo](/docs/ai/) is the place to start. Neo lets you make natural language requests for routine infrastructure tasks, analysis, and management. Instead of writing code for every operation, you describe what you need and Neo handles the implementation, creating task plans, running previews, and opening pull requests for your review.

Whether you're looking to update outdated resources across your infrastructure, analyze your cloud spend, or automate complex multi-step workflows, Neo provides the agent-first experience that's defining the next generation of DevOps tooling.

[Get started with Pulumi Neo](/docs/ai/get-started/) and see how AI-powered infrastructure automation can transform your workflow.
