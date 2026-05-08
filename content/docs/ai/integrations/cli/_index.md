---
title: CLI Integrations
title_tag: Neo CLI Integrations
h1: CLI Integrations
meta_desc: Give Neo scoped access to cloud CLIs (aws, gcloud, az, kubectl) using credentials managed by Pulumi ESC.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: CLI Integrations
        parent: ai-integrations
        weight: 1
        identifier: ai-integrations-cli
---

CLI integrations give Neo scoped access to a cloud command-line tool — `aws`, `gcloud`, `az`, or `kubectl` — using credentials you manage in [Pulumi ESC](/docs/esc/). When Neo runs the CLI, it does so through `pulumi env run`, so the CLI sees only the credentials your ESC environment chooses to expose, and only for the duration of the command.

CLI integrations are distinct from [MCP integrations](/docs/ai/integrations/). MCP integrations bring **context** into a task — issues from Linear, traces from Honeycomb, runbooks from Confluence. CLI integrations let Neo **act** on cloud resources by running the same CLIs your team already uses.

## How CLI integrations work

A connected CLI integration has three parts:

1. **A catalog entry** that identifies the CLI (`aws`, `gcp`, `azure`, `kubernetes`) and tells Neo how to invoke it.
1. **An ESC environment** you own that emits the environment variables that CLI expects (for example, `AWS_ACCESS_KEY_ID` for the AWS CLI).
1. **A user-chosen handle name** (for example, `production-aws`) that Neo uses to refer to the integration in its prompts.

When Neo decides to use the CLI, it runs the equivalent of:

```bash
pulumi env run <orgLogin>/<escProject>/<escEnvironment> -- <cli> <args>
```

ESC opens the environment, materializes its environment variables and files, runs the CLI, and tears the environment back down. **The Pulumi Service never stores cloud credentials for CLI integrations** — ESC owns the credentials and decrypts them only at task time.

## Supported CLIs

| Catalog ID | CLI | Required environment variables | Optional |
|---|---|---|---|
| `aws` | AWS CLI (`aws`) | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | `AWS_SESSION_TOKEN` (temporary credentials), `AWS_REGION` |
| `gcp` | Google Cloud CLI (`gcloud`) | `GOOGLE_APPLICATION_CREDENTIALS` (path to a service-account key file) | `CLOUDSDK_CORE_PROJECT` |
| `azure` | Azure CLI (`az`) | `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID` | `AZURE_SUBSCRIPTION_ID` |
| `kubernetes` | Kubernetes CLI (`kubectl`) | `KUBECONFIG` (path to a kubeconfig file) | — |

### Recommended credential setup

Each catalog entry has a well-supported ESC pattern that issues short-lived credentials at task time, so you don't end up storing long-lived secrets anywhere. For AWS, Google Cloud, and Azure there are two paths: the Login Provider Setup wizard does the work for you, or you can set up the trust relationship by hand. For Kubernetes, you write the ESC environment yourself.

#### Easiest path: Login Provider Setup wizard (AWS, GCP, Azure)

{{% notes type="tip" %}}
**Recommended for first-time setup.** Pulumi Cloud can automate the OIDC trust setup and create a ready-to-use ESC environment in one flow. From the **Environments** page, select **Create environment**, then choose your cloud provider under **Login Provider Setup**. The wizard handles the IAM role or workload-identity-federation setup and writes the ESC environment for you. When it finishes, your environment is ready to use and you can skip ahead to [Connect the integration in Neo](#2-connect-the-integration-in-neo).

See the [ESC onboarding blog post](/blog/esc-new-onboarding/) for a walkthrough with screenshots.
{{% /notes %}}

#### Manual cloud setup (AWS, GCP, Azure)

If you didn't use the wizard — or you'd rather configure the trust relationship explicitly — set up the cloud-side trust and the ESC environment yourself:

- **AWS — use OIDC with the [`aws-login`](/docs/esc/integrations/dynamic-login-credentials/aws-login/) provider.** Pulumi Cloud federates with AWS IAM via OpenID Connect; the `aws-login` provider exchanges a Pulumi-issued OIDC token for short-lived AWS credentials at task time. Follow [Configuring OpenID Connect for AWS](/docs/esc/guides/configuring-oidc/aws/) to set up the IAM role and trust policy.
- **Google Cloud — use OIDC with the [`gcp-login`](/docs/esc/integrations/dynamic-login-credentials/gcp-login/) provider.** Uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation). Follow [Configuring OpenID Connect for Google Cloud](/docs/esc/guides/configuring-oidc/gcp/) to set up the workload identity pool and provider.
- **Azure — use OIDC with the [`azure-login`](/docs/esc/integrations/dynamic-login-credentials/azure-login/) provider.** Uses workload identity federation against a Microsoft Entra App. Follow [Configuring OpenID Connect for Azure](/docs/esc/guides/configuring-oidc/azure/) to set up the federated credential.

If you can't use OIDC (for example, while you're getting started), the same `*-login` providers also accept static credentials — see each provider's documentation for the static-credentials syntax.

#### Kubernetes

The wizard doesn't cover Kubernetes, so set up the kubeconfig in your ESC environment directly. The [Kubernetes Cluster Access](/docs/esc/integrations/kubernetes/kubernetes/) guide walks through both options:

- **Stack-output kubeconfig (recommended for Pulumi-managed clusters).** Use the [`pulumi-stacks`](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/) ESC provider to read the kubeconfig from an EKS, AKS, or GKE stack output, then materialize it through `files.KUBECONFIG`. This way the cluster Neo connects to is always the cluster Pulumi just deployed, with no manual config drift.
- **Static kubeconfig.** Drop a kubeconfig directly into `files.KUBECONFIG` for clusters not managed by a Pulumi program.

## Setting up a CLI integration

CLI integrations are configured by an organization administrator and are available to every Neo task in the organization once enabled.

### 1. Create the ESC environment

If you don't already have one, create an ESC environment that emits the credentials the target CLI needs, following the [recommended credential setup](#recommended-credential-setup) for that CLI.

**Scope the environment to what Neo needs.** The CLI runs with whatever permissions the ESC environment grants. For most use cases, prefer a read-only role and broaden it deliberately as you give Neo more responsibilities.

### 2. Connect the integration in Neo

1. Open your organization's **Neo Settings**, then **Integrations**, then the **CLI tools** section.
1. Under **Available**, find the CLI you want to connect (for example, **AWS**) and select **Connect**.
1. Fill in the form:
    - **Name** — a short, unique name for this CLI integration instance (for example, `aws-dev` or `production-aws`). The name shows up in audit log entries and the per-task selector, **and Neo sees it too** — it's how the agent decides which integration to reach for ("use `production-aws` to investigate the prod outage"). Pick a name that conveys what the integration is for.
    - **ESC environment** — pick the environment you created in the previous step from the dropdown. Only environments in the current organization are listed.
1. Select **Connect**.

You can connect multiple instances of the same CLI — for example, one named `production-aws` and another named `staging-aws` — each pointing at a separate ESC environment. Neo can use any of them in the same task.

### 3. Use the integration in a task

The next time you start a Neo task, Neo will see the connected CLI integration as a tool it can call. You don't need to mention it explicitly — Neo decides when to reach for the CLI based on the conversation. For example:

> **You:** Neo, list the S3 buckets in our `production-aws` account and tell me which ones don't have versioning enabled.

Neo runs `pulumi env run <ref> -- aws s3api list-buckets`, follows up with `get-bucket-versioning` for each, and reports back.

## Per-task selection

By default, every task inherits all CLI integrations the organization has connected. If you want to narrow what Neo can reach for a specific task — for example, running an investigation against staging without granting access to production — open the **CLI integrations** submenu in the task composer and toggle individual instances off before you start the conversation. The toggles only affect the current task; the org-level configuration is unchanged.

If you select every connected instance, the task inherits any future instances connected after the task is created. If you deselect everything, the task runs with no CLI integrations at all.

The submenu also includes a **Manage CLI integrations** shortcut that takes you to the org-level settings page. If your organization hasn't connected any CLI integrations yet, the submenu shows "No CLI integrations connected".

## Disconnecting an integration

To remove a CLI integration, navigate to **Neo Settings**, **Integrations**, **CLI tools**, find the connected row, select **Manage integration**, then select **Disconnect integration**. Disconnecting:

- Removes Neo's reference to the ESC environment. **It does not modify or delete the ESC environment itself** — that remains under your control.
- Immediately prevents new tasks from using the integration.
- Tasks that are already running will lose access to the integration the next time Neo tries to use it.

## Auditing

Connect and disconnect events for CLI integrations are written to your organization's audit log, attributed to the user who performed the action. Each entry records the catalog ID, the handle name, and the ESC environment ref, so you can trace which integrations were available at any point in time.

Individual CLI invocations made by Neo during a task are visible in the task transcript alongside the rest of Neo's tool calls.

## Troubleshooting

**Neo says it can't run the CLI.** Most often the linked ESC environment is missing a required environment variable, or the credentials it produces aren't authorized for the action Neo attempted. Open the ESC environment in Pulumi Cloud and use **Open environment** to check what variables are emitted, then re-run the failing command locally with `pulumi env run <ref> -- <cli> <args>` to reproduce the error.

**Neo picked the wrong account.** If you have several connected instances of the same CLI (for example, both `production-aws` and `staging-aws`), give them clearly distinguishable handle names and mention the handle by name in your task prompt. You can also use [per-task selection](#per-task-selection) to limit the task to a single instance.

**The integration disappeared from the task composer.** Neo reads the catalog at task start. If the integration was disconnected — or if its ESC environment was deleted — Neo will skip it and continue with the rest of the task's tools.
