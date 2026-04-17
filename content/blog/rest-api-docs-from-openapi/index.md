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
    twitter: |
        If you called a Pulumi Cloud REST API endpoint and got back a field the docs never mentioned, that was real drift. The reference was hand-maintained and the API kept moving.

        We changed how it's built. Here's what's different.
    bluesky: |
        If you called a Pulumi Cloud REST API endpoint and got back a field the docs never mentioned, that was real drift. The reference was hand-maintained and the API kept moving.

        Here's how we fixed it.
    linkedin: |
        If you've ever integrated with the Pulumi Cloud REST API and found a parameter the docs never mentioned, or a response field that wasn't in the schema, that was real drift, not your reading.

        The old reference was handwritten. Every endpoint change, renamed parameter, or revised response shape needed a matching docs PR. In practice those PRs didn't always land, and small mismatches compounded over time.

        We changed how the reference is built. The pages at the same URL are now generated from the live OpenAPI spec the API itself publishes.

        We wrote up what's different and what it means for anyone integrating with the API today.
---

The [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/) is now generated directly from the live [OpenAPI spec](https://api.pulumi.com/api/openapi/pulumi-spec.json) at build time. Every endpoint, parameter, request body, and response schema you see on the page comes from the same spec the API itself publishes. The docs now stay in sync with the API automatically!

<!--more-->

## Why this matters

The previous REST API reference was a set of handwritten pages. That meant every new endpoint, renamed parameter, or revised response shape needed a matching docs PR, and in practice the pages drifted. Small inconsistencies added up: missing parameters, outdated request shapes, schemas that no longer matched what the API returned. We wanted a durable fix that keeps the docs in sync as the API grows.

Generating the reference from the OpenAPI spec closes that gap. When the API ships a change, the docs pick it up automatically the next time our docs are built.

## What's new

The reference at `/docs/reference/cloud-rest-api/` now includes:

1. Find what you need faster
    * Endpoints are grouped by product area — Stacks, Deployments, Environments, Organizations, Registry, Insights, AI, Workflows, and more — so you can jump straight to the part of the API you're working with.
1. Complete request and response details
    * Every endpoint documents its parameters, request body, and the exact shape of what it returns, so you know what to send and what to expect back without guessing.
1. One-click navigation between related types
    * When a response references another object, the type name is a link. Click through to drill into its full definition if desired instead of scrolling a lengthy API reference page.

## What this unlocks for agents

Keeping the reference in sync with the spec isn't just a human convenience. It changes what's reliable for AI agents that read the docs and call the API on your behalf. An agent reading a handwritten reference might see a parameter that was renamed six months ago, or miss a field the API now returns, and the call fails silently or in ways that are hard to debug. When the reference is generated from the spec, the agent is working from what the API actually accepts today.

Say you're onboarding a new team and need to stand up their access in Pulumi Cloud. Point an agent at the REST API reference and ask it to create an `sre-oncall` team, add four members, and grant admin on three stacks. The agent walks the teams, memberships, and stack-permissions endpoints, builds the right sequence of calls, and executes.

The same pattern holds for bulk audits and cleanup. Ask an agent to find every stack in your org with no recent updates and tag them `stale`, and it can paginate correctly because the response schema matches reality. While workflows like these were technically possible before, they're much more reliable now.

## Same URL, existing links keep working

The generated docs live at the same URL as the previous reference: `/docs/reference/cloud-rest-api/`. Bookmarks, blog links, and inbound search traffic still land on the right page. Redirects are in place for any API reference docs page that has been tweaked, renamed, or moved.

## Try it out

Start at the new [REST API reference](/docs/reference/cloud-rest-api/) and browse by category. Each page links through to the request and response object schemas it uses.

If you spot anything that looks wrong, the most likely culprit is the OpenAPI spec itself — file an issue in [pulumi/docs](https://github.com/pulumi/docs) and we'll trace it back to the source. For tag intros and structural improvements, PRs to [pulumi/docs](https://github.com/pulumi/docs) are welcome. Questions and feedback are always welcome in the [Pulumi Community Slack](https://slack.pulumi.com).

{{< blog/cta-button "Explore the REST API" "/docs/reference/cloud-rest-api/" >}}
