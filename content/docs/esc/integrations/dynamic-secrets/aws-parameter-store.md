---
title: aws-parameter-store
title_tag: aws-parameter-store Pulumi ESC Provider
meta_desc: The aws-parameter-store Pulumi ESC Provider enables you to dynamically import values from AWS Parameter Store.
h1: aws-parameter-store
menu:
  esc:
    identifier: aws-parameter-store
    parent: esc-dynamic-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/aws-parameter-store/
    - /docs/esc/providers/aws-parameter-store/
---

The `aws-parameter-store` provider enables you to dynamically import values of all types (`String`, `SecureString`, `StringList`) from AWS Parameter Store into your Environment. The provider supports all types and will return a map of names to values.

## Example

```yaml
aws:
  login:
    fn::open::aws-login:
      oidc:
        roleArn: arn:aws:iam::123456789:role/esc-oidc
        sessionName: pulumi-environments-session
  params:
    fn::open::aws-parameter-store:
      region: us-west-2
      login: ${aws.login}
      get:
        parameter:
          name: /parameter/name
        versioned_parameter:
          name: /parameter/name:2
        labeled_parameter:
          name: /parameter/name:labelname
        secure_string_parameter:
          name: /parameter/secret
          decrypt: true
```

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, see [Configuring OpenID Connect for AWS](/docs/pulumi-cloud/oidc/provider/aws/). Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `esc open <your-org>/<your-environment>` command of the [Pulumi ESC CLI](/docs/esc-cli/)
* `pulumi env open <your-org>/<your-environment>` command of the [Pulumi CLI](/docs/install/)

Make sure to replace `<your-org>` and `<your-environment>` with the values of your Pulumi organization and environment file respectively. You should see output similar to the following:

```json
{
  "aws": {
    "login": {
      "accessKeyId": "ASIA....",
      "secretAccessKey": "mWdm....",
      "sessionToken": "Fwo...."
    },
    "params": {
      "parameter": "value1",
      "versioned_parameter": "value2",
      "labeled_parameter": "value3",
      "secure_string_parameter": "my-secret"
    }
  }
}
```

## Inputs

| Property | Type                                                     | Description                                                                                                                  |
|----------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `region` | string                                                   | The AWS region to use.                                                                                                       |
| `login`  | [AWSParameterStoreLogin](#awsparameterstorelogin)        | Credentials to use to log in to AWS.                                                                                         |
| `get`    | map[string][AWSParameterStoreGet](#awsparameterstoreget) | A map from names to parameter names to read from AWS Parameter Store. The outputs will map each name to the data.            |

### AWSParameterStoreLogin

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

### AWSParameterStoreGet

| Property  | Type    | Description                                                                                                                              |
|-----------|---------|------------------------------------------------------------------------------------------------------------------------------------------|
| `name`    | string  | The name of the parameter. A version or label can be optionally specified by appending `:` to the name, e.g. `name:123` or `name:label`. |
| `decrypt` | boolean | [Optional] - Whether or not to decrypt (when the parameter is a SecureString). Defaults to `false`.

## Outputs

| Property | Type   | Description                                        |
|----------|--------|----------------------------------------------------|
| N/A      | object | A map of names to imported Parameters.             |
