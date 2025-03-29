---
title: "Pulumi Docker Provider 4.0: Build Images Up To 50x Faster"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2023-03-08T14:00:00-08:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Create Docker images up to 50x faster with reduced need for rebuilds, Docker
  BuildKit, and caching improvements.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
  - monica-rodriguez
  - guinevere-saenger

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - containers
  - docker
  - providers
  - pulumi-releases
  - features
  - pulumi-news

search:
  keywords:
    - Docker
    - BuildKit
    - Docker Provider
    - Image Resource
---

The [Pulumi Docker Provider](/registry/packages/docker) has been a top Pulumi provider since it launched in 2018. It can be used to provision any of the resources available in Docker, including containers, images, networks, volumes and more.

One of the most heavily used features of this provider is the `docker.Image` resource, which enables Pulumi users to build and (optionally) push a local Docker context (like an application folder) to a registry as part of a Pulumi deployment. Today we are excited to announce a set of improvements to the `docker.Image` resource driven by the feedback we have received from our community. This set of improvements includes:

* Significantly improved performance (including reduced need for rebuilds)
* BuildKit support (including cross-platform builds)
* Rich Docker build logs inside Pulumi IaC program output
* Pulumi YAML and Pulumi Java support

<!--more-->

Our friends Nikhil Benesch and the Materialize team created a Docker image provider that demonstrated better workflows with Docker BuildKit and we’re excited to finally make these improvements part of our official Pulumi Docker Provider.

Below is a video walkthrough of using the v4 Docker provider:
{{< youtube "kr0RZzv-pUI?rel=0" >}}

### Significantly improved performance

To improve the efficiency of the Pulumi Docker Provider, we have changed the default behavior to rebuild only on context change. In addition, the `cacheFrom` option now offers the ability to use a registry as the image cache. By leveraging BuildKit and caching improvements, subsequent rebuilds may be up to 50x faster. This functionality and other improvements of the Pulumi Docker Provider we are announcing today are [highly requested from our community](https://github.com/pulumi/pulumi-docker/issues/132).

### BuildKit support

The enhanced functionality and performance provided by the [Docker BuildKit](https://docs.docker.com/build/buildkit/) can now be fully leveraged in your Pulumi programs. BuildKit is now the default builder version mode. The V1 builder can still be accessed by specifying `Build.BuilderVersion=BuilderV1`. BuildKit comes with functionality to improve your builds’ performance and the reusability of your Dockerfiles. Cross-platform builds are now supported, enabling image building for a target container runtime that is different from the build environment.

```typescript
import * as docker from "@pulumi/docker";
const img = new docker.Image("my-image", {
    imageName: "docker.io/pulumibot/demo-image:latest",
    build: {
        context: "app",
        dockerfile: "Dockerfile",
        args: {
            "BUILDKIT_INLINE_CACHE": "1"
        },
        builderVersion: "BuilderBuildKit", // can also be set to `BuilderV1`
        cacheFrom: {
            images: ["docker.io/pulumibot/demo-image:cache-base"]
        },
        platform: "linux/amd64",
    }
});
```

### Rich Docker build logs inside Pulumi IaC program output

Filtered docker logs during build and push will now be displayed in the Info box on pulumi up.
[![asciicast](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr.svg)](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr)

### Pulumi YAML and Pulumi Java support

We announced [Pulumi YAML and Pulumi Java](https://www.pulumi.com/blog/pulumi-universal-iac/) last year and are excited to have extended support to the Pulumi Docker Provider. This release schematizes all Docker resources, which enables auto-support of all Pulumi languages. In addition, this means the `docker.Image` resource can now participate in the CRUD (create, replace, update, delete) lifecycle.

### Migrating to 4.0

The 4.0 version of the Pulumi Docker Provider consists of a significant overhaul of the `docker.Image` resource. As a result there are some breaking changes to the behavior of the `docker.Image` resource and supporting types, as well as some minor name changes.

As the `docker.Image` resource does not manage any backend state, updating to the 4.0 version does not require any resource imports or stack updates.

For most use cases, migrating should be as simple as updating the `pulumi-docker` version to 4.0.0 and adjusting the Pulumi program code to reflect updated types.

Please find the detailed migration guide in the [release notes for v4.0.0](https://github.com/pulumi/pulumi-docker/releases/tag/v4.0.0).

### Getting started

The Pulumi Docker Provider has everything you need to build, run, and push Docker images for any container registry. Visit the [Pulumi Docker Provider installation and configuration](https://www.pulumi.com/registry/packages/docker/installation-configuration/) page to start building your next image now!
