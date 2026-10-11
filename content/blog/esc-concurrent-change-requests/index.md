---
title: "Concurrent change requests in Pulumi ESC"
date: 2026-10-07
draft: false
meta_desc: "Multiple people can now open change requests on the same Pulumi ESC environment at the same time."
feature_image: feature.png
authors:
    - sean-yeh
tags:
    - esc
    - features
category: product
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: |
        Pulumi ESC environments no longer have a single-change-request bottleneck. Multiple teammates can now propose changes to the same environment at once. Each gets its own review, and you can rebase onto the latest revision in one click.
    linkedin: |
        Pulumi ESC environments no longer have a single-change-request bottleneck. Multiple teammates can now propose changes to the same environment at once. Each gets its own review, and you can rebase onto the latest revision in one click.
    bluesky: |
        Pulumi ESC environments no longer have a single-change-request bottleneck. Multiple teammates can now propose changes to the same environment at once. Each gets its own review, and you can rebase onto the latest revision in one click.
---

With [ESC Approvals](/docs/esc/concepts/approvals/), you can propose, review, and apply environment changes with change requests. Until now, an environment could only have one open change request at a time. If a teammate's change was waiting for review, others were blocked from opening change requests.

Today, multiple people can open change requests on the same environment at the same time. A platform engineer can rotate a database credential while an app team adds a new feature flag, and each change goes through its own review. You no longer need to wait on your teammates' changes!

<!--more-->

## How it works

### Creating and viewing change requests in the Pulumi Cloud console

Creating environment change requests works the same as before - just edit an environment that has approvals enabled, and click "Create Draft" once ready, which opens a change request for your teammates to review. You can view all change requests for the environment from either the version dropdown or the Approvals tab.

![The version dropdown listing two pending drafts by different users above the environment's revisions](revision-picker-drafts.png)

![The Approvals tab listing two pending change requests from different users](approvals-tab-change-requests.png)

### Updating to the latest revision

If another change request gets applied first, yours is now based on an older revision. This is nothing to worry about - just click "Update to latest revision" and your changes are reapplied on top of the latest revision (using a 3-way merge).

![A warning banner reading "This change request is out of date" with an Update to latest revision button](change-request-out-of-date.png)

If there is a merge conflict, the console will show which lines conflict. You can resolve this by either editing the draft or recreating the change request.

![An error banner reading "This change request cannot be updated automatically" listing a conflict at line 7, with a Close change request button](change-request-merge-conflict.png)

## Get started

Concurrent change requests are available today in Pulumi Cloud on the [Pro and Enterprise editions](/pricing/), for any environment with approvals enabled. To get started, see the [Approvals documentation](/docs/esc/concepts/approvals/).

Let us know what you think in the [Pulumi Community Slack](https://slack.pulumi.com/)!
