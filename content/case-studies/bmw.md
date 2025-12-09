---
title_tag: BMW | Case Studies
title: "Unified Infrastructure and Application Management at Scale"
description: |
    Learn how BMW's Software Factory uses Pulumi to manage 20,000+ cloud resources with Python-based infrastructure code.
meta_desc: Learn how BMW's Software Factory uses Pulumi to manage 20,000+ cloud resources with Python-based infrastructure code.

customer_name: BMW
customer_logo: /logos/customers/bmw.svg
customer_url: https://www.bmwusa.com/

quote_block:
    quote: |
        Software Factory manages over 20,000 cloud resources using Python-based infrastructure code integrated with existing CI/CD workflows.
    headline_stat: 20,000+
    headline: cloud resources managed across multiple stacks

aliases:
    - /case-studies/codecraft
---

## The Enterprise Infrastructure Challenge

As organizations scale their cloud infrastructure, they face a critical choice: continue managing infrastructure and applications as separate concerns with different tools and workflows, or unify them under a single, programmable approach. Traditional infrastructure-as-code tools require learning proprietary languages and often force teams to maintain parallel toolchains for application deployment and infrastructure provisioning.

Platform engineering teams need solutions that can scale to thousands of resources across multiple environments while maintaining security, compliance, and developer productivity. They need the full power of real programming languages, not limited domain-specific languages. And they need infrastructure that integrates naturally with their existing CI/CD pipelines rather than requiring separate automation workflows.

## About CodeCraft

The automobile is becoming increasingly more connected over time and software is now central to the operation of nearly every component. This necessitates a development platform that is designed for the continuous evolution of technology in vehicles and the additional complexity it brings. CodeCraft is BMW’s integrated toolchain for the software-defined-vehicle that is managed and deployed by Pulumi.

{{< youtube "HIliBBo4c-g?rel=0" >}}

## Pulumi's Approach

Pulumi addresses these challenges by enabling teams to define both infrastructure and application deployments using familiar programming languages like Python, TypeScript, and Go. This unified approach eliminates the artificial boundary between infrastructure provisioning and application management.

Key capabilities include:

**Real Programming Languages**: Teams can use standard Python, TypeScript, Go, or other languages they already know. This means access to existing libraries, testing frameworks, and development tools rather than learning proprietary syntax.

**Unified Management**: A single Pulumi program can define Kubernetes clusters, configure cloud resources, and deploy applications. This eliminates coordination overhead between separate toolchains and reduces deployment complexity.

**Cloud-Native Integration**: Pulumi works naturally with modern cloud platforms and Kubernetes. Resources are code that integrates directly into existing CI/CD pipelines without requiring additional infrastructure automation.

**Policy as Code**: Security and compliance requirements can be enforced programmatically across all infrastructure. Teams can define policies once and apply them consistently across all cloud providers and services.

**State Management**: Pulumi provides centralized state management that tracks all deployed resources. This enables teams to understand dependencies, audit changes, and coordinate updates across complex infrastructure.

## Proven at Enterprise Scale

BMW Group's Software Factory IT infrastructure platform demonstrates these capabilities in production. The platform manages over 20,000 cloud resources across multiple stacks using Python-based Pulumi programs integrated with their existing CI/CD pipeline. The implementation consolidated earlier toolchain approaches, including Ansible, Terraform, and Helm, into a unified workflow that manages both Kubernetes clusters and the applications deployed to them.

## Results That Matter

Enterprise implementations of Pulumi demonstrate measurable benefits:

**Reduced Complexity**: Unified infrastructure and application management eliminates coordination overhead between separate toolchains

**Familiar Tools**: Infrastructure defined in standard programming languages rather than proprietary domain-specific languages

**Automated Compliance**: Centralized policy enforcement across all cloud resources ensures security and governance requirements are met automatically

**Single Workflow**: Code commit through infrastructure deployment happens in one integrated process

**Incremental Adoption**: Organizations can adopt Pulumi gradually, running it alongside existing tools during migration for low-risk evaluation

## Looking Forward

As organizations move toward platform engineering models, the need for unified infrastructure and application management continues to increase. The artificial separation between infrastructure and application teams breaks down when both manage cloud-native resources through APIs.

Pulumi's approach treats infrastructure as software, applying the same engineering practices to infrastructure that successful organizations already apply to applications. This includes version control, code review, automated testing, and continuous integration and deployment.

For platform teams managing complex multi-cloud or Kubernetes-based infrastructure, this unified approach reduces operational overhead and improves reliability. Rather than coordinating between multiple tools with different workflows, teams can manage their entire stack through a single, programmable interface.
