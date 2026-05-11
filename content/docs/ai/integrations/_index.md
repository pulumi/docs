---
title: Integrations
title_tag: Neo Integrations
h1: Neo Integrations
meta_desc: Neo integrations connect the agent to MCP context sources, cloud CLIs, GitHub, and Slack.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: Integrations
        parent: ai-home
        weight: 55
        identifier: ai-integrations
---

<script>
(function() {
  var mcpAnchors = ['what-you-can-do-with-mcp-integrations', 'enabling-an-mcp-integration', 'credential-storage', 'disabling-an-integration', 'how-integrations-work-at-task-time', 'per-task-control', 'if-an-integration-fails', 'configuration', 'atlassian-jira-confluence', 'datadog', 'honeycomb', 'linear', 'pagerduty', 'supabase'];
  var anchor = window.location.hash.replace(/^#/, '');
  if (anchor && mcpAnchors.indexOf(anchor) !== -1) {
    window.location.replace('/docs/ai/integrations/mcp/#' + anchor);
  }
})();
</script>

Neo on its own knows about your infrastructure footprint: your code, your stacks, your state. Most of what your team actually does happens elsewhere, in the systems you use to plan, communicate, and operate. Integrations bridge that gap in two ways: by connecting Neo to those external systems, and by letting you reach Neo from where you already work.

[MCP integrations](/docs/ai/integrations/mcp/) and [CLI integrations](/docs/ai/integrations/cli/) handle the first part. MCP brings context in from issue trackers, observability platforms, runbook wikis, and on-call tools. CLI integrations cover what MCP doesn't reach, calling out to cloud-provider CLIs against credentials managed in [Pulumi ESC](/docs/esc/). [GitHub](/docs/ai/integrations/github/) and [Slack](/docs/ai/integrations/slack/) handle the second: mention Neo from a PR thread or a Slack channel to start a task without switching to the Pulumi Cloud console.

All integrations are configured at the organization level by an administrator. Once enabled, they're available to every Neo task in the organization.
