---
title_tag: Self-Hosted Feature Parity | Self-Hosting Pulumi
meta_desc: Which Pulumi Cloud features are available in self-hosted Pulumi Cloud, and which need extra configuration or enablement.
title: Feature parity
h1: Self-hosted feature parity
menu:
  administration:
    name: Feature parity
    parent: administration-self-hosting
    weight: 8
    identifier: administration-self-hosted-feature-parity
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

The table below shows whether selected Pulumi Cloud features are available in self-hosted Pulumi Cloud, and what they need. It isn't a complete list of Pulumi Cloud features: to check one that isn't listed, [contact us](/contact/). The [status key](#status-key) below the table explains what each status means.

| Feature | Self-hosted | Details |
|---|---|---|
| [Context API](/docs/discovery-governance/concepts/context-api/) | Requires configuration | Needs a self-hosted release from late October 2026 or later, and the [OpenSearch cluster](/docs/administration/self-hosting/components/search/) that resource search uses. |
| [Custom roles](/docs/administration/concepts/rbac/roles/) | Available |  |
| [Deployments](/docs/administration/self-hosting/components/deployments/) | Requires configuration | There's no Pulumi-hosted runner pool. Deployments run on [customer-managed agents](/docs/administration/concepts/customer-managed-runners/) that you register to an agent pool, and so do discovery scans and policy evaluations. Terraform remote execution and module conversion aren't supported. |
| [Discovery & governance](/docs/discovery-governance/) | Available |  |
| [Drift detection](/docs/deployments/concepts/drift/) | Requires enablement | Off by default. Contact Pulumi support to turn it on. Scheduled drift runs and automatic remediation also need Deployments set up. You can always detect drift from the CLI with `pulumi refresh --preview-only`. |
| [ESC approvals](/docs/esc/concepts/approvals/) | Available |  |
| [Pulumi ESC](/docs/esc/) | Available |  |
| [Pulumi Neo](/docs/ai/concepts/neo/) | Not available | Not available yet. Features built on Neo, such as Neo tasks, aren't available either. |
| [Terraform module registry](/docs/integrations/terraform/module-registry/) | Not available | Not available yet, so modules can't be published to the registry or converted into Pulumi packages. |
| [Terraform remote execution](/docs/integrations/terraform/remote-execution/) | Not available | Not available yet. Workspaces set to remote execution run locally instead. |
| [Terraform state backend](/docs/integrations/terraform/state-backend/) | Requires configuration | Set `PULUMI_TFE_DOMAIN` to a hostname of its own, separate from `PULUMI_API_DOMAIN`, and use that hostname in place of `tf.pulumi.com`. |
| [Webhooks](/docs/deployments/concepts/webhooks/) | Available |  |

## Status key

| Status | Meaning |
|---|---|
| Available | Works the same way as in Pulumi Cloud. |
| Requires enablement | Included, but turned off by default. Contact Pulumi support to turn it on for your installation. |
| Requires configuration | Works once you set up the extra components described in the feature's details. |
| Not available | Not supported in self-hosted Pulumi Cloud yet. |
