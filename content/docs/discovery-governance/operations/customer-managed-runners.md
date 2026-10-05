---
title: Run scans and policy evaluations on customer-managed runners
title_tag: Customer-managed runners | Discovery & governance
h1: Run scans and policy evaluations on customer-managed runners
meta_desc: Run Discovery scans and audit policy evaluations on customer-managed runners, and choose the runner pool for each cloud account and policy group.
menu:
  discovery-governance:
    name: Customer-managed runners
    parent: dg-operations
    weight: 20
aliases:
- /docs/discovery-governance/operations/self-hosted/
- /docs/insights/self-hosted/
- /docs/discovery-governance/self-hosted/
pulumi_cloud_feature: customer-managed-runners
---

By default, [Discovery scans](/docs/discovery-governance/concepts/discovery/) and [policy evaluations](/docs/discovery-governance/concepts/policy-as-code/) run on Pulumi-managed runners. With [customer-managed runners](/docs/administration/concepts/customer-managed-runners/), they run on runners you host in your own infrastructure instead, using the same runner pools that can also run Pulumi Deployments.

## Benefits

Running scans and policy evaluations on customer-managed runners provides several advantages:

- **Data residency**: Keep scan data and policy evaluations within your private network.
- **Private infrastructure access**: Scan resources in fully private VPCs and environments that aren't accessible from the public internet.
- **Compliance**: Meet regulatory requirements by ensuring cloud provider credentials never leave your network.
- **Flexible hosting**: Host runners on any hardware and environment that meets your needs, including Linux and macOS.

## How it works

Runners poll Pulumi Cloud for pending work and execute it in your environment. A single runner can handle deployments, Discovery scans, and policy evaluations. For the execution model, the full list of what runs on customer-managed runners, and the configuration reference, see [Customer-managed runners](/docs/administration/concepts/customer-managed-runners/).

Each kind of work picks a pool in this order:

- **Discovery scans**: the cloud account's pool, then the organization default pool, then the Pulumi hosted pool. A scan started through the [REST API](/docs/reference/cloud-rest-api/) can name a different pool for that one scan.
- **Policy evaluations**: the audit policy group's pool, then the organization default pool, then the Pulumi hosted pool. Only [audit policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/#run-audit-policy-groups-on-customer-managed-runners) use a runner pool. Preventative policy groups run inside `pulumi up` and `pulumi preview` wherever the CLI runs.

## Set up

### Set up Discovery scans

1. [Set up a customer-managed runner pool](/docs/administration/guides/customer-managed-runners/#set-up-a-runner-pool).
1. Navigate to **Resources** > **Discovery** in Pulumi Cloud.
1. Select the runner pool for the account you want to scan.
1. Trigger a scan and confirm it completes successfully.

### Set up policy evaluations

1. [Set up a customer-managed runner pool](/docs/administration/guides/customer-managed-runners/#set-up-a-runner-pool).
1. Navigate to **Governance** > **Policy configuration** in Pulumi Cloud and select the **Policy Groups** tab.
1. Select the runner pool for an audit policy group.
1. Run a policy evaluation against a stack and confirm the results appear as expected.

### Use an organization default pool

If you want every account scan and policy evaluation to use a customer-managed pool by default, set an [organization default runner pool](/docs/administration/guides/customer-managed-runners/#setting-an-organization-default-pool). When set, scans and audit policy groups without an explicit pool use the organization default instead of the Pulumi hosted pool.

### Restrict workflow types

By default, runners handle all workflow types (deployments, Discovery scans, and policy evaluations). You can restrict which workflow types a runner handles using the `enabled_workflow_types` configuration option in `pulumi-workflow-agent.yaml`:

```yaml
enabled_workflow_types:
    - insights_scan
    - policy_evaluation
```

For the full list of configuration options, see the [configuration reference](/docs/administration/concepts/customer-managed-runners/#configuration-reference).
