---
title: "Best Infrastructure Drift Detection Tools in 2026"
date: 2026-11-05
draft: false
meta_desc: "The best drift detection tools in 2026: driftctl, Terraform and OpenTofu, AWS Config, Crossplane, Firefly, and Pulumi, compared on coverage and response."
feature_image: feature.png
authors:
    - pulumi-content-team
tags:
    - infrastructure-as-code
    - devops
    - terraform
    - aws
    - insights
category: general
faq_schema: true
itemlist_name: "Infrastructure Drift Detection Tools"
itemlist:
    - name: "driftctl"
    - name: "Terraform and OpenTofu (plan-based detection)"
    - name: "AWS Config"
    - name: "Crossplane"
    - name: "Spacelift and env zero"
    - name: "Firefly"
    - name: "Pulumi"
      url: "https://www.pulumi.com/"

related_posts:
    - day-2-operations-drift-detection-and-remediation
    - best-terraform-alternatives

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        How good your drift detection is depends on how much of your infrastructure the tool can see, and what it does once it finds a difference.

        We compared driftctl, Terraform and OpenTofu, AWS Config, Crossplane, Firefly, and Pulumi on both questions.
    linkedin: |
        Most drift detection comparisons list features. Two questions sort the tools faster: what can the tool see, and what does it do when it finds a difference?

        Plan-based tools check the resources in your code and state. AWS Config sees every supported resource in an AWS account but knows nothing about your IaC. Firefly and Pulumi Insights inventory the whole estate, including resources nobody codified. On the response side, some tools report, some open pull requests, and some revert the change.

        We compared driftctl (now in maintenance mode), Terraform and OpenTofu, AWS Config, Crossplane, Spacelift and env zero, Firefly, and Pulumi, with a coverage table and a decision table for picking one.

        No tool stops someone from changing a resource in the console. The useful ones find it quickly and give you a clear way to respond.
    bluesky: |
        Drift detection quality depends on two things: how much of your estate the tool can see, and what it does after it finds a difference.

        We compared driftctl, Terraform, AWS Config, Crossplane, Firefly, and Pulumi on both.
---

The best infrastructure drift detection tool depends on how much of your cloud the tool can see and what you want it to do when something changes. Terraform and OpenTofu plans check the resources in your code. AWS Config watches everything in an AWS account. Crossplane reverts changes automatically. Firefly and Pulumi inventory the full estate, including resources nobody codified, and Pulumi adds a refresh-and-preview workflow you can run in CI.

<!--more-->

Infrastructure drift (sometimes called configuration drift) is the gap between what your infrastructure code says should exist and what actually runs in the cloud. A console edit during an incident or a bucket created by hand leaves the code out of date. Drift detection tools exist to find those gaps. We build Pulumi, which is on this list, so we have tried to state its limits as plainly as the others. They differ in two ways that matter more than any feature checklist: what they can detect drift in, and what they do after they find it.

## What should a drift detection tool tell you?

We compared each tool on two questions, plus its cost and maintenance status.

**Coverage: what can it see?** There are three levels. Some tools see only resources declared in your code or state file. Some see the configuration of everything in one cloud account, whether or not your IaC created it. The broadest tools inventory the whole estate and label each resource as managed, drifted, or unmanaged.

**Response: what happens next?** A tool can print a diff, send an alert, open a pull request, revert the cloud to match the code, or help you adopt the change into code. Regulated environments may want a human to approve every revert, while teams running ephemeral environments may want automatic correction.

**Cost and upkeep.** Open source tools are free but need scheduling and alerting wired up. Hosted platforms handle that and charge for it.

No tool on this list eliminates drift. People will still change things in the console, and automation will still touch resources it does not own. What the tools below change is how quickly you find out and how much work it takes to respond.

## The best infrastructure drift detection tools in 2026

### 1. driftctl

[driftctl](https://github.com/snyk/driftctl) was the first widely used open source tool built specifically for drift. Its README describes it as a tool that "Measures infrastructure as code coverage, and tracks infrastructure drift." It compared Terraform state against what existed in AWS, GitHub, Azure, and Google Cloud, and it reported two things: resources that had drifted and resources that existed in the cloud with no Terraform behind them. That second report put it ahead of plain plans on coverage.

The main caveat is project status. The README now says: "This project is now in maintenance mode. We cannot promise to review contributions. Please feel free to fork the project to apply any changes you might want to make." The [latest release on GitHub](https://github.com/snyk/driftctl/releases) is v0.40.0 from December 2023, and we found no official successor named in the repository as of November 2026. It also supports Terraform only.

**Best for:** teams with Terraform state that want a one-off audit of unmanaged resources and are comfortable with an unmaintained tool.

**Watch out for:** new cloud resource types and provider changes will not be tracked. Treat it as a starting point or fork it, and do not build a long-term process on it.

### 2. Terraform and OpenTofu (plan-based detection)

The default drift check for Terraform users is the plan. In the [Terraform plan documentation](https://developer.hashicorp.com/terraform/cli/commands/plan), the `-detailed-exitcode` flag returns 0 when there are no changes, 1 on error, and 2 when changes are present, which makes a scheduled CI job a workable drift alarm. Refresh-only mode "creates a plan whose goal is only to update the Terraform state and any root module output values to match changes made to remote objects outside of Terraform." [OpenTofu](https://opentofu.org/docs/cli/commands/plan/) supports the same flags. We found no built-in scheduled drift detection in the OpenTofu docs as of November 2026, so the schedule comes from your CI system.

For managed scheduling, HCP Terraform offers [health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health). HashiCorp's docs say that "Drift detection determines whether your real-world infrastructure matches your Terraform configuration," and that assessments are available in the Standard and Premium editions. The feature needs remote or agent execution mode.

Coverage is the limit. A plan only sees resources in your configuration and state. Resources created by hand never show up. Terraform has been adding ways to find them: the [bulk import documentation](https://developer.hashicorp.com/terraform/language/import/bulk) says "You can configure queries that instruct Terraform to search your existing infrastructure for unmanaged resources," which helps with adoption but is a separate workflow from drift checks.

**Best for:** teams already on Terraform or OpenTofu who want drift checks with no new tools.

**Watch out for:** blind spots for anything outside state.

### 3. AWS Config

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) starts from the account instead of the code. It "provides a detailed view of the configuration of AWS resources in your AWS account," and you can use rules "to evaluate the configuration settings of your AWS resources." When a resource violates a rule, AWS Config flags it as noncompliant and sends a notification. [Conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) bundle rules and remediation actions for an account, a Region, or an organization, and [remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) runs through AWS Systems Manager Automation documents.

Coverage is broad inside AWS, because Config records supported resources whether or not an IaC tool created them. The tradeoff is that it compares resources against rules and recorded history, and it has no knowledge of your Terraform or Pulumi code. It also covers only AWS. [Pricing](https://aws.amazon.com/config/pricing/) is based on configuration items recorded, rule evaluations, and conformance pack evaluations, which can add up in large accounts.

If you deploy with CloudFormation, its own [drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) compares a stack's actual configuration with its expected configuration. The docs note that "CloudFormation only determines drift for property values that are explicitly set," and resources that do not support drift detection get a status of NOT_CHECKED.

**Best for:** AWS-heavy organizations that want compliance-style detection across every account.

**Watch out for:** rules describe what should be true in general, so you will still need another tool to compare against your IaC.

### 4. Crossplane

[Crossplane](https://docs.crossplane.io/latest/whats-crossplane/) handles drift by continuous reconciliation. Its docs say: "If your software ever *drifts* from your desired state, the control plane automatically corrects the drift." For managed resources, [the docs](https://docs.crossplane.io/latest/managed-resources/managed-resources/) say "Crossplane overrides any changes made to an external resource outside of Crossplane. If a user makes a change inside a Provider’s web console, Crossplane reverts that change back to what's configured in the `forProvider` setting."

That is the most automatic response on this list, and it reconciles continuously instead of on a schedule. Two limits apply. Crossplane covers only resources you define as managed resources, so unmanaged resources in the account stay invisible. And because it is built on Kubernetes, you need a cluster running the controllers, which is real operational weight for a team that does not already run one.

**Best for:** Kubernetes-centric platform teams that want automatic correction.

**Watch out for:** auto-revert is only as safe as your desired state, and the override applies under the default management policy. A wrong manifest gets enforced just as faithfully as a right one.

### 5. Spacelift and env zero

IaC orchestrators run the plan-based approach on a schedule so you do not have to build it. [Spacelift](https://docs.spacelift.io/concepts/stack/drift-detection) has "a built-in mechanism to detect and (optionally) reconcile drift" by "periodically executing proposed runs on your stable infrastructure," and its docs note drift detection only works on private workers. [env zero](https://docs.envzero.com/docs/drift-detection) "schedules deployment tasks that conclude with an analysis of the Terraform plan output" and offers automatic and manual remediation. Scheduled drift sits on paid tiers or under run limits ([Spacelift pricing](https://spacelift.io/pricing), [env zero pricing](https://www.env0.com/pricing)).

Because both rely on plan output, they inherit the plan's coverage: declared resources only.

**Best for:** teams that run many Terraform or OpenTofu stacks and want scheduling, approvals, and alerts in one place.

**Watch out for:** another platform to pay for, with the same visibility limits as the underlying plan.

### 6. Firefly

[Firefly](https://docs.firefly.ai/key-features/cloud-asset-inventory) sits above your IaC tools and inventories the whole estate. Its docs describe "a Cross-Cloud Asset Inventory that gives you complete visibility into all your cloud resources and their IaC status." Each resource gets one of four states: codified (managed by IaC and in sync), drifted (managed by IaC but deviated), unmanaged (created outside IaC), or ghost (exists in code or state but missing from the cloud).

On the response side, [drift detection](https://docs.firefly.ai/key-features/drift-detection) works "in real-time (via event-driven hooks and periodic scans)," and Firefly "can open a Pull Request to your Git repo with the necessary code changes to match the live state (or vice versa)." Its [codification feature](https://docs.firefly.ai/detailed-guides/codification) converts existing resources into IaC in several formats, including Terraform, OpenTofu, Pulumi, and CloudFormation. The [remote state integrations page](https://docs.firefly.ai/integrations/iac-remote-state) lists Terraform-family backends, so check that your state backend is supported.

Firefly [pricing](https://www.firefly.ai/pricing) listed paid plans and a 14-day free trial, with no free tier, when we checked in November 2026.

**Best for:** organizations with a large amount of unmanaged infrastructure and several IaC tools in play.

**Watch out for:** cost, and a second source of truth that your team has to trust and keep configured.

### 7. Pulumi

Pulumi gives you three layers, and they map to the two questions above.

**Detection from the CLI.** The [drift documentation](/docs/iac/operations/stack-management/drift/) calls `pulumi refresh --preview-only` "the canonical way to detect drift from the CLI." The command queries each resource's provider for its actual configuration, compares the result to the stack's state, and prints a diff without changing state or cloud resources. In CI, `pulumi refresh --preview-only --expect-no-changes` exits non-zero when drift exists. Both flags are on the [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) page, and [`pulumi preview --refresh`](/docs/iac/cli/commands/pulumi_preview/) checks for drift as part of a normal preview. If you are coming from Terraform, `pulumi preview` plays the role of `terraform plan` and `pulumi refresh` the role of a refresh-only plan. The [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) maps the rest of the commands.

**Scheduled detection and response in Pulumi Cloud.** [Pulumi Deployments drift detection](/docs/deployments/concepts/drift/) runs a preview-only refresh on a cron schedule, shows every run in a Drift tab on the stack, and can send events to Slack or Teams through webhooks. It can also remediate automatically by re-applying your program with `pulumi up --refresh`. Scheduling and remediation need a paid Pulumi Cloud edition (see [choosing an edition](/docs/administration/get-started/choose-edition/)). Pulumi's agent, Neo, includes a drift response workflow described on the [agents page](/docs/ai/agents/).

**Estate visibility with Insights.** Stack refreshes cover resources a Pulumi program declares. [Discovery](/docs/discovery-governance/concepts/discovery/) in Pulumi Insights scans AWS, Azure, Google Cloud, Oracle Cloud, and Kubernetes accounts and builds an inventory of resources regardless of how they were created. Its Managed By column separates resources managed by a Pulumi stack from "Other" resources that no stack manages. [Visual import](/docs/discovery-governance/guides/visual-import/) can generate Pulumi code from discovered resources, and audit policies report violations on discovered resources without blocking anything. This is a different mechanism from stack drift runs: Discovery tells you what exists, and the refresh workflow tells you whether managed resources still match their code.

**Best for:** teams that want one workflow from CLI checks to scheduled runs to estate inventory, and that write infrastructure in general-purpose languages.

**Watch out for:** refresh checks only cover resources a stack declares, so unmanaged resources show up through Discovery as inventory and need a separate adoption step. The CLI checks are open source, while scheduling, auto-remediation, and the Drift tab need a paid Pulumi Cloud edition. Like every tool here, Pulumi sees a console change after it happens.

## How do the tools compare?

| Tool | Detects drift in | How it detects | When drift is found | Status and cost |
|---|---|---|---|---|
| driftctl | Terraform state plus unmanaged resources (AWS, Azure, GCP, GitHub) | CLI run against state and cloud | Reports a summary | Free, maintenance mode, last release December 2023 |
| Terraform / OpenTofu | Declared resources | Plan or refresh-only plan, from CI or HCP Terraform | Shows a diff, exit code 2 | Free CLI; health assessments in HCP Terraform paid editions |
| AWS Config | All supported AWS resources, checked against rules | Continuous recording and rule evaluation | Flags noncompliant, optional Systems Manager remediation | Usage-based AWS pricing |
| Crossplane | Resources defined as managed resources | Continuous reconciliation in a cluster | Reverts to the declared state | Open source, needs Kubernetes |
| Spacelift / env zero | Declared resources | Scheduled plans | Alerts, optional reconcile | Paid tiers for scheduled drift |
| Firefly | Whole estate, including unmanaged | Event hooks and periodic scans | Pull request, codification | Paid plans, 14-day trial |
| Pulumi | Declared resources (refresh); Insights inventories the wider estate separately | CLI refresh, scheduled runs, Discovery scans | Diff, webhooks, auto-remediation, import | Free CLI; scheduled runs and auto-remediation on paid Pulumi Cloud editions |

## Which tool should you start with?

| If you... | Start with |
|---|---|
| Use Terraform or OpenTofu and want a quick check | A scheduled `plan -detailed-exitcode` job |
| Run AWS only and want compliance coverage | AWS Config with a conformance pack |
| Want automatic reverts and already run Kubernetes | Crossplane |
| Manage many Terraform stacks | Spacelift or env zero |
| Have lots of unmanaged resources across tools | Firefly or Pulumi Insights |
| Want CLI checks, scheduled runs, and estate inventory in one platform | Pulumi |
| Have an old driftctl setup | Plan a move, since the project is in maintenance mode |

## Frequently asked questions

### What is infrastructure drift?

Infrastructure drift is any difference between the infrastructure your code defines and the infrastructure running in your cloud account.

### Is driftctl still maintained?

driftctl is in maintenance mode according to its README. The latest release, v0.40.0, shipped in December 2023, and the maintainers invite forks. We found no named successor in the repository as of November 2026.

### How do I detect drift in Terraform?

Run `terraform plan -detailed-exitcode` on a schedule and treat exit code 2 as a drift signal, or use `-refresh-only` to see only changes made outside Terraform. HCP Terraform health assessments schedule this for you in the Standard and Premium editions.

### Can AWS Config detect drift from my Terraform code?

AWS Config evaluates resources against rules and recorded configuration history. It does not read your Terraform or Pulumi code, so it can flag a noncompliant setting but cannot say the resource differs from your program.

### Can any tool prevent drift entirely?

No. Anyone with console access can change a resource. Detection, fast response, least-privilege access, and policy guardrails reduce how often drift occurs and how long it lasts.

### How does Pulumi detect drift?

`pulumi refresh --preview-only` compares each resource's actual configuration with the stack's state and prints the difference without changing anything. Pulumi Cloud adds scheduled runs, a Drift tab, webhooks, and optional automatic remediation, and Insights Discovery inventories resources that no stack manages.

## Where to go next

- Read the [drift detection and remediation concepts](/docs/iac/operations/stack-management/drift/) for the full CLI workflow.
- Set up [scheduled drift runs and remediation](/docs/deployments/concepts/drift/) in Pulumi Cloud.
- See what [Discovery](/docs/discovery-governance/concepts/discovery/) finds in your cloud accounts.
- Read the [Day 2 operations post on drift detection and remediation](/blog/day-2-operations-drift-detection-and-remediation/).
- If you have unmanaged resources to adopt, follow the [import guide](/docs/iac/guides/migration/import/).
