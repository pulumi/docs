---
title: "Organization Access Tokens"
meta_desc: Overview of Access Tokens in the Pulumi Service for both personal accounts and organizations.
menu:
  intro:
    parent: pulumi-service
    weight: 2
---

Organization Access Tokens provide Enterprise and Business Critical customers the opportunity to manage resources and stack operations for their organization independent of a single-user account.

Leveraging Organization Access Tokens for your organization's automation delivers many benefits over Personal Access Tokens:

* Organization Tokens belong to the organization, rather than an individual member. Any admin in the organization can view, create, and delete all Organization Tokens. If a member of your organization leaves, you don't have to worry about losing access to a core CI/CD token attached to their personal account.
* Promotes less privileged access, as an Organization Access Token, unlike a Personal Access Token, is granted privileges only to the organization in which it was created, rather than to all organizations a single user belongs to.
* Audit logs and update history are attributed to the organization and the name of the token, rather than an individual user.

## Creating an Organization Access Token

Organization tokens are available on trials, and Enterprise and Business Critical subscriptions.

Navigate to your organization and then:

1. Select **Settings**.
1. Navigate to **Access Tokens**.
1. Select **Create token**.

An Organization Access Token must have a name that is unique among all Organization Access Tokens assigned to it. This allows tokens taking operations on behalf of your organization to be identifiable in the event that one is compromised. This name must be unique even among deleted tokens, in order to maintain the integrity of Audit Log Events which persist the token’s name (even for a deleted token) as part of the event (see below). Any other organization admin can delete this token; it is not owned by the admin which created it.

Creation of any Organization Access Token, and the user who performed it, is logged as an Audit Log Event.

## Viewing Organization Access Tokens

Organization Access Tokens are viewed by going to the organization’s Settings page, then selecting Access Tokens from the menu. As with Personal Access Tokens, this table displays all tokens belonging to your organization, and at what time they were last successfully used to carry out an operation. Only organization admins of an organization with an Enterprise or Business Critical subscription will see access to this page.

## Deleting an Organization Access Token

An Organization Access Token can be deleted by any organization admin at any time. No other members are able to delete organization tokens.

From the organization's homepage, follow the same steps as for a Personal Access Token:

1. Select **Settings**.
1. Navigate to **Access Tokens**.
1. Select the ellipsis button.
1. Choose **Delete token**. You will be prompted in a dialog to confirm your choice.

If you choose to delete a token, its access will immediately be revoked and all further operations using it will fail as unauthorized.

## Auditing Organization Token Actions

Since an organization can have multiple Organization Access Tokens, it’s necessary to be able to identify them uniquely in Audit Log Events. All Audit Log Events which were triggered by an Organization Access Token will surface the token’s unique name, and in the event of Audit Log Export, the token’s UUID as well.

## Permissions/Authorization

Organization Access Tokens behave like an organization member with [stack write permissions](https://www.pulumi.com/docs/intro/pulumi-service/projects-and-stacks/#stack-permissions) to all of the organization’s stacks. They do not grant any privileges to view the Pulumi Service ui, or to create additional Organization or Personal Access Tokens. See below for a full list of accessible APIs:

### API Access

See the Pulumi [Service REST API docs](https://www.pulumi.com/docs/reference/service-rest-api/) for more information about each API endpoint.

#### Stacks

| Action | Org Token Access |
|--------|------|
| List Stacks | ✅ |
| Get Stack | ✅ |
| Get Stack State | ✅ |
| Transfer Stack |  |
| Delete Stack | ✅ |

#### Stack Tags

| Action | Org Token Access |
|--------|------|
| Get Stack Tags | ✅ |
| Set Stack Tag | ✅ |
| Delete Stack Tag | ✅ |

#### Stack Updates

| Action | Org Token Access |
|--------|------|
| List Stack Updates | ✅ |
| Get Update Status | ✅ |
| List Update Events | ✅ |
| List Previews | ✅ |

#### Organizations

| Action | Org Token Access |
|--------|------|
| List Users | ✅ |
| Add User to Organization |  |
| Remove User from Organization |  |
| Create Team | ✅ |
| Delete Team | ✅ |
| Update Team Membership |  |
| Grant Stack Access to Team |  |
| Remove Stack Access from Team |  |
| Update User’s Role |  |
| List User Access Tokens |  |
| Create User Access Token |  |
| Delete User Access Token |  |
| Create Webhook | ✅ |
| List Webhooks | ✅ |
| Get Webhook | ✅ |
| Ping Webhook | ✅ |
| List Webhooks Deliveries | ✅ |

#### Audit Logs

| Action | Org Token Access |
|--------|------|
| Get Audit Log Events (JSON) | ✅ |
| Export Audit Log Events (CSV or CEF) | ✅ |
