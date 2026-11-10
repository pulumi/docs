---
title_tag: Troubleshoot Pulumi Delivery pipelines
meta_desc: Diagnose a Pulumi Delivery run that's stuck or failed, including registration messages, missing stacks, ESC permission errors, and blocked stages.
title: Troubleshooting
h1: Troubleshoot a pipeline
menu:
  delivery:
    name: Troubleshooting
    parent: delivery-operations
    weight: 30
aliases: []
---

<!-- TODO(launch): Ask Engineering and the private preview customers for the top issues they hit, and add them here. Organize by symptom. -->

## Registration didn't start a run

`pulumi up` on the pipeline stack always ends with exit code 10, so check its last message:

- "No run starts because commit abc1234 is not the head of branch main." Push your commit, or pull the latest and register again.
- "No run starts because the checkout has uncommitted changes." Commit and push.
- "No run starts because the update has no git commit." Run `pulumi up` from a Git checkout.

## A run is waiting and nothing is happening

Open the run in the Pulumi Cloud console and look at the stage it's on:

- **A gate is waiting.** An approval gate waits until enough approvers approve. If an approver name doesn't match a user or team, the gate waits forever, so check the spelling in `approvers`.
- **The stage is paused.** A rollback pauses its stage. [Resume the stage](/docs/delivery/operations/runs-and-stages/#operate-a-stage) to let newer runs in.
- **Another run holds the stage.** A stage deploys one run at a time. Your run moves once the earlier one finishes.
- **A `Stacks` group is larger than your concurrency limit.** Each entry uses one slot of your organization's concurrency limit, and a group with more entries than the limit can block itself. Delivery fails it after 2 hours without progress. Split the group.
- **Stages form a cycle.** Delivery doesn't detect cycles between stages. Cancel the run and fix the `from` lists.

## A run failed

"The target stack ... does not exist. Create it first."
: Create the target stack with `pulumi stack init`, then [retry the run](/docs/delivery/operations/runs-and-stages/#retry-a-failed-run).

"you do not have permission to open environment '\<org\>/\<project\>/\<env\>'"
: Your organization's default deployment role can't open the target stack's ESC environment. Grant it access. See [Cloud credentials](/docs/delivery/guides/cloud-credentials/).

A source fails to lock a commit
: Every source must be declared at the top level of the pipeline program. A source created from a step's output after the first pass can't lock a commit.

A job fails
: A non-zero exit code fails the job and its stage. Check the job's logs on the run page. For HTTP checks, use `curl -fsS` so an error status fails the command.

A pass fails repeatedly
: A failed pass restarts up to 3 times in a row before the run fails. A pass that makes progress resets the count.

## A canceled update left a stack in a bad state

A canceled update can take a few minutes to stop. Once it has, run `pulumi refresh` on the affected stack before you retry or roll back.
