---
title: Environments
title_tag: Pulumi ESC Environments | Pulumi Concepts
h1: Pulumi ESC Environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  pulumicloud:
    parent: esc
    identifier: environments
    weight: 2
search:
  boost: true
  keywords:
    - environments
    - secrets
    - configuration
---

Pulumi ESC (Environments, Secrets, and Configuration) enables teams to create collections of configuration and secrets called environments. Teams can then access those environment collections using the `esc` CLI, `pulumi` CLI, Pulumi SDK, or Pulumi Cloud REST API for various application and infrastructure needs. These environments can be composed of other environments to allow teams increased flexibility and fine-grained access control. Teams can have as many environments as they need.

Environments have built-in support for dynamic secret and config providers allowing for security and infrastructure best practices such as short-term credentials via OIDC and dynamically pulling secret values as needed for all major cloud providers.

{{% notes type="info" %}}
The examples below use the new standalone `esc` CLI, but all `esc` subcommands are available in the `pulumi` CLI as well. The `pulumi` CLI also has native support for Pulumi ESC environments via `pulumi preview` and `pulumi up`. See [Using with Pulumi IaC](#using-with-pulumi-iac) below for details.
{{% /notes %}}

## Create a new environment

To create a new environment, use `esc env init orgName/environmentName`.  This creates an empty environment.

The environment name must be unique within the organization. Environment names may only contain alphanumeric characters, hyphens, underscores, or periods.

```bash
$ esc env init myorg/test
```

The environment name must be specified in the `orgName/environmentName` format which identifies the environment `environmentName` in the organization `orgName`.

## Listing environments

To see the list of environments, use `esc env ls`:

```bash
$ esc env ls
myorg/dev
myorg/test
myorg/prod
```

Only the environments the user has access to will be listed.

## Set and get values

### Set a value

To set a value, use `esc env set orgName/environmentName key value`:

```bash
$ esc env set myorg/test foo bar
```

### Get a value

To get a preview of that value, use `esc env set orgName/environmentName key`:

```bash
$ esc env get myorg/test foo

   Value

    "bar"

   Definition

    bar

  Defined at

  • test:2:10
```

{{% notes type="info" %}}
Please note that `get` does not resolve providers or secrets. In that case it will display the definition and [unknown] for the value.  To resolve secret or provider values, you need to [open the environment](#getting-access-to-secret-values).
{{% /notes %}}

### Get all values

To get all values, run `esc env get orgName/environmentName`:

```bash
$ esc env get myorg/test

   Value

    {
      "foo": "bar"
    }

   Definition

    values:
      foo: bar
```

You can also get values in a different formats, for example:

```bash
$ esc env get myorg/test --value json
{
  "foo": "bar"
}

$ esc env get myorg/test foo --value json
"bar"
```

### Structured Configuration

Structured configuration is also supported and can be set using `esc env set orgName/environment name key value`, where the key parameter can use either object-property (`.`) or array `[]` syntax. For example:

```bash
$ esc env set myorg/test 'data.active' true
$ esc env set myorg/test 'data.nums[0]' 1
$ esc env set myorg/test 'data.nums[1]' 2
$ esc env get myorg/test

   Value

    {
      "data": {
        "active": true,
        "nums": [
          1,
          2
        ]
      },
      "foo": "bar"
    }

   Definition

    values:
      data:
        active: true
        nums:
          - 1
          - 2
      foo: bar
```

`true` and `false` values are persisted as boolean values, and values convertible to integers are persisted as integers.

You can also get any specific value at any level of the config hierarchy.  For example:

```bash
$ esc env get myorg/test data.nums[1]

   Value

    2

   Definition

    2


   Defined at

  • test:6:15
```

### Interpolated values

Values do not have to be static. You can use interpolation to dynamically compose values from other values. For example:

```bash
$ esc env set myorg/test salutation Hello
$ esc env set myorg/test greeting '${salutation}, ${name}'
$ esc env get myorg/test greeting

   Value

    "Hello, World"

   Definition

    ${salutation}, ${name}


   Defined at

  • test:10:15
```

### Editing config as YAML with the CLI

To edit config in a default editor, use `pulumi edit orgName/environmentName`:

```bash
$ esc env edit myorg/test
```

By default this will drop you into your `$EDITOR`, or `vi` as a fallback.

```shell
values:
    data:
        active: true
        nums:
            - 1
            - 2
    foo: bar
    salutation: Hello
    name: World
    greeting: ${salutation}, ${name}
---
# Please edit the environment definition above.
# The object below is the current result of
# evaluating the environment and will not be
# saved. An empty definition aborts the edit.

{
  "data": {
    "active": true,
    "nums": [
      1,
      2
    ]
  },
  "foo": "bar",
  "greeting": "Hello, World",
  "name": "World",
  "salutation": "Hello"
}
~
~
~
~
"/tmp/122663818.yaml" 29L, 528B
```

You can also specify your editor using the `--editor` flag, such as:

```bash
$ esc env edit --editor="code --wait" myorg/test
```

Run `esc edit --help` for more options.

### Editing config as YAML in the Pulumi Cloud console

Navigate to your organization in the Pulumi Cloud console, choose environments in the left-hand navigation, and select your environment.

![Environments Intelligent YAML Editor](/images/docs/concepts/environments-editor.png)

## Adding OIDC and Secrets providers

So far we have been looking at static config.  What about dynamic config or secrets?

Let's pull in some AWS secrets and wire up OIDC config.  Here is a sample yaml config we can add to our environment:

```yaml
  aws:
    region: us-west-2
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::************:role/deploy-oidc
          sessionName: pulumi-environments-session
  secrets:
    fn::open::aws-secrets:
      region: us-west-2
      login: ${aws.login}
      get:
        paymentsApiKey:
          secretId: path/to/aws/secret
```

Please note that the secrets provider is leveraging the OIDC provider to login and retrieve secrets in this example.

## Getting access to secret values

So far, in our examples we have been previewing static values.

For example if you try to get the value of `aws` in the config right now, it will show `[unknown]`.

In order to see secrets, you need to "open" the environment using `esc env open orgName/environmentName`. For example:

```bash
$ esc env open myorg/test
{
  "aws": {
    "creds": {
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      "sessionToken": "eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTY1NzA3NTIsImV4cCI6MTcyODEwNjc1MiwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0"
    }
  },
  "secrets": {
    "paymentApiKey": "prod_4kcdWj8ZfdBfgjQea135DU00EXAMPLE"
  }
}
```

You can also open and retrieve the value of a specific key, like this:

```bash
$ esc open myorg/test secrets.paymentApiKey
"prod_4kcdWj8ZfdBfgjQea135DU00EXAMPLE"
```

## Projecting Environment Variables

By default, Pulumi ESC does not make assumptions about what values you want to project as Environment Variables or Pulumi Stack config.  This allows you to control the level of exposure for your config/secrets.

### Projecting environment variables

To project environment variables, you can use static or interpolated values, just use the `environmentVariables` parent key.

```yaml
values:
  aws:
    login:
      # provider definition ommited for brevity
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.creds.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.creds.sessionToken}
    MY_ENV_VAR: "true"
```

Now you can see those project environment variables if you open the environment with the `-f shell` or `-f dotenv` option.

```bash
$ esc open -f shell myorg/test
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTY1NzA3NTIsImV4cCI6MTcyODEwNjc1MiwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0"
export MY_ENV_VAR="true"

$ esc open -f dotenv myorg/test
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTY1NzA3NTIsImV4cCI6MTcyODEwNjc1MiwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0"
MY_ENV_VAR="true"
```

You can evaluate those environment variables in your current shell with:

```yaml
$ eval $(esc open -f shell myorg/test)
```

## Running third party commands using Pulumi ESC secrets and config

In are examples so far, we have wired up OIDC and secrets providers, and projected those values as environment variables.

Now we can use that data to run commands without even seeing those secrets at all.  For example, maybe you need to connect using the aws command line to a specific environment, you can use `esc run orgName/environmentName command`.

```bash
$ esc run orgName/environmentName aws s3 ls
2023-05-03 16:09:19 my-s3-bucket
2021-03-14 15:12:42 other-s3-bucket
```

If there are `--` flags in your command, use `--` before your command.

For more options, please run `esc run --help`.

## Composing configuration with imports

There is often shared config in organizations. To prevent copy paste and allow fine grained access control, Pulumi ESC support importing environments from other environments.

Imagine you have a environment `prod` with values like this:

`prod`

```yaml
values:
  environmentName: prod
  instanceType: m5.4xlarge
```

And a region environment `us-west-2` defined as:

`us-west-2`

```yaml
values:
  region: us-west-2
  regionCache: redis-endpoint.us-west-2
```

You can import those environment definitions into your services environment using the imports keyword.

`billing`

```yaml
imports:
- prod
- us-west-2
values:
  serviceName: billing
```

When we run `esc env open` on that environment we get the combined values:

```bash
$ esc open myorg/test
{
  "environmentName": "prod",
  "instanceType": "m5.4xlarge",
  "region": "us-west-2",
  "regionCache": "redis-endpoint.us-west-2",
  "serviceName": "billing"
}
```

Environments can import environments, which also import other environments, which allows you to compose environments to meet any need.

## Using with Pulumi IaC

Now let's incorporate Pulumi ESC into a Pulumi IaC program.

### Projecting Pulumi config

To project Pulumi config for use in your Pulumi stacks, use the `pulumiConfig` key.  For example, we can project the payment api secret we pulled in from AWS in earlier examples:

```yaml
values:
  aws:
    region: us-west-2
    login:
      # OIDC provider ommitted for brevity
  secrets:
    fn::open::aws-secrets:
      region: ${aws.region}
      login: ${aws.login}
      get:
        paymentsApiKey:
          secretId: path/to/aws/secret
  pulumiConfig:
    paymentsApiKey: ${secrets.paymentApiKey}
```

### Referencing an environment in your Pulumi stack config.

In order to reference an environment, we just add a new `environment:` section at the top level of our stack yaml file.

`pulumi.<stack>.yaml`

```yaml
environment:
  - test
config:
  # normal pulumi config
```

Now you can run `pulumi up` as normal:

```bash
$ pulumi stack select test
$ pulumi up
```

You cannot specify the organization in the environment reference, as your stack is already tied to the organization.

This will pull in the environment and any pulumi config will be available just like normal pulumi config.

## Removing an environment

To remove an environment, you can use `esc env rm orgName/environmentName`.

```bash
$ esc env rm myorg/test
This will permanently remove the "myorg/test" environment!
Please confirm that this is what you'd like to do by typing `test/test`:
```
