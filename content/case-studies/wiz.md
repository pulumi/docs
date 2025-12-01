---
title_tag: Wiz | Case Studies
title: "How Wiz Operates Kubernetes at Global Scale with Pulumi"
allow_long_title: true
description: |
    Wiz uses Pulumi's Automation API to manage thousands of Kubernetes clusters across hundreds of data centers worldwide, handling hundreds of thousands of infrastructure updates daily while maintaining over a million cloud resources.
meta_desc: See how Wiz uses Pulumi to operate thousands of Kubernetes clusters globally, processing hundreds of thousands of infrastructure updates daily.
meta_image: "/images/case-studies/wiz.png"

customer_name: Wiz
customer_logo: /logos/customers/wiz.png
customer_url: https://www.wiz.io/

quote_block:
  quote: |
      "We use Pulumi widely at Wiz. It enabled our product to support multi-cloud and to scale quickly - scaling and driving hundreds of thousands of infrastructure updates every day."
  quote_attrib: Yarin Miran, Senior Software Engineer, Wiz
  headline_stat: 1M+ Cloud Resources
  headline: Managed across thousands of Kubernetes clusters

exec_summary: |
    When [Wiz](https://www.wiz.io/) needed to scale their cloud security platform globally, they faced a challenge that would break most traditional infrastructure approaches: dynamically provisioning and managing Kubernetes clusters across every major cloud provider, in every region where their customers operate – including supporting deployments into customers' cloud accounts where required. Using Pulumi's Automation API and Go SDK, Wiz built a system that now manages thousands of Kubernetes clusters across hundreds of data centers worldwide, handling hundreds of thousands of infrastructure updates daily while maintaining over a million cloud resources and tens of thousands of Kubernetes clusters—infrastructure scale that enables Wiz to onboard enterprise customers 5x faster and expand into new markets within days rather than months.

    Applying modern programming languages and Infrastructure as Code (IaC) enabled Wiz to build the global scanning infrastructure that would ultimately contribute to their position as one of the fastest-growing companies in cybersecurity.  This infrastructure foundation became one of the factors in  Wiz's position as one of the fastest-growing companies in cybersecurity history, securing half the Fortune 100 and protecting millions of cloud workloads while maintaining the agility to outpace competitors in new market entry.

sections:
    - label: The Challenge
      anchor: the-challenge
    - label: The Pulumi Solution
      anchor: the-pulumi-solution
    - label: Global Infrastructure
      anchor: global-infrastructure
    - label: Scale
      anchor: scale
    - label: Business Impact
      anchor: business-impact
    - label: Resilience
      anchor: resilience
    - label: Lessons
      anchor: lessons
    - label: The Future
      anchor: the-future
    - label: Conclusion
      anchor: conclusion
---

## The Challenge: Planet-Scale Kubernetes {#the-challenge}

Wiz's core security offering requires them to scan cloud environments and correlate huge amounts of sensitive data: configurations, vulnerabilities, network exposure, identities, permissions, secrets, and workload metadata about where their customers' workloads actually run. This creates a unique infrastructure challenge: they need a presence in every cloud and every region where their customers operate. As Yarin Miran, Lead Engineer at Wiz, explains: "We need to be everywhere. We have clusters in Amazon, Azure, GCP, Alibaba, Oracle Cloud. We have more than a hundred data centers by now, and each data center has its own set of clusters per region, per cloud."

The complexity extends beyond simple geographic distribution. Wiz's scanning infrastructure centers on Kubernetes clusters that attach customer volumes and perform deep security analysis. But customers have varying requirements that make each deployment unique. Some customers require scanning to happen within their own cloud accounts for compliance reasons—what Wiz calls "Outposts." Others need specific networking configurations, security controls, or regulatory compliance measures that vary by region and industry.

This leads to a combinatorial explosion of infrastructure requirements, with virtually limitless permutations. Each customer requires a unique blend of cloud provider, region, network configuration, security controls, and deployment model. Traditional infrastructure management approaches were never designed to support this level of dynamic complexity, automation, and governance at scale—let alone keep pace with constantly evolving customer needs and security threats.

## The Pulumi Solution: Infrastructure as Real Code {#the-pulumi-solution}

Wiz's decision to adopt Pulumi came at a serendipitous moment. "This really clicked for me with Pulumi because when we first thought about the automated solution, how to provision all these clusters, Pulumi had just announced the Automation API," Yarin explains. "I think I started playing with it two days after the announcement."

The Automation API was the key differentiator. Unlike traditional IaC tools that required CLI interactions or external orchestration, Pulumi's Automation API allowed Wiz to embed infrastructure provisioning directly into their Go applications. This meant they could treat infrastructure provisioning as just another service in their distributed system, with the same error handling, monitoring, and operational practices they applied to the rest of their platform.

The Go SDK provided seamless integration with their existing backend services, while Pulumi's multi-cloud support meant they could use a single programming model across AWS, Azure, Google Cloud, Alibaba Cloud, and Oracle Cloud. Most importantly, the programmatic approach allowed them to dynamically generate infrastructure configurations based on customer requirements without maintaining hundreds of static configuration files.

## A Global Infrastructure Orchestration Architecture {#global-infrastructure}

Wiz built their infrastructure provisioning system around two main components that work together to manage their global Kubernetes footprint. The Stack Provisioner uses Pulumi's Automation API to handle the infrastructure layer which involves creating Kubernetes clusters, configuring networking, provisioning storage, and setting up messaging queues for workload distribution. Each deployment is managed as a separate Pulumi stack, giving them fine-grained control over individual customer environments while maintaining consistency across their global infrastructure.

The Helm Provisioner takes over after the infrastructure is ready, managing Kubernetes application deployments through a GitOps approach. This separation of concerns allows them to handle infrastructure provisioning through Pulumi's robust state management while leveraging GitOps patterns for application lifecycle management.

Their architecture dynamically adapts to customer requirements. Outpost deployments configure infrastructure within customer accounts using provided service credentials. Different compliance requirements trigger different networking configurations, security controls, and monitoring setups. Feature flags control which capabilities are enabled for each customer, and the system can provision everything from basic scanning clusters to complex multi-tier infrastructures with specialized storage and networking requirements.

## Millions of Resources, Tens of Thousands Kubernetes Clusters {#scale}

The results speak to the power of programmatic infrastructure management. Wiz now operates thousands of Pulumi stacks, with each stack managing an individual Kubernetes cluster. These clusters span more than 100 data centers globally and manage over a million cloud resources. The system processes hundreds of thousands of stack updates daily, continuously adapting to changing customer requirements and operational needs.

But the real story isn't just about the numbers, it's about operational efficiency. "It's funny, but our team manages more resources than the DevOps team," Yarin observes. This scale is possible because Pulumi's programmatic approach enabled them to build automated systems that handle the complexity of global infrastructure management without requiring proportional increases in operational headcount.

The business impact has been game-changing for revenue growth and market expansion. Wiz can enter new markets in days rather than quarters, provisioning compliant infrastructure across any cloud provider and region. This agility enabled Wiz to capture first-mover advantages in emerging markets and respond to enterprise RFPs 5x faster than competitors still relying on manual infrastructure processes. They can adapt to diverse customer requirements through flexible deployment models. And they can scale their infrastructure automatically as their business grows, without the manual overhead that would typically come with managing thousands of infrastructure deployments.

## From Automation to Business Impact {#business-impact}

Wiz's infrastructure automation delivers measurable business value: 5x faster customer onboarding, 10x more efficient resource management per engineer, and the ability to enter new geographic markets within days rather than months. This operational leverage has been crucial to Wiz's ability to scale revenue while maintaining industry-leading margins in the competitive cybersecurity market.

## From Resilience to FedRAMP {#resilience}

Operating at this scale requires sophisticated engineering practices. Wiz has built comprehensive error handling and recovery mechanisms that go far beyond basic infrastructure management. They've developed multi-layered parsing systems that interpret Pulumi outputs to understand the actual errors, missing permissions, and customer-facing issues that need to be addressed. Their system includes automated recovery mechanisms for interrupted operations, garbage collection for duplicate or orphaned resources, and health monitoring that continuously validates infrastructure state. When operations are interrupted, whether due to pod crashes, node reallocations, or other infrastructure events, their system can automatically detect and recover without manual intervention. The team has also extended Pulumi's capabilities to accelerate their FedRAMP compliance efforts - achieving FedRAMP High authorization in September 2025.

## Lessons in Large-Scale Infrastructure Management {#lessons}

Wiz's experience offers several key insights for organizations operating infrastructure at scale. First, programmatic infrastructure management becomes essential when dealing with dynamic, customer-specific requirements. The ability to use real programming languages for infrastructure provisioning enabled them to build systems that would have been impossible with traditional configuration-based approaches.

Second, the Automation API pattern: embedding infrastructure provisioning directly into applications, provides significant advantages over CLI-based workflows. This approach allows infrastructure provisioning to be treated as a first-class service with the same operational practices applied to other distributed systems.

Third, comprehensive error handling and recovery mechanisms are crucial for large-scale operations. When managing thousands of infrastructure deployments, manual intervention becomes impossible. Automated detection, recovery, and remediation systems are essential for maintaining operational excellence.

Finally, the choice of IaC platform matters significantly when operating at scale. Tools that treat infrastructure as configuration files may work for smaller deployments but become unmaintainable when dealing with hundreds or thousands of unique infrastructure configurations. Programmatic approaches that leverage full programming language capabilities become essential for managing complexity at scale.

## The Future of Infrastructure at Wiz {#the-future}

Wiz continues to expand their use of Pulumi across their platform. They're migrating additional backend services from SDK-based provisioning to Pulumi, enabling more engineering teams to leverage the same infrastructure management capabilities. They're also exploring Pulumi's policy engine for infrastructure governance, which could provide additional controls and compliance capabilities across their global infrastructure.

## Conclusion: Infrastructure as a Competitive Advantage {#conclusion}

Wiz's success stems from several factors, including the ability to scale rapidly and innovate at speed to maximize customer value. As part of that approach, they proved that IaC can become a competitive advantage when done right. By choosing tools that embrace programming languages and programmatic approaches, they built an infrastructure foundation that scales with meteoric business growth while maintaining the flexibility to meet diverse customer requirements across all of the major cloud providers.

Their success with Pulumi reflects Wiz's customer centric mindset and need to serve customers across multiple clouds and regions, ultimately contributing to their position as a leading cloud security platform. As they continue to expand their use of programmatic infrastructure management, Wiz serves as a compelling example of how modern IaC can enable business success at global scale.

The story of Wiz and Pulumi isn't just about managing thousands of  Kubernetes clusters, it's about building infrastructure systems that can adapt, scale, and evolve with business requirements, securely and productively. In an era where infrastructure agility can determine competitive advantage, Wiz's innovative approach to using Pulumi represents the future of modern cloud infrastructure management at scale.

Wiz secures everything built and run in the cloud. The platform powers a new operating model for security, development, and ops teams by providing a holistic view of risk. Wiz gives everyone clear visibility into their cloud and AI environments, enriched with context so they can prioritize what matters most.
