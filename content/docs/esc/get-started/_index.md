---
title: Get Started
title_tag: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
h1: Get Started with Pulumi ESC
meta_desc: Get started with Pulumi ESC. Create an environment, store a secret, retrieve it, and consume it from a Pulumi IaC stack.
weight: 1
menu:
  esc:
    parent: esc-home
    identifier: esc-get-started
aliases:
  - /docs/pulumi-cloud/esc/get-started/
  - /docs/esc/get-started/begin/
  - /docs/esc/get-started/create-environment/
  - /docs/pulumi-cloud/esc/get-started/begin/
  - /docs/pulumi-cloud/esc/get-started/create-environment/
---

Pulumi ESC (Environments, Secrets, and Configuration) is a centralized secrets and configuration management service that is part of Pulumi Cloud. In this quick start, you'll create your first environment, store a secret, retrieve it, and then consume it from a Pulumi IaC stack — the most common ESC workflow.

## Prerequisites

1. **Create a Pulumi account** at [app.pulumi.com](https://app.pulumi.com/signup)
1. **Install the Pulumi CLI**

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
brew install pulumi/tap/pulumi
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
choco install pulumi
```

{{% /choosable %}}

{{% /chooser %}}

See the [Pulumi installation docs](/docs/install/) for more options. The `pulumi env` commands used in this guide ship with the Pulumi CLI, so you don't need to install anything else.

## Create your first environment

Create an environment, then store both plaintext configuration and an encrypted secret in it:

1. Log in to Pulumi Cloud:

    ```bash
    pulumi login
    ```

    You'll be prompted to log in via your browser or with an access token. Follow the instructions to authenticate.

1. Open [Pulumi Cloud](https://app.pulumi.com/signin) and log in
1. Select **Environments** in the left navigation
1. Select **+ Create Environment**
1. Choose **New Environment**
1. For **Project name**, enter: `my-project`
1. For **Environment name**, enter: `dev`
1. Select **Create Environment**
1. In the **Environment definition** editor, erase the contents and replace them with the following YAML:

    ```yaml
    values:
      region: us-west-2
      apiKey:
        fn::secret: demo-secret-123
    ```

    This defines two values: `region` (a plaintext value) and `apiKey` (a secret value, denoted with `fn::secret`).

1. Select **Save**

    ESC automatically encrypts the secret value. If you reopen the environment definition, the plaintext `demo-secret-123` has been replaced with ciphertext, while `region` remains in plaintext:

    ```yaml
    values:
      region: us-west-2
      apiKey:
        fn::secret:
          ciphertext: ZXNjeAAAAAEAAAEAFatkojHgMRjHuWIwKbPqplpSUoKCrtLUCwtU0rhJuhtOa6
    ```

## Retrieve your configuration and secrets

You can retrieve all values, including decrypted secrets, from either the Pulumi Cloud console or the CLI.

### Using the Pulumi Cloud console

1. Open [Pulumi Cloud](https://app.pulumi.com/signin) and select **Environments** in the left navigation
1. Select your `my-project/dev` environment to open it
1. The resolved values, including the decrypted `apiKey`, appear in the preview pane next to the environment definition

### Using the CLI

Open your environment to retrieve all values, including decrypted secrets:

```bash
pulumi env open my-project/dev
```

You should see output like:

```json
{
  "apiKey": "demo-secret-123",
  "region": "us-west-2"
}
```

You've created an environment, stored configuration and secrets, and retrieved them. Notice that the secret is automatically decrypted when you open the environment.

## Add ESC to your Pulumi stack

The most common way to use an ESC environment is to consume it from a Pulumi IaC stack, which centralizes configuration and secrets across all your stacks.

{{< notes type="info" >}}
**ESC requires the Pulumi Cloud backend.** Importing an ESC environment into a stack works only for Pulumi stacks that use Pulumi Cloud as their [state backend](/docs/iac/concepts/state-and-backends/). Stacks stored in self-managed backends (such as S3, Azure Blob Storage, or the local filesystem) can't reference ESC environments.
{{< /notes >}}

### Step 1: Reference your ESC environment

In your stack configuration file (`Pulumi.<stack-name>.yaml`), add an `environment` block that references your ESC environment:

```yaml
environment:
  - <your-project-name>/<your-environment-name>
```

For example, if your ESC environment is `my-project/dev`:

```yaml
environment:
  - my-project/dev
```

You can also reference multiple environments, which will be merged in order (later values override earlier ones):

```yaml
environment:
  - my-project/common
  - my-project/dev
```

{{< notes type="info" >}}
**Pin imports to a specific version.** By default, Pulumi uses the `@latest` tag of each environment (always the most recent revision). To ensure your stack uses a known, fixed version, append a version tag or revision number with `@`:

```yaml
environment:
  - my-project/common@production
  - my-project/dev@3
```

This prevents unexpected changes when someone updates the source environment. Learn more in [Environment versioning](/docs/esc/concepts/versioning/).
{{< /notes >}}

### Step 2: Define configuration in your ESC environment

ESC environments are YAML documents that you can edit using the CLI or Pulumi Cloud console. Use the CLI to edit your environment:

```bash
pulumi env edit my-project/dev
```

You can also edit environments in the [Pulumi Cloud console](https://app.pulumi.com/signin) if you prefer a visual editor.

In your ESC environment, use the `pulumiConfig` block to expose values to Pulumi IaC. Wrap the values you created earlier in a `pulumiConfig` block:

```yaml
values:
  pulumiConfig:
    region: us-west-2
    apiKey:
      fn::secret: demo-secret-123
```

Values in `pulumiConfig` can be strings, numbers, booleans, or secrets (using `fn::secret`).

The `pulumiConfig` block is the bridge between ESC and Pulumi IaC. Any values you define under `pulumiConfig` become available in your Pulumi program through the standard Configuration API.

This allows you to centralize all your configuration and secrets in ESC while accessing them through familiar Pulumi config patterns like `config.get()` or `config.require()`.

### Step 3: Access configuration in your code

Use Pulumi's standard Configuration API to access these values in your infrastructure code:

{{< example-program path="aws-import-export-pulumi-config" >}}

Your Pulumi program now retrieves configuration and secrets from ESC. Run `pulumi preview` or `pulumi up` to see it in action.

## Next steps

Now that you've created your first environment and connected it to a stack, here's where to go next:

- **[Concepts](/docs/esc/concepts/)** - Understand how ESC works and the full set of capabilities it offers
- **[Providers](/docs/esc/providers/)** - Pull secrets and generate dynamic credentials from external sources like AWS, Azure, GCP, Vault, and 1Password
- **[Rotators](/docs/esc/providers/rotators/)** - Automatically rotate credentials like API keys and database passwords on a schedule or on demand
- **[Integrations](/docs/esc/integrations/)** - Consume ESC environments from Kubernetes, the External Secrets Operator, the Secrets Store CSI Driver, and more
- **[Configure OpenID Connect](/docs/esc/guides/configuring-oidc/)** - Set up OIDC trust so ESC can issue short-lived cloud credentials
- **[Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/)** - Dynamic cloud credentials, external secret stores, and environment composition in your stacks
