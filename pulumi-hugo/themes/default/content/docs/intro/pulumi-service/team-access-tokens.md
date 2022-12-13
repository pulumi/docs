---
title_tag: "Pulumi Service: Team Access Tokens"
title: "Team Access Tokens"
meta_desc: Team Access Tokens enable access to be scoped to the stack access of a Pulumi Team, rather than to the entire organization’s stacks. Learn more here.
menu:
  intro:
    parent: pulumi-service
    weight: 6
---
{{% notes "info" %}}
Team Access Tokens are only available to organizations using Pulumi Enterprise or Pulumi Business Critical.
To learn more about our editions, visit our [pricing page](/pricing/).
{{% /notes %}}
Team Access Tokens, like [Organization Access Tokens](/docs/intro/pulumi-service/organization-access-tokens/), provide Enterprise and Business Critical customers the opportunity to manage resources and stack operations for their organization independent of a single-user account. However, Team Access Tokens enable this access to be scoped to the stack access of a [Pulumi Team](/docs/intro/pulumi-service/teams/), rather than to the entire organization's stacks.

Collectively Organization Access Tokens and Team Access Tokens are referred to as "machine tokens", which are not owned by a real user in your organization. This distinguishes them from Personal Access Tokens.

Team Access Tokens are available on Enterprise and Business Critical subscriptions, as well as trials.

Team Access Tokens provide several benefits over Organization and Personal Access Tokens:

* They can be managed by Team Admins in addition to Organization Admins, allowing more users in your organization to leverage machine tokens.
* They support user-independent usage in your CI integrations while having less privileged scope to other stacks in your organization.

## Creating a Team Access Token

Navigate to your Pulumi Organization, then:

1. Select **Teams**.
1. Select the Pulumi Team you would like to attach the token to.
1. Scroll to **Access Tokens**.

Team Access Tokens, like Organization Access Tokens, must have a name that is unique among all Organization Access Tokens assigned to it. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised.

Once you name a token, the name is taken forever, even after you delete it. This is in order to maintain the integrity of Audit Log Events which persist the token's name as part of the event (see below). Any other Organization Admin, or a Team Admin for the associated team, can delete the token since they are managed by the team and not by a user.

The creation of any Team Access Token, and the user who performed it, is logged as an [Audit Log](/docs/intro/pulumi-service/audit-logs/) Event.

## Viewing Team Access Tokens

To view Team Access Tokens, go to your Pulumi Team page within your respective organization and scroll to the Team Access Tokens card. Only Organization Admins and Team Admins for the Team will see this card.

## Deleting a Team Access Token

A Team Access Token can be deleted by any Team Admin, for the specific Team that it belongs to, or any Organization Admin. No other member types of the organization can delete a Team Access Token.

From the organization's homepage, follow the same steps as for all other Access Token types:

1. Select **Teams**.
1. Navigate to the desired Pulumi Team.
1. Scroll to the Team Access Tokens card.
1. Select the ellipsis button.
1. Choose **Delete token**. You will be prompted in a dialog to confirm your choice.

If you choose to delete a token, its access will immediately be revoked and all further operations using it will fail as unauthorized. That token's name will remain reserved for your organization to preserve its uniqueness in Audit Log Events for any operations that it carried out.

## Auditing Team Token Actions

Since an organization can have many machine tokens, it’s necessary to be able to identify them uniquely in Audit Log Events. All Audit Log Events which were triggered by an Team Access Token will surface the token’s unique name, and in the event of Audit Log Export, the token’s UUID as well.

## Permissions/Authorization

Team Access Tokens behave like a team member with the [stack permissions](https://www.pulumi.com/docs/intro/pulumi-service/projects-and-stacks/#stack-permissions) granted by that team. They do not grant any privileges to view the Pulumi Service UI, or to create additional tokens of any type. See below for a full list of accessible APIs:

### API Access

See the Pulumi [Service REST API docs](https://www.pulumi.com/docs/reference/service-rest-api/) for more information about each API endpoint.

#### Stacks

These are dependent on the stack permissions granted to the team associated with the Team Access Token. A stack can only be deleted if the team has Admin stack permissions. Webhooks can only be managed if the team has Write stack permissions.

| Action |  |
|--------|------|
| List Stacks | ✅ |
| Get Stack | ✅ |
| Get Stack State | ✅ |
| Transfer Stack |  |
| Delete Stack | ✅ |
| Create Webhook | ✅ |
| List Webhooks | ✅ |
| Get Webhook | ✅ |
| Ping Webhook | ✅ |
| List Webhooks Deliveries | ✅ |

#### Stack Tags

These are dependent on the stack permissions granted to the team associated with the Team Access Token. A stack tag can only be set or deleted if the team has Write stack permissions.

| Action |  |
|--------|------|
| Get Stack Tags | ✅ |
| Set Stack Tag | ✅ |
| Delete Stack Tag | ✅ |

#### Stack Updates

| Action |  |
|--------|------|
| List Stack Updates | ✅ |
| Get Update Status | ✅ |
| List Update Events | ✅ |
| List Previews | ✅ |

#### Organizations

| Action |  |
|--------|------|
| List Users | ✅ |
| Add User to Organization |  |
| Remove User from Organization |  |
| List Teams | ✅ | |
| Create Team |  |
| Delete Team |  |
| Update Team Membership |  |
| Grant Stack Access to Team |  |
| Remove Stack Access from Team |  |
| Update User’s Role |  |
| List User Access Tokens |  |
| Create User Access Token |  |
| Delete User Access Token |  |
| Create Webhook |  |
| List Webhooks |  |
| Get Webhook |  |
| Ping Webhook |  |
| List Webhooks Deliveries |  |

#### Audit Logs

| Action | Team Token Access |
|--------|------|
| Get Audit Log Events (JSON) |  |
| Export Audit Log Events (CSV or CEF) |  |
