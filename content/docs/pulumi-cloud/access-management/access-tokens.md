---
title_tag: "Pulumi Cloud: Access Tokens"
meta_desc: Learn about the various types of access tokens for the Pulumi Cloud.
title: Access tokens
h1: Pulumi Cloud access tokens
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Access tokens
    parent: pulumi-cloud-access-management
    weight: 3
    identifier: pulumi-cloud-access-management-access-tokens
aliases:
  - /docs/intro/pulumi-service/organization-access-tokens/
  - /docs/intro/pulumi-cloud/organization-access-tokens/
  - /docs/intro/pulumi-service/team-access-tokens/
  - /docs/intro/pulumi-cloud/team-access-tokens/
  - /docs/pulumi-cloud/access-management/organization-access-tokens/
  - /docs/pulumi-cloud/access-management/team-access-tokens/
search:
  keywords:
    - tokens
    - access
    - various
    - types
    - learn
    - cloud
    - organization
---

Use access tokens to sign into the Pulumi Cloud via the CLI or automate your usage of the Pulumi Cloud using the REST API. Learn more about the REST API in the [Pulumi Cloud REST API docs](/docs/pulumi-cloud/cloud-rest-api/).

Pulumi offers three types of access tokens:

1. Personal tokens, which map to the permissions of an individual user. Personal tokens are available to all Pulumi Cloud users.
1. Organization tokens, which map to the permissions of either a regular organization member or an organization admin, depending on the scope of the token. Organization tokens are only available to Enterprise and Business Critical customers.
1. Team tokens, which map to the permissions of a team within an organization. For more information on using teams within your Pulumi Cloud organization, see [Teams & Role-based access control (RBAC)
](/docs/pulumi-cloud/access-management/teams/). Team tokens are only available to Enterprise and Business Critical customers.

When using tokens, be mindful of the following security best practices:

* Organization and team access tokens are machine tokens that are not connected to a user account, and therefore should only be used in scenarios like CI/CD pipelines, where the Pulumi actions are not being performed directly by a particular user.
* Tokens can optionally be assigned an expiration period of up to two years, at which point the token will no longer be valid for any Pulumi operation. Expired tokens cannot be refreshed or reactivated. It's strongly recommended that you assign an expiration to your token to encourage token rotation and improve your organization's security posture.
* All access tokens can create stacks. The stack creator will automatically become its owner and will have all stack permissions, including deletion.

## Access token permissions

Personal access tokens map to the permissions of a user, organization access tokens map to the permissions of an organization member, and team access tokens map to the permissions of a team member.

Both organization and team token activities produce audit log events which are accessible from the **Audit Logs** page. All audit log events surface the token’s unique name, and in the event of audit log export, the token’s UUID as well.

| Action                                | Personal     | Team     | Organization     | Admin     |
|---------------------------------------|--------------|----------|------------------|-----------|
| **Stacks**                            | **Personal** | **Team** | **Organization** | **Admin** |
| List stacks                           | ✅            | ✅        | ✅                | ✅         |
| Get stack                             | ✅            | ✅        | ✅                | ✅         |
| Get stack state                       | ✅            | ✅        | ✅                | ✅         |
| Transfer stack                        |              |          |                  | ✅         |
| Delete stack                          | ✅            | ✅        | ✅                | ✅         |
| List webhooks                         |              | ✅        | ✅                | ✅         |
| Create webhook                        |              | ✅        | ✅                | ✅         |
| Get webhook                           |              | ✅        | ✅                | ✅         |
| Ping webhook                          |              | ✅        | ✅                | ✅         |
| List webhook deliveries               |              | ✅        | ✅                | ✅         |
| **Stack tags**                        | **Personal** | **Team** | **Organization** | **Admin** |
| Get stack tags                        | ✅            | ✅        | ✅                | ✅         |
| Set stack tag                         | ✅            | ✅        | ✅                | ✅         |
| Delete stack tag                      | ✅            | ✅        | ✅                | ✅         |
| **Stack updates**                     | **Personal** | **Team** | **Organization** | **Admin** |
| List stack updates                    | ✅            | ✅        | ✅                | ✅         |
| Get update status                     | ✅            | ✅        | ✅                | ✅         |
| List update events                    | ✅            | ✅        | ✅                | ✅         |
| List previews                         | ✅            | ✅        | ✅                | ✅         |
| **Organizations**                     | **Personal** | **Team** | **Organization** | **Admin** |
| List users                            |              | ✅        | ✅                | ✅         |
| Add user to organization              |              |          |                  | ✅         |
| Remove user from organization         |              |          |                  | ✅         |
| List teams                            |              | ✅        | ✅                | ✅         |
| Create team                           |              |          | ✅                | ✅         |
| Delete team                           |              |          | ✅                | ✅         |
| Update team membership                |              |          |                  | ✅         |
| Grant stack access to team            |              |          |                  | ✅         |
| Remove stack access from team         |              |          |                  | ✅         |
| Create team token                     |              |          |                  | ✅         |
| Delete team token                     |              |          |                  | ✅         |
| Update member role                    |              |          |                  | ✅         |
| List access tokens                    |              |          |                  | ✅         |
| Create access token                   |              |          |                  |           |
| Delete access token                   |              |          |                  |           |
| **Webhooks**                          | **Personal** | **Team** | **Organization** | **Admin** |
| List stack webhooks                   | ✅            | ✅        | ✅                | ✅         |
| Create stack webhook                  | ✅            | ✅        | ✅                | ✅         |
| Get stack webhook                     | ✅            | ✅        | ✅                | ✅         |
| Ping stack webhook                    | ✅            | ✅        | ✅                | ✅         |
| List stack webhooks deliveries        | ✅            | ✅        | ✅                | ✅         |
| List organization webhooks            |              |          |                  | ✅         |
| Create organization webhook           |              |          |                  | ✅         |
| Get organization webhook              |              |          |                  | ✅         |
| Ping organization webhook             |              |          |                  | ✅         |
| List organization webhooks deliveries |              |          |                  | ✅         |
| **Audit logs**                        | **Personal** | **Team** | **Organization** | **Admin** |
| Get audit log events (JSON)           |              |          |                  | ✅         |
| Export audit log events (CSV or CEF)  |              |          |                  | ✅         |

## Personal access tokens

These access tokens have the same permission as your user.

### Creating Personal Access Tokens

To create an access token:

1. Select **Personal access tokens** from the user menu.
1. Select **Create token**, which will open a dialog.
1. Optionally, you may assign a description for additional context.
1. Choose an expiration period up of up to two years. You may also choose that the token does not expire.
1. Select **Create token** in the dialog to create the token.

It is strongly recommended that you choose an expiration period for all access tokens you create.

### Deleting Personal Access Tokens

To delete an access token:

1. Select **Personal access tokens** from the user menu.
2. Select **Delete token** from the 3-dot menu at the end of the table row.

## Organization access tokens

{{< notes type="info" >}}
Please note that this functionality is available only in the [Enterprise and Business Critical editions](https://www.pulumi.com/pricing/) of Pulumi.
{{< /notes >}}

Organization access tokens provide the following benefits:

* Organization access tokens belong to the organization. Any organization admin can view, create, and delete organization tokens. If a member of your organization leaves, you don't have to worry about losing access to core CI/CD tokens attached to their personal account.
* Promotes less privileged access, as an Organization Access Token, unlike a Personal Access Token, is granted privileges only to the organization in which it was created, rather than to all organizations a single user belongs to.
* Audit logs and update history are attributed to the organization, rather than an individual user.

### Creating an organization access token

Navigate to your organization and then:

1. Navigate to **Settings** > **Access Tokens**.
1. Select **Create token**, which will open a dialog.
1. Provide a unique name for this token across your organization. It can be up to 40 characters.
1. Optionally, you may assign a description for additional context.
1. Choose an expiration period up of up to two years. You may also choose that the token does not expire.
1. Select **Create token** in the dialog to create the token.

The token must have a name that is unique among all organization and team access tokens in the organization., including deleted tokens. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised. Any other organization admin can delete this token; it is not owned by the admin which created it. Creation of organization access tokens is logged as an audit log event.

It is strongly recommended that you choose an expiration period for all access tokens you create.

#### Admin organization access tokens

{{% notes type="warning" %}}
Admin organization access tokens have elevated permissions, please use them with caution.
{{% /notes %}}
Admin organization access tokens (or admin tokens) are organization tokens with elevated, administrator-level privileges. Admin tokens allow automated processes to perform any operation supported for organization administrators except for the creation or deletion of other organization tokens.

To create an admin organization access token, select the `Admin` option when creating an organization token, following the steps above.

Exercise caution and limit the use of admin organization access tokens to scenarios where they are absolutely necessary. Avoid unnecessary sharing and adhere to the principle of least privilege. Admin tokens can be deleted from the **Access Tokens** page within your organization settings following the process below.

### Viewing organization access tokens

Organization access tokens are viewed navigating to **Access tokens** from the organization settings.

### Deleting organization access tokens

Organization access tokens can be deleted by any organization admin at any time.

1. Navigate to **Settings** > **Access Tokens**.
1. Choose **Delete token** from the action menu. You will be prompted in a dialog to confirm your choice.

If you choose to delete a token, its access will immediately be revoked and all further operations using it will fail as unauthorized. The token name will remain reserved for your organization after deletion.

## Team access tokens

{{< notes type="info" >}}
Please note that this functionality is available only in the [Enterprise and Business Critical editions](https://www.pulumi.com/pricing/) of Pulumi.
{{< /notes >}}

Team access tokens provide the following benefits:

* Managed by organization and team admins, allowing more users in your organization to leverage machine tokens.
* Support user-independent usage in your CI integrations while having less privileged scope to other stacks in your organization.

### Creating team access tokens

Navigate to your Pulumi Organization, then:

1. Select **Teams**.
1. Select the Pulumi Team you would like to attach the token to.
1. Scroll to **Access Tokens**.
1. Select **Create token**, which will open a dialog.
1. Provide a unique name for this token across your organization. It can be up to 40 characters.
1. Optionally, you may assign a description for additional context.
1. Choose an expiration period up of up to two years. You may also choose that the token does not expire.
1. Select **Create token** in the dialog to create the token.

The token must have a name that is unique among all organization and team access tokens in the organization., including deleted tokens. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised. Any other organization admin can delete this token; it is not owned by the admin which created it. Creation of organization access tokens is logged as an audit log event.

It is strongly recommended that you choose an expiration period for all access tokens you create.

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
