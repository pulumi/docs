---
title: "Query your resource graph with the Insights graph query API"
date: 2026-08-18
meta_desc: Pulumi Insights adds a graph query API for traversing the relationships across your cloud resources, built with coding agents in mind.
authors:
    - christian-nunciato
# TODO(christian): confirm edition availability before publishing (this API is
# entitlement-gated). List the lowest applicable edition and every edition above it.
# editions:
#     - enterprise
#     - business-critical
---

<!-- DRAFT — pending confirmation of GA status, entitlement/editions, and a public
     docs link before this is published. -->

Pulumi Insights now includes a graph query API for exploring the relationships across your cloud resources. Rather than scanning stacks one at a time, you can query the resource graph directly — traverse dependencies and references, filter on resource properties (including semantic-version comparisons), and get results automatically trimmed to what you're allowed to see.

It's also built with agents in mind: the API's schema endpoint serves a primer and cookbook, so a coding agent can learn the query surface and explore your graph on its own.

<!-- TODO(christian): link the Insights graph query API documentation here once it's
     published, and confirm the edition/entitlement note above. -->
To learn more, see the [Pulumi Insights documentation](/docs/insights/).
