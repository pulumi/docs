---
title_tag: Frequently Asked Questions (FAQ) | SCIM
meta_desc: This page describes how to resolve issues that may occur when configuring SCIM provisioning
title: SCIM FAQ
h1: SCIM FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  support:
    name: SCIM FAQ
    parent: support-faq
    weight: 4
    identifier: support-faq-scim
aliases:
  - /docs/administration/access-identity/scim/faq/
  - /docs/guides/scim/faq/
  - /docs/pulumi-cloud/access-management/scim/faq/
---

## FAQ

This page contains information on how to resolve issues that may occur when configuring SCIM provisioning.

### A failure occurred when attempting to provision a user.

These errors can occur when attempting to create (POST), replace (PUT), or update (PATCH) a user. If you encounter difficulties resolving these issues, please contact our [customer support](https://support.pulumi.com/) for assistance.

#### Email already in use

```json
{
    "status": 409,
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": 409,
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

#### UserName already exists

```json
{
    "status": 409,
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": 409,
        "scimType": "uniqueness",
        "detail": "User with userName {userName} already exists."
    }
}
```

Cause: The user being provisioned has the same username as an existing account in the Pulumi Cloud.

Suggested Resolution: Update the username attribute in your identity provider’s console if your identity provider allows, then try reprovisioning the user. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

#### UserName is immutable

```json
{
    "status": 400,
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": 400,
        "scimType": "immutability",
        "detail": "Attribute 'userName' is immutable."
    }
}
```

Cause: Pulumi usernames are immutable and cannot be updated.

Suggested Resolution: Update the attribute mapping in the identity provider so that `userName` is updated only during creation, not creation and update. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

#### Unknown path

```json
{
    "status": 400,
    "response": {
        "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
        "status": 400,
        "scimType": "invalidPath",
        "detail": "Unknown path: {path}."
    }
}
```

Cause: Pulumi only supports adding or updating the following user attributes:

- `userName`
- `displayName`
- `givenName`
- `familyName`
- `active`

Provisioning jobs that try to add or update any other attribute will fail.

Suggested Resolution: Update the attribute mappings in the identity provider and delete all unsupported attributes. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

### A failure occurred when attempting to provision group members.

The creation (POST), update (PATCH) or replacement (PUT) of a group performs member validation prior running the operation. If any of the members provided are not provisioned into your Pulumi organization or is not active, the request will fail with the following response:

```
Status: 400 BAD REQUEST
Bad Request: Cannot add invalid members to team. Invalid member ids: [comma separated list of invalid member ids]
```

The suggested way to resolve this conflict would be to synchronize all the group members to guarantee every member is successfully provisioned and update the user's status. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

### Can I manage Pulumi-local teams if using SCIM?

Yes. In addition to the SCIM-managed teams, one can also configure and manage Pulumi-local teams in the Pulumi Cloud. See [Teams](/docs/administration/organizations-teams/teams/) for how to configure teams in the Pulumi Cloud.

## More FAQ

- [Pulumi IaC FAQ](/docs/iac/support/faq/)
- [Pulumi ESC FAQ](/docs/support/faq/secrets-config/)
- [Pulumi Cloud FAQ](/docs/support/pulumi-cloud-faq/)
- [Pulumi Policies FAQ](/docs/support/faq/policies)
