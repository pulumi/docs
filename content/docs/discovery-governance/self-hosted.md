---
title: Self-hosted Insights
title_tag: Self-hosted Insights | Discovery & Governance
h1: Self-hosted Insights
meta_desc: Run Discovery scans and policy evaluations in your own environment using customer-managed workflow runners.
menu:
  insights:
    parent: insights-home
    weight: 50
pulumi_cloud_feature: insights-self-hosted
---

Pulumi Insights supports self-hosted operation through [customer-managed workflow runners](/docs/deployments/concepts/customer-managed-runners/). This allows you to run [Discovery scans](/docs/insights/discovery/) and [policy evaluations](/docs/insights/policy/) within your own infrastructure, giving you full control over where your data is processed while retaining the power of Pulumi Insights.

## Benefits

Running Insights in your own environment with customer-managed workflow runners provides several advantages:

- **Data residency**: Keep all scan data and policy evaluations within your private network
- **Private infrastructure access**: Scan resources in fully private VPCs and environments that are not accessible from the public internet
- **Compliance**: Meet regulatory requirements by ensuring cloud provider credentials never leave your network
- **Flexible hosting**: Host workflow runners on any hardware and environment that meets your needs, including Linux and macOS

## How it works

Customer-managed workflow runners support multiple workflow types beyond deployments, including Discovery scans and policy evaluations. Workflow runners poll Pulumi Cloud for pending workflows and execute them in your self-hosted environment.

For full setup and configuration details, see the [customer-managed workflow runners](/docs/deployments/concepts/customer-managed-runners/) documentation.

### Setting up Discovery scans

1. [Set up a customer-managed workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#using-customer-managed-workflow-runners)
1. Navigate to **Management** > **Accounts** in Pulumi Cloud
1. Select the workflow runner pool for the account you want to scan
1. Trigger a scan and confirm it completes successfully

### Setting up policy evaluations

1. [Set up a customer-managed workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#using-customer-managed-workflow-runners)
1. Navigate to **Management** > **Policies** > **Policy Groups** in Pulumi Cloud
1. Select the workflow runner pool for an audit policy group
1. Run a policy evaluation against a stack and confirm the results appear as expected

### Using an organization default pool

If you want every account scan and policy evaluation to use a customer-managed pool by default, you can set an [organization default workflow runner pool](/docs/deployments/guides/customer-managed-workflow-runners/#setting-an-organization-default-pool). When set, scans and policy groups without an explicit pool use the organization default instead of the Pulumi Hosted Pool.

### Restricting workflow types

By default, workflow runners handle all workflow types (deployments, Discovery scans, and policy evaluations). You can restrict which workflow types a runner handles using the `enabled_workflow_types` configuration option in `pulumi-workflow-agent.yaml`:

```yaml
enabled_workflow_types:
    - insights_scan
    - policy_evaluation
```

For the full list of configuration options, see the [configuration reference](/docs/deployments/concepts/customer-managed-runners/#configuration-reference).
