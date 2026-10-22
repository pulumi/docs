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

The CLI connection stores a reference to the ESC environment. When the command runs, ESC opens the environment and supplies its variables and temporary files to the CLI.

## Supported CLIs

| CLI | Tool | Required environment variables | Optional |
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

- **Stack-output kubeconfig (recommended for Pulumi-managed clusters).** Use the [`pulumi-stacks`](/docs/esc/providers/iac/pulumi-stacks/) ESC provider to read the kubeconfig from an EKS, AKS, or GKE stack output, then materialize it through `files.KUBECONFIG`. The connection reads the kubeconfig from the stack output when the environment is opened.
- **Static kubeconfig.** Drop a kubeconfig directly into `files.KUBECONFIG` for clusters not managed by a Pulumi program.

## Setting up a CLI integration

A teammate with permission to manage organization integrations (`org_integrations:update`) connects each CLI to an ESC environment. The connection is shared across agents, but using it requires permission to open that environment:

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

To remove a CLI integration, navigate to **Agent Settings**, **Integrations**, **CLI tools**, find the connected row, select **Manage integration**, then select **Disconnect integration**. Disconnecting:

- Removes the connection's reference to the ESC environment. **It does not modify or delete the ESC environment itself.** That remains under your control.
- Immediately prevents new tasks from using the integration.
- Existing tasks reload the available connections when the agent next resumes work. Disconnecting does not revoke permission to open the ESC environment or credentials already issued by it.

## Auditing

Connect and disconnect events for CLI integrations are written to your organization's audit log, attributed to the user who performed the action. Each entry records the CLI, the connection name, and the ESC environment, so you can trace which integrations were available at any point in time.

Individual CLI invocations made by an agent during a task are visible in the task transcript alongside its other tool calls.

## Troubleshooting

**The agent can't run the CLI.** Check that the ESC environment supplies the required variables and that its credentials allow the requested action. For an ESC access error, check the configured agent's role, or the acting user's permissions for Neo. The relevant role or user must be able to open the environment.

**The agent picked the wrong account.** Give connections distinct names, such as `production-aws` and `staging-aws`, and name the intended connection in the task. For Neo, you can also use [per-task selection](#per-task-selection). Limit access to ESC environments through the agent's role or, for Neo, the user's permissions.
