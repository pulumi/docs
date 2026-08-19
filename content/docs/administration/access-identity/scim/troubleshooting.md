---
title_tag: Troubleshooting | SCIM
meta_desc: Troubleshooting guide for SCIM provisioning issues in Pulumi Cloud.
title: Troubleshooting
h1: SCIM troubleshooting
menu:
  administration:
    name: Troubleshooting
    parent: administration-access-identity-scim
    weight: 80
    identifier: pulumi-cloud-access-management-scim-troubleshooting
aliases:
  - /docs/support/faq/scim/
  - /docs/administration/access-identity/scim/faq/
  - /docs/guides/scim/faq/
  - /docs/pulumi-cloud/access-management/scim/faq/
pulumi_cloud_feature: scim
---

This page describes how to resolve issues that may occur when configuring SCIM provisioning.

## User provisioning failures

These errors can occur when attempting to create (POST), replace (PUT), or update (PATCH) a user. If you encounter difficulties resolving these issues, please contact our [customer support](https://support.pulumi.com/) for assistance.

### Email already in use

```json
{
    "status": "409",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "409",
        "scimType": "uniqueness",
        "detail": "Email {email} already in use by another Pulumi account."
    }
}
```

Cause: The user being provisioned has already created a Pulumi account with the same email address. The email needs to be released from our system before it can be used to provision a new user, or the existing account needs to be connected to the new account being provisioned.

Suggested Resolution: There are three possible solutions. The user can either:

1. Delete their existing Pulumi account
1. Change the email associated with their existing Pulumi account
1. Connect their SAML credentials to their existing Pulumi account by navigating to Account Settings > Connect SAML SSO.

{{% notes type="info" %}}
If the existing account is already managed by SAML SSO in another Pulumi organization, use option 3. Signing in to the new organization directly returns an "Email already in use" screen, and an SSO-managed account cannot clear that screen on its own. Connect the new organization's SAML SSO identity from your account settings instead. See [Connect SAML SSO to an existing account](/docs/administration/access-identity/saml/#connect-saml-sso-to-an-existing-account).
{{% /notes %}}

### `userName` already exists

```json
{
    "status": "409",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "409",
        "scimType": "uniqueness",
        "detail": "User with userName {userName} already exists."
    }
}
```

Cause: The user being provisioned has the same username as an existing account in the Pulumi Cloud.

Suggested Resolution: Update the username attribute in your identity provider’s console if your identity provider allows, then try reprovisioning the user. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

### `userName` is immutable

```json
{
    "status": "400",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "400",
        "scimType": "immutability",
        "detail": "Attribute 'userName' is immutable."
    }
}
```

Cause: Pulumi usernames are immutable and cannot be updated. See [Usernames cannot change](/docs/administration/access-identity/scim/#usernames-cannot-change).

Suggested Resolution: Update the attribute mapping in the identity provider so that `userName` is updated only during creation, not creation and update. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

### Unknown path

```json
{
    "status": "400",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "400",
        "scimType": "invalidPath",
        "detail": "Unknown path: {path}."
    }
}
```

Cause: Pulumi only supports adding or updating the following user attributes:

- `userName`
- `displayName`
- `name.givenName`
- `name.familyName`
- `emails[type eq "work"].value`
- `active`

Provisioning jobs that try to add or update any other attribute fail. For the complete supported surface, including group attributes, see [Supported attributes](/docs/administration/access-identity/scim/#supported-attributes).

Suggested Resolution: Update the attribute mappings in the identity provider and delete all unsupported attributes. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

## Group member provisioning failures

The creation (POST), update (PATCH), or replacement (PUT) of a group performs member validation before running the operation. If any of the members provided are not provisioned into your Pulumi organization, or are not active, the request fails with the following response:

```json
{
    "status": "400",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "400",
        "scimType": "invalidValue",
        "detail": "Cannot add invalid members to team. Invalid member ids: {comma separated list of invalid member ids}"
    }
}
```

The suggested way to resolve this conflict would be to synchronize all the group members to guarantee every member is successfully provisioned and update the user's status. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

## Group provisioning failures

### Display name is too long

```json
{
    "status": "400",
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": "400",
        "scimType": "invalidValue",
        "detail": "Display name is too long. It must be 100 characters or less"
    }
}
```

Cause: Pulumi team names created through SCIM must be 100 characters or fewer, and the group being pushed has a longer display name.

Suggested Resolution: Rename the group in the identity provider so that its name fits within the limit, then push it again. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

## Managing Pulumi-local teams alongside SCIM

Alongside the SCIM-managed teams, you can also configure and manage Pulumi-local teams in the Pulumi Cloud. See [Teams](/docs/administration/organizations-teams/teams/) for how to configure teams in the Pulumi Cloud.

## Learn more

- [SCIM overview](/docs/administration/access-identity/scim/)
- [Pulumi Cloud FAQ](/docs/support/faq/pulumi-cloud/)
- [Getting support](/docs/support/getting-support/)
