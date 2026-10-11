---
title: Customer-managed runners
title_tag: Customer-managed runners | Pulumi Cloud
meta_desc: Run Pulumi Deployments, Discovery scans, and audit policy evaluations on runners you host in your own infrastructure.
menu:
  administration:
    name: Customer-managed runners
    parent: administration-concepts
    identifier: administration-concepts-customer-managed-runners
    weight: 11
aliases:
- /docs/deployments/concepts/customer-managed-runners/
- /docs/deployments/concepts/runners/
- /docs/deployments/deployments/runners/
- /docs/pulumi-cloud/deployments/customer-managed-agents/
- /docs/deployments/deployments/customer-managed-agents/
- /docs/deployments/deployments/runs/customer-managed-agents/
- /docs/deployments/deployments/runs/
pulumi_cloud_feature: customer-managed-runners
---
Customer-managed runners let you run [Pulumi Deployments](/docs/deployments/), [Discovery](/docs/discovery-governance/concepts/discovery/) scans, and audit [policy evaluations](/docs/discovery-governance/concepts/policy-as-code/) on runners you host in your own infrastructure. By default, this work runs on [Pulumi-managed runners](/docs/deployments/concepts/pulumi-managed-runners/). You group your runners into one or more runner pools, then choose which pool each stack, cloud account, or policy group uses.

Common reasons to use customer-managed runners:

- **Private network access**: Runners can live inside fully private VPCs and reach resources that aren't accessible from the public internet.
- **Credentials and data stay in your network**: Cloud provider credentials, scan data, and policy evaluation results are processed on hardware you control.
- **Your own environment**: Run on hardware of your choice and configure the runner image and environment you need. Linux and macOS are supported.
- **Mix and match**: Keep using Pulumi-managed runners for some work, such as development stacks, while routing private-network work to your own pools.
- **Scale on your terms**: Create multiple pools and add runners to a pool to increase concurrency, up to 150 concurrent workflows per organization.

To create, scale, and assign a runner pool, see the [customer-managed runners setup guide](/docs/administration/guides/customer-managed-runners/). The rest of this page explains what runs on customer-managed runners, how each kind of work picks a pool, the execution model, how to supply cloud credentials, and the full configuration reference.

## What runs on customer-managed runners

A runner can run three workflow types. All three are enabled by default, and the [`enabled_workflow_types`](#configuration-reference) setting lets you dedicate a runner to a subset.

| Workflow type | `enabled_workflow_types` value | What it covers |
|---|---|---|
| Deployments | `deployment` | Every Pulumi Deployments operation on a stack, from any [deployment trigger](/docs/deployments/concepts/triggers/): on-demand runs from the console or REST API, git push to deploy, [review stacks](/docs/deployments/concepts/review-stacks/), remote Automation API, scheduled [drift detection and remediation](/docs/deployments/concepts/drift/), and [time-to-live stacks](/docs/deployments/concepts/ttl/). |
| Discovery scans | `insights_scan` | On-demand and scheduled [scans of a cloud account](/docs/discovery-governance/concepts/discovery/cloud-accounts/). |
| Policy evaluations | `policy_evaluation` | Evaluations run by [audit policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/). Preventative policy groups run inside `pulumi up` and `pulumi preview` wherever the CLI runs, so they don't use a runner pool. |

## How work chooses a runner pool

Each kind of work resolves its pool independently. If nothing more specific is set, it falls back to the organization's [default runner pool](/docs/administration/guides/customer-managed-runners/#setting-an-organization-default-pool), and then to the Pulumi hosted pool.

- **Deployments**: the pool set in the stack's **Settings** > **Deploy** page (the **Deployment runner pool** dropdown), then the organization default, then the Pulumi hosted pool. See [Runner pools](/docs/deployments/concepts/settings/runner-pools/).
- **Discovery scans**: the cloud account's pool, then the organization default, then the Pulumi hosted pool. A scan started through the [REST API](/docs/reference/cloud-rest-api/) can name a different pool for that one scan. See [Run scans and policy evaluations on customer-managed runners](/docs/discovery-governance/operations/customer-managed-runners/).
- **Policy evaluations**: the audit policy group's pool, then the organization default, then the Pulumi hosted pool.

Self-hosted Pulumi Cloud installations have no Pulumi hosted pool, so all of this work must run on a customer-managed runner pool.

## Not supported on customer-managed runners

The following features run only on Pulumi-managed runners:

- **[Dependency caching](/docs/deployments/concepts/settings/dependency-caching/)**: if a stack is assigned to a customer-managed pool, the setting has no effect. Because you control the runner environment and image, you can manage caching yourself, for example by persisting package manager caches and the Pulumi plugin directory (`~/.pulumi/plugins`) across jobs, or by pre-baking them into your runner image.
- **[Terraform remote execution](/docs/integrations/terraform/remote-execution/)**: Terraform runs can't be assigned to a customer-managed pool.
- **Terraform module conversion** in Pulumi Cloud.
- **[Pulumi Neo](/docs/ai/) tasks**.

## Terminology

The same concept appears under a few names across Pulumi tools:

- The CLI, REST API, and [RBAC scopes](/docs/administration/reference/rbac-scopes/) call a runner pool an **agent pool** (for example, the `agent_pool:*` scopes and agent pool access tokens).
- The runner binary is `customer-managed-workflow-agent`, and its configuration file is `pulumi-workflow-agent.yaml`.
- The Pulumi Cloud console lists pools under **Workflow runner pools** in organization settings, and labels a stack's pool setting **Deployment runner pool**.

## Execution model

A workflow runner is a long-lived agent process. It polls Pulumi Cloud for pending work, claims one job at a time through an exclusive claim, launches an isolated runner environment to execute that job, streams the results back to Pulumi Cloud, and then discards the per-job environment. The agent itself keeps running and polls for the next job.

The [`deploy_target`](#configuration-reference) setting controls *how* the agent creates that per-job environment. It has three values — `docker`, `kubernetes`, and `ecs` — and the choice determines the isolation model, the prerequisites, and how you scale.

```mermaid
sequenceDiagram
    participant Agent as Runner agent
    participant Cloud as Pulumi Cloud
    participant Env as Per-job container, Pod, or ECS task

    loop Until a job is available
        Agent->>Cloud: Poll for pending work
    end
    Cloud-->>Agent: Job claimed exclusively by this agent
    Agent->>Env: Launch isolated runner environment
    activate Env
    Env->>Cloud: Execute the job and stream results
    Agent->>Cloud: Check job status (detects cancellation)
    Env-->>Agent: Job finished
    deactivate Env
    Agent->>Env: Discard the environment
    Note over Agent: Keeps running and polls for the next job
```

### Docker

With `deploy_target: docker` (the default), the agent connects to the local Docker socket and launches a **separate runner container for each job**. Because a runner container runs Pulumi operations that may themselves build images or start containers, this pattern is often referred to informally as **Docker-in-Docker (DinD)**. Mechanically, though, the agent starts a runner container through the Docker socket rather than nesting a Docker daemon.

Docker-specific behavior:

- **`pull_image`** — when `true` (the default), the agent pulls the workflow image from the registry for each job; when `false`, it uses a locally cached image.
- **`env_forward_allowlist`** — host environment variables named here are forwarded into the runner container, which is how you pass cloud provider credentials or other host-defined secrets into a job. `DOCKER_HOST` is always forwarded.
- **`shared_volume_directory`** — the host directory used to create the temporary directories that are mounted into the runner container. Leave it empty to use the operating system's default temporary location.

This mode requires only a Docker daemon on the host, which makes it the simplest way to run an agent on a single VM or bare-metal host.

### Kubernetes

With `deploy_target: kubernetes`, the agent uses the in-cluster Kubernetes API to launch a **runner Pod for each job**, so every job gets Pod-level isolation and is scheduled by Kubernetes across your cluster. In this mode the agent runs as a Kubernetes Deployment, and its configuration is supplied as environment variables on that Deployment or through a configuration file mounted into the agent Pod. Each runner Pod copies the runner binary from the [agent image](#agent-image), and the Kubernetes-specific [`PULUMI_AGENT_IMAGE_PULL_POLICY`](#kubernetes-managed-runners) controls that image's pull policy.

This mode fits environments that already run Kubernetes and want the cluster to handle scheduling and resource limits. It also enables ephemeral, per-job runners: set [`single_run: true`](#configuration-reference) so the agent exits after one job, and drive it with a Kubernetes `Job` or `CronJob` so a fresh agent starts for each job.

### Amazon ECS

{{% notes type="info" %}}
The `ecs` deploy target requires `customer-managed-workflow-agent` v2.3.0 or later.
{{% /notes %}}

With `deploy_target: ecs`, the agent calls the Amazon ECS API to run each job as a **one-off ECS task**. By default, tasks run on AWS Fargate, which gives every job its own microVM. The agent itself can run anywhere with AWS credentials and network access to Pulumi Cloud, such as an ECS service, an EC2 instance, or a host outside AWS. ECS settings go in the [`ecs`](#configuration-reference) block of the agent configuration:

```yaml
deploy_target: ecs
ecs:
  cluster: workflow-jobs
  subnets: [subnet-0123, subnet-4567]
  security_groups: [sg-0123]
  task_definition_template_file: /etc/pulumi/worker-task-definition.json
```

The agent's AWS credentials need these permissions:

- `ecs:RegisterTaskDefinition`, `ecs:DescribeTaskDefinition`, and `ecs:TagResource`
- `ecs:RunTask`, `ecs:DescribeTasks`, and `ecs:StopTask`
- `ecs:DescribeClusters`, which the agent calls at startup to check that the cluster exists
- `iam:PassRole` on the roles in the task definition template

#### Task definition template

`task_definition_template_file` points to a base task definition, in the shape that `aws ecs register-task-definition --cli-input-json` accepts (not a `describe-task-definition` response). Use it to set:

- The **execution role**, which pulls the job image and ships container logs.
- The **task role**, which gives the job its AWS credentials.
- Task `cpu` and `memory`. On Fargate, the default is 1 vCPU and 4 GiB.
- `runtimePlatform`, and any sidecar containers.

`networkMode` must be `awsvpc` (the default), whichever launch type you use. To configure the job's own container, for example its log configuration, include a container named `pulumi-workflow`; the agent sets that container's image, entry point, command, and runner mount. Other container and volume names that start with `pulumi-workflow-` are reserved for the agent.

Without a template, jobs run with no execution or task role. The job image must then be public, nothing ships the containers' logs, and the job gets AWS credentials only from its own configuration, such as [ESC](#deployments) or OIDC.

#### How an ECS task runs a job

Each task starts with a short-lived `pulumi-workflow-prepare` container from the [agent image](#agent-image), which the execution role must be able to pull. It fetches the job from Pulumi Cloud and copies the runner binary into a volume shared with the job's container, then exits. The job's container then runs the job. The prepare container ships its logs with the `pulumi-workflow` container's log configuration.

The job's credentials reach the task as environment overrides on the `RunTask` call. CloudTrail masks those values, but any principal allowed to call `ecs:DescribeTasks` on the cluster can read them while the job runs. Each task is tagged `pulumi-workflow/id` with its job's ID, and inherits the tags of its task definition. When a job is canceled, the agent stops its task.

The agent registers one task definition for each distinct combination of template, job image, and agent image, and reuses it for later jobs. Family names are content hashes, so each task definition is tagged `pulumi-workflow/managed-by=workflow-runner`, plus `pulumi-workflow/job-image` and `pulumi-workflow/agent-image` with the images it runs. Task definitions the agent no longer uses stay `ACTIVE` until you deregister them. If a later job needs a deregistered one, the agent registers it again.

ECS limitations:

- **Image pulls**: Fargate pulls the job image for every job; there is no image cache between tasks.
- **Registry credentials**: the execution role must be able to pull the job image. Registry credentials set on the job aren't supported.
- **No Docker daemon**: Fargate doesn't provide one, so jobs that build container images need a rootless builder or an external build service.

### Agent image

The `kubernetes` and `ecs` deploy targets copy the runner binary into each job from the agent's container image, `pulumi/customer-managed-workflow-agent`. By default, the agent uses its own release of that image, for example `pulumi/customer-managed-workflow-agent:v2.3.0` for agent v2.3.0. Agents before v2.3.0 default to the `latest` tag. To use a mirror, for example in a private registry or an AWS GovCloud (US) ECR repository, set the `PULUMI_AGENT_IMAGE` environment variable on the agent to your mirror of the same release. The agent and the runner binary in the image hand each job off between them, so the image must match the agent's release.

### One job per runner

Regardless of the deploy target, each agent process runs **one deployment at a time** — plus, optionally, one Discovery scan or policy evaluation in parallel — and has no internal worker pool to configure. To run more jobs concurrently, add more agents to the pool rather than trying to scale a single agent. For the full set of scaling patterns, per-organization concurrency limits, and crash-recovery behavior, see [Scaling and concurrency](/docs/administration/guides/customer-managed-runners/#scaling-and-concurrency) in the setup guide.

### Choosing a deploy target

| | Docker (`deploy_target: docker`) | Kubernetes (`deploy_target: kubernetes`) | Amazon ECS (`deploy_target: ecs`) |
|---|---|---|---|
| **Prerequisite** | A Docker daemon on the host | A Kubernetes cluster | An ECS cluster, and AWS credentials for the agent |
| **Per-job unit** | A runner container launched via the Docker socket | A runner Pod launched via the in-cluster API | An ECS task launched via the ECS API |
| **Isolation** | Container-level, sharing the host Docker daemon | Pod-level, scheduled and isolated by the cluster | A microVM per job on Fargate |
| **Scaling** | Run more agent processes (for example, more hosts or systemd units) | Run more agent replicas, or use `single_run` with a `Job`/`CronJob` for ephemeral per-job runners | Run more agent processes |
| **Best fit** | A single VM or host where you want the simplest setup | An existing Kubernetes environment that should schedule and bound runner resources | AWS environments that need per-job isolation without managing hosts or a cluster |

## Providing cloud credentials to runners

Where a job gets its cloud provider credentials depends on its workflow type.

### Deployments

Deployments support three ways to supply credentials:

1. **[Pulumi ESC](/docs/esc/)** (recommended): import an ESC environment into the stack's [environment](/docs/esc/guides/pulumi-iac/), and the Pulumi CLI opens it on the runner during the deployment. ESC environments can issue short-lived credentials themselves, for example with the [`aws-login`](/docs/esc/providers/login/aws-login/) provider.
1. **[Pulumi Deployments OIDC](/docs/deployments/guides/oidc/)**: if your runners can't reach Pulumi Cloud to use ESC, configure OIDC in the stack's deployment settings. Pulumi Cloud issues an OIDC token for each deployment, and the runner exchanges it with your cloud provider before the Pulumi program runs. The runner needs outbound access to the cloud provider's token endpoint, such as AWS STS, and the cloud provider must trust the Pulumi OIDC issuer, just as with Pulumi-managed runners.
1. **Host environment variables**: forward credentials that already exist on the runner host into each job with [`env_forward_allowlist`](#forwarding-host-environment-variables).

For a comparison of ESC and Deployments OIDC, see [Supplying cloud credentials to Pulumi Deployments](/docs/deployments/guides/cloud-credentials/).

### Discovery scans

Discovery scans get their credentials from the ESC environment attached to the [cloud account](/docs/discovery-governance/concepts/discovery/cloud-accounts/#configure-esc-credentials). The scanner opens that environment on your runner and exports its values into the scan, replacing any forwarded host variable with the same name. Deployments OIDC doesn't apply to scans.

The runner needs network access to Pulumi Cloud, which it already has in order to poll for work, and to the cloud provider APIs being scanned.

### Policy evaluations

Policy evaluations don't call cloud provider APIs. They read stack state and discovered resources from Pulumi Cloud, so they need no cloud credentials. If a policy pack needs configuration or secrets, [attach an ESC environment](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#esc-environments) to it. The runner opens that environment and passes its `environmentVariables` and `policyConfig` to the policy pack.

### Forwarding host environment variables

The `env_forward_allowlist` setting forwards named environment variables from the runner host into every job, whatever its workflow type. To use it, set the variables on the host, or pass them when you start the runner:

```bash
VARIABLE=value customer-managed-workflow-agent run
```

Then list the variable names in `pulumi-workflow-agent.yaml`:

```yaml
token: pul-d2d2….
version: v0.0.5
env_forward_allowlist:
    - key_one
    - key_two
    - key_three
```

Don't forward variables that Pulumi sets for each job, such as `PULUMI_ACCESS_TOKEN`. A forwarded variable can replace the value Pulumi provides.

## Configuration reference

You configure customer-managed runners with the `pulumi-workflow-agent.yaml` file, which you can create manually or with the `customer-managed-workflow-agent configure` command, or with `PULUMI_AGENT_` environment variables (see below).

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

# Where workflow jobs are executed. One of: docker, kubernetes, ecs.
# - docker: the agent launches runner containers via the local Docker socket.
# - kubernetes: the agent launches runner Pods via the in-cluster Kubernetes API.
# - ecs: the agent runs each job as an Amazon ECS task (agent v2.3.0 and later).
#   Configure it in the ecs settings below.
# See the "Execution model" section above for how each target runs a job.
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

## Amazon ECS settings
## Used only when deploy_target is ecs. See the "Amazon ECS" section above.
ecs:
  # ECS cluster to run job tasks in. Required.
  # Environment variable override: PULUMI_AGENT_ECS_CLUSTER
  cluster: ""

  # Subnets for each task's awsvpc network interface. Required.
  # Environment variable override: PULUMI_AGENT_ECS_SUBNETS
  # Environment variable format is space-separated:
  #   PULUMI_AGENT_ECS_SUBNETS="subnet-0123 subnet-4567"
  subnets: []

  # Security groups for each task's network interface. If empty, ECS uses the
  # VPC's default security group.
  # Environment variable override: PULUMI_AGENT_ECS_SECURITY_GROUPS
  # Environment variable format is space-separated:
  #   PULUMI_AGENT_ECS_SECURITY_GROUPS="sg-0123 sg-4567"
  security_groups: []

  # ECS launch type for job tasks: FARGATE or EC2. EC2 tasks share their
  # container instance with other tasks, so they don't get a microVM per job.
  # Environment variable override: PULUMI_AGENT_ECS_LAUNCH_TYPE
  launch_type: "FARGATE"

  # If true, give each task a public IP address. Tasks in private subnets need
  # a NAT gateway or VPC endpoints instead, to reach Pulumi Cloud and pull images.
  # Environment variable override: PULUMI_AGENT_ECS_ASSIGN_PUBLIC_IP
  assign_public_ip: false

  # Path to a base task definition for job tasks, in the shape that
  # `aws ecs register-task-definition --cli-input-json` accepts. If empty, jobs
  # run with no execution or task role.
  # Environment variable override: PULUMI_AGENT_ECS_TASK_DEFINITION_TEMPLATE_FILE
  task_definition_template_file: ""

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

### Kubernetes-managed runners

For Kubernetes-native installations, configuration for customer-managed runners is set on the Kubernetes Deployment that runs the workflow runner. Configuration values may be set as environment variables, or by mounting a configuration file in the workflow runner Pod.

The following Kubernetes-specific configuration options are available:

```yaml
# Kubernetes image pull policy https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy
PULUMI_AGENT_IMAGE_PULL_POLICY: IfNotPresent
```

The `kubernetes` and `ecs` deploy targets also read `PULUMI_AGENT_IMAGE`, the image that each job copies the runner binary from. It defaults to the agent's own release; set it only to use a mirror of that release. See [Agent image](#agent-image).
