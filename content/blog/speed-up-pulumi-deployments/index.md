---
title: "Faster Pulumi deployments: Reuse preparation across environments"
# TODO: Set the publication date before publication.
date: 2099-01-01
draft: true
meta_desc: "Choose between dependency caching and prepared Pulumi releases. Compare measured results, include build costs, and try runnable examples in five languages."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - platform-engineering
    - esc
category: best-practices
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

If your platform team deploys reusable infrastructure across hundreds of accounts, preparation can become a significant part of the work. Each runner may download language dependencies, install provider plugins, and compile a program that another environment already uses. Reducing that repetition can save execution time and give you more control over the software deployed across those accounts.

The useful question is where that reusable work should live. A cache can preserve dependencies and build outputs for later jobs. A prepared release can distribute the same executable environment across stacks. Both help, but a program change does not automatically make a prepared release the better choice.

<!--more-->

Tests with a small Go program illustrate the distinction. A source edit retained most cached build work. Updating one dependency caused a managed cache miss on every source stack. The right recommendation depended on what changed and how many deployments reused the release.

## Start by reusing cached work

Go keeps downloaded modules in `GOMODCACHE` and compiled package outputs in `GOCACHE`. When you edit application code, Go checks its build inputs and rebuilds affected packages. Unchanged dependencies can remain reusable. Running from source does not mean compiling everything again.

With dependency caching enabled on Pulumi-managed Deployments runners, Pulumi Cloud stores an archive of both caches. Later deployments restore that archive onto their runner. Go still decides which compiled outputs are valid; Pulumi Cloud preserves the files between jobs.

For supported runtimes, the managed archive also includes provider plugins and policy packs.

These managed caches are scoped to individual stacks. A new stack cannot reuse another stack's entry. For Go, the cache key uses `go.sum`, falling back to `go.mod`. A changed dependency file can select a new entry even when most dependencies remain unchanged.

The [measurement lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/01-measure-and-cache) shows how to enable caching and verify restoration in deployment logs. Measure a source edit as well as an unchanged repeat. Otherwise, you cannot tell whether the cache helps the changes your team normally makes.

Go is the measured example here, not a recommendation to change languages. Managed caching also supports Node.js, Python, and .NET, but the cached contents differ. Package stores, installed environments, and compiled outputs avoid different kinds of work. Java currently lacks this managed cache support. The companion includes functional examples in TypeScript, Python, Go, C#, and Java; the Go timings do not establish their relative performance.

## Build once when deployments can share the preparation

A cache helps where its contents are available and useful. A prepared release lets you reuse work across stacks that would otherwise prepare the program independently. That can matter when creating new environments or deploying a dependency update across many existing environments.

Include the release build and publication in that decision. Moving work into another job does not remove its cost. Compare one release's preparation plus its deployments against preparing the program separately for every deployment. Greater reuse can spread the release cost across more environments.

The [changed-program experiment](https://github.com/pulumi/workshops/tree/d05579c/faster-pulumi-deployments/benchmarks/results/2026-10-30-changes) tested three source stacks and three image stacks. Each received the same baseline, source edit, and dependency update. The source edit changed an exported value without changing resource inputs or dependency files. The dependency update changed one imported library.

All three source stacks restored their cache after the source edit. All three missed it after the dependency update. Including the image release's preparation produced these cumulative elapsed-stage totals:

| Change deployed to three stacks | Run from source | Build and publish once, then run the image |
| --- | ---: | ---: |
| Source-only edit | 168.6 seconds | 178.8 seconds |
| Dependency update | 603.0 seconds | 175.0 seconds |

The source totals include each job's preparation and execution. The image totals include one build and publication plus three deployment jobs. Both exclude queue delays and baseline setup. Full phase breakdowns and sample ranges are in the report.

For the small source edit, cached source remained efficient. For the dependency update, the prepared image avoided repeated work.

The builder also benefited from caching: it retained Go caches across the dependency change, while managed Deployments selected a new archive key. The result combines retained build work with reuse of the executable across stacks. It does not isolate the contribution of each. A source-based runner with persistent Go caches could retain useful work across dependency changes too.

These measurements used a small Random-provider program and an emulated Linux AMD64 builder on an ARM64 host. Cloud comparisons resumed while a service incident was in monitoring. They are not billing measurements or a production break-even rule. They show why source edits and dependency changes deserve separate tests.

## Package the complete execution environment

A compiled Go program contains its imported Go packages, including the Pulumi SDK. It does not contain every executable required for a deployment. Pulumi's architecture also uses:

- The Pulumi CLI and engine.
- A language host, such as `pulumi-language-go`.
- Resource provider plugins that perform resource operations.
- Any component providers, additional runtimes, and tools required by the program.

Some of these ship together in the standard Pulumi distribution, but they remain separate from your compiled program. Precompiling the program alone can leave the runner downloading providers or preparing other tools.

A versioned release bundle or executor image can distribute those dependencies together. The [artifact lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/03-release-artifacts) packages a program with its required provider plugins. The [image lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/04-executor-images) prepares the execution environment inside an image. Skip automatic dependency installation only after the release supplies what that step would prepare.

Keep account-specific configuration and credentials outside the release. Stack configuration and Pulumi ESC can supply environment differences while every stack executes the same prepared program. Pin the image digest or artifact version, and record configuration revisions when you need to reproduce a deployment exactly.

That separation also supports release consistency. Promoting the executable you tested makes it easier to identify which software versions reached each environment. This can justify a prepared release even when its speed advantage is small.

## Put each cache where its work happens

The same distinction applies when you control the runners. On customer-managed Kubernetes runners, a volume mounted into job Pods can preserve Go or package-manager caches. Kubernetes nodes separately cache executor image layers. Replacing a job Pod can retain both kinds of reusable data, but replacing a node can lose its image cache.

The [Kubernetes lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/05-kubernetes-cache) covers worker mounts and image-pull settings. A stable runner pool can reuse image layers across stacks. A nearby registry or pre-pulling can help distribution, but include their costs in your measurements.

GitHub Actions has separate caches too. `actions/setup-go` can restore Go modules and build outputs, while BuildKit caching can reuse image-build work. Neither automatically populates a remote deployment runner's cache. Cache restoration, image construction, and image pulling are distinct operations.

## Choose with your own deployment changes

Start with caching where supported. Measure configuration-only changes, source edits, dependency updates, and first deployments to new stacks separately. Consider a prepared release when many deployments would otherwise repeat preparation, or when promoting a controlled execution environment is valuable in its own right.

Keep queue time separate from job execution. If waiting dominates, dependency tuning addresses only part of the problem; the [rollout lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/06-rollout) covers triggers and concurrency.

Use the [runnable companion](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments) to try these strategies in your existing language. The goal is to stop repeating preparation that your deployments can usefully share. Keep the simplest approach that delivers that benefit for your workload.
