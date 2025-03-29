---
title_tag: Integrate with Cloudflare | Pulumi ESC
title: Cloudflare
h1: "Pulumi ESC: Integrate with Cloudflare"
meta_desc: This page provides an overview of how to use Pulumi ESC with Cloudflare.
menu:
  esc:
    parent: esc-inf-tools-integrations
    weight: 4
aliases:
  - /docs/esc/other-integrations/cloudflare/
search:
  keywords:
    - Cloudflare
    - ESC
    - Cloudflare Workers
    - API token
---

## Overview

Pulumi ESC integrates with [Cloudflare](https://www.cloudflare.com/) to help developers automatically manage configuration and secrets when running [`wrangler`](https://developers.cloudflare.com/workers/wrangler/install-and-update/) commands. Additionally, Pulumi ESC works with the [Pulumi Cloudflare SDK](https://www.pulumi.com/registry/packages/cloudflare/installation-configuration/) to provide secrets to defined Cloudflare resources, such as Workers.

{{< notes type="info" >}}
**What is Pulumi ESC?** Pulumi ESC (Environments, Secrets, and Configuration) allows you to define collections of configuration settings and secrets, known as environments, and utilize them in any application or service. [Learn more](https://www.pulumi.com/docs/esc/)
{{< /notes >}}

## Manage secrets for Wrangler commands

Learn how to:

- Login to your Cloudflare account without having to locally set the `CLOUDFLARE_API_TOKEN` environment variable.
- Populate the `.dev.vars` file from ESC-stored secrets.
- Pass secrets stored in Pulumi ESC to your production Cloudflare Workers without these being directly in your shell.

### Prerequisites

Ensure you have:

- installed [Pulumi ESC](https://www.pulumi.com/docs/install/esc/)
- installed [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/#install-wrangler/)
- a valid and properly scoped [Cloudflare API token](https://developers.cloudflare.com/workers/wrangler/ci-cd/#api-token)
- a Pulumi Cloud account. You can sign up for an [always-free, individual tier](https://app.pulumi.com/signup)

{{< notes type="info" >}}
**New to Pulumi ESC?** Complete the [Getting Started tutorial](https://www.pulumi.com/docs/esc/get-started/)
{{< /notes >}}

### 1. Create an ESC Environment

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, to use the Pulumi Cloud console follow the [console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
esc login # if needed

## create a new ESC Environment
ESC_ENV=my-project/dev-environment
esc env init ${ESC_ENV}
```

Edit the Environment in your terminal:

```bash
esc env edit ${ESC_ENV}
```

Paste the contents below in the editor and replace the `abc...` API token and Account ID value with yours. Note: the API token is declared as a secret. Once the Environment is saved, Pulumi will encrypt its value and replace it with ciphertext.

```yaml
values:
  environmentVariables:
    CLOUDFLARE_API_TOKEN:
      fn::secret: abc123abc123abc123abc123abc123
    CLOUDFLARE_ACCOUNT_ID: abc123abc123
```

Now that the Pulumi ESC Environment is created, it can be consumed in a variety of ways, such as running other shell commands without having to set the environment variables locally first.

The `esc run` command opens the Environment you previously created, sets the specified environment variables into a temporary environment, and then uses those environment variables in the context of the `wrangler` commands.

### 2. Use ESC with `wrangler whoami`

Log into your Cloudflare account without needing to manage the credentials directly in your shell:

```bash
# ensure you're currently not logged in
npx wrangler logout

# retrieve the esc environment and authenticate programmatically
esc run ${ESC_ENV} npx wrangler whoami
```

Because we are running `wrangler` in non-interactive mode, it requires a Cloudflare API token and account ID for authentication. The `wrangler whoami` retrieves details about the provided credentials.

For additional options and details, see `esc run --help`.

### 3. Use ESC to create your `.dev.vars` file

The `.dev.vars` file is located in the root of your wrangler project to define secrets used when running `wrangler dev`. Per [Cloudflare documentation](https://developers.cloudflare.com/workers/configuration/secrets/#secrets-in-development), the `.dev.vars` file should be formatted like a `dotenv` file.

Create a new ESC Environment:

```bash
ESC_ENV=my-project/dev-vars-environment
esc env init ${ESC_ENV}
```

Edit the environment in your terminal:

```bash
esc env edit ${ESC_ENV}
```

There are two options for managing the `.dev.vars` definition.

- Option 1: Utilize the `--format` export flag for flexibility. A dedicated Environment is required as the format flag does not support property paths. Paste the contents below in the editor:

  ```yaml
  values:
    environmentVariables:
      TOP_SECRET:
        fn::secret: "the moon is made of cheese"
  ```

  Generate the `.dev.vars` file:

  ```bash
  esc env open ${ESC_ENV} --format dotenv > .dev.vars
  ```

- Option 2: Use the `files` section to add a value. When the Environment is opened, the value is copied to a temporary file on your system, with the path set as an environment variable with the key name. Paste the contents below in the editor:

  ```yaml
  values:
    environmentVariables:
      TOP_SECRET: "the moon is made of cheese"
    files: |
      DEV_VARS: TOP_SECRET=${environmentVariables.TOP_SECRET}
  ```

  Generate the `.dev.vars` file:

  ```bash
  esc run -i ${ESC_ENV} -- sh -c 'cat $DEV_VARS > .dev.vars'
  ```

  For additional options and details, see `esc run --help`.

### 4. Use ESC with `wrangler secret put`

With Pulumi ESC you can centralize common secrets and then use Wrangler to pass them on to your Workers and other Cloudflare resources as needed:

Add a new value to your `my-project/dev-environment` Environment:

```bash
ESC_ENV=my-project/dev-environment
esc env set ${ESC_ENV} environementVariables.TOP_SECRET "aliens are real" --secret
```

Share the secret with your Worker.

```bash
esc run -i ${ESC_ENV} -- sh -c 'echo "$TOP_SECRET" | npx wrangler secret put TOP_SECRET'
```

Consume the secret in your Worker script. Here's an example using TypeScript:

```typescript
export interface Env {
  TOP_SECRET: string;
}
export default {
  async fetch(request, env, ctx): Promise<Response> {
    return new Response(`Did you know that "${env.TOP_SECRET}"?`);
  }
} satisfies ExportedHandler<Env>;
```

Using Infrastructure as Code (IaC) to manage Workers? See the next section to see how to leverage Pulumi ESC alongside.

## Manage Cloudflare Worker Secrets in IaC

Pulumi ESC works hand-in-hand with [Pulumi IaC](https://www.pulumi.com/docs/get-started/) to simplify configuration management.

Learn how to:

- Add an ESC Environment to your Pulumi stack
- Assign an ESC Secret to Cloudflare resources
- Consume the ESC Secret in a Worker script

### Additional Prerequisites

In addition to the [prerequisites above](#prerequisites), ensure you have:

- installed [Pulumi CLI](https://www.pulumi.com/docs/install/)
- installed a [Pulumi-supported programming language](https://www.pulumi.com/docs/languages-sdks/)

{{< notes type="info" >}}
**New to Pulumi IaC?** Complete the [Getting Started tutorial](https://developers.cloudflare.com/pulumi/tutorial/hello-world/).
{{< /notes >}}

### 1. Create (or Modify) an ESC Environment

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, to use the Pulumi Cloud console follow the [console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
esc login # if needed

## create a new ESC Environment
ESC_ENV=my-project/pulumi-environment
esc env init ${ESC_ENV}
```

Paste the contents below in the editor and replace the `abc...` API token and Account ID value with yours. These values are to be consumed by a Pulumi program hence they are placed under the `pulumiConfig` section. See the [syntax reference](https://www.pulumi.com/docs/esc/reference/) for more options.

```yaml
values:
  pulumiConfig:
    CLOUDFLARE_API_TOKEN:
      fn::secret: abc123abc123abc123abc123abc123
    CLOUDFLARE_ACCOUNT_ID: abc123abc123
    TOP_SECRET:
      fn::secret: "aliens are real"
```

### 2. Add ESC to a Pulumi Stack

You'll create a new stack to test the changes in isolation. Optionally, use an existing Stack.

Inside your Pulumi project directory, run:

```bash
pulumi stack init my-esc-stack
pulumi config env add ${ESC_ENV}
```

### 3. Assign an ESC Secret to a [Worker Secret Binding](https://www.pulumi.com/registry/packages/cloudflare/api-docs/workerscript/#inputs)

With the ESC Environment referenced in the Stack, you'll be able to consume ESC values to assign them to a Secret Binding Input. Here is an example Pulumi program written in TypeScript:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

const config = new pulumi.Config();

// Create a Cloudflare WorkerScript with a secret binding
const workerScript = new cloudflare.WorkerScript("myWorkerScript", {
    name: "my-worker-script",
    content: fs.readFileSync("worker.ts", "utf8"),
    secretTextBindings: [
        {
            name: "TOP_SECRET",
            text: config.requireSecret("TOP_SECRET"),
        },
    ],
});
```

The secret binding configuration allows the Worker to consume the secret in the `fetch` handler. Here's the contents of the `worker.ts` file.

```typescript
export interface Env {
  TOP_SECRET: string;
}
export default {
  async fetch(request, env, ctx): Promise<Response> {
    return new Response(`Did you know that "${env.TOP_SECRET}"?`);
  }
}
```
