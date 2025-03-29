---
title: Customer-managed agents
title_tag: Get started with customer-managed agents
meta_desc: Customer-managed agents allows you to self-host deployment agents and get
  all the power and flexibility of Pulumi Deployments in your isolated environments
menu:
  cloud:
    name: Customer-managed agents
    parent: pulumi-cloud-deployments
    weight: 3
    identifier: pulumi-cloud-deployments-customer-managed-agents
search:
  keywords:
    - agents
    - deployment
    - customer-managed agents
    - deployment agents
---

Customer-Managed Agents allow you to self-host deployment agents bringing the same power and flexibility as Pulumi-hosted deployments. Self-hosting your agents comes with many benefits:

- **Host anywhere**: You can host the deployment agents anywhere to manage infrastructure, even within your fully private VPCs
- **Any hardware, any environment<sup>1</sup>**: Run the agents on any hardware of your choice and configure the environment that meets your needs
- **Mix & match**: You can use standard Pulumi-hosted deployments for your development stacks and use self-hosted Customer-Managed Agents for your private network infrastructure. You can mix and match to suit your unique needs
- **Multiple pools**: You can set up multiple deployment agent pools, assign stacks to specific pools, and scale agents dynamically to increase your deployment concurrency. Customers can have up to 150 concurrent deployments
- **Meet compliance**: You can configure the agents with the credentials needed to manage your infrastructure. This way your cloud provider credentials never leave your private network

<sup>1</sup> *Currently Linux and MacOS are supported*

Customer-Managed Agents support all the [deployment triggers](/docs/pulumi-cloud/deployments/#deployment-triggers) currently offered by Pulumi Deployments such as click to deploy, the Pulumi Deployments REST API, git push to deploy, Review Stacks, and remote Automation API.

{{% notes "info" %}}
Customer-Managed Agents is available on the Business Critical edition of Pulumi Cloud. [Contact sales](/contact/?form=sales) if you are interested and want to enable Customer-Managed Agents.
{{% /notes %}}

## Using Customer-Managed Agents

Before you begin, ensure you have installed the [Pulumi Github App](/docs/using-pulumi/continuous-delivery/github-app/) and updated the [source control settings](/docs/pulumi-cloud/deployments/get-started) of the stack you want to use Deployment agents. [Docker](https://docs.docker.com/engine/) or [Kubernetes](https://kubernetes.io/docs/home/) is a requirement for running the agent.

1. Go to **Deployment runners** under Organization Settings
2. Create a new pool. Ensure to copy and save the token
3. Install the agents as per the instructions on the page
4. Verify the agent status by refreshing the page
5. Configure a stack to use the agent by going to the Deploy tab within Stack Settings, and selecting the pool you created under the **Deployment Runner** pool drop-down
6. **(Optional)** Add more agents to the pool to increase concurrency by using the same token
7. Verify setup by doing a 'pulumi refresh' through the **Actions** drop-down in your stack page

![Pool Details view](../../../../blog/customer-managed-deployment-agents-launch/view-agent-status.png)

Agents poll Pulumi Cloud every 30 seconds to check for pending deployments and will disappear from the Pool details page 1-2 hours after being offline. On the deployments page, you can see all the deployments including pending deployments, and which deployment agents were used in a deployment.

{{% notes "info" %}}
If you are running the agent inside a firewall ensure to allow outbound requests to api.pulumi.com. Ensure agents have the cloud provider credentials to be able to deploy in your environments.
{{% /notes %}}

### Leveraging OpenID Authentication

It is possible to use OpenID authentication to fetch Pulumi Pool tokens dynamically instead of configuring a static token for the agents. You must first register the OpenID provider as a trusted OIDC issuer in your Pulumi account, as documented at [OIDC documentation](/docs/pulumi-cloud/oidc/client).

After registering the provider, this other information is required by the agent:

- `organization_name`: your Pulumi Organization name
- `runner_pool_id`: the pool ID that the instance will connect to
- `token_expiration` (optional): the expiration in seconds for the tokens requested by the agent
- `oidc_token_file`: the location of the file where the OIDC token will be recorded

The agent will attempt to read the `oidc_token_file` for a fresh OIDC token and exchange it automatically for a Pulumi token every time the Pulumi token expires.

## Providing Credentials to Agents

There are two methods to provide cloud provider credentials to the agents:

1. Use [OpenID Connect (OIDC) to generate credentials](/docs/pulumi-cloud/oidc)
2. Directly provide credentials to agents through environment variables configured in the host, or passing the environment variables when invoking the binary. Example:

   ```bash
   VARIABLE=value customer-managed-deployment-agent run
   ```

   You also need to update the `pulumi-deployment-agent.yaml` [configuration file](#configuration-reference) by setting `env_forward_allowlist`. `env_forward_allowlist` expects an array of strings. Example:

    ```yaml
    token: pul-d2d2….
    version: v0.0.5
    env_forward_allowlist:
        - key_one
        - key_two
        - key_three
    ```

## Configuration Reference

All configuration for customer-managed agents are done through the `pulumi-deployment-agent.yaml` file. This can be created manually or with the `customer-managed-deployment-agent configure` command.

The customer-managed agent will look for `pulumi-deployment-agent.yaml` in the following directories:

- Current directory
- Home directory
- `/etc`
- Location of the `customer-managed-deployment-agent` binary

\
Below are available configuration parameters and their default values. In most cases, only `token` is required.

```yaml
# pulumi-deployment-agent.yaml

## Required settings

# Pulumi token provided when creating a new deployment runner pool
# Environment variable override: PULUMI_AGENT_TOKEN
token: pul-xxx

## Optional settings

# Location of temp directory
# Uses the OS's preferred temporary file location (usually /tmp) by default
# Environment variable override: PULUMI_AGENT_SHARED_VOLUME_DIRECTORY
shared_volume_directory: ""

# The base path from which to load the runners
# This defaults to the location of the customer-managed-deployment-agent binary
# (usually ~/.pulumi/bin/customer-managed-deployment-agent)
# Environment variable override: PULUMI_AGENT_WORKING_DIRECTORY
working_directory: "<location of customer-managed-deployment-agent binary>"

# If using Self-Hosted Pulumi, set this to API domain of instance
# Environment variable override: PULUMI_AGENT_SERVICE_URL
service_url: "https://api.pulumi.com"

# If true, exit immediately after completing a single job
# Environment variable override: PULUMI_AGENT_SINGLE_RUN
single_run: false

# If true, always pull the Pulumi image from the Docker registry
# If false, use a local image
# Environment variable override: PULUMI_AGENT_PULL_IMAGE
pull_image: true

# If true, write errors to syslog instead of stderr
# Environment variable override: PULUMI_AGENT_SYSLOG
syslog: false

# Values for configuring OpenID Authentication
# Environment variable override: PULUMI_AGENT_ORGANIZATION_NAME
organization_name: ""
# Environment variable override: PULUMI_AGENT_RUNNER_POOL_ID
runner_pool_id: ""
# Environment variable override: PULUMI_AGENT_TOKEN_EXPIRATION
token_expiration: ""
# Environment variable override: PULUMI_AGENT_OIDC_TOKEN_FILE
oidc_token_file: ""

# List of environment variables to pass to the deployment agent
# Environment variable override: PULUMI_AGENT_ENV_FORWARD_ALLOWLIST
# Environment variable format is: PULUMI_AGENT_ENV_FORWARD_ALLOWLIST="VAR1 VAR2"
env_forward_allowlist: []

# Deployment target for the agent: docker (default) or kubernetes
# Environment variable override: PULUMI_AGENT_DEPLOY_TARGET
deploy_target: "docker"
```

### Kubernetes-Managed Agents

For Kubernetes-native installations, configuration for customer-managed agents is set on the Kubernetes Deployment that runs the agent. Configuration values may be set as environment variables, or by mounting a configuration file in the agent Pod.

The following Kubernetes-specific configuration options are available:

```yaml
# Kubernetes image pull policy https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy
PULUMI_AGENT_IMAGE_PULL_POLICY: IfNotPresent
```
