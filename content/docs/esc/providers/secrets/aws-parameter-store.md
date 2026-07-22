---
title: aws-parameter-store
title_tag: aws-parameter-store Pulumi ESC Provider
meta_desc: The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Systems Manager - Parameter Store.
h1: aws-parameter-store
menu:
  esc:
    identifier: aws-parameter-store
    parent: esc-providers-secrets
    weight: 1
aliases:
    - /docs/pulumi-cloud/esc/providers/aws-parameter-store/
    - /docs/esc/providers/aws-parameter-store/
    - /docs/esc/integrations/dynamic-secrets/aws-parameter-store/
    - /docs/esc/concepts/providers/secrets/aws-parameter-store/
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
  pulumiConfig:
    myKey: ${aws.params.myKey}
    secureKey: ${aws.params.secureKey}
```

## Schema reference

{{< esc-schema-updated >}}

### Inputs

{{< esc-schema type="provider" name="aws-parameter-store" section="inputs" >}}

### Outputs

{{< esc-schema type="provider" name="aws-parameter-store" section="outputs" >}}

## Configuring OIDC

To learn how to configure OpenID Connect (OIDC) between Pulumi Cloud and AWS, see the [OpenID Connect integration](/docs/esc/guides/configuring-oidc/aws/) documentation. Once you have completed these steps, you can validate that your configuration is working by running either of the following:

* `pulumi env open <org>/<project>/<environment>` command of the [Pulumi CLI](/docs/iac/cli/commands/pulumi_env_open/)
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
