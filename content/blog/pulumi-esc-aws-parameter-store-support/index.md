---
title: "Announcing AWS Systems Manager - Parameter Store Support for Pulumi ESC"
date: 2024-12-16T12:00:00-06:00
allow_long_title: true
meta_desc: "Pulumi ESC adds integration support for AWS Parameter Store"
meta_image: meta.png
authors:
  - sean-yeh
  - cleve-littlefield
tags:
  - esc
  - secrets
  - aws
  - features

search:
  keywords:
    - AWS
    - Parameter
    - AWS Parameter
    - Parameter Store
---

We are super excited to announce integration support for AWS Systems Manager - Parameter Store within Pulumi Environments, Secrets, and Configuration ([ESC](/product/esc)). Parameter Store is a popular managed service by AWS for storing and managing secrets and other configuration, and its integration with ESC has been highly requested among the community.

<!--more-->

With the AWS Parameter Store ESC Provider, development teams can now import their AWS Parameter Store parameters as [environment variables](/docs/esc/environments/working-with-environments/#projecting-environment-variables) or as [Pulumi Config](/docs/esc/integrations/infrastructure/pulumi-iac/) in their workflows, all in a secure and convenient way.

As we continue to expand our roster of integrations, it's easier now than ever to manage and use secrets and configuration all in one place by using ESC. If you or your team are users of AWS Parameter Store, say goodbye to managing multiple configuration sources and give this provider a try!

## How does it work?

1. Add parameters to AWS Parameter Store.
2. Use [aws-login](/docs/esc/integrations/dynamic-login-credentials/aws-login/) to authenticate with AWS.
3. Define a path name, and enter the parameter name you want to retrieve. This will be imported into the path name that you have defined.

**AWS Parameter Store provider syntax:**

```yaml
values:
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
```

## Demo

Now that we know how to use the Pulumi ESC Parameter Store provider, let's use it to pull some parameters!

* Setup [OpenID Connect for AWS](/docs/pulumi-cloud/access-management/oidc/provider/aws/). We will use OIDC to authenticate with AWS.
* Store some parameters in Parameter Store. In the demo, we will store a String `/test/api-endpoint` and a SecureString `/test/api-key`
* Create a new Pulumi ESC Environment with the following definition. Make sure to replace the OIDC `roleArn` with your own.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789:role/esc-oidc
          sessionName: pulumi-environments-session
  params:
    fn::open::aws-parameter-store:
      region: us-west-1
      login: ${aws.login}
      get:
        api-endpoint:
          name: /test/api-endpoint
        api-key:
          name: /test/api-key
          decrypt: true
  environmentVariables:
    API_ENDPOINT: ${params.api-endpoint}
    API_KEY: ${params.api-key}
 ```

* Open the environment to ensure we are able to successfully pull the credentials from AWS Parameter Store
* Run `esc open <project/environment> --format shell` to view the exported environment variables from this ESC environment.
* Use [ESC run](/docs/esc/cli/commands/esc_run/) to run any command with these environment variables. For example, we can now run `esc run <project/environment> -- <your command>`

`esc run` passes the configuration stored under the `environmentVariables` section for use with the provided command, without ever storing them locally on your machine.

## Conclusion
We are excited to expand our roster of integrations with the new AWS Parameter Store ESC Provider, providing developers more flexibility and choices. We look forward to seeing what you will create next using Pulumi ESC!

* Visit the [AWS Parameter Store Provider Page](/docs/esc/integrations/dynamic-secrets/aws-parameter-store/) for more detailed documentation on this provider.
* Visit our [Pulumi ESC docs](/docs/esc/) to learn more about Pulumi ESC and its supported [integrations](/docs/esc/integrations/)

As always, we deeply value your insights. Your [feedback](https://github.com/pulumi/esc/issues/new/choose) is instrumental in helping us refine and enhance our solutions to better align with your needs.
