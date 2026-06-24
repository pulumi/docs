---
title_tag: "Pulumi ESC: Approvals"
meta_desc:  Require explicit review and sign-off before applying changes or opening ESC-managed environments.
title: "Approvals"
h1: Approvals in Pulumi ESC
meta_title: Approvals in Pulumi ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-concepts
    weight: 11
  administration:
    name: ESC Approvals
    parent: administration-security-compliance
    weight: 10
aliases:
  - /docs/esc/administration/approvals/
  - /docs/esc/operations/approvals/
---

{{% notes "info" %}}
Approvals in Pulumi ESC are available for organizations using the Enterprise and Business Critical editions.
Learn more about editions on the [pricing page](/pricing/).
{{% /notes %}}

## Overview

Approvals in Pulumi ESC provide a built-in mechanism for enforcing review and sign-off before critical actions are performed on environments. With Approvals, organizations can control both configuration changes and environment access, ensuring that actions are intentional, auditable, and compliant with internal governance requirements.

Pulumi ESC supports two types of approvals:

- **Update approvals**: Require review before modifying an environment.
- **Open approvals**: Require review before granting access to open an environment and view its secrets and credentials.

When approvals are enabled on an environment, users must go through a **request workflow**. Users submit requests, designated reviewers approve or reject them, and only after the required approvals are granted can the requests be applied.

Approvals are configured through rulesets, which define the policies and conditions for reviewing and approving requests. A ruleset controls who can act as reviewers, how many approvals are needed, and under what circumstances approvals must be re-evaluated. This provides teams with flexible governance tailored to their workflows.

## Why use approvals?

Teams can use Pulumi ESC approvals to apply the same rigor of code review workflows to environment configurations and access management. Approvals help organizations enforce governance policies, meet compliance requirements, and reduce risk by requiring explicit review and sign-off. Each request creates a clear, auditable record of who approved what, when, and why, which is especially valuable for regulated industries or teams with strict change-management processes.

By introducing a controlled review process, approvals let users submit requests while ensuring only authorized reviewers can approve and apply them. This balances collaboration with security and accountability, and works seamlessly in both the Pulumi Cloud console and the Pulumi CLI.

## How to Enable and Configure Approvals

Approvals in Pulumi ESC are configured at the environment level using **approval rulesets**. A ruleset defines the policies that control how changes are reviewed and approved before being applied.

### Enabling Approvals

1. Navigate to your environment in the Pulumi Cloud console.
1. Go to **Settings → Approval Rulesets**.
1. Click **Create Ruleset** to add a new approval policy, or select an existing ruleset to edit.

### Configuring a ruleset

When creating or editing a ruleset, you can:

- **Enable or disable the ruleset** to control whether approvals are required.
- **Specify approvers** by adding teams, users, or permissions that grant approval rights.
- **Set the required number of approvals** before a change can be applied.
- **Allow or prevent self‑approval**, determining if the request creator can approve their own changes.
- **Require re‑approval when changes are modified**, ensuring that updates to an approved request must be reviewed again.

## Update approvals

Update approvals control changes to environment configurations. When an update approval ruleset is enabled on an environment, direct writes to the environment are blocked. Instead, users must create **drafts** that propose configuration changes. Drafts go through a review and approval workflow before they can be applied to the environment, ensuring that updates to critical configuration values and secrets are intentional and auditable.

Only one draft can be active on an environment at a time. A draft is mutable — team members can continue editing it until it is approved and applied, similar to collaborating on a shared document.

To enable update approvals, follow the steps in [Configuring a Ruleset](#configuring-a-ruleset) and select **Update** for the **Action**.

### Creating a draft

#### From the Pulumi Cloud console

When update approvals are enabled on an environment, the **Save** button is replaced with a **Create Draft** button. To propose changes:

1. Navigate to your environment in the Pulumi Cloud console.
1. Make your changes in the editor.
1. Select **Create Draft** to submit your proposed changes.

If a draft already exists, the editor opens in read-only mode with a banner indicating that the draft is pending approval.

#### From the CLI

Use the `--draft` flag with [`pulumi env set`](/docs/iac/cli/commands/pulumi_env_set/) or [`pulumi env edit`](/docs/iac/cli/commands/pulumi_env_edit/) to create or update a draft:

```bash
# Create a new draft
pulumi env set --draft my-org/my-project/prod-env FEATURE_X_ENABLED true

# Update an existing draft by ID
pulumi env set --draft=cr-123 my-org/my-project/prod-env FEATURE_X_ENABLED true

# Edit the full environment definition as a draft
pulumi env edit --draft my-org/my-project/prod-env
```

### Editing and reviewing drafts

To edit an existing draft, select **Edit draft** from the read-only banner or from the approval diff view.

The environment editor provides two modes when working with drafts:

- **Edit mode**: The editor is fully editable, allowing you to modify the draft. Select **Update Draft** to save your changes. A banner with a **Review diff to approve** button lets you switch to the approval view when your changes are ready.
- **Approval mode**: A read-only diff view showing what changed between the draft and the current revision. This view includes the review and approval controls along with an **Edit draft** button to switch back to edit mode if further changes are needed.

### Approving and applying drafts

Open drafts are listed in the **Approvals** tab in Pulumi Cloud. Select **Review changes** to open the approval mode diff view, where reviewers can approve or close the draft. Once the required number of approvals is met, the draft can be applied to update the environment.

If the ruleset requires re-approval when changes are modified, any edits to an approved draft reset the approval count and require a fresh round of reviews.

## Open approvals

Open approvals extend Pulumi ESC's approval system to control when environments can be opened (activated). While update approvals govern configuration changes, open approvals enable just-in-time (JIT) access patterns by requiring review and sign-off before users can access an environment's secrets and credentials. Open approvals are useful when you want to grant temporary, auditable access to sensitive environments.

### How open approvals work

Open approvals add an additional gate on top of standard permission checks. Users must have `open` permission on an environment and an active access grant to open it.

When an open approval ruleset is enabled on an environment, users with `open` permission cannot open the environment directly. Instead, they must:

1. Submit an **open request** specifying the reason for access and desired access duration.
1. Wait for the required approvals from designated reviewers.
1. Once approved, apply the request to activate the access grant.
1. Open the environment within the granted time window.

### Configuring open approvals

Open approvals use the same ruleset configuration as update approvals. To enable open approvals, follow the steps in [Configuring a Ruleset](#configuring-a-ruleset), but select **Open** (instead of **Update**) for the **Action**.

Once configured, any attempt to open the environment without an active access grant will be denied.

### Creating open requests

#### From the Pulumi Cloud console

1. In the Pulumi Cloud console, navigate to the environment you need to access.
1. Select **Request Open Access**.
1. Fill in the request form:
   - **Description**: Explain why you need access (e.g., "Investigating production API errors").
   - **Access duration**: How long you need access after first opening the environment (e.g., 2 hours).
   - **Grant expiration**: How long the approval remains valid before it must be activated (e.g., 24 hours).
1. Submit the request.

The request will appear in the **Approvals** tab for designated reviewers.

#### From the CLI

Use the `pulumi env open-request` command to create an access request:

```bash
pulumi env open-request my-org/my-project/prod-env \
  --access-duration-seconds=2h \
  --grant-expiration-seconds=24h
```

### Understanding duration and expiration

Open requests use two time-based controls to limit access:

- **Grant expiration**: How long you have to activate (first open) the grant after it's approved. This accounts for delays in the approval process and allows you to request access in advance.
- **Access duration**: How long the grant remains valid after you first open the environment. Once activated, the grant remains valid for the full access duration, even if that extends beyond the original expiration time.

**Example**: You submit a request for a 2-hour access duration and a 24-hour grant expiration. Once the request is approved and applied, you have 24 hours to open the environment. When you first open it, you can continue to access it for 2 hours.

### Approving and applying open requests

Open requests are listed in the **Approvals** tab in Pulumi Cloud. Select **Review changes** to open the review view, where reviewers can approve or close the request. Once the required number of approvals is met, the request must be applied to activate the access grant. You can apply the request from the review view by selecting **Apply**.

### Opening an environment with an active grant

Once your open request is applied, you can open the environment normally:

```bash
pulumi env open my-org/my-project/prod-env
```

The environment will open successfully as long as:

- You have `open` permission on the environment.
- You have activated your access grant within the grant expiration window.
- You are within the access duration window after first opening the environment.

If you try to open the environment without an active grant, you'll receive an error message indicating that approval is required.

### Imported environments

If an environment imports other environments that also have open approval rulesets enabled, you'll need valid access grants for all of them. When you create an open request, Pulumi ESC automatically creates requests for any imported environments that require approval, making the process more convenient. However, each request must be approved and applied separately by the appropriate reviewers.
