---
title_tag: Explore resources | Discovery & governance
title: Explore resources
h1: Explore resources
meta_desc: Search all your Pulumi-managed and discovered resources on the Resources page in Pulumi Cloud, with query syntax or AI Assist.
weight: 5
menu:
  discovery-governance:
    name: Explore resources
    parent: dg-get-started
    weight: 5
aliases:
  - /docs/insights/get-started/using-resource-explorer/
  - /docs/insights/discovery/get-started/using-resource-explorer/
  - /docs/discovery-governance/discovery/get-started/using-resource-explorer/
pulumi_cloud_feature: resource-search
---

Discovery has now scanned your cloud account, so you can explore what it found. The **Resources** page in Pulumi Cloud shows every resource in your organization in one place: the resources your Pulumi stacks manage and the resources Discovery found in your cloud accounts. You can search across all your clouds at once, for example to find every VPC in AWS and Azure, or every resource tagged for a particular cost center. For how this works, see [Querying resources](/docs/discovery-governance/concepts/discovery/querying-resources/).

To open it, navigate to **Resources** > **Resources** in the Pulumi Cloud console.

The Resources page gives you several ways to find resources:

- **Query syntax**: Search with a structured query language, for example `package:snowflake`.
- **AI Assist**: Describe what you're looking for in plain language, and Pulumi Cloud writes the query for you. This helps when you don't know the exact syntax, type tokens, or package names.
- **Column filters and grouping**: Filter the results by any column, such as type, project, or stack, and group them, for example by cloud account and region.
- **CSV export and API**: Download your results as CSV, or query resources from your own tools with the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/resource-search/).

## Example searches

The following examples use the [query syntax](/docs/discovery-governance/guides/search-resources/) and AI Assist to answer common questions about your infrastructure.

### Query syntax

To see all resources modified in the last 30 days:

```text
modified:<now-30d
```

To find resources with a particular tag, such as every S3 bucket that belongs to a cost center:

```text
type:aws:s3/bucket:Bucket tags.costcenter:1234
```

### AI Assist

Switch the search bar to AI Assist mode and ask a question in plain language. For example, **"show me all cloud storage buckets"** produces a query like:

```text
type:"aws:s3/bucket:Bucket" OR type:"gcp:storage/bucket:Bucket" OR type:"azure:storage/bucket:Bucket"
```

AI Assist is also useful during a security review. **"show me all s3 public buckets"** produces a query like:

```text
type:"aws:s3/bucket:Bucket" .acl:public-read
```

AI Assist's queries are a starting point: review them, and refine the query if it doesn't quite match what you meant. To ask broader questions about your infrastructure, you can also use [Pulumi Neo](/docs/ai/neo/).

{{< get-started-stepper >}}
