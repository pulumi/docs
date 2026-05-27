---
title_tag: "Detecting and reconciling drift | Pulumi Operations"
meta_desc: Detect when cloud resources diverge from your Pulumi program, then remediate (re-apply code) or adopt (accept reality into state and the program).
title: Detecting and reconciling drift
h1: Detecting and reconciling drift
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Drift detection
        parent: iac-operations-stack-management
        weight: 25
---

Drift is what happens when the state of resources running in your cloud account no longer match the desired state described in your Pulumi program. The most common sources of drift are manual, out-of-band changes made to IaC-managed resources (AKA "click-ops"), or changes made to resources as a natural part of a cloud resource's lifecycle (e.g., DNS domain and load balancer changes resulting from deploying a service to a Kubernetes cluster). This page covers how to detect drift and how to reconcile it in one of two ways: re-applying your program so the cloud matches the desired state code (remediation), or accepting the cloud's state into your program (adoption).

## The three states

Every Pulumi stack has three states that drift discussions hinge on:

1. **Desired state** — what your Pulumi program declares. The code is the source of truth for intent.
1. **Current state** — what Pulumi *believes* exists, recorded in the stack's [state file](/docs/iac/concepts/state-and-backends/). Updated by every successful `pulumi up`, `pulumi refresh`, or `pulumi destroy`.
1. **Actual state** — what *really* exists in the cloud provider right now.

Drift is the gap between actual state and current state: Pulumi's recorded view of the world has fallen out of date. Reconciling drift is the work of closing that gap and, separately, deciding whether the desired state should change to match actual state, or whether actual state should change to match desired state.

## Detecting drift

[`pulumi refresh --preview-only`](/docs/iac/cli/commands/pulumi_refresh/) is the canonical way to detect drift from the CLI. The command queries each resource's provider for its actual configuration, compares the response to the stack's current state, and prints a diff. It does not modify the state file and does not change any cloud resources.

```bash
pulumi refresh --preview-only --stack production
```

Read the output the same way you read a `pulumi preview`: each `~` is a property that has drifted, `-` is a resource the provider says no longer exists, and `+` is a resource Pulumi did not know about (rare without imports). If the output is empty, the stack is not drifted.

`pulumi refresh` without `--preview-only` performs the same query but writes the results back into the state file. Do not run it until you have decided which direction you want to reconcile.

To turn detection into a hard signal (useful in CI, where you want the build to fail when drift exists), add the `--expect-no-changes` flag:

```bash
pulumi refresh --preview-only --expect-no-changes --stack production
```

With `--expect-no-changes`, the command exits with a non-zero status if any drift is detected. The exit code is what your CI job, alerting hook, or shell script keys off of to decide whether to page someone. Because `--preview-only` is set, no state is mutated either way.

## Choosing a direction: remediation vs. adoption

Drift detection tells you the cloud and your program disagree. Reconciling that disagreement always means changing one side to match the other, in one of two directions:

- **Remediation** — change the *cloud* to match the *code*. Run `pulumi up`, and Pulumi pushes your program's desired state back onto the cloud, undoing the out-of-band change. Use this when the drift is unwanted: an emergency edit that should not have happened, an unauthorized change, a configuration that violates policy.
- **Adoption** — change the *code* and the *state* to match the *cloud*. Run `pulumi refresh` to write reality into the state file, then edit your program so it describes the new reality. Use this when the drift is correct: a deliberate change someone made in a hurry, a configuration that should have been in the code all along, or a managed-service mutation you want to preserve.

The risk profiles differ sharply. Remediation acts immediately: the next `pulumi up` undoes the out-of-band change, which means whatever business reason drove that change disappears too. Adoption is slower and safer for the running infrastructure, but leaves the program out of sync until you finish the code edit; if you forget, the next person who runs `pulumi up` will see drift again.

When in doubt, adopt first (it's reversible: you can always run `pulumi up` later) and decide whether to keep the change once you understand the reason behind it.

### Drift from humans (or agents acting on their behalf)

When drift comes from a human (or an AI agent that ran on a human's behalf) rather than an automated cloud-side process, find out why before deciding what to do about it. A few of the common cases:

- **They were debugging an incident.** The change was a workaround made under pressure: they may not have had time to wait for a pipeline to run or for a PR to get reviewed. Don't revert it until the underlying problem is fully fixed and the incident is closed. Afterward, the right move is often to incorporate the workaround (or a better version of it) into the program so the next incident doesn't require the same fix.
- **They didn't know the resource was managed by IaC.** They had access, they saw a problem, they fixed it. This is a good opportunity to walk them through the project: where the program lives, how to propose changes, and what the review process looks like. Running through an adoption PR with them is a good way to socialize how IaC works in your organization.
- **They were working around a missing capability.** They needed a tag, a config option, or a feature flag that the program doesn't expose. Adopt the change and add the missing capability to the program. If the program is part of a shared platform that other teams consume, treat the drift as product feedback: a user hit a gap in the platform and worked around it, which is signal you can use to plan a fix. Platforms do best when treated as internal products, with users, a roadmap, and a real feedback loop.

### Drift from automated processes

Drift from a non-human source (autoscaling, managed-service rotation, scheduled cloud-side updates, security tooling, cost-optimization tools) is more deterministic than human drift, but the decision isn't always "ignore it." A few common categories:

- **Ignore it.** The cloud legitimately owns the property: autoscaling group `desiredCapacity` changes with load, last-modified timestamps tick, a managed service rotates a value on its own schedule. Add [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/) for the property and move on.
- **Adopt it.** External tooling makes mutations that should be reflected in your program: a security tool adds compliance tags, a cost-optimization tool rightsizes an instance, a key-rotation system updates a secret. The change is correct and should stay, but adding `ignoreChanges` would be the wrong move because the tooling's behavior is something you want to track in code. Adopt the drift and update the program (or add a config option) so the relationship between the program and the external tool is explicit.
- **Remediate it.** An automated process changed something it shouldn't have. A misconfigured Lambda flipped a flag, a deprecated cron is still running, a third-party integration regressed. Remediate, then figure out where the unwanted change is coming from.

The decision process mirrors the human-drift one: figure out why the change happened before deciding what to do. Logs, audit trails, and provider-side audit events (e.g., AWS CloudTrail, Azure Activity Log, Google Cloud Audit Logs) tell you what made the change. From there it's a matter of deciding whether the system should keep making it, and whether the program should track it.

{{% notes type="info" %}}
If you need to ship updates to other resources before deciding what to do with the drift, you can scope `pulumi up` to leave the drifted resource alone. [Targeted updates](/docs/iac/operations/stack-management/targeted-updates/) accept either an allowlist (`--target` plus the URNs to update) or a denylist (`--exclude` plus the URNs to skip). When you're working around a single drifted resource, `--exclude` is the cleaner choice; when you have a small, known set of resources to update, `--target` works better.
{{% /notes %}}

## The remediation workflow

When the drift is unwanted, the workflow is:

1. **Detect.** `pulumi refresh --preview-only`. Confirm the drift is what you expect.
1. **Preview the remediation.** `pulumi preview --refresh`. The `--refresh` flag refreshes state first, then shows what `pulumi up` would do to put the cloud back on the program's path.
1. **Apply.** `pulumi up --refresh`. This refreshes state, then reconciles every drifted resource by pushing the program's desired state back to the cloud.

Do not skip the preview. Remediation can replace resources: if an out-of-band change touched an immutable property, Pulumi will delete and recreate the resource to restore the declared configuration. Knowing that ahead of time is the difference between a routine remediation and an outage.

## The adoption workflow

When the drift is desired and should stay, adoption is a two-step job: edit state, then edit code. Both steps are required. Stopping after the first leaves your program describing a reality it no longer reflects.

1. **Detect.** `pulumi refresh --preview-only`. Confirm the drift is what you want to keep.
1. **Adopt into state.** `pulumi refresh`. The state file now matches the cloud.
1. **Adopt into the program.** Edit the relevant resource declarations so the program describes the new configuration.
1. **Verify.** `pulumi preview`. The preview should be empty (desired, current, and actual are aligned again).
1. **Commit and merge** the code change.

The third step is the one most often skipped. Without it, the next refresh will look clean but the next `pulumi up` from a freshly cloned repo (CI, a new teammate, a different stack reusing the same program) will undo the change, because the program still describes the *old* configuration. The state-file edit alone is not adoption: it's a half-finished migration.

### Adoption with Pulumi Neo

The code-edit step is the slowest part of adoption: it's tedious to translate a diff full of provider properties back into your program, and it's where most "I'll do it later" abandonments happen. [Pulumi Neo](/docs/ai/) is built for this: hand it the stack and the drift, and it will run the refresh, read the resulting diff, edit the program so it matches, run a clean preview, and open a pull request for you to review.

A task description as direct as *"Adopt the drift on the `production` stack into the program"* is enough to get Neo started. By default Neo runs in [Review mode](/docs/ai/tasks/#task-modes), so the `pulumi up` and the PR both require your approval before they happen: you stay the decision-maker on what gets merged. For large or unfamiliar codebases, enable [Plan Mode](/docs/ai/tasks/#plan-mode) so Neo investigates the program and proposes its approach before making any changes.

Neo doesn't change the mechanics of adoption: the program still has to be updated to match reality, and the PR still has to be reviewed. What changes is the cost of getting there: Neo absorbs the tedium that makes adoption the slower of the two reconciliation paths.

## Scheduling drift checks

Detect drift on every important environment, regardless of how (or whether) you plan to reconcile it. Even when the policy is "always remediate" and a continuous reconciliation job is doing it for you, having a record of what drifted and when is useful for audits, post-incident review, and spotting patterns (e.g., the same resource drifting every week because of a forgotten manual process).

For production, wire drift detection to an alert channel: Slack, email, or a ticket queue, depending on where your team checks during business hours. How urgent the alert should be depends on what kind of drift you're seeing.

Drift that matches a known pattern (a security tool adds tags, a managed service rotates a value, autoscaling adjusts capacity) is routine. File it in a daily review queue and batch the response. Drift you can't immediately explain is its own incident, separate from whatever you eventually decide to do with the diff; treat it as a high-priority notification and drop other work to investigate.

Reserve paging for the narrow set of resources where drift is itself a security or compliance incident (e.g., security group rules on a regulated workload, IAM policies, KMS key bindings), and route those alerts to your on-call system separately. For everything else, remediating when the on-call engineer starts work is rarely worse than remediating it at 2 AM.

Manual `pulumi refresh --preview-only` works for small teams but doesn't scale. Two paths to run it on a schedule:

- **CI/CD cron.** Most CI systems support scheduled workflows. A drift-detection job runs `pulumi refresh --preview-only --expect-no-changes` against each stack: if drift is detected, the command exits non-zero and the job fails, which alerts the channel you've wired to job failures. The GitHub Actions trigger looks like:

    ```yaml
    on:
      schedule:
        - cron: "0 6 * * *"
    ```

    Run it as often as the SLA on drift remediation requires. Hourly for production, daily for staging is a common starting point.

- **Pulumi Deployments.** [Deployments](/docs/deployments/deployments/) runs scheduled drift jobs against your stacks and can either stop at detection (a preview-only refresh that surfaces the diff in the [Drift tab](/docs/deployments/deployments/drift/)) or remediate automatically by running `pulumi up --refresh` after the detection run. [Webhooks](/docs/deployments/webhooks/) fire on every drift event (`drift_detected`, `drift_detection_succeeded`, `drift_detection_failed`, `drift_remediation_succeeded`, `drift_remediation_failed`), so you can route notifications to Slack, Microsoft Teams, PagerDuty, or any HTTP endpoint without writing a custom polling loop. This is the lowest-friction option if you're already on Pulumi Cloud.

## Resource options for safer drift handling

Three resource options let you tell Pulumi which properties it owns and which resources should never be replaced, even when drift would trigger one. Use them to keep remediation from doing damage:

- [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/) — tell Pulumi that specific properties are managed outside the program. Pulumi will keep using the recorded state value for those properties during an update rather than the program value, so `pulumi up` won't try to push the program's value back over the external change. This is what you want for autoscaling counts, server-assigned IDs, tags maintained by external tooling, and other values the cloud (or another system) legitimately owns.
- [`protect`](/docs/iac/concepts/resources/options/protect/) — block Pulumi from deleting or replacing a resource at all. This is the most important safeguard against destructive remediation: even if drift on an immutable property would trigger a replacement, `protect` makes Pulumi refuse rather than risk data loss. Use it on production databases, persistent volumes, long-lived buckets, or anything where "we lost the data" is unacceptable.
- [`deleteBeforeReplace`](/docs/iac/concepts/resources/options/deletebeforereplace/) — for resources whose name is hard-coded (no auto-naming), tell Pulumi to delete the old resource before creating its replacement. Without this, the create-then-delete default will fail on a name conflict if drift remediation forces a replacement, leaving the stack in a broken half-applied state.

Mark the properties the cloud or external tooling owns as `ignoreChanges`, and put `protect` on anything that must not be destroyed. `pulumi refresh --preview-only` will then report only the drift you want to act on, and `pulumi up` will refuse to touch the resources you've fenced off.

## Reducing drift over time with components and policy

Operational drift handling (detect, decide, reconcile) is the short loop. The long loop is making drift less likely in the first place by codifying best practices into the IaC layer, so that doing the right thing requires the least effort. Three Pulumi capabilities support this:

- **[Components](/docs/iac/concepts/components/)** package related resources and their configuration into a single, reusable building block. When platform teams expose a `StandardBucket` component that bakes in tagging, encryption, lifecycle policy, and access controls, developers don't hand-write those properties. They use the component, inherit the right defaults, and have fewer reasons to "fix it in the console later." Components also make adoption of upstream changes straightforward: update the component once, and the next refresh-and-update cycle propagates the fix to every consumer.
- **[Pulumi IDP](/docs/idp/)** turns components, [templates](/docs/idp/concepts/organization-templates/), and a [private registry](/docs/idp/concepts/private-registry/) into a self-service platform that platform teams curate and developers consume. When the golden path is also the path of least resistance, developers don't go around it. Most drift starts when the program doesn't expose what someone needs, or when scaffolding a new service costs more than reaching for the console; IDP closes those gaps.
- **[Pulumi Policy](/docs/insights/policy/)** enforces guardrails at preview time in **Preventative** mode and, against the live cloud, in **Audit** mode — continuously scanning resources discovered through [Pulumi Insights](/docs/insights/) Discovery. Policy matters most when paired with drift handling: it prevents adoption from quietly normalizing a non-compliant change. If a teammate opens a 0.0.0.0/0 ingress in the console and the team decides to adopt the change, a policy that requires private CIDR ranges blocks the PR rather than letting the bad configuration enter the program. Policy in Audit mode also catches drift-introduced compliance violations in production even when no one runs a refresh.

None of these prevent drift on their own. They reduce the rate at which it happens, narrow the kinds of changes that produce it, and prevent the adoption path from quietly degrading the program over time.

## GitOps and continuous reconciliation

The strongest form of drift control is to remediate it in a loop, with no human in the path. In a GitOps setup, a controller watches the git repository and runs `pulumi up --refresh` (or its equivalent) on a fixed cadence, so the cloud matches the program at all times. Out-of-band changes are typically reverted within minutes.

There are two common patterns to set this up with Pulumi:

- **Pulumi Kubernetes Operator.** The [operator](https://github.com/pulumi/pulumi-kubernetes-operator) can be configured with `refresh: true`, `continueResyncOnCommitMatch: true`, and a `resyncFrequencySeconds` value to run `pulumi up --refresh` on a tight loop, regardless of whether the source code has changed.
- **CI/CD cron.** Schedule a job that runs `pulumi up --refresh` on a regular cadence. Combine with [`protect`](/docs/iac/concepts/resources/options/protect/) on resources that must never be deleted, since automated remediation will otherwise replace them if an immutable property has drifted.

The appeal is straightforward: declared state and actual state never diverge for long, audit trails are clean, and out-of-band changes become self-correcting. The fit is narrower than the appeal suggests. Continuous reconciliation works well only when:

- **Environments are highly consistent.** The program describes everything the environment needs and nothing it doesn't. Any property the cloud legitimately owns (autoscaling counts, dynamic IPs, managed-service-rotated values) needs an explicit `ignoreChanges`, or the loop will fight with the cloud indefinitely.
- **Out-of-band changes are genuinely rare, including during incidents.** If on-call engineers regularly need to make emergency changes through the console (to mitigate an outage, unblock a deploy, change a feature flag in a hurry), a tight reconciliation loop will erase their fix while they're still typing the post-incident message. Continuous reconciliation only works in environments where the program is the only acceptable way to change infrastructure, even under pressure.
- **The blast radius of accidental reconciliation is well understood.** A misconfigured loop can destroy a database, revoke a critical IAM role, or replace a resource that wasn't supposed to be replaceable. Pair with `protect` on stateful resources, and run the loop against staging for a long time before turning it on for production.

For most teams, scheduled detection plus human-driven remediation is the safer default. Reach for continuous reconciliation only in environments where the assumptions above hold.

## See also

- [`pulumi refresh`](/docs/iac/cli/commands/pulumi_refresh/) and [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) CLI references.
- [Pulumi Cloud drift detection](/docs/deployments/deployments/drift/) — managed scheduling, the Drift tab, and auto-remediation.
- [Pulumi Neo tasks](/docs/ai/tasks/) — let Neo handle the code-edit step of adoption.
- [Pulumi Kubernetes Operator](https://github.com/pulumi/pulumi-kubernetes-operator) — continuous reconciliation for Kubernetes-hosted stacks.
- [Targeted updates](/docs/iac/operations/stack-management/targeted-updates/) — partial updates are a common source of drift between code and infrastructure.
- [Update plans](/docs/iac/operations/stack-management/update-plans/) — preview-and-approve workflow that pairs well with adoption.
- [Components](/docs/iac/concepts/components/), [Pulumi IDP](/docs/idp/), and [Pulumi Policy](/docs/insights/policy/) — codify best practices to reduce the rate at which drift is introduced.
- Resource options: [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/), [`protect`](/docs/iac/concepts/resources/options/protect/), [`deleteBeforeReplace`](/docs/iac/concepts/resources/options/deletebeforereplace/).
