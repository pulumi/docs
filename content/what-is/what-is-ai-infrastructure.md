---
title: "What Is AI Infrastructure?"
meta_desc: "AI infrastructure is the compute, data, orchestration, and control-plane layers AI workloads run on. Learn what it includes and how teams build it."
type: what-is
page_title: "What Is AI Infrastructure?"
authors: ["pulumi-content-team"]
---

AI infrastructure is the compute, data, orchestration, and control-plane layers that training and inference workloads run on, plus the tooling teams use to provision, govern, and operate it. That includes accelerators and networking, data pipelines and storage, model-serving and orchestration frameworks, and the infrastructure-as-code and policy layer that defines, changes, and secures the rest. This page covers what belongs in each layer, how AI infrastructure differs from the cloud infrastructure teams already run, and how cloud engineering teams actually build and operate it, including with AI agents doing part of the work.

## What counts as AI infrastructure?

AI infrastructure is every layer a model needs to train, serve, and stay operable in production: the hardware that does the math, the data it learns from, the software that schedules and serves the work, and the control plane that provisions and governs all of it. Most definitions stop at the hardware and orchestration layers. The control plane is just as load-bearing, because none of the other layers exist until something provisions them.

### The five layers of AI infrastructure

| Layer | What it does | Examples |
| --- | --- | --- |
| Accelerators and networking | Runs the matrix math for training and inference at scale | GPUs and TPUs, high-bandwidth interconnects, specialized AI clusters from providers like CoreWeave and Lambda |
| Data | Feeds, versions, and retrieves the data models train and reason on | Object storage, feature stores, vector databases, data pipelines |
| Orchestration and scheduling | Packs workloads onto accelerators and keeps them running | Kubernetes, Kueue, Dynamic Resource Allocation (DRA), job schedulers |
| Serving and MLOps | Runs models in production and tracks their behavior over time | KServe, vLLM, MLflow, Weights & Biases |
| Control plane | Provisions, versions, tests, and governs everything above it | Infrastructure as code, policy as code, secrets management, CI/CD |

Most AI infrastructure guides treat that fifth layer as an afterthought, often a single line naming a provisioning tool. That is a gap worth naming directly: an AI stack that nobody can safely change, audit, or roll back is not production infrastructure, it is a demo.

## How is AI infrastructure different from traditional cloud infrastructure?

AI infrastructure runs the same clouds and the same provisioning tools as traditional infrastructure, but it carries different constraints: accelerator scarcity and cost, workloads that hold state across long-running training jobs, and consumers (both people and AI agents) that need to change infrastructure far more often than a typical web service does. Traditional cloud infrastructure optimizes for steady-state reliability. AI infrastructure optimizes for iteration speed under real hardware constraints.

### AI infrastructure vs. traditional cloud infrastructure

| Dimension | Traditional cloud infrastructure | AI infrastructure |
| --- | --- | --- |
| Primary bottleneck | Cost of general-purpose compute | Accelerator supply and cost |
| Workload shape | Mostly stateless services, autoscaled | Long-running training jobs plus latency-sensitive inference |
| Change frequency | Weekly or monthly releases | Continuous, often multiple changes a day, increasingly agent-driven |
| Who requests changes | Developers and operators | Developers, operators, and AI agents and coding assistants |
| Governance surface | Access control and cost policy | Access control, cost policy, and validation of AI-generated changes |

The last two rows are where the category is actually moving. Cloud engineering teams building for AI workloads are not just racking up more compute. They are redesigning who and what is allowed to touch that compute, and how fast.

## What role does infrastructure as code play in AI infrastructure?

Infrastructure as code is how teams provision, version, and repeatedly reproduce every layer of an AI stack, from the Kubernetes cluster running inference to the policies that gate who can change it. It matters more for AI infrastructure than for traditional infrastructure because AI stacks change constantly and increasingly get changed by AI agents rather than only by people, so the interface an agent or engineer uses to make that change determines how fast and how safely it happens.

### What the research shows about agents and infrastructure interfaces

A University of Michigan and UC Berkeley study, ["Cloud Infrastructure Management in the Age of AI Agents"](https://arxiv.org/abs/2506.12270) (Yang et al., June 2025), measured how AI agents perform common Azure infrastructure tasks across four interfaces: cloud SDKs, the CLI, infrastructure-as-code templates, and a browser-based console (ClickOps).

| Interface | Provisioning success rate | Update success rate | Monitoring success rate |
| --- | --- | --- | --- |
| SDK | 0.67 | 0.67 | 0.80 |
| CLI | 1.0 | 0.67 | 0.80 |
| Infrastructure as code | 1.0 | 0.33 | 0.40 |
| Web console (ClickOps) | 0.33 | 0.67 | 1.0 |

The results are a genuine mixed bag, not a clean win for any one interface. Infrastructure as code gave agents a perfect provisioning success rate and let them handle it in a fixed number of steps regardless of how many resources were involved, because a coding agent generates a program the same way whether it describes five resources or fifty. The same interface struggled on updates and monitoring: the researchers found that "IaC's state-centric design only captures the infrastructure composition, but cannot easily retrieve runtime telemetry; thereby struggling the most for monitoring tasks." The browser console, by contrast, was catastrophically inefficient. The study found "the ClickOps agent needed around 30x more steps than the CLI agent" to complete the same provisioning work.

The takeaway for AI infrastructure builders is not that any single interface wins outright. It is that the interface you hand an agent changes its success rate and efficiency by a wide margin, and that agents need both code they can generate reliably and live access to the infrastructure state and telemetry that code alone does not carry.

That interface question is already playing out at platform scale. Kubernetes now runs in production for [82% of container users, up from 66% in 2023](https://www.prnewswire.com/news-releases/kubernetes-established-as-the-de-facto-operating-system-for-ai-as-production-use-hits-82-in-2025-cncf-annual-cloud-native-survey-302663249.html), and 66% of organizations hosting generative AI models use it to manage some or all of their inference workloads, per the CNCF's 2025 Annual Cloud Native Survey. Google Cloud's [2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) found that 90% of organizations have adopted at least one internal platform, and found a direct correlation between platform quality and an organization's ability to get value out of AI, with 90% of surveyed technology professionals now using AI at work. The infrastructure layer AI runs on is converging on the same platforms, and increasingly the same automated interfaces, that the rest of software engineering already uses.

## What makes infrastructure as code agent-ready?

Agent-ready infrastructure as code is written in a language and structure that an AI agent can generate, test, and change with the same reliability a human engineer expects from real software, plus a way to preview and audit every change before and after it happens. A YAML file or a proprietary configuration language gives an agent no compiler, no type system, and no test framework to lean on. A general-purpose language gives it all three, plus the ecosystem of linters, IDEs, and CI pipelines coding agents already operate inside.

### Properties of agent-ready infrastructure

- Written in a real programming language (Python, TypeScript, Go, C#, or Java), so agents can use the same generation, testing, and refactoring patterns they already use for application code.
- Previewable before it runs, so an agent's proposed change is visible as a diff before it touches anything live.
- Auditable after it runs, showing what changed, when, and by whom, including which changes came from an agent.
- Governable by policy, so guardrails apply automatically regardless of whether a human or an agent proposed the change.
- Composable, so agents and engineers can reuse the same components instead of regenerating the same resource definitions from scratch.

{{< pullquote attribution="Joe Duffy, Co-Founder and CEO, Pulumi" >}}
Just as we wouldn't vibe code without git showing us the source changes, we shouldn't vibe infrastructure without a tool that shows what it will do before it does it, and what it has already done in the past. It's like git diff for your infrastructure.
{{< /pullquote >}}

That preview-and-audit discipline is already showing up in the numbers. Pulumi's own telemetry, [published in May 2026](/blog/the-agentic-infrastructure-era/), shows that "LLMs are now doing over 20% of the infrastructure deployments, up from virtually zero a year ago," with that share expected to pass 50% before the end of the year. Agent-generated infrastructure changes are no longer a hypothetical; they are already a meaningful fraction of how infrastructure gets shipped.

## How do AI agents operate AI infrastructure today?

AI agents operate AI infrastructure the same way engineers do: through a coding interface, with a defined scope of what they can touch and what needs a human sign-off. In practice that means a coding agent or infrastructure agent generates or proposes a change, an automated preview shows what it will do, policy checks run against it, and either an automated pipeline or a human approves it before it goes live.

### Where agents plug into the loop

| Entry point | What the agent does |
| --- | --- |
| Coding assistant or IDE agent | Writes or edits infrastructure-as-code programs alongside application code |
| Model Context Protocol (MCP) server | Lets an agent query live stack and resource state, search an organization's cloud estate, and read registry documentation before proposing a change |
| Infrastructure agent (for example, Pulumi Neo) | Investigates existing infrastructure, proposes changes as code, runs previews, and opens pull requests |
| CI/CD pipeline | Runs the same preview, test, and policy checks on agent-authored changes as on human-authored ones |
| Policy gate | Blocks or flags changes, from any author, that violate a defined guardrail before they apply |

This is consistent with where platform teams see the category heading. Platform engineering analyst Luca Galante's ["10 Platform engineering predictions for 2026"](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026) argues that "by 2026, mature platforms will treat agents like any other user persona, complete with RBAC permissions, resource quotas, and governance policies." Agents are not a special case bolted onto infrastructure tooling. They are a user type the tooling needs to support with the same access controls it already applies to people.

Pulumi's [MCP server](/docs/ai/mcp-server/) and [Neo](/product/neo/) are built around that same principle: give an agent grounded access to real stack state, and route what it proposes through the same preview and policy path a human change would go through. For a deeper look at how the protocol itself works, see [what MCP means for infrastructure as code](/what-is/mcp-for-infrastructure-as-code/). For how agents actively managing infrastructure differs from infrastructure that merely supports agent workloads, see [what agentic infrastructure is](/what-is/what-is-agentic-infrastructure/).

## How do teams govern AI infrastructure and AI-generated changes?

Teams govern AI infrastructure the same way they govern any production infrastructure, with policy as code, secrets management, drift detection, and human-in-the-loop approvals, applied consistently regardless of whether a person or an agent proposed the change. The one addition AI-generated changes require is treating the platform itself as a reviewer, not just a delivery mechanism.

### Guardrails that hold up in production

- **Policy as code** evaluates every proposed change, human or agent-authored, against organizational rules before it can apply. See [what policy as code is](/what-is/what-is-policy-as-code/) and [Pulumi Policies](/docs/insights/policy/), Pulumi's implementation.
- **Secrets and configuration management** keeps credentials out of code and out of an agent's prompt context. See Pulumi's [secrets management](/product/secrets-management/).
- **Drift detection and inventory** catch infrastructure that diverged from what is declared, whether a person clicked around in a console or an agent applied a change outside the normal path. See Pulumi's [insights and governance](/product/insights-governance/) capabilities.
- **Human-in-the-loop approval** keeps a person in the decision path for changes above a defined risk threshold, even when an agent generated the change.
- **Change previews** show exactly what a proposed change will do before it runs, and a record of what already ran, for both human and agent authors.

Galante's second 2026 prediction, ["Platforms become the safety net for AI-generated code,"](https://platformengineering.org/blog/10-platform-engineering-predictions-for-2026) makes the same point from the platform engineering side: "as developers increasingly rely on AI to generate infrastructure code, Terraform configurations, and Kubernetes manifests, platforms must serve as the primary reviewer and auto-remediator." The risk he calls out is specific and mundane: "an LLM might invent a plausible-looking Kubernetes API field that passes linting but fails in production." Governance for AI infrastructure has to catch exactly that kind of plausible-but-wrong change, from any source.

## What does an AI infrastructure stack look like in practice?

A working AI infrastructure stack combines accelerator capacity, a data layer, an orchestration and serving layer, and a control plane, usually drawn from several vendors rather than one. No single provider covers every layer today, so the practical question for most teams is less "which vendor" and more "how do these layers get provisioned and kept consistent together."

### Example components by layer

| Layer | Representative tools |
| --- | --- |
| Accelerators | NVIDIA and AMD GPUs, cloud-native accelerator instances from AWS, Azure, and Google Cloud, specialized providers like CoreWeave and Lambda |
| Data | Object storage, vector databases, feature stores, data pipeline tools |
| Orchestration | Kubernetes, Kueue, Dynamic Resource Allocation (DRA) for accelerator scheduling |
| Serving and MLOps | KServe, vLLM, MLflow, Weights & Biases |
| Control plane | Infrastructure as code, policy as code, secrets management, CI/CD |

Kubernetes has become the default orchestration layer for AI workloads specifically, not just container workloads generally — the CNCF figures above show 66% of organizations hosting generative AI models already run inference on it. See [how teams run AI agents on Kubernetes](/blog/ai-agents-on-kubernetes/) for the node groups, schedulers, and serving patterns that show up in practice. Tool selection within each layer is a fast-moving, genuinely vendor-specific decision; for a detailed, evaluated comparison of AI infrastructure tools by category, see [the best AI infrastructure tools](/blog/ai-infrastructure-tools/).

## How do you build AI infrastructure?

Building AI infrastructure follows the same discipline as building any other production infrastructure: define it as code, validate it before it runs, apply it through a controlled pipeline, and keep governance in place as both people and agents make changes.

### A practical sequence

1. **Define the accelerator and data layers as code.** Provision GPU or TPU capacity, networking, and storage using the same infrastructure-as-code tooling as the rest of the stack, rather than a one-off console setup that nobody can reproduce.
2. **Stand up orchestration and serving.** Deploy Kubernetes (or the orchestration layer of choice) along with the scheduling and serving components the workload needs, again as versioned code.
3. **Wire in the control plane.** Add policy as code, secrets management, and drift detection before opening the stack up to routine changes, not after.
4. **Connect agents through a grounded interface.** Give coding assistants and infrastructure agents access to real stack state through something like an MCP server, rather than letting them guess at infrastructure they cannot see.
5. **Route every change, human or agent, through preview and policy.** Require a preview and a policy check on every proposed change regardless of who or what authored it, and keep human approval in the loop for high-risk changes.
6. **Monitor and iterate.** Track drift, cost, and agent-generated change volume over time, and tighten or loosen guardrails as the team's comfort with agent-authored changes grows.

## Frequently asked questions

### What is AI infrastructure?

AI infrastructure is the compute, data, orchestration, and control-plane layers that AI training and inference workloads run on, along with the tooling used to provision and govern them. It spans accelerators and networking, data pipelines, orchestration and serving software, and the infrastructure-as-code and policy layer that defines and secures everything else.

### Is AI infrastructure just GPUs?

No. GPUs and other accelerators are one layer of AI infrastructure, but a working stack also needs data pipelines, orchestration and scheduling, model-serving software, and a control plane that provisions and governs all of it. A pile of accelerators with no orchestration or governance layer is not production-ready AI infrastructure.

### What is the difference between AI infrastructure and MLOps?

AI infrastructure is the compute, data, and orchestration layers that AI workloads run on. MLOps is the set of practices and tooling for managing the model lifecycle on top of that infrastructure, including training pipelines, experiment tracking, and model deployment. MLOps tools like MLflow and Weights & Biases sit at the serving and lifecycle layer of an AI infrastructure stack.

### What is the difference between AI infrastructure and agentic infrastructure?

AI infrastructure is the stack that AI workloads run on, including compute, data, orchestration, and the control plane. Agentic infrastructure specifically refers to infrastructure that AI agents actively investigate, propose changes to, and operate, treating agents as a user persona rather than only as a workload. See [what agentic infrastructure is](/what-is/what-is-agentic-infrastructure/) for the full distinction.

### Do you need Kubernetes for AI infrastructure?

Not strictly, but it has become the default choice. Most production stacks now build on Kubernetes for scheduling and serving; per the CNCF's 2025 Annual Cloud Native Survey, 66% of organizations hosting generative AI models already use it to manage some or all of their inference workloads. Teams can run AI workloads without it, but doing so means giving up the scheduling, autoscaling, and multi-tenant isolation most teams already depend on.

### What is the difference between training and inference infrastructure?

Training infrastructure runs long, resource-intensive jobs that consume large accelerator clusters for hours or days at a time and tolerates some latency in exchange for throughput. Inference infrastructure serves live requests against a trained model and is optimized for low latency and cost per request, often across many smaller, geographically distributed deployments rather than one large cluster.

### What are the best AI infrastructure tools?

The right tools depend on the layer: accelerator providers like NVIDIA, AMD, CoreWeave, and Lambda for compute; Kubernetes, Kueue, and DRA for orchestration; KServe, vLLM, MLflow, and Weights & Biases for serving and MLOps; and infrastructure as code, policy as code, and secrets management for the control plane. See [the best AI infrastructure tools](/blog/ai-infrastructure-tools/) for a detailed, evaluated comparison by category.

### How do AI agents deploy cloud infrastructure?

AI agents deploy cloud infrastructure through a coding interface, generating or editing infrastructure-as-code programs, then routing the resulting change through an automated preview and policy check before it applies. Research on agent performance across cloud interfaces found infrastructure as code gave agents a perfect provisioning success rate in a fixed number of steps, while a browser-based console needed roughly 30 times more steps than the fastest interface tested, the command line. See [what MCP means for infrastructure as code](/what-is/mcp-for-infrastructure-as-code/) for how agents get grounded access to live infrastructure state before proposing changes.

### How do you secure AI infrastructure?

Securing AI infrastructure means applying the same controls used across cloud infrastructure generally, including policy as code, secrets management, drift detection, and human-in-the-loop approval for high-risk changes, and applying those controls consistently to changes proposed by AI agents as well as by people. The specific new risk to guard against is a plausible-looking but incorrect change, such as an AI-generated configuration field that passes linting but fails in production.

## Learn more

AI infrastructure sits at the intersection of cloud engineering and the AI workloads that increasingly run on it, and it works best when the control plane gets the same attention as the compute layer. To go deeper on the pieces covered here, start with [what infrastructure as code is](/what-is/what-is-infrastructure-as-code/) for the foundational concept, then [what agentic infrastructure is](/what-is/what-is-agentic-infrastructure/) for how AI agents actively operate infrastructure, and [what MCP means for infrastructure as code](/what-is/mcp-for-infrastructure-as-code/) for how agents get grounded access to it. For platform-level context, see [what platform engineering is](/what-is/what-is-platform-engineering/) and [what an internal developer platform is](/what-is/what-is-an-internal-developer-platform/). For a deeper look at deploying AI workloads on Kubernetes specifically, see [how teams run AI agents on Kubernetes](/blog/ai-agents-on-kubernetes/), and for tool-by-tool comparisons, see [the best AI infrastructure tools](/blog/ai-infrastructure-tools/).
