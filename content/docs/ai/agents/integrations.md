---
title: Integrations
title_tag: Integrations | Pulumi Agents
h1: Integrations
meta_desc: Connect Pulumi Agents to repositories, cloud providers, monitoring tools, and issue trackers.
menu:
    ai:
        name: Integrations
        parent: ai-home
        identifier: ai-agents-integrations
        weight: 40
integration_groups:
    repositories:
        - name: GitHub
          image: /logos/agents/github.svg
          link: /docs/integrations/version-control/github-app/
        - name: GitLab
          image: /logos/agents/gitlab.svg
          link: /docs/integrations/version-control/gitlab/
        - name: Bitbucket
          image: /logos/tech/bitbucket.svg
          link: /docs/integrations/version-control/bitbucket/
        - name: Azure DevOps
          image: /logos/agents/azuredevops.svg
          link: /docs/integrations/version-control/azure-devops-integration/
        - name: Other Git servers
          image: /logos/tech/git.svg
          link: /docs/integrations/version-control/custom-vcs/
    cloud:
        - name: AWS
          image: /logos/pkg/aws.svg
          link: /docs/ai/agents/integrations/aws/
        - name: Google Cloud
          image: /logos/agents/gcp.svg
          link: /docs/ai/agents/integrations/google-cloud/
        - name: Azure
          image: /logos/agents/azure.svg
          link: /docs/ai/agents/integrations/azure/
        - name: Kubernetes
          image: /logos/agents/kubernetes.svg
          link: /docs/ai/neo/integrations/cli/#kubernetes
        - name: Supabase
          image: /logos/agents/supabase.svg
          link: /docs/ai/neo/integrations/mcp/#supabase
    tools:
        - name: Atlassian
          image: /logos/agents/atlassian.svg
          link: /docs/ai/neo/integrations/mcp/#atlassian-jira-and-confluence
        - name: Dash0
          image: /logos/agents/dash0.svg
          link: /docs/ai/neo/integrations/mcp/#dash0
        - name: Datadog
          image: /logos/agents/datadog.svg
          link: /docs/ai/agents/integrations/datadog/
        - name: Honeycomb
          image: /logos/agents/honeycomb.svg
          link: /docs/ai/neo/integrations/mcp/#honeycomb
        - name: Linear
          image: /logos/agents/linear.svg
          link: /docs/ai/neo/integrations/mcp/#linear
        - name: New Relic
          image: /logos/agents/newrelic.svg
          link: /docs/ai/neo/integrations/mcp/#new-relic
        - name: PagerDuty
          image: /logos/agents/pagerduty.svg
          link: /docs/ai/neo/integrations/mcp/#pagerduty

---

Connect the tools an agent needs to do its work, such as a repository for code changes or Datadog for an investigation. Choose a tool below for setup instructions. See [Permissions](/docs/ai/agents/permissions/#design-access-around-the-job) to choose the access to grant.

Connections are shared across Neo and the agents you configure. Some setup guides are in the Neo documentation; those connection steps apply to both.

## Connect your tools

### Repositories

{{< integration-links "repositories" >}}

### Cloud accounts and Kubernetes

{{< integration-links "cloud" >}}

For AWS, Google Cloud, Azure, and Kubernetes, configure credentials in Pulumi ESC, then [connect the environment to a CLI tool](/docs/ai/neo/integrations/cli/#setting-up-a-cli-integration).

### Monitoring and issue tracking

{{< integration-links "tools" >}}

## Give an agent access

Select MCP integrations in the [agent's configuration](/docs/ai/agents/configure/#connect-the-tools-it-needs). Select CLI integrations, such as an AWS connection, in the task composer.

Give the agent only the permissions it needs for its work. Selecting an integration does not restrict its credentials. See [Permissions](/docs/ai/agents/permissions/) for how to scope access.

To work with an agent from Slack, see [Tasks and collaboration](/docs/ai/agents/tasks/). For automatic runs, see [Events and schedules](/docs/ai/agents/triggers/).
