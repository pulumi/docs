---
title_tag: Pulumi Delivery permissions
meta_desc: Who can register Pulumi Delivery pipelines, dispatch runs, approve and continue gates, and operate stages, and which service principal a pipeline runs as.
title: Permissions
h1: Permissions
menu:
  delivery:
    name: Permissions
    parent: delivery-operations
    weight: 20
aliases: []
---

A pipeline deploys on your behalf, so who can change it and who can move a release through it matter as much as the code. This page covers both.

## The identity a pipeline runs as

Each pipeline runs as a Pulumi Cloud service principal. Every step in every stage of the pipeline uses that one identity, so it's what decides which stacks and ESC environments a run can reach.

You can choose an existing service principal for the pipeline in the pipeline program. If you don't, Delivery creates one when you register the pipeline and gives it access to the pipeline's target stacks only. Before it does, Delivery checks that you have access to those stacks yourself, so registering a pipeline can't give it more access than you have. The same check applies when you choose an existing service principal: you need at least the permissions it has.

To give a pipeline access to more stacks or environments, grant them to its service principal. You can see which service principal a pipeline uses on the pipeline's page in the Pulumi Cloud console.

A pipeline uses the same service principal for all of its stages.

<!--
TODO(launch): DLV-434 (Boris Schlosser) is still being finalized. Before 2026-11-18, confirm:
- The pipeline program property that selects a service principal, and add a code example.
- Whether the created service principal is made at registration or at the first run, and what it's named.
- How to grant it more access (entity assignments?) and link the Pulumi Cloud service principal and RBAC docs once they exist.
- Whether the pipeline page in the console shows the service principal at launch (today's notes list it as a follow-up).
-->

## Protect the pipeline program's branch

Write access to the branch that holds the pipeline program lets someone change what the pipeline deploys, using everything its service principal can reach. Protect that branch with the same review rules you'd use for production infrastructure code.

Approval previews run with the same credential as updates, so only people with write access to the repository can add code that runs during a preview.

## Who can do what

| Action | Who can do it |
| --- | --- |
| Dispatch a run | Any credential with write access to the pipeline stack |
| Continue a manual gate | Any credential with write access to the pipeline stack |
| Approve an approval gate | A user token with read access to the pipeline stack, from someone listed in the gate's `approvers` |
| Retry or cancel a run | A user token with write access to the pipeline stack |
| Pause, resume, promote, roll back, or redeploy a stage | A user token with write access to the pipeline stack |

Organization and team access tokens can dispatch runs and continue manual gates, but they can't retry, cancel, or operate stages.

## Who can approve a gate

<!-- TODO(launch): Replace the next sentence with the pulumi-cloud shortcode for "delivery-approvals" once pulumi/marketing-web adds a hidden `delivery-approvals` feature (min_edition: pro). -->

Approval gates are available in the Pro and Enterprise editions.

An approval gate lists `approvers` by Pulumi username or team name. Anyone in that list can approve, including the person who started the run or pushed the commit. If the list is empty, anyone with update permission on the organization can approve.

<!-- TODO(launch): Confirm whether self-approval can be disabled at GA, and whether approvals respect custom roles. -->

## Reading upstream pipelines

When a pipeline reads another with a `PipelineSource`, the downstream pipeline's service principal needs read access to the upstream pipeline stack. Your own access isn't enough.
