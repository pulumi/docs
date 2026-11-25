---
title: Administration
title_tag: Pulumi ESC administration
meta_desc: Administer Pulumi ESC alongside the rest of your Pulumi Cloud organization, with audit logs, deletion protection, and customer managed keys.
menu:
    esc:
        parent: esc-home
        identifier: pulumi-esc-admin
        weight: 8
aliases:
  - /docs/esc/access-management/
  - /docs/support/faq/secrets-config/
  - /docs/pulumi-cloud/esc/faq
  - /docs/esc/faq/
# The pages listed below mix gated features (audit logs, customer managed keys) with
# ungated ones (deletion protection), so the landing page itself carries no marker.
---

Pulumi ESC is built on [Pulumi Cloud](/docs/administration/) and is administered through the same organization as the rest of Pulumi. Organizations, teams and role-based access control, access tokens, SAML SSO, SCIM, OIDC issuers, and self-hosting are all documented under [Administration](/docs/administration/) and apply to environments exactly as they do to stacks; the permissions that govern environment access are catalogued in [Environment scopes](/docs/administration/reference/rbac-scopes/environments/). Self-hosted Pulumi Cloud deployments include ESC.

The pages below cover what is specific to ESC:

- [Audit logs](/docs/esc/administration/audit-logs/): How environment activity is recorded in your organization's audit log.
- [Deletion protection](/docs/esc/administration/deletion-protection/): Prevent accidental deletion of environments holding critical configuration.
- [Customer managed keys](/docs/esc/concepts/customer-managed-keys/): Bring your own encryption keys to protect the secrets ESC stores.

## How secrets are counted for billing

ESC bills by the number of secrets in your environments.
Each definition of [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/) or `fn::open::*` counts as one secret.
That covers static secrets, [dynamic login credentials](/docs/esc/providers/login/), and [dynamic secrets](/docs/esc/providers/secrets/).
The [`pulumi-stacks` provider](/docs/esc/providers/iac/pulumi-stacks/) is the exception: `fn::open::pulumi-stacks` doesn't count.

Only the latest revision of each environment counts toward your bill.
To see your organization's current usage, open **Settings** > **Billing & usage** in Pulumi Cloud.
For prices, see [pricing](/pricing/).
