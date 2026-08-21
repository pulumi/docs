---
title: "Query Your Infrastructure with the Pulumi Context API"
date: 2026-08-26
meta_desc: "The Pulumi Context API is now in preview: one queryable graph spanning IaC state, stack dependencies, and cloud resources discovered outside IaC."
authors:
    - levi-blackstone
editions:
    - enterprise
    - business-critical
---

The [Pulumi Context API](/docs/insights/context-api/) is now available in preview. It connects everything Pulumi knows about your infrastructure, the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and the resources [Pulumi Insights](/docs/insights/) discovers in your cloud accounts outside IaC, into a single graph you can query.

[Pulumi Neo](/product/neo/) uses the Context API out of the box. Any other agent, including Claude Code, Cursor, and Codex, can onboard itself; the API's schema endpoint answers in Markdown by default with a primer covering the query grammar and worked examples, so an agent learns the whole system in one request and stays current as the API evolves.

Read the [Context API documentation](/docs/insights/context-api/) to get started, browse the [query recipes](/docs/insights/context-api/recipes/) for common questions, or read the [announcement blog post](/blog/pulumi-context-api/) for the full story.
