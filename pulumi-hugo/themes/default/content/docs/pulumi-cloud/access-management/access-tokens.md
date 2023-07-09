---
title_tag: "Pulumi Cloud: Access Tokens"
meta_desc: Learn about the various types of access tokens for the Pulumi Cloud.
title: Access tokens
h1: Pulumi Cloud access tokens
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    parent: access-management
    weight: 2
    identifier: pulumi-cloud-access-tokens
aliases:
- /docs/intro/pulumi-service/organization-access-tokens/
- /docs/intro/pulumi-cloud/organization-access-tokens/
- /docs/intro/pulumi-service/team-access-tokens/
- /docs/intro/pulumi-cloud/team-access-tokens/
- /docs/pulumi-cloud/access-management/organization-access-tokens/
- /docs/pulumi-cloud/access-management/team-access-tokens/
---

Use access tokens to sign into the Pulumi Cloud via the CLI or automate your usage of the Pulumi Cloud using the REST API. Learn more about the REST API in the [Pulumi Cloud REST API docs](/docs/pulumi-cloud/cloud-rest-api/).

Pulumi offers three types of access tokens: Personal, organization, and team. Personal access tokens are available to everyone, organization and team access tokens are only available to Enterprise and Business Critical customers. Organization and team access tokens are machine tokens that are not connected to a user account.

## Access token permissions

Personal access tokens map to the permissions of a user, organization access tokens map to the permissions of an organization member, and team access tokens map to the permissions of a team member.

Both organization and team token activities produce audit log events which are accessible from the **Audit Logs** page. All audit log events surface the token’s unique name, and in the event of audit log export, the token’s UUID as well.

| Action | Personal | Team | Organization |
| - | - | - | - |
| **Stacks** | **Personal** | **Team** | **Organization** |
| List stacks | ✅ | ✅ | ✅ |
| Get stack | ✅ | ✅ | ✅ |
| Get stack state | ✅ | ✅ | ✅ |
| Transfer stack | | | |
| Delete stack | ✅ | ✅ | ✅ |
| List webhooks | | ✅ | ✅ |
| Create webhook | | ✅ | ✅ |
| Get webhook | | ✅ | ✅ |
| Ping webhook | | ✅ | ✅ |
| List webhook deliveries | | ✅ | ✅ |
| **Stack tags** | **Personal** | **Team** | **Organization** |
| Get stack tags | ✅ | ✅ | ✅ |
| Set stack tag | ✅ | ✅ | ✅ |
| Delete stack tag | ✅ | ✅ | ✅ |
| **Stack updates** | **Personal** | **Team** | **Organization** |
| List stack updates | ✅ | ✅ | ✅ |
| Get update status | ✅ | ✅ | ✅ |
| List update events | ✅ | ✅ | ✅ |
| List previews | ✅ | ✅ | ✅ |
| **Organizations** | **Personal** | **Team** | **Organization** |
| List users | | ✅ | ✅ |
| Add user to organization | | | |
| Remove user from organization | | | |
| List teams | | ✅ | ✅ |
| Create team | | | ✅ |
| Delete team | | | ✅ |
| Update team membership | | | |
| Grant stack access to team | | | |
| Remove stack access from team | | | |
| Update member role | | | |
| List access tokens | | | |
| Create access token | | | |
| Delete access token | | | |
| List webhooks | | | ✅ |
| Create webhook | | | ✅ |
| Get webhook | | | ✅ |
| Ping webhook | | | ✅ |
| List webhooks deliveries | | | ✅ |
| **Audit logs** | **Personal** | **Team** | **Organization** |
| Get audit log events (JSON) | | | |
| Export audit log events (CSV or CEF) | | | |

## Personal access tokens

These access tokens have the same permission as your user.

### Creating Personal Access Tokens

To create an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Create token**.

### Deleting Personal Access Tokens

To delete an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Delete token** from the 3-dot menu at the end of the table row.

## Organization access tokens

Organization access tokens provide the following benefits:

* Organization access tokens belong to the organization. Any organization admin can view, create, and delete organization tokens. If a member of your organization leaves, you don't have to worry about losing access to core CI/CD tokens attached to their personal account.
* Promotes less privileged access, as an Organization Access Token, unlike a Personal Access Token, is granted privileges only to the organization in which it was created, rather than to all organizations a single user belongs to.
* Audit logs and update history are attributed to the organization, rather than an individual user.

### Creating an organization access token

Navigate to your organization and then:

1. Navigate to **Settings** > **Access Tokens**.
1. Select **Create token**.

The token must have a name that is unique among all organization and team access tokens in the organization., including deleted tokens. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised. Any other organization admin can delete this token; it is not owned by the admin which created it. Creation of organization access tokens is logged as an audit log event.

### Viewing organization access tokens

Organization access tokens are viewed navigating to **Access tokens** from the organization settings.

### Deleting organization access tokens

Organization access tokens can be deleted by any organization admin at any time.

1. Navigate to **Settings** > **Access Tokens**.
1. Choose **Delete token** from the action menu. You will be prompted in a dialog to confirm your choice.

If you choose to delete a token, its access will immediately be revoked and all further operations using it will fail as unauthorized. The token name will remain reserved for your organization after deletion.

## Team access tokens

Team access tokens provide the following benefits:

* Managed by organization and team admins, allowing more users in your organization to leverage machine tokens.
* Support user-independent usage in your CI integrations while having less privileged scope to other stacks in your organization.

### Creating team access tokens

Navigate to your Pulumi Organization, then:

1. Select **Teams**.
1. Select the Pulumi Team you would like to attach the token to.
1. Scroll to **Access Tokens**.

The token must have a name that is unique among all organization and team access tokens in the organization., including deleted tokens. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised. Any other organization admin can delete this token; it is not owned by the admin which created it. Creation of organization access tokens is logged as an audit log event.

### Viewing team access tokens

To view team access tokens:

1. Select **Teams**.
1. Select a team.
1. Scroll to the **Team Access Tokens** card.

### Deleting team access tokens

Team access tokens can be deleted by any Organization or Team admin.

To delete a team access token:

1. Select **Teams**.
1. Select a team.
1. Scroll to the **Team Access Tokens** card.
1. Select the ellipsis button.
1. Choose **Delete token**. You will be prompted in a dialog to confirm your choice.

If you choose to delete a token, its access will immediately be revoked and all further operations using it will fail as unauthorized. The token name will remain reserved for your organization after deletion.
