---
title_tag: "Pulumi ESC: Approvals"
meta_desc:  Require explicit review and sign-off before applying changes to ESC-managed environments.
title: Approvals  
h1: Approvals in Pulumi ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: pulumi-esc-admin
    weight: 2
---

{{% notes "info" %}}
Approvals in Pulumi ESC are available for organizations using the Enterprise and Business Critical editions.
Learn more about editions on the [pricing page](/pricing/).
{{% /notes %}}

## Overview

Approvals in Pulumi ESC provide a built-in mechanism for enforcing review and sign-off before applying changes to environment configurations. With Approvals, organizations can ensure that updates to critical configuration values, secrets, and policies are intentional, auditable, and compliant with internal governance requirements.

When Approvals are enabled on an environment, all configuration changes must go through a **change request workflow**. Users propose changes, designated reviewers approve or reject them, and only after the required approvals are granted can changes be applied.

Approvals are configured through rulesets, which define the policies and conditions for reviewing and approving changes in an environment. A ruleset controls who can act as reviewers, how many approvals are needed, and under what circumstances approvals must be re-evaluated. This provides teams with flexible governance tailored to their workflows.

## Why use Approvals?

Teams can use Pulumi ESC Approvals to apply the same rigor of code review workflows to environment configurations and secrets management. Approvals help organizations enforce governance policies, meet compliance requirements, and reduce the risk of misconfigurations by requiring explicit review and sign‑off before applying changes. Each request creates a clear, auditable record of who approved what, when, and why, which is especially valuable for regulated industries or teams with strict change‑management processes.

By introducing a controlled review process, Approvals let developers propose updates while ensuring only authorized reviewers can approve and apply them. This balances collaboration with security and accountability, and works seamlessly in both the Pulumi Cloud console and the ESC CLI.

## How to Enable and Configure Approvals

Approvals in Pulumi ESC are configured at the environment level using **approval rulesets**. A ruleset defines the policies that control how changes are reviewed and approved before being applied.

### Enabling Approvals

1. Navigate to your environment in the Pulumi Cloud console.
2. Go to **Settings → Approval Rulesets**.
3. Click **Create Ruleset** to add a new approval policy, or select an existing ruleset to edit.

### Configuring a Ruleset

When creating or editing a ruleset, you can:

- **Enable or disable the ruleset** to control whether approvals are required.
- **Specify approvers** by adding teams, users, or permissions that grant approval rights.
- **Set the required number of approvals** before a change can be applied.
- **Allow or prevent self‑approval**, determining if the request creator can approve their own changes.
- **Require re‑approval when changes are modified**, ensuring that updates to an approved request must be reviewed again.

Once a ruleset is enabled, direct writes to the environment will be blocked. Instead, users will create **change requests**, which must be reviewed and approved according to the rules you’ve defined. After the required approvals are granted, the changes can be applied to the environment.
