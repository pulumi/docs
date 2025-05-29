---
title: aws-secrets
title_tag: aws-secrets Pulumi ESC Provider
meta_desc: The aws-secrets Pulumi ESC Provider enables you to dynamically import Secrets from AWS Secrets Manager.
h1: aws-secrets
menu:
  esc:
    identifier: aws-secrets
    parent: esc-dynamic-secrets
    weight: 2
aliases:
    - /docs/pulumi-cloud/esc/providers/aws-secrets/
    - /docs/esc/providers/aws-secrets/
---

The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment. The provider will return a map of names to Secrets.

## Example: Plain-Text Secrets

The following example demonstrates how to retrieve plain-text (i.e., scalar value) secrets from AWS Secrets Manager:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            # Secret name as shown in the AWS Console, or secret ARN:
            secretId: api-key
          app-secret:
            secretId: app-secret
```

## Example: Key/Value Pair Secrets

The following example demonstrates how to retrieve key/value pair (i.e. JSON) secrets from AWS Secrets Manager and map them to Pulumi IaC configuration values:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          db-creds:
            secretId: prod-db
    secrets-unpacked:
      db-creds:
        fn::fromJSON: ${aws.secrets.my-secret}
  pulumiConfig:
    dbUserName: ${aws.secrets-unpacked.db-creds.userName}
    dbPassword: ${aws.secrets-unpacked.db-creds.password}
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, see [Configuring OpenID Connect for AWS](/docs/esc/environments/configuring-oidc/aws/). Once you have completed these steps, you can validate that your configuration is working by running either of the following:

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
    },
    "secrets": {
      "api-key": "my-api-key",
      "app-secret": "my-app-secret"
    }
  }
}
```

## Inputs

| Property | Type                                       | Description                                                                                                                  |
|----------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `region` | string                                     | The AWS region to use.                                                                                                       |
| `login`  | [AWSSecretsLogin](#awssecretslogin)        | Credentials to use to log in to AWS.                                                                                         |
| `get`    | map[string][AWSSecretsGet](#awssecretsget) | A map from names to secrets to read from AWS Secrets Manager. The outputs will map each name to the secret's sensitive data. |

### AWSSecretsLogin

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

### AWSSecretsGet

| Property       | Type   | Description                                             |
|----------------|--------|---------------------------------------------------------|
| `secretId`     | string | The ID of the secret to import.                         |
| `versionId`    | string | [Optional] - The version of the secret to import.       |
| `versionStage` | string | [Optional] - The version stage of the secret to import. |

## Outputs

| Property | Type   | Description                         |
|----------|--------|-------------------------------------|
| N/A      | object | A map of names to imported Secrets. |
