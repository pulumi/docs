---
title: Guides
title_tag: Pulumi Cloud Administration Guides
h1: Guides
meta_desc: Task-oriented guides for administering Pulumi Cloud — SAML SSO, SCIM, OIDC issuers, audit log export, customer-managed keys, and least privilege.
menu:
  administration:
    name: Guides
    parent: administration-home
    identifier: administration-guides
    weight: 30
---

Procedures for setting up and running a Pulumi Cloud organization. Each guide is self-contained, so start with whichever matches what you are trying to do. For the model these guides configure, see [Concepts](/docs/administration/concepts/).

## Identity and single sign-on

- [SAML SSO](/docs/administration/guides/saml/) — connect Pulumi Cloud to Microsoft Entra ID, Okta, Google Workspace, Auth0, JumpCloud, or OneLogin.
- [SCIM](/docs/administration/guides/scim/) — automate user and team provisioning from your identity provider.
- [OIDC issuers](/docs/administration/guides/oidc-issuers/) — let GitHub, GitLab, or a Kubernetes cluster exchange its own OIDC tokens for Pulumi Cloud credentials.

## Security and compliance

- [Audit logs](/docs/administration/guides/audit-logs/) — download your organization's audit log on demand, or stream it to AWS S3 or Microsoft Sentinel.
- [Customer managed keys](/docs/administration/guides/customer-managed-keys/) — bring your own encryption key from an external key management system.
- [Least privilege](/docs/administration/guides/least-privilege/) — apply least-privilege access across IaC, ESC, and CI/CD.
