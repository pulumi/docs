---
title: Context API
title_tag: "Context API | Discovery & Governance"
h1: Context API
meta_desc: Query IaC state, stack dependencies, and discovered cloud resources as one graph, built for AI agents.
menu:
  insights:
    parent: insights-home
    identifier: insights-context-api
    weight: 30
pulumi_cloud_feature: context-api
---

The Context API connects everything Pulumi knows about your infrastructure into a single queryable graph: the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and the resources [Discovery](/docs/insights/discovery/) has found in your cloud accounts outside IaC entirely. Instead of piecing an answer together from stack state, cloud consoles, and tribal knowledge, you ask the graph directly. Questions like which stacks break if you upgrade a provider, how much of an account lives outside IaC, or which stacks have no dependents and are safe to retire, are each a single query.

The API is designed agent-first. [Pulumi Neo](/product/neo/) queries it out of the box, and any other agent, from Claude Code to Cursor to your own automation, can learn the whole query language in one request by fetching the API's own schema. The rest of this page covers the graph model, how to call the API, and the fetch-the-primer workflow that gets an agent using it without any docs beyond this page.

## The graph model

The graph is built from these node types:

| Node type | Meaning |
|---|---|
| `resource` | anything Pulumi knows about, whether it's declared by a Pulumi program or found by Discovery scanning a cloud account |
| `stack` | a Pulumi stack |

Nodes are connected by these relationship types:

| Relationship | Connects | Meaning |
|---|---|---|
| `pulumi:reference` | resource to resource | one resource depends on another |
| `parent` | resource to resource | containment, such as a component and the resources it creates |
| `provided_by` | resource to resource | a resource and the provider that manages it |
| `in_stack` | resource to stack | a resource belongs to a stack |
| `consumes_outputs_of` | stack to stack | one stack reads another stack's outputs |

A query names a starting point (`anchor`), walks relationships from there (`traverse`), and returns the connected nodes and edges (`return`). The wire format is JSON, not a query language. The full grammar, including field predicates, aggregation, and pagination, lives in the schema the API serves itself, described below.

## Calling the API

The Context API exposes two operations, both documented in the [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/). Call either one through the [Pulumi CLI](/docs/install/) (v3.243.0 or later) or with a plain HTTP request.

To fetch the schema:

```console
$ pulumi api GetGraphSchema -F orgName=<your-org>
```

```console
$ curl -H "Accept: text/markdown" \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    https://api.pulumi.com/api/insights/<your-org>/graph/schema
```

To run a query, with a selector saved to `query.json`:

```console
$ pulumi api GraphQuery -F orgName=<your-org> --input query.json
```

```console
$ curl -X POST https://api.pulumi.com/api/insights/<your-org>/graph/query \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    --data @query.json
```

A response reports whether it's complete: `meta.resultMode` is `exact` or `truncated`. Only an `exact` response can answer a question about absence, such as "nothing depends on this resource." A `truncated` response means the query hit a size limit before it finished, so narrow the anchor or scope and run it again rather than treating a partial answer as final. Each response also carries `meta.schemaVersion`, a date that advances whenever the API's observable behavior changes.

## Fetch the primer first

The schema endpoint doesn't just describe field names, it returns a complete primer: the node and edge vocabulary, the full query grammar, worked examples, and the caps currently in effect. The CLI asks for Markdown by default, meant to be handed straight to an agent (a raw HTTP request must send `Accept: text/markdown`, as shown above). Add `--output=json` to the CLI if you want the machine-readable schema instead; over raw HTTP, JSON is the default.

The primer is the canonical reference for the query language, not this page. It's generated from the deployment that will actually answer your queries, so it's always in sync. Re-fetch it before composing new queries rather than relying on a saved copy or on examples you've seen before, since the vocabulary and caps can change between schema versions.

That makes onboarding an agent a single step: fetch the schema, hand it to the agent, and let the agent compose and run queries from there. If a query is rejected, the error message names exactly what would have been accepted, so an agent can correct itself without a person in the loop.

### Wire it into your agent's instructions

Paste the following into your `AGENTS.md` or `CLAUDE.md` so any agent working in your repository knows to fetch the primer before it queries the graph:

````markdown
## Pulumi Context API

This organization has the Pulumi Context API enabled. Before composing or running a
graph query, fetch the current schema and follow it exactly, since the query
vocabulary and caps can change between schema versions:

```console
$ pulumi api GetGraphSchema -F orgName=<your-org>
```

Use the returned primer to compose a JSON selector, then run it:

```console
$ pulumi api GraphQuery -F orgName=<your-org> --input query.json
```

Don't guess at fields, edge types, or caps, and don't reuse a schema fetched in an
earlier session. If a query is rejected, read the error message and correct the
selector against the schema it names.
````

Replace `<your-org>` with your Pulumi organization name. See the [query recipes](/docs/insights/context-api/recipes/) for worked examples covering common questions.

## Access and permissions

The Context API is read-only. It uses the same permission model as [Resource Search](/docs/insights/discovery/search/): if you can search for a resource in the Pulumi Cloud console, you can reach it through a graph query. Results are trimmed to the caller's permissions at every step of a query, not just at the anchor, so a more restricted caller sees a smaller graph, not an error.

The Context API is in preview, and its contract can still change. Any breaking change will be announced in the [changelog](/releases/).

## Next steps

- [Query recipes](/docs/insights/context-api/recipes/): worked selectors for common questions like provider-upgrade impact, blast radius, and IaC coverage.
- [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/): full request and response schemas for `GetGraphSchema` and `GraphQuery`.
- [Resource Search](/docs/insights/discovery/search/): explore and query resources interactively in the Pulumi Cloud console.
- [Pulumi Neo](/docs/ai/neo/): Pulumi's infrastructure agent, which queries the Context API out of the box.
- [Discovery](/docs/insights/discovery/): how Pulumi finds the cloud resources outside IaC that the graph includes.
