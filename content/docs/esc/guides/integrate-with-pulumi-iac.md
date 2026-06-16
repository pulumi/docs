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
  - /docs/esc/integrations/integrate-with-pulumi-iac/
  - /docs/esc/integrations/infrastructure/pulumi-iac/
---

This guide covers advanced patterns for integrating Pulumi ESC with your Pulumi IaC projects to centralize configuration and secrets across all your stacks.

{{< notes type="info" >}}
**This guide is for existing Pulumi IaC users.** If you're new to Pulumi IaC, start with the [Pulumi IaC Get Started guide](/docs/get-started/) first. If you haven't connected an ESC environment to a stack yet, start with the [ESC Get Started guide](/docs/esc/get-started/), which walks you through referencing an environment and exposing values through `pulumiConfig`.
{{< /notes >}}

## Prerequisites

- [Pulumi CLI](/docs/install/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An existing Pulumi project (or create one with `pulumi new`)
- An ESC environment referenced from your stack (see [Get Started](/docs/esc/get-started/#add-esc-to-your-pulumi-stack))

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

Learn more in [Dynamic login credentials](/docs/esc/providers/login/) and [Configuring OIDC](/docs/esc/guides/configuring-oidc/).

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

Learn more in [Dynamic secrets](/docs/esc/providers/secrets/).

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

Learn more in [Importing environments](/docs/esc/concepts/imports/).

{{< notes type="info" >}}
When a key is set both in an environment's `pulumiConfig` and explicitly in your stack configuration, the explicit stack value takes precedence. See [Precedence](/docs/esc/concepts/outputs/#precedence-1) for the full rules.
{{< /notes >}}

## Convert existing stack config to an ESC environment

To convert your existing stack config to a new ESC environment, use the Pulumi CLI:

```shell
pulumi config env init
```

See the [`pulumi config env init`](/docs/iac/cli/commands/pulumi_config_env_init/) reference for more information.

## Automation API integration

You can manage a stack's imported environments with [Automation API](/docs/iac/concepts/automation-api/) in [Node](/docs/reference/pkg/nodejs/pulumi/pulumi/classes/automation.Stack.html#addEnvironments), [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/auto#LocalWorkspace.AddEnvironments), and [Python](/docs/reference/pkg/python/pulumi/#pulumi.automation.LocalWorkspace.add_environments). The following methods are supported:

- `addEnvironments(...)`: Append environments to your Pulumi stack's import list.
- `listEnvironments()`: Retrieve the environments currently imported into your stack.
- `removeEnvironment(environment)`: Remove a specific environment from your stack's import list.

## Accessing Pulumi stack outputs

You can read [outputs](/docs/iac/concepts/inputs-outputs/#outputs) from other [Pulumi stacks](/docs/iac/concepts/stacks/) into an ESC environment with the [`pulumi-stacks` provider](/docs/esc/providers/iac/pulumi-stacks/).

## Next steps

- [Dynamic login credentials](/docs/esc/providers/login/) - Generate dynamic cloud credentials with OIDC
- [Dynamic secrets](/docs/esc/providers/secrets/) - Pull from AWS, Azure, GCP secret stores
- [Importing environments](/docs/esc/concepts/imports/) - Compose configuration hierarchies
