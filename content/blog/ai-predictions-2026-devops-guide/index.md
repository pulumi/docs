---
title: "AI Predictions for 2027: A DevOps Engineer's Guide, With a 2026 Scorecard"
date: 2025-12-11
updated: 2026-10-27
meta_desc: "We scored our nine AI predictions for 2026 (1 right, 5 partly right, 3 wrong), then made five new ones for 2027 on agents, Kubernetes, and sovereignty."
authors:
    - engin-diri
tags:
    - ai
    - devops
    - platform-engineering
    - automation
    - kubernetes
    - aws
    - nova-forge
    - bedrock-agentcore
    - pulumi-neo
category: perspectives

social:
    twitter: "We scored our 9 AI predictions for 2026: 1 right, 5 partly right, 3 wrong. Then we made 5 new ones for 2027 on agent-driven infrastructure, Kubernetes as the AI substrate, and sovereignty."
    linkedin: |
        AI Predictions for 2027, with a scorecard for our 2026 calls

        In December 2025 we made nine predictions about AI and DevOps. We went back and scored them honestly:

        - 1 right (LLM providers specialize)
        - 5 partly right (agent-first IDEs, local AI hardware, engineers as architects, code execution and skills, A2A)
        - 3 wrong so far (machine payments at scale, artifact review replacing diffs, shipping unread code)

        Then the 2027 calls:

        - Agents become a primary author of infrastructure change
        - Kubernetes becomes the default substrate for AI workloads
        - Sovereignty gets enforced as code
        - Agent identity and audit become first-class infrastructure concerns
        - Agent standards consolidate while payments stay fragmented

        Each one ends with how we will score it next year.

        #AI #DevOps #PlatformEngineering #Kubernetes #CloudNative
---

In December 2025 we made nine predictions about how AI would change DevOps in 2026. Here is the scorecard: one right, five partly right, three wrong so far. Below, each original prediction is kept as written, followed by its verdict and evidence. After the scorecard come five predictions for 2027, each with a way to score it next year.

We kept the wrong calls in. A prediction post that only reports its hits is not worth citing.

<!--more-->

## How did our 2026 AI predictions hold up?

| 2026 prediction | Verdict | Evidence in one line |
| --- | --- | --- |
| IDEs are dead | **Partially right** | Agent-first products shipped, but the editor survives as one view |
| Providers will specialize | **Right** | Anthropic leads enterprise coding spend; OpenAI remains large |
| Local AI breakthrough | **Partially right** | The hardware arrived; mainstream adoption did not |
| Engineers as system architects | **Partially right** | Heavy delegation, low trust, verification is the hard part |
| Code execution replaces tool calling | **Partially right** | Skills and Code Mode won; MCP tool calling stayed |
| A2A goes mainstream | **Partially right** | Spec reached v1.0; no usage data shows MCP-scale adoption |
| Machines paying machines | **Wrong so far** | Backing arrived; volume is tens of millions of dollars |
| Artifact reviews replace diff reviews | **Wrong so far** | Review got stricter after incidents |
| Shipping code you've never read | **Wrong so far** | Trust is low and sign-off rules tightened |

The pattern is consistent. Where we predicted a shift in tooling or standards (agent-first interfaces, Agent Skills, MCP-centered protocols), we were mostly right about direction and too aggressive about replacement. Where we predicted a shift in human behavior (shipping unread code, trusting artifacts over diffs), we were wrong, because trust in AI output stayed low and review practice tightened after high-profile incidents.

### IDEs are dead (at least as we know them)

Traditional IDEs where the code is the focus of the interface are simply going to become irrelevant. We're moving toward agent manager interfaces where we can kick off agents in parallel to work on different features in a codebase or even work on different projects at the exact same time.

We're already seeing this transition. [Google Antigravity](https://developers.googleblog.com/en/build-with-google-antigravity-our-new-agentic-development-platform/) combines a familiar AI-powered coding experience with a new agent-first interface. You can deploy agents that autonomously plan, execute, and verify complex tasks across your editor, terminal, and browser. [Cursor 2.0](https://cursor.com/changelog/2-0) lets you run up to eight agents in parallel on a single prompt, using git worktrees or remote machines to prevent file conflicts. Each agent operates in its own isolated copy of your codebase.

AWS validated this direction at [re:Invent 2025](/blog/aws-reinvent-2025-roundup/) by announcing "frontier agents" including Kiro for autonomous coding, along with dedicated security and DevOps agents. These agents maintain state, log actions, operate with policy guardrails, and integrate directly with CI/CD pipelines.

For infrastructure specifically, [Pulumi Neo](/docs/ai/get-started/neo/) represents this same shift. Instead of writing code or running CLI commands for every operation, you describe what you need in natural language and Neo handles the implementation. It works across your entire infrastructure, understanding dependencies and creating execution plans that go through pull requests for review.

For DevOps engineers, this means your pipelines need to accommodate AI-generated code at scale. Multiple agents working simultaneously need isolated, reproducible environments. More generated code means more artifacts to track, version, and deploy.

**Verdict: Partially right.** The direction held. Cursor 3.0 was, in [Every's review](https://every.to/vibe-check/cursor), "a rebuilt product made for dispatching, monitoring, and managing AI agents rather than manually writing code," and the same piece argues that Claude Code "shifted the dominant coding paradigm away from pair programming—which requires a code editor—toward agent delegation and orchestration—which doesn't." [Futurum's read of Cursor 3.2](https://futurumgroup.com/insights/cursor-3-2-reframes-the-ide-as-an-agent-execution-runtime/) describes the editor as "a single view within a broader agentic system rather than as the product center." The word "dead" was too strong, though. The editor survives as one view among several, and Every also judged Cursor's rebuilt product "still too early in its lifecycle" to compete with the more mature orchestration offerings from Anthropic and OpenAI.

### The different paths to AI dominance

A lot of people think that in the future, a single large language model will have a monopoly and be the best at absolutely everything. But what's really going to happen is different providers will specialize and focus on being the best at different things.

Google is going down the generalist route with Gemini, aiming to be the jack-of-all-trades. Anthropic is focusing on being the best for coding. You can see this in the benchmarks: when Opus 4.5 came out, the first benchmark they highlighted was for software engineering, because that's what Anthropic is focusing on.

Amazon is carving out its own niche with the [Nova model family](https://www.aboutamazon.com/news/aws/aws-agentic-ai-amazon-bedrock-nova-models), announced at re:Invent 2025. The Nova 2 lineup includes specialized models: Pro for complex reasoning, Sonic for real-time voice conversations, and Omni for simultaneous text, audio, and video processing. With [Nova Forge](/blog/aws-reinvent-2025-roundup/#rent-the-lab-nova-forge), organizations can build custom frontier models by combining their proprietary data with AWS open weight models. The re:Invent message was clear: leveraging your first-party data is now fundamental to going beyond generic AI. We're talking about 30-40% increases in accuracy when you bring your own data into the equation.

But here's the hot take: I don't think OpenAI is going to come out on top with any kind of specialization. They've [disappointed time and time again](https://garymarcus.substack.com/p/gpt-5-overdue-overhyped-and-underwhelming) with GPT-5 and GPT-4.5. With 4.5, they seemed to try to be the creative specialist, but it just didn't work. The [GPT-5 launch in August 2025](https://www.axios.com/2025/08/12/gpt-5-bumpy-launch-openai) was described as "barely better than last month's flavor of the month" and on some metrics it's actually worse than earlier models.

For DevOps teams, this specialization means you'll need infrastructure that's model-agnostic and supports multiple AI backends. Plan for secrets management across multiple LLM providers and design your systems to swap models based on the task at hand.

**Verdict: Right.** The specialization half of the call held up. Based on [Menlo Ventures survey data](https://www.sentisight.ai/openai-vs-anthropic-sales-success/) as reported in September 2026, Anthropic holds about 40% of enterprise LLM API spending against OpenAI's 27%, and Claude commands roughly 54% of enterprise AI coding usage against about 21% for Codex. The hot take that OpenAI would not win through specialization needs a caveat. The same report puts OpenAI at more than 900 million weekly ChatGPT users and annualized revenue above $40 billion in August 2026, so it is far from out. It just is not the specialist leader in coding. We also found no 2026 adoption data for Amazon's Nova niche, so we are not scoring that part.

### The local AI breakthrough

2026 will be the year of local AI. We didn't see that much this year besides DeepSeek at the start of 2025, which was a big deal. We had a couple of new models like Qwen 3, but nothing that fundamentally changed the game. Now we're starting to see new hardware that makes it obvious we're going to be able to run very large models on smaller devices.

There's new AI chips that can run upwards of 120 billion parameter large language models on the edge, which would be a complete game-changer. Right now, hardware requirements are one of the biggest challenges for scaling local AI. If we can solve the hardware problem, we get 100% data privacy and zero-millisecond latency for our agents.

AWS is addressing this with [Trainium3 UltraServers](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/), their 3nm AI chips delivering 4.4x more compute than the previous generation. More significantly, [AWS AI Factories](https://www.geekwire.com/2025/amazon-unveils-frontier-agents-new-chips-and-private-ai-factories-in-aws-reinvent-rollout/) allow organizations to deploy racks of Trainium chips and NVIDIA GPUs directly into their own data centers, addressing data sovereignty concerns while keeping AI inference close to the data.

For DevOps, this opens the door to zero-latency inference in CI/CD pipelines, complete data privacy for sensitive codebases, and reduced cloud costs for AI-heavy workloads.

**Verdict: Partially right.** The hardware arrived. [TechRadar's DGX Spark coverage](https://www.techradar.com/pro/so-freaking-cool-first-reviews-of-nvidia-dgx-spark-leave-absolutely-no-doubt-this-may-be-nvidias-apple-mac-moment) describes a small box with 128GB of unified memory that lets users "load and run large language models locally without relying on cloud infrastructure," which is the class of machine that can host a 120B-parameter model. We could not find adoption data that makes 2026 "the year of local AI," though. Local inference remains a developer and enthusiast practice, while enterprise demand for private AI is being met through on-premises racks from the hyperscalers, as the AWS AI Factories announcement showed. The sovereignty demand we pointed to is real, and it shows up again in our 2027 predictions below.

### Engineers as system architects

We're finally going to get to the point where we're not the coders. We delegate that entirely to our coding agents, and we become the system architects. This mirrors the evolution of other engineering disciplines. Civil engineers don't fabricate the steel beams; they design the structure and verify the integrity.

I think of this as a three-step process:

1. **Define**: Set your objectives and the system that your agents will operate under
1. **Orchestrate**: Delegate the coding to your agents
1. **Validate**: Ensure the quality of the outputs and the overall system

We're still in the loop. We are the final say in whatever is created, but we're delegating the grunt work to our coding agents.

This is exactly the model that [Pulumi Neo](/docs/ai/concepts/neo/tasks/) implements for infrastructure. When you give Neo a complex request, it creates a task plan outlining the steps it will take to accomplish your goal. This plan provides transparency into Neo's approach and gives you the opportunity to adjust the strategy before execution begins. Neo operates in different modes: Review mode where previews, deployments, and pull requests need approval, Balanced mode where only deployments need sign-off, or Auto mode where Neo requests no approvals. You define the boundaries, Neo orchestrates the work, and you validate through pull requests and previews.

For DevOps engineers, this shift means building robust validation infrastructure becomes critical. When AI writes the code, you need automated testing pipelines, security scanning, and verification systems that can operate at the speed of AI-generated changes.

**Verdict: Partially right.** Engineers are delegating a lot, but they are not delegating everything. The [Stack Overflow 2026 survey](https://www.theregister.com/software/2026/10/10/stack-overflow-survey-finds-devs-hooked-on-ai-but-not-totally-sold-on-its-judgment/5301662/), covered by The Register, received 30,903 responses, and about 80 percent of daily AI users reported using the tools for at least an hour a day. The same coverage reports that only about 7 percent of developers trusted AI output for important work decisions, while 48 percent trusted it when they could easily verify it. The architect role is emerging, and the Validate step in Define, Orchestrate, Validate turned out to be the hard part.

### Code execution is replacing tool calling

Here's a key insight that kept coming up at re:Invent: models are no longer the bottleneck. Context is. Our agents are going to change a lot next year because code execution is starting to replace tool calling. The problem with tool calling right now is that all the capabilities you give an agent take up context upfront. When you try to give a lot of different tools to an agent, you completely overwhelm it.

[Anthropic's research on code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) addresses exactly this problem. Code execution is a massive token reduction, faster, and more flexible. You're giving the agent the ability to generate its own capabilities at runtime by writing code to interact with APIs. A workflow that previously consumed about 150,000 tokens when tools were passed directly through the model was reimplemented with code execution and used only about 2,000 tokens. That's a 98.7% reduction.

AWS embraced this pattern with [Amazon Bedrock AgentCore](https://www.aboutamazon.com/news/aws/amazon-sagemaker-ai-amazon-bedrock-aws-ai-agents), which now includes code interpretation capabilities. AgentCore supports any agent framework (CrewAI, LangGraph, OpenAI SDK) and provides memory, browser tools, and observability features that make code execution practical at enterprise scale.

For DevOps, this means you need sandboxed, secure execution environments for AI-generated code. Running agent-generated code requires appropriate isolation, resource limits, and monitoring.

#### Progressive disclosure and composable skills

The best part about code execution flexibility is it unlocks progressive disclosure. All I mean by that is: you have a lot of capabilities for an agent, but you don't actually give all of them upfront. Instead, you allow the agent to discover capabilities and then leverage them in a more flexible way.

For each capability, you just have a bit of metadata or description that loads upfront. When the agent decides to leverage that capability, then you load the full instructions. Now you can practically scale to infinity because all capabilities don't have to be loaded at runtime.

[Claude Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) is a good example of this pattern. Skills are organized folders of instructions, scripts, and resources that agents can discover and load dynamically. At session start, the agent scans available skills and populates the system prompt with just a brief name and description (around 100 tokens). The full skill prompt loads only after Claude selects it, preventing context bloat while maintaining discoverability.

[Kiro Powers](https://kiro.dev/powers/) addresses the same problem. Connecting five MCP servers can consume over 50,000 tokens, roughly 40% of an AI model's context window, before you even type your first request. Powers bundle MCP servers, steering files, and hooks into units that load dynamically based on conversation context. Mention "payment" and the Stripe power activates. [Datadog, Figma, and others](https://venturebeat.com/ai/aws-launches-kiro-powers-with-stripe-figma-and-datadog-integrations-for-ai) have powers available.

For DevOps, this translates to modular infrastructure definitions, on-demand capability loading, and efficient resource utilization. Think about how you can apply this pattern to your own automation.

{{< blog/cta-card title="Equip your agents with Pulumi skills" href="/docs/ai/concepts/agent-skills/" >}}
Give Claude Code, Cursor, or any coding agent working Pulumi patterns through Agent Skills and the Pulumi MCP server, so it generates infrastructure that deploys.
{{< /blog/cta-card >}}

**Verdict: Partially right.** Progressive disclosure won. In October 2026 Anthropic [donated the Agent Skills standard to the Linux Foundation's Agentic AI Foundation](https://simonwillison.net/2026/Oct/22/donating-agent-skills/), saying it is "committed to keeping Agent Skills open, community-driven, and vendor-neutral." Code execution also reached production scale. Cloudflare reports that its Code Mode MCP server "has scaled up to thousands of requests per second and served billions of tool calls." Tool calling did not go away, however. Cloudflare's [MCP update](https://blog.cloudflare.com/mcp-v2) says the 2026-07-28 spec makes MCP "a fully stateless protocol," so the standard tool interface got stronger while code execution layered on top of it. "Replacing" overstated it.

### Agent-to-agent protocols are finally happening

Agent-to-agent protocols are where AI agents operate in a peer network, discover each other's capabilities in real time, and interact autonomously. When Google released their [A2A protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) earlier this year, there was a ton of buzz. A lot of people thought it was going to be the next big standard, like the next MCP. But then it kind of fell to the wayside.

The big reason is the chicken-and-egg problem. For A2A to be useful, you need many people to adopt it at the same time. Otherwise, if you build an A2A-compatible agent, it has no other agents to talk to. The whole value proposition is lost unless you already have a big network to attach to.

But that's finally changing. The [Linux Foundation launched the A2A project](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) in June 2025, and adoption is accelerating. Adobe, Microsoft, SAP, ServiceNow, and S&P Global are all implementing A2A. In July 2025, Google released [version 0.3 of the A2A protocol](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade) with a more stable interface critical to accelerating enterprise adoption.

**Verdict: Partially right.** A2A matured as a standard. The project's [GitHub releases](https://github.com/a2aproject/A2A/releases) now include v1.0.0 and v1.0.1, a long way from the v0.3 we cited. We could not find usage-volume data showing agents actually talking to each other over A2A at a scale comparable to MCP. Cloudflare's post calls MCP "the universal standard for how agents interact with external services," which is the position we expected A2A to contest. The spec is ready, and the network effect we described has not visibly arrived.

### Machines paying machines

My next big prediction is that machines paying machines is going to become a very big thing. [Coinbase released the x402 protocol](https://www.coinbase.com/developer-platform/discover/launches/x402) for exactly this: building AI agents that you expose over the internet but require payment whenever someone else interacts with them.

This goes really well with agent-to-agent protocols. You can create a peer network where you monetize your agents. They all leverage each other but make payments whenever they take advantage of another agent's capabilities. Cryptocurrency is the perfect solution for this kind of machine-to-machine network because it enables micropayments to be made quickly and globally.

The x402 protocol has achieved [156,000 weekly transactions with 492% growth](https://www.coingecko.com/learn/x402-autonomous-ai-agent-payment-coinbase) since launching in May 2025. It's now integrated with [Anthropic's MCP Protocol](https://docs.cdp.coinbase.com/x402/welcome), Google Gemini, OpenAI Codex, and other platforms. Stablecoins like USDC enable charging per request, per service, or per second of usage at near-zero transaction costs, enabling payments as low as $0.001 per request.

**Verdict: Wrong so far.** The institutional backing arrived and the volume did not. The Linux Foundation announced the [operational launch of the x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications) with 40 members in July 2026. On the usage side, [one October 2026 roundup](https://www.patechlabs.com/news/ai-agent-payments-guide-x402-ap2-mpp-visa-mastercard) reports that the x402.org counter shows 75.41 million transactions and $24.24 million in volume over the last 30 days, and notes that the counter "does not disclose its method." That is a lot of transactions and a small amount of money, which is not the "very big thing" we predicted. The same roundup shows agent payments splitting across several competing protocols rather than converging on one.

### Artifact reviews instead of diff reviews

When we want to do a rigorous code review, traditionally, we look line by line at all the changes. But coding agents are getting to the point where they can prove their code works through artifacts. Instead of reviewing line by line, we can look at browser recordings, full working demos of a backend API, and other artifacts.

[Google Antigravity](https://developers.googleblog.com/en/build-with-google-antigravity-our-new-agentic-development-platform/) is a perfect example. As part of its coding process, it can autonomously spin up your website, visit it, scroll through it, take screenshots, and record everything. Agents generate artifacts, including tangible deliverables like task lists, implementation plans, screenshots, and browser recordings. You can verify the agent's logic at a glance.

[Amazon Nova Act](https://aws.amazon.com/blogs/aws/build-reliable-ai-agents-for-ui-workflow-automation-with-amazon-nova-act-now-generally-available/) takes this further. It enables AI agents to automate browser-based tasks like form filling, QA testing, and workflow validation with over 90% reliability. The service includes built-in observability through live viewing, CloudTrail logging, and session replay, making it possible to review what an agent actually did rather than parsing through code changes.

**Verdict: Wrong so far.** Agents do produce artifacts now, but we found no evidence that artifact review replaced diff review. The industry moved the other way after incidents. Following outages tied to AI coding tools, [Amazon was reported](https://tech.yahoo.com/articles/ai-code-wreaked-havoc-amazon-160849695.html) to require that "engineers must get two people to review changes before deployment." Futurum's analysis of Cursor 3.2 also flags that [governance and observability gaps](https://futurumgroup.com/insights/cursor-3-2-reframes-the-ide-as-an-agent-execution-runtime/) "widen as parallel subagents fan out." Artifacts are useful evidence, and review practice is getting stricter rather than lighter.

### Shipping code you've never read

For the last prediction, we're tying everything together. We've talked about reviewing artifacts instead of diffs, creating systems instead of coding, and the new capabilities for agents with code execution.

We're going to get to the point very quickly where we're shipping code that we have never read before. And I'm not talking about people who vibe code. Even experienced engineers are going to trust their systems so much that they have the ability to review the code but they're not going to. We're just going to ship to production after reviewing the artifacts.

I presented on this exact topic at [the Tel Aviv Pulumi User Group meetup at Qodo HQ](https://luma.com/pulumi) back in October, where I demonstrated how Pulumi Neo's autonomous decision-making capabilities can handle infrastructure tasks that we traditionally managed manually. [Qodo](https://www.qodo.ai/) is doing fascinating work in this space with their agentic development tools, building systems that let you trust the output without necessarily reviewing every line.

The claim kept the human in the loop: we would trust our systems and run a validation process that includes us, without necessarily reading the code ourselves. Tools like Pulumi Neo create pull requests with clear documentation of changes, run previews to validate infrastructure modifications, and provide the transparency needed to ship with confidence.

**Verdict: Wrong so far.** This was the boldest call and the data does not support it as a norm. Only about 7 percent of developers in the [Stack Overflow survey](https://www.theregister.com/software/2026/10/10/stack-overflow-survey-finds-devs-hooked-on-ai-but-not-totally-sold-on-its-judgment/5301662/) trusted AI output for important work decisions. The best-known 2026 incident, which [Yahoo Tech's recap](https://tech.yahoo.com/articles/ai-code-wreaked-havoc-amazon-160849695.html) says caused 120,000 lost orders and 1.6 million website errors on March 2, 2026, led to more human sign-off, not less. Some engineers certainly ship code they have not read. It has not become the accepted practice for experienced teams.

## AI predictions for 2027

The 2026 scorecard suggests a rule for 2027: bet on infrastructure, standards, and constraints, and be skeptical of predictions that need people to change how much they trust a system. The five predictions below follow that rule. They center on three themes: agent-driven infrastructure change, Kubernetes as the substrate for AI, and sovereignty pressure.

### Agents become a primary author of infrastructure changes

By the end of 2027, agents will write more infrastructure changes than humans do on many platform teams, and the human job will be approving previews, policy results, and pull requests. This is the narrower, safer version of last year's "never read the code" call, and it has better support.

The numbers are already moving. Pulumi's [State of Agentic Infrastructure 2026](/state-of-agentic-infrastructure/) survey of 510 platform, DevOps, and product engineers found that 81% let agents change production, but almost all of that is gated: "with approval" (62%) far outweighs "autonomously" (19%). Its takeaway: "Speed is solved; control isn't." Our [explainer on agentic infrastructure](/what-is/what-is-agentic-infrastructure/) reports that as of May 2026 LLMs were doing over 20% of infrastructure deployments, up from nearly zero a year earlier.

An infrastructure agent like [Pulumi Neo](/product/neo/) fits this shape: it plans, runs previews, and opens pull requests, while approval modes decide how much a human signs off. Expect the approval gates to become the product surface that teams argue about.

The risk is cost and quality. [Gartner predicts](https://www.langchain.com/blog/what-is-an-agent) that more than 40% of agentic AI projects will be canceled by the end of 2027 because of escalating costs, unclear business value, or inadequate risk controls. Teams with previews, tests, and policy in place will be on the right side of that line.

**How we'll score this in 2027:** Right if a comparable late-2027 survey shows agents authoring infrastructure code as a top-three agent use (it trailed every other use at 29% in the 2026 survey) while the autonomous share of production changes stays under 40%.

### Kubernetes becomes the default substrate for AI workloads

Inference, agent runtimes, and GPU scheduling will converge on Kubernetes, and teams will stop treating AI infrastructure as a separate stack. This prediction is about plumbing, which is where our 2026 calls held up best.

The groundwork is public. The [CNCF 2025 Annual Survey](https://www.linuxfoundation.org/research/cncf-2025-annual-survey) names "Kubernetes' evolution from container orchestrator to AI infrastructure platform" as one of its three main themes. Dynamic Resource Allocation, the Kubernetes mechanism for requesting GPUs and other devices, [graduated to GA in Kubernetes 1.34](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/). The Kubernetes SIGs project [agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) targets "isolated, stateful, singleton workloads, ideal for use cases like AI agent runtimes." CNCF also established a [Certified Kubernetes AI Conformance program](https://www.cncf.io/news/2025/11/18/forbes-cncf-establishes-standards-for-running-ai-workloads-on-kubernetes/) as a community-defined standard for running AI workloads consistently.

For platform teams, this means the cluster you already operate becomes the place where agents run, and sandboxing and resource quotas for agent-generated code become normal platform work. We covered the mechanics in [AI agents on Kubernetes](/blog/ai-agents-on-kubernetes/) and [Kubernetes agent sandboxes](/blog/kubernetes-agent-sandbox/).

**How we'll score this in 2027:** Right if the next CNCF annual survey lists AI workloads among the leading new uses of production Kubernetes and the AI Conformance program covers the major managed Kubernetes services.

### Sovereignty becomes a procurement requirement that teams enforce as code

Data residency and operator-jurisdiction rules will move from legal documents into deployment pipelines in 2027. This carries forward the sovereignty thread from our local AI call, which was right about the demand and wrong about the mechanism.

The supply side is here. AWS announced that the [AWS European Sovereign Cloud is generally available](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/) to all customers. On the regulatory side, the European Commission adopted its [Cloud and AI Development Act proposal on 3 June 2026](https://digitalhorizon.hannessnellman.com/ai-strategy/cloud-and-ai-development-act-cada/), and it is now under consideration by the European Parliament and the Council. The EU Data Act also takes a step in 2027: from 12 January 2027, [providers may no longer impose switching charges](https://www.loyensloeff.com/insights/news--events/news/data-act-requirements-on-customer-switching-and-portability/) on customers moving between data processing services.

Taken together, teams will be asked to prove where workloads run and to keep the option of moving them. That is a job for policy as code and infrastructure as code: region allow-lists, residency checks in previews, and portable definitions that work across clouds. Pulumi Policies can enforce rules like these before a deployment happens.

**How we'll score this in 2027:** Right if the Cloud and AI Development Act clears both Parliament and the Council in 2027 with its public-sector sovereignty provisions intact, and at least one other major cloud provider launches a dedicated sovereign region.

### Agent identity, permissions, and audit become first-class infrastructure concerns

Every serious agent deployment in 2027 will have its own identity, scoped short-lived credentials, and an audit trail, because the 2026 incidents made the cost of skipping them visible. This follows directly from the scorecard: low trust is rational.

Only about 7 percent of developers in the [Stack Overflow 2026 survey](https://www.theregister.com/software/2026/10/10/stack-overflow-survey-finds-devs-hooked-on-ai-but-not-totally-sold-on-its-judgment/5301662/) trusted AI output for important work decisions. After AI coding tools contributed to a March 2026 incident with 120,000 lost orders, [Amazon was reported](https://tech.yahoo.com/articles/ai-code-wreaked-havoc-amazon-160849695.html) to have added formal approval processes and stricter automated checks. The Pulumi survey above shows the same gap from the other side: trust in agents is high, while guardrails lag.

Infrastructure teams own the fix. Secrets and configuration need to hand agents the minimum credentials for the task, and policy needs to evaluate what an agent proposes before it applies. Teams that treat an agent like a service account with a reviewer, rather than a colleague with admin rights, will have fewer incidents to explain.

**How we'll score this in 2027:** Right if the major agent platforms and cloud providers document per-agent identities with scoped, short-lived credentials as the default pattern, and a public postmortem in 2027 cites missing agent permission boundaries as a root cause.

### Agent standards consolidate while agent payments stay fragmented

Agent protocols will keep consolidating under the Linux Foundation, and no single payment protocol will win in 2027. This is the correction to two of our 2026 calls.

On standards, MCP, and now [Agent Skills](https://simonwillison.net/2026/Oct/22/donating-agent-skills/), sit under the Linux Foundation's Agentic AI Foundation, and A2A has reached 1.0. Neutral governance lowers the risk of building on them, which is what enterprise adoption needs. On payments, the [x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications) launched with 40 members, but one [October 2026 roundup](https://www.patechlabs.com/news/ai-agent-payments-guide-x402-ap2-mpp-visa-mastercard) describes several competing agent payment protocols, including Google's AP2 and card-network efforts, with volumes still small in dollar terms.

For DevOps teams, the practical advice is to build on the standards under neutral governance and keep payment integrations behind an interface you can swap.

**How we'll score this in 2027:** Right if no single agent payment protocol is accepted by a majority of the largest merchants and payment networks by the end of 2027, and at least one more major agent standard moves under Linux Foundation governance.

## The path forward

The scorecard and the 2027 predictions point the same way. AI changes how software gets built faster than it changes how much people trust it, so the winning infrastructure makes agent work reviewable, constrained, and reversible. For DevOps engineers that is an opportunity to become more strategic and less operational.

The immediate requirements have not changed. Your CI/CD pipelines need to accommodate AI-generated code at scale, your secrets management needs to handle multiple LLM providers, and your execution environments need proper sandboxing for agent-generated code. Add three from this year's scorecard: previews and policy checks that run before any agent change applies, identities and audit trails for the agents themselves, and region and residency rules written as code.

The engineers who thrive will embrace the system architect role. Define clear objectives and constraints for your AI agents. Build validation frameworks that can verify outcomes. Design infrastructure that is modular enough to load capabilities on demand. The technology to do all of this ships today, and the open question for 2027 is how many teams will have the guardrails in place when agents write most of the changes.

## Start building for the AI-driven future today

If you want to see agent-driven infrastructure change in practice, the fastest path is Pulumi Neo. Neo takes natural language requests for routine infrastructure tasks, analysis, and management, then creates task plans, runs previews, and opens pull requests for your review. Whether you are updating outdated resources, analyzing cloud spend, or automating multi-step workflows, you stay in control through approval modes and plan review.

- [**Get started with Pulumi Neo**](/docs/ai/get-started/neo/) and run your first task with previews and approvals in place.
- **Project**: [Build a production-ready AI agent](/blog/from-works-on-my-machine-to-production-ready-ai-agents-with-amazon-bedrock-agentcore/) by moving from local prototypes to deployed infrastructure with Amazon Bedrock AgentCore, the Strands SDK, and Pulumi.
