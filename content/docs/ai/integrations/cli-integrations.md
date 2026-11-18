---
title: CLI integrations
title_tag: CLI integrations | Pulumi Agents
h1: CLI integrations
meta_desc: Give Pulumi Agents scoped access to cloud CLIs (aws, gcloud, az, kubectl) using credentials managed by Pulumi ESC.
aliases:
- /docs/ai/integrations/cli/
- /docs/ai/neo/integrations/cli/
menu:
    ai:
        name: Cloud CLI integrations
        parent: ai-agents-integrations
        weight: 20
        identifier: ai-integrations-cli
---

Connect a cloud CLI so an agent can inspect resources in AWS, Google Cloud, Azure, or Kubernetes. Each connection uses a [Pulumi ESC](/docs/esc/) environment to supply credentials when the agent runs a command. Those credentials determine which resources the agent can access and whether it can change them.

## How CLI integrations work

A connection pairs a CLI with an ESC environment and a name, such as `production-aws`, that you can use in task messages.

When an agent decides to use the CLI, it runs the equivalent of:

```bash
pulumi env run <orgLogin>/<escProject>/<escEnvironment> -- <cli> <args>
```

The connection stores the environment's organization, project, and name. It does not copy its credentials. ESC supplies the environment's current variables and temporary files whenever the CLI runs.

## Supported CLIs

| Integration ID | CLI | Required environment variables | Optional |
|---|---|---|---|
| `aws` | AWS CLI (`aws`) | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | `AWS_SESSION_TOKEN` (temporary credentials), `AWS_REGION` |
| `gcp` | Google Cloud CLI (`gcloud`) | `CLOUDSDK_AUTH_ACCESS_TOKEN` (access token) | `CLOUDSDK_CORE_PROJECT` |
| `azure` | Azure CLI (`az`) | `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID` | `AZURE_SUBSCRIPTION_ID` |
| `kubernetes` | Kubernetes CLI (`kubectl`) | `KUBECONFIG` (path to a kubeconfig file) | None |

### Recommended credential setup

- [AWS](/docs/ai/agents/integrations/aws/): use ESC's `aws-login` provider to issue temporary credentials for an IAM role.
- [Google Cloud](/docs/ai/agents/integrations/google-cloud/): export the `gcp-login` provider's access token as `CLOUDSDK_AUTH_ACCESS_TOKEN`.
- [Azure](/docs/ai/agents/integrations/azure/): supply service principal credentials and include the Azure CLI sign-in instructions in the connection notes.

The **Login Provider Setup** wizard on the **Environments** page can create cloud trust relationships and ESC environments. Check the environment's outputs against the CLI requirements above before connecting it. An environment configured for a Pulumi provider may use different variables from its cloud CLI.

#### Kubernetes

The [Kubernetes Cluster Access](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) guide walks through both options:

- **Stack-output kubeconfig (recommended for Pulumi-managed clusters).** Use the [`pulumi-stacks`](/docs/esc/providers/iac/pulumi-stacks/) ESC provider to read the kubeconfig from an EKS, AKS, or GKE stack output, then write it to a temporary file through `files.KUBECONFIG`. The connection reads the kubeconfig from the stack output when the environment is opened.
- **Static kubeconfig.** Set the kubeconfig contents in `files.KUBECONFIG` for clusters not managed by a Pulumi program.

If the kubeconfig runs an authentication command, supply the credentials that command needs in the same ESC environment. For example, [Amazon EKS uses `aws eks get-token`](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html), so an EKS connection also needs AWS credentials for an identity with access to the cluster.

## Setting up a CLI integration

You need permission to manage organization integrations (`org_integrations:update`) to create a connection. You also need an ESC environment that supplies credentials for the cloud account or Kubernetes cluster.

To use the connection, the agent must be able to retrieve those credentials by opening the ESC environment (`environment:open`):

- For an agent your team configures, grant access through the agent's Pulumi Cloud role.
- For a Neo task, the user running it needs access.

The cloud credentials separately control access to cloud resources. See [Permissions and approvals](/docs/ai/agents/permissions/#scope-credentials-for-connected-tools) to restrict that access.

### 1. Create the ESC environment

If you don't already have one, create an ESC environment that supplies the credentials the CLI needs, following the [recommended credential setup](#recommended-credential-setup) for that CLI.

### 2. Connect the CLI to an ESC environment {#2-connect-the-integration-in-neo}

{{% agent-cli-connection %}}

You can connect multiple instances of the same CLI (for example, one named `production-aws` and another named `staging-aws`), each pointing at a separate ESC environment. An agent can use multiple connections in the same task if it can open their ESC environments.

### 3. Use the integration in a task

For an agent your team has configured, connected CLI integrations are available without a selection step. Name the connection and resources in your assignment so the agent knows which account to use. The [provider guides](#recommended-credential-setup) include examples.

## Per-task selection

Neo tasks provide a per-task CLI selector. Tasks for agents your team configures do not have this selector.

By default, all CLI integrations connected to your organization are selected for a Neo task. Open the **CLI integrations** submenu in the task composer and turn off connections that are not needed for the assignment. The selection affects only that task; the organization configuration is unchanged.

Selecting connections does not narrow their credentials or revoke access to other ESC environments. To restrict a Neo task to staging, give the user access only to the staging ESC environments and use credentials that can access only staging resources.

If you keep all connections selected, the task can also use connections added later. If you deselect every connection, the task has no CLI integrations.

The submenu also includes a **Manage CLI integrations** shortcut that takes you to the organization settings page. If your organization hasn't connected any CLI integrations yet, the submenu shows "No CLI integrations connected".

## Disconnecting an integration

To remove a CLI integration, navigate to **Agent Settings**, **Integrations**, **CLI tools**, find the connected row, select **Manage integration**, then select **Disconnect integration**. New tasks can no longer use the connection. Existing tasks stop using it when the agent next resumes work.

Disconnecting leaves the ESC environment unchanged. It does not revoke permission to open that environment or invalidate credentials already issued. To remove access immediately, revoke it in ESC or at the cloud provider as appropriate.

## Auditing

Connect and disconnect events for CLI integrations are written to your organization's audit log, attributed to the user who performed the action. Each entry records the CLI, the connection name, and the ESC environment, so you can trace which integrations were available at a given time.

Individual CLI invocations made by an agent during a task are visible in the task transcript alongside its other tool calls.

## Troubleshooting

**The agent can't run the CLI.** Check that the ESC environment supplies the required variables and that its credentials allow the requested action. For an ESC access error, check the configured agent's role, or the acting user's permissions for a Neo task. The relevant role or user must be able to open the environment.

**The agent picked the wrong account.** Give connections distinct names, such as `production-aws` and `staging-aws`, and name the intended connection in the task. For Neo tasks, you can also use [per-task selection](#per-task-selection). Limit access to ESC environments through the agent's role or, for Neo tasks, the user's permissions.
