---
title: What Is Infrastructure Drift?
meta_desc: "Infrastructure drift is when live cloud resources diverge from your IaC code. Learn what causes it, how to detect it, and how to reconcile it safely."
type: what-is
date: 2026-07-07T15:30:27-07:00
page_title: "What Is Infrastructure Drift?"
authors: ["alex-leventer"]
---

**Infrastructure drift is the gap that opens when the cloud resources running in your account no longer match the desired state described in your infrastructure as code. It happens when someone changes a resource out-of-band—through the console, a CLI, or an automated process—so what's actually deployed diverges from what your code says should exist.** Left undetected, drift erodes the core promise of IaC: that your code is a reliable description of your infrastructure.

Drift is not a bug in your tooling. It's a natural consequence of running real infrastructure where more than one actor can make changes—a human debugging an incident, a managed service rotating a credential, an autoscaler adjusting capacity. The question is never whether drift will occur, but whether you'll detect it and decide, deliberately, what to do about it.

In this article, we'll cover the key questions about infrastructure drift:

* What is infrastructure drift?
* What causes infrastructure drift?
* Why does infrastructure drift matter?
* How do you detect drift?
* How do you reconcile drift?
* How do you prevent drift?
* How does Pulumi handle drift?
* Frequently asked questions about infrastructure drift

## What is infrastructure drift?

To understand drift precisely, it helps to name the three states that every [infrastructure as code](/what-is/what-is-infrastructure-as-code/) stack tracks:

1. **Desired state** — what your program declares. The code is the source of truth for intent.
1. **Current state** — what your IaC tool *believes* exists, recorded in a state file. It's updated by every successful deploy, refresh, or destroy.
1. **Actual state** — what *really* exists in the cloud provider right now.

Drift is the gap between actual state and current state: your tool's recorded view of the world has fallen out of date because something changed the cloud without going through your code. When the three states agree, there is no drift. When actual state diverges from what the tool recorded, the stack has drifted, and every assumption built on "the code describes reality" is now suspect.

This is distinct from a pending change you haven't applied yet. If you edit your program but haven't deployed, desired state and actual state differ by design—that's a planned update, not drift. Drift is specifically the *unrecorded* divergence: a change to the live environment that your IaC tool didn't make and doesn't know about.

## What causes infrastructure drift?

Drift comes from two broad sources, and telling them apart is the first step in deciding what to do.

**Human, out-of-band changes.** Someone with cloud access makes a change directly—through the console ("click-ops"), a cloud CLI, or a script—rather than through the IaC program. The classic cases:

* An on-call engineer edits a security group or scales a database under incident pressure, when waiting for a pipeline and a PR review isn't an option.
* Someone fixes a problem without realizing the resource was managed by IaC at all.
* A developer works around a capability the program doesn't expose—a tag, a config option, a feature flag—by setting it directly in the console.

**Automated, cloud-side changes.** Non-human processes mutate resources as part of normal operation:

* Autoscaling changes an autoscaling group's desired capacity as load shifts.
* A managed service rotates a secret, certificate, or key on its own schedule.
* External tooling—a security scanner adding compliance tags, a cost-optimization tool rightsizing an instance—modifies resources you manage.

The distinction matters because the right response differs. A managed service legitimately owning a property is something you learn to ignore; an unauthorized human change to an IAM policy is a potential security incident. The same phenomenon—drift—can be routine noise or a five-alarm fire depending on its source.

## Why does infrastructure drift matter?

Drift undermines the guarantees that make IaC valuable in the first place.

**It breaks the reliability of your code as documentation.** The whole point of IaC is that the program is an accurate, reviewable description of your infrastructure. Once drift accumulates, that's no longer true—and no one can trust the code to answer "what's actually running?"

**It turns routine deployments into hazards.** When you finally run a deploy against a drifted stack, the tool reconciles based on stale state. A property someone changed by hand gets silently reverted; worse, if the out-of-band change touched an immutable property, the tool may delete and recreate the resource to restore the declared configuration—a routine update becomes an outage.

**It hides security and compliance regressions.** A security group opened to `0.0.0.0/0` in the console, an encryption setting flipped off, an IAM policy widened—these are exactly the changes that drift silently and that matter most. Without detection, a compliant environment quietly becomes a non-compliant one, and no one knows until an audit or an incident.

**It compounds.** The longer drift goes unnoticed, the more infrastructure gets built on top of the diverged resource, and the larger the blast radius of eventually reconciling it. Small, frequent detection keeps that blast radius small.

The stakes rise as more infrastructure changes flow through automation. As [AI agents increasingly provision and modify infrastructure](/what-is/what-is-agentic-infrastructure/), the ability to detect when reality has diverged from code—and to reconcile it deliberately—becomes a core safety mechanism, not an operational nicety.

## How do you detect drift?

Detection means asking the cloud provider what actually exists and comparing the answer to what your tool recorded. In Pulumi, the canonical command is a preview-only refresh:

```bash
pulumi refresh --preview-only --stack production
```

This queries each resource's provider for its live configuration, compares the response to the stack's recorded state, and prints a diff—without modifying the state file or touching any cloud resource. You read the output the way you'd read any preview: a `~` marks a property that has drifted, a `-` marks a resource the provider says no longer exists, and a `+` marks one the tool didn't know about. Empty output means no drift.

To turn detection into a hard pass/fail signal—useful in CI, where you want a scheduled job to fail loudly when drift appears—add `--expect-no-changes`:

```bash
pulumi refresh --preview-only --expect-no-changes --stack production
```

Now the command exits non-zero if any drift is found, and your CI job, alert hook, or shell script can key off the exit code. Because `--preview-only` is set, nothing is mutated either way.

Detection is only useful if it runs on a schedule. Manual checks work for a handful of stacks but don't scale. Two common approaches:

* **CI/CD cron.** Most CI systems support scheduled workflows. A job runs the preview-only refresh against each stack on a cadence—hourly for production, daily for staging is a common starting point—and alerts the channel you've wired to job failures.
* **Managed drift detection.** [Pulumi Deployments](/docs/deployments/concepts/drift/) runs scheduled drift jobs for you, surfaces diffs in a Drift tab, and fires [webhooks](/docs/deployments/concepts/webhooks/) on every drift event so you can route notifications to Slack, PagerDuty, or any HTTP endpoint without writing a polling loop.

## How do you reconcile drift?

Detection tells you the cloud and your code disagree. Reconciling that disagreement always means changing one side to match the other, and there are exactly two directions:

**Remediation — change the cloud to match the code.** You re-apply your program, pushing the declared desired state back onto the cloud and undoing the out-of-band change. This is the right move when the drift is *unwanted*: an unauthorized change, an emergency edit that shouldn't persist, a configuration that violates policy. Remediation acts immediately—which means whatever business reason drove the original change disappears with it, so preview first. If a drifted immutable property would force a replacement, you want to know before you run it.

**Adoption — change the code to match the cloud.** You accept reality into your state file, then edit your program so it describes the new configuration. This is the right move when the drift is *correct*: a deliberate fix someone made in a hurry, a managed-service mutation worth preserving, a setting that should have been in the code all along. Adoption is safer for the running infrastructure but has a trap: the state edit alone isn't enough. If you don't finish the job by updating the program, the next deploy from a fresh checkout will reintroduce the drift, because the code still describes the old configuration.

When in doubt, adopt first—it's reversible—and decide whether to keep the change once you understand why it happened. And before deciding either way, find out *what* made the change: provider-side audit logs (AWS CloudTrail, Azure Activity Log, Google Cloud Audit Logs) tell you who or what touched the resource, which usually tells you which direction to reconcile.

## How do you prevent drift?

You can't eliminate drift, but you can lower the rate at which it happens and blunt its impact.

**Tell your tool which properties it doesn't own.** Some drift is legitimate and perpetual—an autoscaler will always adjust capacity, a managed service will always rotate its secret. Pulumi's [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/) resource option marks those properties as externally managed, so a refresh reports only the drift you actually want to act on and a deploy won't fight the cloud over them.

**Fence off what must never be destroyed.** The [`protect`](/docs/iac/concepts/resources/options/protect/) option blocks deletion or replacement of a resource entirely. It's the most important safeguard against destructive remediation: even if drift on an immutable property would trigger a replacement, `protect` makes the tool refuse rather than risk data loss on a production database or a long-lived bucket.

**Codify the golden path.** Most drift starts when the program doesn't expose what someone needs, or when reaching for the console is easier than changing the code. [Components](/docs/iac/concepts/components/) package best-practice defaults (tagging, encryption, access controls) into reusable building blocks so developers inherit the right configuration instead of hand-rolling it and fixing it later. A self-service [internal developer platform](/what-is/what-is-an-internal-developer-platform/) makes that golden path the path of least resistance.

**Enforce guardrails that survive adoption.** [Policy as code](/what-is/what-is-policy-as-code/) matters most when paired with drift handling. If a teammate opens a `0.0.0.0/0` ingress in the console and the team moves to adopt it, a policy requiring private CIDR ranges blocks the PR rather than letting the bad configuration quietly enter the program. Policy run in audit mode also catches drift-introduced compliance violations in production even when no one runs a refresh.

**Reconcile continuously, where it fits.** The strongest form of drift control is a [GitOps](/docs/iac/operations/stack-management/drift/) loop: a controller re-applies the program on a fixed cadence, so out-of-band changes are reverted within minutes. This works beautifully in highly consistent environments where the program is the *only* acceptable way to change infrastructure—and poorly where on-call engineers regularly make emergency console changes, since the loop will erase their fix while they're still typing. For most teams, scheduled detection plus human-driven remediation is the safer default.

## How does Pulumi handle drift?

Pulumi treats drift as a first-class part of the stack lifecycle rather than an afterthought, with support at every step from detection to reconciliation:

* **Detection** via [`pulumi refresh --preview-only`](/docs/iac/cli/commands/pulumi_refresh/) from the CLI, or scheduled, managed detection through [Pulumi Deployments](/docs/deployments/concepts/drift/) with a Drift tab and event webhooks.
* **Reconciliation** in either direction: remediate with [`pulumi up --refresh`](/docs/iac/cli/commands/pulumi_up/), or adopt by refreshing state and updating the program.
* **Guardrails** through resource options ([`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/), [`protect`](/docs/iac/concepts/resources/options/protect/)) and [Pulumi Policy](/docs/insights/policy/) enforcement that spans both preview-time prevention and audit of live resources.

The code-edit step of adoption—translating a provider-property diff back into your program—is the slowest and most-abandoned part of the whole workflow. [Pulumi Neo](/product/neo/), the AI infrastructure agent built into Pulumi Cloud, is designed for exactly this: hand it a drifted stack and it runs the refresh, reads the diff, edits the program to match, runs a clean preview, and opens a pull request for your review. It doesn't change the mechanics—the program still has to be updated and the PR still has to be approved—but it absorbs the tedium that makes adoption the slower reconciliation path.

For the complete, step-by-step workflows, see [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/) in the Pulumi docs.

## Frequently asked questions about infrastructure drift

### What is infrastructure drift in simple terms?

Infrastructure drift is when the cloud resources you're actually running stop matching the infrastructure as code that's supposed to define them. Someone or something changed a resource outside your IaC workflow—usually through a console click or an automated cloud process—so your code no longer describes reality.

### What causes configuration drift?

Two main sources: manual, out-of-band changes (an engineer editing a resource directly in the console or CLI, often during an incident) and automated cloud-side changes (autoscaling adjusting capacity, a managed service rotating a secret, external tooling modifying tags or sizing). Human drift needs investigation into *why* it happened; automated drift is more predictable but still requires a decision about whether to track it in code.

### How do you detect infrastructure drift?

Query the cloud provider for each resource's live configuration and compare it against what your IaC tool recorded. In Pulumi, `pulumi refresh --preview-only` prints the diff without changing anything; adding `--expect-no-changes` makes the command exit non-zero when drift exists, which turns it into a pass/fail signal for a scheduled CI job or alert. Managed options like Pulumi Deployments run this detection on a schedule and surface the results for you.

### How do you fix infrastructure drift?

You reconcile it in one of two directions. *Remediation* re-applies your code to push the cloud back to the declared state—use it when the change was unwanted. *Adoption* updates your state file and your program to match the cloud—use it when the change was correct and should stay. Always preview a remediation first, because reverting a change to an immutable property can force the tool to delete and recreate the resource.

### What's the difference between drift and a normal pending change?

A pending change is a difference between your code and the cloud that *you created on purpose* by editing the program and haven't deployed yet—your tool knows about it. Drift is an *unrecorded* difference: a change made to the live cloud that your tool didn't make and doesn't know about, so its recorded state is now wrong.

### Can you prevent infrastructure drift entirely?

Not entirely—any environment where more than one actor can change resources will drift eventually. But you can reduce it and control its impact: mark cloud-owned properties with `ignoreChanges`, protect resources that must never be destroyed, codify best practices into reusable components and a self-service platform so the console is rarely the easy path, enforce policy that blocks non-compliant changes from being adopted, and, where the environment allows, run a continuous [GitOps](/what-is/what-is-gitops/) reconciliation loop.

### Is infrastructure drift a security risk?

It can be. Some of the most consequential drift is exactly the security-relevant kind—an ingress rule opened to the internet, encryption disabled, an IAM policy widened. Because these changes bypass code review, they escape the usual controls. This is why detection should run continuously on sensitive environments, and why policy-as-code enforcement in audit mode is valuable: it flags drift-introduced compliance violations even when no one has run a refresh.

## Learn more

Pulumi detects, reconciles, and helps prevent infrastructure drift across any cloud—CLI-driven refresh and remediation, managed scheduled detection in Pulumi Deployments, and AI-assisted adoption with Pulumi Neo. [Read the drift detection and reconciliation guide](/docs/iac/operations/stack-management/drift/) to see the full workflow.

Related reading:

* [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/)
* [Pulumi Cloud drift detection](/docs/deployments/concepts/drift/)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is policy as code?](/what-is/what-is-policy-as-code/)
* [What is agentic infrastructure?](/what-is/what-is-agentic-infrastructure/)
* [What is an internal developer platform?](/what-is/what-is-an-internal-developer-platform/)
