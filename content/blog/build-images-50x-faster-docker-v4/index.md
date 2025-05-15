---
title: "Pulumi Docker Provider 4.0: Build Images Up To 50x Faster"
date: 2023-03-08T14:00:00-08:00
updated: 2025-03-24
meta_desc: Build Docker images up to 50x faster with Pulumi 4.0. Use BuildKit, smart caching, cross-platform support, and rich Docker logs in IaC output.
meta_image: meta.png
authors:
    - monica-rodriguez
    - guinevere-saenger

tags:
    - containers
    - docker
    - providers
    - pulumi-releases
    - features
    - pulumi-news

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
<div>
    <div class="accordion-item text-2xl py-3 border-b-2 border-t-2">
        <input type="checkbox" class="absolute hidden" id="Transcript" />
        <label for="Transcript" class="accordion-label">
            <h5 class="mt-2 w-2/3">Video Transcript</h5>
            <div class="flex flex-grow justify-end items-center">
                <span class="closed-accordion">+</span>
                <span class="open-accordion hidden">-</span>
            </div>
        </label>
        <div class="accordion-item-body-no-animation text-base">
            <p>
                Welcome to another episode of Modern Infrastructure Wednesday! I’m Aaron Cal, and I’m excited to announce the release of version 4 of the Pulumi Docker Provider. This provider allows you to provision any Docker resources—containers, images, networks, volumes, and more—through your Pulumi programs. One of its most popular features is the docker.Image resource, which lets you build and optionally push a local Docker context to a registry as part of a Pulumi deployment. Based on community feedback, we’ve made several improvements in v4: significantly enhanced build performance (including a reduced need for rebuilds), full support for Docker BuildKit with cross-platform builds, richer Docker build logs displayed in the Pulumi output, and support for both Pulumi YAML and Pulumi Java.
            </p>
            <p>
To showcase these updates, I adapted a simple MERN stack grocery list app, originally created by my colleague Christian, and containerized it for local Docker use. The app consists of a MongoDB database, a Node.js/Express backend, and a React frontend—all running locally in Docker. Using the updated Docker provider, we configure our network, define Docker images from a folder containing the app, and build them with BuildKit enabled. We also use a MongoDB community image to create a database container. Environment variables like the database URL are passed between services using a shared local Docker network.
            </p>
            <p>
Once the setup is complete, we run pulumi stack init to initialize the project, followed by pulumi up to deploy the resources. Pulumi creates six total resources, including two images and two containers. During the build process, you’ll now see filtered Docker logs directly in the Pulumi output—another improvement introduced in this release. After deployment, the app is available at a local URL, where we can interact with the grocery list—adding and removing items—and confirm that data is being stored in the MongoDB container.
            </p>
            <p>
This demo shows how easy it is to use Pulumi’s Docker Provider v4 to build and deploy containerized apps with better speed, control, and visibility. To learn more about the new features, check out the blog post from Monica and Guinevere linked below. You can also explore the GitHub repo with the MERN stack example if you’d like to try it out yourself. And of course, don’t forget to like and subscribe if you enjoyed the video—see you next time on Modern Infrastructure Wednesday!
            </p>
        </div>
    </div>
</div>

## Significantly improved performance

To improve the efficiency of the Pulumi Docker Provider, we have changed the default behavior to rebuild only on context change. In addition, the `cacheFrom` option now offers the ability to use a registry as the image cache. By leveraging BuildKit and caching improvements, subsequent rebuilds may be up to 50x faster. This functionality and other improvements of the Pulumi Docker Provider we are announcing today are [highly requested from our community](https://github.com/pulumi/pulumi-docker/issues/132).

## BuildKit support for faster, cross-platform builds

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

## Rich Docker build logs inside Pulumi IaC program output

Filtered docker logs during build and push will now be displayed in the Info box on pulumi up.
[![asciicast](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr.svg)](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr)

## Support for Pulumi YAML and Java SDKs

We announced [Pulumi YAML and Pulumi Java](https://www.pulumi.com/blog/pulumi-universal-iac/) last year and are excited to have extended support to the Pulumi Docker Provider. This release schematizes all Docker resources, which enables auto-support of all Pulumi languages. In addition, this means the `docker.Image` resource can now participate in the CRUD (create, replace, update, delete) lifecycle.

## How to Migrate to Pulumi Docker Provider 4.0

The 4.0 version of the Pulumi Docker Provider consists of a significant overhaul of the `docker.Image` resource. As a result there are some breaking changes to the behavior of the `docker.Image` resource and supporting types, as well as some minor name changes.

As the `docker.Image` resource does not manage any backend state, updating to the 4.0 version does not require any resource imports or stack updates.

For most use cases, migrating should be as simple as updating the `pulumi-docker` version to 4.0.0 and adjusting the Pulumi program code to reflect updated types.

Please find the detailed migration guide in the [release notes for v4.0.0](https://github.com/pulumi/pulumi-docker/releases/tag/v4.0.0).

## Getting started

The Pulumi Docker Provider has everything you need to build, run, and push Docker images for any container registry. Visit the [Pulumi Docker Provider installation and configuration](https://www.pulumi.com/registry/packages/docker/installation-configuration/) page to start building your next image now!
