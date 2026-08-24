---
title_tag: Use Pulumi ESC with Pulumi IaC
title: Use with Pulumi IaC
h1: Use Pulumi ESC with Pulumi IaC
meta_desc: Use Pulumi ESC environments in your Pulumi infrastructure as code projects to centralize secrets and configuration across all your stacks.
menu:
  esc:
    name: Use with Pulumi IaC
    parent: esc-guides
    identifier: esc-guides-pulumi-iac
    weight: 10
aliases:
  - /docs/esc/guides/integrate-with-pulumi-iac/
  - /docs/esc/get-started/integrate-with-pulumi-iac/
  - /docs/pulumi-cloud/esc/get-started/integrate-with-pulumi-iac/
  - /docs/esc/integrations/integrate-with-pulumi-iac/
  - /docs/esc/integrations/infrastructure/pulumi-iac/
---

Consuming an ESC environment from a Pulumi IaC program is the most common way to use ESC. It lets you define configuration and secrets once in an environment and share them across every stack that imports it, instead of duplicating values in each `Pulumi.<stack>.yaml` file. It's also how you give your stacks short-lived cloud credentials: rather than storing static access keys, an environment can generate temporary AWS, Azure, or GCP credentials on demand through [OIDC](/docs/esc/guides/configuring-oidc/).

This section explains how the integration works, then points to task-focused guides for adopting ESC and migrating existing patterns to it.

{{< notes type="info" >}}
**New to this?** If you haven't connected an environment to a stack yet, start with the [ESC Get Started guide](/docs/esc/get-started/#add-esc-to-your-pulumi-stack), which walks you through referencing an environment and exposing values through `pulumiConfig`. This section picks up from there.
{{< /notes >}}

## How the integration works

Two pieces connect ESC to a Pulumi program:

1. **The `environment` block** in your stack configuration file (`Pulumi.<stack>.yaml`) lists the environments the stack imports. Environments are merged in order, with later values overriding earlier ones:

    ```yaml
    environment:
      - my-project/common
      - my-project/dev
    ```

1. **The `pulumiConfig` block** inside an environment declares which values flow into your program as stack configuration. Anything you put under `pulumiConfig` becomes available through the standard [Configuration API](/docs/iac/concepts/config/) — `config.get()`, `config.require()`, and their secret variants:

    ```yaml
    values:
      pulumiConfig:
        aws:region: us-west-2
        myApp:apiKey:
          fn::secret: super-secret-value
    ```

Values wrapped in [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/) arrive in your program as [Pulumi IaC secrets](/docs/iac/concepts/secrets/): they're masked in CLI output and encrypted in your stack's state file, exactly as if you'd set them with `pulumi config set --secret`.

{{< notes type="info" >}}
**ESC requires the Pulumi Cloud backend.** Importing an environment into a stack works only for stacks that use Pulumi Cloud as their [state backend](/docs/iac/concepts/state-and-backends/). Stacks stored in DIY backends (such as S3, Azure Blob Storage, or the local filesystem) can't reference ESC environments.
{{< /notes >}}

## Guides

- [Adopt ESC for config and secrets](/docs/esc/guides/pulumi-iac/adopt-esc-for-config-and-secrets/) — move the plaintext configuration and secrets in your stack files into ESC, safely and at scale.
- [Migrate from stack references to `pulumi-stacks`](/docs/esc/guides/pulumi-iac/migrate-from-stack-references/) — replace `StackReference` resources with the ESC `pulumi-stacks` provider and stack configuration.

## Common patterns

Once your stack imports an environment, these are the patterns you'll reach for most often. Each links to its dedicated reference:

- **Dynamic cloud credentials.** Generate short-lived AWS, Azure, or GCP credentials with OIDC instead of storing static keys, and share them across every stack and CI/CD context. See [Dynamic login credentials](/docs/esc/providers/login/) and [Configuring OIDC](/docs/esc/guides/configuring-oidc/).
- **API keys and third-party secrets.** Store a secret directly in an environment with `fn::secret`, or have ESC pull it at open time from an external store like AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, Vault, or 1Password. Where the value lives is a backend detail; either way it reaches your program the same way, as an ordinary [Pulumi secret](/docs/iac/concepts/secrets/). See [Dynamic secrets](/docs/esc/providers/secrets/) for the external-store providers.
- **Environment-specific configuration.** Compose environments so shared values live in a common environment and each stack overrides only what it needs. See [Importing environments](/docs/esc/concepts/imports/).
- **Reading other stacks' outputs.** Import outputs from other Pulumi (or Terraform) stacks into an environment with the [`pulumi-stacks` provider](/docs/esc/providers/iac/pulumi-stacks/).

{{< notes type="info" >}}
When a key is set both in an environment's `pulumiConfig` and explicitly in your stack configuration, the explicit stack value wins. See [Precedence](/docs/esc/concepts/outputs/#precedence-1) for the full rules.
{{< /notes >}}

## Manage imports with Automation API

You can add, list, and remove a stack's imported environments programmatically with [Automation API](/docs/iac/concepts/automation-api/). See [Manage ESC resources with Automation API](/docs/esc/integrations/automation-api/) for the available methods, per-language support, and runnable examples.

## Next steps

- [Adopt ESC for config and secrets](/docs/esc/guides/pulumi-iac/adopt-esc-for-config-and-secrets/) - Move your stack files' config and secrets into ESC
- [Dynamic login credentials](/docs/esc/providers/login/) - Generate dynamic cloud credentials with OIDC
- [Dynamic secrets](/docs/esc/providers/secrets/) - Pull from AWS, Azure, GCP secret stores
- [Importing environments](/docs/esc/concepts/imports/) - Compose configuration hierarchies
