---
title_tag: Frequently Asked Questions (FAQ) | SCIM
meta_desc: This page describes how to resolve issues that may occur when configuring SCIM provisioning
title: FAQ
h1: Pulumi Cloud SCIM FAQ
menu:
    pulumicloud:
        identifier: faq-scim
        parent: scim
        weight: 4
aliases:
  - /docs/guides/scim/faq/
---

## FAQ

This page contains information on how to resolve issues that may occur when configuring SCIM provisioning.

### A failure occurred when attempting to provision a user.

This failure occurred because there is a conflict with an existing user account in the Pulumi Cloud application. When this occurs our service returns a 409 HTTP response code, indicating a conflict, which you should be able to see in your identity provider's (e.g. Okta, Azure AD) console logs. This means that there is a conflict with an existing account that already contains either that user's username or email. These attributes must be unique for each user in our system which is why the provisioning failed. The steps below describe the process needed to resolve the conflict.

**Resolving an email conflict** - This occurs when the user being provisioned has already created a Pulumi account with the same email address. The conflict must be resolved by changing the email associated with their Pulumi account and releasing it from our system or connecting the existing account to the new account being provisioned. If you encounter this issue, please contact our [customer support](https://support.pulumi.com/) for assistance.

**Resolving a username conflict** - This occurs when the user being provisioned has the same username as an existing account in the Pulumi Cloud. This does not guarantee that the usernames in conflict both belong to the same individual since a username is not something guaranteed to be unique across multiple applications. Therefore connecting to the existing account is not an option in this case since we do not know for sure they are owned by the same individual. The suggested way to resolve this conflict would be to update the username attribute in your identity provider’s console if your identity provider allows. _This action must be done by an admin on the identity provider side (e.g. Okta)_.

1. Navigate to the user's profile settings in your identity provider's console.
2. Next change the username attribute to a different value.
3. Retry provisioning that user. This should now succeed if the username is now unique in the Pulumi Cloud.

If your identity provider doesn't allow you to control the username attribute's value, please contact our [customer support](https://support.pulumi.com/) for assistance.

### Can I manage Pulumi-local teams if using SCIM?

Yes. In addition to the SCIM-managed teams, one can also configure and manage Pulumi-local teams in the Pulumi Cloud. See [Teams](/docs/pulumi-cloud/access-management/teams/) for how to configure teams in the Pulumi Cloud.

## More FAQ

* [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
* [Policy as code FAQ](/docs/using-pulumi/crossguard/faq/)
* [Pulumi Deployments FAQ](/docs/pulumi-cloud/deployments/faq/)
* [Pulumi CLI & Pulumi Cloud FAQ](/docs/support/faq/)
