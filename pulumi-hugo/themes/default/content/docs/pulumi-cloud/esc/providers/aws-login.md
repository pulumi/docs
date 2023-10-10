---
title_tag: aws-login Pulumi ESC Provider
meta_desc: The aws-login Pulumi ESC Provider enables you to log in to AWS using OIDC or static credentials.
title: aws-login
h1: aws-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: aws
        parent: esc-providers
        weight: 1
---

The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or by providing static credentials. The provider will return a set of credentials that can be used to access AWS resources or fetch secrets using the `aws-secrets` provider.

## Example

```yaml
aws:
  login:
    fn::open::aws-login:
      oidc:
        roleArn: arn:aws:iam::123456789:role/esc-oidc
        sessionName: pulumi-environments-session
```

## Configuring OIDC

To add the Pulumi Cloud as an OIDC provider for IAM, see the [relevant AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

* For the provider URL, use `https://api.pulumi.com/oidc`
* For the audience, use the name of your organization

### Configuring the IAM Role and Trust Policy

To configure the role and trust in IAM, see the AWS documentation for [creating a role for web identity or OpenID connect federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create).

* For the identity provider, choose the provider you created above
* For the audience, choose the name of your organization

For more granular access control, edit the trust policy to add the `sub` claim to the policy's conditions with an appropriate pattern. In the following example, the role may only be assigned by the `core` Environment:

```json
"Condition": {
  "StringLike": {
    "api.pulumi.com/oidc:aud": "<organization name>",
    "api.pulumi.com/oidc:sub": "pulumi:environments:org:<organization name>:env:core"
  }
}
```

Make a note of the IAM role's ARN; it will be a necessary input to the `aws-login` provider.

## Inputs

| Property | Type                              | Description                                                       |
|----------|-----------------------------------|-------------------------------------------------------------------|
| `oidc`   | [AWSLoginOIDC](#awsloginoidc)     | [Optional] - OIDC configuration to log in to AWS.                 |
| `static` | [AWSLoginStatic](#awsloginstatic) | [Optional] - A static set of credentials to use to log in to AWS. |

### AWSLoginOIDC

| Property      | Type     | Description                                                             |
|---------------|----------|-------------------------------------------------------------------------|
| `roleArn`     | string   | The ARN of the role to assume.                                          |
| `sessionName` | string   | The name of the role session.                                           |
| `duration`    | string   | [Optional] - The duration of the role session.                          |
| `policyArn`   | string[] | [Optional] - ARNs for additional policies to apply to the role session. |

### AWSLoginStatic

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

## Outputs

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |
