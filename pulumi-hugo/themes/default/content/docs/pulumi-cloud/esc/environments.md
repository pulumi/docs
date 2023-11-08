---
title: Environments
title_tag: Pulumi ESC Environments
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

Pulumi ESC (Environments, Secrets, and Configuration) lets you define collections of configuration settings and secrets called _environments_ and use them in any application or service. Environments are YAML documents composed of static key-value pairs, programmatic expressions, dynamically retrieved values from supported providers including all major clouds through OpenID Connect (OIDC), and other Pulumi ESC environments.

Environments are accessible with the standalone [`esc` CLI](/docs/install/esc/), the [`pulumi` CLI](/docs/install/), the [Pulumi SDK](https://github.com/pulumi/esc/issues/60), and the [Pulumi Cloud console](#editing-an-environment-as-yaml-in-the-pulumi-cloud-console) and [REST API](/docs/pulumi-cloud/cloud-rest-api/#environments), and you can have as many environments as you need. Pulumi ESC is a service of Pulumi Cloud and is currently in public preview.

{{% notes type="info" %}}
The examples below use the new `esc` CLI, but all `esc` subcommands are available on the `pulumi` CLI as well. The `pulumi` CLI also provides fully integrated support for configuring Pulumi stacks with Pulumi ESC. See [Using with Pulumi IaC](#using-environments-with-pulumi-iac) below for details.
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

Note that `esc env get` returns only statically defined plain-text values and definitions; it does not resolve provider-managed values or secrets. (For these, `get` returns the item definition with a value of `[unknown]`.) To resolve dynamically retrieved values or secrets, you must instead [open the environment](#opening-an-environment).

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

In addition to static and interpolated values, environments can incorporate dynamically retrieved settings and secrets from many [supported providers](/docs/pulumi-cloud/esc/providers/), including cloud providers via OpenID Connect (OIDC).

The following example combines the [`aws-login`](/docs/pulumi-cloud/esc/providers/aws-login/) and [`aws-secrets`](/docs/pulumi-cloud/esc/providers/aws-secrets/) providers to obtain short-lived credentials from AWS to pull two secrets from AWS Secrets Manager (`api-key` and `app-secret`) into an environment:

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

Environment variables are defined under the optional `environmentVariables` key, which can accept either static or interpolated values based on settings defined within the environment or [imported](#importing-other-environments) from other environments:

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

## Running commands with environment variables

You can also run CLI commands directly, using environment variables obtained with Pulumi ESC --- without having to export those variables into the shell first.

To do this, use `esc run <environment-name> <command>`:

```bash
$ esc run myorg/test aws s3 ls
2023-10-10 16:09:19 my-s3-bucket
```

If you need to pass one or more flags to the command, prefix the command with `--`:

```bash
$ esc run myorg/test -- aws s3 ls s3://my-s3-bucket --recursive --summarize
...
Total Objects: 5087
   Total Size: 2419123156
```

For additional options and details, see `esc run --help`.

## Importing other environments

Environments can also be composed from other environments.

Different applications are often configured in similar ways and with common values --- for example, an e-commerce site and order-management system both configured to use the same cloud account, database-connection string, and third-party API key. Managing the duplication of these values across multiple configuration files, however, can be difficult, especially when one of those values changes --- e.g., when an API key is regenerated.

To address these challenges, Pulumi ESC allows you to identify common or closely related configuration settings and define them only once, as individual environments, and then _import_ those environments into other, more specialized environments as needed. Imports also allow you to expose certain environments without having to distribute any concrete values and to delegate responsibility for particular environments to other teams in your organization. Environments can import both static and dynamic values, including secrets, from any number of other environments.

In the following example, two environments, `aws-dev` and `stripe-dev`, are used to compose a third environment, `myapp-dev`:

```yaml
# myorg/aws-dev
values:
  aws:
    region: us-west-2
    login:
      fn::open::aws-login:
        static:
          accessKeyId:
            fn::secret: AKIAIOSFODNN7EXAMPLE
          secretAccessKey:
            fn::secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE
```

```yaml
# myorg/stripe-dev
values:
  stripe:
    apiURL: https://api.stripe.com
    apiKey:
      fn::secret: sk_XemWAl12i4x3hZhp4vBKDEXAMPLE
```

The application-specific `myapp-dev` environment then `imports` these two environments and use their settings to compose new values:

```yaml
# myorg/myapp-dev
imports:
  - aws-dev
  - stripe-dev

values:
  greeting: Hello from the dev environment!

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    STRIPE_API_KEY: ${stripe.apiKey}
    STRIPE_API_URL: ${stripe.apiURL}
    GREETING: ${greeting}
```

Finally, `esc run` renders `myapp-dev`'s environment variables for use on the command line:

```bash
$ esc run myorg/myapp-dev -- bash -c 'echo $GREETING'
Hello from the dev environment!

$ esc run myorg/myapp-dev -- bash -c 'echo $STRIPE_API_URL'
https://api.stripe.com

$ esc run myorg/myapp-dev -- bash -c 'echo $STRIPE_API_KEY'
[secret]

$ esc run myorg/myapp-dev -- bash -c 'echo $AWS_SECRET_ACCESS_KEY'
[secret]

$ echo "'$GREETING'"
''
```

Notice in the example that the `environmentVariables` were exposed to the `bash` command, but not to the surrounding shell, and that the values marked as secrets with `fn::secret` were protected from exposure.

## Using environments with Pulumi IaC

With support for Pulumi ESC built into the Pulumi CLI, you can expose an environment's settings and secrets to any or all of your Pulumi stacks, bypassing the need to define and maintain individual configuration settings or secrets "locally" in Pulumi config files. The optional `pulumiConfig` key enables this.

The following example updates the `myorg/myapp-dev` environment by adding a `pulumiConfig` block. This block specifies the [Pulumi configuration](/docs/concepts/config/) settings to expose to the Pulumi stack at runtime:

```yaml
# myorg/myapp-dev
imports:
  - aws-dev
  - stripe-dev

values:
  greeting: Hello from the dev environment!

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    STRIPE_API_KEY: ${stripe.apiKey}
    STRIPE_API_URL: ${stripe.apiURL}
    GREETING: ${greeting}

  # Add a `pulumiConfig` block to expose these settings to your Pulumi stacks.
  pulumiConfig:
    aws:region: ${aws.region}
    stripeApiKey: ${stripe.apiKey}
    stripeApiURL: ${stripe.apiURL}
    greeting: ${greeting}
```

Any stack belonging to the `myorg` organization can inherit these settings by adding the optional `environment` block to its stack-configuration file:

```yaml
# Pulumi.dev.yaml
environment:
  - myapp-dev
```

Values are accessible using the standard [configuration API](/docs/concepts/config/#code):

```typescript
// index.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Import the values using the standard Pulumi configuration API.
const config = new pulumi.Config();
const greeting = config.require("greeting");
const stripeApiKey = config.requireSecret("stripeApiKey");
const stripeApiURL= config.requireSecret("stripeApiURL");

const callbackFunction = new aws.lambda.CallbackFunction("callback", {
    callback: async () => ({
        statusCode: 200,
        body: JSON.stringify({
            greeting,

            // Use them in your program as would any config value.
            stripeApiURL: process.env.STRIPE_API_URL,
         }),
    }),.
    environment: {
        variables: {
            STRIPE_API_URL: stripeApiURL,
        },
    },
});

const functionUrl = new aws.lambda.FunctionUrl("url", {
    functionName: callbackFunction.name,
    authorizationType: "NONE",
});

export const url = functionUrl.functionUrl;
```

Stacks may only read from environments that belong to the same Pulumi organization.

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

Environments cannot be renamed.
