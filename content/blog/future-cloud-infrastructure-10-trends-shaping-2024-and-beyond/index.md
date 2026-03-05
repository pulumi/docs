---
title: "Future of the Cloud: 10 Trends Shaping 2026 and Beyond"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-12-04T07:56:40Z
updated: 2026-02-12

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Explore 2026’s top cloud trends, including AI infrastructure, Kubernetes evolution, IaC, DevSecOps, platform engineering, and modern cloud governance.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: "2026-cloud-trends -ai-idp-security.png"

aliases:
    - /future-cloud-infrastructure-10-trends-shaping-2026-and-beyond/
    - /blog/future-cloud-infrastructure-10-trends-shaping-2026-and-beyond/

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston
# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - ai
    - cloud-native
    - infrastructure-as-code
    - cloud-computing
    - multi-cloud
    - platform-engineering
    - devops
    - devsecops
    - security
    - kubernetes

---

In 2026, several trends will dominate cloud computing, driving innovation, efficiency, and scalability. From Infrastructure as Code (IaC) to AI/ML, platform engineering to multi-cloud and hybrid strategies, and security practices, let's explore the 10 biggest emerging trends.

<!--more-->

## On This Article

- [1. Cloud Will Become a Business Necessity by 2028](#1-cloud-will-become-a-business-necessity-by-2028)
- [2. Hyperscalers Accelerate AI-Driven Cloud Expansion](#2-hyperscalers-accelerate-ai-driven-cloud-expansion)
- [3. Hybrid and Multi-Cloud to Drive Innovation](#3-hybrid-and-multi-cloud-to-drive-innovation)
- [4. Enterprises Rebuild Their Cloud Foundations to Operationalize AI](#4-enterprises-rebuild-their-cloud-foundations-to-operationalize-ai)
- [5. IaC Drives Scalable Cloud, Multi-Cloud, and AI Operations](#5-iac-drives-scalable-cloud-multi-cloud-and-ai-operations)
- [6. DevSecOps Evolves Into AI-Integrated Security](#6-devsecops-evolves-into-ai-integrated-security)
- [7. Platform Engineering and Internal Developer Platforms](#7-platform-engineering--internal-developer-platforms-idps)
- [8. AIOps Matures Into a Cloud Operations Standard](#8-aiops-matures-into-a-cloud-operations-standard)
- [9. Kubernetes Dominance and Increased Complexity](#9-kubernetes-dominance-and-increased-complexity)
- [10. AI Code Assistants in the Enterprise](#10-ai-code-assistants-in-the-enterprise)
- [The Future of Cloud: Reinvented for an AI-First Decade](#the-future-of-cloud-reinvented-for-an-ai-first-decade)

## 1. Cloud Will Become a Business Necessity by 2028

According to [Gartner](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/cloud-computing), by 2028 the cloud will be the key driver for business innovation, and estimates that over 95% of new digital workloads will be deployed on cloud-native platforms.

{{< figure alt="The future of cloud computing. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/gartner-cloud-2028.png" caption="The future of cloud computing. Credit: Gartner" width=100% >}}

According to McKinsey & Company's "[In search of cloud value](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/in-search-of-cloud-value-can-generative-ai-transform-cloud-roi)" report:

- **Cloud value is driven by innovation**, worth 5x more than cost savings.
- **EBITDA uplift of 20–30% by 2030** for high-performing organizations.
- **Asia leads in projected cloud value**, followed by the US and Europe.
- High-ROI organizations excel by aligning cloud strategy with business priorities, building strong cloud foundations, and using modern operating models.

Teams succeeding in this transition increasingly use Infrastructure as Code, automation, and unified governance frameworks like [Pulumi Insights + Policies](https://www.pulumi.com/product/insights-governance/) to operationalize this value.

## 2. Hyperscalers Accelerate AI-Driven Cloud Expansion

Hyperscalers are making the largest infrastructure investments in cloud history — nearly all centered on AI workloads, inference, and high-performance compute.

- **AWS** has integrated [Anthropic’s Claude 3 and Claude 4 models into Amazon Bedrock](https://www.aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock) for enterprise LLM workflows. “Claude Opus 4 and Claude Sonnet 4 are available today in Amazon Bedrock, enabling customers to build agents with stronger reasoning, memory, and tool use.” — AWS, May 2025
- **Microsoft Azure** revenue rose 33% year-over-year in Q3 (ended March 31), outperforming estimates of ~29.7%. [AI contributed 16 percentage points to this growth](https://www.reuters.com/business/microsoft-beats-quarterly-revenue-estimates-ai-shift-bolsters-cloud-demand-2025-04-30/), up from 13 points in the prior quarter. "Microsoft is on track to invest approximately $80 billion to build out AI-enabled datacenters to train AI models and deploy AI and cloud-based applications around the world," said Brad Smith, the Microsoft Vice Chair and President.
- **Google Cloud** is committing [$25 billion over two years for data center and AI infrastructure expansion](https://www.utilitydive.com/news/google-cloud-blackstone-aws-us-ai-data-center-buildouts/753202) across the PJM grid, with total capital expenditure for 2025 ranging from $75–85 billion. "As our CEO has said, in these early days of a very transformative technology, the risks of under-investing are dramatically higher than the risks of over-investing," said Eunice Huang, Head of AI and Emerging Tech Policy.
- **Oracle** anticipates 15–20% cloud revenue growth in FY 2026–2027 attributable to AI infrastructure demand, tied to its partnership in the [Stargate initiative](https://www.pcgamer.com/software/ai/openais-skyrocketing-spending-could-see-billions-of-dollars-in-silicon-headed-down-the-ai-mines-in-the-next-few-years-including-2-million-nvidia-chips-headed-to-texas-stargate-facility/).

As hyperscalers integrate AI deeper into their service layers, engineering teams must adapt with IaC-driven automation, reusable patterns, and policy controls to deploy cloud and AI infrastructure consistently.
See how organizations [deploy AWS infrastructure at the speed of AI with Pulumi](https://www.pulumi.com/aws/#video) and [Pulumi Policies](https://www.pulumi.com/docs/insights/policy/).

## 3. Hybrid and Multi-Cloud to Drive Innovation

Hybrid and multi-cloud strategies are now mainstream:

- Hybrid cloud will grow from **$130B to $310–330B** by 2030 ([ResearchAndMarkets](https://www.businesswire.com/news/home/20250513124988/en/Hybrid-Cloud-Market-Analysis-Growth-Trends-and-Forecasts-Report-2024-2025-2030-Surging-Demand-for-Seamless-Interoperability-Between-Cloud-Services-and-Existing-Systems---ResearchAndMarkets.com)).
- **87% of enterprises** run workloads across multiple clouds ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/hybrid-cloud-market)).
- Gartner predicts that **40% of enterprises** will adopt hybrid compute architectures in mission-critical workflows by 2028 (up from 8%).

{{< figure alt="Most popular cloud computing infrastructure by industry. Credit: Cloud Worldwide Service, Forbes" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/most-popular-cloud-computing-infrastructure-by-industry.png" caption="Credit: Cloud Worldwide Service, Forbes" width=100% >}}

As AI and regulatory requirements grow, organizations must deploy workloads across AWS, Azure, Google Cloud, on-prem, and edge — while maintaining consistent security, compliance, and configuration.

Modern cloud teams use:

- **Infrastructure as Code** for consistent multi-cloud provisioning and environment standardization, forming the backbone of AI infrastructure orchestration
- **Reusable components and internal platforms** to define scalable architecture patterns and accelerate delivery across Kubernetes, AI/ML pipelines, and hybrid environments
- **Policy-driven guardrails** to maintain cost, security, and compliance across environments, supporting cloud governance automation and modern cloud cost governance

Pulumi enables all three through its [multi-cloud IaC model](https://www.pulumi.com/docs/iac/), [Pulumi Policies](https://www.pulumi.com/product/insights-governance#video), and [internal developer platform capabilities](https://www.pulumi.com/product/internal-developer-platforms/#video).

## 4. Enterprises Rebuild Their Cloud Foundations to Operationalize AI

While hyperscalers are transforming the global cloud platform, enterprises face a different challenge: adapting their own cloud foundations to support AI at scale. Organizations are moving beyond prototypes and integrating AI into core products, internal workflows, and customer-facing systems, requiring new levels of automation, governance, and AI infrastructure orchestration.

According to [Gartner](https://www.networkworld.com/article/4058786/gartner-ai-spending-to-reach-1-5-trillion-dollars-this-year.html), global AI infrastructure spending is expected to surpass **$2 trillion in 2026**. [IDC predicts that by 2027](https://blogs.idc.com/2025/10/22/futurescape-2026-moving-into-the-agentic-future/), more than 50% of enterprises will use AI agents to drive core workflows, which requires scalable, secure, and automated cloud architectures to support model execution and orchestration.

To enable this transition, enterprises are investing in:

- **GPU provisioning and orchestration**, data pipelines, vector databases, feature stores, and LLM infrastructure needed for real-time AI workloads.
- **Data pipelines, vector databases, and feature stores** needed for real-time AI workloads
- **Model-serving infrastructure**, including gateways, inference routers, and autoscaling layers
- **Strong identity, secrets, and access controls** as AI systems increase security exposure
- **Automation through Infrastructure as Code** to ensure reproducibility and reduce drift
- **Policy-driven governance** to secure cost, compliance, and architectural consistency

As AI becomes deeply embedded across engineering organizations, teams are increasingly using software engineering approaches such as Infrastructure as Code, reusable components, platform engineering, and policy automation to standardize how AI infrastructure is deployed, scaled, and secured across clouds.

To support this shift, Pulumi's perspective on [Superintelligence Infrastructure](https://www.pulumi.com/product/superintelligence-infrastructure/) explains why AI workloads, from pre-training to inference at massive scale, require dynamic infrastructure orchestration rather than static configuration.

### Pulumi users increasingly rely on:

- [Pulumi IaC](https://www.pulumi.com/docs/iac/) for standardized AI infrastructure
- [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) to manage all secrets and configuration at scale
- [Pulumi Insights](https://www.pulumi.com/product/insights-governance/) for visibility and misconfiguration analysis
- [Pulumi Policies](https://www.pulumi.com/docs/insights/policy/) for AI-specific guardrails in code, cost detection, and to provide automated compliance protections

## 5. IaC Drives Scalable Cloud, Multi-Cloud, and AI Operations

As cloud environments expand and AI workloads demand highly dynamic infrastructure, Infrastructure as Code (IaC) is becoming the foundation for scaling reliably across all environments. Organizations are increasingly adopting IaC in general-purpose languages to unify development and infrastructure workflows, reduce configuration drift, and deliver cloud resources at speed.

Modern [Infrastructure as Code](https://www.pulumi.com/what-is/what-is-infrastructure-as-code/) is advancing far beyond simple provisioning:

- **Standardizing multi-cloud and hybrid patterns** so teams can deploy consistently across AWS, Azure, Google Cloud, on-prem, and edge environments.
- **Integrating seamlessly with cloud providers and third-party services**, including data platforms and messaging systems like CockroachDB, Confluent Cloud, and Kafka.
- **Providing deeper validation and type-safety**, ensuring parameters, dependencies, and security controls are correct before deployment.
- **Improving cloud resource efficiency and visibility** with tools like [Pulumi Insights Discovery](https://www.pulumi.com/docs/insights/discovery/).
- **Embedding security and compliance through [Policy as Code](https://www.pulumi.com/docs/insights/policy/)**, enforcing guardrails, cost controls, and regulatory requirements automatically, enabling truly policy-driven cloud management.
- **Enabling intelligent automation**, from unit and integration tests to auto-remediation policies and policy-driven approvals.
- **Incorporating AI-driven optimization and insights**, helping teams detect misconfigurations, analyze usage patterns, and generate infrastructure updates with tools like [Pulumi Neo](https://www.pulumi.com/product/neo/) and [Pulumi Policies](https://www.pulumi.com/blog/policy-next-gen/).

As organizations scale both traditional cloud workloads and AI-driven systems, IaC has become critical for achieving secure, repeatable, and high-velocity operations across every environment.

## 6. DevSecOps Evolves Into AI-Integrated Security

As AI becomes embedded across cloud-native systems, DevSecOps is entering a new era. Gartner predicts that by **2028, over 50% of enterprises will use AI security platforms** to protect their AI investments. Below are the 3 key predictions for the future of DevSecOps:

1. **AI-driven security automation**: Teams will increasingly rely on AI to detect threats, enforce policies, and generate secure infrastructure patches. See Pulumi’s capabilities in [AI-powered remediation](https://www.pulumi.com/product/insights-governance/#video).

2. **More focus on secrets management**: With AI systems accessing more sensitive data, secure secret storage will be essential. [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) helps teams centralize and govern credentials, keys, and tokens safely.

3. **Greater cross-team collaboration**: Dev, Sec, and Ops workflows will converge under shared frameworks: IaC, policy automation, runtime scanning, and GitOps.

As organizations increase their use of AI across cloud-native systems, the need for tightly aligned security, governance, and cloud governance automation becomes even more urgent. At the Gartner Data & Analytics Summit in Sydney, Carlie Idoine, VP Analyst at Gartner, emphasized this growing dependency:

*"[AI]... it doesn’t deliver value on its own – AI needs to be tightly aligned with data, analytics, and governance to enable intelligent, adaptive decisions and actions across the organization."*

This perspective mirrors what we’re seeing across modern DevSecOps practices: AI can amplify security, but only when paired with strong foundations in secrets management, governance, and cross-team collaboration.

## 7. Platform Engineering & Internal Developer Platforms (IDPs)

According to [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering), **by 2026, 80% of large software engineering organizations will establish platform engineering teams** as internal providers of reusable services, components, and tools for application delivery. Platform engineering will ultimately solve the central problem of cooperation between software developers and operators.

Mid-size to large companies will begin or continue to invest in implementing [platform engineering practices](https://www.pulumi.com/blog/platform-engineering-pillars-3/), with large tech companies as first adopters. They will provide [Internal Developer Platforms (IDP)](https://www.pulumi.com/blog/announcing-pulumi-idp/) to elevate the [Developer Experience](https://www.pulumi.com/blog/developer-experience-business-critical/) (DX, sometimes referred to as DE or DevEx), helping them work faster, like abstracting the complexities of configuring, testing, and validation, deploying infrastructure, and scanning their code for security.

{{< figure alt="Internal developer platform-in-a-box. Credit: Pulumi" src="https://www.pulumi.com/blog/developer-portal-platform-teams/platform-teams.png" caption="Internal developer platform-in-a-box. Credit: Pulumi" width=100% >}}

IDPs are reshaping how developers interact with cloud infrastructure, bringing together platform engineering, automation, and emerging AI platform engineering practices.

## 8. AIOps Matures into a Cloud Operations Standard

AIOps is becoming mainstream, helping teams predict failures, auto-scale infrastructure, and resolve incidents with minimal manual effort. As AI and automation continue to evolve, the fusion of these technologies will enable organizations to achieve unprecedented levels of efficiency and scalability.

- **Proactive Operations**: AI-powered tools will assist teams in foreseeing issues with greater accuracy, minimizing downtime, and reducing the firefighting nature of incident management. These tools will automatically detect anomalies, optimize performance, and trigger remediation actions.
- **[Intelligent Automation](https://www.pulumi.com/docs/iac/packages-and-automation/automation-api/)**: Routine operational tasks like patching, monitoring, and resource scaling will be fully automated. AI-driven decision-making will allow for smarter resource allocation and optimization, dynamically adjusting infrastructure and workloads in response to real-time demands and predictions.
- **[Data-Driven Insights](https://www.pulumi.com/docs/pulumi-cloud/insights/)**: AIOps will analyze vast amounts of operational data and provide actionable insights, enabling teams to focus on high-impact tasks such as improving system architecture and user experience. The AI-powered insights will also inform better strategic decisions, helping teams to continuously evolve their DevOps practices.
- **Collaboration Across Teams**: AIOps will bridge the gap between DevOps, SecOps, and IT operations by bridging monitoring and automation. Cross-team collaboration will improve as AI systems consolidate and interpret data from various departments, allowing for a more cohesive approach to system management.

AIOps features include observability, automation, and real-time analytics to bridge DevOps, SRE, and IT operations.

## 9. Kubernetes Dominance and Increased Complexity

Kubernetes will continue its ascent in 2026. According to [Research & Markets](https://www.researchandmarkets.com/reports/6110428/kubernetes-global-strategic-business-report), the global Kubernetes market was valued at USD 2.3 billion in 2024 and is projected to reach USD 8.2 billion by 2030, with a CAGR of 23.8% over the forecast period.

The CNCF Annual Survey shows AI/ML workloads rapidly moving onto Kubernetes — including batch pipelines, model experimentation, real-time inference, and data preprocessing — even as only 41% of ML/AI developers are cloud-native today. This shift is accelerating as teams need flexible GPU scheduling, distributed pipelines, and portable execution environments.

[Kubernetes is also evolving in response to AI demands](https://www.pulumi.com/blog/beyond-yaml-kubernetes-2026-automation-era/#the-2026-convergence-of-ai-platforms-and-policy-in-kubernetes). Inference workloads, powered by LLMs and GPUs, now require low-latency execution closer to the user. This shift is pushing organizations to build intelligent orchestration layers that schedule AI pipelines across edge and core clusters, often leveraging Kubernetes as the common control plane for AI cluster orchestration.

As we move into 2026, three patterns are becoming clear:

- **Kubernetes is evolving to support AI** through GPU-aware scheduling, Kubernetes GPU scheduling optimizations, and more advanced workload orchestration.
- **Governance and consistency matter more than ever**, as teams struggle to secure and manage multi-cluster, multi-cloud environments.
- **Platform engineering is essential**, providing curated patterns and automation rather than raw YAML to reduce cognitive load.

Kubernetes will remain a strategic foundation — but operating it effectively now depends on robust automation, strong security controls, and standardized delivery models that scale across clouds, clusters, and AI pipelines.

## 10. AI Code Assistants in the Enterprise

AI-powered coding assistants like GitHub Copilot, Claude Code, Cursor, and others are rapidly becoming part of modern software development.

**By 2027, the use of AI assistants will dramatically increase developer velocity** to meet functional business requirements for 70% of new digital solutions in production (source: [IDC](https://www.digitalnewsasia.com/business/idc-reveals-its-top-predictions-cloud-2023-and-beyond)).

{{< figure alt="The value of AI code assistants. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/ai_code_assistants_value.png" caption="The value of AI code assistants. Credit: Gartner" width=100% >}}

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028), **by 2028, 75% of enterprise software engineers will use dedicated AI code assistants**, and 63% of organizations are currently piloting, deploying or beginning to use AI code assistants.

As enterprise adoption of AI assistants increases, expectations are rising: they must not only generate code but also understand the state of infrastructure, configurations, and security posture. That means being able to answer questions about environments, surface misconfigurations, or act directly on infrastructure.

One of the newest developments is the release of [Pulumi Agent Skills](https://www.pulumi.com/blog/pulumi-agent-skills/), a collection of infrastructure expertise packaged for use in AI coding assistants. These skills teach tools such as Claude Code, Cursor, or Gemini CLI to reason about Pulumi projects, reducing hallucination and improving outputs based on real infrastructure conventions and practices.

Combined with infrastructure access via tools like [Pulumi’s Remote MCP Server](https://www.pulumi.com/blog/remote-mcp-server/), teams can build secure, AI-driven workflows where assistants provide insights and Pulumi Neo safely executes actions with previews, policies, and orchestration.

AI code assistants are no longer experimental; they're fast becoming a competitive advantage in cloud software development.

## The Future of Cloud: Reinvented for an AI-First Decade

Cloud infrastructure is entering its most transformative era since the rise of Kubernetes. The trends shaping 2026 reveal a clear pattern: AI is no longer a workload — it’s becoming the organizing principle of cloud strategy.

- **AI-native cloud architectures** that require elastic compute, GPU orchestration, fast data access, and governance built into every layer
- **Infrastructure as Code as the operational backbone**, standardizing deployments across AI, cloud, and hybrid environments
- **Platform engineering and IDPs** to enable self-service, gold-standard patterns, and automated guardrails
- **Security integrated into every pipeline**, with AI-assisted threat detection, strong secrets management, and policy-driven compliance
- **AIOps and intelligent automation** are becoming standard for scaling modern cloud systems
- **Kubernetes evolving for AI**, driving new orchestration patterns across edge, core, and inference clusters
- **Multi-cloud and hybrid ecosystems** accelerating to support interoperability, resilience, and global workload placement

Taken together, these shifts point to a new model of cloud operations that is intelligent, automated, policy-aware, and built on software engineering principles rather than manual configuration.

Organizations that invest now in **modern IaC**, **unified governance**, **reusable components**, and **policy frameworks** — all core capabilities of the Pulumi Cloud platform — will be positioned to lead in an AI-first world. The gap between teams that modernize and those that do not will widen rapidly in 2026 and beyond.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
