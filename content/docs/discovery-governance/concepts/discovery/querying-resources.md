---
title: Querying resources
title_tag: Querying resources | Discovery & governance
h1: Querying resources
meta_desc: Pulumi Cloud lets you search every resource in your organization in one place, whether Pulumi manages it or Discovery found it in a cloud account.
menu:
  discovery-governance:
    name: Querying resources
    parent: dg-concepts-discovery
    weight: 15
pulumi_cloud_feature: resource-search
---

Pulumi Cloud gives you one place to find and query all the infrastructure in your organization. Resource search covers two kinds of resources side by side:

- **Pulumi-managed resources**: resources in your Pulumi stacks, whether you created them with Pulumi IaC or imported them.
- **Discovered resources**: resources that [Discovery](/docs/discovery-governance/concepts/discovery/) found when it scanned your [cloud accounts](/docs/discovery-governance/concepts/discovery/cloud-accounts/), however they were created: in the cloud console, with another IaC tool such as Terraform or CloudFormation, or by a cloud service itself.

Because both kinds appear in the same results, one query answers questions about your whole estate, such as "which storage buckets exist in production?", without checking each stack and each cloud console separately.

## Pulumi-managed and discovered resources together

Each resource in the results shows how it's managed. The **Managed By** column reads **Pulumi** for resources in a Pulumi stack and **Other** for resources that Discovery found but no Pulumi stack manages. Filtering on this column shows you what isn't under IaC yet, a natural starting point for bringing resources under Pulumi management with [Visual Import](/docs/discovery-governance/concepts/discovery/visual-import/).

A resource can come from more than one source: a stack might manage a bucket that Discovery also found in the same cloud account. Pulumi Cloud recognizes these as the same resource and shows a single entry for it, so your results don't double-count.

## Ways to query

- **Search queries**: Search by name, type, stack, project, or resource property, combine terms with logical operators, and group the results, for example by cloud account and region. For the syntax, see [Search resources](/docs/discovery-governance/guides/search-resources/).
- **Natural language**: Ask a question in plain language, such as "How many VPCs do I have?", and Pulumi Cloud writes the search query for you. You can also ask [Pulumi Neo](/docs/ai/neo/) questions about your resources.
- **Export and API**: Download the results as CSV, or query resources from your own tools with the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/resource-search/). See [Export resource data](/docs/discovery-governance/guides/export-resource-data/).
- **Relationship queries**: To follow dependencies between resources, stacks, and their consumers, use the [Context API](/docs/discovery-governance/concepts/context-api/).

## Who can see which resources

Everyone in an organization can search, but each person sees only the resources they have [permission](/docs/administration/concepts/rbac/permission-sets/#stack-permission-sets) to access. For the details, see [Access controls](/docs/discovery-governance/guides/search-resources/#access-controls).
