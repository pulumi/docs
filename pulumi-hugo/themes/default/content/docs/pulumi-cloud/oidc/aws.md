---
title_tag: Configure OpenID Connect for AWS | OIDC
meta_desc: This page describes how to configure OIDC token exchange in AWS for use with Pulumi Deployments
title: AWS
h1: Configuring OpenID Connect for AWS
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: openid-connect
        weight: 1

aliases:
- /docs/guides/oidc/aws
- /docs/intro/deployments/oidc/aws/
- /docs/pulumi-cloud/deployments/oidc/aws/
---

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with AWS. OIDC in AWS uses a web identity provider to assume an IAM role. Access to the IAM role is authorized using a trust policy that validates the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.

## Adding the identity provider to AWS

To add the Pulumi Cloud as an OIDC provider for IAM, see the [relevant AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

* For the provider URL, use `https://api.pulumi.com/oidc`
* For the audience, use the name of your organization

## Configuring the IAM Role and Trust Policy

To configure the role and trust in IAM, see the AWS documentation for [creating a role for web identity or OpenID connect federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create).

* For the identity provider, choose the provider you created above
* For the audience, choose the name of your organization

For more granular access control, edit the trust policy to add the `sub` claim to the policy's conditions with an appropriate pattern. In the following example, the role may only be assigned by stacks within the "Core" project:

```json
"Condition": {
  "StringLike": {
    "api.pulumi.com/oidc:aud": "<organization name>",
    "api.pulumi.com/oidc:sub": "pulumi:deploy:org:<organization name>:project:Core:*"
  }
}
```

Make a note of the IAM role's ARN; it will be necessary to enable OIDC for your stack.

## Enabling OIDC for your Stack via the Pulumi Console

{{% notes "info" %}}
In addition to the Pulumi Console, deployment settings including OIDC can be configured for a stack using the [pulumiservice.DeploymentSettings](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/deploymentsettings/) resource or via the [REST API](/docs/pulumi-cloud/deployments/api/#patchsettings).
{{% /notes %}}

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable AWS Integration".
5. Enter the ARN of the IAM role to created above in the "Role ARN" field.
6. Enter a name for the assumed role session in the "Session Name" field.
7. If you would like to use additional policies to further constrain the session's capabilities, enter the policies' ARNs separated by commas in the "Policy ARNs" field.
8. If you would like to constrain the duration of the assumed role session, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for AWS credentials using the specified IAM role prior to running any pre-commands or Pulumi operations. The fetched credentials are published in the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
