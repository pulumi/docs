---
title_tag: Manage Pulumi Delivery runs and stages
meta_desc: Retry a failed Pulumi Delivery run, cancel an active one, and roll back, redeploy, force-promote, or pause a stage.
title: Runs and stages
h1: Manage runs and stages
menu:
  delivery:
    name: Runs and stages
    parent: delivery-operations
    weight: 10
aliases: []
---

Delivery never retries a member on its own. When something goes wrong, a person decides what happens next, either from the run page in the Pulumi Cloud console or through the REST API.

## Retry a failed run

Fix the cause first, for example by creating a missing target stack. Then retry:

```bash
curl -X POST \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/runs/<run-number>/retry
```

A retry reruns only the members that failed. Members that succeeded keep their results. Because a `Stacks` group is one unit, a retry reruns every entry in a group where one entry failed.

A retry uses the same commit, recorded values, and release as the original run. A fix you push afterward doesn't reach the retry, but a fix outside the repository, such as creating a missing stack, does.

You can retry only a failed run. If a newer release has since deployed to the failed member's stage, a newer run is waiting for that stage, or the run stack is gone, [roll back](#operate-a-stage) instead.

## Cancel an active run

You can cancel a run while a gate is waiting or a member is running:

```bash
curl -X POST \
    -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
    https://api.pulumi.com/api/preview/stacks/acme/shop-delivery/main/delivery/runs/<run-number>/cancel
```

The run shows as canceled right away, but an update in progress can take a few minutes to stop. Wait for it to end before you start recovering its stack, which might need a `pulumi refresh`.

## Operate a stage

These actions each create a new run for one stage. That run reuses the release, recorded values, and outputs of an earlier run rather than reading the latest ones, and it skips the stage's gate.

Roll back
: Deploys an earlier release that previously reached the stage, then pauses the stage. Newer runs wait until you resume it.

Redeploy
: Deploys the stage's current release again.

Force-promote
: Moves a release into the stage.

Pause and resume
: Pausing stops the stage from admitting new runs. A run that already holds the stage keeps it. Resuming lets the stage admit runs again.

Use the console, or the REST API routes under `/api/preview/stacks/<org>/<project>/<stack>/delivery/stages/<stage>/`.

<!-- TODO(launch): Add the exact route for each stage action and a console screenshot of the stage menu. Confirm the definition-list syntax renders well on the docs theme; switch to a list if not. -->

These actions need a user token with write access to the pipeline stack. See [Permissions](/docs/delivery/operations/permissions/).
