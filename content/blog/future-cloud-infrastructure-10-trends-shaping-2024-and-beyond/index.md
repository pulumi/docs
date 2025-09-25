---
title: "Future of the Cloud: 10 Trends Shaping 2026 and Beyond"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-11-18T07:56:40Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: "The year of Cloud Optimization is here! Explore the top 10 trends, including IaC, AI/ML, Kubernetes, platform engineering, security, FinOps, data, and more."

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: "cloud-computing-forecast.png.png"

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
    - finops
    - platform-engineering
    - devops
    - devsecops
    - security

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

In 2026, several trends will dominate cloud computing, driving innovation, efficiency, and scalability. From Infrastructure as Code (IaC) to AI/ML, platform engineering to multi-cloud and hybrid strategies, and security practices, let's explore the 10 biggest emerging trends.

<!--more-->

## 1. Cloud Will Become a Business Necessity by 2028

According to [Gartner](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/cloud-computing), by 2028 the cloud will be the key driver for business innovation, and estimates that over 95% of new digital workloads will be deployed on cloud-native platforms.

{{< figure alt="The future of cloud computing. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/gartner-cloud-2028.png" caption="The future of cloud computing. Credit: Gartner" width=100% >}}

According to McKinsey & Company's "[In search of cloud value](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/in-search-of-cloud-value-can-generative-ai-transform-cloud-roi)" report:

- Cloud enables businesses to innovate, which is worth more than x5 what is possible by simply reducing costs.
- The anticipated increase in EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization) attributable to cloud adoption is projected to range between 20% and 30% by the year 2030 - but it's expected to vary across different sectors.
- Asian companies have the most to gain from the cloud, with $1.2 trillion in EBITDA. American institutions stand to capture about $1.1 trillion in cloud value, while European institutions are at $773 billion due to regulatory constraints.
- Companies that have captured the most ROI consistently do 3 things well: 1/ work closely with business leaders to focus on high-value business cases, 2/ build a robust cloud foundation, and 3/ adopt a product-oriented operating model.

## 2. AI-Driven Expansion and Investment from Hyperscalers

AI workloads, especially large language models (LLMs), are driving unprecedented demand for cloud infrastructure.

- **AWS** has integrated [Anthropic’s Claude 3 and Claude 4 models into Amazon Bedrock](https://www.aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock) for enterprise LLM workflows. “Claude Opus 4 and Claude Sonnet 4 are available today in Amazon Bedrock, enabling customers to build agents with stronger reasoning, memory, and tool use.” — AWS, May 2025
- **Microsoft Azure** revenue rose 33% year-over-year in Q3 (ended March 31), outperforming estimates of ~29.7%. [AI contributed 16 percentage points to this growth](https://www.reuters.com/business/microsoft-beats-quarterly-revenue-estimates-ai-shift-bolsters-cloud-demand-2025-04-30/), up from 13 points in the prior quarter. "Microsoft is on track to invest approximately $80 billion to build out AI-enabled datacenters to train AI models and deploy AI and cloud-based applications around the world," said Brad Smith, the Microsoft Vice Chair and President.
- **Google Cloud** is committing [$25 billion over two years for data center and AI infrastructure expansion](https://www.utilitydive.com/news/google-cloud-blackstone-aws-us-ai-data-center-buildouts/753202) across the PJM grid, with total capital expenditure for 2025 ranging from $75–85 billion. "As our CEO has said, in these early days of a very transformative technology, the risks of under investing are dramatically higher than the risks of over investing," said Eunice Huang, Head of AI and Emerging Tech Policy.
- **Oracle** anticipates 15–20% cloud revenue growth in FY 2026–2027 attributable to AI infrastructure demand, tied to its partnership in the [Stargate initiative](https://www.pcgamer.com/software/ai/openais-skyrocketing-spending-could-see-billions-of-dollars-in-silicon-headed-down-the-ai-mines-in-the-next-few-years-including-2-million-nvidia-chips-headed-to-texas-stargate-facility/).

{{< figure alt="Most popular cloud computing infrastructure by industry. Credit: Cloud Worldwide Service, Forbes" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/most-popular-cloud-computing-infrastructure-by-industry.png" caption="Credit: Cloud Worldwide Service, Forbes" width=100% >}}

## 3. Cloud Infrastructure Meets Physical Limits

The massive growth in AI infrastructure is pushing power and water systems to their limits. According to [Goldman Sachs](https://www.goldmansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030/), data center power demand will increase by 50% by 2027 and 165% by 2030. The International Energy Agency (IEA) projects that data centers could account for over 20% of electricity demand growth in advanced economies.

Cloud providers like AWS, Microsoft, and Google are investing heavily in renewable energy, modular data centers, and efficient cooling systems. Sustainability is no longer optional, it’s a capacity constraint.

- **AWS** announced they will [expand water recycling at data center to over 120 locations by 2030](https://www.aboutamazon.com/news/sustainability/amazon-water-conservation-replenishment-sustainability?p=amazon-to-expand-water-recycling-at-data-centers-to-over-120-locations-across-the-us). “AWS’ new initiative will support communities by easing pressure on local water systems while meeting the needs of the rapidly growing AI economy," said Howard Carter, president of Water Environment Federation (WEF).
- **Google** continues its [goal set in 2021 to replenish 120% of the water](https://blog.google/outreach-initiatives/sustainability/4-new-partnerships-to-help-water-stewardship-and-sustainable-farming/) used in its offices and to cool data centers by 2030. "Google's water stewardship strategy goes beyond managing our own water use — we're actively working to improve watershed health in the communities where we operate," said Ben Townsend, Head of Infrastructure & Sustainability.
- **Microsoft Azure** had ambitious goals for 2025, aiming to power all its data centres with renewable energy sources such as wind, solar, hydroelectric, or geothermal. They continue to work towards being carbon negative by 2030. "We are also on track to replenish more water than we consume across global operations and improve datacenter water use efficiency, including through a new innovative datacenter design that optimizes AI workloads and consumes zero water for cooling to avoid the use of an estimated 125,000 cubic meters annually per facility," said Melanie Nakagawa, Chief Sustainability Officer.

## 4. Hybrid, Multi-Cloud, and Edge as the New Normal

Recent market analysis from [ResearchAndMarkets](https://www.businesswire.com/news/home/20250513124988/en/Hybrid-Cloud-Market-Analysis-Growth-Trends-and-Forecasts-Report-2024-2025-2030-Surging-Demand-for-Seamless-Interoperability-Between-Cloud-Services-and-Existing-Systems---ResearchAndMarkets.com?utm_source=chatgpt.com) forecasts that the **hybrid cloud market** will double in size from **~$130B in 2024 to $310–330B by 2030**, a shift driven by AI workloads, platform engineering, microservices, and edge computing. [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/hybrid-cloud-market) also reports that **~87% of enterprises run workloads across multiple providers**, confirming that multi-cloud is practically universal among large organizations as of 2025.

{{< figure alt="Most popular cloud computing infrastructure by industry. Credit: Cloud Worldwide Service, Forbes" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/most-popular-cloud-computing-infrastructure-by-industry.png" caption="Credit: Cloud Worldwide Service, Forbes" width=100% >}}

Generative AI workloads are also accelerating hybrid and edge adoption. According to [Nutanix’s 2025 Enterprise Cloud Index](https://www.nutanix.com/enterprise-cloud-index), **90% of enterprises report that GenAI strategy affects infrastructure planning**. While model training remains centralized, inference is increasingly executed near users to reduce latency. AWS and NVIDIA have extended their cooperation with the Project Ceiba supercomputer to meet these needs. As a result, orchestration software must now schedule AI pipelines across edge clusters and centralized data centers—deepening enterprise reliance on hybrid cloud architectures.

## 5. Infrastructure as Code (IaC) Crucial for Scalability

IaC in general-purpose languages is gaining prominence as organizations seek to automate and streamline their infrastructure management processes and reduce the divide between application development and cloud infrastructure development.

[Infrastructure as Code](https://www.pulumi.com/what-is/what-is-infrastructure-as-code/) is maturing beyond taming the complexity of the cloud:

- Facilitating the adoption and configuration standardization of multi-cloud and hybrid strategies
- Better integration with multiple cloud providers, like [AWS](https://www.pulumi.com/docs/iac/clouds/aws/), [Azure](https://www.pulumi.com/docs/iac/clouds/azure/), and [Google Cloud](https://www.pulumi.com/docs/iac/clouds/gcp/), data stores, and third-party services like [Cockroach Labs db](https://www.pulumi.com/registry/packages/cockroach/), [Confluent cloud](https://www.pulumi.com/registry/packages/confluentcloud/), [Kafka](https://www.pulumi.com/registry/packages/kafka/), and more
- Deeper validation on parameters that people are passing in, checking all critical components, ensuring they are configured correctly before deployment
- More [efficient resource management](https://www.pulumi.com/docs/pulumi-cloud/insights/)
- Robust security and [Policy as Code](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/core-concepts/) to enforce security practices, guardrails, compliance, cost policies, and more
- Intelligent automation, including [automated tests](https://www.pulumi.com/docs/iac/concepts/testing/) and [remediation policies](https://www.pulumi.com/blog/remediation-policies/)
- [AI-driven automation and insights](https://www.pulumi.com/product/pulumi-insights/)

## 6. DevSecOps and Policy-as-Code Become Standard

Security is now embedded directly into cloud-native workflows. DevSecOps practices, backed by AI-powered threat detection and automated remediation, are becoming mainstream. Below are the 3 key predictions for the future of DevSecOps:

1. **AI-Driven Security**: AI and machine learning (ML) will be instrumental in automating security and in [providing real-time insights](https://www.pulumi.com/blog/pulumi-insights-2/), enabling proactive and predictive security measures.
2. **More Focus on Secrets Management**: Organizations will prioritize [robust secrets management](https://www.pulumi.com/product/secrets-management/) within their DevSecOps processes as data privacy concerns escalate. It will be essential to secure sensitive data such as API keys, credentials, and other secrets to ensure compliance and avoid unauthorized access.
3. **Collaboration as a Key Factor**: Collaboration between development, security, and operations teams will be crucial for the success of DevSecOps efforts.

[Policy as Code](https://www.pulumi.com/docs/iac/packages-and-automation/crossguard/) will also be an indispensable pillar in many security aspects:

1. Use off-the-shelf rules or define your best practices for security, cost, compliance, and reliability
2. Maintain security across all cloud infrastructure assets
3. Catch policy violations before they escape using CI/CD
4. Automate governance using programmable libraries and REST APIs, easily integrating with external services such as web services, asset tracking databases, pricing lists, and more

## 7. Platform Engineering & Internal Developer Platforms (IDPs)

According to [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering), **by 2026, 80% of large software engineering organizations will establish platform engineering teams** as internal providers of reusable services, components, and tools for application delivery. Platform engineering will ultimately solve the central problem of cooperation between software developers and operators.

Mid-size to large companies will begin or [continue to invest in implementing platform engineering practices](https://www.pulumi.com/product/internal-developer-platforms/), with large tech companies as first adopters. They will provide [Internal Developer Portals (IDP)](https://www.pulumi.com/blog/building-developer-portals/) to elevate the Developer Experience (DX, sometimes referred to as DE or DevEx), helping them work faster, like abstracting the complexities of configuring, testing, and validation, deploying infrastructure, and scanning their code for security.

{{< figure alt="Internal developer platform-in-a-box. Credit: Pulumi" src="https://www.pulumi.com/blog/developer-portal-platform-teams/platform-teams.png" caption="Internal developer platform-in-a-box. Credit: Pulumi" width=100% >}}

IDPs are reshaping how developers interact with cloud infrastructure—via UI, CLI, APIs, or GitOps—making self-service infrastructure a reality.

## 8. AIOps Matures into a Cloud Operations Standard

AIOps is becoming is mainstream, helping teams predict failures, auto-scale infrastructure, and resolve incidents with minimal manual effort. As AI and automation continue to evolve, the fusion of these technologies will enable organizations to achieve unprecedented levels of efficiency and scalability.

- **Proactive Operations**: AI-powered tools will assist teams in foreseeing issues with greater accuracy, minimizing downtime, and reducing the firefighting nature of incident management. These tools will automatically detect anomalies, optimize performance, and trigger remediation actions.
- **[Intelligent Automation](https://www.pulumi.com/docs/iac/packages-and-automation/automation-api/)**: Routine operational tasks like patching, monitoring, and resource scaling will be fully automated. AI-driven decision-making will allow for smarter resource allocation and optimization, dynamically adjusting infrastructure and workloads in response to real-time demands and predictions.
- **[Data-Driven Insights](https://www.pulumi.com/docs/pulumi-cloud/insights/)**: AIOps will analyze vast amounts of operational data and provide actionable insights, enabling teams to focus on high-impact tasks such as improving system architecture and user experience. The AI-powered insights will also inform better strategic decisions, helping teams to continuously evolve their DevOps practices.
- **Collaboration Across Teams**: AIOps will bridge the gap between DevOps, SecOps, and IT operations by bridging monitoring and automation. Cross-team collaboration will improve as AI systems consolidate and interpret data from various departments, allowing for a more cohesive approach to system management.

AIOps features include observability, automation, and real-time analytics to bridge DevOps, SRE, and IT operations.

## 9. Kubernetes Dominance and Increased Complexity

Kubernetes, the open-source container orchestration platform, will continue its ascent in 2026. According to [Markets N Research](https://marketsnresearch.com/report/1649/global-kubernetes-market), the global Kubernetes market size was valued at USD 1.8 billion in 2022 and is projected to be **USD 7.8 billion by 2030, exhibiting a CAGR of 23.40%** during the forecast period.

The "growing pains" will also increase with rising concerns in security, networking, deployment, scalability, cost, and impact on developer productivity. Read the previous LinkedIn Newsletter article [From Complexity to Simplicity: Streamlining Kubernetes with Infrastructure as Code](https://www.linkedin.com/pulse/from-complexity-simplicity-streamlining-kubernetes-infrastructure?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BHF6x7jyoRWSmk9POeHy0TA%3D%3D).

Kubernetes is also evolving in response to AI demands. Inference workloads, powered by LLMs and GPUs, now require low-latency execution closer to the user. This shift is pushing organizations to build intelligent orchestration layers that schedule AI pipelines across edge and core clusters—often leveraging Kubernetes as the common control plane.
Additionally, FinOps and security are becoming deeply integrated into Kubernetes workflows. Policy-as-code extensions are gaining traction to ensure cost transparency, policy enforcement, and secure defaults.

## 10. AI Code Assistants in the Enterprise

Developers worldwide have explored or are currently using AI-powered coding assistants. However, many enterprises have shown resistance to allowing them to be part of their AI tools in software development. Still, software engineering leaders are beginning to recognize that these coding assistants can enhance team productivity, improve code quality, and maintain a competitive advantage.

**By 2027, the use of [AI assistants](https://www.pulumi.com/product/copilot/) will dramatically increase developer velocity** to meet functional business requirements for 70% of new digital solutions in production (source: [IDC](https://www.digitalnewsasia.com/business/idc-reveals-its-top-predictions-cloud-2023-and-beyond)).

{{< figure alt="The value of AI code assistants. Credit: Gartner" src="/blog/future-cloud-infrastructure-10-trends-shaping-2024-and-beyond/ai_code_assistants_value.png" caption="The value of AI code assistants. Credit: Gartner" width=100% >}}

According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028), **by 2028, 75% of enterprise software engineers will use dedicated AI code assistants**, and 63% of organizations are currently piloting, deploying or beginning to [use AI code assistants, just like Pulumi AI](https://www.pulumi.com/ai).

## Future Cloud Trends: AI-Native, Sustainable, and Composable

Cloud infrastructure is entering a new era. By 2030, the dominant cloud model will be:

- **AI-native**, integrating LLMs and inference at the infrastructure level
- **Sustainable by design**, driven by power, water, and climate constraints
- **Composable and sovereign**, blending public, private, edge, and national clouds
- **Governed by code**, through DevSecOps, AIOps, and FinOps automation

Organizations that embrace these shifts—backed by modern infrastructure as code and platform engineering practices—will lead the next wave of cloud innovation.
