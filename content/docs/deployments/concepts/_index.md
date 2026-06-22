---
title: Concepts
title_tag: "Pulumi Deployments"
h1: "Pulumi Deployments"
meta_desc: What Pulumi Deployments is, why it exists, and an overview of its core concepts.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    parent: deployments-home
    identifier: deployments-concepts
    weight: 10
aliases:
- /docs/deployments/concepts/introduction/
- /docs/deployments/deployments/
- /docs/pulumi-cloud/deployments/
- /docs/platform/deployments/
- /docs/intro/pulumi-service/deployments/
- /docs/intro/deployments/
- /docs/intro/deployments/platform/
- /docs/pulumi-cloud/deployments/platform/
- /docs/pulumi-cloud/deployments/using/
- /docs/pulumi-cloud/deployments/using-deployments/
- /docs/deployments/deployments/reference/
- /docs/pulumi-cloud/deployments/reference/
- /docs/platform/deployments/reference/
- /docs/intro/deployments/reference/
---

Pulumi Deployments is a managed service that runs Pulumi operations — `pulumi up`, `preview`, `refresh`, and `destroy` — on Pulumi-hosted or self-hosted compute rather than on a developer's machine. You configure how a stack should be deployed once, and Pulumi Cloud runs those operations for you: on demand, in response to version control events, on a schedule, or through the REST API.

## Why Pulumi Deployments exists

Running infrastructure updates from local machines or hand-built CI pipelines is hard to keep consistent and secure. Every engineer needs cloud credentials, the toolchain has to be installed and version-pinned, and there is no shared record of what ran or who ran it.

Pulumi Deployments moves that work into a managed, isolated environment that already has the Pulumi CLI and language runtimes installed. Cloud credentials and secrets are supplied through [Pulumi ESC](/docs/pulumi-cloud/esc) and OIDC instead of living on laptops or in pipeline configuration, deployments can run automatically from your [version control system](/docs/integrations/version-control/), and every run is recorded in Pulumi Cloud. A stack's [deployment settings](/docs/deployments/concepts/settings/) capture everything a run needs — source location, credentials, environment variables, and build requirements — so the same deployment behaves the same way no matter what triggers it.

## In this section

- **[Deployments Settings](/docs/deployments/concepts/settings/)** — the per-stack configuration that defines how a deployment runs: source, credentials, environment variables, path and tag filters, and runner pool.
- **[Deployment Triggers](/docs/deployments/concepts/triggers/)** — the ways a deployment is initiated, including the console's Click to Deploy, the REST API, and webhooks.
- **[Drift Detection](/docs/deployments/concepts/drift/)** — detecting when deployed infrastructure no longer matches your Pulumi program, and optionally remediating it on a schedule.
- **[TTL Stacks](/docs/deployments/concepts/ttl/)** — automatically destroying a stack at a set time, for temporary or ephemeral environments.
- **[Review Stacks](/docs/deployments/concepts/review-stacks/)** — ephemeral environments stood up automatically for each pull request and torn down when it closes.
- **[Scheduled operations](/docs/deployments/concepts/schedules/)** — running any Pulumi operation on a recurring schedule.
- **[Pulumi-managed runners](/docs/deployments/concepts/pulumi-managed-runners/)** — the Pulumi-hosted compute that runs deployments by default, including its hardware and image.
- **[Customer-managed runners](/docs/deployments/concepts/customer-managed-runners/)** — self-hosting that compute on your own infrastructure.
- **[Webhooks](/docs/deployments/concepts/webhooks/)** — notifying external systems, or triggering other stacks, in response to events in your Pulumi organization.

For task-oriented walkthroughs — supplying cloud credentials, building custom images, configuring OIDC, and more — see the [Deployments guides](/docs/deployments/guides/).

## Getting started

To start using Pulumi Deployments:

1. Create a new project with the Pulumi Cloud [New Project Wizard](/docs/idp/concepts/new-project-wizard), which configures Deployments for your repository automatically, or
1. Follow the [Getting Started guide](/docs/deployments/get-started/) to set it up on an existing project.
