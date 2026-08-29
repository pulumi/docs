---
title: "Best Policy as Code Tools in 2026"
date: 2026-08-28
draft: false
meta_desc: "Compare the best policy as code tools in 2026: OPA, HashiCorp Sentinel, Kyverno, Checkov, and Pulumi Policies, chosen honestly by fit."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - policy-as-code
    - security
    - infrastructure-as-code
    - devops
    - ai-agents
category: general
faq_schema: true
itemlist_name: "Policy as Code Tools"
itemlist:
    - name: "Open Policy Agent (OPA)"
    - name: "HashiCorp Sentinel"
    - name: "Kyverno"
    - name: "Checkov"
    - name: "Pulumi Policies"
    - name: "OPA Gatekeeper"
    - name: "Conftest"
    - name: "Cloud Custodian"

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Policy as code used to be a compliance checkbox. Now it is the layer that decides whether an AI agent's proposed infrastructure change actually ships.

        We compared the real options: OPA, Sentinel, Kyverno, Checkov, and Pulumi Policies.
    linkedin: |
        "Policy as code" and "IaC security scanning" get lumped together constantly, and they solve different problems. A scanner reports that a resource is misconfigured. A policy engine holds the authority, natively, to decide whether a proposed change is allowed to happen at all before it is applied.

        That distinction matters more now that AI agents are proposing infrastructure changes alongside engineers. An agent's blast radius is bounded by two things: what it can reach, and what a policy will let it do.

        We compared the tools that actually do policy-as-code enforcement in 2026: Open Policy Agent, HashiCorp Sentinel, Kyverno, Checkov, and Pulumi Policies, plus where Gatekeeper, Conftest, and Cloud Custodian fit. Each entry includes where the tool is a good fit and where it is not.
    bluesky: |
        Policy as code vs. IaC security scanning: not the same category.

        We compared OPA, Sentinel, Kyverno, Checkov, and Pulumi Policies on what they actually enforce, and when.
---

Policy as code means writing infrastructure rules as version-controlled code, then having a policy engine evaluate every proposed change against those rules before it takes effect. It matters more as AI agents start proposing infrastructure changes alongside engineers, because a policy engine decides whether a given change is allowed to happen, regardless of who or what authored it.

<!--more-->

## Why AI agents raise the stakes for policy as code

An AI agent that can open a pull request against your infrastructure code can also, in principle, propose a change that deletes a production database, widens a security group to the internet, or spins up resources nobody approved. Most of the current conversation about containing that risk focuses on identity: scoping what an agent's credentials can reach, and limiting which systems it can call. That is necessary, and it is not the whole answer.

Identity scoping bounds what an agent *could* touch. It says nothing about what a specific, concrete change *will actually do*. Policy as code operates at a different point in the pipeline. When a policy engine runs against an infrastructure preview, before anything is created, replaced, or destroyed, it evaluates the real, itemized set of resource changes a specific plan would make, and it can block that plan outright if it violates a rule. That is a stronger and more precise guarantee than credential scoping alone, and it holds whether the change came from a human running `terraform apply`, a CI pipeline, or an autonomous agent.

This is the vocabulary infrastructure and security teams reach for by default when this comes up: bounding the blast radius of a change before it executes, on top of bounding the reach of whoever or whatever proposed it. Pulumi's own documentation on [policy as code](/docs/insights/policy/) describes preventative policies this way: evaluated during `pulumi preview` and `pulumi up`, blocking a deployment outright when a resource change violates a rule, before that resource is ever touched. For a fuller definition of the category and how the major engines differ, see [what is policy as code](/what-is/what-is-policy-as-code/).

## What counts as a policy as code tool, and what does not

Search for "policy as code tools" today and you will find genuine policy engines sitting next to products built for a related but different job: scanning infrastructure-as-code for misconfigurations, or reviewing code changes for security issues. Both categories matter. They are not interchangeable, and conflating them leads teams to pick the wrong tool for the problem they actually have.

A policy engine evaluates a proposed change against rules you write, and it can block that change from ever being applied. A security scanner inspects code or a running environment and reports what it finds; some can open a fix as a pull request, and one wired into a CI gate can fail a build and stop a deploy that way. The real distinction is where the blocking authority lives: a policy engine holds it natively, while a scanner borrows it from whatever pipeline hosts it. The table below draws that line using Checkov as the bridge case, since it legitimately does both.

| Tool category | Who writes the rules | When it runs | Can it block a deploy | What it is optimized for |
| --- | --- | --- | --- | --- |
| Policy engine (OPA, Sentinel, Kyverno, Pulumi Policies) | Your team, in code | Before or as part of the deployment | Yes, when set to a blocking enforcement level | Enforcing an organization's own rules on every change |
| Scanner with a policy layer (Checkov) | Built-in rule library, extensible with your own YAML or Python checks | Usually in CI, against code, ahead of deployment | Only if wired into a CI gate that fails the build | Broad coverage of known misconfiguration patterns |
| AI-assisted code security tools (gomboc.ai, CodeAnt AI) | Vendor's rule set, applied by an AI reviewer | In CI or as an assistant reviewing pull requests | Not at deploy time; some can gate a merge, and remediation is typically a PR for a human to approve | Finding and proposing fixes for security issues in code |
| Cloud security platforms (CNAPPs) | Vendor's rule set | Continuously, against running cloud accounts | Generally not part of the deploy path; they alert and prioritize findings | Runtime visibility, posture management, and threat detection across an entire cloud estate |

None of this makes the second and third rows less useful. It means a team choosing "a policy as code tool" to gate deployments should look at the first row, and a team choosing a broader security posture tool has a different, equally valid, shopping list.

## Open Policy Agent (OPA)

Open Policy Agent is the general-purpose policy engine behind much of the policy-as-code ecosystem. Rules are written in Rego, a purpose-built query language, and OPA itself is cloud- and stack-agnostic: it ships as a standalone binary, a sidecar, an embeddable library, or built into other tools such as Envoy, Kubernetes admission controllers, and CI checks. OPA is a graduated Cloud Native Computing Foundation project and is licensed under Apache 2.0, with governance held by the CNCF rather than any single vendor. As of OPA 1.0, Rego v1 is the default dialect, tightening syntax that had accumulated ambiguity over the years.

OPA's strength is its reach: one policy language, evaluated consistently across Kubernetes, service meshes, CI pipelines, and infrastructure tooling that embeds it. That same generality is its cost. Rego has a real learning curve for teams used to YAML or a general-purpose language, and OPA by itself is an evaluation engine, not a full workflow; you still need to decide where it plugs in and how violations get surfaced. Teams that want policy as code across many different systems, and are willing to invest in Rego, tend to get the most out of it. Teams that only need to govern a single Kubernetes cluster or a single IaC tool often find a narrower, native option a faster starting point.

## HashiCorp Sentinel

Sentinel is HashiCorp's policy-as-code framework, built into HCP Terraform, Terraform Enterprise, Vault, Consul, and Nomad Enterprise. Unlike OPA, Sentinel is proprietary to HashiCorp's own products rather than a general embeddable engine, and it uses its own policy language rather than Rego. Policies attach directly to a Terraform run and can enforce advisory, soft-mandatory, or hard-mandatory checks against the plan before it applies.

The practical advantage of Sentinel is that it requires no separate integration if your team already runs Terraform through HCP Terraform: policy as code, including both Sentinel and OPA support, is available starting on HCP Terraform's free tier, not gated behind an enterprise contract. The tradeoff is scope. Sentinel only governs HashiCorp's own products, so a team standardizing policy across Terraform, Kubernetes, and a homegrown CI pipeline will still need a second engine for everything outside the HashiCorp stack. IBM completed its acquisition of HashiCorp in early 2025; there is no publicly confirmed change to Sentinel's licensing or integration model as a result, though HashiCorp's product direction under IBM is still settling, so it is worth confirming current terms directly with HashiCorp before committing to it for a new rollout.

## Kyverno

Kyverno is a policy engine built specifically for Kubernetes, and it is the clearest example of "native" policy as code: rules are written as Kubernetes YAML resources, not a separate language, so a team already comfortable with Kubernetes manifests can read and write Kyverno policies with almost no additional learning. It runs as an admission controller, validating, mutating, generating, or cleaning up resources as they are created or changed, and it also ships a CLI for testing policies offline before they reach a cluster. Kyverno is a graduated CNCF project under Apache 2.0.

Kyverno's fit is obvious for teams whose policy problem is entirely inside Kubernetes: pod security standards, image provenance, resource quotas, and similar admission-time rules. Its fit gets weaker the moment policy needs to extend outside the cluster, to cloud accounts, CI pipelines, or non-Kubernetes infrastructure, since that is explicitly not what it was built for. Teams managing a mixed estate typically pair Kyverno for in-cluster rules with a broader engine, such as OPA or a provider-level tool, for everything else.

## Checkov

Checkov started as a static analysis tool for infrastructure-as-code files, built at Bridgecrew and now part of Palo Alto Networks' Prisma Cloud. Out of the box, it is best described as a scanner: it ships with more than a thousand pre-built checks covering common misconfigurations across Terraform, CloudFormation, Kubernetes manifests, and other formats, and it runs in CI to fail a build when a check trips.

What earns Checkov a place in a policy-as-code roundup rather than a pure scanner roundup is that it also supports genuine custom policy authoring, in either YAML (for attribute and connection-state checks with AND/OR logic) or Python (for anything the YAML format cannot express). A team can write its own organization-specific rules the same way it would with a dedicated policy engine. Checkov's primary mode of use, though, remains its built-in rule library rather than custom authoring, and it does not run inside the deployment tool itself the way Sentinel or Pulumi Policies do; it depends on a CI gate to have any blocking authority. Teams that want broad, low-effort coverage of known misconfiguration patterns, with the option to add custom rules later, tend to reach for Checkov first.

## Pulumi Policies

Pulumi Policies let a team write policy rules in the same general-purpose languages they already use for infrastructure: TypeScript, JavaScript, and Python, alongside OPA and Rego for teams that want to reuse existing Rego rules. A policy pack is a project directory, scaffolded with `pulumi policy new`, and a team can start using one locally and for free with `pulumi preview --policy-pack <path>` against any backend, with no enterprise tier required to try it.

Two things distinguish how Pulumi Policies apply policy in practice. Preventative policy groups run before a resource is deployed, evaluating the actual, itemized set of changes a `pulumi preview` or `pulumi up` would make, and a policy set to the mandatory enforcement level blocks the deployment outright if it fails. Audit policy groups run on a schedule instead, against both Pulumi-managed stacks and cloud accounts connected through Pulumi's resource discovery, and they report violations rather than blocking anything, which makes them the documented way to test how a new policy would behave, its own blast radius, before flipping it to mandatory in production. A third enforcement level, remediate, automatically fixes a resource's properties in flight so a deployment can proceed compliant, though this only applies to resource-level checks, not whole-stack validation.

Pre-built policy packs cover common compliance frameworks including CIS benchmarks for AWS, Azure, and GCP, CIS Kubernetes benchmarks, and frameworks such as NIST, PCI DSS, and ISO 27001. Pulumi Policies fit teams that want policy written in the same language as their infrastructure, evaluated at the same point the infrastructure itself is evaluated, whether the change was authored by an engineer or by an AI agent working through Pulumi. Teams with no existing investment in Pulumi as an infrastructure tool will generally find a standalone engine like OPA or Sentinel a more natural starting point: because Pulumi Policies evaluates the actual resource graph a Pulumi deployment is about to change, its deployment-time enforcement is most direct for infrastructure that is also defined in Pulumi.

## Also worth knowing: Gatekeeper, Conftest, and Cloud Custodian

A handful of other tools round out the category. OPA Gatekeeper packages OPA specifically as a Kubernetes admission controller, using constraint templates and custom resources rather than Kyverno's native YAML, for teams who prefer Rego but want Kubernetes-native packaging. Conftest, also built on OPA, is a command-line tool for testing structured configuration files, including YAML, JSON, and Terraform plan output, against Rego policies in a CI pipeline, ahead of the deploy step rather than at it. Cloud Custodian takes a different approach: YAML rules for governing existing cloud resources, such as tagging, retention, and cost controls, evaluated on a schedule against live accounts rather than at deployment time. It is a Cloud Native Computing Foundation incubating project. Each fills a specific gap the five tools above do not fully cover.

## How the policy as code tools compare

| Tool | Policy language | Primary scope | Where it runs | License / governance | Best fit |
| --- | --- | --- | --- | --- | --- |
| Open Policy Agent | Rego | General purpose, any system that embeds it | Standalone, sidecar, or embedded | Apache 2.0, CNCF graduated | Teams standardizing one engine across many systems |
| HashiCorp Sentinel | Sentinel language | HashiCorp products only | Inside HCP Terraform, Vault, Consul, Nomad Enterprise | Proprietary to HashiCorp | Teams already centered on HCP Terraform |
| Kyverno | Kubernetes YAML (plus CEL) | Kubernetes only | Kubernetes admission controller, plus CLI | Apache 2.0, CNCF graduated | Teams whose policy needs are entirely in-cluster |
| Checkov | YAML or Python for custom checks, plus a built-in library | IaC files across many formats | CI, against code | Apache 2.0 | Teams that want broad, ready-made misconfiguration coverage |
| Pulumi Policies | TypeScript, Python, or Rego | Pulumi-managed infrastructure and, via audit groups, connected cloud accounts | Pulumi preview and up, plus scheduled audits | Open source SDK; some pre-built packs are Business Critical edition | Teams already building infrastructure with Pulumi |

## How to choose a policy as code tool

The right starting question is not which tool is best in the abstract, but where the policy needs to live. A few things worth checking before committing:

- Does the policy need to block a change before it happens, or is it enough to flag a violation after the fact? Preventative enforcement and audit-style scanning solve different problems, and most mature setups eventually use both.
- Is the scope a single system, such as one Kubernetes cluster or one Terraform workspace, or does it need to span multiple infrastructure tools and cloud providers?
- Who is going to write and maintain the policies? A team already fluent in Rego gets more mileage from OPA-based tools; a team that wants policy in the same language as its infrastructure code will get more mileage from a tool like Pulumi Policies or Checkov's Python checks.
- Does the team need pre-built compliance frameworks out of the box, or is it starting from custom, organization-specific rules?

Most organizations end up running more than one of these tools rather than picking a single winner, since a Kubernetes-native engine, a CI-time scanner, and a deployment-time policy engine are each solving a distinct part of the problem.

## Frequently asked questions

### Is policy as code the same as IaC security scanning?

No. Policy as code evaluates a proposed change against rules a team writes and can block that change before it is applied. IaC security scanning inspects code or a running environment for known misconfiguration patterns and reports what it finds. Checkov is the clearest example of a tool that does real work in both categories, since it ships a large built-in scanning library alongside genuine custom policy authoring in YAML or Python. Most other tools, including the AI-assisted code security products and the broader cloud security platforms that show up in the same searches, sit firmly on the scanning and reporting side rather than the blocking side.

### Can policy as code stop an AI agent from making a destructive change?

It can, when a preventative policy is set to a blocking enforcement level and the agent's change goes through the same deployment path as any human-authored change. Because a preventative policy evaluates the actual, itemized set of resources a specific change would create, replace, or delete, it applies regardless of who or what proposed the change, which is a stronger guarantee than restricting an agent's credentials alone. It is not a complete answer on its own: a policy only covers what it was written to check, so gaps in policy coverage remain gaps regardless of who is deploying.

### Do you need more than one policy as code tool?

Often, yes. A team running Kubernetes, a CI pipeline, and infrastructure-as-code typically ends up with a Kubernetes-native engine like Kyverno or Gatekeeper for in-cluster rules, a scanning tool like Checkov in CI, and a deployment-time engine such as Sentinel or Pulumi Policies wherever infrastructure is actually provisioned. Consolidating onto a single general-purpose engine such as OPA is possible, but it trades that consolidation for the cost of writing and maintaining Rego across every integration point.

### What is the difference between blocking a change and auditing existing resources?

Blocking, sometimes called preventative or mandatory enforcement, evaluates a proposed change before it happens and stops it if it violates a rule. Auditing evaluates resources that already exist, whether they were created through the tool being audited or by some other means entirely, and reports violations without stopping anything. Audit-style checks are also the safer way to introduce a new policy: running it in report-only mode first shows how many existing resources it would affect before anyone sets it to block deployments outright.

## Where to go next

For a fuller definition of the category and how the major engines compare on language and scope, start with [what is policy as code](/what-is/what-is-policy-as-code/). For the business case behind adopting policy as code in the first place, see [the benefits of policy as code](/blog/benefits-of-policy-as-code/). For a walkthrough of getting a team started with Pulumi's own policy engine, see [take control with policy as code](/blog/take-control-with-pac/), and for the full reference on preventative and audit policy groups, enforcement levels, and pre-built packs, see the [Pulumi Insights policy documentation](/docs/insights/policy/).
