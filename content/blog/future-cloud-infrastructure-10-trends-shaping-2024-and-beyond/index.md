---
title: "Future of the Cloud: 10 Trends Shaping 2027 and Beyond"
title_tag: "Future of the Cloud: 10 Trends for 2027"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-12-04T07:56:40Z
updated: 2026-09-15

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Explore 2027's biggest cloud trends, from agentic infrastructure and hyperscaler AI spend to Kubernetes, IaC, DevSecOps, and platform engineering.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.

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
category: general

---

Cloud infrastructure in 2027 turns on one shift: AI agents are moving from writing code to operating infrastructure directly, with humans approving changes rather than authoring every one. Hyperscaler capital spending, Kubernetes-for-AI adoption, and platform engineering are all accelerating alongside it. Here are the 10 trends shaping cloud computing through 2027 and beyond.

Last year's edition of this piece predicted a cloud-first, AI-driven decade. The numbers came in since: Microsoft's Azure business crossed $100 billion in trailing revenue, Google Cloud's backlog reached $514 billion, and AWS's AI and custom-silicon businesses each passed a $25 billion annualized run rate. The 2026 predictions held up. What follows is the update for 2027.

<!--more-->

## 1. Cloud Will Become a Business Necessity by 2028

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-10-23-gartner-it-symposium-xpo-2024-orlando-day-3-highlights), by 2028 cloud-native platforms will serve as the foundation for more than 95% of new digital initiatives, up from less than 50% in 2023. Gartner has also forecast that [worldwide public cloud spending will exceed $1 trillion in 2027](https://www.gartner.com/en/newsroom/press-releases/2023-11-29-gartner-says-cloud-will-become-a-business-necessity-by-2028), en route to cloud becoming, in Gartner's words, a business necessity.

{{< figure alt="The future of cloud computing. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/gartner-cloud-2028.png" caption="The future of cloud computing. Credit: Gartner" width=100% >}}

According to McKinsey & Company's "[In search of cloud value](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/in-search-of-cloud-value-can-generative-ai-transform-cloud-roi)" report:

- **Cloud value is driven by innovation**, worth 5x more than cost savings.
- **EBITDA uplift of 20–30% by 2030** for high-performing organizations.
- **Asia leads in projected cloud value**, followed by the US and Europe.
- High-ROI organizations excel by aligning cloud strategy with business priorities, building strong cloud foundations, and using modern operating models.

Teams succeeding in this transition increasingly use infrastructure as code, automation, and unified governance frameworks like [Pulumi Insights + Policies](https://www.pulumi.com/product/insights-governance/) to operationalize this value.

## 2. Hyperscalers Accelerate AI-Driven Cloud Expansion

Hyperscalers are making the largest infrastructure investments in cloud history, nearly all centered on AI workloads, inference, and high-performance compute.

- **AWS** posted its fastest revenue growth since 2021: [$42.2 billion in Q2 2026, up 37% year-over-year](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/), accelerating from 28% growth the prior quarter. AWS's AI business and its chips business, which includes its custom Trainium and Graviton silicon, each exceeded a $25 billion annualized revenue run rate, growing triple-digit percentages year-over-year.
- **Microsoft Azure** crossed a threshold of its own: [Azure's full fiscal-year 2026 revenue surpassed $100 billion for the first time](https://news.microsoft.com/source/2026/07/29/microsoft-cloud-and-ai-strength-fuels-fourth-quarter-results-4/) in Microsoft's fiscal Q4 2026 (ended June 30, 2026), with Azure revenue growing 43% year-over-year, up from 40% the prior quarter. "This year, Azure revenue surpassed $100 billion for the first time," said Satya Nadella, Microsoft's chairman and CEO.
- **Google Cloud** revenue rose 82% year-over-year to $24.8 billion in Q2 2026, and its backlog reached $514 billion, up from $106 billion a year earlier. Alphabet [raised its full-year 2026 capital expenditure guidance to $195–205 billion](https://abc.xyz/investor/events/event-details/2026/2026-Q2-Earnings-Call-2026-GgTAq7Is0z/default.aspx), up from an earlier $180–190 billion estimate that had itself already been raised twice this year.
- **Oracle** reported FY2026 cloud revenue of $34.0 billion, up 39% year-over-year, with [remaining performance obligations reaching $638 billion](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/default.aspx), up 363% year-over-year on the strength of large-scale AI infrastructure contracts, including prepaid and customer-supplied GPU deals now totaling $75 billion.

As hyperscalers integrate AI deeper into their service layers, engineering teams must adapt with IaC-driven automation, reusable patterns, and policy controls to deploy cloud and AI infrastructure consistently.
See how organizations [deploy AWS infrastructure at the speed of AI with Pulumi](https://www.pulumi.com/aws/#video) and [Pulumi Policies](https://www.pulumi.com/docs/insights/policy/).

## 3. Hybrid and Multi-Cloud to Drive Innovation

Hybrid and multi-cloud strategies are now mainstream:

- Hybrid cloud will grow from **$130B to $310–330B** by 2030 ([ResearchAndMarkets](https://www.businesswire.com/news/home/20250513124988/en/Hybrid-Cloud-Market-Analysis-Growth-Trends-and-Forecasts-Report-2024-2025-2030-Surging-Demand-for-Seamless-Interoperability-Between-Cloud-Services-and-Existing-Systems---ResearchAndMarkets.com)).
- **87% of enterprises** run workloads across multiple clouds ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/hybrid-cloud-market)).
- Gartner predicts that **40% of enterprises** will adopt hybrid compute architectures in mission-critical workflows by 2028 (up from 8%).
- In Pulumi's own [2026 survey of 510 platform, DevOps, and product engineers](https://www.pulumi.com/state-of-agentic-infrastructure/), multi-cloud is already the norm at the teams surveyed: 64% run on AWS, 55% on Google Cloud, and 45% on Azure, with most running more than one.

{{< figure alt="Most popular cloud computing infrastructure by industry. Credit: Cloud Worldwide Service, Forbes" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/most-popular-cloud-computing-infrastructure-by-industry.png" caption="Credit: Cloud Worldwide Service, Forbes" width=100% >}}

As AI and regulatory requirements grow, organizations must deploy workloads across AWS, Azure, Google Cloud, on-prem, and edge while maintaining consistent security, compliance, and configuration.

Modern cloud teams use:

- **Infrastructure as Code** for consistent multi-cloud provisioning and environment standardization, forming the backbone of AI infrastructure orchestration
- **Reusable components and internal platforms** to define scalable architecture patterns and accelerate delivery across Kubernetes, AI/ML pipelines, and hybrid environments
- **Policy-driven guardrails** to maintain cost, security, and compliance across environments, supporting cloud governance automation and modern cloud cost governance

Pulumi enables all three through its [multi-cloud IaC model](https://www.pulumi.com/docs/iac/), [Pulumi Policies](https://www.pulumi.com/product/insights-governance#video), and [internal developer platform capabilities](https://www.pulumi.com/product/internal-developer-platforms/#video).

## 4. Enterprises Rebuild Their Cloud Foundations to Operationalize AI

While hyperscalers are transforming the global cloud platform, enterprises face a different challenge: adapting their own cloud foundations to support AI at scale. Organizations are moving beyond prototypes and integrating AI into core products, internal workflows, and customer-facing systems, requiring new levels of automation, governance, and AI infrastructure orchestration.

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026), total worldwide AI spending, spanning software, hardware, and services, is forecast to reach **$2.59 trillion in 2026**, a 47% increase year-over-year. [IDC predicts that by 2027](https://www.idc.com/resource-center/blog/futurescape-2026-moving-into-the-agentic-future/), half of enterprises will be using AI agents to redefine how humans and machines collaborate, which requires scalable, secure, and automated cloud architectures to support model execution and orchestration.

To enable this transition, enterprises are investing in:

- **GPU provisioning and orchestration**, data pipelines, vector databases, feature stores, and LLM infrastructure needed for real-time AI workloads
- **Model-serving infrastructure**, including gateways, inference routers, and autoscaling layers
- **Strong identity, secrets, and access controls** as AI systems increase security exposure
- **Automation through Infrastructure as Code** to ensure reproducibility and reduce drift
- **Policy-driven governance** to secure cost, compliance, and architectural consistency

As AI becomes deeply embedded across engineering organizations, teams are increasingly using software engineering approaches such as infrastructure as code, reusable components, platform engineering, and policy automation to standardize how AI infrastructure is deployed, scaled, and secured across clouds.

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
- **Incorporating AI-driven optimization and insights**, helping teams detect misconfigurations, analyze usage patterns, and generate infrastructure updates through [Pulumi Policies](https://www.pulumi.com/blog/policy-next-gen/).

As organizations scale both traditional cloud workloads and AI-driven systems, IaC has become critical for achieving secure, repeatable, and high-velocity operations across every environment.

## 6. DevSecOps Evolves Into AI-Integrated Security

As AI becomes embedded across cloud-native systems, DevSecOps is entering a new era. [Gartner predicts](https://www.gartner.com/en/newsroom/press-releases/2026-03-17-gartner-predicts-ai-applications-will-drive-50-percent-of-cybersecurity-incident-response-efforts-by-2028) that by **2028, over 50% of enterprises will use AI security platforms** to secure third-party AI service usage and protect custom-built AI applications, with total spending on securing AI reaching roughly $4.8 billion in 2027. Below are the 3 key predictions for the future of DevSecOps:

1. **AI-driven security automation**: Teams will increasingly rely on AI to detect threats, enforce policies, and generate secure infrastructure patches. See Pulumi’s capabilities in [AI-powered remediation](https://www.pulumi.com/product/insights-governance/#video).

2. **More focus on secrets management**: With AI systems accessing more sensitive data, secure secret storage will be essential. [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) helps teams centralize and govern credentials, keys, and tokens safely.

3. **Greater cross-team collaboration**: Dev, Sec, and Ops workflows will converge under shared frameworks: IaC, policy automation, runtime scanning, and GitOps.

As organizations increase their use of AI across cloud-native systems, the need for tightly aligned security, governance, and cloud governance automation becomes even more urgent. At the Gartner Data & Analytics Summit in Sydney, Carlie Idoine, VP Analyst at Gartner, emphasized this growing dependency:

*"[AI]... it doesn’t deliver value on its own – AI needs to be tightly aligned with data, analytics, and governance to enable intelligent, adaptive decisions and actions across the organization."*

This perspective mirrors what we’re seeing across modern DevSecOps practices: AI can amplify security, but only when paired with strong foundations in secrets management, governance, and cross-team collaboration.

{{< blog/cta-card title="Build for an AI-first cloud" >}}
Pulumi gives teams infrastructure as code, reusable components, and policy guardrails to deliver consistently across every cloud and AI workload.
{{< /blog/cta-card >}}

## 7. Platform Engineering & Internal Developer Platforms (IDPs)

According to [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering), **by 2026, 80% of large software engineering organizations will establish platform engineering teams** as internal providers of reusable services, components, and tools for application delivery. That target year has now arrived, and CNCF's own research shows the shift underway: its [Q1 2026 Technology Radar report with SlashData](https://www.cncf.io/announcements/2026/03/24/cncf-and-slashdata-report-finds-platform-engineering-tools-maturing-as-organizations-prepare-for-ai-driven-infrastructure/) found 28% of surveyed organizations already have a dedicated platform engineering team, and 35% are running a hybrid platform that combines existing developer platforms with specialized AI tooling.

"Cloud native platforms have reached a point where developers are not just experimenting but standardizing on CNCF projects that make software delivery reliable at scale," said Chris Aniszczyk, CTO of CNCF. "What's especially notable about this research is how organizations are extending those same platforms to support AI workloads, showing how cloud native is the base layer of powering the next era of applications."

Mid-size to large companies continue to invest in implementing [platform engineering practices](https://www.pulumi.com/blog/platform-engineering-pillars-3/), with large tech companies as first adopters. They provide [Internal Developer Platforms (IDP)](https://www.pulumi.com/blog/announcing-pulumi-idp/) to elevate the [Developer Experience](https://www.pulumi.com/blog/developer-experience-business-critical/) (DX, sometimes referred to as DE or DevEx), helping teams work faster by abstracting the complexities of configuring, testing, validating, deploying infrastructure, and scanning code for security.

{{< figure alt="Internal developer platform-in-a-box. Credit: Pulumi" src="https://www.pulumi.com/blog/developer-portal-platform-teams/platform-teams.png" caption="Internal developer platform-in-a-box. Credit: Pulumi" width=100% >}}

IDPs are reshaping how developers interact with cloud infrastructure, bringing together platform engineering, automation, and emerging AI platform engineering practices.

## 8. AIOps Becomes Agentic: From Suggestions to Supervised Execution

AIOps in 2027 turns on one question: how much of a change does an agent execute, and how closely does a human still review it? [Gartner predicts](https://www.gartner.com/en/articles/ai-for-infrastructure-operations) that agentic AI deployment in IT operations grows from under 5% in 2025 to 70% by 2029, while human-in-the-loop requirements in IT operations workflows fall from 95% in 2025 to 40% by 2028.

Pulumi's own [2026 survey of 510 platform, DevOps, and product engineers](https://www.pulumi.com/state-of-agentic-infrastructure/) shows the same shift starting inside real teams, and a gap between sentiment and practice that's worth naming honestly:

- **82% agree** that AI and agents will meaningfully change how they write infrastructure within 12 months.
- **63% say they trust agents to make production changes**, yet manual approval remains close to universal today. Pulumi's report describes this as stated trust outrunning real guardrails.
- Teams expecting agents to generate half or more of their infrastructure code rise from **45% today to 52%** within six months.

That gap between trust and guardrails is exactly what a supervised, agentic operating model has to close: an agent that proposes a change, runs a preview, and waits for approval, rather than one that only writes YAML for someone else to apply by hand. [Pulumi Neo](https://www.pulumi.com/product/neo/) is built around that loop, proposing infrastructure changes, running previews, and executing approved updates with policy guardrails in place, so the human stays the one accountable for what ships. Pulumi's [The Agentic Infrastructure Era](https://www.pulumi.com/blog/the-agentic-infrastructure-era/) makes the fuller case for why AIOps is headed toward this operating model rather than toward faster dashboards and alerting alone.

AIOps still includes observability, automation, and real-time analytics bridging DevOps, SRE, and IT operations. What's changed for 2027 is that those signals increasingly feed an agent empowered to act on them, with a person still reviewing the result.

## 9. Kubernetes Dominance and Increased Complexity

Kubernetes will continue its ascent in 2027. According to [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/kubernetes-market), the global Kubernetes market is valued at USD 3.13 billion in 2026 and is projected to reach USD 8.41 billion by 2031, a 21.85% CAGR.

The [CNCF's Q3 2025 State of Cloud Native Development report](https://www.cncf.io/wp-content/uploads/2025/11/cncf_report_stateofcloud_111025a.pdf) puts cloud-native adoption among professional ML/AI developers at 41%, with 30% of backend developers now using Kubernetes directly, down from a peak of 36% in Q3 2023, a slow decline the report attributes to the technology's growing maturity. Even so, teams still need flexible GPU scheduling, distributed pipelines, and portable execution environments as AI workloads scale.

[Kubernetes is also evolving in response to AI demands](https://www.pulumi.com/blog/beyond-yaml-kubernetes-2026-automation-era/#the-2026-convergence-of-ai-platforms-and-policy-in-kubernetes), a shift Pulumi covers in more depth in its [comparison of Kubernetes IaC tools](https://www.pulumi.com/blog/best-kubernetes-iac-tools-2026/). Inference workloads, powered by LLMs and GPUs, now require low-latency execution closer to the user, pushing organizations to build intelligent orchestration layers that schedule AI pipelines across edge and core clusters, often leveraging Kubernetes as the common control plane for AI cluster orchestration.

As we move into 2027, three patterns are becoming clear:

- **Kubernetes is evolving to support AI** through GPU-aware scheduling, Kubernetes GPU scheduling optimizations, and more advanced workload orchestration.
- **Governance and consistency matter more than ever**, as teams struggle to secure and manage multi-cluster, multi-cloud environments.
- **Platform engineering is essential**, providing curated patterns and automation rather than raw YAML to reduce cognitive load.

Kubernetes will remain a strategic foundation, but operating it effectively now depends on robust automation, strong security controls, and standardized delivery models that scale across clouds, clusters, and AI pipelines.

## 10. AI Code Assistants in the Enterprise

AI-powered coding assistants like GitHub Copilot, Claude Code, Cursor, and others have moved from novelty to everyday tooling for a large share of enterprise software teams, and the same shift is now reaching infrastructure code.

{{< figure alt="The value of AI code assistants. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/ai_code_assistants_value.png" caption="The value of AI code assistants. Credit: Gartner" width=100% >}}

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028), **by 2028, 75% of enterprise software engineers will use dedicated AI code assistants**, and 63% of organizations are currently piloting, deploying or beginning to use AI code assistants.

As enterprise adoption of AI assistants increases, expectations are rising: they must not only generate code but also understand the state of infrastructure, configurations, and security posture. That means being able to answer questions about environments, surface misconfigurations, or act directly on infrastructure. The [July 2026 revision of the Model Context Protocol](https://blog.modelcontextprotocol.io/posts/2026-07-28/), described by its maintainers as the largest revision of the protocol to date, is part of what makes that direct action practical: AWS shipped a [general-availability MCP server](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) for its Agent Toolkit, and Kubernetes tooling vendors like [Mirantis's Lens](https://www.mirantis.com/company/press-center/company-news/lens-launches-built-in-mcp-server-connecting-ai-coding-assistants-to-kubernetes/) have followed with built-in MCP servers of their own.

One of the newest developments is the release of [Pulumi Agent Skills](https://www.pulumi.com/blog/pulumi-agent-skills/), a collection of infrastructure expertise packaged for use in AI coding assistants. These skills teach tools such as Claude Code, Cursor, or Gemini CLI to reason about Pulumi projects, reducing hallucination and improving outputs based on real infrastructure conventions and practices.

Combined with infrastructure access via tools like [Pulumi’s Remote MCP Server](https://www.pulumi.com/blog/remote-mcp-server/), teams can build secure, AI-driven workflows where assistants provide insights and Pulumi Neo safely executes actions with previews, policies, and orchestration.

AI code assistants are no longer experimental; they're fast becoming a competitive advantage in cloud software development.

## The Future of Cloud: Built Around Agentic Operations

Cloud infrastructure is entering its most transformative era since the rise of Kubernetes. The trends shaping 2027 point to one clear pattern: AI now sets the organizing principle for cloud strategy, ahead of any single workload running on top of it.

- **AI-native cloud architectures** that require elastic compute, GPU orchestration, fast data access, and governance built into every layer
- **Infrastructure as Code as the operational backbone**, standardizing deployments across AI, cloud, and hybrid environments
- **Platform engineering and IDPs** to enable self-service, gold-standard patterns, and automated guardrails
- **Security integrated into every pipeline**, with AI-assisted threat detection, strong secrets management, and policy-driven compliance
- **AIOps and intelligent automation** are becoming standard for scaling modern cloud systems
- **Kubernetes evolving for AI**, driving new orchestration patterns across edge, core, and inference clusters
- **Multi-cloud and hybrid ecosystems** accelerating to support interoperability, resilience, and global workload placement

Taken together, these shifts point to a new model of cloud operations that is intelligent, automated, policy-aware, and built on software engineering principles rather than manual configuration.

Organizations that invest now in **modern IaC**, **unified governance**, **reusable components**, and **policy frameworks**, all core capabilities of the Pulumi Cloud platform, will be positioned to lead in an AI-first world. The gap between teams that modernize and those that do not will widen rapidly in 2027 and beyond.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}
