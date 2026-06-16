---
title: Customer-managed workflow runners
title_tag: Get started with customer-managed workflow runners
meta_desc: Self-host workflow runners and get all the power and flexibility of Pulumi Deployments in your isolated environments.
menu:
  deployments:
    name: Customer-managed workflow runners
    parent: deployments-deployments-runs
    weight: 20
    identifier: deployments-deployments-runs-customer-managed-agents

aliases:
- /docs/pulumi-cloud/deployments/customer-managed-agents/
- /docs/deployments/deployments/customer-managed-agents/
---

Customer-Managed Workflow Runners allow you to self-host workflow runners, bringing the same power and flexibility as Pulumi-hosted workflows. Self-hosting your workflow runners comes with many benefits for deployments, [Insights](/docs/insights/) discovery scans, and [policy evaluations](/docs/insights/policy/):

- **Host anywhere**: You can host the workflow runners anywhere to manage infrastructure, even within your fully private VPCs
- **Any hardware, any environment<sup>1</sup>**: Run the workflow runners on any hardware of your choice and configure the environment that meets your needs
- **Mix & match**: You can use standard Pulumi-hosted workflows for your development stacks and use self-hosted Customer-Managed Workflow Runners for your private network infrastructure. You can mix and match to suit your unique needs
- **Multiple pools**: You can set up multiple workflow runner pools, assign stacks to specific pools, and scale workflow runners dynamically to increase your workflow concurrency. Customers can have up to 150 concurrent workflows
- **Meet compliance**: You can configure the workflow runners with the credentials needed to manage your infrastructure. This way your cloud provider credentials never leave your private network

<sup>1</sup> *Currently Linux and macOS are supported*

Customer-Managed Workflow Runners support all the [deployment triggers](/docs/deployments/deployments/#deployment-triggers) currently offered by Pulumi Deployments such as click to deploy, the Pulumi Deployments REST API, git push to deploy, Review Stacks, and remote Automation API. They also support running Insights discovery scans and policy evaluations.

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
   - **Deployments**: Go to **Stack Settings** > **Deploy** tab and select the pool under the **Deployment Runner** pool dropdown
   - **Insights discovery scans**: Go to **Management** > **Accounts** and select the pool for the account you want to scan
   - **Policy evaluation**: Go to **Management** > **Policies** > **Policy Groups** and select the pool for an audit policy group
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

## Providing credentials to workflow runners

{{% notes type="info" %}}
For most users, Pulumi recommends [Pulumi ESC](/docs/esc/) for supplying cloud credentials to Deployments. However, if your customer-managed agents can't reach Pulumi Cloud over the network to use ESC, [Pulumi Deployments OIDC](/docs/deployments/deployments/oidc/) is an appropriate solution. For a comparison, see [Supplying Cloud Credentials to Pulumi Deployments](/docs/deployments/deployments/cloud-credentials/).
{{% /notes %}}

There are two methods to provide cloud provider credentials to the workflow runners:

1. Use [OpenID Connect (OIDC) to generate credentials](/docs/deployments/deployments/oidc/)
2. Directly provide credentials to workflow runners through environment variables configured in the host, or passing the environment variables when invoking the binary. Example:

   ```bash
   VARIABLE=value customer-managed-workflow-agent run
   ```

   You also need to update the `pulumi-workflow-agent.yaml` [configuration file](#configuration-reference) by setting `env_forward_allowlist`. `env_forward_allowlist` expects an array of strings. Example:

    ```yaml
    token: pul-d2d2….
    version: v0.0.5
    env_forward_allowlist:
        - key_one
        - key_two
        - key_three
    ```

## Configuration reference

All configuration for customer-managed workflow runners is done through the `pulumi-workflow-agent.yaml` file. This can be created manually or with the `customer-managed-workflow-agent configure` command.

The workflow runner will look for `pulumi-workflow-agent.yaml` in the following directories:

- Current directory
- Home directory
- `/etc`
- Location of the `customer-managed-workflow-agent` binary

Below are the available configuration parameters and their default values. In most cases, only `token` is required.

Any setting can also be provided as an environment variable using the `PULUMI_AGENT_` prefix and the upper-cased key name (for example, `token` → `PULUMI_AGENT_TOKEN`, `polling_interval` → `PULUMI_AGENT_POLLING_INTERVAL`). Environment variables take precedence over values in the configuration file.

Duration values use Go duration syntax: a sequence of decimal numbers each with an optional fraction and a unit suffix, such as `300ms`, `30s`, `1m`, or `1h30m`. Valid units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, and `h`.

```yaml
# pulumi-workflow-agent.yaml

## Required settings

# Pulumi token provided when creating a new workflow runner pool.
# Required unless using OIDC.
# Environment variable override: PULUMI_AGENT_TOKEN
token: pul-xxx

## Optional settings

# If using Self-Hosted Pulumi, set this to the API domain of your instance.
# Trailing slashes are stripped automatically.
# Environment variable override: PULUMI_AGENT_SERVICE_URL
service_url: "https://api.pulumi.com"

# The base path from which to load the runner binaries (workflow-runner and,
# for Docker, workflow-runner-embeddable). Defaults to the directory of the
# customer-managed-workflow-agent binary (usually ~/.pulumi/bin/).
# Environment variable override: PULUMI_AGENT_WORKING_DIRECTORY
working_directory: "<location of customer-managed-workflow-agent binary>"

# Host directory used to create temporary directories that are mounted into
# the runner container. Leave empty to use the OS default temporary location.
# Environment variable override: PULUMI_AGENT_SHARED_VOLUME_DIRECTORY
shared_volume_directory: ""

# Where workflow jobs are executed. One of: docker, kubernetes.
# - docker: the agent launches runner containers via the local Docker socket.
# - kubernetes: the agent launches runner Pods via the in-cluster Kubernetes API.
# Environment variable override: PULUMI_AGENT_DEPLOY_TARGET
deploy_target: "docker"

# If true, the runner exits after completing a single workflow job.
# Useful for ephemeral, one-shot runners (for example, Kubernetes Jobs).
# Environment variable override: PULUMI_AGENT_SINGLE_RUN
single_run: false

# If true, the runner pulls the workflow image from the registry on each
# job. If false, it uses a locally cached image. (Docker target only.)
# Environment variable override: PULUMI_AGENT_PULL_IMAGE
pull_image: true

# Workflow types this runner is allowed to claim. All types are enabled by
# default. Set this to dedicate runners to specific kinds of work.
# Valid values: deployment, insights_scan, policy_evaluation.
# Environment variable override: PULUMI_AGENT_ENABLED_WORKFLOW_TYPES
# Environment variable format is comma-separated:
#   PULUMI_AGENT_ENABLED_WORKFLOW_TYPES="deployment,insights_scan,policy_evaluation"
enabled_workflow_types:
    - deployment
    - insights_scan
    - policy_evaluation

# Host environment variables that are forwarded into runner containers.
# Use this to pass cloud provider credentials or other secrets defined on the
# host into workflow jobs. DOCKER_HOST is always forwarded.
# Environment variable override: PULUMI_AGENT_ENV_FORWARD_ALLOWLIST
# Environment variable format is space-separated:
#   PULUMI_AGENT_ENV_FORWARD_ALLOWLIST="VAR1 VAR2"
env_forward_allowlist: []

## OpenID Connect (OIDC) settings
## See the "Leveraging OpenID authentication" section. When oidc_token_file is set,
## `organization_name` and `runner_pool_id` are required, and `token` is not used.

# Path to a file containing an OIDC token that will be exchanged for a
# Pulumi token. The file is re-read whenever the Pulumi token expires.
# Environment variable override: PULUMI_AGENT_OIDC_TOKEN_FILE
oidc_token_file: ""

# Pulumi organization name. Required when using OIDC.
# Environment variable override: PULUMI_AGENT_ORGANIZATION_NAME
organization_name: ""

# Pool ID this runner will connect to. Required when using OIDC.
# (Without OIDC, the pool is inferred from the token.)
# Environment variable override: PULUMI_AGENT_RUNNER_POOL_ID
runner_pool_id: ""

# Requested lifetime for tokens issued via the OIDC exchange (duration).
# Environment variable override: PULUMI_AGENT_TOKEN_EXPIRATION
token_expiration: ""

## Polling and retry settings

# Default polling interval for checking for new workflow jobs. The server
# may return a Retry-After hint that supersedes this value (see
# polling_interval_override).
# Environment variable override: PULUMI_AGENT_POLLING_INTERVAL
polling_interval: "1m"

# If true, ignore any Retry-After header from the server and always use
# polling_interval instead.
# Environment variable override: PULUMI_AGENT_POLLING_INTERVAL_OVERRIDE
polling_interval_override: false

# How often the runner checks the status of an in-progress job (used to
# detect cancellations).
# Environment variable override: PULUMI_AGENT_JOB_STATUS_LOOP_INTERVAL
job_status_loop_interval: "30s"

# Per-call timeout for API requests to Pulumi Cloud.
# Environment variable override: PULUMI_AGENT_REQUEST_TIMEOUT
request_timeout: "30s"

# Maximum number of retries for rate-limited or transient API failures.
# Environment variable override: PULUMI_AGENT_REQUEST_RETRY_COUNT
request_retry_count: 2

# Initial backoff between retries.
# Environment variable override: PULUMI_AGENT_REQUEST_RETRY_WAIT
request_retry_wait: "20s"

# Cap on the backoff between retries.
# Environment variable override: PULUMI_AGENT_REQUEST_RETRY_MAX_WAIT
request_retry_max_wait: "2m"

# Number of consecutive API failures before the circuit breaker trips and
# polling pauses. Each failure already includes its own retries, so the
# effective number of failed requests is higher than this value.
# Environment variable override: PULUMI_AGENT_CIRCUIT_BREAKER_FAILURES
circuit_breaker_failures: 2

# How long the circuit breaker stays open after tripping.
# Environment variable override: PULUMI_AGENT_CIRCUIT_BREAKER_TIMEOUT
circuit_breaker_timeout: "10m"

## Health and observability

# Port for the runner's local HTTP server, which exposes a health check
# endpoint.
# Environment variable override: PULUMI_AGENT_HTTP_SERVER_PORT
http_server_port: 8080

# Maximum time the runner can go without making progress before the health
# endpoint reports unhealthy. If unset (the default), the threshold is
# automatically derived as twice the longer of polling_interval and
# job_status_loop_interval.
# Environment variable override: PULUMI_AGENT_HEALTH_THRESHOLD
health_threshold: ""

# If true, write log output to syslog instead of stderr.
# Environment variable override: PULUMI_AGENT_SYSLOG
syslog: false
```

### Kubernetes-managed workflow runners

For Kubernetes-native installations, configuration for customer-managed workflow runners is set on the Kubernetes Deployment that runs the workflow runner. Configuration values may be set as environment variables, or by mounting a configuration file in the workflow runner Pod.

The following Kubernetes-specific configuration options are available:

```yaml
# Kubernetes image pull policy https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy
PULUMI_AGENT_IMAGE_PULL_POLICY: IfNotPresent
```
