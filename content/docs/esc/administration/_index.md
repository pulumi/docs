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
# The pages listed below mix gated features (audit logs, customer managed keys) with
# ungated ones (deletion protection), so the landing page itself carries no marker.
---

Pulumi ESC is built on [Pulumi Cloud](/docs/administration/) and is administered through the same organization as the rest of Pulumi. Organizations, teams and role-based access control, access tokens, SAML SSO, SCIM, OIDC issuers, and self-hosting are all documented under [Administration](/docs/administration/) and apply to environments exactly as they do to stacks; the permissions that govern environment access are catalogued in [Environment scopes](/docs/administration/reference/rbac-scopes/environments/). Self-hosted Pulumi Cloud deployments include ESC.

The pages below cover what is specific to ESC:

- [Audit logs](/docs/esc/administration/audit-logs/): How environment activity is recorded in your organization's audit log.
- [Deletion protection](/docs/esc/administration/deletion-protection/): Prevent accidental deletion of environments holding critical configuration.
- [Customer managed keys](/docs/esc/concepts/customer-managed-keys/): Bring your own encryption keys to protect the secrets ESC stores.
