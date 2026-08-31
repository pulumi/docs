---
title: "Query your infrastructure with the Pulumi Context API"
date: 2026-08-26
meta_desc: "The Pulumi Context API is now in public preview: a queryable graph spanning IaC state, stack dependencies, and discovered cloud resources."
authors:
    - levi-blackstone
editions:
    - enterprise
    - business-critical
---

The Pulumi Context API is now available in public preview. It connects everything Pulumi knows about your infrastructure, the resources your programs manage, the dependencies between them, how stacks consume each other's outputs, and the resources [Discovery](/docs/insights/discovery/) finds in your cloud accounts, into a queryable graph.

[Pulumi Neo](/product/neo/) uses the Context API out of the box. Any other agent, including Claude Code, Codex, and Cursor, learns what it needs to get started with a Markdown document served by the graph API.

Check out the [announcement blog post](/blog/pulumi-context-api/) for the full story.
