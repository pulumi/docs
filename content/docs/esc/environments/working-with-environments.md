---
title: Working with environments
title_tag: Pulumi ESC environments
h1: Working with environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
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
  # - /docs/esc/environments/
---

{{% notes type="info" %}}
The examples below use the new `esc` CLI, but all `esc` subcommands are available on the `pulumi` CLI as well. The `pulumi` CLI also provides fully integrated support for configuring Pulumi stacks with Pulumi ESC. See [Using with Pulumi IaC](#using-environments-with-pulumi-iac) below for details.
{{% /notes %}}

## Creating a new environment

To create a new, empty environment, use `esc env init [<org-name>/]<project-name>/<environment-name>`, where `<org-name>` is optional and defaults to your Pulumi Cloud username.

Environment names must be unique within a project and may only contain alphanumeric characters, hyphens, underscores, and periods.

```bash
$ esc env init myorg/myproject/test
Environment created.
```

## Listing environments

To list the environments you have access to, use `esc env ls`:

```bash
$ esc env ls
myorg/myproject/test
```

You can filter this list to a particular organization by passing its name:

```bash
$ esc env ls --organization myorg
myorg/myproject/test
```

You can filter this list to a particular project by passing it's name:

```bash
$ esc env ls -p myproject
myorg/myproject/test
```

## Getting and setting environment values

### Setting a value

To set a new value or update an existing value, use `esc env set <key> <value>`:

```bash
$ esc env set myorg/myproject/test foo bar
```

### Getting a value

To retrieve a single value and its definition, use `esc env get <project-name>/<environment-name> <key>`:

```bash
$ esc env get myorg/myproject/test foo

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

To retrieve all values in an environment, run `esc env get <project-name>/<environment-name>`:

```bash
$ esc env get myorg/myproject/test

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
$ esc env get myorg/myproject/test --value json
{
  "foo": "bar"
}

$ esc env get myorg/myproject/test foo --value json
"bar"
```

Note that the `dotenv` and `shell` options return values only when an environment defines one or more environment variables. See [Projecting environment variables](#projecting-environment-variables) for details.

### Structured configuration

Structured data like maps and arrays can also be set with `esc env set <project-name>/<environment-name> <key> <value>` using object-property (`.`) or array (`[]`) syntax:

```bash
$ esc env set myorg/myproject/test 'data.active' true
$ esc env set myorg/myproject/test 'data.nums[0]' 1
$ esc env set myorg/myproject/test 'data.nums[1]' 2
$ esc env get myorg/myproject/test

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
$ esc env get myorg/myproject/test 'data.nums[1]'

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
$ esc env set myorg/myproject/test salutation Hello
$ esc env set myorg/myproject/test name World
$ esc env set myorg/myproject/test greeting '${salutation}, ${name}'
$ esc env get myorg/myproject/test greeting

   Value

    "Hello, World"

   Definition

    ${salutation}, ${name}


   Defined at

  • test:10:15
```

### Pulumi Contextual information {#pulumi-contextual-information}

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

To edit an environment using your shell's default text editor (as defined by the `$EDITOR` environment variable), use `esc env edit <project-name>/<environment-name>`:

```bash
$ esc env edit myorg/myproject/test
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
$ esc env edit --editor="code" myorg/myproject/test
```

Doing so overrides any value set in `$EDITOR`. See `esc env edit --help` for more options.

### In the Pulumi Cloud console

To edit an environment in the Pulumi Cloud console, select your organization, choose Environments in the left-hand menu, and select the environment you wish to edit:

![Environments Intelligent YAML Editor](/images/docs/concepts/environments-editor.png)

Click Save to apply your changes immediately or Delete to remove the environment.

### With the Pulumi Cloud REST API

You can also use the Pulumi Cloud REST API to perform standard CRUD operations on your environments. See the [Environments section of the REST API docs](/docs/pulumi-cloud/cloud-rest-api/#environments) for details.

## Using secrets providers and OIDC {#using-secrets-providers-and-oidc}

In addition to static and interpolated values, environments can incorporate dynamically retrieved settings and secrets from many [supported providers](/docs/esc/integrations/), including cloud providers via OpenID Connect (OIDC).

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

To do so, use `esc env open <project-name>/<environment-name>`:

```bash
$ esc env open myorg/myproject/test
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
$ esc env open myorg/myproject/test 'data.active'
true

$ esc env open myorg/myproject/test 'data.nums'
[
  1,
  2
]

$ esc env open myorg/myproject/test 'aws.secrets.app-secret' | jq -r 'fromjson | . .secretName'
secretValue
```

{{% notes type="warning" %}}

**Why is my environment failing to open**

Extremely large environments (>10mb) may fail to open due to timeouts. It's recommended to keep only values you
are using within your environment.
{{% /notes %}}

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
$ esc env open myorg/myproject/test --format shell
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
export AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOEXAMPLE"
export MY_ENV_VAR="true"

$ esc env open myorg/myproject/test --format dotenv
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLE"
AWS_SESSION_TOKEN="eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOEXAMPLE"
MY_ENV_VAR="true"
```

Export them into the current shell using `eval` or similar:

```yaml
$ eval $(esc env open myorg/myproject/test --format shell)
$ echo $MY_ENV_VAR
true
```

## Running commands with environment variables

You can also run CLI commands directly, using environment variables obtained with Pulumi ESC --- without having to export those variables into the shell first.

To do this, use `esc run <project-name>/<environment-name> <command>`:

```bash
$ esc run myorg/myproject/test aws s3 ls
2023-10-10 16:09:19 my-s3-bucket
```

If you need to pass one or more flags to the command, prefix the command with `--`:

```bash
$ esc run myorg/myproject/test -- aws s3 ls s3://my-s3-bucket --recursive --summarize
...
Total Objects: 5087
   Total Size: 2419123156
```

For additional options and details, see `esc run --help`.

## Importing other environments

Environments can also be composed from other environments.

Different applications are often configured in similar ways and with common values --- for example, an e-commerce site and order-management system both configured to use the same cloud account, database-connection string, and third-party API key. Managing the duplication of these values across multiple configuration files, however, can be difficult, especially when one of those values changes --- e.g., when an API key is regenerated.

To address these challenges, Pulumi ESC allows you to identify common or closely related configuration settings and define them only once, as individual environments, and then _import_ those environments into other, more specialized environments as needed. Imports also allow you to expose certain environments without having to distribute any concrete values and to delegate responsibility for particular environments to other teams in your organization. Environments can import both static and dynamic values, including secrets, from any number of other environments.

In the following example, two environments, `aws/dev` and `stripe/dev`, are used to compose a third environment, `myapp/dev`:

```yaml
# myorg/aws/dev
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
# myorg/stripe/dev
values:
  stripe:
    apiURL: https://api.stripe.com
    apiKey:
      fn::secret: sk_XemWAl12i4x3hZhp4vBKDEXAMPLE
```

The application-specific `myapp/dev` environment then `imports` these two environments and use their settings to compose new values:

```yaml
# myorg/myapp/dev
imports:
  - aws/dev
  - stripe/dev

values:
  greeting: Hello from the dev environment!

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    STRIPE_API_KEY: ${stripe.apiKey}
    STRIPE_API_URL: ${stripe.apiURL}
    GREETING: ${greeting}
```

Finally, `esc run` renders `myapp/dev`'s environment variables for use on the command line:

```bash
$ esc run myorg/myapp/dev -- bash -c 'echo $GREETING'
Hello from the dev environment!

$ esc run myorg/myapp/dev -- bash -c 'echo $STRIPE_API_URL'
https://api.stripe.com

$ esc run myorg/myapp/dev -- bash -c 'echo $STRIPE_API_KEY'
[secret]

$ esc run myorg/myapp/dev -- bash -c 'echo $AWS_SECRET_ACCESS_KEY'
[secret]

$ echo "'$GREETING'"
''
```

Notice in the example that the `environmentVariables` were exposed to the `bash` command, but not to the surrounding shell, and that the values marked as secrets with `fn::secret` were protected from exposure.

## Using environments with Pulumi IaC

With support for Pulumi ESC built into the Pulumi CLI, you can expose an environment's settings and secrets to any or all of your Pulumi stacks, bypassing the need to define and maintain individual configuration settings or secrets "locally" in Pulumi config files. The optional `pulumiConfig` key enables this.

The following example updates the `myorg/myapp/dev` environment by adding a `pulumiConfig` block. This block specifies the [Pulumi configuration](/docs/concepts/config/) settings to expose to the Pulumi stack at runtime:

```yaml
# myorg/myapp/dev
imports:
  - aws/dev
  - stripe/dev

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
  - myapp/dev
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

### With Automation API

You can use ESC with [Automation API](/docs/using-pulumi/automation-api/) in [Node](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3@v3.117.0/go/auto#LocalWorkspace.AddEnvironments), and [Python](docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments). The following methods are supported today:

* `addEnvironments(...)`: Append environments to your Pulumi stack's [import](/docs/esc/environments/#using-environments-with-pulumi-iac) list.
* `listEnvironments()`: Retrieve a list of environments currently imported into your stack.
* `removeEnvironment(environment)`: Remove a specific environment from your stack's import list.

## Versioning Environments

Every time you make changes and save an environment, a new, immutable **revision** is created. You can see the history of revisions using `esc env version history` or in the Pulumi Cloud Console.

```bash
$ esc env version history myorg/myproject/test
revision 3 (tag: latest)
Author: <Name> <User-ID>
Date: 2024-04-18 12:42:18.02 -0700 PDT

revision 2
...
```

Compare revisions using `esc env diff`.

```bash
$ esc env diff myorg/myproject/test@3 myorg/myproject/test@2
 Value

    --- myorg/myproject/test@3
    +++ myorg/myproject/test@2
...
```

### Tagging Versions

You can tag your revisions with meaningful names like `prod`, `stable`, `v1.1.2`. Each environment has a built-in `latest` tag that always points to the environment’s most recent revision. Use `esc env version tag` to tag a revision. In the following example we are assign `prod` tag to revision 3 of environment `test`.

```bash
$ esc env version tag myorg/myproject/test@prod @3
```

You can also manage tags in the Pulumi Cloud UI by selecting the environment's `Versions` tab and then selecting the `Actions` menu for the given version of the environment you want to tag:

![envtagui.png](../envtagui.png)

### Using Tagged Versions

Once you tag a revision, you can use the tag to [open](/docs/esc/environments/#opening-an-environment) a specific environment version.

```bash
$ esc open myorg/myproject/test@prod
```

You can specify the tagged version when importing the environment. This helps you ensure that you are importing a stable environment version that is not affected by changes.

```yaml
# Importing in another ESC Environment
imports:
  - myproject/test@prod

# Importing in Pulumi stack Config
# Pulumi.dev.yaml
environment:
  - myproject/test@prod
```

You can find more commands and options in the [ESC CLI documentation](/docs/esc-cli/).

## Precedence rules

When multiple environment sources are combined and settings overlap, values are applied successively in the order in which they're imported and defined.

For example, in the following scenario, three environments define a key `foo`, each with a different value. The third environment, `project/environment-c`, imports `project/environment-a` and `project/environment-b` (importantly, in that order):

```yaml
# project/environment-a
values:
  foo: bar
```

```yaml
# project/environment-b
imports:
  - project/environment-a
values:
  foo: baz
  pulumiConfig:
    foo: ${foo}
```

```yaml
# project/environment-c
imports:
  - project/environment-a
  - project/environment-b
values:
  foo: qux
  pulumiConfig:
    foo: ${foo}
```

Notice how the value of `foo` is overwritten with each successive environment:

```bash
$ esc env open project/environment-a foo
"bar"

$ esc env open project/environment-b foo
"baz"

$ esc env open project/environment-c foo
"qux"

$ pulumi preview
Diagnostics:
  pulumi:pulumi:Stack (dev):
    { foo: 'qux' }
```

Also notice that when the local definition of `foo` is removed from `project/environment-c` and its imports are reordered, the value of `foo` changes to reflect the value inherited from `project/environment-a` --- i.e., the last-imported one:

```yaml
# project/environment-c
imports:
  - project/environment-b
  - project/environment-a
values:
  pulumiConfig:
    foo: ${foo}
```

```bash
$ esc env open project/environment-c foo
"bar"

$ pulumi preview
Diagnostics:
  pulumi:pulumi:Stack (dev):
    { foo: 'bar' }
```

To unset a value inherited from another environment, overwrite it with `null`.

## Setting up access to environments

{{% notes "info" %}}
Access controls and Teams are only available to organizations using Pulumi Enterprise Edition and Pulumi Business Critical Edition.To learn more about editions visit the [pricing page](/pricing/).
{{% /notes %}}

### Organization-wide permissions

Go to the `Access Management` page under Settings to set Organization-wide environment permissions. Members of the organization will receive these permissions. By default, the environment permissions for the organization is set to `write`. There are four options:

* `none`: Members have access to none of the environments
* `read`: Members can view only plaintext key values (i.e., the definition of the environment). They won’t be able to see the secret values in plaintext, run any provider configurations to retrieve credentials or run any functions. They cannot perform any Pulumi IaC operations such as `refresh`, `up`, `destroy` on stacks that imports the environment
* `open`: Members with ‘open’ permissions can decrypt secrets and see them in plaintext. Additionally, they can get dynamic credentials using provider configurations and evaluate functions defined in the environment. They can perform any Pulumi IaC operation on stacks that import an environment as long as they have ‘write’ access to the stack and ‘open’ access to the environment
* `write`: Members will have permissions to `open` and `update` any environment

### Team permissions

You can grant environment-wise permissions to members of a Team. There are four roles:

* `Environment reader`: Team members will have `read` permissions
* `Environment opener`: Team members will have `open` permissions
* `Environment editor`: Team members will have `write` permissions
* `Environment admin`: Team members will have `write` and `delete` permissions

## Deleting an environment

To remove an environment, use `esc env rm [<org-name>/]<project-name>/<environment-name>`:

```bash
$ esc env rm myorg/myproject/test
This will permanently remove the "myorg/myproject/test" environment!
Please confirm that this is what you'd like to do by typing `myorg/myproject/test`: myorg/myproject/test
Environment "myorg/myproject/test" has been removed!
```

## Cloning an environment

Environments cannot be renamed, however, they can be cloned into a new project/environment. This is intentional as it allows for the ability to "rename" an environment by cloning the source into a new destination project/environment and updating all the references to the source environment without breaking any references. Once all references have been updated, the old environment can be deleted.

Cloning an environment takes various options that allow for configuring what is included from the source environment when creating the new environment. These options are:

| Option                    | Description                                                                |
|---------------------------|----------------------------------------------------------------------------|
| Preserve History          | Preserve all prior versions of the environment up until the cloned version |
| Preserve Environment Tags | Preserve all environment tags on the source environment                    |
| Preserve Revision Tags    | Preserve all revision tags on the versions being cloned                    |
| Preserve Team Access      | Preserve any team access that he source environment had                    |

An example clone command might look like:

```bash
$ esc env clone default/dev my-app/dev --preserve-history --preserve-env-tags --preserve-rev-tags --preserve-access
```

## Tagging Environments

Environments support the ability to add contextual information about them via Environment Tags. Tags are a collection of both user-defined and auto-generated key/value pairs that can be used to group and search for environments.

```bash
$ esc env tag myorg/myproject/test region us-east-1
Name: region
Value: us-east-1
Last updated at 2024-09-11 01:45:10.738 -0700 PDT by Derek <dschaller>
```
