---
title: "Manage Pulumi ESC change requests from the CLI"
date: 2026-10-26
draft: false
meta_desc: "The new `pulumi env change-request` commands let you review, approve, and apply Pulumi ESC change requests from the CLI."
authors:
    - sean-yeh
tags:
    - esc
    - pulumi-cli
    - features
category: product
feature_image: feature.png
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

With [ESC Approvals](/docs/esc/concepts/approvals/), changes to a protected environment go through a change request. Teammates can review and approve the change before it's applied.

Today we're introducing the `pulumi env change-request` command to work with change requests from the CLI.

Review changes without switching to the Pulumi Cloud console, script your approval workflows, or let an agent propose a change while a teammate signs off on it.

<!--more-->

## How it works

Let's say your `my-project/prod` ESC environment is set up to require approval on change. Alice wants to scale the app to 3 replicas, so she opens a change request:

```bash
$ pulumi env set my-project/prod app.replicas 3 --draft
```

You're the reviewer. Here's how you'd take it from there.

### Find the change request

List the open change requests for an environment:

```bash
$ pulumi env change-request list --env my-project/prod
┌──────────────────────────────────────┬────────┐
│ ID                                   │ AUTHOR │
├──────────────────────────────────────┼────────┤
│ 3045b80b-9a13-43c3-9f63-59fa1b09e18d │ alice  │
│ 0dace5b4-ef98-4b4c-9a17-627db3662d3f │ bob    │
└──────────────────────────────────────┴────────┘
```

### Review the change

See the details of a change request:

```bash
$ pulumi env change-request get 3045b80b-9a13-43c3-9f63-59fa1b09e18d
ID: 3045b80b-9a13-43c3-9f63-59fa1b09e18d
Environment: acme/my-project/prod
Action: update
Status: pending
Author: Alice <alice>
Created: 2 hours ago
Revision: 1
Base environment revision: 2
Current environment revision: 2
Description:
  Scale up to 3 replicas
Approved: false
  prod-approvers (not satisfied): 0 of 1 approvals
URL: https://app.pulumi.com/acme/esc/my-project/prod?version=3045b80b-9a13-43c3-9f63-59fa1b09e18d
```

See what it changes:

```bash
$ pulumi env change-request diff 3045b80b-9a13-43c3-9f63-59fa1b09e18d
--- acme/my-project/prod@2
+++ draft 3045b80b-9a13-43c3-9f63-59fa1b09e18d
@@ -1,3 +1,3 @@
 values:
   app:
-    replicas: 2
+    replicas: 3
```

### Approve the change

Approve it with a comment. The CLI shows the diff again before you confirm:

```bash
$ pulumi env change-request approve 3045b80b-9a13-43c3-9f63-59fa1b09e18d -m "Looks good"
Change request 3045b80b-9a13-43c3-9f63-59fa1b09e18d will update environment acme/my-project/prod.
...

Do you want to approve this change request? yes
Approved change request 3045b80b-9a13-43c3-9f63-59fa1b09e18d
```

### Apply the change

Once the change request has the required approvals, you or Alice can go ahead and apply it:

```bash
$ pulumi env change-request apply 3045b80b-9a13-43c3-9f63-59fa1b09e18d
Change request 3045b80b-9a13-43c3-9f63-59fa1b09e18d will update environment acme/my-project/prod.
...

Do you want to apply this change request? yes
Applied change request 3045b80b-9a13-43c3-9f63-59fa1b09e18d
```

That's it! Alice's change is now live in `prod`.

## Beyond the basics

- For scripts and agents: pass `--yes` to `approve` and `apply` to skip the confirmation prompt, and `--output json` to get machine-readable output from commands like `list`, `get`, and `apply`.
- **[Concurrent change requests](/blog/esc-concurrent-change-requests/)**: if another change request is applied before yours, run `pulumi env change-request rebase <id>` to update yours to the latest revision.

## Get started

Change requests are available on the Pulumi Cloud [Pro and Enterprise editions](/pricing/). See the [`pulumi env change-request` docs](/docs/iac/cli/commands/pulumi_env_change-request/) to learn more. Give it a try, and let us know what you think in the [Pulumi Community Slack](https://slack.pulumi.com/)!
