---
title_tag: TypeScript/JavaScript SDK | Pulumi ESC
title: TypeScript (Node.js)
h1: "Pulumi ESC: TypeScript/JavaScript SDK"
meta_desc: This page provides an overview on how to use Pulumi ESC TypeScript/JavaScript
  SDK.
menu:
  esc:
    parent: esc-languages-sdks
    identifier: esc-typescript-sdk
    weight: 1
aliases:
  - /docs/esc/sdk/javascript/
search:
  keywords:
    - TypeScript
    - Node.js
    - JavaScript SDK
    - environment definitions
    - access token
---

The [JavaScript/TypeScript SDK](https://www.npmjs.com/package/@pulumi/esc-sdk) for [Pulumi ESC (Environments, Secrets, and Configuration)](/product/esc/) allows you to automate Pulumi ESC.

Here are some of the scenarios the SDK can automate:

* List environments and read environment definitions
* Open environments to access config and resolve secrets
* Create, update, decrypt, and delete environment definitions
    * Supports both structured types and yaml text
* List environment revisions and create new revision tags
* Check environment definitions for errors

## Install the SDK package

Run `npm install @pulumi/esc-sdk` or `yarn add @pulumi/esc-sdk` to install the SDK package.

## Examples

These samples show how to create an `EscApi` client with an access token and use it to perform various ESC tasks.

All of these examples expect a `PULUMI_ACCESS_TOKEN` and `PULUMI_ORG` environment variable to be set.

### Manage environment example

This example creates a new environment, opens that environment to access a secret, and the list the environments.

{{< chooser language "typescript" >}}

{{% choosable language "typescript" %}}

```typescript
import * as esc from "@pulumi/esc-sdk";

async function main() {
    const PULUMI_ACCESS_TOKEN = process.env.PULUMI_ACCESS_TOKEN!;
    const orgName = process.env.PULUMI_ORG!;
    const config = new esc.Configuration({ accessToken: PULUMI_ACCESS_TOKEN });
    const client = new esc.EscApi(config);

    const projName = "examples";
    const envName = "sdk-typescript-example";

    // Create a new environment
    await client.createEnvironment(orgName, projName, envName);

    const envDef: esc.EnvironmentDefinition = {
        values: {
            my_secret: {
                "fn::secret": "shh! don't tell anyone",
            },
        },
    };

    // Update the environment with the new definition
    await client.updateEnvironment(orgName, projName, envName, envDef);

    // Open and read the environment
    const openEnv = await client.openAndReadEnvironment(orgName, projName, envName);

    if (!openEnv) {
        console.error("Failed to open and read the environment");
        return;
    }

    // Acces the value of the secret
    const secretValue = openEnv.values?.my_secret;
    console.log(`Secret value: ${secretValue}\n`);

    // List all the environments in the organization
    const orgEnvs = await client.listEnvironments(orgName);
    if (!orgEnvs || !orgEnvs.environments) {
        console.log("No environments found");
        return;
    }

    for (const env of orgEnvs.environments) {
        console.log(`Environment: ${env.project}/${env.name}`);
    }
}

(async ()=>{
    await main();
})();
```

{{% /choosable %}}
{{< /chooser >}}

### Tag revision example

This example lists revisions for an environment, tags a revision, and lists revision tags.

{{< chooser language "typescript" >}}

{{% choosable language "typescript" %}}

```typescript

import * as esc from "@pulumi/esc-sdk";

async function main() {
    const PULUMI_ACCESS_TOKEN = process.env.PULUMI_ACCESS_TOKEN!;
    const orgName = process.env.PULUMI_ORG!;
    const config = new esc.Configuration({ accessToken: PULUMI_ACCESS_TOKEN });
    const client = new esc.EscApi(config);

    const projName = "examples";
    const envName = "sdk-typescript-example";

    // List environment revisions
    const revisions = await client.listEnvironmentRevisions(orgName, projName, envName);

    if (!revisions || revisions.length < 2) {
        throw new Error(`Expected at least 2 revisions for environment ${projName}/${envName}`);
    }

    // Get the second latest revision
    const revision = revisions[1];
    await client.createEnvironmentRevisionTag(orgName, projName, envName, "stable", revision.number);

    console.log(`Tagged revision ${revision.number} as 'stable'`);

    // List tags
    const tags = await client.listEnvironmentRevisionTags(orgName, projName, envName);
    if (!tags || !tags.tags) {
        throw new Error(`Expected tags for environment ${projName}/${envName}`);
    }

    for (const tag of tags?.tags) {
        console.log(`Tag ${tag.name} at revision ${tag.revision}`);
    }
}

(async ()=>{
    await main();
})();


```

{{% /choosable %}}
{{< /chooser >}}

## Documentation

* [API Reference Documentation](/docs/reference/pkg/nodejs/pulumi/esc-sdk/)
