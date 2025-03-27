---
title: "Pulumi Release Notes: Pulumi ESC Rotated Secrets, Policy Enhancements"
allow_long_title: true
date: 2025-03-28T11:06:04-08:00
draft: false
meta_desc: to-be-aded
meta_image: meta.png
authors:
    - arun-loganathan
    - meagan-cojocar 
tags:
    - features
    - release-notes
---

<b>Intro to be added</b>

<!--more-->

- [Pulumi IaC Cloud](#pulumi-iac-cloud)
- [Pulumi ESC](#pulumi-esc)
  - [Rotated Secrets](#rotated-secrets)
  - [Pulumi ESC GitHub Action](#pulumi-esc-github-action)
- [Pulumi Insights](#pulumi-insights)
  - [Enforce Policy as Code on Discovered Resources](#enforce-policy-as-code-on-discovered-resources)
- [Wrap up](#wrap-up)

## Pulumi IaC Cloud


## Pulumi ESC

### Rotated Secrets

Address the persistent challenge of static, long-lived credentials with the new Rotated Secrets capability in Pulumi ESC. Static secrets pose significant security risks due to potential exposure and infrequent, error-prone manual rotation. While [dynamic secrets](/docs/esc/integrations/dynamic-login-credentials/) are ideal, Rotated Secrets provide a powerful alternative for applications requiring long-lived credentials, systems needing persistent connections, or where dynamic credentials aren't feasible. Automatically rotate credentials like AWS IAM user access keys (with more integrations coming soon) on flexible schedules or on-demand, eliminating manual effort and reducing the window of vulnerability. Rotated Secrets seamlessly integrate into ESC environments, utilize a "two-secret" strategy for smooth transitions, offer robust auditing, and allow for separation of administrative and consumer roles. Configure rotations directly within your ESC definitions and set up webhooks to automate downstream updates. [Read the blog post](/blog/announcing-pulumi-esc-github-action/).

### Pulumi ESC GitHub Action

Securely inject secrets and configuration directly into your GitHub Actions workflows with the new [Pulumi ESC GitHub Action](https://github.com/marketplace/actions/esc-action). This action lets you dynamically inject values from your Pulumi ESC environments as needed during CI/CD runs, eliminating the need to store static, long-lived credentials within GitHub and reducing secret sprawl. Leverage Pulumi ESC's automatic secret rotation capabilities and run ESC commands directly within your workflows for streamlined environment management. Combine this action with [pulumi/auth-actions](https://github.com/marketplace/actions/pulumi-auth-action) for seamless, tokenless authentication to Pulumi Cloud using OIDC, further enhancing security. [Read the blog post](/blog/announcing-pulumi-esc-github-action/).


## Pulumi Insights

### Enforce Policy as Code on Discovered Resources

Extend the governance reach of Pulumi [Policy as Code](/docs/iac/using-pulumi/crossguard/) beyond IaC-managed resources to encompass your entire cloud environment with a powerful new capability in [Pulumi Insights](/docs/insights/). You can now automatically apply your existing policies to resources discovered by Pulumi Insights, regardless of how they were created. Simply link your [Insights Accounts](/docs/insights/accounts/) (representing cloud provider integrations) to your Policy Groups alongside your stacks. Pulumi will then evaluate all resources within those accounts against your defined policies, surfacing violations centrally. This allows you to write policies once and apply them universally across both IaC and discovered resources, dramatically simplifying how you maintain consistent security and compliance standards at scale across AWS, Azure, OCI, and Kubernetes. [Read the blog post](/blog/enforcing-policy-as-code-on-discovered-resources-with-pulumi/). 



## Wrap up

<b>Add a conclusion</b>

Explore all the new capabilities and share your feedback – we're always listening! Open an issue in the [Pulumi Cloud requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) or the [pulumi/pulumi repository](https://github.com/pulumi/pulumi) for anything CLI-related. Stay tuned for more exciting updates!
