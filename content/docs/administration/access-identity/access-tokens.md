---
title_tag: "Pulumi Cloud: Access Tokens"
meta_desc: Learn about the various types of access tokens for the Pulumi Cloud.
title: Access tokens
h1: Pulumi Cloud access tokens
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Access tokens
    parent: administration-access-identity
    weight: 3
aliases:
- /docs/administration/access-identity/access-tokens/
- /docs/intro/pulumi-service/organization-access-tokens/
- /docs/intro/pulumi-cloud/organization-access-tokens/
- /docs/intro/pulumi-service/team-access-tokens/
- /docs/intro/pulumi-cloud/team-access-tokens/
- /docs/pulumi-cloud/access-management/organization-access-tokens/
- /docs/pulumi-cloud/access-management/team-access-tokens/
- /docs/pulumi-cloud/access-management/access-tokens/
---

Use access tokens to sign into the Pulumi Cloud via the CLI or automate your usage of the Pulumi Cloud using the REST API. Learn more about the REST API in the [Pulumi Cloud REST API docs](/docs/reference/cloud-rest-api/).

Pulumi offers three types of access tokens:

1. **Personal tokens**, which carry the permissions of the individual user who created them. Personal tokens are available to all Pulumi Cloud users.
1. **Organization tokens**, which authenticate as the organization itself rather than any individual user. Actions taken with organization tokens appear in audit logs attributed to the organization. Organization tokens are only available to Enterprise and Business Critical customers.
1. **Team tokens**, which authenticate as a specific team within an organization rather than any individual user. Actions taken with team tokens appear in audit logs attributed to the team. Team tokens are only available to Enterprise and Business Critical customers.

When using tokens, be mindful of the following security best practices:

* Organization and team access tokens are machine tokens that are not connected to a user account, and therefore should only be used in scenarios like CI/CD pipelines, where the Pulumi actions are not being performed directly by a particular user.
* Tokens can optionally be assigned an expiration period of up to two years, at which point the token will no longer be valid for any Pulumi operation. Expired tokens cannot be refreshed or reactivated. It's strongly recommended that you assign an expiration to your token to encourage token rotation and improve your organization's security posture.
* Access tokens can create stacks if the organization's access management settings permit all members to do so, or if the token's assigned role includes the `stack:create` scope. Admin organization tokens always have this capability. The stack creator will automatically become its owner and will have all stack permissions, including deletion. See [RBAC](/docs/administration/access-identity/rbac/) for more on how org-wide settings and role scopes interact.

## Access token permissions

### Personal tokens

Personal access tokens carry the same permissions as the user who created them. This includes all organization memberships, team memberships, and role assignments that apply to the user across every Pulumi Cloud organization they belong to.

### Organization tokens

Organization tokens act on behalf of the organization itself. Rather than mapping to a fixed set of capabilities, organization tokens derive their permissions from the [RBAC role](/docs/administration/access-identity/rbac/roles/) assigned to them at creation time. This means you can tailor the exact level of access an organization token has—from read-only access to a subset of stacks, to full administrative control—by assigning the appropriate role.

Organization tokens that are assigned no explicit role receive the organization's [default member role](/docs/administration/access-identity/rbac/roles/). The token's access is automatically limited to the single organization it was created in, unlike a personal token which spans all of a user's organizations.

### Team tokens

Team tokens act on behalf of a specific team within the organization. A team token's effective permissions are determined by the [roles assigned to that team](/docs/administration/access-identity/rbac/teams/) at the time each request is evaluated. If a team's role assignments change, those changes are immediately reflected in what the team token can do.

Team tokens are useful for CI/CD pipelines that should be scoped to only the resources a particular team manages, without requiring a personal token from any individual team member.

For a detailed reference on how permissions are structured and evaluated, see [Role-Based Access Control (RBAC)](/docs/administration/access-identity/rbac/).

## Personal access tokens

Personal access tokens have the same permissions as your Pulumi Cloud user. This includes your respective permissions for all Pulumi Cloud organizations in which your user is a member.

### Creating personal access tokens

To create an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Create token**, which will open a dialog.
1. Optionally, you may assign a description for additional context.
1. Choose an expiration period of up to two years. You may also choose that the token does not expire.
1. Select **Create token** in the dialog to create the token.

It is strongly recommended that you choose an expiration period for all access tokens you create.

### Deleting personal access tokens

To delete an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Delete token** from the 3-dot menu at the end of the table row.

## Organization access tokens {#creating-an-organization-access-token}

{{% notes type="info" %}}
Please note that this functionality is available only in the [Enterprise and Business Critical editions](https://www.pulumi.com/pricing/) of Pulumi.
{{% /notes %}}

Organization tokens authenticate as the organization itself rather than any individual user. They are the recommended token type for any automated or non-interactive workflow, including:

* **CI/CD pipelines**: deploying infrastructure updates without tying operations to an individual's account.
* **Drift detection**: monitoring stacks across the organization for configuration drift.
* **Policy enforcement**: running compliance checks or applying policy packs programmatically.
* **Org-level reporting**: querying stack state or resource data for dashboards and auditing.

Unlike personal tokens, organization tokens are scoped to a single organization and are not affected when team members join or leave. By assigning a [custom role](/docs/administration/access-identity/rbac/roles/) with only the scopes your automation needs, you can follow the principle of least privilege and limit the blast radius of any single token.

### What organization tokens can do

An organization token can do anything its assigned [RBAC role](/docs/administration/access-identity/rbac/roles/) permits. By assigning different roles, you can scope a token to exactly the operations your automation needs — for example, a token that can only read stack state, or one that can deploy updates to a specific set of stacks. If no role is assigned at creation time, the token receives the organization's default member role.

Actions taken by organization tokens appear in audit logs attributed to the organization rather than an individual user, with the token's unique name surfaced in every event.

### Who can manage organization tokens

Any organization admin can create, view, and delete organization tokens via **Settings** > **Access Tokens**. Tokens are not owned by the admin who created them — if that person leaves the organization, other admins retain full access. Each token's name must be unique across all organization and team tokens in the organization, including deleted tokens, so that tokens can be reliably identified in audit logs and incident response.

Deleting a token immediately revokes its access; all further operations using it will fail as unauthorized. The token name is permanently reserved after deletion to preserve audit log integrity.

## Team access tokens

{{% notes type="info" %}}
Please note that this functionality is available only in the [Enterprise and Business Critical editions](https://www.pulumi.com/pricing/) of Pulumi.
{{% /notes %}}

Team tokens are machine tokens scoped to the resources and permissions of a specific team. They are useful for automated processes (like CI/CD pipelines) that should only be able to access the infrastructure a particular team owns. This avoids the need to use a personal token from any individual team member.

### What team tokens can do

A team token's effective permissions are the union of all [roles assigned to that team](/docs/administration/access-identity/rbac/teams/), evaluated at the time of each request. If the team's role assignments change — for example, the team is granted access to a new set of stacks — the token's capabilities update automatically without any token recreation. This makes team tokens a good fit for long-lived automation where access needs may evolve over time.

As with organization tokens, team token activity is recorded in audit logs with the token's name, keeping actions traceable without exposing individual users.

### Who can manage team tokens

Organization admins and team admins can create and delete team tokens. Tokens are found under the team's page (**Teams** > select a team > **Access Tokens**) and are not owned by the admin who created them. Each token name must be unique across all organization and team tokens in the organization, including deleted tokens.

Deleting a token immediately revokes its access. The token name is permanently reserved after deletion to preserve audit log integrity.

## Legacy organization token types

Before role assignment was available for organization tokens, organization tokens were created with one of two fixed permission levels:

* **Standard organization tokens** had member-level permissions — they could perform read and write operations within the organization but could not manage members, modify organization settings, or perform other administrative actions. This is equivalent to assigning the built-in Member role to an organization token today.

* **Admin organization tokens** had full administrator-level permissions — they could perform any operation an organization administrator can perform, except creating or deleting other organization tokens. This is equivalent to assigning the built-in Admin role to an organization token today.

{{% notes type="warning" %}}
Admin organization tokens have elevated permissions; please use them with caution.
{{% /notes %}}

Both token types continue to work. The admin/standard distinction maps directly onto the built-in Admin and Member roles in the current RBAC system. When creating new organization tokens, you can reproduce these permission levels by assigning the corresponding built-in role. For new automation, prefer assigning a [custom role](/docs/administration/access-identity/rbac/roles/) instead — custom roles let you follow the principle of least privilege by granting only the scopes your automation actually needs.

## OIDC issued tokens

OIDC-issued access tokens generated in CI/CD workflows (such as GitHub Actions) do not receive admin privileges by default. To perform operations that require elevated access—such as creating or deleting stacks—you must explicitly request the admin scope when exchanging the OIDC token.

For example:

```json
{
  "provider": "github",
  "audience": "pulumi",
  "scope": "admin"
}
```
