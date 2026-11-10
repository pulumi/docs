---
title_tag: Pulumi Delivery permissions
meta_desc: Who can register Pulumi Delivery pipelines, dispatch runs, approve and continue gates, and operate stages, and what the Delivery identity can reach.
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

## Protect the pipeline program's branch

Write access to the branch that holds the pipeline program gives deploy access to every stack your organization's Delivery identity can reach. Protect that branch with the same review rules you'd use for production infrastructure code.

Approval previews run with the same credential as updates, so only people with write access to the repository can add code that runs during a preview.

<!-- TODO(launch): Explain what "the Delivery identity of the organization" is, where it's configured, and how to scope it (DLV-434). -->

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

{{< pulumi-cloud "delivery-approvals" />}}

An approval gate lists `approvers` by Pulumi username or team name. Anyone in that list can approve, including the person who started the run or pushed the commit. If the list is empty, anyone with update permission on the organization can approve.

<!-- TODO(launch): Confirm whether self-approval can be disabled at GA, and whether approvals respect custom roles. -->

## Reading upstream pipelines

When a pipeline reads another with a `PipelineSource`, your organization's Delivery identity needs read access to the upstream pipeline stack. Your own access isn't enough.
