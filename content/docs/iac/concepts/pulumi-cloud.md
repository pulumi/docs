---
title_tag: Pulumi Cloud and Open Source Pulumi
meta_desc: Learn how Pulumi Cloud relates to the open source Pulumi infrastructure as code tool.
title: Pulumi Cloud and Open Source Pulumi
h1: Pulumi Cloud and Open Source Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi Cloud
        parent: iac-concepts
        weight: 15
    concepts:
        weight: 2
aliases:
  - /docs/deployments/get-started/what-is-it/
  - /docs/pulumi-cloud/get-started/what-is-it/
---

Pulumi infrastructure as code is open source. Pulumi Cloud is a managed service that provides state management, team collaboration, and cloud governance features. This page explains how they relate and helps you understand what Pulumi Cloud offers beyond the open source tool.

## Introduction

Pulumi Cloud is a managed service that helps teams adopt collaborative, secure, and robust cloud engineering practices. This includes infrastructure as code, secrets management, and continuous enforcement of cloud policies. Pulumi's [open source](https://github.com/pulumi) infrastructure as code tool is how many community members initially learn about Pulumi. The two are related in that Pulumi IaC uses Pulumi Cloud by default to make adopting IaC in your team easier, secure, and reliable automatically.

Pulumi IaC can also be used with a self-managed backend if you prefer, which comes with some tradeoffs outlined below.

{{% notes "info" %}}
An analogy to other software you may be familiar with is that, just like Git is fully open source and you can host, secure, and manage repositories yourself, so too can you with hosting your Pulumi infrastructure as code projects and stacks. However, especially in a team setting, using Git in conjunction with GitHub provides built-in security, reliability, and collaboration features like Pull Requests. A similar dynamic exists with Pulumi and Pulumi Cloud.
{{% /notes %}}

{{% notes "info" %}}
For technical details on how Pulumi manages state and how to configure different backends, see [State and Backends](/docs/iac/concepts/state-and-backends/).
{{% /notes %}}

Pulumi Cloud is a platform of three products: [Pulumi IaC](/product/infrastructure-as-code), the companion to Pulumi open source IaC; [Pulumi ESC](/product/secrets-management), a secrets and configuration solution; and [Pulumi Insights](/product/pulumi-insights), an intelligent cloud inventory, compliance, and management product. Pulumi Cloud is offered as a service (SaaS) as well as a self-hosted edition that you can run anywhere. It features a client/server architecture to increase your confidence in using the SaaS.

## Key capabilities

Pulumi Cloud provides several capabilities beyond what is available in the open source Pulumi IaC tool:

### State management and collaboration

Pulumi Cloud provides centralized state management with automatic locking and transactional checkpointing for fault tolerance. [Projects, stacks, and resources](/docs/deployments/projects-and-stacks/) are organized and searchable, with complete deployment history including resource diffs and links to source changes and cloud resources.

[Audit logs](/docs/administration/security-compliance/audit-logs/) capture all actions taken by team members. Deployment logs are maintained for debugging, particularly useful for automated deployments via the [Pulumi Automation API](/automation) and [Pulumi Kubernetes Operator](/docs/iac/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/).

Team management integrates with [SAML/SSO providers](/docs/administration/access-identity/saml/) for automated onboarding, offboarding, and role assignment. Pulumi Cloud integrates with [over a dozen CI/CD systems](/docs/iac/using-pulumi/continuous-delivery/) including GitHub Actions, GitLab Pipelines, and Jenkins, plus [a built-in deployment service](/docs/deployments/deployments/) for Git-based workflows. The Pulumi GitHub App provides deployment previews directly in pull request comments.

[Pulumi ESC](/product/secrets-management/) allows you to group configuration and secrets into composable, versioned environments for sharing across projects and stacks. [Review Stacks](/docs/deployments/deployments/review-stacks/) provide ephemeral environments for pull request validation, while [TTL Stacks](/docs/deployments/deployments/ttl/) automatically clean up temporary infrastructure.

[Pulumi Neo](/docs/ai/), an AI agent integrated with Pulumi Cloud, assists with debugging failures, writing infrastructure code, and answering questions about your infrastructure.

### Security and access control

Pulumi Cloud provides [identity and access management](/docs/pulumi-cloud/access-management/) that integrates with Azure Active Directory, Google Workspace, Okta, and other SAML/SSO providers. [Role-based access control (RBAC)](/docs/administration/organizations-teams/teams/) integrates with projects and stacks, and you can [generate access tokens](/docs/administration/access-identity/access-tokens/) with fine-grained permissions for automation.

State files are encrypted at rest and in transit. Pulumi's [secrets model](/docs/iac/concepts/secrets/) ensures sensitive information is encrypted in state files. With Pulumi Cloud, each organization and stack is encrypted securely by default, with managed encryption keys.

### Governance and extensibility

Pulumi Cloud enables organization-wide policies using [Pulumi CrossGuard](/crossguard/) for security, compliance, and cost enforcement. Policies can block violations at deployment time or find and remediate existing violations through Pulumi Insights, with support for auto-remediation.

[Private templates](/docs/idp/developer-portals/templates/) and [an Internal Developer Platform experience](/docs/idp/developer-portals/new-project-wizard/) allow you to define approved infrastructure patterns for your organization. [Drift detection](/docs/deployments/deployments/drift/) identifies manual changes made outside of infrastructure as code, with automatic remediation capabilities.

All Pulumi Cloud functionality is accessible through [a REST API](/docs/reference/cloud-rest-api/cloud-rest-api/) for custom integrations. [Webhooks](/docs/deployments/webhooks/) enable event-driven workflows for deployments, policy violations, and other events. Pulumi Cloud undergoes annual SOC 2 Type II audits and implements compliance best practices.

## Next steps

Pulumi Cloud is the easiest way to adopt Pulumi's open source IaC tool at scale, securely, reliably, and collaboratively.

That said, DIY backends are fully supported, and this article aims to help you make an informed decision about which option best suits your use case. The [state and backends topic](/docs/iac/concepts/state-and-backends/) describes in-depth how Pulumi IaC uses Pulumi Cloud and DIY backends and other architectural considerations.

A complete list of Pulumi Cloud's features and capabilities is available [on the pricing page](/pricing#compare). For more details about adopting Pulumi Cloud in your team, [see the onboarding guide](/docs/deployments/get-started/onboarding-guide). This guide also includes best practices to help you completely adopt the full platform.

To get started today, [sign up for a free Pulumi Cloud account](https://app.pulumi.com/signup). Pulumi Cloud is free for individuals and small teams, and has advanced capabilities for larger teams and enterprises.
