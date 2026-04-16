---
title: "Pulumi Cloud REST API Docs, Now Generated from OpenAPI"
date: 2026-04-16
draft: false
meta_desc: "The Pulumi Cloud REST API reference at /docs/reference/cloud-rest-api/ is now generated directly from the live OpenAPI spec, so it stays in sync with the API."
meta_image: meta.png
feature_image: feature.png
authors:
    - devon-grove
tags:
    - pulumi-cloud
    - features
    - api
social:
    twitter: "The Pulumi Cloud REST API reference is now generated from our live OpenAPI spec. Same URL, always in sync with the API, with full schema docs and cross-linked endpoints."
    bluesky: "The Pulumi Cloud REST API reference is now generated from our live OpenAPI spec. Same URL, always in sync with the API, with full schema docs and cross-linked endpoints."
    linkedin: "Our REST API reference docs at /docs/reference/cloud-rest-api/ are now generated from the live OpenAPI spec. Endpoints, parameters, request and response schemas all track the real API, so the docs no longer drift from reality."
---

The [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/) is now generated directly from the live [OpenAPI spec](https://api.pulumi.com/api/openapi/pulumi-spec.json) at build time. Every endpoint, parameter, request body, and response schema you see on the page comes from the same spec the API itself publishes. The docs now stay in sync with the API automatically!

<!--more-->

## Why this matters

The previous REST API reference was a set of handwritten pages. That meant every new endpoint, renamed parameter, or revised response shape needed a matching docs PR, and in practice the pages drifted. Small inconsistencies added up: missing parameters, outdated request shapes, schemas that no longer matched what the API returned. We've heard feedback in this area, and wanted to respond with a durable solution for docs accuracy that will scale with us.

Generating the reference from the OpenAPI spec closes that gap. When the API ships a change, the docs pick it up automatically the next time our docs are built.

## What's new

The reference at `/docs/reference/cloud-rest-api/` now includes:

1. **One page per API category**, generated from the OpenAPI tags: Stacks, Deployments, Environments, Organizations, Registry, Insights, AI, Workflows, and more. Each page lists every endpoint under that tag with its method, path, parameters, request body, and response schemas.
1. **A full [schema reference](/docs/reference/cloud-rest-api/schema/)** covering every component in the spec, several hundred in all. Parameter and response types link directly to their schema definitions, so you can follow a `stackReference` field straight to the full object shape.
1. **Cross-linked schemas.** When an endpoint returns a complex type, the type name is a link, so you can jump straight to the definition instead of scrolling a giant single page.
1. **Editorial intros per tag.** Each category page has a short, handwritten intro above the endpoint list explaining what the API area is for and when to use it. These live in the repo at [`assets/openapi/tag-intros/`](https://github.com/pulumi/docs/tree/master/assets/openapi/tag-intros); send a PR to improve the framing or add context.

## Same URL, existing links keep working

The generated docs live at the same URL as the previous reference: `/docs/reference/cloud-rest-api/`. Bookmarks, blog links, and inbound search traffic still land on the right page. Aliases are in place for every old subpage path, so links like `/docs/reference/cloud-rest-api/webhooks/` redirect to the new index.

One caveat: deep anchor links into the old single-page structure (for example `#data-export`) won't scroll to a matching heading anymore, because endpoints now live on per-tag pages. Those links still reach the reference — they just land on the index rather than a specific heading.

## Try it out

Start at the new [REST API reference](/docs/reference/cloud-rest-api/) and browse by category, or jump straight to the [schema reference](/docs/reference/cloud-rest-api/schema/) if you want to see every component in one place.

If you spot anything that looks wrong, the most likely culprit is the OpenAPI spec itself — file an issue and we'll trace it back to the source. For tag intros and structural improvements, PRs to [pulumi/docs](https://github.com/pulumi/docs) are welcome. Questions and feedback are always welcome in the [Pulumi Community Slack](https://slack.pulumi.com).

{{< blog/cta-button "Explore the REST API" "/docs/reference/cloud-rest-api/" >}}
