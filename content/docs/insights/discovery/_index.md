---
title: Discovery
title_tag: "Pulumi Insights Discovery Overview"
meta_desc: Discover and manage all your cloud infrastructure with Pulumi Insights Discovery—scan accounts, explore resources, and gain complete visibility.
h1: Discovery
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: insights-home
    identifier: insights-discovery
    weight: 5
aliases:
- /docs/intro/insights/
- /docs/pulumi-cloud/insights/
- /docs/insights/concepts/
- /docs/insights/concepts/how-insights-works/
---

Pulumi Insights Discovery enables organizations to gain complete visibility into their cloud infrastructure by scanning cloud provider accounts and building a comprehensive inventory of all resources—regardless of how those resources were created or are currently managed.

## How discovery works

Discovery integrates with [Pulumi ESC](/docs/esc/) to securely manage credentials and scan your cloud infrastructure. The process involves:

1. **Account management**: Create and configure accounts through the [Accounts page](/docs/insights/discovery/accounts/) in Pulumi Cloud, where you can view scan status, monitor progress, and manage settings.

2. **Resource scanning**: Discovery authenticates to your cloud provider using read-only credentials from ESC, then identifies resources, collects metadata, records relationships, and updates the Insights supergraph with the latest state.

3. **Exploration**: Once scanning completes, explore your infrastructure through [Resource Search](/docs/insights/discovery/search/), which provides powerful filtering, grouping, and natural language queries via [Pulumi Copilot](/docs/ai/copilot/).

4. **Import**: Use [Visual Import](/docs/insights/discovery/visual-import/) to convert discovered resources into Pulumi IaC code, bringing unmanaged infrastructure under automated management.

### Account hierarchies

Discovery automatically creates child accounts when applicable. For AWS, each selected region becomes a child account under the main parent account, making it easy to manage resources across regions. Actions performed on parent accounts (like scanning or deletion) cascade to all children, while individual child accounts can be managed independently.

## Key capabilities

### Resource search and exploration

The Resource Search interface provides:

- **Advanced search**: Query resources by name, type, stack, project, properties, and more using a rich query syntax
- **Filtering and grouping**: Organize resources by dragging column headers to create custom views
- **Column customization**: Show or hide information to focus on what matters
- **Favorites**: Save and share custom views with your team
- **AI assist**: Use natural language queries to find resources (e.g., "How many VPCs do I have?")

Resources are displayed in a paginated table showing up to 10,000 results. For larger datasets, use the [Data Export](/docs/insights/discovery/data-export/) feature or the [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api#resource-search).

### Resource relationships

Discovery maintains a graph of relationships between resources, tracking connections like S3 buckets and their bucket policies, virtual machines and attached storage, or network interfaces and security groups. These relationships are visible in the Resource Explorer and help you understand infrastructure dependencies.

### Unified resources

When a resource exists in multiple sources (IaC stacks and Discovery scans), Pulumi Cloud consolidates them in search results, indicated by a spoke icon. This reduces duplicate entries while ensuring all sources matching your query are considered.

### Managed by attribute

The **Managed By** column categorizes resources as either:

- **Pulumi**: Resources provisioned and tracked through Pulumi stacks
- **Other**: Resources detected by Discovery but not managed by any Pulumi stack

This helps identify which infrastructure is under IaC management and which could benefit from being imported.

## Access controls

Resource search is available to all organization members, but users can only see and query resources they have [permission](/docs/deployments/projects-and-stacks/#stack-permissions) to access:

- Organization admins have access to all resources
- If an organization has a default permission of read or write, all users can query all resources
- If an organization has no default permission, users can only query resources they have access to via Stack or Team permissions

## Next steps

- [Get started with Insights Discovery](/docs/insights/discovery/get-started/)
- [Create and manage accounts](/docs/insights/discovery/accounts/)
- [Learn Resource Search syntax](/docs/insights/discovery/search/)
- [Import resources into Pulumi IaC](/docs/insights/discovery/visual-import/)
- [Export resource data](/docs/insights/discovery/data-export/)
