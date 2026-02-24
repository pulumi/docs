---
title: Self-hosted Insights
title_tag: Self-hosted Insights | Pulumi Insights
h1: Self-hosted Insights
meta_desc: Run Pulumi Insights discovery scans and policy evaluations in your own environment using customer-managed workflow runners.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: insights-home
    weight: 50
---

Pulumi Insights supports self-hosted operation for Business Critical customers through [customer-managed workflow runners](/docs/deployments/deployments/customer-managed-agents/). This allows you to run [discovery scans](/docs/insights/discovery/) and [policy evaluations](/docs/insights/policy/) within your own infrastructure, giving you full control over where your data is processed while retaining the power of Pulumi Insights.

{{% notes "info" %}}
Self-hosted Insights is available on the Business Critical edition of Pulumi Cloud. [Contact sales](/contact/?form=sales) if you are interested in enabling this feature.
{{% /notes %}}

## Benefits

Running Insights in your own environment with customer-managed workflow runners provides several advantages:

- **Data residency**: Keep all scan data and policy evaluations within your private network
- **Private infrastructure access**: Scan resources in fully private VPCs and environments that are not accessible from the public internet
- **Compliance**: Meet regulatory requirements by ensuring cloud provider credentials never leave your network
- **Flexible hosting**: Host workflow runners on any hardware and environment that meets your needs, including Linux and macOS

## How it works

Customer-managed workflow runners support multiple workflow types beyond deployments, including Insights discovery scans and policy evaluations. Workflow runners poll Pulumi Cloud for pending workflows and execute them in your self-hosted environment.

For full setup and configuration details, see the [customer-managed workflow runners](/docs/deployments/deployments/customer-managed-agents/) documentation.

### Setting up Insights scans

1. [Set up a customer-managed workflow runner pool](/docs/deployments/deployments/customer-managed-agents/#using-customer-managed-workflow-runners)
2. Navigate to **Management** > **Accounts** in Pulumi Cloud
3. Select the workflow runner pool for the account you want to scan
4. Trigger a scan and confirm it completes successfully

### Setting up policy evaluations

1. [Set up a customer-managed workflow runner pool](/docs/deployments/deployments/customer-managed-agents/#using-customer-managed-workflow-runners)
2. Navigate to **Management** > **Policies** > **Policy Groups** in Pulumi Cloud
3. Select the workflow runner pool for an audit policy group
4. Run a policy evaluation against a stack and confirm the results appear as expected

### Restricting workflow types

By default, workflow runners handle all workflow types (deployments, Insights scans, and policy evaluations). You can restrict which workflow types a runner handles using the `enabled_workflow_types` configuration option in `pulumi-workflow-agent.yaml`:

```yaml
enabled_workflow_types:
    - insights_scan
    - policy_evaluation
```

For the full list of configuration options, see the [configuration reference](/docs/deployments/deployments/customer-managed-agents/#configuration-reference).
