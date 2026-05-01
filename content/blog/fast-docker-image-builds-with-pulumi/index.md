---
title: "Fast Docker Image Builds with Pulumi"
date: 2023-03-08T14:00:00-08:00
updated: 2026-04-30
meta_desc: Build Docker images faster with Pulumi using BuildKit, buildx, multi-stage Dockerfiles, registry caching, and the dedicated Docker Build provider.
meta_image: meta.png
authors:
    - monica-rodriguez
    - guinevere-saenger
aliases:
    - /blog/build-images-50x-faster-docker-v4/
tags:
    - containers
    - docker
    - providers
    - features
---

**How do I speed up Docker image builds with Pulumi?** Use [BuildKit](https://docs.docker.com/build/buildkit/) (the default since Docker 23), enable a registry or layer cache so repeated builds reuse work, write a multi-stage Dockerfile so production images skip build-time dependencies, and reach for the dedicated [Docker Build provider](/registry/packages/docker-build/) when you need buildx features like multi-platform images, build secrets, or Docker Build Cloud. With these techniques together, repeat builds in a Pulumi program commonly drop from minutes to seconds.

<!--more-->

## TL;DR

* **BuildKit is the default** in current Docker releases and in the Pulumi Docker providers — you generally do not need to opt in.
* **Cache your layers somewhere persistent.** A registry cache (`cacheFrom` / `cacheTo`) is what makes CI builds fast across runners and contributors.
* **Multi-stage Dockerfiles** are the single biggest win for image size and rebuild speed when you have a compile or bundle step.
* **Use [`pulumi/docker-build`](/registry/packages/docker-build/)** for new projects. It exposes the full buildx surface (multi-platform, secrets, multiple cache backends, Docker Build Cloud).
* **Use [`pulumi/docker`](/registry/packages/docker/) v4+** if you already depend on it — its `docker.Image` resource also rebuilds only on context change and supports BuildKit and registry caching.

### What actually moves the needle

The numbers below are representative of what teams report from a typical Node.js or Python web app (single Dockerfile, ~300 MB final image). Your mileage varies with project size, network, and runner specs — treat this as a directional comparison, not a benchmark suite.

| Configuration | Cold build | Repeat build (no source change) | Repeat build (small source change) |
| --- | --- | --- | --- |
| Legacy builder, no caching | minutes | minutes | minutes |
| BuildKit, local layer cache only | minutes | seconds (cache hit) | tens of seconds |
| BuildKit + multi-stage Dockerfile | minutes | seconds (cache hit) | tens of seconds |
| BuildKit + multi-stage + registry cache (`cacheFrom`/`cacheTo`) | minutes (first run) | seconds (cache hit) | **seconds–tens of seconds, even on a fresh CI runner** |
| `docker-build` provider with buildx + Docker Build Cloud | under 2 min | seconds (cache hit) | seconds |

The headline pattern: each row past the first is dominated by *what the build can skip*, not by raw CPU. Pulumi's job is to wire those caches up declaratively so they keep working across every `pulumi up`.

## How does Pulumi build Docker images?

Pulumi has two providers for image builds, and which one you should use depends on how new your project is.

* The [**Docker provider**](/registry/packages/docker/) (`pulumi/docker`) is the original. Its `docker.Image` resource can build a local context and push to any registry as part of a Pulumi deployment, alongside resources for containers, networks, and volumes. Since v4 it rebuilds only when the build context changes and uses BuildKit by default.
* The [**Docker Build provider**](/registry/packages/docker-build/) (`pulumi/docker-build`) is a newer, dedicated provider focused exclusively on image builds. It exposes Docker's [buildx](https://docs.docker.com/build/) interface, so you get multi-platform builds, multiple cache backends, build secrets, and [Docker Build Cloud](https://www.docker.com/products/build-cloud/) as first-class features.

For new projects, prefer `docker-build`. For existing programs that already use `docker.Image`, you do not have to migrate — `docker.Image` continues to receive the speed and caching improvements covered below.

## Why are my Docker builds slow?

Three things make Docker builds slow in practice, and Pulumi addresses each one declaratively.

1. **No cache, or the wrong cache.** A fresh CI runner has no local Docker layers. Without a remote cache, every build reinstalls every dependency.
1. **Cache busting on noise.** If your Dockerfile copies `package.json` and the rest of your source in the same step, every source change invalidates the dependency-install layer. Order layers from least-changing to most-changing.
1. **Building dev tooling into the production image.** Compilers, linters, and test frameworks have no business in a runtime image. Multi-stage builds let you discard them.

## How do I enable BuildKit and registry caching in Pulumi?

BuildKit has been the default builder since Docker 23 and is the default in both Pulumi providers. The piece you usually have to configure is *where the cache lives* — local disk on a developer laptop is fine, but for CI you almost always want a registry cache so layers persist across runners.

### With the Docker Build provider (recommended)

```typescript
import * as docker_build from "@pulumi/docker-build";

const image = new docker_build.Image("my-image", {
    tags: ["docker.io/pulumibot/demo-image:latest"],
    context: { location: "./app" },
    dockerfile: { location: "./app/Dockerfile" },
    platforms: [
        "linux/amd64",
        "linux/arm64",
    ],
    cacheFrom: [{ registry: { ref: "docker.io/pulumibot/demo-image:cache" } }],
    cacheTo: [{ registry: { ref: "docker.io/pulumibot/demo-image:cache", mode: "max" } }],
    push: true,
});
```

`cacheFrom` and `cacheTo` together are the important pair: the first run populates the cache, every later run on any machine pulls it. `mode: "max"` exports cache for every layer, not just the final ones.

### With the Docker provider (`docker.Image`)

```typescript
import * as docker from "@pulumi/docker";

const image = new docker.Image("my-image", {
    imageName: "docker.io/pulumibot/demo-image:latest",
    build: {
        context: "app",
        dockerfile: "Dockerfile",
        platform: "linux/amd64",
        cacheFrom: {
            images: ["docker.io/pulumibot/demo-image:cache-base"],
        },
    },
});
```

The `docker.Image` resource accepts a list of cache images via `cacheFrom.images`. Tag a previous build with a stable cache tag (for example, `:cache-base`) and reference it here so subsequent builds reuse its layers.

## How do I write a Dockerfile that builds fast?

The Dockerfile matters at least as much as the Pulumi code wrapping it. Two patterns do most of the work.

**Order layers least-volatile first.** Copy lockfiles and run dependency installs *before* copying source code. That way changing a `.ts` file does not bust the `npm ci` layer.

```dockerfile
# Dependencies — only invalidates when lockfiles change
COPY package.json package-lock.json ./
RUN npm ci

# Source — changes constantly, but the dependency layer above survives
COPY . .
RUN npm run build
```

**Use multi-stage builds to drop tooling.** Compile in a fat image, copy the artifact into a slim one. The runtime image stays small and the build stage gets cached independently.

```dockerfile
FROM node:20 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-slim AS runtime
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```

When you combine multi-stage with a registry cache (`cacheTo` mode `max`), CI runs on fresh machines reuse both stages — the row in the table above where small source changes finish in 10–30 seconds.

## How do I build multi-platform images with Pulumi?

Use the `docker-build` provider and pass a list to `platforms`. BuildKit will build all variants in parallel and push a manifest list, so a single tag serves whatever architecture the puller needs.

```typescript
const image = new docker_build.Image("api", {
    tags: ["ghcr.io/example/api:latest"],
    context: { location: "./api" },
    platforms: [
        "linux/amd64",
        "linux/arm64",
    ],
    push: true,
});
```

If you are still on `docker.Image`, the `build.platform` field accepts a single target (for example, `"linux/amd64"`); for true multi-arch manifests, prefer `docker-build`.

## How do I see Docker build output in Pulumi?

Filtered Docker build and push logs render directly in `pulumi up` output for both providers, so you can debug a failing layer without leaving your Pulumi run. With the Docker Build provider, structured progress shows per-stage timing — useful when you are trying to figure out *which* layer is the slow one.

## How do I migrate an older `docker.Image` program?

If you are upgrading from a pre-v4 program, `pulumi-docker` v4 reshaped the `docker.Image` resource and renamed several supporting types, but does not manage backend state, so updating the package version and adjusting types is generally enough. The full migration guide lives in the [v4.0.0 release notes](https://github.com/pulumi/pulumi-docker/releases/tag/v4.0.0).

If you are starting fresh or want the full BuildKit feature set, install `pulumi-docker-build` instead and follow the [Docker Build provider getting started guide](/registry/packages/docker-build/).

## Getting started

* [Docker Build provider](/registry/packages/docker-build/) — recommended for new projects.
* [Docker provider](/registry/packages/docker/) — the original, including `docker.Image`, containers, and networks.
* [Introducing the Docker Build provider](/blog/docker-build/) — deeper dive on buildx, secrets, and Docker Build Cloud.

The cheapest performance win in most Pulumi programs is wiring up a registry cache and a multi-stage Dockerfile. Start there, then reach for buildx features as the project grows.
