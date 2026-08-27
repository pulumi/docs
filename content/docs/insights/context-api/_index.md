---
title: Context API
title_tag: "Context API overview"
h1: Context API
meta_desc: "Understand how the Context API queries the Pulumi Cloud infrastructure graph to answer dependency, ownership, and impact questions."
menu:
  insights:
    name: Context API
    parent: insights-home
    identifier: insights-context-api
    weight: 30
pulumi_cloud_feature: context-api
---

The Context API is a read-only Pulumi Cloud API for asking questions about how infrastructure is connected. It queries an organization's infrastructure graph, which connects nodes like resources (IaC or [Discovered](/docs/insights/discovery/)) and stacks through relationships such as dependencies, parent-child links, provider ownership, and stack output consumption.

The API is especially useful when the answer depends on those relationships rather than the properties of one resource. Users can execute queries through the Pulumi CLI or REST API.

## How can the Context API help

The Context API can help platform engineers, infrastructure owners, and incident responders investigate questions such as:

| Question | How the graph helps answer it |
|---|---|
| Which stacks consume outputs from this stack? | Follow stack output consumption relationships to downstream stacks. |
| What depends on this resource? | Walk declared references and optionally include inferred references as leads to verify. |
| What could a provider upgrade affect? | Find resources owned by matching provider instances, then follow their dependents and stack relationships. |
| Which resources use an outdated provider version? | Match provider nodes by package and version, then follow provider ownership relationships. |
| How many resources of each type are in a project? | Group matching resource nodes by type and count them. |

These answers can support investigation and planning. For decisions such as deleting infrastructure or declaring a blast radius complete, also evaluate the response's completeness signals and confirm the result against the relevant source of record.

## Choose the right API

[Resource Search](/docs/insights/discovery/search/) filters and groups indexed resources by their properties. Start there when a set of resource records can answer the question.

The Context API starts from matching nodes (resources, stacks, etc.) and follows typed relationships between them. Use it when the question depends on connections, multiple hops, or evidence showing how one node is related to another. The two APIs are complementary, and both answer from data visible to the caller.

## How a query works

The basic mental model is: **find nodes, walk edges, choose the answer**.

1. An `anchor` finds the nodes where the query starts.
1. One or more `traverse` steps walk named relationships to new sets of nodes.
1. A `return` clause chooses which sets, fields, and evidence paths appear in the response.

Queries may narrow anchor selection with `scope`, group matching nodes with `aggregate`, and page through larger results. See the [Context API query guide](/docs/insights/guides/context-api/) for details and examples.

## What the graph includes

The current graph has two node types:

- Resource nodes can represent resources managed by Pulumi or resources found through Pulumi Discovery.
- Stack nodes represent Pulumi stacks.

Typed edges describe relationships such as a resource reference, an inferred reference, a parent-child relationship, provider ownership, stack membership, or one stack consuming another stack's outputs. The available fields, edge types, directions, and limits can change during public preview. [Get the deployed schema](/docs/insights/guides/context-api/#get-the-deployed-schema) for the current vocabulary and engine limits.

## Get access

The Context API is in public preview. To run a query, you need:

- Pulumi CLI v3.243.0 or later, authenticated with `pulumi login`, or a Pulumi access token for direct REST requests.
- An organization with access to the Context API.
- A role that grants the [`resources:search` permission](/docs/administration/reference/rbac-scopes/org-settings/#resources). The default Member and Admin roles grant this permission.

Use `pulumi api GraphQuery` to call the API from the CLI, or send a request to the Graph Query endpoint through the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/). Start with [Run your first query](/docs/insights/guides/context-api/#run-your-first-query) for complete CLI and REST examples.

## Interpret answers with care

A Context API response describes what the query engine could establish from the selector, the caller's authorized view, and the current search index. The response does not unconditionally guarantee facts about every resource in the organization.

Read these signals before relying on an answer:

| Signal | Meaning |
|---|---|
| `meta.resultMode` | `exact` means no engine cap was reported and the search backend reported a complete answer. `truncated` means matching data may exist beyond what the API could return. |
| `meta.visibility` | For traversal queries, `complete` means the API did not detect permission trimming during the walk. `trimmed` means permissions hid data or the API could not verify visibility. Aggregation responses omit this field. |
| `pageInfo.continuationToken` | When present, another page of retained results remains. This signal is independent of `resultMode`. |
| `meta.schemaVersion` | Identifies the graph contract revision used for the query. |

{{% notes type="warning" %}}
Do not use a `truncated` result, a `trimmed` traversal, or an unread continuation page to prove absence, produce an exhaustive cleanup list, report a complete total, or declare a full blast radius. Even after every page reports `exact` and, for a traversal, `complete`, the answer depends on the selector and caller's access. Indexing lag, relationships the graph does not model, inferred relationships, and graph changes between pages can lead to misleading or outdated results.
{{% /notes %}}

See [Check completeness before acting](/docs/insights/guides/context-api/#check-completeness-before-acting) for the full interpretation rules and recovery guidance.

## Next steps

- [Run your first query](/docs/insights/guides/context-api/#run-your-first-query).
- [Learn the query mental model and work through complete examples](/docs/insights/guides/context-api/).
- [Review the formal selector and response reference](/docs/insights/guides/context-api/#query-reference).
- [Fetch the deployed schema and agent primer](/docs/insights/guides/context-api/#get-the-deployed-schema).
