---
title: "Faster Pulumi deployments, part 6: Reduce rollout time"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-06
draft: true
meta_desc: "Reduce unnecessary Pulumi deployments, test queue consolidation, and measure stack concurrency after optimizing runner setup."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - performance
    - platform-engineering
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

After reducing preparation time, it is worth examining why jobs enter the queue and how long they wait there. A monorepo can trigger stacks after unrelated changes, while a busy branch can enqueue several revisions before the first deployment finishes. Those jobs consume capacity even when the desired outcome is already represented by a later revision.

Adding runners can reduce the wait, but first determine whether the queue contains work that needs to run at all. Avoiding an unnecessary deployment removes its execution cost instead of assigning that cost to another machine. Once the remaining work is understood, you can measure how much capacity it needs without carrying unrelated jobs through the comparison.

<!--more-->

## Measure the full rollout

Trigger equivalent operations for your test stacks at the same time. Record when each job was requested, when execution began, and when it completed.

Total runner time and elapsed rollout time answer different questions. The earlier artifact and cache changes can reduce how much work each stack performs, while additional concurrency lets independent stacks perform their work simultaneously. A rollout can therefore finish sooner without consuming fewer runner minutes. Decide which outcome you need, and report both so a change in scheduling is not mistaken for a reduction in execution cost.

For a larger test, use disposable environments with representative configuration. Compare new-stack deployments with other new-stack deployments, rather than with updates that change nothing.

## Make deployment triggers reflect program dependencies

In a monorepo, a stack's deployment trigger should reflect its dependencies rather than every file that happens to share the repository. [Path filters](/docs/deployments/concepts/settings/path-filtering/) let you express that relationship, but the relevant paths may extend beyond the program's own directory. A shared library, lock file, or release script can change what the stack deploys even when none of its immediate source files change. Include those dependencies when defining the filter.

For example, a program under `infrastructure/service-a/` that uses code under `infrastructure/shared/` could use these patterns:

```text
infrastructure/service-a/**
infrastructure/shared/**
go.mod
go.sum
```

Adapt the patterns to the actual repository layout. Include release scripts, manifests, and configuration files that affect deployment. Filters match paths from the repository root.

Test the filters with separate commits: one changes an unrelated directory, and another changes a shared dependency. Confirm that the first does not trigger the stack and the second does.

Repeat the test for stack-specific configuration. Treat these checks as part of the deployment process, not an optional check of the filter syntax. A filter that excludes a required update makes the pipeline faster by leaving the environment out of date.

## Skip queued intermediate changes

For stacks that receive frequent commits, enable [Skip intermediate deployments](/docs/deployments/concepts/settings/skip-intermediate-deployments/) in deployment settings.

Test this on a disposable stack. While one operation runs, queue several operations of the same type. When the active operation finishes, confirm that Pulumi runs the newest queued operation and skips the intermediate ones.

Wait until the first deployment is running before submitting the queued operations. If it finishes before the next request arrives, every deployment may run normally and the test says nothing about queue consolidation. A temporary `sleep 45` pre-run command on the first test deployment provides time to queue two more updates. Remove the delay from the later requests, then verify that the middle request is marked **Skipped** and the newest request completes.

Let the active deployment finish. This setting combines queued operations of the same type; it does not cancel work already in progress. An update also does not replace a queued destroy, because the operation types differ.

Skipping intermediate deployments is appropriate when reaching the latest desired state is the purpose of the queued work. It is less appropriate when each revision represents an operation that must happen, rather than another description of the state you ultimately want. A requirement to retain a deployment record for every commit is also a reason to keep the individual runs. Check these assumptions before treating the skipped jobs as redundant.

Record the number of executed jobs and the time until the newest revision completes. This experiment measures avoided work rather than faster execution of one job.

## Add runner capacity when queue time requires it

When jobs spend more time waiting than executing, the remaining problem may be runner capacity or an organization concurrency limit. At that point, further changes to dependency preparation address a smaller part of the elapsed rollout. The work is ready to execute but has no available slot, so capacity is the next variable to test.

Each customer-managed agent executes one deployment at a time. Add another agent to the test pool, then repeat the same two-stack rollout. Keep the image, artifact revision, and cache configuration unchanged.

If you use persistent volumes from [part 5](/blog/cache-pulumi-kubernetes-runners/), confirm that additional agents can schedule without waiting for a volume attachment. Storage constraints can cancel the benefit of extra compute.

Measure cloud API throttling as well as elapsed time. More agents can send more requests to the same account or service, producing retries instead of useful parallel work. Increase concurrency only while the measured rollout improves.

### Distinguish resource concurrency from stack concurrency

The [`pulumi up --parallel` option](/docs/iac/cli/commands/pulumi_up/) controls simultaneous resource operations inside one update. It does not add runner capacity or allow multiple updates of the same stack to proceed together.

Trust the resource dependency graph to determine which operations can run together. Increasing parallelism helps only where independent work exists and provider APIs can handle it. A required dependency chain remains sequential regardless of how much concurrency you allow.

## Keep the release process repeatable and the results attributable

Return to the measurements from [part 1](/blog/speed-up-pulumi-deployments/). Summarize the setup cost removed at each stage, including the costs added by artifact retrieval or cache restoration.

Keep cold-run and warm-run results separate, and include the initial build cost in the rollout comparison. The benefit of preparing a release once grows with the amount of repeated preparation it avoids. A single-stack deployment may not justify the same process as one program deployed across many environments.

Throughout these changes, preserve the relationship between the artifact you tested and the artifact you promote through environments. Stack configuration and ESC can supply the differences without requiring another compilation for each environment. Rebuilding the same source repeatedly adds work, and it also creates another opportunity for build inputs to differ. Reusing the tested artifact gives you both a performance benefit to measure and a clearer account of what was deployed.

Once resource creation dominates the remaining time, more dependency tuning is unlikely to change the total much. That is a useful stopping point: the preparation work you set out to reduce is no longer the main cost. Keep the changes supported by your measurements and apply the same reasoning to the next constraint, whether that is provider behavior or application builds. The result should be a process you can explain and repeat, rather than a collection of optimizations whose individual effects are unknown.
