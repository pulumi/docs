---
title: Faster Deployments
title_tag: Reuse preparation across stacks | Pulumi Deployments
h1: Reuse preparation across stacks
meta_desc: Use dependency caching, custom executor images, release bundles, or runner storage so Pulumi Deployments stops preparing the same program for every stack.
menu:
  deployments:
    name: Faster Deployments
    parent: deployments-guides
    weight: 35
    identifier: deployments-guides-faster-deployments
---

Before a deployment runs a Pulumi operation, it prepares the program: it downloads dependencies and [provider plugins](/docs/iac/concepts/plugins/), and for some languages it compiles the program. When one program deploys to many [stacks](/docs/iac/concepts/stacks/), each stack repeats that preparation on its own, and a rollout that changes one line of configuration can spend most of its time preparing.

This guide explains how a deployment prepares a program, describes the options that reuse that work, and recommends options for common situations. The options are:

- **[Dependency caching](/docs/deployments/concepts/settings/dependency-caching/)** keeps each stack's downloaded dependencies, build outputs, and plugins between that stack's deployments. Each stack still prepares from source, but it reuses what it prepared last time.
- **A [custom executor image](/docs/deployments/concepts/settings/custom-executor-images/)** contains the prepared program. You build it once in a release pipeline, and every stack runs the same image without installing or compiling anything.
- **A release bundle** is a versioned archive of the prepared program, which a deployment downloads from object storage instead of pulling a private image. It serves the same purpose as a custom image where a private registry isn't available.
- **Persistent storage on customer-managed runners** keeps package caches and image layers on runners you operate, where you decide what survives between jobs.

Some rollouts are slow because deployments wait in the queue rather than because they prepare slowly. [Skipping intermediate deployments](/docs/deployments/concepts/settings/skip-intermediate-deployments/) and tuning [triggers](/docs/deployments/concepts/triggers/) address that case.

## How a deployment prepares your program

Every deployment runs inside a container called the executor image. By default, Pulumi Deployments uses the [`pulumi/pulumi` image](/docs/deployments/guides/custom-images/#the-default-executor-image), which includes the Pulumi CLI, the supported language runtimes, and common build tools.

A deployment from source fetches the program from its [source](/docs/deployments/concepts/settings/source/), installs its dependencies with the language's package manager, runs any [pre-run commands](/docs/deployments/concepts/settings/pre-run-commands/), and then runs the Pulumi operation. During that operation, the Pulumi engine starts a [language host](/docs/iac/guides/basics/how-pulumi-works/), which builds and runs your program, and loads the provider plugins that perform resource operations. The CLI downloads each plugin the first time a program needs it, unless the plugin is already installed. For a Go program, the language host also compiles the program before it runs.

Each language keeps the results of this work in its own directories. Go keeps downloaded modules in `GOMODCACHE` and compiled package outputs in `GOCACHE`. When you edit application code, Go rebuilds only the affected packages and reuses the compiled dependencies, provided those directories are still available. Node.js, Python, and .NET keep their equivalents in `node_modules` and the npm cache, a virtual environment, and the NuGet package folder.

Where those directories live determines how much a deployment can reuse. On [Pulumi-managed runners](/docs/deployments/concepts/pulumi-managed-runners/), each deployment runs on a single-use virtual machine, so nothing on the runner survives from one deployment to the next. Without one of the options in this guide, every deployment downloads, installs, and compiles everything again.

### Measure before you choose

The deployment logs show how long each step takes. Before you choose an option, compare the setup, dependency installation, and Pulumi operation steps across a few recent deployments, and note how long deployments wait before they start. The [measurement lab](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/labs/01-measure-and-cache/README.md) in the companion workshop shows how to export those timings.

## Dependency caching

When you turn on **Cache dependencies to speed up deployments** in a stack's deployment settings, Pulumi Cloud archives the language's package and build directories at the end of a deployment and restores them at the start of the next one. For Go, that means both `GOMODCACHE` and `GOCACHE`. The language's own tools still decide what is current: Go checks its build inputs and rebuilds whatever changed. Each cache entry also includes the downloaded provider plugins and [policy packs](/docs/discovery-governance/concepts/policy-as-code/policy-packs/), which are often among the largest downloads in a deployment.

Caching supports Node.js, Python, .NET, and Go. See [what gets cached](/docs/deployments/concepts/settings/dependency-caching/#what-gets-cached) for each one. The deployment logs show whether a cache was used: the **Restore cache** step prints `Cache restored successfully` for a hit and `No cache to restore, skipping...` for a miss. The [troubleshooting reference](/docs/deployments/concepts/settings/dependency-caching/#verifying-and-troubleshooting) lists the other messages.

Two properties of the cache decide which deployments it helps:

- **Cache entries are [scoped to a single stack](/docs/deployments/concepts/settings/dependency-caching/#enabling-dependency-caching).** A new stack starts without a cache, even when another stack in the same project deploys the same program. Its first deployment prepares everything and then saves its own entry.
- **Each entry is keyed by the contents of the program's lock files.** For Go, the key comes from `go.sum`, falling back to `go.mod`. Lock files such as `package-lock.json`, `uv.lock`, and `packages.lock.json` play the same role for the other runtimes. A source edit leaves the lock file unchanged, so the next deployment restores the existing entry. A dependency update changes the lock file, so the first deployment of that release misses the cache on every stack.

As a result, caching helps most with source edits to existing stacks. Dependency updates and new stacks miss the cache on every stack, and each stack repeats the same preparation.

Managed caching is [unavailable on customer-managed runners](/docs/administration/concepts/customer-managed-runners/#not-supported-on-customer-managed-runners). There, you provide persistence yourself, as described in [Persistent storage on customer-managed runners](#persistent-storage-on-customer-managed-runners).

## Custom executor images

A custom executor image replaces the default image with one that you build, host in a registry, and reference from the stack's [deployment settings](/docs/deployments/concepts/settings/custom-executor-images/). When the image already contains the prepared program and its plugins, the deployment has nothing left to install or compile. You can then turn on [Skip package manager dependency installation](/docs/deployments/concepts/settings/skip-dependency-installation/) and leave dependency caching off.

### What the image contains

A complete image contains:

- The Pulumi CLI, which supplies the engine and the language hosts for Node.js, Python, Go, .NET, Java, and YAML.
- The language runtime. For Go, this applies even to a prebuilt executable, because the Go language host currently looks for the `go` binary before it runs the program ([pulumi/pulumi#25549](https://github.com/pulumi/pulumi/issues/25549)).
- The prepared program: a compiled executable for Go, or installed dependencies for languages such as TypeScript and Python.
- The provider plugins that the program uses, installed with [`pulumi plugin install`](/docs/iac/cli/commands/pulumi_plugin_install/). An image without them downloads the plugins during each deployment.
- Any additional tools, such as component provider runtimes or cloud CLIs.

The image must also meet the [executor image requirements](/docs/deployments/guides/custom-images/#image-requirements): a Linux image based on glibc, with `curl` and `pulumi` on the `PATH`. The single-language images from [`pulumi/pulumi-docker-containers`](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md), such as `pulumi/pulumi-go`, meet these requirements and include the language runtime, which makes them good starting points. The smaller `pulumi/pulumi-base` image includes the CLI but no language runtime.

The image holds only what every stack shares. Stack configuration supplies the values that differ between environments, and [Pulumi ESC environments](/docs/esc/concepts/environments/) supply credentials and shared settings. For cloud credentials, Pulumi Deployments can exchange an [OpenID Connect (OIDC) token](/docs/deployments/guides/oidc/) for short-lived credentials during each deployment, so no long-lived secret is stored in the image. Because the configuration still comes from Git, recording the configuration revision along with the image digest identifies exactly what each stack ran.

### How the image reaches the runner

Pulumi Deployments has no managed cache for custom images comparable to dependency caching. The default image is pre-cached on Pulumi-managed runners, but a [custom image is not](/docs/deployments/guides/custom-images/#cold-starts). Because each deployment runs on a fresh virtual machine, the runner pulls a custom image during setup on every deployment. The pull takes longer for a larger image and for a registry farther from the runners, which run in AWS `us-west-2`. A small base image and a multi-stage build that leaves compilers out of the final image keep the pull short.

Pulumi-managed runners authenticate to a private registry only with a [static username and password](/docs/deployments/concepts/settings/custom-executor-images/). Pulls that use OIDC or an IAM role aren't supported. Docker Hub, GitHub Container Registry, and Artifactory work with static credentials. A private Amazon Elastic Container Registry (ECR) repository doesn't, because its registry password is a token that expires after 12 hours.

### How the image is built

The image build runs in your release pipeline, which has its own caches. In GitHub Actions, [`actions/setup-go`](https://github.com/actions/setup-go#caching-dependency-files-and-build-outputs) restores Go modules and build outputs, and [BuildKit's GitHub Actions cache](https://docs.docker.com/build/cache/backends/gha/) reuses image layers across builds. These caches have the same limitation as dependency caching: `actions/setup-go` keys its cache on `go.sum`, so a dependency update starts the build without a usable Go cache. A persistent build host, or an [`actions/cache`](https://github.com/actions/cache) configuration with fallback restore keys, keeps more of that work across dependency updates. Build on the runners' platform, Linux AMD64 for Pulumi-managed runners, so that the build doesn't run under emulation.

The [image lab](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/labs/04-executor-images/README.md) builds an image with the language runtime, CLI, prepared program, and provider plugins, and deploys it by digest.

## Release bundles

A release bundle separates the prepared program from the image. The [artifact lab](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/labs/03-release-artifacts/README.md) packages the program, its runtime dependencies, and its provider plugins into a versioned archive in Amazon S3, with a checksum. The executor image then holds only tools: the language runtime, Pulumi CLI, AWS CLI, and checksum utilities. It contains nothing proprietary, so it can live in a public registry.

A pre-run command fetches the archive with AWS credentials from an ESC environment, which can issue short-lived credentials through [AWS login](/docs/esc/providers/login/aws-login/). It then verifies the checksum and installs the provider plugins from the archive. A new release changes only the archive, and the tools image stays the same.

A bundle adds an archive download and a verification step to each deployment, and the deployment still pulls its tools image. In return, the program never goes into a registry, and object storage access can use the same short-lived credentials as the rest of the deployment.

## Persistent storage on customer-managed runners

[Customer-managed runners](/docs/administration/concepts/customer-managed-runners/) run on infrastructure you operate. The agent either launches a container through a local Docker daemon or, with the [Kubernetes deploy target](/docs/administration/concepts/customer-managed-runners/#kubernetes), launches a Pod for each job. Because you control the runners, you decide what persists between jobs, and you can pull private images with any mechanism your platform supports, including an IAM role.

Two kinds of work can persist:

- **Package and build caches.** On Kubernetes, the agent's worker Pod template can mount a PersistentVolumeClaim into the `pulumi-workflow` container, and environment variables can point the language's cache directories at it, such as `GOMODCACHE` and `GOCACHE` for Go. Unlike the managed cache, this volume isn't scoped to a stack or keyed on a lock file: the first stack to deploy a release prepares it, and the stacks after it reuse that work, including new stacks. The volume needs a size limit and a cleanup plan, because nothing removes old entries. A `ReadWriteOnce` volume also restricts job Pods to the node it's attached to, so a pool with several nodes needs `ReadWriteMany` storage or a volume for each node.
- **Image layers.** Each node's container runtime keeps the image layers it has downloaded. A job Pod reuses them when the pull policy of its `pulumi-workflow` container allows it. That policy comes from the agent's worker Pod template, or from the Kubernetes default, which is `IfNotPresent` for an image referenced by digest. The agent's `PULUMI_AGENT_IMAGE_PULL_POLICY` setting applies to the init container that copies the agent's runner binary into the Pod, not to the executor container.

Because nodes keep layers, the order of the image's layers matters on these runners. When the CLI, runtime, and provider plugins are in early layers and the program is in the last layer, a new release changes only the program layer, and a node that already holds the earlier layers downloads only that one.

Source deployments that don't set an executor image use the full, multi-language `pulumi/pulumi:latest` image on customer-managed runners. That image is large, and the `latest` tag changes the CLI version whenever a new release is published.

The [Kubernetes lab](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/labs/05-kubernetes-cache/README.md) configures a cache volume, the worker Pod template, and the executor's image pull policy.

## Recommendations

Start from the kind of change that dominates your deployments and the runners you use. Most teams combine options: caching for everyday edits, and a prepared release for the changes that reach many stacks at once.

### Source edits to existing stacks

Turn on dependency caching. A source edit leaves the lock file unchanged, so each stack restores its own cache and compiles only what changed. Building an image for every edit adds a release build and an image pull without much preparation left to save. Check the **Restore cache** step in the logs to confirm the hits.

### Dependency updates rolled out to many stacks

Build a custom executor image once and deploy it to every stack. With caching alone, every stack misses its cache on the new lock file and prepares the same release separately. With an image, that preparation happens once, in the release build.

Keep the release build itself fast across dependency updates, since that's where the work moved. Use a persistent build host or an `actions/cache` configuration with fallback restore keys, so that the build reuses compiled packages that didn't change.

### Frequent creation of new stacks

Use a custom executor image. A new stack has no cache to restore, and an image arrives already prepared. If you onboard accounts in batches, this case resembles a dependency rollout: many stacks that would each prepare the same program.

### Programs that need extra tools

Use a custom executor image when a program needs component provider runtimes, cloud CLIs, or other tools beyond the default image. Installing them once in the image replaces pre-run commands that install them during every deployment.

### Promoting a tested release

Deploy a custom executor image by digest. The same program, CLI, language host, and plugins that passed testing then reach every environment, and the digest records which version each stack ran. Keep configuration in Git and record its revision with the digest.

### Pulumi-managed runners without a usable private registry

When the only private registry available is one that issues short-lived passwords, such as private ECR, or when security policy rules out stored registry credentials, use a release bundle with a public tools image. It provides the same build-once release as a private image, at the cost of a download and verification step in each deployment.

| Runners and registry | Build once as |
| --- | --- |
| Customer-managed runners | Custom executor image, pulled with any mechanism you configure |
| Pulumi-managed runners, static registry credentials acceptable | Custom executor image in a private registry |
| Pulumi-managed runners, short-lived registry credentials only | Release bundle with a public tools image |

### Customer-managed runners on Kubernetes

Mount a persistent cache volume into the worker Pods before you build images for speed. Because the volume is shared across stacks, it covers dependency updates and new stacks as well as source edits, so source deployments may be enough. Reserve images for the other reasons in this section: extra tools and pinned, tested releases.

Set a pinned, single-language executor image, such as `pulumi/pulumi-go`, in each stack's [executor image setting](/docs/deployments/concepts/settings/custom-executor-images/), so that source deployments don't pull the full default image and the CLI version changes only when you change it.

When you do use custom images, reference them by digest and set `imagePullPolicy: IfNotPresent` on the `pulumi-workflow` container in the worker Pod template. Order the image's layers so that a release changes only the last one. Keep a stable runner node pool so that nodes retain base layers across releases, and pre-pull a new release onto the runner nodes before a large rollout.

### Deployments that wait to start

If deployments spend more time in the queue than running, preparation changes won't help. Use [skip intermediate deployments](/docs/deployments/concepts/settings/skip-intermediate-deployments/) so that a burst of commits produces one deployment per stack, and review the [triggers](/docs/deployments/concepts/triggers/) that start each rollout. The [rollout lab](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/labs/06-rollout/README.md) covers triggers and concurrency for rollouts across many stacks.

## Verify the change

How much each option saves depends on the program's language and size, its providers, the image size, the registry, and the number of stacks that receive each release. Measure the change on a few stacks before you roll it out widely. Compare the step durations in the deployment logs before and after, and include the release build time when you compare a prepared release with source deployments. The companion workshop's [timing tools](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/benchmarks/README.md) export step timings and run controlled comparisons.

The [companion workshop](https://github.com/pulumi/workshops/blob/7f9af44/faster-pulumi-deployments/README.md) has working examples in TypeScript, Python, Go, C#, and Java, with labs for caching, release bundles, executor images, Kubernetes runners, and rollouts. Managed dependency caching supports Node.js, Python, .NET, and Go. Java stacks can use a custom executor image or a release bundle.
