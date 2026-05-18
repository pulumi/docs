---
title: "Agent-Friendly Markdown Docs for Pulumi Providers and Components"
allow_long_title: true
date: 2026-05-19
draft: false
meta_desc: "Public Pulumi Cloud registry endpoints serve READMEs, nav, per-resource docs, and examples for any package version. Markdown or JSON, via `pulumi api`."
meta_image: meta.png
feature_image: feature.png
authors:
    - idp-team
tags:
    - features
    - pulumi-cli
    - registry
    - ai
schema_type: auto

social:
    twitter: |
        Five new public endpoints on the Pulumi Cloud registry serve docs for any package version, including private ones over pulumi api.

        Query params tune the output: lang, os, depth, limit, search.
    linkedin: |
        We've made five Pulumi Cloud registry documentation endpoints public: READMEs, installation guides, navigation trees, per-resource docs, and aggregated examples for any package version.

        The marketing registry already serves markdown variants of its pages, which works well for public packages and the versions we publish there. The cloud registry endpoints fill in two gaps: every published version is addressable, and pulumi api reuses your CLI auth to reach private packages.

        Query parameters tune the response: lang to filter to one language, os for OS choosers, q + depth=full to search the nav tree, limit on examples. pulumi package add now prints a copy-pasteable pulumi api pointer when it detects an AI coding agent.
    bluesky: |
        Five new public endpoints on the Pulumi Cloud registry serve docs for any package version, including private ones over pulumi api.

        pulumi package add now prints a copy-pasteable pointer when it detects an AI coding agent.
---

Coding agents and CLI users need to see what's inside a Pulumi package: READMEs, installation guides, navigation trees, per-resource docs, examples. They need it pinned to the version the project actually uses, filterable to one language, and reachable over the same auth as the CLI, so private packages work the same way as public ones. Five Pulumi Cloud registry documentation endpoints flipped from Preview to Public this month to make that work for every published package. The schemas are in the [Pulumi Cloud REST API reference](/docs/reference/cloud-rest-api/registry/). Every published version of every package is addressable, and private packages resolve through the CLI's existing auth via `pulumi api`.

<!--more-->

## How to use them now

The examples below use [`pulumi api`](/docs/iac/cli/api/), available in Pulumi CLI v3.238.0 and later. See [Download & Install Pulumi](/docs/install/) if you need to upgrade.

The five endpoints share a version-pinned prefix:

```text
/api/registry/packages/{source}/{publisher}/{name}/versions/{version}
```

With these suffixes:

- [`/readme`](/docs/reference/cloud-rest-api/registry/#get-apiregistrypackagessourcepublishernameversionsversionreadme): package overview.
- [`/installation`](/docs/reference/cloud-rest-api/registry/#get-apiregistrypackagessourcepublishernameversionsversioninstallation): installation and configuration guide; returns 404 when the package doesn't ship one.
- [`/nav`](/docs/reference/cloud-rest-api/registry/#get-apiregistrypackagessourcepublishernameversionsversionnav): navigation tree of modules, resources, and functions.
- [`/docs/{token}`](/docs/reference/cloud-rest-api/registry/#get-apiregistrypackagessourcepublishernameversionsversiondocstoken): structured docs for a single resource or function, keyed by Pulumi token.
- [`/examples`](/docs/reference/cloud-rest-api/registry/#get-apiregistrypackagessourcepublishernameversionsversionexamples): code examples across the package, filterable and paginated.

Each accepts `Accept: application/json` (the default) or `Accept: text/markdown`.

`pulumi api` reuses whatever auth `pulumi login` set up, so private packages and public ones work the same way:

```bash
# README for random@4.19.1 as Markdown, in Python
pulumi api --output=markdown \
    '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/readme?lang=python'

# Navigation tree, filtered to password resources
pulumi api '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/nav?q=password&depth=full'

# Per-resource docs for random:index/randomPassword:RandomPassword
pulumi api --output=markdown \
    '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/docs/random%3Aindex%2FrandomPassword%3ARandomPassword?lang=python'
```

Public packages are also reachable without authentication, so a quick check from anywhere works:

```bash
curl -H "accept: text/markdown" \
     'https://api.pulumi.com/api/registry/packages/pulumi/pulumi/random/versions/latest/readme?lang=python'
```

Pulumi tokens are RFC 3986 path segments, so `:` and `/` need to be escaped when used in a URL. Both percent-encoded (`random%3Aindex%2FrandomPassword%3ARandomPassword`) and partially-escaped (`random:index%2FrandomPassword:RandomPassword`) forms work.

Resolved-version responses (anything that isn't `latest`) are immutable and carry a one-day `Cache-Control` header.

## The CLI points agents at these endpoints

`pulumi package add` and `pulumi package gen-sdk` now print a docs pointer when they detect they're running inside an AI coding agent (Claude Code, Cursor, Codex, Aider, and so on):

```text
Added package random
Documentation:
  pulumi api --output=markdown '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/readme'                    # package readme
  pulumi api --output=markdown '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/nav'                       # doc tree (modules)
  pulumi api --output=markdown '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/nav?q=<term>&depth=full'   # search for resources/functions
  pulumi api --output=markdown '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/docs/<token>'              # one resource or function (token from /nav)
```

Each line is copy-pasteable on its own. The agent can pull the README, walk the nav, search for a resource, or fetch a single resource's docs, all pinned to the version it just installed. If the install fails because the package doesn't exist, the CLI wraps the error with a `pulumi api '/api/registry/packages?search=<term>'` hint so the agent can recover by searching the registry.

Humans see the unchanged install output. The hint only appears when the CLI detects an agent environment, and the same path resolution drives both the install and the docs URL, so private and community packages get their actual canonical path, not a hardcoded `pulumi/pulumi`.

## What this means for Neo

[Neo](/docs/ai/), Pulumi's own coding agent, is the first-party consumer of these endpoints. Neo already had access to predecessor endpoints, but those returned more data than the agent needed for a given question and only spoke JSON. The new endpoints let Neo pull a per-resource doc in the one language the project uses, as Markdown, scoped to the version of the package it's working with, whether public or private.

## Tuning the response with query parameters

Filter `/readme` to one language and OS, and the code choosers collapse to plain prose:

```bash
pulumi api --output=markdown \
    '/api/registry/packages/pulumi/pulumi/random/versions/4.19.1/readme?lang=python&os=linux'
```

`/nav` defaults to a summary shape: modules with `resourcesTotal` and `functionsTotal` counts but no inline lists. Pass `?depth=full` for the whole tree, or layer `?q=lambda&depth=full` to get matching resources and functions inlined with their tokens. `/examples` takes `?q=` and `?limit=` directly: a single `aws` request can pull all 1,189 examples, or `?limit=10&q=alias` can pull the first ten matching ones.

`/docs/{token}` accepts `?lang=` to pin the language across names, types, descriptions, and code samples in one go. Cross-type references come back as `typeRef` objects with the target token (and, for cross-package refs, package and version), which clients turn directly into the next URL to fetch.

## Why Markdown for agents

`Accept: application/json` gives a parseable tree with structured fields. `Accept: text/markdown` gives prose the same shape the response would render to. For an LLM consuming the response into a context window, Markdown is the native format: no JSON parsing, no client-side filtering, just text the model reads directly. It's also consistently smaller than the equivalent JSON, because the JSON shape carries the same content plus structural keys, language maps, and content-node metadata:

| Package      | Endpoint                  | JSON     | Markdown | Tokens saved |
| ------------ | ------------------------- | -------- | -------- | ------------ |
| random       | `/readme`                 | 10.68 KB | 6.04 KB  | 43%          |
| aws          | `/readme`                 | 4.22 KB  | 2.54 KB  | 40%          |
| aws          | `/nav?depth=full`         | 204 KB   | 170 KB   | 17%          |
| aws          | `/docs/{resource token}`  | 15.24 KB | 11.28 KB | 26%          |
| azure-native | `/docs/{resource token}`  | 48.13 KB | 30.37 KB | 37%          |
| aws          | `/docs/{function token}`  | 2.40 KB  | 1.46 KB  | 39%          |

The `/docs/{token}` rows use `aws:accessanalyzer/analyzer:Analyzer`, `azure-native:aad:DomainService`, and `aws:index/getArn:getArn` respectively, all at `?lang=typescript`. `?lang=` filtering compounds the savings for `/docs/{token}` and `/readme` because language-specific names, types, descriptions, and code samples collapse to the requested language only.

For tooling that genuinely needs structured access (type signatures programmatically, deprecation flags, cross-package refs as objects), JSON is still the right format. For an agent consuming docs to write code, Markdown wins on both axes.

## Advertising the Markdown variant

A pattern that's emerged across documentation tooling is to put a `<link rel="alternate" type="text/markdown" href="...">` in the `<head>` of every HTML page that has a Markdown counterpart. An agent fetching the page sees the alternate and follows it for a clean Markdown response. We [shipped that for the docs site](https://github.com/pulumi/docs/pull/18914) recently.

The cloud registry endpoints extend the convention into the API surface. Every JSON response from the five endpoints carries a `Link` header advertising the Markdown twin at the same URL:

```http
Link: </api/registry/packages/pulumi/pulumi/random/versions/4.19.1/docs/random%3Aindex%2FrandomPassword%3ARandomPassword>; rel="alternate"; type="text/markdown"
```

A client that lands on the JSON response discovers, from the header alone, that the same URL serves Markdown when asked with `Accept: text/markdown`. The negotiation runs through a small shared helper in our REST framework: handlers declare which media types they support, and the helper parses the client's `Accept` header (including `q=` weights, comma-separated alternatives, and `*/*` wildcard) to pick one. An unsupported `Accept` value returns 406 with a list of what works.

On the discovery side, we reorganized [llms.txt](https://www.pulumi.com/llms.txt) to lead the "For agents" block with the cloud registry API, so an agent consuming the standard llms.txt file lands on these endpoints first, with copy-pasteable `pulumi api` and `curl` examples right there.

If you build with these endpoints, or your agent uses them, we'd like to hear about it in the [Community Slack](https://slack.pulumi.com/) or on [GitHub](https://github.com/pulumi/pulumi/issues).
