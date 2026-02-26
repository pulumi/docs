---
title: "Run Pulumi Insights on Your Own Infrastructure"
date: 2026-02-26T00:06:00-07:00
draft: false
meta_desc: "Run Pulumi Insights discovery scans and policy evaluations on your own infrastructure with customer-managed workflow runners."
meta_image: meta.png
authors:
    - levi-blackstone
tags:
    - insights
    - features
    - pulumi-cloud
    - policy-as-code
---

[Pulumi Insights](/docs/insights/) gives you visibility and governance across your entire cloud footprint: **discovery scans** catalog every resource in your cloud accounts, and **policy evaluations** continuously enforce compliance against those resources. Until now, Insights workflows ran exclusively on Pulumi-hosted infrastructure. That works well for many teams, but enterprises with strict data residency requirements, private network constraints, or regulatory obligations need to run this work in their own environments. Today, Pulumi Insights supports [customer-managed workflow runners](/docs/deployments/deployments/customer-managed-agents/) for both SaaS Pulumi Cloud and [self-hosted Pulumi Cloud](/docs/administration/self-hosting/) installations.

<!--more-->

## Insights at a glance

Insights provides two complementary capabilities that together form a governance lifecycle for your cloud infrastructure.

**Discovery** scans cloud accounts across AWS, Azure, GCP, and more to catalog every resource regardless of how it was provisioned: Pulumi, Terraform, CloudFormation, or manual creation. Once cataloged, you can search, filter, group, and [export](/docs/insights/discovery/data-export/) your resource data. You can also [import](/docs/insights/discovery/visual-import/) unmanaged resources into Pulumi to bring them under IaC management.

**Policy** enforces compliance with policy-as-code written in TypeScript or Python. Pulumi ships [pre-built compliance packs](/docs/insights/policy/policy-packs/pre-built-packs/) for CIS, NIST, PCI DSS, HITRUST, and other frameworks so you can start evaluating without writing any code. [Audit policy groups](/docs/insights/policy/policy-groups/#audit-policy-groups) continuously evaluate all discovered resources and IaC stacks, while preventative policies block non-compliant deployments before they reach production.

This enables you to map out your cloud estate, evaluate compliance, and then remediate any issues uncovered by policy.

## Why self-hosted?

Running Insights on your own infrastructure with [customer-managed workflow runners](/docs/deployments/deployments/customer-managed-agents/) gives you:

- **Data residency**: Scan execution and policy evaluation run entirely within your private network.
- **Private infrastructure access**: Scan resources in VPCs and environments that are not accessible from the public internet.
- **Compliance**: Cloud provider credentials can stay internal to your network, meeting regulatory requirements for credential handling.
- **Flexible hosting**: Run workflow runners on any environment that meets your needs, including Linux, macOS, Docker, and Kubernetes.

## How it works

Customer-managed workflow runners are lightweight agents that poll Pulumi Cloud for pending work, execute it locally, and report results back. You can configure runners to handle specific workflow types: discovery scans, policy evaluations, deployments, or all three.

This works identically whether you use SaaS Pulumi Cloud or a self-hosted installation. The runner communicates with the Pulumi Cloud API over HTTPS, so no inbound connectivity is required, making it well suited to run in restricted network environments.

Under the hood, this is powered by a distributed work scheduling system that routes activities to the right runner pool, handles lease-based execution, and recovers automatically from failures. For a deep dive on the architecture, see [How We Built a Distributed Work Scheduling System for Pulumi Cloud](/blog/how-we-built-a-distributed-work-scheduling-system-for-pulumi-cloud/).

If your team already uses customer-managed workflow runners for [Pulumi Deployments](/docs/deployments/), your existing runner pools can handle Insights workflows with no additional infrastructure.

## Get started

Self-hosted Insights is available on the Business Critical edition of Pulumi Cloud. To learn more or get set up:

- [Self-hosted Insights documentation](/docs/insights/self-hosted/) — configuration and setup for discovery scans and audit policy evaluations on your own infrastructure
- [Customer-managed workflow runners](/docs/deployments/deployments/customer-managed-agents/) — runner installation, configuration reference, and pool management
- [Insights & Governance overview](/docs/insights/) — full documentation for discovery and policy capabilities
- [Contact sales](/contact/?form=sales) to enable self-hosted Insights for your organization
