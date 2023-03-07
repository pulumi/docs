---
title: "Pulumi Docker Provider 4.0: Build Images Up To 50x Faster"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2023-02-28T09:00:00-05:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Create Docker images up to 50x faster with reduced need for rebuilds, Docker BuildKit, and caching improvements.

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

---

The Pulumi Docker Provider has been a top Pulumi provider since it launched in 2018. It can be used to provision any of the resources available in Docker, including managing containers, images, networks, volumes and more.

One of the most heavily used features of this provider is the `docker.Image` resource, which enables Pulumi users to build and (optionally) push a local Docker context (like an application folder), to a registry as part of a Pulumi deployment. Today we are excited to announce a set of improvements to the Pulumi Docker Provider Image Resource driven by the feedback we have received from our community. This set of improvements includes:

* Significantly improved performance (including reduced need for rebuilds)
* BuildKit support (including cross-platform builds)
* Rich Docker build logs inside Pulumi IaC
* Pulumi YAML and Pulumi Java support

<!--more-->

### Significantly improved performance

To improve the efficiency of the Docker Provider, we have changed the default behavior to rebuild only on context change. In addition, the `cacheFrom` option now offers the ability to use a registry as the image cache. By leveraging BuildKit and caching improvements, subsequent rebuilds may be up to 50x faster. This functionality and other improvements of the Docker Provider we are announcing today are [highly requested from our community](https://github.com/pulumi/pulumi-docker/issues/132).

<!-- Add image/gif showing output during build, side by side comparison of old vs new?, or graph with speed comparison -->

### BuildKit support

The enhanced functionality and performance provided by the [Docker BuildKit](https://docs.docker.com/build/buildkit/) is now fully available to be leveraged in your Pulumi programs. BuildKit comes with functionality to improve your builds’ performance and the reusability of your Dockerfiles. Cross-platform builds are now supported, enabling image building for a target container runtime that is different from the build environment. BuildKit is now the default builder version mode. The V1 builder can still be accessed by specifying `Build.BuilderVersion=BuilderV1`.

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

## Rich Docker build logs inside Pulumi IaC

Filtered docker logs during build and push will now be displayed in the Info box on pulumi up.
[![asciicast](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr.svg)](https://asciinema.org/a/I8Xzmfme56ZP4uD6uo2U4i2wr)

### Pulumi YAML and Pulumi Java support

We announced [Pulumi YAML and Pulumi Java](https://www.pulumi.com/blog/pulumi-universal-iac/) last year and are excited to have extended support to the Pulumi Docker Provider. This release schematizes all Docker resources, which enables auto-support of all Pulumi languages. In addition, this means the Docker image resource can now participate in the CRUD (create, replace, update, delete) lifecycle.

### Migrating to 4.0

The 4.0 version of the Docker provider consists of a significant overhaul of the Image Resource.
These changes are mainly a result of either the way Pulumi generates language SDKs from a schematized resource, or of migrating to using the docker-go client library instead of invoking the Docker CLI.
A few additional changes are about streamlining the resource properties available.

#### Inputs

`LocalImageName`: Deprecated. Use `ImageName` in conjunction with `SkipPush:true`.

`Build`: No longer a required input. No longer accepts a string for a custom build context. Use `Build.Context` instead.

`ExtraOptions`: Deprecated. This was a way to pass arbitrary CLI flags to the Docker CLI.
These are being implemented as top-level fields; currently available are:

* `Build.Platform` - note that this can only take a single value currently, not a list of target platforms.
* `Build.Target`
* `Build.CacheFrom` - no longer accepts a boolean. Specify explicitly in images list:
  * `Build.CacheFrom.Images` - replaces `Build.CacheFrom.Stages`, with updated functionality (a list of images to use as build cache)

`Env`: Deprecated. This field’s use case was mainly for passing `DOCKER_BUILDKIT=1` to the CLI invocation of docker build. Use `Build.BuilderVersion` instead. You do not need to specify `Build.BuilderVersion` if you are running in Buildkit mode, which is the default.

`ImageName`: Must be of fully qualified repository format, i.e. `registry.domain.abc/repositoryname/image`. The tag will be inferred as `:latest` unless otherwise specified. `Docker.io` will no longer be automatically inferred.

#### Outputs

`Id`: Deprecated. Use `ImageName` for a unique identifier.

`Digest`: Deprecated as of an older version of pulumi-docker 3.6; this removes it entirely.

#### Language specific package type updates

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language csharp %}}

```csharp
Docker.ImageRegistry → Docker.Inputs.RegistryArgs
Docker.DockerBuild → Docker.Inputs.DockerBuildArgs
```

{{% /choosable %}}

{{% choosable language go %}}

```go
docker.ImageRegistry → docker.Registry
```

{{% /choosable %}}

{{% choosable language python %}}

```python
DockerBuild → DockerBuildArgs
ImageRegistry → RegistryArgs
```

{{% /choosable %}}

{{< /chooser >}}

The Docker Provider Image Resource has everything you need to build, run, and push Docker images for any container registry. Build your next image now!
