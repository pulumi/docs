---
title: "Pushing Pulumi ESC Secrets into External Platforms"
date: 2024-09-17T00:00:00-03:00
draft: false
meta_desc: "Sync secrets and configuration values across external platforms using
  Pulumi ESC and Pulumi IaC."
meta_image: "meta.png"
authors:
  - komal-ali
tags:
  - esc
  - secrets
search:
  keywords:
    - Secrets
    - Sync
    - Secrets Manager
    - Secret Management
---

Managing secrets across multi-cloud infrastructures has long been a challenge for developers and operations teams. This article explores [Pulumi IaC](/docs/iac/)-based strategy to centrally define secrets and configuration in [Pulumi ESC](/docs/esc/) and automatically sync these values across the external platforms where they will be utilized, effectively reducing secret sprawl and manual overhead.

<!--more-->

## The Secret Management Conundrum

Traditional secret management often leads to a phenomenon known as secret sprawl. This occurs when secrets are duplicated across multiple systems, including various repositories, cloud providers, and CI/CD pipelines. The result is a tangled web of inconsistencies that makes tracking and managing secrets a Herculean task.

Updating secrets manually across all these systems is not only tedious but also error-prone. Each time a secret changes, it needs to be updated in every repository, cloud platform, and CI/CD tool where it's used. This process is time-consuming and frustrating, often leading to mistakes that can compromise security.

Moreover, the lack of a centralized system makes it difficult to track where secrets are stored and who has access to them. This complicates security audits and compliance efforts. When a secret is compromised, the process of revoking and rotating it across multiple systems can be slow and disruptive, potentially leading to application downtime.

## ESC Sync with Infrastructure as Code

Using Pulumi building blocks like ESC and IaC, we can create a pattern where secrets and configuration can be centrally defined in ESC, and then automatically synced across the external platforms where they will be utilized.

Consider the following ESC environment, which imports an environment "my-project/my-imported-env" and defines a set of secrets and configuration values to be synced:

```yaml
imports:
  - my-project/my-imported-env@stable
values:
  sync:
    awsSecretsManager:
      value:
        myConfigKey: ${my-imported-env-foo}
        myNestedKey:
          haha: ${my-imported-env-bar}
        mySecret: ${my-imported-env-password}
      name: name-in-secrets-manager
```

The `sync` block defines the secrets and configuration values to be synced. In this example, we are syncing values to AWS Secrets Manager. The `value` field contains the actual values to be synced, while the `name` field specifies the name of the secret in AWS Secrets Manager.

To automate the synchronization process, we define a Pulumi program that creates a Pulumi ESC environment, Pulumi IaC stack, and Pulumi [deployment](/docs/pulumi-cloud/deployments/) settings for the target stack. We then define a set of pre-run commands that extract the values from the environment and set them as configuration values in the target stack. The `syncCronSchedule` variable specifies how often the synchronization process should run.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as service from "@pulumi/pulumiservice";

const config = new pulumi.Config();
const orgName = pulumi.getOrganization();

// projectName is the name of the project where the target stack is located
const projectName = config.require("projectName");

// stackName is the name of the target stack
const stackName = config.get("stackName") || "dev";

// repository is the GitHub repository where the target stack is located (for deployment settings)
const repository = config.require("repository");

// how often you want to sync. Default is hourly
const syncCronSchedule = config.get("syncCronSchedule") || "0 * * * *"

// envPath is the path to the environment file that contains the secrets or configuration to be synced
const envPath = config.get("envPath") || "syncEnv.yaml";

const env = new service.Environment("env", {
  organization: orgName,
  project: projectName,
  name: stackName,
  yaml: new pulumi.asset.FileAsset(envPath)
});

const stack = new service.Stack("esc-sync-aws-secretsmanager", {
    organizationName: orgName,
    projectName,
    stackName,
})

const fullyQualifiedStackName = pulumi.interpolate`${orgName}/${projectName}/${stackName}`;
const fullyQualifiedEnvName = pulumi.interpolate`${orgName}/${projectName}/${env.name}`;

const settings = new service.DeploymentSettings("deployment_settings", {
    organization: orgName,
    project: stack.projectName,
    stack: stack.stackName,
    github: {
        repository,
    },
    sourceContext: {
        git: {
            branch: "main",
            repoDir: "sync/target",
        }
    },
    operationContext: {
        preRunCommands: [
            'pulumi login',
            pulumi.interpolate`pulumi config env add ${projectName}/${env.name} -s ${fullyQualifiedStackName} --yes`,
            pulumi.interpolate`pulumi env open ${fullyQualifiedEnvName} sync.awsSecretsManager.value > sync.json`,
            pulumi.interpolate`pulumi config set -s ${fullyQualifiedStackName} secretName $(pulumi env open ${fullyQualifiedEnvName} sync.awsSecretsManager.name)`,
        ]
    }
});

const schedule = new service.DeploymentSchedule("update_schedule", {
    organization: orgName,
    project: settings.project,
    stack: settings.stack,
    scheduleCron: syncCronSchedule,
    pulumiOperation: "update",
})
```

Finally, we define a Pulumi program that creates the AWS Secrets Manager secret and secret version based on the values extracted from the environment file. The `sync.json` file contains the values to be synced, which are read and set as the secret string in the secret version. This Pulumi program is executed on a schedule to ensure that the secrets and configuration values are up-to-date between Pulumi ESC and AWS Secrets Manager.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const config = new pulumi.Config();
const name = config.require("secretName");

// Read a json file from the local filesystem using node.js fs module
const json = fs.readFileSync("sync.json", "utf8");

const secret = new aws.secretsmanager.Secret(name, {
    recoveryWindowInDays: 0,
})

const secretVersion = new aws.secretsmanager.SecretVersion(`${name}-version`, {
    secretId: secret.id,
    secretString: json,
})

// Export the name of the secret
export const secretName = secret.name;
```

This pattern allows you to define secrets and configuration values in a single location and automatically sync them across external platforms. The same pattern can be extended to create secrets in other platforms like [Azure Key Vault](https://github.com/pulumi/esc-examples/tree/main/sync/azure-key-vault), [GCP Secrets Manager](https://github.com/pulumi/esc-examples/tree/main/sync/gcp-secrets-manager), [GitHub Secrets](https://github.com/pulumi/esc-examples/tree/main/sync/github-secrets), [HashiCorp Vault](https://github.com/pulumi/esc-examples/tree/main/sync/vault) and countless others.

## Webhooks: An Event-Driven Alternative Approach

In addition to the scheduled synchronization approach, Pulumi ESC also supports [webhooks](/docs/esc/environments/webhooks/). Webhooks allow you to respond to events in real-time, such as when a secret is updated in ESC, and take immediate action to sync the new value to an external platform.

In the example below, instead of a scheduled deployment, we define a webhook that triggers when the Pulumi ESC environment is updated. This ensures that the secrets and configuration values are always in sync between Pulumi ESC and the external platform.

```typescript
const webhook = new service.Webhook("webhook", {
    organizationName: orgName,
    projectName: settings.project,
    stackName: settings.stack,
    displayName: "Sync to AWS Secrets Manager",
    environmentName: pulumi.interpolate`${env.project}/${env.name}`,
    filters: [WebhookFilters.ImportedEnvironmentChanged],
    format: WebhookFormat.PulumiDeployments,
    payloadUrl: pulumi.interpolate`${stack.projectName}/${stack.stackName}`,
    active: true,
})
```

When the webhook is triggered (i.e. the "my-project/my-imported-env" environment is updated), a deployment is automatically triggered, and the secrets and configuration values are synced to AWS Secrets Manager.

## Embracing a New Era of Secret Management

Using Pulumi IaC to synchronize secrets and configuration across platform boundaries represents a giant step forward in secret management. By centralizing and automating the handling of sensitive data, it addresses the key challenges of traditional approaches. Secret sprawl becomes a thing of the past, and the risks associated with manual updates are significantly reduced.

Whether you're working with AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, GitHub Secrets or other platforms, Pulumi ESC provides a streamlined solution that ensures your secrets are always secure and up-to-date. It offers the convenience and security of a single source of truth for all your secrets, allowing you to focus on building and improving your applications rather than wrestling with secret management.

We encourage you to explore [Pulumi's documentation](https://www.pulumi.com/docs/pulumi-cloud/esc/get-started) and dive into the [Pulumi ESC Sync Examples repository](https://github.com/pulumi/esc-examples/tree/main/sync) to see how you can implement this powerful tool in your own projects. Join our vibrant [community on Slack](https://slack.pulumi.com/) to discuss your experiences, ask questions, and share insights. Together, we can make secret management simpler, more secure, and more efficient.
