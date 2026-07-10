---
title_tag: Adopt Pulumi ESC for config and secrets
title: Adopt ESC for config and secrets
h1: Adopt Pulumi ESC for config and secrets
meta_desc: Move the plaintext configuration and secrets in your Pulumi stack files into a Pulumi ESC environment, and roll the change out safely across many stacks.
menu:
  esc:
    parent: esc-guides-pulumi-iac
    identifier: esc-guides-adopt-esc-config-secrets
    weight: 10
---

Most Pulumi projects start with configuration and secrets stored directly in each stack's `Pulumi.<stack>.yaml` file. That works, but the values are duplicated across every stack and project that needs them, and each copy has to be updated by hand. Moving those values into a Pulumi ESC environment gives you one source of truth that every stack imports.

This guide walks through moving a single stack's configuration and secrets into an environment, then shows how to roll the change out across many stacks without a risky big-bang migration.

{{< notes type="info" >}}
**This guide is for existing Pulumi IaC users.** If you're new to the ESC/Pulumi IaC integration, read [Use with Pulumi IaC](/docs/esc/guides/pulumi-iac/) first for the mental model, and the [ESC Get Started guide](/docs/esc/get-started/) for a from-scratch walkthrough.
{{< /notes >}}

## Prerequisites

- [Pulumi CLI](/docs/install/) v3.99.0 or later installed
- A [Pulumi account](https://app.pulumi.com/signup) — ESC requires the [Pulumi Cloud backend](/docs/iac/concepts/state-and-backends/)
- An existing Pulumi project whose stack uses the Pulumi Cloud backend

## The starting point

Imagine a small project, `myapp`, that runs a containerized workload. Its `dev` stack needs one plaintext value (the region) and one secret (a database connection string). Today those live in `Pulumi.dev.yaml`:

```yaml
config:
  aws:region: us-west-2
  myapp:containerImage: nginx:1.27
  myapp:dbConnectionString:
    secure: v1:9RmvK2v6Nlc8Xtbp:0Vq2b...
```

The program reads them with the standard [Configuration API](/docs/iac/concepts/config/):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const containerImage = config.require("containerImage");
const dbConnectionString = config.requireSecret("dbConnectionString");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()
container_image = config.require("containerImage")
db_connection_string = config.require_secret("dbConnectionString")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
conf := config.New(ctx, "")
containerImage := conf.Require("containerImage")
dbConnectionString := conf.RequireSecret("dbConnectionString")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var containerImage = config.Require("containerImage");
var dbConnectionString = config.RequireSecret("dbConnectionString");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var config = ctx.config();
var containerImage = config.require("containerImage");
var dbConnectionString = config.requireSecret("dbConnectionString");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  containerImage:
    type: string
  dbConnectionString:
    type: string
    secret: true
```

{{% /choosable %}}

{{< /chooser >}}

Nothing in your program changes when you move these values to ESC: they still arrive as stack configuration.

## Move config and secrets into an environment

The Pulumi CLI can convert a stack's configuration into a new environment in one step. From your project directory, run:

```bash
pulumi config env init --stack dev
```

This creates an environment named after the stack (`myapp/dev` by default), copies the stack's configuration and secrets into its `pulumiConfig` block, and replaces the values in `Pulumi.dev.yaml` with a reference to the new environment. Secrets stay encrypted the whole way. They're re-encrypted under ESC rather than exposed.

Afterward, `Pulumi.dev.yaml` contains only the environment reference:

```yaml
environment:
  - myapp/dev
```

And the new `myapp/dev` environment holds the values:

```yaml
values:
  pulumiConfig:
    aws:region: us-west-2
    myapp:containerImage: nginx:1.27
    myapp:dbConnectionString:
      fn::secret:
        ciphertext: ZXNjeAAAAAEAAAEAe3jKq...
```

{{< notes type="info" >}}
Pass `--keep-config` if you'd rather leave the values in the stack file while you test the environment, and remove them yourself once you're confident. Use `--env <name>` to choose an environment name other than `<project>/<stack>`.
{{< /notes >}}

To do the same thing by hand (for example, when you want the values in a shared environment rather than a per-stack one), create the environment with [`pulumi env init`](/docs/iac/cli/commands/pulumi_env_init/), add the values under `pulumiConfig` with [`pulumi env edit`](/docs/iac/cli/commands/pulumi_env_edit/), and add the `environment` block to your stack file yourself.

## Pin the environment

By default, a stack imports the latest revision of an environment. That means a change to the environment takes effect on your next `pulumi up` with no change to the stack itself. That's convenient, but it also means an unrelated edit can alter a stack you weren't touching.

For anything beyond experimentation, **pin the import to a specific version** so updates are deliberate. Append a revision number or a version tag with `@`:

```yaml
environment:
  - myapp/dev@1
```

Using a named tag (for example `@production`) instead of a raw revision number lets you move the tag forward when you're ready to promote a new revision, without editing every stack that imports it. See [Environment versioning](/docs/esc/concepts/versioning/) for how revisions and tags work.

## Verify end to end

Confirm the values resolve as expected before and after wiring them into the stack:

1. Open the environment directly and check the resolved values, including the decrypted secret:

    ```bash
    pulumi env open myapp/dev
    ```

1. Preview the stack and confirm Pulumi sees the same configuration it did before the move:

    ```bash
    pulumi preview --stack dev
    ```

    The plan should be a no-op: the program receives identical inputs, just sourced from ESC instead of the stack file.

1. Run `pulumi up` to apply.

## Adopt safely at scale

Once a single stack works end to end, resist the urge to convert everything at once. The reliable pattern is **get one path working, then fan out**:

1. **Prove it on one non-production stack.** Convert a single low-risk stack (like `dev`), verify a no-op preview, and deploy. This validates your environment structure and backend setup with nothing important on the line.

1. **Factor shared values into a common environment.** Values that are identical across stacks (a region, a registry, a shared API endpoint) belong in one environment that the others [import](/docs/esc/concepts/imports/), so you define them once:

    ```yaml
    # myapp/common
    values:
      pulumiConfig:
        aws:region: us-west-2
        myapp:containerImage: nginx:1.27
    ```

    Each stack's environment imports `common` and adds only what's specific to it:

    ```yaml
    # myapp/prod
    imports:
      - myapp/common
    values:
      pulumiConfig:
        myapp:dbConnectionString:
          fn::secret: ${prodDbConnectionString}
    ```

1. **Promote to production as a series of no-ops.** For each remaining stack, make the switch a preview-clean change: move its values into ESC, confirm `pulumi preview` shows no diff, then deploy. A migration that never changes a plan is one you can roll out with confidence.

1. **Pin every production import.** Non-production stacks can track `@latest` for convenience; production stacks should pin to a version or tag so environment changes reach them only when you promote.

Following this order (one stack, then shared values, then a no-op rollout), you can move an entire portfolio onto ESC incrementally, with a working, verifiable state at every step.

## Next steps

- [Migrate from stack references to `pulumi-stacks`](/docs/esc/guides/pulumi-iac/migrate-from-stack-references/) - Apply the same incremental approach to cross-stack outputs
- [Importing environments](/docs/esc/concepts/imports/) - Compose shared and per-stack configuration
- [Environment versioning](/docs/esc/concepts/versioning/) - Pin and promote environment revisions
- [Dynamic secrets](/docs/esc/providers/secrets/) - Replace static secrets with values pulled from external stores at open time
