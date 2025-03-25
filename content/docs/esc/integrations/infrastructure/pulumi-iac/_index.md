---
title: Pulumi IaC
title_tag: Pulumi ESC and IaC integration
h1: ESC Pulumi IaC Integration
meta_desc: Pulumi ESC integrates with Pulumi IaC to expose environment settings and
  secrets to Pulumi stacks, simplifying configuration management.
menu:
  esc:
    identifier: esc-pulumi-iac-integrations
    parent: esc-inf-tools-integrations
    weight: 1
search:
  keywords:
    - iac
    - simplifying
    - expose
    - integrates
    - stacks
    - esc
    - management
---

With support for Pulumi ESC built into the Pulumi CLI, you can expose an environment's settings and secrets to any or all of your Pulumi stacks, bypassing the need to define and maintain individual configuration settings or secrets "locally" in Pulumi config files. The optional `pulumiConfig` key enables this.

{{% notes type="info" %}}
The [pulumi](/docs/iac/cli/) CLI (as of v3.139.0) now tracks ESC environments used in stack updates. You can view which ESC environments were used in your updates on the Stack Overview page within the Pulumi Cloud Console.
{{% /notes %}}

The following example updates the `myorg/myapp/dev` environment by adding a `pulumiConfig` block. This block specifies the [Pulumi configuration](/docs/concepts/config/) settings to expose to the Pulumi stack at runtime:

```yaml
# myorg/myapp/dev
imports:
  - aws/dev
  - stripe/dev

values:
  greeting: Hello from the myapp/dev environment!

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

### Convert existing Stack Config to an ESC Environment

To convert your existing stack config to a new ESC Environment, you can use the pulumi CLI to run the following:

```shell
pulumi config env init
```

See [here](/docs/iac/cli/commands/pulumi_config_env_init/) for more information.

### Automation API integration

You can use ESC with [Automation API](/docs/using-pulumi/automation-api/) in [Node](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3@v3.117.0/go/auto#LocalWorkspace.AddEnvironments), and [Python](docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments). The following methods are supported today:

* `addEnvironments(...)`: Append environments to your Pulumi stack's [import](/docs/esc/environments/#using-environments-with-pulumi-iac) list.
* `listEnvironments()`: Retrieve a list of environments currently imported into your stack.
* `removeEnvironment(environment)`: Remove a specific environment from your stack's import list.

### Accessing Pulumi Stack outputs

You can also access [outputs](/docs/iac/concepts/inputs-outputs/#outputs) from [Pulumi IaC stacks](/docs/iac/concepts/stacks/) within an ESC environment using the [`pulumi-stacks` provider](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/).

```yaml
values:
  stackRefs:
    fn::open::pulumi-stacks:
      stacks:
        vpcInfra:
          stack: vpc-infra/dev
  pulumiConfig:
    vpcId: ${stackRefs.vpcInfra.vpcId}
    publicSubnetIds: ${stackRefs.vpcInfra.publicSubnetIds}
    privateSubnetIds: ${stackRefs.vpcInfra.privateSubnetIds}
```
