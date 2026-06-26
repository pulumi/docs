---
title_tag: "Deployment Triggers | Pulumi Deployments"
meta_desc: Learn how to configure and use Deployment Triggers for Pulumi Deployments
title: "Deployment Triggers"
h1: "Deployment Triggers"
aliases:
- /docs/deployments/deployments/using/triggers/
- /docs/pulumi-cloud/deployments/using/triggers/
menu:
  deployments:
    name: Deployment Triggers
    parent: deployments-concepts
    identifier: deployments-concepts-triggers
    weight: 30
---

A deployment trigger is how a Pulumi Deployment gets initiated. Some triggers are configured in a stack's [deployment settings](/docs/deployments/concepts/settings/) and fire automatically in response to source events; others start a deployment on demand. This page describes each trigger and links to where it is configured.

- **[Push to deploy](#push-to-deploy):** run a `pulumi preview` on a pull request, a `pulumi up` when commits merge to a branch, or a `pulumi up` when a matching git tag is pushed.
- **[Click to Deploy](#click-to-deploy):** run an operation on demand from the Pulumi Cloud console.
- **[REST API](#rest-api):** start a deployment programmatically, with settings supplied in the request.
- **[Scheduled operations, drift, and TTL](#scheduled-operations-drift-and-ttl-stacks):** run operations on a schedule, on a recurring drift check, or at a stack's time to live.
- **[Review stacks](#review-stacks):** stand up an ephemeral stack for each pull request.
- **[Deployment webhooks](#deployment-webhooks):** trigger a deployment on another stack in response to an event.

## Deployment operations

Each Pulumi Deployment runs a single operation — a `pulumi` CLI command. Pulumi Deployments supports:

- **Update:** `pulumi up` to create or update stack resources.
- **Preview:** `pulumi preview` to review changes without applying them.
- **Refresh:** `pulumi refresh` to reconcile your stack's state with your cloud provider.
- **Destroy:** `pulumi destroy` to delete all resources in the stack.
- **Detect drift:** refresh state and fail if any changes are detected.
- **Remediate drift:** refresh state and re-apply your program so resources match its declared state (`pulumi up --refresh`).

Not every operation is available for every trigger. For background on drift, see [Detecting and reconciling drift](/docs/iac/operations/stack-management/drift/).

## Push to deploy

When a stack uses a [version control integration](/docs/integrations/version-control/) as its source, pushes to your repository can trigger deployments automatically: a `pulumi preview` when a pull request is opened, a `pulumi up` when commits merge to the configured branch, and a `pulumi up` when a matching git tag is pushed. These triggers — and the toggles and filters that control them — are configured in the stack's deployment settings. See [Source settings](/docs/deployments/concepts/settings/#source-settings), [Path Filtering](/docs/deployments/concepts/settings/#path-filtering), and [Tag Filtering](/docs/deployments/concepts/settings/#tag-filtering).

## Click to Deploy

You can run a deployment on demand from the Pulumi Cloud console using the **Deploy** menu on a stack. Click to Deploy lets you choose which [operation](#deployment-operations) to run, but it always uses the stack's saved [deployment settings](/docs/deployments/concepts/settings/) — you cannot override them for a single run.

## REST API

The Pulumi Deployments REST API starts a deployment programmatically with a `POST` request. Unlike the other triggers, the request body carries the deployment settings: a stack does not need any saved settings — you can supply them entirely in the request — and if the stack does have saved settings, you can override any of them per request. This makes the REST API the way to run a deployment with arbitrary, one-off settings.

For the endpoint and request schema, see [Create deployment](/docs/reference/cloud-rest-api/deployments/#post-apistacksorgnameprojectnamestacknamedeployments) in the Pulumi Deployments REST API docs.

## Scheduled operations, drift, and TTL stacks

These triggers run operations on a time basis rather than in response to a source event:

- **[Scheduled operations](/docs/deployments/concepts/schedules/):** run any operation on a recurring (cron) schedule.
- **[Drift detection](/docs/deployments/concepts/drift/):** a scheduled detect-drift (and optional remediate-drift) run.
- **[TTL stacks](/docs/deployments/concepts/ttl/):** a one-time `pulumi destroy` at a stack's time to live.

## Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) are ephemeral environments created automatically for each pull request and destroyed when it closes. They are enabled through deployment settings (the **Use this stack as a template for pull request stacks** toggle).

## Deployment webhooks

A [deployment webhook](/docs/deployments/concepts/webhooks/#deployment-webhooks) triggers a deployment on another stack in response to an event — for example, updating a dependent stack when an upstream stack (referenced via a [stack reference](/docs/iac/concepts/stacks/#stackreferences)) changes, or promoting a change from a lower environment to a higher one. A deployment webhook runs the target stack using that stack's existing [deployment settings](/docs/deployments/concepts/settings/); it cannot override them. To trigger a deployment with custom or one-off settings, use the [REST API](#rest-api) instead.

The [Pulumi Auto Deploy package](/registry/packages/auto-deploy) (currently in Preview) lets you manage dependent stack updates declaratively.
