---
title: Query Recipes
title_tag: "Query Recipes | Context API"
h1: Query Recipes
meta_desc: Curated Context API query recipes for provider-upgrade impact, cross-stack dependencies, and infrastructure coverage.
menu:
  insights:
    parent: insights-context-api
    weight: 10
pulumi_cloud_feature: context-api
---

These recipes translate common infrastructure questions into [Context API](/docs/insights/context-api/) selectors. Each one answers a specific question a platform team runs into repeatedly, such as scoping a provider upgrade or finding resources that live outside IaC.

{{% notes type="info" %}}
The schema returned by `pulumi api GetGraphSchema -F orgName=<org>` is the canonical reference for the query vocabulary and caps, and it can change between schema versions. Fetch it before composing new queries rather than relying on the examples below verbatim.
{{% /notes %}}

The selectors below use an example organization (`acme-corp`) whose projects include `payments`, `invoicing`, `reporting`, and `audit`, each with `prod` and `staging` stacks. Substitute your own organization, project, and stack names. Each recipe includes the response the example organization gets back, collapsed under the query.

## What does an outdated provider still manage?

Before upgrading a provider, which resources does the old version still manage?

```json
{
  "scope": { "stacks": ["payments/*"] },
  "anchor": { "nodeType": "resource", "match": { "type": "pulumi:providers:aws", "fields": { "provider_version": { "op": "lt", "value": "7.0.0" } } } },
  "traverse": [ { "edgeTypes": ["provided_by"], "direction": "in", "depth": { "min": 1, "max": 1 }, "alias": "managed" } ],
  "return": { "select": ["anchor", "managed"] }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "nodeType": "resource",
      "frontier": [
        "managed"
      ],
      "urn": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "type": "aws:ec2/instance:Instance",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/subnet:Subnet::payments-subnet-a",
      "nodeType": "resource",
      "frontier": [
        "managed"
      ],
      "urn": "urn:pulumi:prod::payments::aws:ec2/subnet:Subnet::payments-subnet-a",
      "type": "aws:ec2/subnet:Subnet",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/vpc:Vpc::payments-vpc",
      "nodeType": "resource",
      "frontier": [
        "managed"
      ],
      "urn": "urn:pulumi:prod::payments::aws:ec2/vpc:Vpc::payments-vpc",
      "type": "aws:ec2/vpc:Vpc",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db",
      "nodeType": "resource",
      "frontier": [
        "managed"
      ],
      "urn": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db",
      "type": "aws:rds/instance:Instance",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "pulumi:providers:aws",
      "stack": "prod",
      "project": "payments"
    }
  ],
  "edges": [
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/subnet:Subnet::payments-subnet-a|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/subnet:Subnet::payments-subnet-a",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/vpc:Vpc::payments-vpc|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/vpc:Vpc::payments-vpc",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 5
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-21",
    "visibility": "complete"
  }
}
```

{{< /details >}}

The anchor matches provider resources below version 7.0.0 (versions compare as semantic versions, not as strings, so `10.0.0` counts as newer than `7.0.0`); walking `provided_by` inward from there returns everything each of those providers manages. Check `meta.resultMode` before treating the returned list as complete: `truncated` means more managed resources may exist that this response didn't reach, so narrow the query (a tighter `scope`, or a more selective anchor) and re-run.

## What's the full blast radius of upgrading this provider?

If I upgrade this provider, what's the complete set of resources and stacks that could be affected?

```json
{
  "scope": { "stacks": ["payments/*"] },
  "anchor": { "nodeType": "resource", "match": { "type": "pulumi:providers:aws", "fields": { "provider_version": { "op": "lt", "value": "7.0.0" } } } },
  "traverse": [
    { "edgeTypes": ["provided_by"],         "direction": "in",  "depth": { "min": 1, "max": 1 }, "alias": "managed" },
    { "edgeTypes": ["pulumi:reference"],    "direction": "in",  "depth": { "min": 0, "max": 4 }, "alias": "dependents" },
    { "edgeTypes": ["in_stack"],            "direction": "out", "depth": { "min": 1, "max": 1 }, "alias": "stacks" },
    { "edgeTypes": ["consumes_outputs_of"], "direction": "in",  "depth": { "min": 0, "max": 3 }, "alias": "blastRadius" }
  ],
  "return": { "select": ["blastRadius"], "paths": true },
  "page": { "pageSize": 500 }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [
    {
      "id": "stack:acme-corp/audit/prod",
      "nodeType": "stack",
      "frontier": [
        "blastRadius"
      ],
      "stack": "prod",
      "project": "audit"
    },
    {
      "id": "stack:acme-corp/invoicing/prod",
      "nodeType": "stack",
      "frontier": [
        "blastRadius"
      ],
      "stack": "prod",
      "project": "invoicing"
    },
    {
      "id": "stack:acme-corp/payments/prod",
      "nodeType": "stack",
      "frontier": [
        "blastRadius"
      ],
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "stack:acme-corp/reporting/prod",
      "nodeType": "stack",
      "frontier": [
        "blastRadius"
      ],
      "stack": "prod",
      "project": "reporting"
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
      "id": "stack:acme-corp/audit/prod|consumes_outputs_of|stack:acme-corp/invoicing/prod",
      "from": "stack:acme-corp/audit/prod",
      "to": "stack:acme-corp/invoicing/prod",
      "type": "consumes_outputs_of"
    },
    {
      "id": "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
      "from": "stack:acme-corp/invoicing/prod",
      "to": "stack:acme-corp/payments/prod",
      "type": "consumes_outputs_of"
    },
    {
      "id": "stack:acme-corp/reporting/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
      "from": "stack:acme-corp/reporting/prod",
      "to": "stack:acme-corp/payments/prod",
      "type": "consumes_outputs_of"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:acme-corp/payments/prod",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "stack:acme-corp/payments/prod",
      "type": "in_stack"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4|in_stack|stack:acme-corp/payments/prod",
      "from": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "to": "stack:acme-corp/payments/prod",
      "type": "in_stack"
    }
  ],
  "paths": [
    {
      "nodes": [
        "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
        "stack:acme-corp/payments/prod"
      ],
      "edges": [
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:acme-corp/payments/prod"
      ]
    },
    {
      "nodes": [
        "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod"
      ],
      "edges": [
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod"
      ]
    },
    {
      "nodes": [
        "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod",
        "stack:acme-corp/audit/prod"
      ],
      "edges": [
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
        "stack:acme-corp/audit/prod|consumes_outputs_of|stack:acme-corp/invoicing/prod"
      ]
    },
    {
      "nodes": [
        "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/reporting/prod"
      ],
      "edges": [
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|provided_by|urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
        "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0|in_stack|stack:acme-corp/payments/prod",
        "stack:acme-corp/reporting/prod|consumes_outputs_of|stack:acme-corp/payments/prod"
      ]
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 6
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-21",
    "visibility": "complete"
  }
}
```

{{< /details >}}

This chains four hops: provider, to what it manages, to what depends on those resources, to the stacks that contain them, to every stack consuming those stacks' outputs. `return.paths: true` returns one evidence trail per node, so each result comes with a concrete path showing how it's connected to the original provider. Because a blast-radius answer is only useful if it's complete, treat `meta.resultMode: "truncated"` as disqualifying: narrow the scope and re-run rather than acting on a partial result.

## Which stacks consume this stack's outputs?

If I change this stack, which other stacks read its outputs and could break?

```json
{
  "anchor": { "nodeType": "stack", "match": { "fields": { "name": { "op": "in", "values": ["payments/prod", "payments/staging"] } } } },
  "traverse": [ { "edgeTypes": ["consumes_outputs_of"], "direction": "in", "depth": { "min": 1, "max": 3 }, "alias": "downstream" } ],
  "return": { "select": ["anchor", "downstream"], "paths": true }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [
    {
      "id": "stack:acme-corp/audit/prod",
      "nodeType": "stack",
      "frontier": [
        "downstream"
      ],
      "stack": "prod",
      "project": "audit"
    },
    {
      "id": "stack:acme-corp/invoicing/prod",
      "nodeType": "stack",
      "frontier": [
        "downstream"
      ],
      "stack": "prod",
      "project": "invoicing"
    },
    {
      "id": "stack:acme-corp/payments/prod",
      "nodeType": "stack",
      "frontier": [
        "anchor"
      ],
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "stack:acme-corp/payments/staging",
      "nodeType": "stack",
      "frontier": [
        "anchor"
      ],
      "stack": "staging",
      "project": "payments"
    },
    {
      "id": "stack:acme-corp/reporting/prod",
      "nodeType": "stack",
      "frontier": [
        "downstream"
      ],
      "stack": "prod",
      "project": "reporting"
    }
  ],
  "edges": [
    {
      "id": "stack:acme-corp/audit/prod|consumes_outputs_of|stack:acme-corp/invoicing/prod",
      "from": "stack:acme-corp/audit/prod",
      "to": "stack:acme-corp/invoicing/prod",
      "type": "consumes_outputs_of"
    },
    {
      "id": "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
      "from": "stack:acme-corp/invoicing/prod",
      "to": "stack:acme-corp/payments/prod",
      "type": "consumes_outputs_of"
    },
    {
      "id": "stack:acme-corp/reporting/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
      "from": "stack:acme-corp/reporting/prod",
      "to": "stack:acme-corp/payments/prod",
      "type": "consumes_outputs_of"
    }
  ],
  "paths": [
    {
      "nodes": [
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod"
      ],
      "edges": [
        "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod"
      ]
    },
    {
      "nodes": [
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/invoicing/prod",
        "stack:acme-corp/audit/prod"
      ],
      "edges": [
        "stack:acme-corp/invoicing/prod|consumes_outputs_of|stack:acme-corp/payments/prod",
        "stack:acme-corp/audit/prod|consumes_outputs_of|stack:acme-corp/invoicing/prod"
      ]
    },
    {
      "nodes": [
        "stack:acme-corp/payments/prod",
        "stack:acme-corp/reporting/prod"
      ],
      "edges": [
        "stack:acme-corp/reporting/prod|consumes_outputs_of|stack:acme-corp/payments/prod"
      ]
    }
  ],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 5
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-21",
    "visibility": "complete"
  }
}
```

{{< /details >}}

The anchor is the stack, or stacks, you're changing; walking `consumes_outputs_of` inbound up to three hops catches both direct consumers and stacks that consume a consumer. `return.paths` distinguishes the two: a one-edge path is a direct dependency, a longer one is transitive. An empty `downstream` frontier with `meta.resultMode: "exact"` means no stack currently consumes this one's outputs, at least none the caller can see.

## Which stacks have no downstream consumers?

Which stacks are safe to decommission because nothing else depends on them?

```json
{
  "anchor": { "nodeType": "stack", "match": { "fields": { "name": { "op": "in", "values": ["payments/prod", "payments/staging"] } } } },
  "traverse": [ { "edgeTypes": ["consumes_outputs_of"], "direction": "in", "depth": { "min": 1, "max": 3 }, "target": { "absent": true }, "alias": "unconsumed" } ],
  "return": { "select": ["unconsumed"] }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [
    {
      "id": "stack:acme-corp/payments/staging",
      "nodeType": "stack",
      "frontier": [
        "unconsumed"
      ],
      "stack": "staging",
      "project": "payments"
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
    "schemaVersion": "2026-08-21",
    "visibility": "complete"
  }
}
```

{{< /details >}}

`target.absent: true` inverts the traversal, returning the stacks from which the walk reaches no consumer at all, the candidates for cleanup. Treat this as a lead, not a final verdict: absence is judged only against what the calling identity can see, so a consumer the caller lacks permission to see won't disqualify a stack from appearing here. Only trust the result when `meta.resultMode` is `exact`; a `truncated` answer means the check isn't reliable, so narrow the query and re-run before acting on it.

## How much of each cloud account is covered by IaC, versus discovered separately?

How much infrastructure did Pulumi Insights find in each cloud account that no Pulumi program declared?

```json
{
  "anchor": { "nodeType": "resource", "match": { "fields": { "account": { "op": "present" } } } },
  "aggregate": { "groupBy": ["account"], "metrics": [ { "op": "count", "alias": "found" } ] }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [],
  "edges": [],
  "aggregations": {
    "buckets": [
      {
        "key": {
          "account": "gq-legacy-aws"
        },
        "metrics": {
          "found": 1
        }
      },
      {
        "key": {
          "account": "gq-prod-aws/payments-legacy-cfn"
        },
        "metrics": {
          "found": 2
        }
      },
      {
        "key": {
          "account": "gq-prod-aws"
        },
        "metrics": {
          "found": 4
        }
      }
    ]
  },
  "pageInfo": {
    "resultCount": 3
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-21"
  }
}
```

{{< /details >}}

Only resources discovered by cloud scanning carry an `account` field, so this anchor isolates them from Pulumi-declared resources; grouping by `account` gives a per-account count of what's outside IaC. Use it alongside your own stack resource counts to gauge coverage and prioritize which accounts to bring under management first. If `meta.resultMode` is `truncated`, some accounts are missing from the list entirely; the counts inside the buckets that were returned are still complete, so narrow the anchor and re-run to see the rest.

## Is this resource managed by a Pulumi stack, or was it only discovered?

How can I tell whether a given resource is under Pulumi management or was found by a cloud scan?

```json
{
  "anchor": { "nodeType": "resource", "match": { "fields": { "account": { "op": "present" } } } },
  "traverse": [ { "edgeTypes": ["in_stack"], "direction": "out", "depth": { "min": 1, "max": 1 }, "alias": "stacks" } ],
  "return": { "select": ["anchor", "stacks"] }
}
```

{{< details "Example response" >}}

```json
{
  "nodes": [
    {
      "id": "urn:insights:gq-legacy-aws::aws::aws:ec2/instance:Instance::i-0ccc333",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-legacy-aws::aws::aws:ec2/instance:Instance::i-0ccc333",
      "type": "aws:ec2/instance:Instance",
      "account": "gq-legacy-aws"
    },
    {
      "id": "urn:insights:gq-prod-aws/payments-legacy-cfn::pulumi::pulumi:cloudformation:index/resource:Resource::payments-legacy-assets",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws/payments-legacy-cfn::pulumi::pulumi:cloudformation:index/resource:Resource::payments-legacy-assets",
      "type": "pulumi:cloudformation:index/resource:Resource",
      "account": "gq-prod-aws/payments-legacy-cfn"
    },
    {
      "id": "urn:insights:gq-prod-aws/payments-legacy-cfn::pulumi::pulumi:cloudformation:index/stack:Stack::payments-legacy-cfn",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws/payments-legacy-cfn::pulumi::pulumi:cloudformation:index/stack:Stack::payments-legacy-cfn",
      "type": "pulumi:cloudformation:index/stack:Stack",
      "account": "gq-prod-aws/payments-legacy-cfn"
    },
    {
      "id": "urn:insights:gq-prod-aws::aws::aws:ec2/instance:Instance::i-0aaa111",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws::aws::aws:ec2/instance:Instance::i-0aaa111",
      "type": "aws:ec2/instance:Instance",
      "account": "gq-prod-aws"
    },
    {
      "id": "urn:insights:gq-prod-aws::aws::aws:ec2/instance:Instance::i-0bbb222",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws::aws::aws:ec2/instance:Instance::i-0bbb222",
      "type": "aws:ec2/instance:Instance",
      "account": "gq-prod-aws"
    },
    {
      "id": "urn:insights:gq-prod-aws::aws::aws:ec2/securityGroup:SecurityGroup::sg-0demo123",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws::aws::aws:ec2/securityGroup:SecurityGroup::sg-0demo123",
      "type": "aws:ec2/securityGroup:SecurityGroup",
      "account": "gq-prod-aws"
    },
    {
      "id": "urn:insights:gq-prod-aws::aws::aws:rds/instance:Instance::payments-db-prod",
      "nodeType": "resource",
      "frontier": [
        "anchor"
      ],
      "urn": "urn:insights:gq-prod-aws::aws::aws:rds/instance:Instance::payments-db-prod",
      "type": "aws:rds/instance:Instance",
      "account": "gq-prod-aws"
    }
  ],
  "edges": [],
  "aggregations": {
    "buckets": []
  },
  "pageInfo": {
    "resultCount": 7
  },
  "meta": {
    "resultMode": "exact",
    "schemaVersion": "2026-08-21",
    "visibility": "complete"
  }
}
```

{{< /details >}}

`in_stack` only exists for resources a Pulumi program deployed, so walking it outward from a resource returns a stack if, and only if, that resource is Pulumi-managed. A resource discovered by cloud scanning produces an empty `stacks` frontier every time, because a scan deploys nothing and creates no such edge. This is the reliable way to distinguish IaC-managed resources from ones Insights found on its own.
