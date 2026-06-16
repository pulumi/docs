---
title: Customer-Managed Workflow Runners
title_tag: Set up customer-managed workflow runners | Pulumi Deployments
meta_desc: Set up, scale, and configure self-hosted workflow runner pools so Pulumi Deployments runs in your own environments.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Customer-Managed Workflow Runners
    parent: deployments-guides
    weight: 20
    identifier: deployments-guides-customer-managed-runners
---

Customer-managed workflow runners let you self-host the compute that runs Pulumi Deployments, [Insights](/docs/insights/) discovery scans, and [policy evaluations](/docs/insights/policy/), so workflows execute inside your own network and on hardware you control. For an overview of how runners fit into a deployment run — and the full configuration reference — see [Runners](/docs/deployments/deployments/runners/).

{{% notes "info" %}}
Customer-Managed Workflow Runners are available on the Business Critical edition of Pulumi Cloud. [Contact sales](/contact/?form=sales) if you are interested and want to enable Customer-Managed Workflow Runners.
{{% /notes %}}

## Using customer-managed workflow runners

Before you begin, ensure you have [Docker](https://docs.docker.com/engine/) or [Kubernetes](https://kubernetes.io/docs/home/) installed, which is required for running the workflow runner. If you plan to use workflow runners for **deployments**, you must also install the [Pulumi Github App](/docs/using-pulumi/continuous-delivery/github-app/) and update the [source control settings](/docs/deployments/get-started/) of the stack you want to deploy.

1. In the left nav, open the **Settings** dropdown and select **Organization**, then choose the **Workflow Runner Pools** tab
1. Create a new pool. Copy and save the token
1. Install the workflow runners as per the instructions on the page
1. Verify the workflow runner status by refreshing the page
1. Configure the workflow runner pool for the workflows you want to run:
   - **Deployments**: Navigate to **Stack Settings** > **Deploy** tab and select the pool under the **Deployment Runner** pool dropdown
   - **Insights discovery scans**: Navigate to **Management** > **Accounts** and select the pool for the account you want to scan
   - **Policy evaluation**: Navigate to **Management** > **Policies** > **Policy Groups** and select the pool for an audit policy group
1. **(Optional)** Add more workflow runners to the pool to increase concurrency by using the same token
1. Verify your setup:
   - **Deployments**: Run a `pulumi refresh` through the **Actions** dropdown in your stack page
   - **Insights discovery scans**: Trigger a scan from the **Management** > **Accounts** page and confirm it completes successfully
   - **Policy evaluation**: Run a policy evaluation against a stack and confirm the results appear as expected

Workflow runners poll Pulumi Cloud for pending workflows at a configurable interval (default: every 1 minute) and will disappear from the Pool details page 1-2 hours after being offline. On the deployments page, you can see all the deployments including pending deployments, and which workflow runners were used in a deployment.

Workflow runners support multiple workflow types beyond deployments, including Pulumi Insights scans and policy evaluations. By default, all workflow types are enabled. You can restrict which workflow types a workflow runner handles using the `enabled_workflow_types` configuration option.

### Scaling and concurrency

Each workflow runner process runs **one deployment at a time**, plus optionally **one Insights scan or policy evaluation in parallel**, and has no internal worker pool to configure. To increase the number of jobs your pool can run in parallel, add more workflow runner instances to the pool — each instance contributes one deployment slot and, if the pool also handles non-deployment workflow types, one additional slot for Insights scans or policy evaluations.

Pulumi Cloud assigns each pending job to exactly one runner using an exclusive claim. When multiple runners poll the same pool simultaneously, the service hands each pending job to a single runner, so the same job is never processed by two runners at the same time. Recovery behavior depends on the workflow type:

- **Insights scans and policy evaluations** are lease-based: if a runner crashes or loses connectivity mid-job, the lease eventually expires and another runner in the pool picks up the job.
- **Deployments** are not redelivered. If a runner stops heartbeating for 10 minutes mid-deployment, the deployment is marked failed rather than handed to another runner.

Per-organization concurrency limits are enforced server-side: even with many runners available, deployments for a given organization will not exceed that organization's configured concurrency limit. Increasing the number of runners beyond that limit lets the pool absorb bursts and serve other workflow types (Insights scans, policy evaluations) in parallel, but it does not raise the deployment cap for a single organization.

Patterns for scaling:

- **Long-running runners**: Run multiple instances (for example, replicas of a Kubernetes Deployment, or several systemd units across hosts). Each replica adds one deployment slot, plus an Insights/policy slot if those workflow types are enabled on the pool.
- **Ephemeral runners**: Set `single_run: true` and use a Kubernetes `Job`/`CronJob` (or equivalent) to start a runner per job; the process exits after completing the job.
- **Specialized pools**: Use `enabled_workflow_types` to dedicate some runners to deployments and others to Insights scans or policy evaluations, so heavy deployments do not crowd out faster scan jobs.

{{% notes "info" %}}
If you are running the workflow runner inside a firewall ensure to allow outbound requests to api.pulumi.com. Ensure workflow runners have the cloud provider credentials to be able to deploy in your environments.
{{% /notes %}}

### Setting an organization default pool

You can designate one pool as the **organization default**. When a default pool is set, any deployment, Insights discovery scan, or policy evaluation that does not have an explicit workflow runner pool configured will use the default pool instead of the Pulumi Hosted Pool.

The resolution order for each workflow is:

1. The pool configured on the stack, account, or policy group.
1. The organization default pool (if set).
1. The Pulumi Hosted Pool.

To set a default:

1. In the left nav, open the **Settings** dropdown and select **Organization**, then choose the **Workflow Runner Pools** tab.
1. Open the row actions menu on the pool you want to designate and choose **Set as default**.

The **Pulumi Hosted Pool** row at the top of the list represents the built-in Pulumi-managed pool. Selecting **Set as default** on that row clears any customer-managed default, restoring the built-in pool as the fallback. If a custom default pool is deleted, the organization automatically reverts to the Pulumi Hosted Pool.

An explicit pool assigned to a stack, account, or policy group always takes precedence over the organization default.

### Leveraging OpenID authentication

It is possible to use OpenID authentication to fetch Pulumi Pool tokens dynamically instead of configuring a static token for the workflow runners. You must first register the OpenID provider as a trusted OIDC Issuer in your Pulumi account, as documented in the [OIDC Issuers documentation](/docs/administration/access-identity/oidc-issuers/).

When running workflow runners on a Kubernetes cluster, see the cluster-specific guides:

- [Configuring OpenID Connect for Amazon EKS](/docs/administration/access-identity/oidc-issuers/kubernetes-eks/)
- [Configuring OpenID Connect for Google Kubernetes Engine](/docs/administration/access-identity/oidc-issuers/kubernetes-gke/)

After registering the provider, the workflow runner requires this information:

- `organization_name`: your Pulumi Organization name
- `runner_pool_id`: the pool ID that the instance will connect to
- `token_expiration` (optional): the lifetime of tokens requested by the workflow runner (Go duration syntax, e.g. `1h`)
- `oidc_token_file`: the location of the file where the OIDC token will be recorded

The workflow runner will attempt to read the `oidc_token_file` for a fresh OIDC token and exchange it automatically for a Pulumi token every time the Pulumi token expires.

## Providing credentials and configuring runners

For the credentials your runners need to manage infrastructure, see [Runners](/docs/deployments/deployments/runners/#providing-credentials-to-workflow-runners). For the full set of configuration options for the `pulumi-workflow-agent.yaml` file, see the [configuration reference](/docs/deployments/deployments/runners/#configuration-reference).
