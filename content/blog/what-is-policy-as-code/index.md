---
title: What Is Policy as Code?
date: 2026-06-25
draft: false
meta_desc: "Policy as code applies software engineering practices to infrastructure governance. Learn what it is, how it works, the top tools, and how to enforce it."
meta_image: meta.png
feature_image: feature.png
authors:
    - alex-leventer
tags:
    - policy-as-code
    - security
    - governance
---

For most of the last decade, the rules that govern cloud infrastructure have lived somewhere other than the infrastructure itself: in a wiki page, a spreadsheet of controls, a reviewer's head, or a checklist someone is supposed to run before shipping. Infrastructure became code, but the guardrails around it stayed manual. That gap is exactly where misconfigurations slip through.

<!--more-->

Policy as code closes it. **It's the practice of defining and enforcing security, compliance, cost, and operational governance rules as version-controlled, testable code, evaluated automatically in CI/CD pipelines and at deployment time, rather than through manual reviews, console clicks, or static documents.** The same engineering discipline that brought infrastructure under code-based control (version control, testing, peer review, automation) now applies to the rules that govern it.

In other words, it treats compliance requirements the same way software teams already treat application code: write it, review it, test it, version it, and run it automatically so no step depends on someone remembering to do it. Below, I'll walk through what that looks like in practice, why it matters more than ever as AI agents start writing infrastructure, the tools that implement it, and how to get your first policy running in a few minutes.

## What is policy as code?

Policy as code applies the same principles that infrastructure as code brought to cloud provisioning (version control, peer review, automated testing, and continuous enforcement) to the governance rules that control what infrastructure can be created and how it must be configured.

Before policy as code, governance happened through spreadsheets of controls, manual reviewer checklists, or ad-hoc scripts that someone ran (or forgot to run) before a change reached production. As teams scaled, that model broke. A single misconfigured S3 bucket or open security group slips through, and the breach that follows can cost millions of dollars and months of recovery work.

Policy as code emerged alongside [infrastructure as code](/what-is/what-is-infrastructure-as-code/) in the mid-2010s. HashiCorp introduced Sentinel in 2017 to enforce governance across Terraform and described the goal plainly: "an automated way to check in minutes or seconds if requirements are met," rather than waiting for the next audit cycle. The Cloud Native Computing Foundation (CNCF) donated Open Policy Agent (OPA) in 2018, giving the ecosystem an open-source reference implementation that could apply policies across any layer of the stack: Kubernetes admission, API gateways, CI/CD pipelines, and IaC deployments alike.

The core idea is simple: write a rule in code, commit it to a repository, run it automatically, and get a pass or fail result before anything reaches production. The rule travels with your codebase, improves through code review, and generates an audit trail that a compliance team can verify.

## Why does policy as code matter?

Cloud misconfigurations are the leading cause of cloud security incidents. Gartner and the Cloud Security Alliance have found that [misconfigurations drive 80% of data security breaches](https://cloudsecurityalliance.org/blog/2023/08/14/managing-cloud-misconfigurations-risks), and that up to 99% of cloud failures trace back to human error. The average cost of a data breach has reached [$4.88 million globally and $10.22 million in the United States](https://www.ibm.com/reports/data-breach), according to IBM's 2024 Cost of a Data Breach report. Even as IaC adoption has grown (Datadog's State of DevSecOps 2024 found that 71% of AWS organizations use IaC), 38% of those organizations still used ClickOps in all accounts, including production, leaving a gap where misconfigurations can appear without any automated check.

Manual policy review doesn't scale. A security team reviewing hundreds of pull requests for infrastructure changes will miss things. More importantly, by the time a human reviewer catches a misconfigured resource, a developer has already created it, someone else has built on top of it, and the blast radius of changing it has grown. Policy as code shifts enforcement left, to the same moment the infrastructure code is being written and previewed, so violations are caught before they become deployed resources.

The stakes are only growing. As AI agents increasingly write and modify infrastructure, the policies that govern those modifications become the primary safety layer between automation and production.

## How does policy as code work?

A policy as code system follows a consistent lifecycle regardless of which tool you use.

**Write rules in code.** Engineers express governance rules as functions, data structures, or domain-specific query language expressions. A rule might say "no S3 bucket may have public access enabled" or "all resources must have a cost-center tag." The rule lives in a file, alongside the rest of the codebase.

**Store in version control.** Policy files are committed to Git just like application code. Changes go through code review, get a commit history, and can be rolled back. Audit teams can see exactly what the policy was on any given date and who changed it.

**Evaluate automatically.** Policies run in CI/CD pipelines when infrastructure changes are proposed, during `pulumi preview` before any resource is created, or at admission time for Kubernetes clusters. The evaluation compares the proposed or existing resource configuration against the policy rules and produces a pass or fail result.

**Enforce or warn.** Enforcement modes vary. Advisory mode warns developers without blocking a deployment, which is useful during rollout. Mandatory mode blocks a deployment if a policy fails. Some systems support automatic remediation that corrects the violation without requiring human intervention.

**Audit continuously.** Policy as code systems can evaluate already-deployed infrastructure, not just new deployments, giving operations and security teams ongoing visibility into compliance posture across their entire cloud estate.

The two most important enforcement dimensions are **preventative** (block a resource from being created if it violates policy) and **audit** (continuously evaluate existing resources and flag violations). Both are valuable. Preventative enforcement stops misconfigurations from entering production; audit-mode enforcement finds the ones that got in before policy was in place, or that drifted after the fact.

## What are the benefits of policy as code?

Policy as code provides five categories of benefits that address the practical problems teams encounter when trying to govern cloud infrastructure at scale.

**Cost control.** Cost policies can enforce tagging requirements (so resources are attributable to teams and projects), set spend limits on instance types, or flag resources that should be shut down outside business hours. Violations surface during preview, before the expensive resource is created, rather than on the next monthly bill.

**Compliance and security.** Security policies prevent the most common misconfiguration patterns. No S3 bucket should have public access enabled. No database should be exposed to the open internet. No security group should allow ingress from 0.0.0.0/0. These rules are trivial to express in code and can be enforced on every deployment across every team, eliminating the class of incidents that results from one engineer who didn't know the rule.

**Early validation.** Policy evaluation during `pulumi preview` means developers see violations the moment they write the code, not after the resource exists in production. The feedback loop is the same as a failed unit test: immediate, local, and easy to fix.

**Best practices as versioned, testable code.** Policy packs can be published, versioned, and shared across an organization like libraries. A central platform team maintains a canonical set of compliance rules; individual product teams consume them. Policies can have unit tests, just like application code, so regressions are caught before new rules are deployed.

**Consistency at scale.** Without automated enforcement, governance quality varies by team. Some teams are thorough; others are fast and skip steps. Policy as code makes the rule the same for every team, every deployment, automatically. It also integrates with cloud-native controls like AWS IAM Access Analyzer and AWS Organizations tag policies, complementing rather than replacing the native governance primitives each cloud provides.

## What policy as code tools are available?

Several mature tools now handle policy as code across different parts of the stack. Each has a distinct scope and approach.

**Open Policy Agent (OPA)** is the most broadly deployed policy engine in cloud-native environments. OPA uses a query language called Rego to express policies that can govern Kubernetes admission, API gateway authorization, CI/CD pipelines, Terraform plans, and virtually any other system that can send JSON to the OPA API. OPA graduated as a CNCF project in February 2021. It was originally created by Styra, and is now maintained by the broader CNCF community. Its strength is breadth: a single Rego policy set can span multiple layers of an architecture. The learning curve for Rego is steeper than for general-purpose languages, which matters when policies need to be maintained by engineers who are not policy specialists.

**HashiCorp Sentinel** is a policy framework embedded in HashiCorp's commercial products, including HCP Terraform (Standard tier and above), HCP Vault Dedicated, HCP Consul, and Nomad Enterprise. Sentinel uses a proprietary DSL that is purpose-built for policy expression. For teams deeply invested in the HashiCorp ecosystem and using HCP Terraform, Sentinel is a natural fit. It is not available as an independent open-source tool.

**Kyverno** is a Kubernetes-native policy engine that uses YAML and Common Expression Language (CEL) rather than a custom query language, which makes it approachable for teams already fluent in Kubernetes manifest syntax. Kyverno validates, mutates, and generates Kubernetes resources, and can also clean up resources on a schedule. It graduated from the CNCF in March 2026. Kyverno's scope is expanding beyond Kubernetes, but its primary strength remains admission control for Kubernetes clusters.

**Pulumi Policies** adds policy as code to the Pulumi [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform. Policies are written in TypeScript, JavaScript, Python, or Rego (via OPA integration), making them accessible to the same engineers who write the infrastructure code. Policies apply during `pulumi preview` and `pulumi up`, blocking violations before resources are created or modified. Pulumi Policies also powers audit-mode evaluation of resources discovered through Pulumi Insights, including infrastructure that was provisioned with Terraform, CloudFormation, or directly through cloud consoles.

| Tool | Policy language | Primary scope | Open source / governance | Origin |
|---|---|---|---|---|
| Open Policy Agent (OPA) | Rego | General-purpose: Kubernetes, APIs, CI/CD, Terraform | Open source (Apache 2.0); CNCF graduated Feb 2021 | Created by Styra; donated to CNCF; community maintained |
| HashiCorp Sentinel | Sentinel (proprietary DSL) | HashiCorp suite (HCP Terraform, HCP Vault Dedicated, HCP Consul, Nomad Enterprise) | Proprietary; requires paid HCP Terraform Standard+ | HashiCorp (now IBM) |
| Kyverno | YAML + CEL | Kubernetes-native (validate, mutate, generate, cleanup) | Open source; CNCF graduated Mar 2026 | Created by Nirmata; donated to CNCF |
| Pulumi Policies | TypeScript, JavaScript, Python, or Rego | Any cloud (170+ providers) during Pulumi deployments; also audit of discovered resources via Insights | Policy SDK open source (Apache 2.0); org-wide policy group management on paid Pulumi Cloud | Pulumi |

## How does Pulumi implement policy as code?

Pulumi Policies is Pulumi's policy as code engine, built into the [Pulumi platform](/docs/insights/policy/). It runs during every `pulumi preview` and `pulumi up`, evaluating resources against a set of policies before any change reaches the cloud.

**Languages you already know.** Policies are written in TypeScript, JavaScript, Python, or Rego. There is no new language to learn. Engineers write policy functions the same way they write the infrastructure code itself, using the same loops, conditionals, helper functions, unit tests, and package management.

**Policy hierarchy.** Pulumi Policies organizes governance through three levels. Individual policies express a single rule. Policy packs group related policies into a deployable unit (for example, a "CIS AWS Foundations" pack). Policy groups apply a pack at org-wide, project, or stack scope, making enforcement consistent without requiring every team to opt in.

**Enforcement levels.** Every policy operates at one of four enforcement levels:

* **Advisory**: a warning is surfaced, but the deployment continues. Use this during rollout to measure the blast radius of a new rule before enforcing it.
* **Mandatory**: a violation blocks the deployment. Use this for security-critical rules that cannot have exceptions.
* **Remediate**: the violation is corrected automatically in the resource configuration before deployment proceeds.
* **Disabled**: the policy is skipped entirely. Use this to temporarily exempt a rule without removing it from the pack.

**Automatic remediation.** The `remediate` enforcement level uses a `remediateResource` function that Pulumi calls when a policy is violated. Instead of failing the deployment, Pulumi corrects the configuration in place (enabling encryption on a storage bucket that the developer left unencrypted, for example) and proceeds. This is particularly valuable for rules where the fix is deterministic and the goal is adoption rather than blockage.

**Audit mode for existing resources.** Pulumi Policies integrates with Pulumi Insights to evaluate resources that are already running, including those provisioned with Terraform, CloudFormation, or manually through cloud consoles. This means organizations can get compliance visibility over their entire cloud estate, not just the portion managed with Pulumi IaC.

**Pre-built compliance packs.** Pulumi publishes pre-built policy packs for CIS 8.1 (covering AWS, Azure, and Google Cloud), CIS Kubernetes, HITRUST CSF 11.5, NIST SP 800-53 (AWS), PCI DSS v4.0.1 (AWS), and Pulumi Best Practices. These packs can be used as-is or extended with organization-specific rules.

**Open source core.** The Pulumi Policies SDK is open source under Apache 2.0 at [github.com/pulumi/pulumi-policy](https://github.com/pulumi/pulumi-policy). Local enforcement via `--policy-pack` (including advisory, mandatory, and remediate modes) is free. Org-wide policy group management in Pulumi Cloud requires a paid plan.

## How do you get started with policy as code in Pulumi?

Getting started with Pulumi Policies takes a few minutes if you already have Pulumi installed.

1. **Create a new policy pack.** Run `pulumi policy new aws-typescript` to scaffold a TypeScript policy pack for AWS. Additional templates include `aws-python`, `aws-opa`, `azure-opa`, `gcp-opa`, and `kubernetes-opa`.

2. **Write a rule.** Open `index.ts` (or the Python equivalent) and add a `validateResource` function with your policy logic. Assign the rule an `enforcementLevel` of `advisory` to start.

3. **Test locally.** Run `pulumi preview --policy-pack .` from your Pulumi project directory. Pulumi Policies evaluates your policy against the preview plan and reports violations inline. No cloud resources are created during this step.

4. **Publish the policy pack.** When the pack is ready to share, run `pulumi policy publish` from within the policy pack directory. Pulumi infers the organization from your logged-in context and makes the pack available to your organization.

5. **Enable org-wide enforcement.** Run `pulumi policy enable <your-org>/<pack-name> latest` to apply the pack across all stacks in your organization. Pulumi Cloud automatically downloads the pack for every deployment, with no `--policy-pack` flag required on individual runs.

6. **Graduate to mandatory enforcement.** Start in `advisory` mode to understand the scope of violations, then promote critical rules to `mandatory` as teams address them. Use the `remediate` level for rules where automatic correction is appropriate.

The [Pulumi Policies documentation](/docs/insights/policy/) and [policy packs guide](/docs/insights/policy/policy-packs/) walk through the full lifecycle in detail.

## What does policy as code look like in production?

### Spear AI: 18-month ATO reduced to 3 months

Spear AI builds AI-powered software for the United States Navy and needs to operate in AWS commercial, AWS GovCloud, air-gapped environments, and naval edge deployments, each with strict security controls. Achieving Authorization to Operate (ATO) is a multi-year process of proving to military auditors that every resource meets the required security posture.

Spear AI used Pulumi Policies to define their security controls as policy packs, then gave the auditors direct access to those packs. As Michael Hunter, co-founder and CEO of Spear AI, described it:

> "We gave our auditors access to our policy packs because it's far easier to understand and prove controls in code than in a bunch of docs and diagrams. That process of manual review has gone away. We've gone down from a year and a half to expecting an ATO in three months."

The policy packs served simultaneously as the enforcement mechanism and the audit evidence, collapsing what had been a manual documentation exercise into a code review.

### Modivcare: up to 25% infrastructure cost reduction and governance over legacy infrastructure

Modivcare needed to bring governance to a mixed environment: some infrastructure managed by Pulumi IaC, some inherited from Terraform, some provisioned manually. Pulumi Policies in audit mode, combined with Pulumi Insights account scanning, gave them visibility across the entire estate.

As Zachary Cook, Senior Manager of DevOps at Modivcare, put it:

> "By integrating Pulumi Policy as Code with Insights Account Scanning and our developer portal, we're achieving the holy grail for Platform Engineering: instant visibility and governance over legacy infrastructure that isn't yet defined in IaC, while also accelerating our path to production for new cloud-native projects."

The combination of [policy as code enforcement](/docs/insights/policy/) with [Insights-based governance](/product/insights-governance/) let Modivcare start enforcing cost controls on resources they didn't even write with Pulumi, reducing infrastructure costs by up to 25%.

## Why this matters more every day

The case for policy as code used to rest on scale: too many teams, too many pull requests, too many ways for a single misconfigured bucket to reach production. That argument still holds. But the ground is shifting underneath it.

As AI agents begin writing and modifying infrastructure, the volume and velocity of changes will outpace anything a human review process was designed to handle. The policies that govern those changes become the primary safety layer between automation and production, and a rule encoded as code, enforced on every deployment, doesn't care whether the change came from an engineer or an agent. As Pulumi CEO Joe Duffy puts it, "the smartest agent in the world still needs guardrails, audit trails, and policy enforcement to be trusted with production systems at scale, and that layer gets more valuable as agents get more capable, not less."

That's the real promise here: policy as code is what lets you say yes to faster, more automated infrastructure without giving up control over what actually ends up running.

## Frequently asked questions about policy as code

### What is policy as code in simple terms?

Policy as code means writing your organization's IT governance rules (what can be deployed, how it must be configured, what tags it must have) as code files that are version-controlled and enforced automatically. Instead of a PDF document that a human checks manually, the rule is a function that runs in a pipeline and produces a pass or fail result.

### How is policy as code different from infrastructure as code?

Infrastructure as code defines and provisions the cloud resources you want to exist. Policy as code defines the rules that govern how those resources are allowed to be configured. They are complementary: IaC creates the infrastructure, and policy as code ensures the infrastructure stays within acceptable bounds. You can apply policy as code to infrastructure that was not created with IaC (through audit mode), and you can run IaC deployments through a policy gate that blocks non-compliant changes before they reach the cloud.

### What problems does policy as code solve?

Policy as code addresses three core problems. First, it eliminates manual review that does not scale: a security team cannot reliably review every pull request touching infrastructure across dozens of teams. Second, it shifts enforcement left to the moment the code is written, so violations are caught before resources exist in production. Third, it creates an auditable, version-controlled record of what the organization's policies were at any point in time, which simplifies compliance evidence gathering.

### What languages can you write policies in?

It depends on the tool. OPA uses Rego, a purpose-built query language. HashiCorp Sentinel uses its own proprietary DSL. Kyverno uses YAML with CEL expressions. Pulumi Policies supports TypeScript, JavaScript, Python, and Rego, allowing engineers to write policies in the same languages they use for their infrastructure code and application code.

### What is the difference between advisory and mandatory enforcement?

Advisory enforcement surfaces a violation as a warning but allows the deployment to proceed. It is the appropriate mode when rolling out a new policy, because it shows which existing resources would be affected without breaking anyone's workflow. Mandatory enforcement blocks the deployment when a violation is detected. Security-critical rules, such as "no database may be publicly exposed," belong in mandatory mode. Most teams start new policies in advisory mode and promote them to mandatory after confirming the blast radius.

### Can policy as code automatically fix violations?

Yes, some systems support automatic remediation. Pulumi Policies' `remediate` enforcement level calls a `remediateResource` function that corrects the configuration before deployment proceeds. For example, if a policy requires encryption on all storage buckets and a developer forgets to enable it, Pulumi Policies can enable it automatically rather than failing the deployment. Remediation is most appropriate for rules where the correct value is deterministic and the goal is adoption rather than blockage.

### Does policy as code work with Terraform or existing cloud resources?

Yes. Pulumi Policies integrates with Pulumi Insights to evaluate resources that were provisioned with Terraform, CloudFormation, or directly through cloud consoles, and not only those managed with Pulumi IaC. This audit mode gives organizations compliance visibility across their entire cloud estate. For native Terraform policies, OPA (with the `conftest` tool) and HashiCorp Sentinel can evaluate Terraform plan output.

### What is the difference between OPA, Sentinel, and Kyverno?

OPA is a general-purpose policy engine that works across any system sending JSON, not just infrastructure. Sentinel is embedded in HashiCorp's commercial products and is not available as a standalone open-source tool. Kyverno is purpose-built for Kubernetes admission control, using YAML and CEL rather than a custom query language. All three have different strengths, scopes, and licensing models. The comparison table earlier in this post covers these dimensions in detail.

### What are the best policy as code tools?

The right tool depends on your stack. For Kubernetes-focused teams that want to avoid learning a new language, Kyverno is the most approachable. For teams building on the HashiCorp ecosystem and already paying for HCP Terraform, Sentinel integrates naturally. For multi-layer enforcement across Kubernetes, APIs, and CI/CD with a single policy language, OPA is the most flexible. For teams using Pulumi IaC who want policies in the same language as their infrastructure code, with support for automatic remediation and audit of discovered resources, Pulumi Policies is the natural choice.

### Is Pulumi Policies free?

Local enforcement via the `--policy-pack` flag (including advisory, mandatory, and remediate modes) is free with any Pulumi project. The Pulumi Policies SDK itself is open source under Apache 2.0. Org-wide policy group management in Pulumi Cloud, which automatically applies packs to all stacks across an organization, requires a paid plan. Pre-built compliance packs (CIS, NIST, PCI DSS, HITRUST) are included for organizations on qualifying plans.

## Learn more

Pulumi Policies enforces policy as code across any cloud using TypeScript, Python, or Rego (170+ providers supported), with automatic remediation and audit coverage for resources that weren't provisioned with Pulumi IaC. [Get started with Pulumi Policies](/docs/insights/policy/get-started/) to write your first policy pack in minutes.

Related reading:

* [Pulumi Policies documentation](/docs/insights/policy/)
* [Policy packs guide](/docs/insights/policy/policy-packs/)
* [Insights and governance](/product/insights-governance/)
* [Benefits of policy as code](/blog/benefits-of-policy-as-code/)
* [Enforcing policy as code on discovered resources](/blog/enforcing-policy-as-code-on-discovered-resources-with-pulumi/)
* [OPA support for Pulumi Policies](/blog/opa-support-for-crossguard/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is cloud security?](/what-is/what-is-cloud-security/)
* [What is platform engineering?](/what-is/what-is-platform-engineering/)
* [What is DevOps?](/what-is/what-is-devops/)
