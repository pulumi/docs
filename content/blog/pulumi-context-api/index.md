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

        We designed it agent-first. The API serves its own primer, so any agent, from Neo to Claude Code to your own automation, can learn the whole query language in one request. Validation errors even list the legal values, so agents correct their own queries without help.

        Which stacks break if we upgrade this provider? How much of our infrastructure lives outside IaC? What has no dependents and can be retired? Each one is a single query.
    bluesky: |
        We just launched the Pulumi Context API: everything Pulumi knows about your infrastructure as one queryable graph, built agent-first. Any agent can learn it in one request, and Neo uses it out of the box.

        We wrote up what it can answer.
---

Every platform team fields the same questions: What is running? What breaks if we change this? What can we safely delete? The answers exist, but they're scattered across state files, cloud consoles, and the memories of whoever set things up. Today we're launching the Pulumi Context API, which connects what Pulumi knows about your infrastructure into a single graph you can query. It's designed agent-first: [Pulumi Neo](/product/neo/), our infrastructure agent, uses it out of the box, and the API itself teaches any other agent everything it needs in one request. It's available in preview for organizations on the Enterprise and Business Critical editions.

<!--more-->

## Answers that span all your infrastructure

Pulumi already holds a detailed picture of your infrastructure. It knows the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and which resources in your cloud accounts [Pulumi Insights](/docs/insights/) has discovered outside IaC entirely. Each of those views is useful on its own. The Context API connects them, so you can ask the questions that cut across all of them:

- **Impact**: Which stacks are affected if we upgrade this provider? If this stack changes, what consumes its outputs?
- **Coverage**: How much of our infrastructure lives outside IaC, and in which accounts?
- **Cleanup**: Which stacks have no dependents and can be retired?

Each of these is a single query. The graph covers your resources (both Pulumi-managed and discovered), your stacks, and the relationships that connect them, from dependencies and containment to providers and cross-stack references.

A query names its starting nodes (`anchor`), walks the relationships between them (`traverse`), and returns the connected results. Here's one that finds every resource still managed by an AWS provider older than 7.0:

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

The response includes the matching nodes, the edges between them, and, when you ask for them, the paths that connect them, so an answer shows its evidence. Each response also reports whether it is complete. That means an empty answer to "does anything depend on this?" is one you can act on.

## Ask Neo, or bring your own agent

We expect AI agents to be the primary users of the Context API, and it's designed for them. [Pulumi Neo](/product/neo/) uses it out of the box: ask Neo what breaks if a stack changes, and it queries the graph on your behalf, with the permissions of the user who invoked it.

Any other agent, whether that's Claude Code, Cursor, Codex, or your own automation, can learn the API in one request. The schema endpoint answers in Markdown by default with a short primer covering the node and edge vocabulary, the query grammar, and worked examples. That document is the entire onboarding. Fetch it with the Pulumi CLI:

```bash
pulumi api GetGraphSchema -F orgName=my-org
```

or over plain HTTP:

```bash
curl -H "Accept: text/markdown" \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    https://api.pulumi.com/api/insights/my-org/graph/schema
```

Paste the primer into a chat, or put the fetch command in your `AGENTS.md` or `CLAUDE.md` so your agent pulls a fresh copy when it needs one (the primer evolves with the API, so a saved copy goes stale). Your agent can then compose queries from plain-English questions and run them with the same CLI or token access shown above. Validation errors list the legal values and point back at the schema endpoint, so agents recover from their own mistakes without help.

## Available in preview

The Context API is available now for every organization on the Enterprise and Business Critical editions. The `pulumi api` commands shown here need [Pulumi CLI](/docs/install/) v3.243.0 or later. The API is read-only. Access uses the same permission as [Resource Search](/docs/insights/discovery/search/), so if you can search resources in the console today, you can query the graph. Results are trimmed to the caller's permissions at every step of a query, so a more restricted caller sees less. While the API is in preview the contract can still change; any breaking change will be announced in the [changelog](/releases/) before it ships.

## The graph will grow

This launch is the first step in a larger effort to make everything Pulumi knows about your infrastructure available as context, wherever you need it. The graph vocabulary is designed to grow without breaking existing consumers. In the future, we plan to bring in more of what Pulumi knows, including [Pulumi ESC](/docs/esc/) environments (trace which stacks a configuration or secret change reaches), teams and roles (who owns what), cloud accounts, and service catalog concepts from [Pulumi IDP](/docs/idp/), our internal developer platform.

## Get started

If your organization uses [Neo](/product/neo/), skip the steps and just ask it a question. For any other agent:

1. Fetch the primer: `pulumi api GetGraphSchema -F orgName=<your-org>`. The primer is the reference documentation, served by the API itself, so it's always in sync with the deployment answering your queries.
1. Hand it to your favorite agent.
1. Ask a question: tell your agent in plain English what you want to know, or compose a query from the primer's examples and run it with `pulumi api GraphQuery -F orgName=<your-org> --input query.json`.

The [Context API documentation](/docs/insights/context-api/) covers access, permissions, and worked query recipes if you want more than the primer.

Give it a try today, and share your feedback in the [Pulumi Community Slack](https://slack.pulumi.com/) or through your account team. Your feedback will guide what we prioritize next, especially if there's a question you want answered that the graph doesn't handle yet.
