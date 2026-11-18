---
title: Integrations
title_tag: Integrations | Pulumi Agents
h1: Integrations
meta_desc: Connect Pulumi Agents to repositories, cloud providers, monitoring tools, and issue trackers.
aliases:
- /docs/ai/neo/integrations/
menu:
    ai:
        name: Integrations
        parent: ai-agents
        identifier: ai-agents-integrations
        weight: 70
integration_groups:
    repositories:
        - name: GitHub
          image: /logos/tech/github.svg
          link: /docs/integrations/version-control/github-app/
        - name: GitLab
          image: /logos/tech/gitlab.svg
          link: /docs/integrations/version-control/gitlab/
        - name: Bitbucket
          image: /logos/tech/bitbucket.svg
          link: /docs/integrations/version-control/bitbucket/
        - name: Azure DevOps
          image: /logos/tech/ci-cd/azure-devops.svg
          link: /docs/integrations/version-control/azure-devops-integration/
        - name: Other Git servers
          image: /logos/tech/git.svg
          link: /docs/integrations/version-control/custom-vcs/
    cloud:
        - name: Cloudflare
          image: /logos/agents/cloudflare.svg
          link: /docs/ai/integrations/external-mcp-servers/#cloudflare
        - name: AWS
          image: /logos/pkg/aws.svg
          link: /docs/ai/agents/integrations/aws/
        - name: Google Cloud
          image: /logos/tech/gcp-logo.svg
          link: /docs/ai/agents/integrations/google-cloud/
        - name: Azure
          image: /logos/tech/azure-logo.svg
          link: /docs/ai/agents/integrations/azure/
        - name: Kubernetes
          image: /logos/tech/kubernetes.svg
          link: /docs/ai/integrations/cli-integrations/#kubernetes
        - name: Supabase
          image: /logos/agents/supabase.svg
          link: /docs/ai/integrations/external-mcp-servers/#supabase
    tools:
        - name: Atlassian
          image: /logos/agents/atlassian.svg
          link: /docs/ai/integrations/external-mcp-servers/#atlassian-jira-and-confluence
        - name: Dash0
          image: /logos/agents/dash0.svg
          link: /docs/ai/integrations/external-mcp-servers/#dash0
        - name: Datadog
          image: /logos/agents/datadog.svg
          link: /docs/ai/agents/integrations/datadog/
        - name: Honeycomb
          image: /logos/agents/honeycomb.svg
          link: /docs/ai/integrations/external-mcp-servers/#honeycomb
        - name: Linear
          image: /logos/agents/linear.svg
          link: /docs/ai/integrations/external-mcp-servers/#linear
        - name: New Relic
          image: /logos/agents/newrelic.svg
          link: /docs/ai/integrations/external-mcp-servers/#new-relic
        - name: Sentry
          image: /logos/agents/sentry.svg
          link: /docs/ai/integrations/external-mcp-servers/#sentry
        - name: PagerDuty
          image: /logos/agents/pagerduty.svg
          link: /docs/ai/integrations/external-mcp-servers/#pagerduty

---

<script>
// Redirect anchors that belonged to the MCP content formerly on this page.
// The MCP integrations content moved to /docs/ai/integrations/external-mcp-servers/.
(function() {
  var mcpAnchors = ['what-you-can-do-with-mcp-integrations', 'enabling-an-mcp-integration', 'credential-storage', 'disabling-an-integration', 'how-integrations-work-at-task-time', 'per-task-control', 'if-an-integration-fails', 'configuration', 'atlassian-jira-and-confluence', 'datadog', 'honeycomb', 'linear', 'pagerduty', 'supabase'];
  var anchor = window.location.hash.replace(/^#/, '');
  if (anchor && mcpAnchors.indexOf(anchor) !== -1) {
    window.location.replace('/docs/ai/integrations/external-mcp-servers/#' + anchor);
  }
})();
</script>

Connect the tools an agent needs to do its work, such as a repository for code changes or Datadog for an investigation. See [Permissions](/docs/ai/agents/permissions/#design-access-around-the-job) to choose the access to grant.

Connections belong to your organization and can be used by more than one agent. Give each agent access to the connections it needs.

## Connect your tools

### Repositories

{{< integration-links "repositories" >}}

### Cloud accounts and Kubernetes

{{< integration-links "cloud" >}}

For AWS, Google Cloud, Azure, and Kubernetes, store the credential settings in [Pulumi ESC](/docs/esc/), then [connect the environment to a CLI tool](/docs/ai/integrations/cli-integrations/#setting-up-a-cli-integration).

### Monitoring and issue tracking

{{< integration-links "tools" >}}

## Give an agent access

After connecting a tool, [select it for the agent](/docs/ai/agents/configure/#select-integrations). Cloud CLI connections instead require [permission to open their ESC environments](/docs/ai/agents/permissions/#scope-pulumi-cloud-access). For Neo, see [CLI connection selection](/docs/ai/integrations/cli-integrations/#per-task-selection).

The connected credentials determine what the agent can do in that system. Selecting an integration does not narrow those credentials; [configure their permissions](/docs/ai/agents/permissions/#scope-credentials-for-connected-tools) for the agent's work.
