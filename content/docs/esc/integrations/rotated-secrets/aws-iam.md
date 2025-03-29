---
title: aws-iam
title_tag: aws-iam Pulumi ESC Rotator
meta_desc: The `aws-iam` rotator enables you to rotate access credentials for an AWS
  IAM User.
h1: aws-iam
menu:
  esc:
    identifier: aws-iam
    parent: esc-rotated-secrets
    weight: 1
search:
  keywords:
    - aws
    - IAM
    - aws-iam
    - access credentials
    - OpenID Connect
---

The `aws-iam` rotator enables you to rotate access credentials for an AWS IAM user in your Environment. Check out the [aws-login documentation](/docs/esc/integrations/dynamic-login-credentials/aws-login/) to learn more about authenticating with AWS.

## Example

```yaml
# my-org/logins/production
values:
  aws:
    region: us-west-2
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
          subjectAttributes:
            - currentEnvironment.name
```

```yaml
# my-org/rotators/key-rotator
values:
  iam:
    fn::rotate::aws-iam:
      inputs:
        region: ${environments.logins.production.aws.region}
        login: ${environments.logins.production.aws.login}
        userArn: arn:aws:iam::<account id>:user/<username>
```

If you have existing access and secret key(s) you want ESC to keep track of, you can optionally provide an initial `state`.

```yaml
# my-org/rotators/key-rotator
values:
  iam:
    fn::rotate::aws-iam:
      inputs:
        region: ${environments.logins.production.aws.region}
        login: ${environments.logins.production.aws.login}
        userArn: arn:aws:iam::<account id>:user/<username>
      state:
        current:
          accessKeyId: <access key>
          secretAccessKey:
            fn::secret: <secret key>
        previous:
          accessKeyId: <access key>
          secretAccessKey:
            fn::secret: <secret key>
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, see the [OpenID Connect integration](/docs/pulumi-cloud/oidc/provider/aws/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <org>/<project>/<environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<org>`, `<project>`, and `<environment>` with the values of your Pulumi organization and environment identifier respectively. You should see output similar to the following:

```json
{
  "aws": {
    "login": {
      "accessKeyId": "ASIA....",
      "secretAccessKey": "mWdm....",
      "sessionToken": "Fwo...."
    }
  },
  "iam": {
   "current": {
      "accessKeyId": "AKIA...",
      "createdAt": "2025-01-01T12:00:00Z",
      "secretAccessKey": "[secret]"
    },
    "previous": {
      "accessKeyId": "AKIA...",
      "createdAt": "2025-01-01T13:00:00Z",
      "secretAccessKey": "[secret]"
    }
  }
}
```

### Permissions

The minimum permissions required for the rotation role are:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListAccessKeys",
        "iam:CreateAccessKey",
        "iam:DeleteAccessKey",
        "iam:GetUser",
        "iam:TagUser"
      ],
      "Resource": "arn:aws:iam::<account id>:user/<username>"
    }
  ]
}
```

## Inputs

| Property   | Type                                                     | Description                                                                                                              |
|------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `region`   | string                                                   | [Optional] - The AWS region to use.                                                                                      |
| `login`    | [AWSIAMLogin](#awsiamlogin)                              | Credentials to use to log in to AWS.                                                                                     |
| `userArn`  | string                                                   | The ARN of the IAM User.                                                                                                 |

## State (Optional)

| Property | Type                            | Description                                                                                                            |
|----------|---------------------------------|------------------------------------------------------------------------------------------------------------------------|
| current  | [AWSIAMOutputs](#awsiamoutputs) | [Optional] - Current credential information. These are the newest and recommended credentials.                         |
| previous | [AWSIAMOutputs](#awsiamoutputs) | [Optional] - Previous credential information. These credentials are still valid, but will be phased out next rotation. |

### AWSIAMLogin

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

## Outputs

| Property | Type                            | Description                                                                                               |
|----------|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| current  | [AWSIAMOutputs](#awsiamoutputs) | Current credential information. These are the newest and recommended credentials.                         |
| previous | [AWSIAMOutputs](#awsiamoutputs) | Previous credential information. These credentials are still valid, but will be phased out next rotation. |

### AWSIAMOutputs

| Property          | Type   | Description                                    |
|-------------------|--------|------------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                          |
| `secretAccessKey` | string | The AWS secret access key, stored as a secret. |
| `createdAt`       | string | Creation timestamp (in RFC3339 format)         |
