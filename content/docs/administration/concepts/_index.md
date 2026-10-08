---
title: Concepts
title_tag: Pulumi Cloud Administration Concepts
h1: Concepts
meta_desc: "The Pulumi Cloud organization and access model: organizations, SAML SSO, SCIM, accounts, access tokens, RBAC, audit logs, and customer-managed keys."
menu:
  administration:
    name: Concepts
    parent: administration-home
    identifier: administration-concepts
    weight: 20
aliases:
  - /docs/administration/organizations-teams/
---

How Pulumi Cloud models your organization and who can do what inside it. Read these to understand the system; see [Guides](/docs/administration/guides/) for the procedures that configure it.

## Organization and identity

- [Organizations](/docs/administration/concepts/organizations/) — the top-level container that owns your stacks, environments, and settings.
- [Identity providers and SSO](/docs/administration/concepts/identity-providers/) — SAML 2.0 single sign-on, GitHub, GitLab, or Bitbucket: the provider that governs who can be a member of your organization.
- [SCIM provisioning](/docs/administration/concepts/scim/) — how a SAML-backed organization synchronizes users and teams from its identity provider, and the behavior to plan for.
- [Accounts](/docs/administration/concepts/accounts/) — individual user accounts, profiles, and identity providers.
- [Organization-managed users](/docs/administration/concepts/org-managed-users/) — accounts an organization creates and controls through SAML or SCIM, and the restrictions that come with them.
- [Agent accounts](/docs/administration/concepts/agent-accounts/) — accounts for AI agents and automation acting on your organization's behalf.
- [Billing managers](/docs/administration/concepts/billing-managers/) — the role that delegates billing access without granting admin rights.
- [Access tokens](/docs/administration/concepts/access-tokens/) — personal, team, and organization tokens for authenticating the CLI, CI/CD, and the REST API.
- [OIDC issuers](/docs/administration/concepts/oidc-issuers/) — trust relationships that let CI/CD systems and Kubernetes workloads exchange their own OIDC tokens for short-lived Pulumi access tokens.

## Access control

- [Role-based access control (RBAC)](/docs/administration/concepts/rbac/) — entities, scopes, permission sets, roles, and teams, and how permissions accumulate across them.

## Security and compliance

- [Audit logs](/docs/administration/concepts/audit-logs/) — the record of user and system activity in your organization.
- [Customer managed keys](/docs/administration/concepts/customer-managed-keys/) — using your own encryption keys to protect data at rest, currently for Pulumi ESC with AWS KMS.

## Compute

- [Customer-managed runners](/docs/administration/concepts/customer-managed-runners/) — runners you host in your own infrastructure for deployments, Discovery scans, and audit policy evaluations.
