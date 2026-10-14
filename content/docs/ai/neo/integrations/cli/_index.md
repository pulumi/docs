---
title: CLI integrations
title_tag: CLI integrations | Pulumi Agents
h1: CLI integrations
meta_desc: Give Pulumi Agents scoped access to cloud CLIs (aws, gcloud, az, kubectl) using credentials managed by Pulumi ESC.
aliases:
- /docs/ai/integrations/cli/
menu:
    ai:
        name: Cloud CLI integrations
        parent: ai-agents-integrations
        weight: 20
        identifier: ai-integrations-cli
---

CLI integrations let Pulumi Agents query your cloud infrastructure directly, through `aws`, `gcloud`, `az`, and `kubectl`. When an agent needs to list S3 buckets, inspect a Kubernetes deployment, or check a firewall rule, it calls the CLI against credentials you manage in [Pulumi ESC](/docs/esc/), scoped to exactly the permissions you choose.

## How CLI integrations work

A connected CLI integration has three parts:

1. **A supported CLI**: `aws`, `gcp`, `azure`, or `kubernetes`. Agents know how to invoke each one.
1. **An ESC environment** you own that emits the environment variables the CLI expects (for example, `AWS_ACCESS_KEY_ID` for the AWS CLI).
1. **A name** you give the connection (for example, `production-aws`). The agent refers to the connection by this name when it decides which one to use.

When an agent decides to use the CLI, it runs the equivalent of:

```bash
pulumi env run <orgLogin>/<escProject>/<escEnvironment> -- <cli> <args>
```

ESC opens the environment, materializes its environment variables and files, runs the CLI, and tears the environment back down. **Pulumi Cloud never stores cloud credentials for CLI integrations.** ESC owns the credentials and decrypts them only at task time.

## Supported CLIs

| CLI | Tool | Required environment variables | Optional |
|---|---|---|---|
| `aws` | AWS CLI (`aws`) | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | `AWS_SESSION_TOKEN` (temporary credentials), `AWS_REGION` |
| `gcp` | Google Cloud CLI (`gcloud`) | `GOOGLE_APPLICATION_CREDENTIALS` (path to a service-account key file) | `CLOUDSDK_CORE_PROJECT` |
| `azure` | Azure CLI (`az`) | `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID` | `AZURE_SUBSCRIPTION_ID` |
| `kubernetes` | Kubernetes CLI (`kubectl`) | `KUBECONFIG` (path to a kubeconfig file) | None |

### Recommended credential setup

Each CLI has a well-supported ESC pattern that issues short-lived credentials at task time, so you don't end up storing long-lived secrets anywhere. For AWS, Google Cloud, and Azure there are two paths: the Login Provider Setup wizard does the work for you, or you can set up the trust relationship by hand. For Kubernetes, you write the ESC environment yourself.

#### Recommended path: Login Provider Setup wizard (AWS, GCP, Azure)

{{% notes type="tip" %}}
**Recommended for first-time setup.** Pulumi Cloud can automate the OIDC trust setup and create a ready-to-use ESC environment in one flow. From the **Environments** page, select **Create environment**, then choose your cloud provider under **Login Provider Setup**. The wizard handles the IAM role or workload-identity-federation setup and writes the ESC environment for you. When it finishes, your environment is ready to use and you can skip ahead to [Connect the integration in Neo](#2-connect-the-integration-in-neo).

See the [ESC onboarding blog post](/blog/esc-new-onboarding/) for a walkthrough with screenshots.
{{% /notes %}}

#### Manual cloud setup (AWS, GCP, Azure)

If you didn't use the wizard, or you'd rather configure the trust relationship explicitly, set up the cloud-side trust and the ESC environment yourself:

- **AWS: use OIDC with the [`aws-login`](/docs/esc/providers/login/aws-login/) provider.** Pulumi Cloud federates with AWS IAM via OpenID Connect; the `aws-login` provider exchanges a Pulumi-issued OIDC token for short-lived AWS credentials at task time. Follow [Configuring OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/) to set up the IAM role and trust policy.
- **Google Cloud: use OIDC with the [`gcp-login`](/docs/esc/providers/login/gcp-login/) provider.** Uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation). Follow [Configuring OpenID Connect for Google Cloud](/docs/esc/guides/configuring-oidc/gcp/) to set up the workload identity pool and provider.
- **Azure: use OIDC with the [`azure-login`](/docs/esc/providers/login/azure-login/) provider.** Uses workload identity federation against a Microsoft Entra App. Follow [Configuring OpenID Connect for Azure](/docs/esc/guides/configuring-oidc/azure/) to set up the federated credential.

If you can't use OIDC (for example, while you're getting started), the same `*-login` providers also accept static credentials. See each provider's documentation for the static-credentials syntax.

#### Kubernetes

The [Kubernetes Cluster Access](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) guide walks through both options:

- **Stack-output kubeconfig (recommended for Pulumi-managed clusters).** Use the [`pulumi-stacks`](/docs/esc/providers/iac/pulumi-stacks/) ESC provider to read the kubeconfig from an EKS, AKS, or GKE stack output, then materialize it through `files.KUBECONFIG`. This way the cluster Neo connects to is always the cluster Pulumi just deployed, with no manual config drift.
- **Static kubeconfig.** Drop a kubeconfig directly into `files.KUBECONFIG` for clusters not managed by a Pulumi program.

## Setting up a CLI integration

An organization administrator connects each CLI to an ESC environment. The connection is shared across agents, but using it requires permission to open that environment:

- For an agent your team configures, grant access through the agent's Pulumi Cloud role.
- For Neo, the user running the task needs access.

The credentials in the environment determine what the CLI can do in the cloud account. Grant only the access the agent needs. See [Permissions](/docs/ai/agents/permissions/).

### 1. Create the ESC environment

If you don't already have one, create an ESC environment that emits the credentials the target CLI needs, following the [recommended credential setup](#recommended-credential-setup) for that CLI.

**Scope the credentials to the agent's work.** Grant only the actions and resources it needs. Apply this to every connection.

### 2. Connect the integration in Neo

{{% agent-cli-connection %}}

You can connect multiple instances of the same CLI (for example, one named `production-aws` and another named `staging-aws`), each pointing at a separate ESC environment. An agent can use multiple connections in the same task if it can open their ESC environments.

### 3. Use the integration in a task

For an agent your team has configured, connected CLI integrations are available without a selection step. Name the connection and resources in your assignment so the agent knows which account to use. For example:

> List the S3 buckets in the `production-aws` account and identify those without versioning enabled.

The agent needs permission to open the connection's ESC environment, and the AWS credentials must allow it to list buckets and read their versioning settings.

## Per-task selection

Neo provides a per-task CLI selector. Tasks for agents your team configures do not have this selector.

By default, a Neo task inherits all CLI integrations the organization has connected. If you want to narrow what Neo can reach for a specific task (for example, running an investigation against staging without granting access to production), open the **CLI integrations** submenu in the task composer and toggle individual instances off before you start the conversation. The toggles only affect the current task; the org-level configuration is unchanged.

If you select every connected instance, the task inherits any future instances connected after the task is created. If you deselect everything, the task runs with no CLI integrations at all.

The submenu also includes a **Manage CLI integrations** shortcut that takes you to the org-level settings page. If your organization hasn't connected any CLI integrations yet, the submenu shows "No CLI integrations connected".

## Disconnecting an integration

To remove a CLI integration, navigate to **Neo Settings**, **Integrations**, **CLI tools**, find the connected row, select **Manage integration**, then select **Disconnect integration**. Disconnecting:

- Removes the connection's reference to the ESC environment. **It does not modify or delete the ESC environment itself.** That remains under your control.
- Immediately prevents new tasks from using the integration.
- Tasks that are already running will lose access to the integration the next time the agent tries to use it.

## Auditing

Connect and disconnect events for CLI integrations are written to your organization's audit log, attributed to the user who performed the action. Each entry records the CLI, the connection name, and the ESC environment, so you can trace which integrations were available at any point in time.

Individual CLI invocations made by an agent during a task are visible in the task transcript alongside its other tool calls.

## Troubleshooting

**The agent can't run the CLI.** Check that the ESC environment supplies the required variables and that its credentials allow the requested action. For an ESC access error, check the configured agent's role, or the acting user's permissions for Neo. The relevant role or user must be able to open the environment.

**The agent picked the wrong account.** Give connections distinct names, such as `production-aws` and `staging-aws`, and name the intended connection in the task. For Neo, you can also use [per-task selection](#per-task-selection). Limit access to ESC environments through the agent's role or, for Neo, the user's permissions.
