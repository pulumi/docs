---
title: "Pulumi IAM Now Available for Self-Hosted Pulumi Cloud"
allow_long_title: true
date: 2026-01-14T11:18:00Z
draft: false
meta_desc: "Pulumi IAM with Custom Roles and scoped Access Tokens is now available for self-hosted Pulumi Cloud instances."
meta_image: meta.png
authors:
  - davide-massarenti
  - devon-grove
  - casey-huang
  - arun-loganathan
tags:
  - iam
  - rbac
  - security
  - features
  - pulumi-cloud
  - access-tokens
  - self-hosted
---

We're excited to announce that **Pulumi Identity and Access Management (IAM)** is now available for self-hosted instances of Pulumi Cloud. This foundational security capability brings the same [enterprise-grade access management](/blog/pulumi-cloud-iam-launch/) we launched for Pulumi Cloud SaaS to organizations running Pulumi on their own infrastructure.

<!--more-->

## Enterprise Security for Self-Hosted Deployments

Self-hosted Pulumi Cloud customers can now leverage the full power of **Custom Roles** and **Granular Access Tokens** to implement Zero Trust security principles and least privilege access controls within their own environments. This means you can:

* **Define Custom Permissions** with fine-grained scopes (e.g., `stack:delete`, `environment:read`) tailored to your organization's security requirements.
* **Create Custom Roles** by combining these permissions with specific Pulumi entities (Stacks, Environments, etc.).
* **Generate Scoped Organization Access Tokens** that are precisely limited to the permissions defined in their associated roles, dramatically reducing the blast radius if credentials are compromised.

## Secure Automation for On-Premises Infrastructure

This release is powerful for self-hosted Pulumi Cloud deployments where security and compliance requirements are often even more stringent. You can now:

* **Implement Least Privilege CI/CD:** Scope pipeline tokens to only the actions and resources they absolutely need, ensuring your automation follows the same security standards as your infrastructure.
* **Enhance Compliance Posture:** Demonstrate precise, auditable control over programmatic access to auditors and security teams.
* **Reduce Operational Risk:** Limit the potential impact of compromised tokens by restricting them to specific roles and permissions.

## Getting Started

Self-hosted customers can access IAM features through the same intuitive interface available in Pulumi Cloud SaaS. Navigate to **Settings** -> **Access Management** -> **Roles** to begin creating Custom Permissions and Custom Roles, then generate scoped Organization Access Tokens from **Settings** -> **Access Management** -> **Access Tokens**.

For detailed information about Pulumi IAM capabilities, including step-by-step guides and best practices, see our [comprehensive announcement blog post](/blog/pulumi-cloud-iam-launch/).

## Learn More

Explore the IAM & RBAC documentation to get started:

* [Overview](/docs/pulumi-cloud/access-management/rbac)
* [Roles](/docs/pulumi-cloud/access-management/rbac/roles)
* [Permissions](/docs/pulumi-cloud/access-management/rbac/permissions)
* [Scopes](/docs/pulumi-cloud/access-management/rbac/scopes)

We're committed to bringing enterprise-grade security features to all Pulumi deployments, whether in the cloud or on-premises. If you have questions or feedback, please reach out through your account representative or our [GitHub repository](https://github.com/pulumi/pulumi-cloud-requests/issues).
