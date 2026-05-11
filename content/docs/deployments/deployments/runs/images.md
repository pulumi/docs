---
title: Images
title_tag: Deployment images | Pulumi Deployments
meta_desc: Understand the container image that runs your Pulumi deployments, when to customize it, and how to add the tools your project needs.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Images
    parent: deployments-deployments-runs
    weight: 10
    identifier: deployments-deployments-runs-images
aliases:
- /docs/deployments/deployments/execution-environment/
---

Pulumi Cloud runs your Pulumi program inside a container image called the *deployment executor image*. This page covers what is in that image and how to customize it.

## The default executor image

By default, every deployment runs in [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi), a Linux image that includes:

- The `pulumi` CLI on `$PATH`
- [LTS versions](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md#version-policy) of all supported language runtimes: Node.js, Python, Go, .NET, and Java
- Common build tools: `git`, `curl`, and the package manager for each runtime

For most projects this is the right choice. The image is updated with every Pulumi CLI release, security-patched on a regular cadence, and pre-cached on Pulumi-hosted workflow runners, so deployments start quickly without paying a registry pull.

The image is published in [`pulumi/pulumi-docker-containers`](https://github.com/pulumi/pulumi-docker-containers). That repository also publishes smaller variants you can use as a base for a custom image. See [Choosing a base image](#choosing-a-base-image) below.

## When to customize

You need a different setup when your deployment depends on something not in the default image. Common cases:

- A CLI such as `gh` or `aws` that your Pulumi program or a deployment hook invokes
- A language runtime version different from the LTS in the default image
- A system package required by a native dependency
- A private credential helper

There are two ways to handle this. Pick based on how often you need the tool and how much you care about deployment speed.

## Choosing the right approach

| Approach | Best for | Cost |
|---|---|---|
| **Pre-run commands** | One-off tools, scripts, or quick experiments | The install runs on every deployment, adding setup time to each run |
| **Custom executor image** | Stable tool sets used on every deployment | Slower cold starts on fresh runners, and an image you have to maintain |

## Pre-run commands

If you need a tool occasionally, or you are still prototyping, install it from a [pre-run command](/docs/deployments/deployments/using/settings/#pre-run-commands) in your deployment settings:

```bash
apt-get update && apt-get install -y my-tool
```

Pros:

- No image to build or maintain
- Easy to change: edit the command and the next deployment picks it up
- Works with the default `pulumi/pulumi` image, so cold starts stay fast

Cons:

- The install runs on every deployment, adding wall-clock time
- Network failures during the install fail the deployment
- Not suitable for very large installs

Reach for a custom image only when the install cost starts to hurt.

## Custom executor image

A custom executor image is a container image you build, host, and reference from your stack's deployment settings. Pulumi pulls it before running each deployment.

### Choosing a base image

Pick the smallest base that has the language runtime(s) you need. Pull time scales with image size, so a smaller base means faster first deployments on fresh runners.

| Base image | Size (approx.) | Contents | Best for |
|---|---|---|---|
| `pulumi/pulumi-base` | ~200 MB | `pulumi` CLI only | You will install your own language runtime, or use a single language version not in the SDK images |
| `pulumi/pulumi-nodejs`, `pulumi-python`, `pulumi-go`, `pulumi-dotnet`, `pulumi-java` | 200–400 MB | `pulumi` plus one language runtime | Single-language projects |
| `pulumi/pulumi` | ~2 GB | `pulumi` plus all language runtimes | Polyglot projects, or when you do not want to pick a runtime |

If you do not need every language runtime, start from `pulumi/pulumi-base` or a language-specific variant. The full `pulumi/pulumi` image is convenient but copies ~2 GB of layers your project will not use.

All variants are listed in the [`pulumi/pulumi-docker-containers` README](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md).

### Example: adding the GitHub CLI

```dockerfile
# Pin the Pulumi CLI version explicitly. Floating tags like :latest mean the
# image and your local CLI can drift apart between deployments.
FROM pulumi/pulumi-base:3.236.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends gh \
    && rm -rf /var/lib/apt/lists/*
```

Build, push to a registry your deployment runner can reach, then point your stack at it from the [Custom Executor Image setting](/docs/deployments/deployments/using/settings/#custom-executor-images) or the `executorContext.executorImage` field of the [REST API](/docs/reference/cloud-rest-api/deployments/).

### Image requirements

A custom executor image must:

- Be a Linux image
- Include `curl` on `$PATH`
- Include the `pulumi` CLI on `$PATH`
- Include the language runtime(s) for the projects that will use it
- Use a glibc-based libc. Most Pulumi resource provider plugins are glibc-linked, so musl-only images such as Alpine are not supported

If you start from one of the `pulumi/*` base images, all of these are already true.

### Trade-offs

#### Cold starts

The default image is pre-cached on Pulumi-hosted workflow runners. Custom images are not. Every newly-provisioned runner pulls your image from its registry the first time it runs your deployment, which can add minutes to the "Preparing environment" phase.

To reduce cold-start time:

- Start from a small base (`pulumi-base` or a single-language variant)
- Host the image close to the runner. Pulumi-hosted runners run in AWS `us-west-2`, so an image in a `us-west-2` ECR is faster than one on Docker Hub.
- Pin a digest so the runner can rely on its layer cache between deployments instead of re-fetching by tag.

#### Static credentials only

If your image lives in a private registry, you must supply static username and password credentials in the deployment settings. OIDC and IAM-role-based pulls are not supported for custom executor images. If your security model requires short-lived registry credentials, [Customer-Managed Workflow Runners](/docs/deployments/deployments/runs/customer-managed-agents/) run in your own infrastructure and can use whatever pull mechanism you configure.

## See also

- [Deployment settings](/docs/deployments/deployments/using/settings/): UI walkthrough for configuring the executor image on a stack
- [Customer-Managed Workflow Runners](/docs/deployments/deployments/runs/customer-managed-agents/): full control over the runner host, registry pulls, network access, and lifecycle
- [Pre-run commands](/docs/deployments/deployments/using/settings/#pre-run-commands): where pre-run installs run
- [`pulumi/pulumi-docker-containers`](https://github.com/pulumi/pulumi-docker-containers): image source, variants, and contribution guide
