---
title: "Pulumi Release Notes: Pulumi MCP Server, Pulumi ESC Rotated Secrets, and Policy Enhancements"
allow_long_title: true
date: 2025-04-25
draft: false
meta_desc: "Explore Pulumi's latest features including AI-assisted development with MCP Server, cross-language Components, ESC Rotated Secrets, and much more!"
meta_image: meta.png
authors:
    - arun-loganathan
    - meagan-cojocar 
tags:
    - features
    - release-notes
social:
    twitter: "Pulumi Releases Notes: AI-assisted IaC with our MCP Server, new cross-language components, registry expansion, ESC Rotated Secrets, and more! Check out all the new features we've shipped in the last two months!."
    linkedin: "Pulumi Release Notes are out! Take a look at the improvements we have shipped in the last two months across the Pulumi ecosystem! From AI-assisted IaC with our MCP Server to new cross-language components to powerful new capabilities in Pulumi ESC and Insights, these updates deliver on our commitment to making cloud management more powerful, accessible, and secure. Check out our latest release notes to see what's new!"
---

We've been busy over the past two months, shipping significant enhancements across the Pulumi ecosystem. From major improvements to our core IaC platform with Azure Native V3 and cross-language Components to powerful new capabilities in Pulumi ESC and Insights, these updates deliver on our commitment to making cloud management more powerful, accessible, and secure. We're particularly excited about our AI integration through the MCP Server, enabling developers to work with infrastructure in a more intuitive, contextual way. Let's dive into the details of what's new.

<!--more-->

- [Pulumi IaC](#pulumi-iac)
  - [Azure Native V3](#azure-native-v3)
  - [Pulumi Model Context Protocol (MCP) Server](#pulumi-model-context-protocol-mcp-server)
  - [Next-Generation Pulumi Components](#next-generation-pulumi-components)
  - [Registry Wave 2: 27 New Providers](#registry-wave-2-27-new-providers)
  - [Enhanced Terraform Conversion](#enhanced-terraform-conversion)
  - [Improved Refresh and Destroy Experience](#improved-refresh-and-destroy-experience)
  - [GitLab Integration Improvements](#gitlab-integration-improvements)
  - [Faster Secrets Management](#faster-secrets-management)
  - [Pulumi Kubernetes Operator 2.0](#pulumi-kubernetes-operator-20)
  - [Java SDK 1.0](#java-sdk-10)
  - [Pulumi Copilot in VSCode](#pulumi-copilot-in-vscode)
  - [Autonaming Configuration](#autonaming-configuration)
- [Pulumi ESC](#pulumi-esc)
  - [Rotated Secrets](#rotated-secrets)
  - [Pulumi ESC GitHub Action](#pulumi-esc-github-action)
- [Pulumi Insights](#pulumi-insights)
  - [Enforce Policy as Code on Discovered Resources](#enforce-policy-as-code-on-discovered-resources)
- [Wrap up](#wrap-up)

## Pulumi IaC

### Azure Native V3

We're excited to announce the release of Pulumi Azure Native V3, delivering a remarkable 75% reduction in SDK size while maintaining complete coverage of the Azure ecosystem. The new SDK provides faster downloads, more manageable package sizes, and more reliable performance while maintaining access to all Azure resource properties. With a modern API surface, consistent input/output schemas, and simplified version management, it's now easier than ever to build and deploy Azure resources with Pulumi. [Read the blog post](/blog/azure-native-v3/) or check out the [Azure Native Provider documentation](/registry/packages/azure-native/).

### Pulumi Model Context Protocol (MCP) Server

The new Pulumi Model Context Protocol (MCP) Server integration brings AI-assisted infrastructure development directly into your coding workflow. By connecting AI-powered code assistants with Pulumi's CLI and registry, MCP enables real-time resource information and infrastructure management without leaving your editor. This integration drastically reduces context switching, accelerates resource discovery, and enables faster coding with intelligent assistance. Use it with tools like GitHub Copilot, Anthropic's Claude Code, Cursor, and others to streamline your infrastructure development experience. [Learn more about AI-assisted IaC](/blog/mcp-server-ai-assistants/).

### Next-Generation Pulumi Components

Introducing the next generation of Pulumi Components with enhanced cross-language capabilities, enabling you to create reusable infrastructure abstractions once and deploy them using any supported Pulumi language. These improved components allow platform teams to codify organizational standards into shareable libraries while giving developers simpler, more approachable interfaces that enforce best practices automatically. With built-in input validation, detailed documentation, improved error messages, and cross-language support, your components can now reach a wider audience of developers regardless of their preferred programming language. [Read the blog post](/blog/pulumi-components/) or explore the [Components documentation](/docs/iac/concepts/resources/components/).

### Registry Wave 2: 27 New Providers

We've expanded the Pulumi Registry with 27 new native providers, bringing the total to over 150 providers and 7,500 resource types. This wave adds support for popular services like Jira, Gitlab, Railway, Neon, PlanetScale, and many more, giving you more options for managing your entire cloud infrastructure with Pulumi. Each provider is published as a standalone package, making it easier to adopt new providers without updating your entire Pulumi installation. Start using these providers today to expand your infrastructure management capabilities. [Read the blog post](/blog/registry-wave-2/) or browse the [Pulumi Registry](/registry/).

### Enhanced Terraform Conversion

With Pulumi CLI version 3.153.0 and above, we've supercharged our Terraform conversion capabilities. Now you can automatically convert **ANY** Terraform project to Pulumi and import its resources - even if it uses providers that don't have native Pulumi equivalents. This breakthrough eliminates a significant migration barrier, allowing teams to convert their entire Terraform codebase without provider limitations. The enhanced converter handles mixed provider scenarios effortlessly, maintaining access to specialized Terraform providers you already leverage while modernizing your infrastructure deployment. This builds on our existing capability to use [any Terraform/OpenTofu provider](/blog/any-terraform-provider/) in your Pulumi projects, making it easier than ever to migrate your infrastructure as code to Pulumi. [Read the blog post](/blog/pulumi-convert-terraform-improvements/) to see examples and learn how to try it for yourself.

### Improved Refresh and Destroy Experience

As of Pulumi CLI version 3.160.0, we've introduced a significant enhancement to the `pulumi refresh` and `pulumi destroy` commands. These commands now support the `--run-program` flag, which enables them to run your program code before refreshing or destroying your stack. This is especially valuable for teams working with short-lived credentials, dynamic resources, or any workflow where your code needs to run to establish the right context. Previously, while these commands took into account updated configuration from your `Pulumi.<stack>.yaml` files, they didn't consider changes in your actual code, which could break workflows that depend on code to update credentials or determine resources to manage. This improvement ensures your infrastructure operations have the full context they need to succeed, particularly important when using OIDC-based authentication, dynamically fetching credentials from a secrets manager, or working with dynamic providers. We plan to make this the default behavior eventually, but are introducing it as an opt-in flag first to ensure a smooth transition. [Read more in our RFC](https://github.com/pulumi/pulumi/discussions/19102) on making program execution the default behavior.

### GitLab Integration Improvements

We've significantly enhanced our GitLab integration with support for multiple pipeline jobs and simplified authentication. The improved integration works with both GitLab CI/CD server and SaaS offerings, supporting parallel execution of multiple Pulumi steps within a single GitLab pipeline. Authentication has been streamlined with a new method that eliminates the need for personal access tokens, instead leveraging GitLab's CI/CD variables for secure, seamless authentication. These enhancements make it easier than ever to implement GitOps workflows with Pulumi and GitLab. [Read the blog post](/blog/gitlab-better-than-ever/) or check out the [documentation](/docs/using-pulumi/continuous-delivery/gitlab-app/).

### Faster Secrets Management

We've optimized secrets performance in Pulumi, resulting in significantly faster operations when working with large numbers of secrets. Through focused engineering efforts, we've achieved up to 75% reduction in secrets processing time for large stacks, with the most dramatic improvements seen in stacks with many outputs. This enhancement particularly benefits workflows involving many secrets, resource outputs, or stack references. The improvements are available starting with Pulumi 3.123.0 and require no changes to your existing code. [Read the blog post](/blog/faster-secrets-management/) to learn more about these performance improvements.

### Pulumi Kubernetes Operator 2.0

The Pulumi Kubernetes Operator 2.0 is now generally available, bringing advanced automation capabilities for managing Pulumi stacks within Kubernetes clusters. The new version includes a completely rewritten, faster codebase with enhanced reconciliation logic, better error handling, and improved CRD management. Version 2.0 also adds critical features like automatic retry for temporary failures, fine-grained refresh control, idempotent updates, and advanced stack management capabilities. These improvements make the operator more reliable and powerful for managing infrastructure directly from your Kubernetes clusters. [Read the blog post](/blog/pko-2-0-ga/) or check out the [operator documentation](/docs/kubernetes/pulumi-kubernetes-operator/).

### Java SDK 1.0

The Pulumi Java SDK is now generally available with its 1.0 release, providing first-class support for Java in Pulumi's multi-language ecosystem. The GA release includes feature parity with other Pulumi languages, improved documentation, enhanced type safety, and support for the complete Pulumi programming model. We've also expanded the Java SDK to support all current LTS versions and ensure smooth interoperability with the broader Java ecosystem. This milestone makes Pulumi an excellent choice for Java teams looking to manage their infrastructure using their preferred language. [Read the blog post](/blog/java-1-0/) or check out the [Java getting started guide](/docs/languages/java/).

### Pulumi Copilot in VSCode

Pulumi Copilot is now available in Visual Studio Code, bringing AI-powered assistance directly to your infrastructure development environment. The VSCode extension helps you write, understand, and debug Pulumi code with inline explanations, transformation suggestions, and code generation capabilities. Copilot can also assist with converting between Pulumi languages and translating from other IaC tools like Terraform and CloudFormation. This integration makes it easier to learn Pulumi, accelerate your infrastructure development, and solve complex configuration challenges. [Read the blog post](/blog/copilot-in-vscode/) or [install the extension](https://marketplace.visualstudio.com/items?itemName=pulumi.pulumi-vscode-copilot) today.

### Autonaming Configuration

We've enhanced Pulumi's autonaming feature with new configuration options that give you more control over resource naming. You can now globally disable autonaming or configure it on a per-component basis, allowing you to precisely control when Pulumi generates names for your resources. This is particularly valuable for organizations that want to ensure consistent, predictable resource naming across their infrastructure. The new configuration is available in Pulumi CLI version 3.91.1 and later, and requires no code changes to implement. [Read the blog post](/blog/autonaming-configuration/) or check out the [documentation](/docs/iac/concepts/resources/names/) for implementation details.

## Pulumi ESC

### Rotated Secrets

Address the persistent challenge of static, long-lived credentials with the new Rotated Secrets capability in Pulumi ESC. Static secrets pose significant security risks due to potential exposure and infrequent, error-prone manual rotation. While [dynamic secrets](/docs/esc/integrations/dynamic-login-credentials/) are ideal, Rotated Secrets provide a powerful alternative for applications requiring long-lived credentials, systems needing persistent connections, or where dynamic credentials aren't feasible. Automatically rotate credentials like AWS IAM user access keys (with more integrations coming soon) on flexible schedules or on-demand, eliminating manual effort and reducing the window of vulnerability. Rotated Secrets seamlessly integrate into ESC environments, utilize a "two-secret" strategy for smooth transitions, offer robust auditing, and allow for separation of administrative and consumer roles. Configure rotations directly within your ESC definitions and set up webhooks to automate downstream updates. [Read the blog post](/blog/announcing-pulumi-esc-github-action/).

### Pulumi ESC GitHub Action

Securely inject secrets and configuration directly into your GitHub Actions workflows with the new [Pulumi ESC GitHub Action](https://github.com/marketplace/actions/esc-action). This action lets you dynamically inject values from your Pulumi ESC environments as needed during CI/CD runs, eliminating the need to store static, long-lived credentials within GitHub and reducing secret sprawl. Leverage Pulumi ESC's automatic secret rotation capabilities and run ESC commands directly within your workflows for streamlined environment management. Combine this action with [pulumi/auth-actions](https://github.com/marketplace/actions/pulumi-auth-action) for seamless, tokenless authentication to Pulumi Cloud using OIDC, further enhancing security. [Read the blog post](/blog/announcing-pulumi-esc-github-action/).


## Pulumi Insights

### Enforce Policy as Code on Discovered Resources

Extend the governance reach of Pulumi [Policy as Code](/docs/iac/using-pulumi/crossguard/) beyond IaC-managed resources to encompass your entire cloud environment with a powerful new capability in [Pulumi Insights](/docs/insights/). You can now automatically apply your existing policies to resources discovered by Pulumi Insights, regardless of how they were created. Simply link your [Insights Accounts](/docs/insights/accounts/) (representing cloud provider integrations) to your Policy Groups alongside your stacks. Pulumi will then evaluate all resources within those accounts against your defined policies, surfacing violations centrally. This allows you to write policies once and apply them universally across both IaC and discovered resources, dramatically simplifying how you maintain consistent security and compliance standards at scale across AWS, Azure, OCI, and Kubernetes. [Read the blog post](/blog/enforcing-policy-as-code-on-discovered-resources-with-pulumi/). 

## Wrap up

These new features and enhancements represent our ongoing commitment to improving the cloud management experience for developers and platform teams. Whether you're managing cloud resources with our streamlined Azure Native V3 provider, creating reusable abstractions with cross-language Components, leveraging AI assistance with the MCP Server, or strengthening your security posture with ESC Rotated Secrets and policy enforcement, we're focused on making your infrastructure management more efficient, secure, and enjoyable. As we continue to innovate, your feedback helps shape our roadmap and prioritize improvements that matter most to you.

Explore all the new capabilities and share your feedback – we're always listening! Open an issue in the [Pulumi Cloud requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) or the [pulumi/pulumi repository](https://github.com/pulumi/pulumi) for anything CLI-related. Stay tuned for more exciting updates!
