---
title_tag: SAML Admin | SAML SSO
meta_desc: Learn about the SAML admin role and how to configure it in Pulumi Cloud.
title: SAML admin
h1: SAML admin
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: SAML admin
    parent: administration-access-identity-saml
    weight: 70
    identifier: pulumi-cloud-access-management-saml-admin
---

A SAML admin can log in to your Pulumi organization using an alternative login method. This ensures someone can always log in to your organization to help resolve errors with the SAML configuration.

Whoever configures SAML for your organization is automatically made the SAML admin. To change the SAML admin:

1. Navigate to **Settings** > **Access Management**.
1. Select the **SAML & SCIM** tab.
1. In the **SAML SSO** section, select the **SAML Admin** dropdown.
1. Select a new SAML admin from the list.

{{% notes type="info" %}}
Only organization admins can be SAML admins. If you want to designate a member or billing manager as the SAML admin, you will first need to change their role to admin, then make them a SAML admin.
{{% /notes %}}

{{% notes type="warning" %}}
When a user stops being a SAML admin, they will automatically lose all other login methods.
{{% /notes %}}

Only one SAML admin per organization is supported at this time.
