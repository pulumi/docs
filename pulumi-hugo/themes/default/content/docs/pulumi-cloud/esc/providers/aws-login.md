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

To configure OIDC between Pulumi Cloud and AWS, see the [relevant Pulumi documentation](/docs/pulumi-cloud/oidc/aws/).

## Inputs

| Property | Type                              | Description                                                       |
|----------|-----------------------------------|-------------------------------------------------------------------|
| `oidc`   | [AWSLoginOIDC](#awsloginoidc)     | [Optional] - OIDC configuration to log in to AWS.                 |
| `static` | [AWSLoginStatic](#awsloginstatic) | [Optional] - A static set of credentials to use to log in to AWS. |

### AWSLoginOIDC

| Property      | Type     | Description                                                                                                                                                                                                                                       |
|---------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `roleArn`     | string   | The ARN of the role to assume.                                                                                                                                                                                                                    |
| `sessionName` | string   | The name of the role session.                                                                                                                                                                                                                     |
| `duration`    | string   | [Optional] - The duration of the role session. Defaults to 2 hours. Unless explicitly specified, AWS sets MaxDuration to 1 hour by default. You may need to configure your AWS role with a higher MaxDuration or set the duration here to 1 hour. |
| `policyArn`   | string[] | [Optional] - ARNs for additional policies to apply to the role session.                                                                                                                                                                           |

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
