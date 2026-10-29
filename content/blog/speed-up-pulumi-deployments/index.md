---
title: "Faster Pulumi deployments, part 1: Measure and cache"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-01
draft: true
meta_desc: "Measure deployment setup time, enable Pulumi Deployments dependency caching, and compare first and repeated runs on separate stacks."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - go
    - esc
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

Imagine you are a platform engineer responsible for infrastructure deployments across hundreds of AWS accounts. Your team has captured its infrastructure patterns in Pulumi components and template programs, with environment-specific values kept in stack configuration. Developers reuse those building blocks instead of designing and implementing the same infrastructure for every application. That investment is already saving development time and giving your organization a more consistent way to deploy infrastructure.

Now you want to improve the deployment process itself. Each environment may use the same program revision, yet its runner still downloads dependencies, installs provider plugins, and compiles code before managing any resources. Across hundreds of accounts, that repeated preparation consumes runner time and repeats dependency retrieval for code you have already built and tested.

<!--more-->

The goal is to make deployments faster and more repeatable while reducing runner costs and improving control over your dependency supply chain. A centralized build can establish which dependency versions belong to a release and produce artifacts that every environment reuses. With pinned versions and controlled publication, you can identify and verify what will execute instead of reconstructing the execution environment separately for every stack. Caching can reduce the preparation that remains, especially for programs that continue to install dependencies at deployment time.

This tutorial series develops that process with Pulumi Deployments and Pulumi ESC. It covers building Go programs and their SDK dependencies centrally, packaging matching provider plugins, and distributing the executable release in a container image. It also covers persistent caches for customer-managed runners, including programs written in other languages. Each stage builds on the previous one so you can measure whether the change improves your workload.

The program remains configurable throughout. Compiling a Go program includes its SDK dependencies, but Pulumi still supplies the selected stack's configuration when the executable runs. ESC can manage those values and credentials separately from the build, allowing the same tested artifact to serve different accounts and environments. Provider plugins remain separate executables, so they must be prepared alongside the program and matched to the SDK versions it uses.

The six parts follow this sequence:

1. **Measure before optimizing.** Establish a baseline and test dependency caching in this post.
1. **[Build each program revision once](/blog/precompile-pulumi-go-programs/).** Reuse the executable across stacks while keeping configuration specific to each environment.
1. **[Release the matching plugins with the program](/blog/version-pulumi-deployment-artifacts/).** Make the required versions explicit and remove redundant installation work.
1. **[Package the executable release in a container image](/blog/prebuilt-pulumi-executor-images/).** Reuse image layers while keeping configuration outside the image.
1. **[Persist caches on customer-managed Kubernetes runners](/blog/cache-pulumi-kubernetes-runners/).** Retain dependencies after job Pods exit, including for programs in other languages.
1. **[Reduce unnecessary deployments and queue time](/blog/reduce-pulumi-rollout-time/).** Schedule the work you need and provide enough capacity to run it.

Each of these changes comes with a tradeoff. A dependency cache takes time to restore, an artifact takes time to download, and a custom image takes time to pull. Moving work out of the deployment only helps when the replacement costs less, or when enough deployments reuse the result to justify the preparation. For that reason, the series introduces one change at a time and compares it with the preceding version of the process.

## Use a representative program and control the comparison

Use a Go project that already deploys successfully through [Pulumi Deployments](/docs/deployments/get-started/). Choose two disposable stacks in the same Pulumi Cloud project, running the same source revision with different stack configuration. This series calls them `bench-a` and `bench-b`; use your own stack names in commands.

If you need a small project to check the mechanics first, the `random-go` template provides a working provider-backed program without provisioning cloud infrastructure:

```bash
pulumi new random-go --name fleet-infra --stack <org>/fleet-infra/bench-a
pulumi stack init <org>/fleet-infra/bench-b
```

Put the generated project in a Git repository and [connect both stacks to Pulumi Deployments](/docs/deployments/get-started/deployments-using-cli/#configure-deployment-settings). The Random provider is useful for checking the build and execution steps, but its timings do not represent a larger infrastructure program. Use representative infrastructure for performance conclusions.

Use a program that represents your actual infrastructure rather than choosing the smallest example that can complete a deployment. An output-only program is useful for demonstrating configuration behavior, but it leaves out the provider dependencies that may account for much of your setup time. A test is useful only if the work it measures resembles the work you want to improve.

For this first part, use Pulumi-managed runners. If your organization requires customer-managed runners, follow the measurement method here, then use the cache implementation in [part 5](/blog/cache-pulumi-kubernetes-runners/). The managed cache setting has no effect on customer-managed runner pools.

The comparison also depends on controlling the inputs. Record the program commit, Pulumi CLI version, Go version, and executor image so you can identify the environment behind each result. Keep the committed `go.mod` and `go.sum` unchanged during the comparison, along with the runner configuration and cloud credentials. If several inputs change together, a shorter deployment leaves you uncertain about which change helped.

Later parts use S3 for artifacts. If you plan to follow that path, use an executor image with the AWS CLI before collecting this baseline. Otherwise, record the image change as a separate experiment when you reach part 2.

## Record the baseline without caching

Open **Settings** → **Deploy** for each test stack. Leave **Cache dependencies to speed up deployments** disabled. Keep automatic dependency installation enabled.

Run a deployment of `bench-a`, then repeat it without changing the program or configuration. Open each deployment's logs and record the durations of runner preparation, dependency installation, and the Pulumi operation. Record queue time separately from execution time.

Use this worksheet for each experiment. Enter measured values rather than estimates:

| Run | Queue | Runner and source setup | Cache restore/save | Dependency installation | Pulumi operation | Total elapsed |
| --- | --- | --- | --- | --- | --- | --- |
| Cache disabled, first run | | | | | | |
| Cache disabled, repeat | | | | | | |
| Cache enabled, first run | | | | | | |
| Cache enabled, repeat | | | | | | |
| Second stack, same lock files | | | | | | |

Be careful about what the total duration represents. Creating a new database and updating a stack with no changes are different workloads, even if both execute the same program. Keep new-stack results separate from repeated updates, and use no-change previews to understand setup and evaluation without the cost of resource creation. Otherwise, the apparent improvement may come from asking the provider to do less work.

Repeat the comparisons and keep the slower results as well as the typical ones. A warm runner can make a process look attractive while hiding the preparation that a new runner must perform. This matters particularly for platforms that mostly create new environments, where the steady-state behavior of an existing stack may be the less relevant measurement.

## Reuse dependencies before changing how you build

For both stacks, open **Settings** → **Deploy** and enable **Cache dependencies to speed up deployments**. Save the settings, then deploy `bench-a` again.

[Managed dependency caching](/docs/deployments/concepts/settings/dependency-caching/) is a useful starting point because it leaves your program and build process intact. It includes Go's module and build caches, along with Pulumi provider plugins and policy packs. The first run can prepare a cache entry that later deployments restore instead of retrieving the same dependencies individually. You still use the existing installation process, but give it previously prepared files to work with.

In the **Restore cache** log, look for `Cache restored successfully` or `No cache to restore, skipping...`. In **Save cache**, check that Pulumi captured and uploaded the cache. A `Skipping caching step` message needs investigation before you attribute a result to caching.

Repeat the deployment with the same commit and stack configuration. Record the cache transfer time as well as any reduction in dependency installation or program execution.

Leave dependency installation enabled for this experiment. A cache supplies files that the existing installation process can reuse. [Skipping installation](/docs/deployments/concepts/settings/skip-dependency-installation/) removes that process entirely, so you must first supply everything it would have prepared.

## Compare new-stack and repeat-run cache behavior

Deploy `bench-b` using the same source revision and lock files. Confirm that caching is enabled for this stack too.

Managed dependency caches are scoped to individual stacks. Enabling caching on `bench-b` does not let it restore an entry populated by `bench-a`, even when both stacks belong to the same project and use identical lock files. This separation matters for a platform that mostly creates new environments: each new stack must populate its own cache.

Expect the first `bench-b` run to report `No cache to restore, skipping...`. Wait for its **Save cache** step to finish, then repeat the deployment and compare the logs. The repeat should restore the entry saved by that stack. The artifact and image approaches in later parts provide an explicit way to share prepared code across environments without relying on another stack's managed cache.

Use an update to populate the cache for this comparison. Previews can restore an existing cache for their stack, but they do not save new entries. A preview with changed dependencies can therefore remain cold until an update populates the corresponding entry.

Next, make a deliberate dependency update on a test branch and repeat the measurement. A changed lock file produces a different cache key. Record the first run after that change separately from warm runs.

Avoid clearing the cache on a production project for this experiment. The **Clear cache** action clears entries for the whole project, not only the selected stack.

## Keep the cache when it saves more time than it costs

Compare the baseline and warm runs for the same operation. Include cache restoration and saving in the total. If caching adds time, inspect archive size and the work that was actually avoided.

Also keep the deployment's execution time separate from the time an entire rollout takes to finish. Two shorter jobs can still wait for the same runner, so reducing preparation may save runner time without eliminating the queue. That is a useful result, but it points to a different next step than further cache tuning.

If compilation still accounts for meaningful execution time, you can take the separation further and publish an executable that no deployment needs to rebuild. [Part 2](/blog/precompile-pulumi-go-programs/) develops that approach using the same program and test stacks, with these cache results as the comparison.
