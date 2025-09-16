---
title: "Announcing New Policy Packs and Policy Management Experience"
date: 2025-09-17
authors:
    - luke-ward
    - dan-biwer
    - insights-team
meta_desc: "Announcing new UX for Pulumi Policy and new pre-built policy packs, providing essential guardrails for all cloud infrastructure automation"
allow_long_title: true
meta_image: "meta.png"
tags:
    - pulumi-service
    - policy-as-code
    - crossguard
    - features
    - user-experience
    - pulumi-neo
    - ai
---

AI has fundamentally changed application development. Developers are shipping more code, faster than ever before. Every new feature and application generated needs to run on the cloud, creating an unprecedented amount of new infrastructure for platform teams to manage.

This explosion in developer velocity has created a massive governance challenge. How do you ensure all this new infrastructure is secure, compliant, and cost-effective when it's being created at a speed that's impossible to manually review?

The answer is to build automated guardrails that apply everywhere, regardless of the entry point—whether infrastructure is provisioned by a developer using an AI assistant or self-service Internal Developer Platform (IDP). Yesterday, we introduced [Pulumi Neo](/blog/pulumi-neo/), our own AI platform engineer that helps manage this complexity. Today, we're excited to announce the other side of the story: a fundamentally redesigned policy management experience that provides a consistent governance layer for your entire platform.

<!--more-->

## Primer on Pulumi Policy

[Pulumi Policy as Code](/docs/iac/crossguard/) (PaC) applies the same principles of DevOps and Infrastructure as Code to your organization's governance. PaC allows you to version, test, and peer-review your policies through pull requests, just like any other critical software. It’s the only way to scale governance to match the speed of modern development.

Unlike other PaC tools that rely on restrictive, domain-specific languages (DSLs) or YAML, Pulumi Policy uses the general-purpose programming languages you already know and love: **TypeScript and Python**. It unlocks powerful capabilities that are difficult or impossible to achieve with other approaches. With PaC you can:

* **Express rich, conditional logic** to codify your organization's nuanced rules.
* **Create reusable functions and abstractions** to build a library of policies that can be shared across your organization.
* **Write unit tests** for your policies to ensure they work as intended before you deploy them.

It allows you to codify your rules with precision and scale. And with today's announcement, we've made this powerful foundation more accessible and easier to manage than ever.

## A New, Simplified Approach

While Pulumi Policy has always allowed you to enforce compliance using TypeScript and Python, the existing workflow could be cumbersome—discovering policies required switching between the console and CLI, and applying them involved multiple steps.

We've removed that friction to provide the seamless guardrails needed for this high-velocity, AI-driven world. The new experience is built around a streamlined, in-console workflow for discovering, applying, and managing your policies.

### In-Console Discoverability

We are making it easier to find and understand policy packs. You can now browse a rich set of pre-built policy packs directly within the Pulumi Cloud console—no CLI or context switching required.

You’ll find:

* **A rich browsing experience:** See all available policy packs in one place.
* **Detailed information:** Each pack comes with a clear description of the policies included and usage instructions.
* **Organization-approved packs:** Org admins can curate a list of approved policy packs, ensuring your teams—and AI agents like Neo—are using a vetted set of policies.

### New Pre-Built Policy Packs

To help you establish guardrails immediately, we have authored several [pre-built policy packs](/docs/insights/pre-built-packs/). We are excited to highlight two that are available today:

* **Pulumi Best Practices:** A foundational set of recommended governance and security controls that serves as a strong starting point for any organization.
* **HITRUST CSF v11.5:** Provides predefined controls that help align cloud resources with HITRUST CSF requirements.

### Streamlined Policy Management and Application

The new policy management experience dramatically simplifies policy application:

* **Intuitive Interface:** Browse, select, and apply policies through a streamlined workflow using **Policy Groups** to bundle related policies and apply them to your stacks or cloud accounts.
* **Expanded Scale:** We've eliminated the 4,000 stack UI limit on policy groups, allowing you to scale policies across your entire infrastructure.
* **Granular Enforcement:** Configure the enforcement level (`advisory` or `mandatory`) for policies to either warn developers or block non-compliant deployments entirely.

### Understanding Policy Approaches

The new UI simplifies the two powerful enforcement approaches Pulumi supports:

* **Preventative policies**: Block non-compliant deployments during `pulumi up`, providing real-time guardrails for developers and AI agents.
* **Audit policies**: Continuously scan existing resources for ongoing compliance monitoring, giving you a complete picture of your cloud security posture.

This dual approach ensures new deployments meet standards while maintaining visibility across your entire infrastructure. Learn more in our [Preventative vs. Audit Policies](/docs/insights/preventative-vs-audit-policies/) guide.

## How to Get Started

Getting started with the new policy management experience is straightforward:

1. **Browse Policy Packs:** Navigate to the Policies tab in your Pulumi Cloud console to discover pre-built policy packs like Pulumi Best Practices and HITRUST CSF. Learn more about [Policy as Code](/docs/insights/policy-as-code/) configuration and setup.
![Policy Packs Browser](policy-management-1.png)
1. **Choose Your Approach:** Decide whether you need preventative policies (to block non-compliant deployments during `pulumi up`) or audit policies (for continuous compliance monitoring across all cloud resources).
![Preventative Policy Overview](policy-management-3.png)
1. **Create Policy Groups:** Set up policy groups to bundle related policies and apply them to your stacks or cloud accounts.
![Policy Group Configuration](policy-management-4.png)
1. **Configure Enforcement:** Set enforcement levels (advisory, mandatory, or remediate) for each policy based on your requirements.

## Now Available To Team and Enterprise Customers

To ensure every organization can build with confidence, these policy management enhancements and the `pulumi-best-practices` policy packs are **now available to Team and Enterprise customers**. Checkout our [pricing](/pricing) page for more information.

## Conclusion

The enhanced Pulumi Policy experience is a major step forward in making governance accessible and scalable for the entire platform. By focusing on discoverability and a simplified workflow, we've delivered essential guardrails that apply consistently, whether a developer is using a self-service portal or an AI agent is remediating an issue.

This is how you escape the velocity trap: by building a governance foundation that turns safety and compliance into an accelerant for everyone. It ensures that no matter how fast your teams move, they are always moving safely and within your organization's standards

We'd love for you to try out the new experience in the Pulumi Cloud\! Don't hesitate to reach out on the [Pulumi Community Slack](https://slack.pulumi.com/) to share your thoughts.
