---
title: Working with environments
title_tag: Pulumi ESC environments
h1: Pulumi ESC environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  pulumiesc:
    identifier: working-with-environments
    parent: esc-environments
    weight: 1
search:
  boost: true
  keywords:
    - environments
    - secrets
    - configuration
aliases:
  - /docs/pulumi-cloud/esc/environments/
  - /docs/esc/environments/
---

{{% notes type="info" %}}
The examples below use the `esc` CLI, but all `esc` subcommands are available on the `pulumi` CLI as well. The `pulumi` CLI also provides fully integrated support for configuring Pulumi stacks with Pulumi ESC. See [Using with Pulumi IaC](/docs/esc/integrations/infrastructure/pulumi-iac/) for details.
{{% /notes %}}

## Creating a new environment

To create a new, empty environment, use `esc env init [<org-name>/]<environment-name>`, where `<org-name>` is optional and defaults to your Pulumi Cloud username.

Environment names must be unique within an organization and may only contain alphanumeric characters, hyphens, underscores, and periods.

```bash
$ esc env init myorg/test
Environment created.
```

## Listing environments

To list the environments you have access to, use `esc env ls`:

```bash
$ esc env ls
myorg/test
```

You can filter this list to a particular organization by passing its name:

```bash
$ esc env ls --organization myorg
myorg/test
```

## Getting and setting environment values

### Setting a value

To set a new value or update an existing value, use `esc env set <key> <value>`:

```bash
$ esc env set myorg/test foo bar
```

### Getting a value

To retrieve a single value and its definition, use `esc env get <environment-name> <key>`:

```bash
$ esc env get myorg/test foo

   Value

    "bar"

   Definition

    bar


   Defined at

  • test:2:10
```

{{% notes type="warning" %}}

**Why is the value shown as `[unknown]`?**

The command `esc env get` returns statically defined plain-text values and definitions. It does **not** return secrets defined in the environment nor resolves values from specified provider configuration, therefore, attempting to `get` a secret results in an `[unknown]` output.

Use [`esc env open`](#opening-an-environment) to access secrets; this opens the environment and resolves dynamically retrieved values or secrets.

{{% /notes %}}

### Getting all values

To retrieve all values in an environment, run `esc env get <environment-name>`:

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

You can also get values in other formats, such as `json`, `dotenv`, or `shell`:

```bash
$ esc env get myorg/test --value json
{
  "foo": "bar"
}

$ esc env get myorg/test foo --value json
"bar"
```

Note that the `dotenv` and `shell` options return values only when an environment defines one or more environment variables. See [Projecting environment variables](#projecting-environment-variables) for details.

### Structured configuration

Structured data like maps and arrays can also be set with `esc env set <environment-name> <key> <value>` using object-property (`.`) or array (`[]`) syntax:

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
    foo: bar
    data:
      active: true
      nums:
        - 1
        - 2
```

Boolean and numeric values are implicitly converted and persisted in their respective types.

You can also fetch individual values at any level in the hierarchy. For example, to fetch the second item from the nested array in the example above:

```bash
$ esc env get myorg/test 'data.nums[1]'

   Value

    2

   Definition

    2


   Defined at

  • test:7:15
```

### Interpolating values

Values don't have to be static. You can also use string interpolation to transform values or compose new values from other values. For example:

```bash
$ esc env set myorg/test salutation Hello
$ esc env set myorg/test name World
$ esc env set myorg/test greeting '${salutation}, ${name}'
$ esc env get myorg/test greeting

   Value

    "Hello, World"

   Definition

    ${salutation}, ${name}


   Defined at

  • test:10:15
```

### Pulumi Contextual information

Contextual information is available and can be used to interpolate on any environment value.

```yaml
values:
  personalNamespace: ${context.rootEnvironment.name}/${context.pulumi.user.login}
```

It can be accessed through the `context` attribute with the following options:

* `context.rootEnvironment.name`: the name of the root environment being evaluated
* `context.currentEnvironment.name`: the name of the current environment being evaluated
* `context.pulumi.user.login`: the user login identifier
* `context.pulumi.organization.login`: the organization login identifier

## Editing environments

Environments may be edited in a number of ways.

### With the Pulumi ESC CLI

To edit an environment using your shell's default text editor (as defined by the `$EDITOR` environment variable), use `esc env edit <environment-name>`:

```bash
$ esc env edit myorg/test
```

When `$EDITOR` is unset, `esc` uses `vi` as a fallback:

```
values:
    foo: bar
    data:
        active: true
        nums:
            - 1
            - 2
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
"/tmp/2198639483.yaml" 29L, 528B
```

You can also specify the editor you want to use by passing its name with the `--editor` flag:

```bash
$ esc env edit --editor="code" myorg/test
```

Doing so overrides any value set in `$EDITOR`. See `esc env edit --help` for more options.

### In the Pulumi Cloud console

To edit an environment in the Pulumi Cloud console, select your organization, choose Environments in the left-hand menu, and select the environment you wish to edit:

![Environments Intelligent YAML Editor](/images/docs/concepts/environments-editor.png)

Click Save to apply your changes immediately or Delete to remove the environment.

### With the Pulumi Cloud REST API

You can also use the Pulumi Cloud REST API to perform standard CRUD operations on your environments. See the [Environments section of the REST API docs](/docs/pulumi-cloud/cloud-rest-api/#environments) for details.

## Using secrets providers and OIDC

In addition to static and interpolated values, environments can incorporate dynamically retrieved settings and secrets from many [supported providers](/docs/esc/integrations/), including cloud providers via OpenID Connect (OIDC).

The following example combines the [`aws-login`](/docs/esc/integrations/dynamic-login-credentials/aws-login/) and [`aws-secrets`](/docs/esc/integrations/dynamic-secrets/aws-secrets/) providers to obtain short-lived credentials from AWS to pull two secrets from AWS Secrets Manager (`api-key` and `app-secret`) into an environment:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::01234567891011:role/some-role
          sessionName: some-session

    secrets:
      fn::open::aws-secrets:
        region: us-west-1
        login: ${aws.login}
        get:
          api-key:
            secretId: api-key
          app-secret:
            secretId: app-secret
```

## Opening an environment {#opening-an-environment}

As mentioned, `esc env get` doesn't resolve dynamic or secret values --- for example, those managed with third-party services like AWS Secrets Manager. Instead, to gain access to these values, you must _open_ the environment.

To do so, use `esc env open <environment-name>`:

```bash
$ esc env open myorg/test
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
  "salutation": "Hello",
  "aws": {
    "login": {
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE",
      "sessionToken": "eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOEXAMPLE"
    },
    "secrets": {
      "api-key": "{\"keyName\":\"keyValue\"}",
      "app-secret": "{\"secretName\":\"secretValue\"}"
    }
  }
}
```

You can also use `open` to resolve the value of an individual key:

```bash
$ esc env open myorg/test 'data.active'
true

$ esc env open myorg/test 'data.nums'
[
  1,
  2
]

$ esc env open myorg/test 'aws.secrets.app-secret' | jq -r 'fromjson | . .secretName'
secretValue
```

## Projecting environment variables

Pulumi ESC can automatically project the settings of a given environment as a set of environment variables. This projection does not happen by default, however; instead, you must define which settings to project, as well as how to name and format them.

Environment variables are defined under the optional `environmentVariables` key, which can accept either static or interpolated values based on settings defined within the environment or [imported](/docs/esc/environments/imports/) from other environments:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::01234567891011:role/some-role
          sessionName: some-session

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    MY_ENV_VAR: "true"
```

To render these `environmentVariables` for use in the shell, use `esc env open`, passing either `--format shell` or `--format dotenv`:

```bash
$ esc env open myorg/test --format shell
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
export AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOEXAMPLE"
export MY_ENV_VAR="true"

$ esc env open myorg/test --format dotenv
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOEXAMPLE"
MY_ENV_VAR="true"
```

Export them into the current shell using `eval` or similar:

```yaml
$ eval $(esc env open myorg/test --format shell)
$ echo $MY_ENV_VAR
true
```

## Precedence rules

When multiple environment sources are combined and settings overlap, values are applied successively in the order in which they're imported and defined.

For example, in the following scenario, three environments define a key `foo`, each with a different value. The third environment, `environment-c`, imports `environment-a` and `environment-b` (importantly, in that order):

```yaml
# environment-a
values:
  foo: bar
```

```yaml
# environment-b
imports:
  - environment-a
values:
  foo: baz
  pulumiConfig:
    foo: ${foo}
```

```yaml
# environment-c
imports:
  - environment-a
  - environment-b
values:
  foo: qux
  pulumiConfig:
    foo: ${foo}
```

Notice how the value of `foo` is overwritten with each successive environment:

```bash
$ esc env open environment-a foo
"bar"

$ esc env open environment-b foo
"baz"

$ esc env open environment-c foo
"qux"

$ pulumi preview
Diagnostics:
  pulumi:pulumi:Stack (dev):
    { foo: 'qux' }
```

Also notice that when the local definition of `foo` is removed from `environment-c` and its imports are reordered, the value of `foo` changes to reflect the value inherited from `environment-a` --- i.e., the last-imported one:

```yaml
# environment-c
imports:
  - environment-b
  - environment-a
values:
  pulumiConfig:
    foo: ${foo}
```

```bash
$ esc env open environment-c foo
"bar"

$ pulumi preview
Diagnostics:
  pulumi:pulumi:Stack (dev):
    { foo: 'bar' }
```

To unset a value inherited from another environment, overwrite it with `null`.

## Deleting an environment

To remove an environment, use `esc env rm [<org-name>/]<environment-name>`:

```bash
$ esc env rm myorg/test
This will permanently remove the "myorg/test" environment!
Please confirm that this is what you'd like to do by typing `myorg/test`: myorg/test
Environment "myorg/test" has been removed!
```

## Renaming an environment

Environments cannot be renamed. However, you can achieve the same result by creating a new environment with the desired name, copying over all configurations and secrets from the original environment, and then deleting the old one.
