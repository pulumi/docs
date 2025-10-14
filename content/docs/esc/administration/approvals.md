---
title_tag: "Pulumi ESC: Approvals"
meta_desc:  Require explicit review and sign-off before applying changes or opening ESC-managed environments.
title: "Approvals"
h1: Approvals in Pulumi ESC
meta_title: Approvals in Pulumi ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: pulumi-esc-admin
    weight: 2
  administration:
    name: ESC Approvals
    parent: administration-security-compliance
    weight: 10
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

![Approvals workflow](/images/docs/esc/approvals/approvals-workflow.png)

## Why use approvals?

Teams can use Pulumi ESC approvals to apply the same rigor of code review workflows to environment configurations and access management. Approvals help organizations enforce governance policies, meet compliance requirements, and reduce risk by requiring explicit review and sign-off. Each request creates a clear, auditable record of who approved what, when, and why, which is especially valuable for regulated industries or teams with strict change-management processes.

By introducing a controlled review process, approvals let users submit requests while ensuring only authorized reviewers can approve and apply them. This balances collaboration with security and accountability, and works seamlessly in both the Pulumi Cloud console and the ESC CLI.

## How to Enable and Configure Approvals

Approvals in Pulumi ESC are configured at the environment level using **approval rulesets**. A ruleset defines the policies that control how changes are reviewed and approved before being applied.

### Enabling Approvals

1. Navigate to your environment in the Pulumi Cloud console.
2. Go to **Settings → Approval Rulesets**.
3. Click **Create Ruleset** to add a new approval policy, or select an existing ruleset to edit.

![Approvals ruleset configuration](/images/docs/esc/approvals/approvals-ruleset.png)

### Configuring a ruleset

When creating or editing a ruleset, you can:

- **Enable or disable the ruleset** to control whether approvals are required.
- **Specify approvers** by adding teams, users, or permissions that grant approval rights.
- **Set the required number of approvals** before a change can be applied.
- **Allow or prevent self‑approval**, determining if the request creator can approve their own changes.
- **Require re‑approval when changes are modified**, ensuring that updates to an approved request must be reviewed again.

## Update approvals

Update approvals control changes to environment configurations. When an update approval ruleset is enabled on an environment, direct writes to the environment are blocked. Instead, users must create **change requests** that specify the proposed configuration changes.

Change requests must be reviewed and approved according to the rules defined in your ruleset. After the required approvals are granted, the changes can be applied to the environment. This ensures that updates to critical configuration values and secrets are intentional and auditable.

To enable update approvals, follow the steps in [Configuring a Ruleset](#configuring-a-ruleset) and select **Update** for the **Action**.

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

Use the `esc env open-request` command to create an access request:

```bash
esc env open-request my-org/my-project/prod-env \
  --access-duration=2h \
  --grant-expiration=24h \
  --description="Investigating production issue #1234"
```

### Understanding duration and expiration

Open requests use two time-based controls to limit access:

- **Grant expiration**: How long you have to activate (first open) the grant after it's approved. This accounts for delays in the approval process and allows you to request access in advance.
- **Access duration**: How long the grant remains valid after you first open the environment. Once activated, the grant remains valid for the full access duration, even if that extends beyond the original expiration time.

**Example**: You submit a request for a 2-hour access duration and a 24-hour grant expiration. Once the request is approved and applied, you have 24 hours to open the environment. When you first open it, you can continue to access it for 2 hours.

### Approving and applying open requests

Reviewers can approve open requests from the **Approvals** tab in Pulumi Cloud. Once the required number of approvals is met, the request must be applied to activate the access grant. You can apply the request from the Pulumi Cloud console by selecting the approved request and choosing **Apply**.

### Opening an environment with an active grant

Once your open request is applied, you can open the environment normally:

```bash
esc env open my-org/my-project/prod-env
```

The environment will open successfully as long as:

- You have `open` permission on the environment.
- You have activated your access grant within the grant expiration window.
- You are within the access duration window after first opening the environment.

If you try to open the environment without an active grant, you'll receive an error message indicating that approval is required.

### Imported environments

If an environment imports other environments that also have open approval rulesets enabled, you'll need valid access grants for all of them. When you create an open request, Pulumi ESC automatically creates requests for any imported environments that require approval, making the process more convenient. However, each request must be approved and applied separately by the appropriate reviewers.
