---
title_tag: "Pulumi Docker Images | IaC Operations"
meta_desc: Pulumi's official Docker images bundle the CLI with language runtimes — for CI/CD, Kubernetes pods, Deployments, or as a base for custom images.
title: Docker Images
h1: Pulumi Docker Images
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Docker Images
        parent: iac-operations
        weight: 45
        identifier: iac-operations-docker-images
---

Pulumi publishes and supports an official family of Docker images that bundle the [Pulumi CLI](/docs/iac/cli/) with one or more language runtimes. The images are scanned nightly for vulnerabilities and released on the same cadence as the Pulumi CLI, so a given tag matches a known Pulumi release. They are useful wherever you need a turnkey Pulumi environment — running Pulumi in CI/CD, in Kubernetes pods, as a [Pulumi Deployments custom executor](/docs/deployments/deployments/runs/images/), or as a base for derivative images that add tools the default images don't ship.

The image source lives at [`pulumi/pulumi-docker-containers`](https://github.com/pulumi/pulumi-docker-containers) on GitHub.

## Available images

- [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) — the kitchen sink: the Pulumi CLI plus every supported language runtime (Go, Python, Node.js, .NET, Java). Approximately 2 GB. Right when you want one image that works for any language, or for polyglot projects.
- [`pulumi/pulumi-base`](https://hub.docker.com/r/pulumi/pulumi-base) — the Pulumi CLI only, no language runtime. Approximately 200 MB. Right when you'll install your own language runtime, or when you only use the CLI (for example, to manage stacks or run `pulumi import`).
- Language-specific slim images — the Pulumi CLI plus a single language runtime, 200–300 MB each. Right for single-language projects:
  - [`pulumi/pulumi-go`](https://hub.docker.com/r/pulumi/pulumi-go)
  - [`pulumi/pulumi-python`](https://hub.docker.com/r/pulumi/pulumi-python)
  - [`pulumi/pulumi-nodejs`](https://hub.docker.com/r/pulumi/pulumi-nodejs)
  - [`pulumi/pulumi-dotnet`](https://hub.docker.com/r/pulumi/pulumi-dotnet)
  - [`pulumi/pulumi-java`](https://hub.docker.com/r/pulumi/pulumi-java)
- Per-language-version variants of the slim images — for example, `pulumi/pulumi-nodejs-22`, `pulumi/pulumi-python-3.12`, `pulumi/pulumi-dotnet-9.0`. The unsuffixed image is built on the current default runtime version; see [Choosing a language version](#choosing-a-language-version).

## Where to get them

Every image is pushed to three registries:

- [Docker Hub](https://hub.docker.com/u/pulumi)
- [Amazon ECR Public Gallery](https://gallery.ecr.aws/pulumi/)
- [GitHub Container Registry](https://github.com/orgs/pulumi/packages)

Pull from whichever is closest to your runner to minimize cold-start time.

## Tags and release cadence

Image tags mirror the Pulumi CLI's git tags. When [`pulumi v3.244.0`](https://github.com/pulumi/pulumi/releases) is released, you'll find a corresponding [`pulumi/pulumi:3.244.0`](https://hub.docker.com/r/pulumi/pulumi) in all three registries. The `latest` tag tracks the latest stable Pulumi CLI release.

The images are released automatically as part of the Pulumi CLI's release process. New minor releases arrive roughly weekly, with patch releases more frequently as needed.

For reproducible builds, pin to a specific version (`pulumi/pulumi:3.244.0`) rather than `latest`. Pinning also keeps the image and your local CLI from drifting apart.

## Base images and platforms

The `pulumi/pulumi` kitchen-sink image is built on Debian for both `linux/amd64` and `linux/arm64`.

Each slim image is built on a matrix of base images and platforms, with a suffix on the tag:

- `-debian-amd64`, `-debian-arm64` — single-platform Debian images.
- `-debian` — manifest list combining the two Debian platforms. `docker pull` picks the right one for the host architecture, so this is the default choice.
- `-ubi` — Red Hat UBI-minimal base, available for `linux/amd64` only. UBI uses [`microdnf`](https://github.com/rpm-software-management/microdnf) as a package manager instead of `yum` to keep the image small.

The unsuffixed tag is identical to the corresponding `-debian` tag. For the current Debian and UBI major versions, see the [Build Matrix](https://github.com/pulumi/pulumi-docker-containers#build-matrix) in the source repo's README.

## Default language versions

Unsuffixed images use a default version of each language runtime, generally tracking current LTS releases. The defaults rotate as new releases land, so the source repo's README is the authoritative reference — see [Language Versions](https://github.com/pulumi/pulumi-docker-containers#language-versions) for the current default per language and the policy that drives them.

Pin the image tag to a specific Pulumi CLI version to avoid an unintended runtime upgrade when the default rotates.

## Choosing a language version

### Slim images

For the language-specific slim images, use the suffixed tag to select a runtime version. For example, `pulumi/pulumi-nodejs-22` for Node.js 22, `pulumi/pulumi-python-3.12` for Python 3.12, `pulumi/pulumi-dotnet-9.0` for .NET 9.0. The currently published variants are listed on each image's Docker Hub page.

### Kitchen-sink (`pulumi/pulumi`)

The kitchen-sink image carries several language runtimes simultaneously. How you select among them depends on the language:

**.NET** — the `TargetFramework` property in your project's `.csproj` or `.fsproj` file selects the SDK:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    ...
```

**Go** — the `go` directive in your `go.mod` file selects the toolchain. See [Go Toolchains](https://go.dev/doc/toolchain).

**Java** — the kitchen-sink image ships a single JDK.

**Node.js** — the image uses [`fnm`](https://github.com/Schniz/fnm) to manage Node.js versions and ships the latest patch releases of several Node.js majors pre-installed (see the [README](https://github.com/pulumi/pulumi-docker-containers#language-versions) for the bundled set). To select a version, place a `.node-version` file containing the version number in your project directory and run `pulumi install --use-language-version-tools`. To avoid re-downloading Node.js on each run, specify only the major version; `fnm` then picks the pre-installed patch release for that major.

**Python** — the image uses [`pyenv`](https://github.com/pyenv/pyenv) and ships several Python minor versions pre-installed (see the [README](https://github.com/pulumi/pulumi-docker-containers#language-versions) for the bundled set). To select a version, place a `.python-version` file in your project directory. As with Node.js, specify only the major.minor version so the pre-installed build is used instead of being rebuilt at runtime.

If you build your own image on top of `pulumi/pulumi`, you can change the default Node.js version with `fnm alias <version> default`.

## Extending the images

The base and SDK images intentionally don't ship tools that are specific to a single provider or workflow — for example, `helm` and `kubectl` for the [Kubernetes provider](/registry/packages/kubernetes/), cloud-provider CLIs, or private credential helpers. When you need one of those tools available alongside the Pulumi CLI, derive your own image from the closest Pulumi image and install what you need:

```dockerfile
FROM pulumi/pulumi-base:3.244.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends helm kubectl \
    && rm -rf /var/lib/apt/lists/*
```

Build the image, push it to a registry your runner can reach, and reference it from your CI/CD job's container image setting or from your [Pulumi Deployments custom executor settings](/docs/deployments/deployments/runs/images/#custom-executor-image). Pin the `FROM` line to a specific Pulumi CLI tag rather than `latest` so that the image and your local CLI don't drift apart between rebuilds.

This same pattern lets you bake provider plugins into the image with `pulumi plugin install`, eliminating the per-run plugin download in ephemeral runners. See the [plugins documentation](/docs/iac/concepts/plugins/) for details.

## Scanning

Images are scanned for vulnerabilities nightly. Pulumi remediates issues where it can, on a best-effort basis. Some vulnerabilities — for example, CVEs in upstream base images with no published fix — are outside Pulumi's direct control and persist until the upstream is patched.

## See also

- [`pulumi/pulumi-docker-containers`](https://github.com/pulumi/pulumi-docker-containers) — image source and contribution guide.
- [Pulumi Deployments executor images](/docs/deployments/deployments/runs/images/) — using and customizing the executor image for Pulumi Deployments.
- [Continuous Delivery](/docs/iac/operations/continuous-delivery/) — CI/CD guides for the systems where these images are commonly used.
- [Docker provider](/registry/packages/docker/) — manage Docker resources (containers, networks, volumes) with Pulumi.
- [Docker Build provider](/registry/packages/docker-build/) — build and push Docker images to any registry with Pulumi.
