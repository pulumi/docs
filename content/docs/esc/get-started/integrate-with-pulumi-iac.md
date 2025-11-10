---
title_tag: Integrate with Pulumi IaC | Pulumi ESC
title: Integrate with Pulumi IaC
h1: "Pulumi ESC: Integrate with Pulumi IaC"
meta_desc: This page provides an overview on how to use Pulumi ESC with Pulumi IaC.
weight: 4
menu:
  esc:
    parent: esc-get-started
    identifier: esc-get-started-integrate-with-pulumi-iac
aliases:
---

## Overview

Add Pulumi ESC to your existing Pulumi IaC projects in three steps to centrally manage configuration and secrets across all your stacks. This integration works seamlessly everywhere Pulumi runs, including locally, in CI/CD, Pulumi Deployments, and GitHub Actions.

## Add ESC to your Pulumi project

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

You can also reference multiple environments, which will be merged in order:

```yaml
environment:
  - my-org/common
  - my-org/aws-prod
```

### Step 2: Define configuration in your ESC environment

In your ESC environment file, use the `pulumiConfig` block to expose values to Pulumi IaC:

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

## Practical examples

### Centralizing cloud credentials

To share AWS OIDC credentials across multiple stacks, configure your ESC environment like this:

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

Learn more about [dynamic cloud credentials](/docs/esc/get-started/use-short-term-credentials/).

### Managing API keys and secrets

Store third-party API keys centrally and reference them across projects:

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

Learn more about [retrieving secrets from external sources](/docs/esc/get-started/retrieve-external-secrets/).

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

Learn more about [importing and composing environments](/docs/esc/get-started/import-environments/).

## Next steps

Now that you've integrated ESC with your Pulumi IaC project, explore more ESC features:

- [Store and retrieve secrets](/docs/esc/get-started/store-and-retrieve-secrets/) - Learn how to manage secrets in ESC
- [Import environments](/docs/esc/get-started/import-environments/) - Compose environments for team boundaries
- [Dynamic cloud credentials](/docs/esc/get-started/use-short-term-credentials/) - Generate short-lived OIDC credentials
- [External secret providers](/docs/esc/get-started/retrieve-external-secrets/) - Pull secrets from AWS, Azure, GCP, and more
- [ESC + Pulumi IaC reference](/docs/esc/integrations/infrastructure/pulumi-iac/) - Complete integration documentation

{{< get-started-stepper >}}
