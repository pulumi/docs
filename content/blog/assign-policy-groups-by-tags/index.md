---
title: "Assign policy groups by stack and account tags"
date: 2026-10-19
draft: false
meta_desc: "Policy groups can now add stacks and cloud accounts by tag, so new infrastructure gets the right policy coverage automatically as it's created."
feature_image: feature.png
authors:
    - dan-biwer
tags:
    - policy-as-code
    - governance
    - compliance
    - features
# Required: exactly one category (a scalar) from the closed set in
# data/blog_categories.yaml. Use "general" for posts that don't clearly fit a
# specific kind. Validated by `make lint`.
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Every new Pulumi stack used to need someone to add it to the right policy group by hand. Miss one, and that production stack isn't covered by your production policies.

        That step is now optional. Here's how it works.
    linkedin: |
        Policy groups decide which policy packs apply to which Pulumi stacks and cloud accounts. Until now, every stack and account had to be added to a group by hand.

        That works until someone creates a new production stack and nobody remembers to add it to the production group.

        We changed how stacks and accounts join a policy group, so nobody has to edit the group when a new one appears.

        We wrote up how it works, with examples for production stacks and PCI-scoped cloud accounts.
    bluesky: |
        Pulumi policy groups can now find their own members, so new stacks get the right policies without anyone editing the group.

        The same works for cloud accounts in audit groups. Here's how it works.
---

[Policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) decide which [policy packs](/docs/discovery-governance/concepts/policy-as-code/policy-packs/) apply to which stacks and cloud accounts. Until now, stacks and accounts were added to policy groups individually, so every new stack required opting into their correct group by hand. Policy groups membership can now be managed by tags, so new infrastructure gets the right policy coverage automatically as it's created.

<!--more-->

## What's new

Policy groups now support tag matching conditions. Every stack or cloud account whose tags match the condition joins the group, and membership stays current as tags change. Tag rules work alongside the stacks and accounts you add individually, so you can adopt them without restructuring your existing groups.

To add one, open a policy group in Pulumi Cloud and select **Match by tags**.

![Adding a tag rule that matches stacks and accounts tagged env: prod, with a preview of the matching entities](add-tag-rule.png)

Or define it in code with the [Pulumi Service Provider](/registry/packages/pulumiservice/):

```typescript
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.api.PolicyGroup("payments-production", {
    orgName: "my-org",
    name: "payments-production",
    mode: "preventative",
    stackMatchRule: pulumiservice.buildStackMatchRuleOutput({
        rules: [{ conditions: [{ key: "env", value: "prod" }, { key: "team", value: "payments" }] }],
    }).matchRule,
});

new pulumiservice.api.PolicyGroup("pci-accounts", {
    orgName: "my-org",
    name: "pci-accounts",
    mode: "audit",
    accountMatchRule: pulumiservice.buildAccountMatchRuleOutput({
        rules: [{ conditions: [{ key: "env", value: "prod" }, { key: "compliance", value: "pci" }] }],
    }).matchRule,
});
```

## Example: enforcement by environment

A common pattern is one policy group per environment tier, with stricter enforcement in production:

- A **production** preventative group with a rule matching `env: prod`, where critical policies are `mandatory`.
- A **development** preventative group with a rule matching `env: dev`, where the same packs are `advisory`.

A new stack tagged `env: prod` joins your production policy group automatically, with no one editing the group. The same approach works for audit groups and cloud accounts, for example matching accounts tagged `compliance: pci` to an audit group running a [PCI DSS policy pack](/docs/discovery-governance/guides/pre-built-policy-packs/).

## Get started

Tag rules are available now in Pulumi Cloud. To learn more, see [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#tag-rules).
