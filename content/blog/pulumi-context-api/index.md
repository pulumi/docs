---
title: "Pulumi Context API: One Graph for All Your Infrastructure"
date: 2026-08-26
draft: false
meta_desc: "The Pulumi Context API is now in preview: query IaC state, stack dependencies, and discovered cloud resources as one graph built for AI agents."
feature_image: feature.png
authors:
    - levi-blackstone
tags:
    - features
    - ai-agents
    - pulumi-cloud
category: product
schema_type: auto
pulumi_cloud_feature: context-api

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        What breaks if we change this stack? What can we safely delete? The answers exist, scattered across state files, cloud consoles, and whoever set things up.

        We connected everything Pulumi knows into one graph your AI agent can query. Here's how it works.
    linkedin: |
        Every platform team fields the same questions. What is running? What breaks if we change this? What can we safely delete?

        The answers exist. They're just scattered across state files, cloud consoles, and the memories of whoever set things up.

        Pulumi already holds most of the picture: the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and the resources discovered in your cloud accounts outside IaC entirely. Today we launched the Context API, which connects those views into a single graph you can query.

        We designed it agent-first. The API serves its own primer, so any agent, from Neo to Claude Code to your own automation, can learn the whole query language in one request. Validation errors are specific enough that agents correct their own queries without help.

        Which stacks break if we upgrade this provider? How much of our infrastructure lives outside IaC? What has no dependents and can be retired? Each question can be answered with a single query.
    bluesky: |
        We just launched the Pulumi Context API: everything Pulumi knows about your infrastructure as one queryable graph, built agent-first. Any agent can learn it in one request, and Neo uses it out of the box.

        Here's a brief tour.
---

Every platform team fields the same questions: What is running? What breaks if we change this? What can we safely delete? The answers exist, but they're scattered across state files, cloud consoles, and the memories of whoever set things up. Today we're launching the Pulumi Context API, which connects what Pulumi knows about your infrastructure into a single graph you can query. It's designed agent-first: [Pulumi Neo](/product/neo/), our infrastructure agent, uses it out of the box, and the API itself teaches any agent what it needs to know to get started. It's available in preview.

<!--more-->

## Answers that span all your infrastructure

Pulumi already holds a detailed picture of your infrastructure. It knows the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and which resources in your cloud accounts [Discovery](/docs/insights/discovery/) found outside IaC entirely. Each of those views is useful on its own. Now, the Context API lets you ask questions that cut across all of them:

- **Impact**: Which stacks are affected if we upgrade this provider? If this stack changes, what consumes its outputs?
- **Coverage**: How much of our infrastructure lives outside IaC, and in which accounts?
- **Cleanup**: Which stacks have no dependents and are candidates for retirement?

Each of these can be answered with a query against a graph that covers your resources (both Pulumi-managed and discovered), your stacks, and the relationships that connect them.

A query is a JSON document with a handful of clauses. `anchor` names the starting nodes, `traverse` walks relationships from there, and `return` picks what comes back. To run one, POST it to `https://api.pulumi.com/api/insights/<your-org>/graph/query`, or use the CLI: `pulumi api GraphQuery -F orgName=<your-org> --input query.json`. Here's a query that finds every resource that's managed by an AWS provider older than version 7.0.0:

```json
{
  "anchor": {
    "nodeType": "resource",
    "match": {
      "type": "pulumi:providers:aws",
      "fields": { "provider_version": { "op": "lt", "value": "7.0.0" } }
    }
  },
  "traverse": [
    { "edgeTypes": ["provided_by"], "direction": "in", "depth": { "min": 1, "max": 1 }, "alias": "managed" }
  ],
  "return": { "select": ["anchor", "managed"] }
}
```

And here's the response, trimmed to a few nodes and fields:

```json
{
  "nodes": [
    {
      "id": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db",
      "nodeType": "resource",
      "frontier": ["managed"],
      "type": "aws:rds/instance:Instance",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/vpc:Vpc::payments-vpc",
      "nodeType": "resource",
      "frontier": ["managed"],
      "type": "aws:ec2/vpc:Vpc",
      "stack": "prod",
      "project": "payments"
    },
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "nodeType": "resource",
      "frontier": ["anchor"],
      "type": "pulumi:providers:aws",
      "stack": "prod",
      "project": "payments"
    }
  ],
  "edges": [
    {
      "from": "urn:pulumi:prod::payments::aws:rds/instance:Instance::payments-db",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    }
  ],
  "pageInfo": { "resultCount": 5 },
  "meta": {
    "resultMode": "exact",
    "visibility": "complete",
    "schemaVersion": "2026-08-25"
  }
}
```

Each node shows the traversal step that reached it with the `frontier` field. In this example, the `anchor` is the outdated provider and the resources are `managed` by it. The `meta` fields tell you whether the answer is complete: `resultMode` flips to `truncated` if a size limit capped the results or the search backend answered partially, and `visibility` is `trimmed` if your RBAC permissions hid part of the graph. A continuation token appears in `pageInfo` if the answer was split into multiple pages.

## Ask Neo, or bring your own agent

We expect AI agents to be the primary users of the Context API. [Pulumi Neo](/product/neo/) uses it out of the box: ask Neo what breaks if a stack changes, and it queries the graph on your behalf, with the permissions of the user who invoked it.

Any other agent, whether that's Claude Code, Cursor, Codex, or your own automation, can learn the API in one request. The schema endpoint returns a Markdown document ("primer") covering the node and edge vocabulary, the full query grammar, and examples. Fetch it with the Pulumi CLI:

```bash
pulumi api GetGraphSchema -F orgName=my-org
```

or over plain HTTP:

```bash
curl -H "Accept: text/markdown" \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    https://api.pulumi.com/api/insights/my-org/graph/schema
```

The primer is the complete reference for the query language. To onboard an agent, have it fetch the primer with `pulumi api GetGraphSchema -F orgName=<your-org>`. Putting that command in your `AGENTS.md` or `CLAUDE.md` means the agent pulls a fresh copy whenever it needs one; the primer evolves with the API. From there, your agent composes queries from natural language questions and runs them with `pulumi api GraphQuery`. Most validation errors list the legal values inline, so an agent that re-reads the primer on rejection can correct its own queries.

## Available in preview

The `pulumi api` commands shown here need [Pulumi CLI](/docs/install/) v3.243.0 or later. Access uses the same permission as [Resource Search](/docs/insights/discovery/search/), so if you can search resources in the console today, you can query the graph. Results are trimmed to the caller's permissions. While the API is in preview the contract may change; any breaking changes will be announced in the [changelog](/releases/).

## The graph will grow

This launch is a first step. The graph vocabulary is designed to grow without breaking existing consumers, and we plan to bring in more of what Pulumi knows: [Pulumi ESC](/docs/esc/) environments, so you can trace which stacks a configuration or secret change reaches; teams and roles, so the graph knows who owns what; cloud accounts; and service catalog concepts from [Pulumi IDP](/docs/idp/), our internal developer platform.

## Get started

If your organization uses [Neo](/product/neo/), it already knows about the latest graph schema. For any other agent, tell it to fetch the primer with `pulumi api GetGraphSchema -F orgName=<your-org>`. Then, start asking questions about your infrastructure graph using natural language.

Give it a try today, and share your feedback in the [Pulumi Community Slack](https://slack.pulumi.com/) or through your account team. If there's a question you want answered that the graph doesn't handle yet, tell us. That will shape what we build next.
