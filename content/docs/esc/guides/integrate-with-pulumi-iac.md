---
title_tag: Integrate ESC with Pulumi IaC
title: Integrate with Pulumi IaC
h1: Integrate ESC with Pulumi IaC
meta_desc: Learn how to use Pulumi ESC environments in your Pulumi infrastructure as code projects to centralize secrets and configuration.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-integrate-pulumi-iac
    weight: 1
aliases:
  - /docs/esc/get-started/integrate-with-pulumi-iac/
  - /docs/pulumi-cloud/esc/get-started/integrate-with-pulumi-iac/
---

This guide shows you how to integrate Pulumi ESC with your Pulumi IaC projects to centralize configuration and secrets across all your stacks.

## Prerequisites

- [Pulumi CLI](/docs/install/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An existing Pulumi project (or create one with `pulumi new`)
- An ESC environment with configuration values (see [Managing secrets](/docs/esc/guides/managing-secrets/) to create one)

## Add ESC to your Pulumi stack

### Step 1: Reference your ESC environment

In your stack configuration file (`Pulumi.<stack-name>.yaml`), add an `environment` block that references your ESC environment:

```yaml
environment:
  - <your-org>/<your-environment-name>
```

For example, if your ESC environment is `my-org/aws-prod`:

```yaml
environment:
  - my-org/aws-prod
```

You can also reference multiple environments, which will be merged in order (later values override earlier ones):

```yaml
environment:
  - my-org/common
  - my-org/aws-prod
```

### Step 2: Define configuration in your ESC environment

ESC environments are YAML documents typically managed in Pulumi Cloud. To edit your environment:

**Via the Pulumi Cloud console:**

1. Navigate to [Pulumi Cloud](https://app.pulumi.com)
1. Select **Environments** in the left navigation
1. Select your environment to open the editor
1. Add configuration in the YAML editor

**Via the CLI:**

```bash
esc env edit <your-org>/<your-environment-name>
```

In your ESC environment, use the `pulumiConfig` block to expose values to Pulumi IaC:

```yaml
values:
  pulumiConfig:
    aws:region: us-west-2
    myApp:apiKey:
      fn::secret: demo-api-key-123
```

The `pulumiConfig` block maps ESC values to Pulumi configuration keys. Values defined here become available to your Pulumi program through the standard Configuration API.

### Step 3: Access configuration in your code

Use Pulumi's standard Configuration API to access these values in your infrastructure code:

{{< example-program path="aws-import-export-pulumi-config" >}}

That's it! Your Pulumi program now retrieves configuration and secrets from ESC. Run `pulumi preview` or `pulumi up` to see it in action.

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

This pattern works everywhere Pulumi runs: locally, in CI/CD, Pulumi Deployments, and GitHub Actions.

Learn more in [Setting up OIDC](/docs/esc/guides/setting-up-oidc/).

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

Learn more in [Integrating external secrets](/docs/esc/guides/external-secrets/).

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

- [Setting up OIDC](/docs/esc/guides/setting-up-oidc/) - Generate dynamic cloud credentials
- [Integrating external secrets](/docs/esc/guides/external-secrets/) - Pull from AWS, Azure, GCP vaults
- [Importing environments](/docs/esc/guides/importing-environments/) - Compose configuration hierarchies
- [ESC + Pulumi IaC reference](/docs/esc/integrations/infrastructure/pulumi-iac/) - Complete integration documentation
