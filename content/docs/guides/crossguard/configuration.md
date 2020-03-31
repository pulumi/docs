---
title: Configurable Policy Packs
meta_desc: Configuration allows you to write flexible policies that can be reused across you organization.
linktitle: Configuration
weight: 2

menu:
  userguides:
    parent: crossguard
---

<!-- markdownlint-disable ul code -->
{{% crossguard-preview %}}

## Overview

Configuration allows you to author flexible Policy Packs that can be reused across your entire organization. As an organization administrator, you can use a single Policy Pack yet vary configuration (e.g. enforcement level, the allowed instance types, cost allowances, etc.) from one Policy Group to the next. For example, you may have a Policy Group for your non-production stacks that allow smaller instance types, while your Production Policy Group allows for use of large instance types.

Configuration schema is defined per policy, and then the actual configuration can be set via a form in the Pulumi Console or using a JSON file.

Configuration is currently supported for the Node.js Policy SDK (TypeScript/JavaScript). Python support for configuration is [coming soon](https://github.com/pulumi/pulumi-policy/issues/210).

## Writing Configurable Policy Packs

### Enforcement Level

The Policy SDK will automatically make the enforcement levels of all policies configurable. You can configure the enforcement level for all policies in a Policy Pack or configure it for each individual policy level. The top level enforcement level under `all` will override the existing enforcement levels of all policies in the Policy Pack. A configured enforcement level for a specific policy will override the policy's existing enforcement level as well as the top level configured enforcement level.

In the example configuration below, all policies in the Policy Pack would be `disabled` with the exception of the `a-policy` policy, which would be `mandatory`.

```json
{
    "all": {
        "enforcementLevel": "disabled"
    },
    "a-policy": {
         "enforcementLevel": "mandatory"
    }
}
```

### Custom Configuration

Policy authors can denote the schema for a particular Policy's configuration using the `configSchema` field. The configuration schema uses [JSON Schema](https://json-schema.org/) to describe the acceptable configuration for a Policy.

The below example shows a  `ResourceValidationPolicy` that has a required `message` field, which must be between five and fifty characters. Then, from within the `validateResource` function the configuration value can be accessed using `args.getConfig`.

```typescript
const examplePolicy: ResourceValidationPolicy = {
    name: "example-policy-with-schema",
    ...
    configSchema: {
        properties: {
            message: {
                type: "string",
                minLength: 5,
                maxLength: 50,
                default: "This is a configurable message."
            }
        },
        required: ["message"],
    },
    validateResource: validateTypedResource(aws.s3.Bucket, (_, args, reportViolation) => {
        const config = args.getConfig<{ message: string }>();
        reportViolation("Here is the configurable message: " + config.message);
    }),
}
```

At the top level, the `configSchema` for each Policy has only the `properties` and `required` fields. Within the `properties` field, you may use the entire breadth of [validations keywords provided by the JSON Schema](https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6). Validation keywords are fields like `minLength` and `maxLength` in the above example.

## Configuring a Policy Pack

You can configure a Policy Pack via the `pulumi` CLI or the Pulumi Console.

### Using the Pulumi CLI

#### Running Policy Packs Locally

If you are using the `pulumi` CLI to run local Policy Packs, you can store the configuration in a file and then use a flag to pass the file to the CLI.

With the above example Policy, we can write the following configuration to a `config.json` file:

```json
{
    "all": {
        "enforcementLevel": "mandatory"
    },
    "example-policy-with-schema":{
        "message": "Here is my message."
    }
}
```

To run this Policy Pack locally with the configuration, you can run:

```bash
$ pulumi preview --policy-pack <path-to-policy-pack-directory> --policy-pack-config <path-to-policy-pack-config-file>
```

#### Validating Configuration

If the Policy Pack has already been [published to the Pulumi Console]({{< relref "/docs/get-started/crossguard/enforcing-a-policy-pack" >}}), you can validate the configuration using the `pulumi policy validate-config` command.

```bash
$ pulumi policy validate-config <org-name>/<policy-pack-name> <version> --config <path-to-policy-pack-config-file>
```

#### Enabling the Policy Pack

Once you are satisfied with the configuration, (if Policy as Code is enabled for your organization) you can enable the Policy Pack and configuration for your organization's default Policy Group by running:

```bash
$ pulumi policy enable <org-name>/<policy-pack-name> <version> --config <path-to-policy-pack-config-file>
```

If you would like to enable it for a specific Policy Group, you can specify the group using the `--policy-group` flag as follows:

```bash
$ pulumi policy enable <org-name>/<policy-pack-name> <version> --config <path-to-policy-pack-config-file> --policy-group <policy-group-name>
```

### Using the Pulumi Console

Configuration can also be added, edited and enabled via the Pulumi Console. Once a Policy Pack has been [published to the Pulumi Console]({{< relref "/docs/get-started/crossguard/enforcing-a-policy-pack" >}}), organization administrators can enable the pack with configuration on a Policy Group using the console.

On a Policy Group page, you can click the ADD button to enable a new Policy Pack.

![Enable Policy Pack](/images/docs/guides/crossguard/enable-policy-pack.jpg)

If the selected Policy Pack has configuration, a form will appear for you to enter the configuration. The form provides automatic validation to ensure the supplied configuration meets the configuration schema.

![Policy Pack Configuration Form](/images/docs/guides/crossguard/config-dialog.jpg)
