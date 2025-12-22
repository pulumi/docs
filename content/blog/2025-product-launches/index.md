---
title: "Pulumi 2025: Neo, Next-Gen Policies, and Platform Engineering at Scale"
allow_long_title: true
date: 2025-12-22
draft: false
meta_desc: "Pulumi 2025 launches: Neo AI agent for platform engineers, next-gen policy management, IDP, ESC integrations, and IaC enhancements."
meta_image: meta.png
authors:
    - arun-loganathan
tags:
    - features
    - product-launches
    - pulumi-cloud
---

The era of AI-accelerated development has arrived, creating both unprecedented opportunity and unprecedented challenge. Developers ship code faster than ever, but platform teams struggle to keep pace. The velocity gap threatens to become a bottleneck.

As 2025 comes to a close, let's look back at how we addressed this challenge.

This year, we took a giant leap forward to close that gap with several major innovations, including purpose-built AI for platform engineers, next-generation policy management that transforms governance into an accelerator, and the foundation for building Internal Developer Platforms that enable self-service without sacrificing control.

<!--more-->

- [Pulumi Neo: Your Newest Platform Engineer](#pulumi-neo-your-newest-platform-engineer)
  - [AI-Assisted Development Everywhere](#ai-assisted-development-everywhere)
- [Next-Generation Policy Management: AI-Powered Governance at Scale](#next-generation-policy-management-ai-powered-governance-at-scale)
- [Internal Developer Platform: Self-Service Infrastructure at Scale](#internal-developer-platform-self-service-infrastructure-at-scale)
- [Secrets Management: Taming Sprawl at Scale](#secrets-management-taming-sprawl-at-scale)
- [Identity and Access Management](#identity-and-access-management)
- [Pulumi IaC](#pulumi-iac)
  - [Cloud Provider Support](#cloud-provider-support)
  - [Language Support](#language-support)
  - [Infrastructure Operations](#infrastructure-operations)
  - [Kubernetes Operator](#kubernetes-operator)
- [The Year Ahead](#the-year-ahead)

## Pulumi Neo: Your Newest Platform Engineer

We launched [Pulumi Neo](/blog/pulumi-neo/), purpose-built AI specifically designed for platform engineering challenges. Neo fundamentally changed how platform engineers work.

{{< youtube "9GB9M2l1OgY?rel=0" >}}

The problem Neo solves is critical: while AI coding assistants have accelerated developers substantially, platform teams have struggled to keep pace. Every line of code that ships faster creates new platform needs - monitoring, secrets, pipelines, compliance checks. The velocity gap between development and platform teams was widening, threatening to become a bottleneck that would slow down entire organizations.

Neo levels the playing field by giving platform engineers their own dedicated AI tool. Unlike generic AI coding assistants that lack infrastructure context, Neo deeply understands cloud environments, infrastructure as code, secrets management, and the unique challenges platform teams face. It speaks their language and works within their constraints.

What makes Neo different is how it's built. Neo operates on top of Pulumi's existing platform capabilities - the same IaC, ESC, and policy features you already use for governance become Neo's operational guardrails. It automatically respects your security and policy rules, works within your governance frameworks, and maintains the audit trails and compliance controls your organization requires. This isn't experimental AI retrofitted with infrastructure plugins - it's enterprise-ready intelligence built from the ground up on proven foundations.

Throughout the year, we enhanced Neo with capabilities that scale your team's expertise. [Custom Instructions and Slash Commands](/blog/slash-commands-custom-instructions/) let you encode organizational standards once and Neo applies them automatically, while turning proven prompts into reusable shortcuts anyone can use. [Operating Modes](/blog/neo-levels-up/) give you flexible control - from full review to autonomous execution. And [full Pulumi CLI integration](/blog/neo-levels-up/) means Neo can handle complete infrastructure workflows, from stack operations to cloud CLI commands.

### AI-Assisted Development Everywhere

Beyond Neo, we brought AI assistance directly into development workflows throughout the year. The [Pulumi Model Context Protocol (MCP) Server](/blog/mcp-server-ai-assistants/) connects AI-powered code assistants with Pulumi's CLI and registry, enabling real-time resource information without leaving your editor. Use it with GitHub Copilot, Anthropic's Claude Code, and Cursor to accelerate resource discovery and write infrastructure code faster. We enhanced this with [remote MCP server](/blog/remote-mcp-server/) support for centralized management and [CLI AI extensions](/blog/cli-ai-extensions/) for intelligent command-line assistance.

## Next-Generation Policy Management: AI-Powered Governance at Scale

With Neo giving platform teams AI superpowers, we needed to ensure AI-accelerated development remained safe and compliant. The challenge isn't detecting security issues - it's fixing them at scale. Most policy tools stop at detection, leaving teams with overwhelming backlogs and no scalable way to remediate violations.

We ended that compromise with the [next generation of Pulumi Policies](/blog/policy-next-gen/). This comprehensive governance solution moves beyond detection to deliver AI-powered remediation through a two-step lifecycle:

{{< youtube "mwcrOTEf1EQ?rel=0" >}}

**Get Clean:** We introduced the [Policy Findings Hub](/blog/policy-issue-management/) that gives every stakeholder their needed view - leadership sees compliance scores, auditors get control-centric compliance views, and platform teams get a collaborative workspace to triage and track remediation. Combined with [audit scans](/blog/policy-audit-scans-for-stacks/), you get instant compliance baselines without blocking developers. Neo integrates directly into the Policy Findings hub to automate the fix itself, generating pull requests with exact code changes needed. For unmanaged resources, Neo even generates code to import the resource into a Pulumi stack and apply the fix.

**Stay Clean:** We launched [pre-built compliance packs](/blog/policy-packs-cis-nist-pci/) for **CIS, NIST, PCI, and HITRUST** across AWS, Azure, and Google Cloud. These out-of-the-box policy packs let you enforce industry-standard compliance frameworks immediately without writing custom policies. They act as universal guardrails by blocking non-compliant changes during deployment. Neo can even author new custom policies - ask Neo to "create a policy that prevents overly permissive IAM roles," and it generates the code. This is how we make AI safe to go fast.

## Internal Developer Platform: Self-Service Infrastructure at Scale

{{< youtube "3gZmKaAeppc?rel=0" >}}

Platform engineering teams face a persistent challenge: they're constantly responding to infrastructure requests instead of building the systems that enable self-service at scale. This reactive cycle prevents platform teams from doing their most valuable work - establishing patterns, codifying standards, and creating golden paths that empower developers without sacrificing control.

We delivered the foundation to break this cycle with [Pulumi IDP](/blog/announcing-pulumi-idp/). Pulumi IDP provides everything platform teams need to build world-class internal developer platforms. Codify organizational standards into reusable building blocks. Give developers simple, approachable interfaces that enforce best practices automatically. Transform platform engineering from reactive ticket-taking to strategic enablement.

The key is [Pulumi Private Registry](/blog/announcing-pulumi-private-registry/), your organization's source of truth for golden paths and platform building blocks. Private Registry provides streamlined publishing workflows and simplified discovery, making it easy to share infrastructure abstractions across your organization. Combined with our expanded [public registry](/blog/registry-wave-2/) (now over 150 providers and 7,500 resource types), you have comprehensive options for managing infrastructure across your entire cloud estate.

What makes this powerful is [next-generation Pulumi Components](/blog/pulumi-components/) with true cross-language support. Author infrastructure abstractions once in your preferred language, then consume them in any supported Pulumi language - including YAML for non-programmers, and soon, [HCL](/blog/all-iac-including-terraform-and-hcl/). Components include built-in input validation, detailed documentation, and improved error messages. This means platform teams can reach every developer in their organization regardless of language preference, scaling their expertise without scaling their team.

## Secrets Management: Taming Sprawl at Scale

The proliferation of secrets across modern cloud environments creates massive security risks. Long-lived credentials pose significant vulnerabilities. Secrets scattered across systems make it nearly impossible to track usage or enforce consistent policies. And manual rotation processes are error-prone and rarely done.

2025 saw significant expansion of Pulumi ESC to address these challenges across your entire secrets ecosystem:

**Automated Rotation:** We launched [ESC Rotated Secrets](/blog/esc-rotated-secrets-launch/), automatically rotating credentials like AWS IAM access keys on flexible schedules. This eliminates manual rotation effort and significantly reduces vulnerability windows. We expanded this with [database credential rotation](/blog/esc-db-secrets-rotation-launch/) for PostgreSQL and MySQL, including support for databases in private VPCs via AWS VPC Lambda connectors.

**Universal Integration:** We integrated ESC with the secrets management platforms you're already using:

- [Snowflake](/blog/esc-snowflake-providers-launch/) - Dynamic OIDC tokens for temporary authentication plus automated RSA keypair rotation
- [Infisical](/blog/esc-infisical-providers-launch/) - Dynamic OIDC login and secret fetching from the open-source secrets platform
- [Doppler](/blog/esc-doppler-providers-launch/) - OIDC access tokens and centralized secret fetching

For systems without native support, we launched [ESC Connect](/blog/esc-connect/), enabling you to build simple HTTPS adapters that integrate any custom or proprietary secret source with ESC.

These integrations let you maintain existing secrets infrastructure while gaining ESC's centralized management, audit capabilities, and governance controls. You don't have to rip and replace - ESC works with what you have.

**Better Experience:** We improved ESC usability throughout the year with [streamlined onboarding](/blog/esc-new-onboarding/), [approval workflows](/blog/esc-open-approvals/) for sensitive environments, and [deletion protection](/blog/esc-deletion-protection/) to prevent accidents.

**Security & Trust:** For organizations with strict compliance needs like HIPAA or GDPR, we launched [Customer-Managed Keys (BYOK)](/blog/bring-your-own-keys-with-pulumi-esc/). This allows you to bring your own encryption keys (via AWS KMS) to encrypt secrets stored in ESC, giving you full control over key lifecycles and revocation.

## Identity and Access Management

Modern security demands unwavering trust in your security posture. How do you empower teams to deploy rapidly without opening doors to risk or violating compliance mandates?

We launched [Pulumi IAM](/blog/pulumi-cloud-iam-launch/), embedding robust, granular security directly into your cloud development lifecycle. Pulumi IAM provides the unified framework for fine-grained authorization needed to confidently manage modern cloud infrastructure:

- **Custom Roles**: Define reusable permissions with fine-grained scopes tailored to your organization's specific needs
- **Least Privilege Enforcement**: Control precisely who can do what on which specific resources, minimizing the impact if credentials are compromised
- **Secure Automation**: Generate scoped access tokens for CI/CD pipelines with only the necessary permissions, eliminating over-privileged service accounts
- **Zero Trust Foundation**: Verify every access request and grant minimum necessary access, implementing true Zero Trust principles

This foundational capability enables true least-privilege for CI/CD pipelines, reduces blast radius if tokens are compromised, and provides the compliance evidence auditors require. Platform and security teams finally have the fine-grained control needed to scale Pulumi usage securely across enterprise organizations without sacrificing velocity.

## Pulumi IaC

Platform teams need IaC tools that keep pace with rapidly evolving cloud platforms while providing operational flexibility and reliability. This year we shipped hundreds of enhancements to Pulumi's core IaC capabilities, from major cloud provider updates to new operational primitives that give teams more control over infrastructure lifecycles.

### Cloud Provider Support

Managing multi-cloud infrastructure requires comprehensive provider support that keeps pace with rapidly evolving cloud platforms. This year we shipped major provider updates:

**[AWS Provider 7.0](/blog/announcing-7-0-of-the-pulumi-aws-provider/)** brought game-changing improvements: manage resources across multiple AWS regions with a single provider instance, enhanced IAM role chaining with better error handling, and simplified S3 resource management.

**[Azure Native V3](/blog/azure-native-v3/)** delivered a 75% reduction in SDK size while maintaining 100% Azure ARM API coverage. Faster downloads, more manageable package sizes, and improved reliability.

**[Google Cloud Provider 9.0](/blog/gcp-v9-release/)** brought updated API versions, new modules for AI and Google Gemini, and expanded resource support for the latest GCP services.

**[Direct Terraform Module Support](/blog/announcing-direct-tf-modules/)** was one of our most requested features. Execute Terraform modules directly in Pulumi without conversion, providing a seamless migration path for module-heavy projects.

### Language Support

**[Java SDK 1.0 GA](/blog/java-1-0/)** provides first-class Java support with feature parity to other Pulumi languages, support for all current LTS Java versions, and complete Automation API support.

### Infrastructure Operations

**[Resource Hooks](/blog/resource-hooks/)** was one of our most requested features. Run custom code at any point in a resource's lifecycle - before creation, after updates, before deletion. This unlocks scenarios like validation checks before deployment, triggering external systems when infrastructure changes, and custom logging and auditing.

We also shipped [dependent resource replacements](/blog/dependent-resource-replacements/), [excluding specific targets from stack operations](/blog/excluding-targets-from-stack-operations/), [state taint capabilities](/blog/pulumi-state-taint/), [improved refresh and destroy experience](/blog/improved-refresh-destroy-experience/) for short-lived credentials, and [CLI control through environment variables](/blog/controlling-the-cli-through-environment-variables/).

### Kubernetes Operator

The [Pulumi Kubernetes Operator 2.0 reached GA](/blog/pko-2-0-ga/) with a completely rewritten, faster codebase featuring enhanced reconciliation logic, better error handling, and automatic retry for temporary failures. We continued enhancing it with [version 2.3.0](/blog/pulumi-kubernetes-operator-2-3/) adding preview mode for validating infrastructure changes and structured configuration support for GitOps workflows.

## The Year Ahead

2025 was the year we gave platform engineers the tools to thrive in the age of AI-accelerated development. We ended the impossible choice between velocity and control. We transformed governance from a blocker into an accelerator. We enabled self-service without sacrificing governance.

But this is just the beginning. The foundation we built this year sets the stage for even bigger innovations ahead. Neo will get smarter as it learns from infrastructure patterns across the community. Policy management will expand to more compliance frameworks. IDP will enable more sophisticated self-service workflows. ESC will integrate with more platforms.

The future of platform engineering is strategic, proactive, and AI-enabled. Platform teams won't be bottlenecks - they'll be the strategic enablers who make sustainable velocity possible.

Thank you for being part of the Pulumi community. Your feedback drives everything we build. We can't wait to show you what comes next.

Want to try these features? Check out our [documentation](/docs/), join our [community Slack](https://slack.pulumi.com/), or [contact us](/contact/) to discuss how Pulumi can transform your platform engineering practice.

Here's to an incredible 2025, and an even better 2026!
