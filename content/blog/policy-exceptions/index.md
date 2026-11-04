---
title: "Policy exceptions: enforce every policy, document every exception"
# TODO(launch-date): set the real publish date before undrafting.
date: 2026-11-03
draft: true
meta_desc: "Make policies mandatory without blocking teams. Policy exceptions exempt specific resources with a reason, optional approval and expiry, and a record."
feature_image: feature.png
authors:
    - alejandro-cotroneo
tags:
    - policy-as-code
    - governance
    - compliance
    - pulumi-cloud
    - features
category: product
schema_type: auto
canonical_url: "https://www.pulumi.com/docs/discovery-governance/concepts/policy-as-code/policy-exceptions/"
related_posts:
    - deployment-guardrails-with-policy-as-code
    - policy-issue-management
    - esc-open-approvals
resource_links:
    - type: documentation
      url: /docs/discovery-governance/concepts/policy-as-code/policy-exceptions/
      text: "Policy exceptions documentation"
    - type: slack
      url: https://slack.pulumi.com/

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Making a policy mandatory usually means fixing every old violation first, or blocking pipelines until someone does.

        Policy exceptions, now in public preview in Pulumi Policies, add a third option. Here's how it works.
    linkedin: |
        Plenty of policies that should be mandatory stay advisory. Turning one on blocks every stack with an old violation, and some violations are intentional: a bucket that hosts a static website has to be public.

        In practice, that leaves workarounds that give up either enforcement or the record: a cloned policy group with one rule turned off, a policy relaxed for one deployment, or a decision in a chat thread that's hard to trace back to the resource.

        Policy exceptions, now in public preview in Pulumi Policies, let you enforce every policy and document every exception. The policy keeps blocking everything an exception doesn't cover, and each exception records who requested it, why, and which resources it covers.

        That changes how early you can make a policy mandatory. Here's how it works, and when to let teams create their own exceptions instead of requiring approval.
    bluesky: |
        A bucket that hosts a static website has to be public. A mandatory policy says it can't be. So the policy stays advisory, and prevents nothing.

        Policy exceptions, now in public preview in Pulumi Policies: enforce every policy, document every exception. Here's how they work.
---

Policy exceptions, now in public preview in [Pulumi Policies](/docs/discovery-governance/concepts/policy-as-code/), let you require policies without blocking teams that have a valid reason to break them. An exception lets specific resources bypass specific policies, with a written reason. You can also require approval and set an expiry. Policies block everything not covered by an exception, while teams can unblock themselves without waiting for a policy change. Each exception records who created it, why, and which resources it covers.

<!--more-->

## Why do mandatory policies stall?

Mandatory policies prevent misconfigurations. Advisory policies only show warnings that busy developers may miss. Mandatory policies stop `pulumi preview` or `pulumi up` before a public bucket or open security group reaches production.

The hard part is turning it on. A new required policy applies to every stack, including resources created before it existed. Some violations are intentional: a bucket hosting a static website must be public, and a log bucket must allow the log delivery group. The policy is still correct; it needs to permit a few known exceptions.

Without a governed way to allow them, what happens in practice is a workaround, and each one gives up either enforcement or the record:

- **Leaving the policy advisory or disabled.** Nothing is blocked, so nothing is prevented.
- **Turning off the policy for a few stacks.** A copied policy group with one rule disabled affects every resource in those stacks, not only the one that needs it, creating more copies.
- **Relaxing the policy for one deployment.** Someone switches it to advisory, deploys, then switches it back. The deployment proceeds, but there’s no record of which resource needed it or why.
- **Keeping the decision elsewhere**, in a chat thread, a ticket, or a spreadsheet that may be difficult to trace back to the resource.

## What changes with policy exceptions?

### Mandatory stays mandatory

An exception is not a weaker enforcement level or a one-time pass for a deployment. It applies only to specified policies and resources. The policy still blocks all other resources, and all other policies still apply to exempted resources. With exceptions, you can make a policy mandatory without first resolving every existing violation.

Exceptions work with any policy pack, including the [pre-built compliance packs](/docs/discovery-governance/guides/pre-built-policy-packs/). Pulumi matches violations against your exceptions, so there's no need to clone or edit a pack.

### Teams unblock themselves, on terms you set

If a deployment hits a violation that the developer can’t fix yet, they can request an exception directly from the pulumi CLI or the failed stack page and explain why. The organization settings decide whether exceptions can be created immediately, with a full audit trail maintained, or require approval from designated people.

An exception can expire. If a team plans to fix a violation, set an expiry to keep the exception temporary. Once it expires, the exception is removed, and the violation blocks again on the next update. Without an expiry, the exception can become part of the policy, so set one whenever a fix is planned.

### Everything is on the record

An exempted violation is still reported. By default, the CLI summarizes exempted violations with the rest of the policy results:

```output
Policies:
    ⚠️ aws-guard@v1.0.0
        - [advisory]  bucket-versioning  (aws:s3:Bucket: logs-bucket)
          Buckets should enable versioning
        · [exempted]  s3-no-public-read  (1 violation)
```

Each exception records its reason, who requested it, the change request that approved it, its expiry, and each policy and resource it applied to. Creating and removing exceptions are recorded in your [audit logs](/docs/administration/concepts/audit-logs/), and removed and expired exceptions remain always accessible. When an auditor asks why a resource is out of policy, the answer is the exception attached to the resource.

## How does it work for each team?

<!-- TODO(edition): confirm edition wording -->

<!-- TODO(decision): the pulumi policy exception commands must ship in a CLI release (pulumi/pulumi#25417) before undrafting. -->

In Pulumi Cloud, exceptions belong to your organization and apply to the policy packs within your [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#preventative-policy-groups). When a preview or update starts, Pulumi Cloud sends the stack's active exceptions to the CLI, so no local configuration is required. Applying them needs Pulumi CLI v3.272.0 or later.

- **Developers** request an exception from the **Policy exceptions** card on the stack's **Overview** page or via the experimental `pulumi policy exception new` command. They select the findings from the stack's latest run, enter a reason, and optionally an expiry. The exception takes effect from the stack's next run, once it's approved if approval is required.
- **Admins** decide whether exceptions require approval, and if so, who approves (organization admins, policy managers, or specific teams and users) and how many approvals a request requires. No one approves their own request unless you allow it.
- **Approvers** review requests on the **Approvals** page, where findings, the reason, and the expiry are all in one place. Approving a request creates the exception.
- **Security and compliance teams** see both active and removed exceptions on a single list, and anyone with permission to remove exceptions can remove one at any time. In the next preview or update, its violations are reported again, and mandatory ones block.

## How do you roll out mandatory policies with exceptions?

With exceptions, you don't have to fix every existing violation before making a policy mandatory. A violation a team can't fix yet costs them an exception request, not a blocked pipeline, so you can enforce sooner.

```mermaid
flowchart LR
    A{"Know what the<br/>policy would flag?"} -->|No| B["Audit policy group:<br/>measure and announce"]
    A -->|Yes| C["Mandatory in a<br/>preventative policy group"]
    B --> C
    C -->|Many expected exceptions| D["No approval:<br/>self-service, audited,<br/>removable any time"]
    C -->|Few, or a sensitive policy| E["Approval required"]
```

Start from where you are:

- **If you don't know what a policy would flag**, add its pack to an audit policy group first. Audit scans report existing violations without blocking anything, so you can see the volume and let teams know what's coming.
- **Otherwise, make the policy mandatory** in a preventative policy group, and choose how exceptions are granted based on how many you expect:
    - **No approval**, when there are many. Developers create their own exceptions with a reason and keep deploying. You still get the full audit trail, and you can remove any exception, so its violations block again from the next update.
    - **Approval required**, when there are few or the policy is sensitive. Each exception waits for a reviewer before it applies.

You can switch between the two at any time. Either way, the policy is mandatory from the start and always documented.

## Can you use exceptions without Pulumi Cloud?

Yes! The Pulumi CLI applies exceptions from a local policy pack config file with any backend. It uses the same matching and reporting as other exceptions. See [exceptions in a local policy pack config file](/docs/discovery-governance/concepts/policy-as-code/policy-exceptions/#exceptions-in-a-local-policy-pack-config-file) for the format.

## Next steps

Policy exceptions are in public preview, and applying exceptions from Pulumi Cloud requires Pulumi CLI v3.272.0 or later. Older versions will ignore the exceptions and report the violations as usual.

- Read the [policy exceptions documentation](/docs/discovery-governance/concepts/policy-as-code/policy-exceptions/) for matching rules, approvals, expiry, and permissions.
- Plan a staged rollout with [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#adopting-policy-across-an-organization).
- Share feedback in the [Pulumi Community Slack](https://slack.pulumi.com/) or on [GitHub](https://github.com/pulumi/pulumi/issues).
