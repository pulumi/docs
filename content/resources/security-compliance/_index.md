---
title: "Security & Compliance"
meta_desc: "Guides, comparisons, and evaluations for infrastructure security, policy as code, secrets management, and compliance automation with Pulumi."
meta_image: /images/docs/meta-images/docs-meta.png
type: resources
tagline: "Enforce security policies and meet compliance requirements without slowing engineering"
last_reviewed: 2026-03-11
related_capabilities:
  - policy-as-code
  - secrets-management
  - drift-detection
  - compliance
related_areas:
  - infrastructure-unification
  - ai-ready-infrastructure
cta:
  text: "Explore Pulumi ESC"
  url: "/product/esc/"
faq:
  - question: "How does policy as code work for infrastructure?"
    answer: "Policy as code lets teams define security, compliance, and cost rules as code that runs automatically during infrastructure deployments. Instead of relying on manual reviews or post-deployment audits, policies are evaluated before resources are created or modified. Pulumi CrossGuard supports writing policies in Python, TypeScript, Go, or OPA Rego, enforcing them across all deployments."
  - question: "What is infrastructure drift and how do you detect it?"
    answer: "Infrastructure drift occurs when the actual state of deployed resources diverges from what is defined in code, often due to manual changes, emergency fixes, or out-of-band modifications. Drift detection tools compare the desired state in your IaC definitions against the live state in your cloud provider, flagging discrepancies that could introduce security vulnerabilities or compliance violations."
  - question: "How does Pulumi help with secrets management?"
    answer: "Pulumi ESC (Environments, Secrets, and Configuration) provides centralized secrets management with dynamic credential generation, composable environments, and automatic rotation. It integrates with existing secrets stores like AWS Secrets Manager, HashiCorp Vault, and Azure Key Vault, giving teams a single interface for managing secrets across all environments and applications."
  - question: "Can Pulumi help with SOC 2 and other compliance frameworks?"
    answer: "Yes. Pulumi's combination of policy as code (CrossGuard), audit logging, secrets management (ESC), and drift detection provides the infrastructure automation foundation for meeting SOC 2, HIPAA, ISO 27001, and FedRAMP requirements. Policies can encode specific compliance rules and enforce them automatically on every deployment."
---

Infrastructure security and compliance is about enforcing security policies, detecting configuration drift, meeting audit requirements, and ensuring infrastructure changes don't introduce vulnerabilities, all without slowing down engineering velocity. For organizations operating under SOC 2, HIPAA, or other compliance frameworks, automating these controls is not optional.

## The challenge: security at the speed of deployment

Security and compliance teams face a fundamental tension. Engineering teams need to move fast: deploying multiple times per day, spinning up new environments, and iterating on infrastructure alongside application code. But every change is a potential security risk, and every resource must meet organizational and regulatory standards.

Manual security reviews can't keep pace with modern deployment velocity. When policy checks happen after deployment, violations are expensive to remediate. When checks happen before deployment through manual approval gates, they become the bottleneck that teams work around rather than through.

The challenge compounds with scale. As organizations grow to thousands of cloud resources across multiple accounts and providers, maintaining visibility into what's deployed, who changed it, and whether it complies with policy becomes increasingly difficult. Configuration drift from manual hotfixes and emergency changes creates gaps between what's defined in code and what's actually running.

This is Pulumi's biggest content gap despite Security & Compliance being a major driver of platform adoption. Organizations evaluating infrastructure platforms consistently cite policy enforcement, secrets management, and compliance automation as critical requirements.

## How Pulumi addresses security and compliance

Pulumi provides an integrated approach to infrastructure security, combining policy as code, secrets management, drift detection, and audit capabilities into the same platform used for infrastructure deployment.

**Policy as code with CrossGuard.** [Pulumi CrossGuard](/docs/iac/packages/crossguard/) lets teams write security and compliance rules in Python, TypeScript, Go, or OPA Rego. Policies run automatically during `pulumi preview` and `pulumi up`, catching violations before resources are created. Rules can enforce anything from "S3 buckets must have encryption enabled" to "no public endpoints without WAF" to cost guardrails on instance sizes.

**Centralized secrets with Pulumi ESC.** [Pulumi ESC](/product/esc/) (Environments, Secrets, and Configuration) provides dynamic credential generation, composable environments, and automatic rotation. Rather than scattering secrets across multiple vault systems, ESC gives teams a single interface that integrates with AWS Secrets Manager, HashiCorp Vault, Azure Key Vault, 1Password, and more. Dynamic credentials are generated on demand and automatically expire, eliminating long-lived secrets.

**AI-powered security operations.** Pulumi Neo can analyze infrastructure configurations for security issues, suggest policy improvements, and help enforce compliance standards. Because Pulumi uses general-purpose programming languages that AI agents understand natively, security automation can participate in the same AI-assisted workflows as application development.

**Audit logging and visibility.** Every infrastructure change flows through Pulumi Cloud with full audit trails: who made the change, what changed, when, and whether it passed policy checks. [Pulumi Insights](/product/pulumi-insights/) provides search and visibility across all cloud resources, making it possible to answer questions like "which resources are publicly accessible?" or "which deployments occurred outside business hours?"

For a comprehensive look at secrets management solutions, see our [Secrets Management Tools Guide](/resources/security-compliance/secrets-management-tools-guide/).

## Key capabilities

**Policy as code.** Define and enforce security rules that run automatically on every deployment. Write policies in the same languages your team already knows, and apply them consistently across all cloud providers and environments.

**Secrets management.** Centralize secrets, generate dynamic credentials, compose environments from reusable configurations, and rotate credentials automatically. Pulumi ESC eliminates secrets sprawl while integrating with your existing vault infrastructure.

**Compliance automation.** Encode compliance framework requirements as automated policies. SOC 2 controls, HIPAA safeguards, and FedRAMP requirements become enforceable rules that run on every deployment, reducing audit preparation from weeks to hours. Customers like Spear AI have achieved 6x faster Authorization to Operate using Pulumi's compliance capabilities.
