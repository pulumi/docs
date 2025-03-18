---
title: aws-parameter-store
title_tag: aws-parameter-store Pulumi ESC Provider
meta_desc: The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Systems Manager - Parameter Store.
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

The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Systems Manager - Parameter Store into your Environment. The provider will return a map of names to parameters.

## Example

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
    params:
      fn::open::aws-parameter-store:
        region: us-west-1
        login: ${aws.login}
        get:
          myKey:
            name: /myNamespace/myKey
          myKeyByVersion:
            name: /myNamespace/myKey:1
          myKeyByVersionLabel:
            name: /myNamespace/myKey:stable
          secureKey:
            name: /myNamespace/secureKey
            decrypt: true
          myList:
            name: /myNamespace/myList
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
    },
    "params": {
      "myKey": "latest value",
      "myKeyByVersion": "old value",
      "myKeyByVersionLabel": "stable value",
      "secureKey": "secret value",
      "myList": [
        "value 1",
        "value 2"
      ]
    }
  }
}
```

## Inputs

| Property | Type                                       | Description                                                                                                                             |
|----------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `region` | string                                                   | The AWS region to use.                                                                                                    |
| `login`  | [AWSParameterStoreLogin](#awsparameterstorelogin)        | Credentials to use to log in to AWS.                                                                                      |
| `get`    | map[string][AWSParameterStoreGet](#awsparameterstoreget) | A map from names to parameters to read from AWS Parameter Store. The outputs will map each name to the parameter's data.  |

### AWSParameterStoreLogin

| Property          | Type   | Description                                 |
|-------------------|--------|---------------------------------------------|
| `accessKeyId`     | string | The AWS access key ID                       |
| `secretAccessKey` | string | The AWS secret access key                   |
| `sessionToken`    | string | [Optional] - The AWS session token, if any. |

### AWSParameterStoreGet

| Property  | Type    | Description                                                                                                                                                |
|-----------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`    | string  | The name of the parameter to import. To query by parameter label, use `"name": "name:label"`. To query by parameter version, use `"name": "name:version"`. |
| `decrypt` | boolean | [Optional] - Whether to decrypt the value.  Only affects values of type SecureString.                                                                      |

## Outputs

| Property | Type   | Description                            |
|----------|--------|----------------------------------------|
| N/A      | object | A map of names to imported parameters. |
