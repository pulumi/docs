---
title: "Pulumi Context API: query your infrastructure as a graph"
date: 2026-08-26
updated: 2026-08-28
draft: false
meta_desc: "The Pulumi Context API is now in public preview: query Pulumi-managed and discovered resources, stacks, and their relationships as a graph."
feature_image: feature.png
authors:
    - levi-blackstone
tags:
    - features
    - ai-agents
    - pulumi-cloud
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        What breaks if we change this stack? What can we safely delete? The answers are scattered across state files and cloud consoles.

        The Context API connects Pulumi-managed and discovered resources, stacks, and relationships in a graph your agent can query.
    linkedin: |
        Every platform team fields the same questions. What is running? What breaks if we change this? What can we safely delete?

        The answers exist. They're just scattered across state files, cloud consoles, and the memories of whoever set things up.

        Pulumi already holds most of the picture: the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and the resources discovered in your cloud accounts outside IaC entirely. Today we launched the Context API, which connects those views into a single graph you can query.

        We designed it agent-first. The API serves its own primer, so any agent that can run authenticated Pulumi CLI commands can fetch the current graph vocabulary and query language on demand. Validation errors are specific enough that agents can often correct their own queries.

        Which stacks break if we upgrade this provider? How much of our infrastructure lives outside IaC? What has no dependents and can be retired? These are the kinds of questions the Context API helps an agent investigate.
    bluesky: |
        We just launched the Pulumi Context API: Pulumi-managed and discovered resources, stacks, and their relationships in one queryable graph, built agent-first. Neo uses it out of the box, and other agents can fetch the current query primer.

        Here's a brief tour.
---

Every platform team fields the same questions: What is running? What breaks if we change this? What can we safely delete? The answers exist, but they're scattered across state files, cloud consoles, and the memories of whoever set things up. Today we're launching the [Pulumi Context API](/docs/insights/context-api/), a read-only API that connects Pulumi-managed and discovered resources, stacks, and their relationships into a graph. It's designed agent-first: [Pulumi Neo](/product/neo/), our infrastructure agent, uses it out of the box, and other agents can fetch the current graph vocabulary and query guidance on demand. It's available in public preview for organizations on the Enterprise and Business Critical editions.

<!--more-->

## Answers that follow infrastructure relationships

Pulumi already records the resources your programs manage, their dependencies, how stacks consume each other's outputs, and the resources [Pulumi Discovery](/docs/insights/discovery/) finds outside infrastructure as code (IaC). The Context API connects this data so you can ask questions that depend on the relationships:

- **Impact**: Which stacks are affected if we upgrade this provider? If this stack changes, what consumes its outputs?
- **Coverage**: How much of our infrastructure lives outside IaC, and in which accounts?
- **Cleanup**: Which stacks have no dependents and are candidates for retirement?

A query is a JSON document with a handful of clauses. `anchor` names the starting nodes, `traverse` follows relationships from there, and `return` chooses what comes back. You can run a query through the Pulumi CLI or REST API. Here's a selector that starts from AWS provider instances older than version 7.0.0 and follows incoming `provided_by` relationships back to the visible resources they manage:

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
    {
      "edgeTypes": ["provided_by"],
      "direction": "in",
      "alias": "managed"
    }
  ],
  "return": { "select": ["anchor", "managed"] }
}
```

A response for one matching provider and one managed resource looks like this (abridged for clarity):

```json
{
  "nodes": [
    {
      "id": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "nodeType": "resource",
      "frontier": ["anchor"],
      "type": "pulumi:providers:aws"
    },
    {
      "id": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "nodeType": "resource",
      "frontier": ["managed"],
      "type": "aws:ec2/instance:Instance"
    }
  ],
  "edges": [
    {
      "from": "urn:pulumi:prod::payments::aws:ec2/instance:Instance::payments-web-0",
      "to": "urn:pulumi:prod::payments::pulumi:providers:aws::default_6_0_4",
      "type": "provided_by"
    }
  ],
  "pageInfo": { "resultCount": 2 },
  "meta": {
    "resultMode": "exact",
    "visibility": "complete"
  }
}
```

The `anchor` frontier marks the provider, while `managed` marks the EC2 instance reached by the traversal. The `provided_by` edge keeps its defined direction from the instance to its provider, and `resultCount` reflects the two nodes on this page. The [Context API query guide](/docs/insights/guides/context-api/#put-the-clauses-together) walks through the complete response, and its [completeness guidance](/docs/insights/guides/context-api/#check-completeness-before-acting) explains how to assess an answer before acting on it.

## Ask Neo or bring your own agent

Start by asking an agent a question in natural language. [Pulumi Neo](/product/neo/) uses the Context API out of the box and runs queries with the permissions of the person who invoked it.

Claude Code, Cursor, Codex, and other agents that can run authenticated Pulumi CLI commands can fetch the schema endpoint's Markdown primer:

```bash
pulumi api GetGraphSchema -F orgName=my-org
```

Replace `my-org` with your organization name. The primer explains the current graph vocabulary, query grammar, engine limits, examples, pagination, and completeness checks. Put the command in your `AGENTS.md` or `CLAUDE.md` so the agent can refresh the primer as the API evolves. The [human-readable query guide](/docs/insights/guides/context-api/) explains the same concepts and includes direct CLI and REST examples.

## Available in public preview

The Context API is available now for every organization on the Enterprise and Business Critical editions. The [`pulumi api` access requirements](/docs/insights/context-api/#get-access) include [Pulumi CLI](/docs/install/) v3.243.0 or later, an authenticated session, and a role with the [`resources:search` permission](/docs/administration/reference/rbac-scopes/org-settings/#resources). The default Member and Admin roles grant this permission. Pulumi Cloud [role-based access control](/docs/administration/concepts/rbac/) limits responses to the resources, stacks, and cloud accounts the caller can read.

During public preview, the graph vocabulary and limits may change. Fetch the [deployed schema](/docs/insights/guides/context-api/#get-the-deployed-schema) when you need the current contract. We also plan to connect more Pulumi Cloud data, including [Pulumi ESC](/docs/esc/) environments, teams and roles, cloud accounts, and service catalog concepts from [Pulumi IDP](/docs/idp/). Feedback during preview will shape the relationships and data sources we add next.

## Get started

Start with the [Context API overview](/docs/insights/context-api/), then follow the [agent workflow](/docs/insights/guides/context-api/#ask-questions-through-an-ai-agent) to equip your agent. Ask a natural-language question such as, "Which stacks consume outputs from the `payments/prod` stack?"

Give it a try today, and share your feedback in the [Pulumi Community Slack](https://slack.pulumi.com/) or through your account team.
