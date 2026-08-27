---
title: Query the Context API
title_tag: "Query the Context API"
h1: Query the Context API
meta_desc: "Learn how to build Context API graph queries, follow infrastructure relationships, interpret results, and use the JSON selector reference."
menu:
  insights:
    name: Query the Context API
    parent: insights-context-api
    weight: 10
aliases:
  - /docs/insights/context-api/query-reference/
pulumi_cloud_feature: context-api
---

The Context API is a read-only Pulumi Cloud API for querying the infrastructure graph. For an introduction to the product, use cases, and access requirements, see the [Context API overview](/docs/insights/context-api/).

The graph connects nodes like resources (IaC or [Discovered]((/docs/insights/discovery/)) and stacks through relationships such as dependencies, parent-child links, provider ownership, and stack output consumption.

Queries use a JSON selector that says where to start, which relationships to follow, and which parts of the result to return. The API returns the selected graph data as nodes, edges, and optional evidence paths. The selector is JSON, not GraphQL, GQL, or Cypher text.

The Context API is in public preview. Before running a query, make sure that:

- You have [Pulumi CLI](/docs/install/) v3.243.0 or later and are logged in with `pulumi login`.
- Your organization has access to the Context API.
- Your role grants the [`resources:search` permission](/docs/administration/reference/rbac-scopes/org-settings/#resources). The default Member and Admin roles grant this permission.

## Run your first query

Start with one anchor, no traversal, and two projected fields. Save this selector as `query.json`:

```json
{
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "aws:s3/bucket:Bucket"
    }
  },
  "return": {
    "select": ["anchor"],
    "fields": ["name", "modified"]
  }
}
```

Read it in English as: **Find visible S3 buckets, walk no relationships, and return each bucket's name and modification time.**

Run the query against your Pulumi organization:

```bash
pulumi api GraphQuery -F orgName=my-org --input query.json
```

Replace `my-org` with your organization name. The first response page includes selected bucket nodes and their standard identity fields. When available, the requested `name` and `modified` values appear in each node's `fields` object. Before treating the list as exhaustive, follow [Check completeness before acting](#check-completeness-before-acting).

You can also call the REST endpoint directly. This example requires a [Pulumi access token](/docs/administration/concepts/access-tokens/) in `PULUMI_ACCESS_TOKEN`:

```bash
curl -X POST "https://api.pulumi.com/api/insights/my-org/graph/query" \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    --data @query.json
```

The example responses on this page are deliberately small. They show valid response shapes with fictional IDs and values, and their `resultCount` values match the entries shown. A real response can contain many more array entries. This editorial shortening is different from `meta.resultMode: "truncated"`, which means an engine cap was reached or the search backend returned a partial answer, so the API cannot certify the underlying result as complete. The example `schemaVersion` is also illustrative.

{{% details "Representative response" %}}

```json
{
  "nodes": [
    {
      "id": "urn:pulumi:prod::website::aws:s3/bucket:Bucket::assets",
      "nodeType": "resource",
      "frontier": ["anchor"],
      "urn": "urn:pulumi:prod::website::aws:s3/bucket:Bucket::assets",
      "type": "aws:s3/bucket:Bucket",
      "stack": "prod",
      "project": "website",
      "fields": {
        "modified": "2026-08-26T19:04:12Z",
        "name": "assets"
      }
    }
  ],
  "edges": [],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 1
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-25",
    "visibility": "complete"
  }
}
```

{{% /details %}}

The graph response envelope includes `nodes`, `edges`, `aggregations`, `pageInfo`, and `meta`. `paths` appears only when requested. For a graph result, `pageInfo.resultCount` counts nodes on that page.

## How queries work

The core mental model is: **find nodes, walk edges, choose the answer**. A frontier is the named set of nodes produced at one stage of the query.

| Stage | Selector clause | What it does |
|---|---|---|
| Find nodes | `anchor` | Selects the nodes where the query starts. |
| Walk edges | `traverse` | Follows typed relationships from one frontier of nodes to the next. |
| Choose the answer | `return` | Selects which frontiers, projected fields, and evidence paths appear in the response. |

Three optional clauses support that flow. `scope` narrows anchor selection, `aggregate` groups and counts anchors instead of walking the graph, and `page` controls response pagination.

The following snippets isolate one clause at a time. A selector containing only `anchor` is a complete request; the `traverse` and `return` objects are clause fragments to add to a request that already has an anchor. The complete query after them combines all three.

### Anchor: choose where to start

An anchor always names a node type. With no predicate, it selects every visible node of that type.

Before, every visible resource is an anchor:

```json
{
  "anchor": {
    "nodeType": "resource"
  }
}
```

After, only AWS provider resources below version 7.0.0 are anchors:

```json
{
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "pulumi:providers:aws",
      "fields": {
        "provider_version": {
          "op": "lt",
          "value": "7.0.0"
        }
      }
    }
  }
}
```

All predicates in `match` must be true. The API compares `provider_version` as a semantic version, so `10.0.0` is newer than `7.0.0`.

### Traverse: follow a relationship

Without a traversal, the query stops at its anchors:

```json
{
  "traverse": []
}
```

Add a traversal step to follow `provided_by` inward from each provider to the resources it manages:

```json
{
  "traverse": [
    {
      "edgeTypes": ["provided_by"],
      "direction": "in",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "managed"
    }
  ]
}
```

`depth` is an inclusive range of edge hops, where one hop means following one edge. Here, `min: 1` and `max: 1` mean exactly one hop, and `managed` names the frontier containing the nodes reached at that depth. For edge types that support multiple hops, a wider range puts nodes reached at any allowed depth into the same frontier. Setting `min` to `0` also keeps the nodes where the step started. If you omit `depth`, the step defaults to exactly one hop.

Directions are relative to an edge's defined orientation. A `provided_by` edge points from a managed resource to its provider, so walking it `in` from a provider reaches managed resources.

### Return: choose what comes back

This return clause includes both the starting providers and the `managed` traversal frontier:

```json
{
  "return": {
    "select": ["anchor", "managed"]
  }
}
```

Narrow the response to managed resources and only include the fields you need:

```json
{
  "return": {
    "select": ["managed"],
    "fields": ["name", "stack", "provider_version"]
  }
}
```

Every traversal alias names a frontier. `return.select` accepts `anchor` and those aliases. If you omit `return.select`, the API returns the anchor and the final traversal frontier.

### Put the clauses together

This complete query finds resources managed by an outdated AWS provider in the `payments` project:

```json
{
  "scope": {
    "stacks": ["payments/*"]
  },
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "pulumi:providers:aws",
      "fields": {
        "provider_version": {
          "op": "lt",
          "value": "7.0.0"
        }
      }
    }
  },
  "traverse": [
    {
      "edgeTypes": ["provided_by"],
      "direction": "in",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "managed"
    }
  ],
  "return": {
    "select": ["anchor", "managed"],
    "fields": ["name", "stack", "provider_version"]
  }
}
```

Read it in English as: **Start at AWS providers below version 7.0.0 in `payments` stacks, follow `provided_by` inward, and return the providers and the resources they manage.**

{{% details "Representative response" %}}

```json
{
  "nodes": [
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "nodeType": "resource",
      "frontier": ["managed"],
      "urn": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "type": "aws:ec2/instance:Instance",
      "stack": "prod",
      "project": "payments",
      "fields": {
        "name": "payments-web-0",
        "stack": "prod"
      }
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "nodeType": "resource",
      "frontier": ["anchor"],
      "urn": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "pulumi:providers:aws",
      "stack": "prod",
      "project": "payments",
      "fields": {
        "name": "default_6_0_4",
        "provider_version": "6.0.4",
        "stack": "prod"
      }
    }
  ],
  "edges": [
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 2
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-25",
    "visibility": "complete"
  }
}
```

{{% /details %}}

The `frontier` values distinguish the starting provider from the `managed` result. The edge keeps its defined managed-resource-to-provider orientation even though the query walked it inward. Requested field keys appear only when a value is stored, so the managed node in this example has no `provider_version` key.

`scope` restricts only where the anchors come from. A traversal can leave the named scope.

## Read the response

A graph query returns part of a graph rather than a table of rows.

| Response field | Meaning |
|---|---|
| `nodes` | The nodes selected for this page. Every node includes `id`, `nodeType`, and `frontier`; resource and stack identity fields appear when available. |
| `nodes[].frontier` | `anchor` and traversal aliases that selected the node. An empty array marks a node included only to support a returned path. |
| `nodes[].fields` | Extra values requested with `return.fields`. |
| `edges` | Directed, typed relationships between returned nodes or nodes returned on an earlier page. |
| `paths` | Evidence trails to the final traversal frontier when `return.paths` is true. A path is evidence of one route, not an enumeration of every route. |
| `aggregations.buckets` | Group keys and metrics returned by an aggregation query. |
| `pageInfo` | The result count for this page and, when another page exists, an opaque continuation token. |
| `meta` | Result fidelity, the contract revision, and traversal visibility. These fields describe how the API evaluated the selector, not whether the indexed facts are current. |

### Check completeness before acting

{{% notes type="warning" %}}
Do not treat a result as proving absence, an exhaustive cleanup-candidate list, a total across all groups, or a full blast radius until you have read every page, every page reports `meta.resultMode: "exact"`, and, for a traversal, every page reports `meta.visibility: "complete"`. These checks are necessary, but they certify the answer only relative to the selector, the caller's access, and the current search index.
{{% /notes %}}

Read these response signals together:

| Signal | What it means | Implications and next steps |
|---|---|---|
| `meta.resultMode` | `exact` means no engine cap was reported and the search backend reported a complete answer. `truncated` means a cap was reached or the backend returned a partial answer, so matching data may exist that is unreachable by this query. The public response does not identify which cause applied. | A `truncated` result cannot support an empty-result conclusion, an exhaustive list, a total across groups, an absence claim, or a full impact analysis. Returned nodes and edges, and the existence of returned aggregation buckets, remain positive evidence, but a bucket's metric can be incomplete. |
| `meta.visibility` | For a traversal, `complete` means the API did not detect a permission-trimmed walk. `trimmed` means permissions hid something the traversal encountered or the API could not verify visibility. Aggregations omit it. | A `trimmed` traversal cannot support an absence or full-impact claim. If access limited the walk, have a caller with broader access run the query before making a broader claim. |
| `pageInfo.continuationToken` | A present token means more of the result retained by the API remains. It is independent of `resultMode`. The key is absent on the final page of results. | A conclusion that depends on the full result remains incomplete while a token is present. Pass the opaque token back as `page.continuationToken` without modifying it. When `resultMode` is `exact`, each returned bucket's metric is complete for that key even if other bucket pages remain. |
| `meta.schemaVersion` | The graph contract revision used to evaluate the selector. It is not a completeness signal by itself. | If your client or saved selector assumes another revision, re-fetch the deployed schema and validate those assumptions before interpreting the result. |

If `resultMode` is `truncated`, retry the same selector once in case the search backend returned a transient partial response. If truncation persists, partition the anchors or narrow the scope or traversal. Remember that narrowing the selector also narrows the question it can answer.

Even an exact, complete, fully drained response can fail to support the conclusion you intended:

- Scope, predicates, edge types, and traversal depth define the question. For example, a three-hop query says nothing about a fourth-hop consumer and still reports `exact`.
- Anchor selection and aggregation include only nodes the caller can access. `meta.visibility` reports permission trimming during traversal; it does not report matching anchors excluded by access controls. To make an organization-wide absence or total claim, run the query with read access to every stack and cloud account. Otherwise, limit the claim to nodes visible to the caller.
- The API answers from the search index. Indexing lag, relationships the graph does not model, and `inferred_reference` edges can make the indexed graph differ from the source of record. An `inferred_reference` represents a possible dependency rather than a declared relationship.
- Resources pending deletion are outside the graph, so a graph count can be lower than a [Resource Search](/docs/insights/discovery/search/) count over an otherwise similar selection.
- Pages are evaluated as they are requested. If the graph changes while you drain a query, the combined pages may be inconsistent.
- `fieldsUnavailable: true` means projected fields could not be evaluated for that node. Do not base a field-dependent conclusion on that node's missing keys.

Process pages cumulatively. An edge or path on a later page can refer to a node returned earlier.

Confirm high-stakes absence answers against current stack state before deleting or decommissioning infrastructure.

## Complete query examples

The following examples apply the selector and response concepts above to common infrastructure questions. Substitute your own project, stack, resource type, and provider version.

### Which stacks consume these stack outputs

```json
{
  "anchor": {
    "nodeType": "stack",
    "match": {
      "fields": {
        "name": {
          "op": "in",
          "values": ["payments/prod", "payments/staging"]
        }
      }
    }
  },
  "traverse": [
    {
      "edgeTypes": ["consumes_outputs_of"],
      "direction": "in",
      "depth": {
        "min": 1,
        "max": 3
      },
      "alias": "downstream"
    }
  ],
  "return": {
    "select": ["anchor", "downstream"],
    "paths": true
  }
}
```

Read it in English as: **Start at the `payments/prod` and `payments/staging` stacks, follow stack output consumption inward for up to three hops, and return the starting stacks, their downstream consumers, and evidence paths.**

{{% details "Representative response" %}}

```json
{
  "nodes": [
    {
      "id": "stack:my-org/invoicing/prod",
      "nodeType": "stack",
      "frontier": ["downstream"],
      "stack": "prod",
      "project": "invoicing"
    },
    {
      "id": "stack:my-org/payments/prod",
      "nodeType": "stack",
      "frontier": ["anchor"],
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "stack:my-org/payments/staging",
      "nodeType": "stack",
      "frontier": ["anchor"],
      "stack": "staging",
      "project": "payments"
    }
  ],
  "edges": [
    {
      "id": "stack:my-org/invoicing/prod|consumes_outputs_of|stack:my-org/payments/prod",
      "from": "stack:my-org/invoicing/prod",
      "to": "stack:my-org/payments/prod",
      "type": "consumes_outputs_of"
    }
  ],
  "paths": [
    {
      "nodes": [
        "stack:my-org/payments/prod",
        "stack:my-org/invoicing/prod"
      ],
      "edges": [
        "stack:my-org/invoicing/prod|consumes_outputs_of|stack:my-org/payments/prod"
      ]
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 3
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-25",
    "visibility": "complete"
  }
}
```

{{% /details %}}

The path lists node IDs in traversal order and the edge IDs that connect them. The edge's `from` and `to` fields still use the relationship's defined orientation.

The three-hop depth is part of the question. Consumers farther away are not included, and that user-selected bound does not make `meta.resultMode` become `truncated`.

### What is the blast radius of a provider upgrade

```json
{
  "scope": {
    "stacks": ["payments/*"]
  },
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "pulumi:providers:aws",
      "fields": {
        "provider_version": {
          "op": "lt",
          "value": "7.0.0"
        }
      }
    }
  },
  "traverse": [
    {
      "edgeTypes": ["provided_by"],
      "direction": "in",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "managed"
    },
    {
      "edgeTypes": ["reference"],
      "direction": "in",
      "depth": {
        "min": 0,
        "max": 4
      },
      "alias": "dependents"
    },
    {
      "edgeTypes": ["in_stack"],
      "direction": "out",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "stacks"
    },
    {
      "edgeTypes": ["consumes_outputs_of"],
      "direction": "in",
      "depth": {
        "min": 0,
        "max": 3
      },
      "alias": "blastRadius"
    }
  ],
  "return": {
    "select": ["blastRadius"],
    "paths": true
  },
  "page": {
    "pageSize": 500
  }
}
```

Read it in English as: **Start at outdated AWS providers in `payments`, find what they manage, follow declared dependents, move from resources to their stacks, follow stack output consumers, and return the affected stacks with evidence paths.**

{{% details "Representative response" %}}

```json
{
  "nodes": [
    {
      "id": "stack:my-org/payments/prod",
      "nodeType": "stack",
      "frontier": ["blastRadius"],
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "nodeType": "resource",
      "frontier": [],
      "urn": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "type": "aws:ec2/instance:Instance",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "nodeType": "resource",
      "frontier": [],
      "urn": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "pulumi:providers:aws",
      "stack": "prod",
      "project": "payments"
    }
  ],
  "edges": [
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:my-org/payments/prod",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "stack:my-org/payments/prod",
      "type": "in_stack"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4|in_stack|stack:my-org/payments/prod",
      "from": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "to": "stack:my-org/payments/prod",
      "type": "in_stack"
    }
  ],
  "paths": [
    {
      "nodes": [
        "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
        "stack:my-org/payments/prod"
      ],
      "edges": [
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:my-org/payments/prod"
      ]
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 3
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-25",
    "visibility": "complete"
  }
}
```

{{% /details %}}

Only `blastRadius` was selected for return. The provider and managed resource therefore have empty `frontier` arrays, but the API includes them to make the evidence path self-contained. `pageInfo.resultCount` includes these supporting nodes.

`page.pageSize` requests up to 500 nodes per response page. Follow any `pageInfo.continuationToken` before treating the result as complete.

This selector follows declared `reference` edges. Add `inferred_reference` to the same reference step when you want possible dependencies as leads, and verify them before acting. The selected depth bounds limit which nodes the query can reach. The engine path cap limits the returned evidence and marks the result as truncated if it's reached.

### How many resources of each type are in a project

```json
{
  "scope": {
    "stacks": ["payments/*"]
  },
  "anchor": {
    "nodeType": "resource"
  },
  "aggregate": {
    "groupBy": ["type"],
    "metrics": [
      {
        "op": "count",
        "alias": "resources"
      }
    ]
  }
}
```

Read it in English as: **Start at resources in every `payments` stack, group them by resource type, and count each group.**

{{% details "Representative response" %}}

```json
{
  "nodes": [],
  "edges": [],
  "aggregations": {
    "buckets": [
      {
        "key": {
          "type": "aws:ec2/instance:instance"
        },
        "metrics": {
          "resources": 12
        }
      },
      {
        "key": {
          "type": "aws:rds/instance:instance"
        },
        "metrics": {
          "resources": 3
        }
      }
    ]
  },
  "pageInfo": {
    "resultCount": 2
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-25"
  }
}
```

{{% /details %}}

Aggregation returns buckets instead of nodes and edges. This response contains two buckets: the `resources` metric reports 12 EC2 instances and 3 RDS instances. `pageInfo.resultCount` is `2` because it counts buckets, and `meta.visibility` is absent because aggregation does not traverse the graph.

Follow every `pageInfo.continuationToken` and require `meta.resultMode: "exact"` on every page before treating the bucket list as complete. Run the query with access to all `payments` stacks when you need a project-wide view. Type bucket keys are lowercase even though resource type tokens use mixed case.

## Query reference

This section summarizes the current selector contract. The Context API is in public preview, so use the deployed schema and OpenAPI definition described in [Get the deployed schema](#get-the-deployed-schema) instead of depending on this snapshot.

### Top-level clauses

| Clause | Required | Purpose |
|---|---|---|
| `scope` | No | Narrows anchor selection by stacks, Discovery cloud accounts, or discovered-resource inclusion. |
| `anchor` | Yes | Selects the zero-hop starting nodes. |
| `traverse` | No | Applies ordered edge-walking steps. |
| `aggregate` | No | Groups and measures resource anchors instead of returning a graph walk. |
| `return` | No | Chooses frontiers, projected fields, and evidence paths. |
| `page` | No | Sets a page size or continues from a previous response. |

### Scope

Use `stacks` with either a `resource` or `stack` anchor. This complete selector starts at IaC resources in every stack in the `payments` project:

```json
{
  "scope": {
    "stacks": ["payments/*"],
    "includeDiscovered": false
  },
  "anchor": {
    "nodeType": "resource"
  }
}
```

Each `stacks` entry is either an exact `project/stack` name, such as `payments/prod`, or `project/*`, which selects every stack in that project. The request already identifies the organization, so omit it from the entry.

Use `accounts` with a `resource` anchor to select resources from Discovery cloud accounts:

```json
{
  "scope": {
    "accounts": ["production-aws"]
  },
  "anchor": {
    "nodeType": "resource"
  }
}
```

An account entry selects that account and its `/`-separated descendants. For example, `production-aws` also selects `production-aws/us-west-2`. To query stack nodes, use `scope.stacks` with a `stack` anchor.

- `accounts` entries name cloud accounts visible to the caller.
- Entries within each list are alternatives. When both lists are present on a resource query, an anchor must match a stack entry and an account entry.
- `includeDiscovered` defaults to `true`. Set it to `false` to exclude resources found by Discovery. It has no effect on a `stack` anchor.
- Scope restricts anchor selection only. Traversal can reach nodes outside it.

### Anchors and node types

Resources and stacks use different names when you select them and when you read them from a response:

- To select one resource, put `"urn": { "op": "eq", "value": "urn:pulumi:prod::payments::aws:s3/bucket:Bucket::assets" }` in `match.fields`. The returned node uses the same URN for both `id` and `urn`. When available, it also reports `type`, `project`, and `stack`.
- To select one stack, put `"name": { "op": "eq", "value": "payments/prod" }` in `match.fields`. Stack selectors omit the organization. The returned node includes it in `id`, for example `stack:my-org/payments/prod`, and reports `"project": "payments"` and `"stack": "prod"` separately.

An anchor accepts these fields:

| Field | Meaning |
|---|---|
| `nodeType` | Required. `resource` or `stack`. |
| `match` | A structured match. All present predicates are combined with AND. |
| `query` | A [Resource Search query](/docs/insights/discovery/search/) string. Valid only for a `resource` anchor and mutually exclusive with `match`. |
| `limit` | Bounds resolved anchors. Under aggregation it limits returned buckets, not the resources counted in a returned bucket. |

Omitting both `match` and `query` selects every visible node of the given type. For resource anchors, `match.type` is an exact resource type token such as `aws:s3/bucket:Bucket`. For `match.fields`, use fields listed in the deployed schema under `nodeTypes[].selectableFields`.

### Field predicates

| Operator | JSON shape | Meaning |
|---|---|---|
| `eq` | `{ "op": "eq", "value": "x" }` | Equal to one value. |
| `in` | `{ "op": "in", "values": ["x", "y"] }` | Equal to any listed value. |
| `lt` | `{ "op": "lt", "value": "x" }` | Less than the value. |
| `lte` | `{ "op": "lte", "value": "x" }` | Less than or equal to the value. |
| `gt` | `{ "op": "gt", "value": "x" }` | Greater than the value. |
| `gte` | `{ "op": "gte", "value": "x" }` | Greater than or equal to the value. |
| `present` | `{ "op": "present" }` | The field has a non-empty value or list. |
| `absent` | `{ "op": "absent" }` | The field has no value or has an empty value or list. |

Ordered comparisons are lexicographic except for `provider_version`, which uses semantic-version ordering. Predicate values are strings, and using an invalid operand key is rejected with an error.
For a stack node's `name` field, only `eq` and `in` are accepted.

### Traversal steps

This step starts from the current frontier, follows incoming declared `reference` edges for one to three hops, keeps the EC2 instances it reaches, and names that result `dependents`:

```json
{
  "edgeTypes": ["reference"],
  "direction": "in",
  "depth": {
    "min": 1,
    "max": 3
  },
  "target": {
    "match": {
      "type": "aws:ec2/instance:Instance"
    }
  },
  "alias": "dependents"
}
```

| Field | Example value | Effect |
|---|---|---|
| `edgeTypes` | `["reference"]` | Required. Follows declared dependency relationships. `["reference", "inferred_reference"]` is the only current multi-edge combination. |
| `direction` | `"in"` | Required. For `reference`, walks from a dependency to resources that depend on it. |
| `depth` | `{"min": 1, "max": 3}` | Includes nodes reached in one, two, or three hops. Omit it for exactly one hop. Set `min` to `0` to also keep the step's source nodes. |
| `target.match` | `{"type": "aws:ec2/instance:Instance"}` | Keeps only reached EC2 instance nodes. |
| `target.absent` | `true` | If added to `target` above, returns source nodes from which no matching EC2 instance is reachable within the depth range. Use it only on the final traversal step. |
| `alias` | `"dependents"` | Names this result so `return.select` can include it. Without an alias, the first step is `step0`, the second is `step1`, and so on. |

Before choosing an edge, direction, target field, or depth, fetch the [deployed schema](#get-the-deployed-schema). Each `edgeTypes[]` entry describes the edge's orientation and supported directions. The `singleHop` field identifies edges limited to one hop. For fields in `target.match`, use the target node type's `nodeTypes[].projectableFields`.

Aliases must be unique identifiers: a letter or underscore followed by letters, digits, or underscores. A traversal alias cannot be `anchor` or repeat an earlier alias.

`target.absent` evaluates only the edge types named in that step. Include both `reference` and `inferred_reference` when possible dependents should count alongside declared dependents. Treat an absence result as complete only when `meta.resultMode` is `exact` and `meta.visibility` is `complete`.

`in_stack` is a special traversal step. It resolves stack membership for every resource frontier accumulated so far, not only the immediately preceding frontier.

### Edge types and directions

The following table is a snapshot. Directions describe what a walk reaches from the current frontier.

| Edge type | Edge orientation | Supported directions | `out` reaches | `in` reaches | Hops | Basis |
|---|---|---|---|---|---|---|
| `reference` | dependent resource to dependency | `in`, `out`, `both` | Dependencies | Declared dependents | Multiple | Declared |
| `inferred_reference` | possible dependent to possible dependency | `in`, `out`, `both` | Possible dependencies | Possible dependents | Multiple | Inferred |
| `parent` | child resource to parent resource | `in`, `out`, `both` | Parent | Children | Multiple | Declared |
| `provided_by` | managed resource to provider resource | `in`, `out`, `both` | Provider | Managed resources | One | Declared |
| `in_stack` | resource to stack | `out` | Stack | Not supported | One | Declared |
| `consumes_outputs_of` | consumer stack to producer stack | `in`, `out` | Producers it consumes | Consumers of its outputs | Multiple | Declared |

`reference` records a declared dependency. `inferred_reference` is produced heuristically by matching scanned property values to destination provider IDs; treat it as a lead, not a fact.

A resource-level `reference` walk stops at a `pulumi:pulumi:StackReference` resource because that node has no direct edge to the producer stack it reads. For example, this selector starts at StackReference resources in `invoicing/prod` and reaches every producer stack whose outputs `invoicing/prod` consumes:

```json
{
  "scope": {
    "stacks": ["invoicing/prod"]
  },
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "pulumi:pulumi:StackReference"
    }
  },
  "traverse": [
    {
      "edgeTypes": ["in_stack"],
      "direction": "out",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "consumerStack"
    },
    {
      "edgeTypes": ["consumes_outputs_of"],
      "direction": "out",
      "depth": {
        "min": 1,
        "max": 1
      },
      "alias": "producerStacks"
    }
  ],
  "return": {
    "select": ["anchor", "consumerStack", "producerStacks"]
  }
}
```

The `in_stack` step moves from each StackReference resource to its containing consumer stack. Because `consumes_outputs_of` points from a consumer stack to a producer stack, the `out` step reaches the producer stacks. This second hop runs at stack level and can return multiple producer stacks. It does not associate a returned producer with a particular StackReference resource. To find stacks that consume a producer's outputs, use `direction: "in"` on the second step.

### Return, aggregation, and paging

`return` supports:

- `select`: Frontiers to include, using `anchor` and traversal aliases. It defaults to the anchor plus the final traversal frontier.
- `fields`: Requests additional resource fields in `nodes[].fields`. Choose field names from `nodeTypes[].projectableFields` in the current schema. When projection succeeds, the response includes each requested field that has a stored value. `fieldsUnavailable: true` means the node has no indexed document, so the requested fields could not be evaluated.
- `paths`: When `true`, includes up to one evidence path for each node in the final traversal frontier that has a recorded predecessor, regardless of which frontiers `select` includes. The engine returns at most `limits.maxPaths` paths for a query, currently 500. Reaching this result limit stops path generation and sets `meta.resultMode` to `truncated`; narrow the query when complete path evidence matters. Returned paths are not guaranteed to be shortest.

Use `aggregate` when you need grouped counts instead of individual nodes. This selector counts resources in each `payments` stack:

```json
{
  "scope": {
    "stacks": ["payments/*"]
  },
  "anchor": {
    "nodeType": "resource"
  },
  "aggregate": {
    "groupBy": ["stack"],
    "metrics": [
      {
        "op": "count",
        "alias": "resources"
      }
    ]
  }
}
```

`groupBy` creates one bucket per stack, `count` counts the matching resources in each bucket, and `alias` names that count `resources` in the bucket's `metrics` object. Aggregations return `aggregations.buckets` instead of resource nodes. See [How many resources of each type are in a project](#how-many-resources-of-each-type-are-in-a-project) for a complete response.

`aggregate` supports resource anchors only and cannot be combined with `traverse`, `return.select`, `return.fields`, or `return.paths`. An anchor that compares `provider_version` by using `lt`, `lte`, `gt`, or `gte` is also incompatible. `aggregate` accepts:

- `groupBy`: One or two distinct fields from `nodeTypes[].groupByFields`. Fields are applied in nesting order. Resources whose grouped field is missing, empty, or too long to be indexed as a grouping value appear in no bucket. These omissions do not by themselves set `meta.resultMode` to `truncated`.
- `metrics`: One or more metrics for each bucket. The current metric operation is `count`; each metric also needs a unique identifier as its `alias` for the result key.

`page.pageSize` defaults to 200. A response with `pageInfo.continuationToken` has another page. Copy the opaque value into `page.continuationToken` without modifying it.

### Current limits

These values are a snapshot, not a compatibility promise. Check `GetGraphSchema` for current values.

| Limit | Current cap | Behavior at the limit |
|---|---:|---|
| Traversal steps per query | 4 | A larger selector is rejected. |
| `depth.max` per step | 6 | A larger selector is rejected. |
| Entries in `scope.stacks` | 100 | A larger selector is rejected. |
| Entries in `scope.accounts` | 100 | A larger selector is rejected. |
| Fields in `aggregate.groupBy` | 2 | A larger selector is rejected. |
| Resolved anchors, aggregation buckets, or `in` values | 1,000 | More matching anchors or aggregation buckets mark the result `truncated`; a traversal query that would clip anchors is rejected instead. An `in` predicate with more values is rejected. |
| New nodes per traversal level | 8,000 | The result is marked `truncated`. |
| Nodes held by one query | 20,000 | The result is marked `truncated`. |
| Recorded edge crossings | 80,000 | The result is marked `truncated`. |
| Evidence paths | 500 | The result is marked `truncated`. |
| `page.pageSize` | 1,000 | A larger value is silently reduced to 1,000. |

## Get the deployed schema

Fetch the latest schema before composing or validating selectors:

```bash
pulumi api GetGraphSchema -F orgName=my-org --output=json
```

The JSON response is authoritative for the deployed schema version, node types, fields available for selection, projection, and grouping, fixed field values, edge types and directions, metric operations, and engine limits. This response is not a complete JSON Schema for the request body.

Fetch the Markdown representation when you want the deployed agent primer, including selector guidance and worked examples:

```bash
pulumi api GetGraphSchema -F orgName=my-org --output=markdown
```

The [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/) defines the accepted request and response shapes. While the Context API remains in public preview, re-fetch the deployed schema instead of relying on a saved copy.
