---
title_tag: Integrate ESC with Pulumi IaC
title: Integrate with Pulumi IaC
h1: Integrate ESC with Pulumi IaC
meta_desc: Learn how to use Pulumi ESC environments in your Pulumi infrastructure as code projects to centralize secrets and configuration.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-integrate-pulumi-iac
    weight: 10
aliases:
  - /docs/esc/get-started/integrate-with-pulumi-iac/
  - /docs/pulumi-cloud/esc/get-started/integrate-with-pulumi-iac/
---

This guide shows you how to integrate Pulumi ESC with your Pulumi IaC projects to centralize configuration and secrets across all your stacks.

{{< notes type="info" >}}
**This guide is for existing Pulumi IaC users.** If you're new to Pulumi IaC, start with the [Pulumi IaC Get Started guide](/docs/get-started/) first.
{{< /notes >}}

If you completed the [ESC Get Started guide](/docs/esc/get-started/), you already have an environment with values like `region` and `apiKey`. This guide shows you how to reference that same environment from your Pulumi stack configuration.

## Prerequisites

- [Pulumi CLI](/docs/install/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An existing Pulumi project (or create one with `pulumi new`)
- An ESC environment with configuration values (see [Get Started](/docs/esc/get-started/) to create one)

## Add ESC to your Pulumi stack

### Step 1: Reference your ESC environment

In your stack configuration file (`Pulumi.<stack-name>.yaml`), add an `environment` block that references your ESC environment:

```yaml
environment:
  - <your-org>/<your-environment-name>
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

### Step 2: Define configuration in your ESC environment

ESC environments are YAML documents that you can edit using the CLI or Pulumi Cloud console. Use the CLI to edit your environment:

```bash
esc env edit <your-proj>/<your-environment-name>
```

You can also edit environments in the [Pulumi Cloud console](https://app.pulumi.com) if you prefer a visual editor.

In your ESC environment, use the `pulumiConfig` block to expose values to Pulumi IaC. If you're using the environment from the Get Started guide, wrap your existing values in a `pulumiConfig` block:

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

## Common patterns

### Using dynamic cloud credentials

To share AWS OIDC credentials across multiple stacks, configure your ESC environment to generate short-lived credentials:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/pulumi-deployment-role
          sessionName: pulumi-session
  pulumiConfig:
    aws:region: ${aws.login.region}
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

This pattern works everywhere Pulumi runs: locally, in CI/CD, Pulumi Deployments, and GitHub Actions. Similar patterns are available for Azure (`fn::open::azure-login`) and GCP (`fn::open::gcp-login`).

Learn more in [Dynamic login credentials](/docs/esc/integrations/dynamic-login-credentials/) and [Configuring OIDC](/docs/esc/guides/configuring-oidc/).

### Managing API keys and secrets

Pull third-party API keys from external secret stores:

```yaml
values:
  pulumiConfig:
    myApp:datadogApiKey:
      fn::secret:
        fn::open::azure-secrets:
          login: ${azure.login}
          get:
            secretId: https://my-keyvault.vault.azure.net/secrets/datadog-api-key
```

Learn more in [Dynamic secrets](/docs/esc/integrations/dynamic-secrets/).

### Environment-specific configuration

Compose environments to share common configuration while overriding values per environment:

```yaml
# common environment
values:
  pulumiConfig:
    myApp:instanceType: t3.micro
    myApp:replicas: 1

# production environment (imports common)
imports:
  - common
values:
  pulumiConfig:
    myApp:instanceType: t3.large  # override for production
    myApp:replicas: 3              # override for production
```

Learn more in [Importing environments](/docs/esc/guides/importing-environments/).

## Next steps

- [Dynamic login credentials](/docs/esc/integrations/dynamic-login-credentials/) - Generate dynamic cloud credentials with OIDC
- [Dynamic secrets](/docs/esc/integrations/dynamic-secrets/) - Pull from AWS, Azure, GCP secret stores
- [Importing environments](/docs/esc/guides/importing-environments/) - Compose configuration hierarchies
- [Pulumi IaC integration reference](/docs/esc/integrations/infrastructure/pulumi-iac/) - Complete integration documentation
