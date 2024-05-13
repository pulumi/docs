---
title: "Introducing the new Docker Build provider"
date: 2024-04-25T09:00:00-07:00
draft: false
meta_desc: >-
    Pulumi's new Docker Build provider offers support for Docker builds using modern buildx/BuildKit APIs.
meta_image: meta.png
authors:
    - bryce-lampe
tags:
    - docker
    - buildx
    - buildkit
    - containers
---

Deploying and managing containerized workloads is one of Pulumi's fastest-growing areas. Standing up managed container services and Kubernetes clusters is a common area for automation, and many of our customers use Pulumi to automate building and publishing images to their registry of choice.

Given this critical use case, we are thrilled to introduce the latest addition to the Pulumi ecosystem: the new [Docker Build provider](https://www.pulumi.com/registry/packages/docker-build/), designed to streamline and modernize Docker image builds from your Pulumi programs.

This new addition expands upon the solid foundation of our highly utilized [Docker provider]. It elevates the `docker.Image` resource, one of the most heavily used and most powerful resources in the Pulumi ecosystem, into its very own dedicated package. By fully embracing the power of [BuildKit], the Docker Build provider brings many new features to support the best-in-class Docker capabilities developers love.

The new provider exposes Docker's next-gen [buildx] interface, so now even your most complex Docker images can be handled by Pulumi. This is a remarkably flexible and versatile tool for building images and includes key features such as,

* __Multi-platform image support__: Build images that run seamlessly across different hardware architectures.
* __Advanced caching mechanisms__: Speed up builds and reduce resource consumption by utilizing cache backends like S3, GitHub Actions, local disk, and more.
* __Support for build secrets__: Unlike building images with the `docker` CLI, which requires juggling environment variables or files on disk, Pulumi's first-class support for secrets means you can now safely and efficiently incorporate sensitive information into your builds. With Pulumi ESC ([Environments, Secrets, and Configuration](../environments-secrets-configurations-management)), it's easy to share build secrets with other developers and teams.
* __Support for multiple export types__: Export your images to registries, disk, or blob storage to increase the power and flexibility of your workflows.
* __Support for Docker Build Cloud__: Use [Docker Build Cloud](https://www.docker.com/products/build-cloud/) to offload your builds and caches to the cloud, enhancing productivity and performance.

  {{< video title="Docker Build Cloud" src="dbc.mp4" autoplay="true" loop="true" >}}

## A brief history

Pulumi first introduced the [Docker provider] in 2018, and it has been widely adopted since. Over the years, Pulumi has invested in the Docker provider, notably introducing version 4.0 [last year](../build-images-50x-faster-docker-v4) and additional improvements like `build-on-preview` behavior.

At the same time, the Docker build ecosystem has seen tremendous advancements in how images can be built and distributed. These changes were initially experimental, but they became official when [BuildKit] graduated to become the
default builder in Docker version 23.

We have heard many requests from users to expose more [BuildKit] functionality in the Docker provider. After some consideration, we decided that a new, standalone provider focused exclusively on building images would provide the best overall user experience. In addition, it allows Pulumi to stay current with the evolving Docker build landscape.

## Getting started

Add the `docker-build` package to your Pulumi program to take full advantage of modern image builds.

{{< chooser language "typescript,python,csharp,go,yaml,java" / >}}
{{% choosable language typescript %}}

```typescript
import * as docker_build from "@pulumi/docker-build";
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_docker_build as docker_build
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using DockerBuild = Pulumi.DockerBuild;
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import "github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
    my-image:
        type: docker-build:Image
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.dockerbuild.Image
```

{{% /choosable %}}

Suppose your Pulumi program has a subfolder called `./app` that contains a file named `Dockerfile` (its contents can be as simple as `FROM alpine`). In that case, the example below shows:

* how to build a multi-platform image (`linux/amd64` and `linux/arm64`),
* publish the image to a remote AWS ECR registry, and;
* use an inline cache to speed up subsequent builds.

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi"
import * as aws from "@pulumi/aws";
import * as docker_build from "@pulumi/docker-build";

// Create an ECR repository for pushing.
const ecrRepository = new aws.ecr.Repository("ecr-repository", {});

// Grab auth credentials for ECR.
const authToken = aws.ecr.getAuthorizationTokenOutput({
    registryId: ecrRepository.registryId,
});

// Build and push an image to ECR with inline caching.
const myImage = new docker_build.Image("my-image", {
    // Tag our image with our ECR repository's address.
    tags: [pulumi.interpolate`${ecrRepository.repositoryUrl}:latest`],
    context: {
        location: "./app",
    },
    // Use the pushed image as a cache source.
    cacheFrom: [{
        registry: {
            ref: pulumi.interpolate`${ecrRepository.repositoryUrl}:latest`,
        },
    }],
    // Include an inline cache with our pushed image.
    cacheTo: [{
        inline: {},
    }],
    // Build a multi-platform image manifest for ARM and AMD.
    platforms: [
        "linux/amd64",
        "linux/arm64",
    ],
    // Push the final result to ECR.
    push: true,
    // Provide our ECR credentials.
    registries: [{
        address: ecrRepository.repositoryUrl,
        password: authToken.password,
        username: authToken.userName,
    }],
});

// Export a ref for the pushed images so we can deploy it.
export const ref = myImage.ref;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_docker_build as docker_build

# Create an ECR repository for pushing.
ecr_repository = aws.ecr.Repository("ecr-repository")

# Grab auth credentials for ECR.
auth_token = aws.ecr.get_authorization_token_output(registry_id=ecr_repository.registry_id)

# Build and push an image to ECR with inline caching.
my_image = docker_build.Image("my-image",
    # Tag our image with our ECR repository's address.
    tags=[ecr_repository.repository_url.apply(lambda repository_url: f"{repository_url}:latest")],
    context=docker_build.BuildContextArgs(
        location="./app",
    ),
    # Use the pushed image as a cache source.
    cache_from=[docker_build.CacheFromArgs(
        registry=docker_build.CacheFromRegistryArgs(
            ref=ecr_repository.repository_url.apply(lambda repository_url: f"{repository_url}:latest"),
        ),
    )],
    # Include an inline cache with our pushed image.
    cache_to=[docker_build.CacheToArgs(
        inline=docker_build.CacheToInlineArgs(),
    )],
    # Build a multi-platform image manifest for ARM and AMD.
    platforms=[
        docker_build.Platform.LINUX_AMD64,
        docker_build.Platform.LINUX_ARM64,
    ],
    # Push the final result to ECR.
    push=True,
    # Provide our ECR credentials.
    registries=[docker_build.RegistryArgs(
        address=ecr_repository.repository_url,
        password=auth_token.password,
        username=auth_token.user_name,
    )],
)

# Export a ref for the pushed images so we can deploy it.
pulumi.export("ref", my_image.ref)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;
using DockerBuild = Pulumi.DockerBuild;

return await Deployment.RunAsync(() =>
{
    // Create an ECR repository for pushing.
    var ecrRepository = new Aws.Ecr.Repository("ecr-repository");

    // Grab auth credentials for ECR.
    var authToken = Aws.Ecr.GetAuthorizationToken.Invoke(new()
    {
        RegistryId = ecrRepository.RegistryId,
    });

    // Build and push an image to ECR with inline caching.
    var myImage = new DockerBuild.Image("my-image", new()
    {
        // Tag our image with our ECR repository's address.
        Tags = new[]
        {
            ecrRepository.RepositoryUrl.Apply(repositoryUrl => $"{repositoryUrl}:latest"),
        },
        Context = new DockerBuild.Inputs.BuildContextArgs
        {
            Location = "./app",
        },
        // Use the pushed image as a cache source.
        CacheFrom = new[]
        {
            new DockerBuild.Inputs.CacheFromArgs
            {
                Registry = new DockerBuild.Inputs.CacheFromRegistryArgs
                {
                    Ref = ecrRepository.RepositoryUrl.Apply(repositoryUrl => $"{repositoryUrl}:latest"),
                },
            },
        },
        // Include an inline cache with our pushed image.
        CacheTo = new[]
        {
            new DockerBuild.Inputs.CacheToArgs
            {
                Inline = null,
            },
        },
        // Build a multi-platform image manifest for ARM and AMD.
        Platforms = new[]
        {
            DockerBuild.Platform.Linux_amd64,
            DockerBuild.Platform.Linux_arm64,
        },
        // Push the final result to ECR.
        Push = true,
        // Provide our ECR credentials.
        Registries = new[]
        {
            new DockerBuild.Inputs.RegistryArgs
            {
                Address = ecrRepository.RepositoryUrl,
                Password = authToken.Apply(getAuthorizationTokenResult => getAuthorizationTokenResult.Password),
                Username = authToken.Apply(getAuthorizationTokenResult => getAuthorizationTokenResult.UserName),
            },
        },
    });

    // Export a ref for the pushed images so we can deploy it.
    return new Dictionary<string, object?>
    {
        ["ref"] = myImage.Ref,
    };
});

```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "fmt"

    "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ecr"
    "github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an ECR repository for pushing.
        ecrRepository, err := ecr.NewRepository(ctx, "ecr-repository", nil)
        if err != nil {
            return err
        }

        // Grab auth credentials for ECR.
        authToken := ecr.GetAuthorizationTokenOutput(ctx, ecr.GetAuthorizationTokenOutputArgs{
            RegistryId: ecrRepository.RegistryId,
        }, nil)

        // Build and push an image to ECR with inline caching.
        myImage, err := dockerbuild.NewImage(ctx, "my-image", &dockerbuild.ImageArgs{
            // Tag our image with our ECR repository's address.
            Tags: pulumi.StringArray{
                ecrRepository.RepositoryUrl.ApplyT(func(repositoryUrl string) (string, error) {
                    return fmt.Sprintf("%v:latest", repositoryUrl), nil
                }).(pulumi.StringOutput),
            },
            Context: &dockerbuild.BuildContextArgs{
                Location: pulumi.String("./app"),
            },
            // Use the pushed image as a cache source.
            CacheFrom: dockerbuild.CacheFromArray{
                &dockerbuild.CacheFromArgs{
                    Registry: &dockerbuild.CacheFromRegistryArgs{
                        Ref: ecrRepository.RepositoryUrl.ApplyT(func(repositoryUrl string) (string, error) {
                            return fmt.Sprintf("%v:latest", repositoryUrl), nil
                        }).(pulumi.StringOutput),
                    },
                },
            },
            // Include an inline cache with our pushed image.
            CacheTo: dockerbuild.CacheToArray{
                &dockerbuild.CacheToArgs{
                    Inline: nil,
                },
            },
            // Build a multi-platform image manifest for ARM and AMD.
            Platforms: dockerbuild.PlatformArray{
                dockerbuild.Platform_Linux_amd64,
                dockerbuild.Platform_Linux_arm64,
            },
            // Push the final result to ECR.
            Push: pulumi.Bool(true),
            // Provide our ECR credentials.
            Registries: dockerbuild.RegistryArray{
                &dockerbuild.RegistryArgs{
                    Address: ecrRepository.RepositoryUrl,
                    Password: authToken.ApplyT(func(authToken ecr.GetAuthorizationTokenResult) (*string, error) {
                        return &authToken.Password, nil
                    }).(pulumi.StringPtrOutput),
                    Username: authToken.ApplyT(func(authToken ecr.GetAuthorizationTokenResult) (*string, error) {
                        return &authToken.UserName, nil
                    }).(pulumi.StringPtrOutput),
                },
            },
        })
        if err != nil {
            return err
        }

        // Export a ref for the pushed images so we can deploy it.
        ctx.Export("ref", myImage.Ref)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
description: Push to AWS ECR with caching
name: ecr
outputs:
    ref: ${my-image.ref}
resources:
    # Create an ECR repository for pushing.
    ecr-repository:
        type: aws:ecr:Repository

    # Build and push an image to ECR with inline caching.
    my-image:
        type: docker-build:Image
        properties:
            # Tag our image with our ECR repository's address.
            tags:
                - ${ecr-repository.repositoryUrl}:latest
            context:
                location: ./app
            # Use the pushed image as a cache source.
            cacheFrom:
                - registry:
                    ref: ${ecr-repository.repositoryUrl}:latest
            # Include an inline cache with our pushed image.
            cacheTo:
                - inline: {}
            # Build a multi-platform image manifest for ARM and AMD.
            platforms:
                - linux/amd64
                - linux/arm64
            # Push the final result to ECR.
            push: true
            # Provide our ECR credentials.
            registries:
                - address: ${ecr-repository.repositoryUrl}
                  password: ${auth-token.password}
                  username: ${auth-token.userName}

runtime: yaml
variables:
    auth-token:
        # Grab auth credentials for ECR.
        fn::aws:ecr:getAuthorizationToken:
            registryId: ${ecr-repository.registryId}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myapp;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.ecr.Repository;
import com.pulumi.aws.ecr.EcrFunctions;
import com.pulumi.aws.ecr.inputs.GetAuthorizationTokenArgs;
import com.pulumi.dockerbuild.Image;
import com.pulumi.dockerbuild.ImageArgs;
import com.pulumi.dockerbuild.inputs.CacheFromArgs;
import com.pulumi.dockerbuild.inputs.CacheFromRegistryArgs;
import com.pulumi.dockerbuild.inputs.CacheToArgs;
import com.pulumi.dockerbuild.inputs.CacheToInlineArgs;
import com.pulumi.dockerbuild.inputs.BuildContextArgs;
import com.pulumi.dockerbuild.inputs.RegistryArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Create an ECR repository for pushing.
        var ecrRepository = new Repository("ecrRepository");

        // Grab auth credentials for ECR.
        final var authToken = EcrFunctions.getAuthorizationToken(GetAuthorizationTokenArgs.builder()
            .registryId(ecrRepository.registryId())
            .build());

        // Build and push an image to ECR with inline caching.
        var myImage = new Image("myImage", ImageArgs.builder()
            // Tag our image with our ECR repository's address.
            .tags(ecrRepository.repositoryUrl().applyValue(repositoryUrl -> String.format("%s:latest", repositoryUrl)))
            .context(BuildContextArgs.builder()
                .location("./app")
                .build())
            // Use the pushed image as a cache source.
            .cacheFrom(CacheFromArgs.builder()
                .registry(CacheFromRegistryArgs.builder()
                    .ref(ecrRepository.repositoryUrl().applyValue(repositoryUrl -> String.format("%s:latest", repositoryUrl)))
                    .build())
                .build())
            // Include an inline cache with our pushed image.
            .cacheTo(CacheToArgs.builder()
                .inline()
                .build())
            // Build a multi-platform image manifest for ARM and AMD.
            .platforms(
                "linux/amd64",
                "linux/arm64")
            // Push the final result to ECR.
            .push(true)
            // Provide our ECR credentials.
            .registries(RegistryArgs.builder()
                .address(ecrRepository.repositoryUrl())
                .password(authToken.applyValue(getAuthorizationTokenResult -> getAuthorizationTokenResult).applyValue(authToken -> authToken.applyValue(getAuthorizationTokenResult -> getAuthorizationTokenResult.password())))
                .username(authToken.applyValue(getAuthorizationTokenResult -> getAuthorizationTokenResult).applyValue(authToken -> authToken.applyValue(getAuthorizationTokenResult -> getAuthorizationTokenResult.userName())))
                .build())
            .build());

        ctx.export("ref", myImage.ref());
    }
}
```

{{% /choosable %}}

The Pulumi output, `ref`, provides a convenient way to reference the pushed image in downstream Pulumi resources like [ECS TaskDefinitions](https://www.pulumi.com/registry/packages/aws/api-docs/ecs/taskdefinition/) or [Kubernetes Deployments](https://www.pulumi.com/registry/packages/kubernetes/api-docs/apps/v1/deployment/).

## Migrating from docker.Image to docker_build.Image

The new `docker_build.Image` replaces the old `docker.Image` resource. It adds new features and addresses many bugs with the previous resource by fully aligning with Docker's underlying [buildx] commands. From now on, we will continue to invest in Docker Build and the `docker_build.Image` resource.

We do not expect to make further changes to `docker.Image`. It will remain available for the foreseeable future, so you can continue using it if it meets your needs. However, we **recommend** you migrate your images to `docker_build.Image` to get the best possible support, features, and performance. We expect to deprecate the `docker.Image` resource in the future.

The migration process is straightforward and detailed in the [API documentation](https://www.pulumi.com/registry/packages/docker-build/api-docs/image/). Docker Build provides a superset functionality over the previous
`docker.Image` resource; thus, you can migrate existing resources without issue. The new Docker Build Image options will look very familiar if you use the Docker command-line tool.

{{% notes %}}

The new Docker Build provider matches the Docker CLI behavior. Thus, it does **not** push images by default. If you want to push to a registry, include [`push: true`](https://www.pulumi.com/registry/packages/docker-build/api-docs/image/#push_nodejs) in the code just as you would include `--push` on the command line.

{{% /notes %}}

{{% notes %}}

The new Docker Build provider builds images by default during [previews](https://www.pulumi.com/docs/cli/commands/pulumi_preview/) to reduce the risk of merging broken images as part of CI pipelines. You can change the default behavior by specifying a [`buildOnPreview`](https://www.pulumi.com/registry/packages/docker-build/api-docs/image/#buildonpreview_nodejs) flag.

{{% /notes %}}

Jump over to the applicable migration guide to learn how to update your existing Pulumi program:

* [Migrating from Docker provider v3](#migrating-from-docker-provider-v3)
* [Migrating from Docker provider v4](#migrating-from-docker-provider-v4)

### Migrating from Docker provider v3

Version 3.x of the Docker provider is still widely used because it exposes `BuildKit` functionality through raw command-line arguments. However, the new Docker Build provider exposes those arguments as top-level fields on the resource.

Reference the below TypeScript code to compare a v3 definition of a `docker.Image` with the new `dockerbuild.Image`. In particular, note the `extraOptions` in v3 are now top-level fields, e.g., `cacheFrom`, `cacheTo`, `platforms`, etc.

```typescript
// v3 Image
const v3 = new docker.Image("v3-image", {
  imageName: "myregistry.com/user/repo:latest",
  localImageName: "local-tag",
  skipPush: false,
  build: {
    dockerfile: "./Dockerfile",
    context: "../app",
    target: "mytarget",
    args: {
      MY_BUILD_ARG: "foo",
    },
    env: {
      DOCKER_BUILDKIT: "1",
    },
    extraOptions: [
      "--cache-from",
      "type=registry,myregistry.com/user/repo:cache",
      "--cache-to",
      "type=registry,myregistry.com/user/repo:cache",
      "--add-host",
      "metadata.google.internal:169.254.169.254",
      "--secret",
      "id=mysecret,src=/local/secret",
      "--ssh",
      "default=/home/runner/.ssh/id_ed25519",
      "--network",
      "host",
      "--platform",
      "linux/amd64",
    ],
  },
  registry: {
    server: "myregistry.com",
    username: "username",
    password: pulumi.secret("password"),
  },
});

// v3 Image after migrating to docker-build.Image
const v3Migrated = new dockerbuild.Image("v3-to-buildx", {
    tags: ["myregistry.com/user/repo:latest", "local-tag"],
    push: true,
    dockerfile: {
        location: "./Dockerfile",
    },
    context: {
        location: "../app",
    },
    target: "mytarget",
    buildArgs: {
        MY_BUILD_ARG: "foo",
    },
    cacheFrom: [{ registry: { ref: "myregistry.com/user/repo:cache" } }],
    cacheTo: [{ registry: { ref: "myregistry.com/user/repo:cache" } }],
    secrets: {
        mysecret: "value",
    },
    addHosts: ["metadata.google.internal:169.254.169.254"],
    ssh: {
        default: ["/home/runner/.ssh/id_ed25519"],
    },
    network: "host",
    platforms: ["linux/amd64"],
    registries: [{
        address: "myregistry.com",
        username: "username",
        password: pulumi.secret("password"),
    }],
});

```

### Migrating from Docker provider v4

The new Docker Build provider largely exposes the same fields as v4, but the fields are pluralized or renamed to better align with the Docker CLI.

Reference the below TypeScript code to compare a v4 definition of a `docker.Image` with the new `dockerbuild.Image`. In particular, note the top-level, pluralized names, e.g., `registries`, `platforms`, etc.

```typescript
// v4 Image
const v4 = new docker.Image("v4-image", {
    imageName: "myregistry.com/user/repo:latest",
    skipPush: false,
    build: {
        dockerfile: "./Dockerfile",
        context: "../app",
        target: "mytarget",
        args: {
            MY_BUILD_ARG: "foo",
        },
        cacheFrom: {
            images: ["myregistry.com/user/repo:cache"],
        },
        addHosts: ["metadata.google.internal:169.254.169.254"],
        network: "host",
        platform: "linux/amd64",
    },
    buildOnPreview: true,
    registry: {
        server: "myregistry.com",
        username: "username",
        password: pulumi.secret("password"),
    },
});

// v4 Image after migrating to docker-build.Image
const v4Migrated = new dockerbuild.Image("v4-to-buildx", {
    tags: ["myregistry.com/user/repo:latest"],
    push: true,
    dockerfile: {
        location: "./Dockerfile",
    },
    context: {
        location: "../app",
    },
    target: "mytarget",
    buildArgs: {
        MY_BUILD_ARG: "foo",
    },
    cacheFrom: [{ registry: { ref: "myregistry.com/user/repo:cache" } }],
    cacheTo: [{ registry: { ref: "myregistry.com/user/repo:cache" } }],
    addHosts: ["metadata.google.internal:169.254.169.254"],
    network: "host",
    platforms: ["linux/amd64"],
    registries: [{
        address: "myregistry.com",
        username: "username",
        password: pulumi.secret("password"),
    }],
});

```

## Conclusion

Launching the new [Docker Build provider] marks a significant milestone in modernizing container management for developers. The new package, which contains the `docker_build.Image` resource reflects our commitment to innovation and user-centric development. By incorporating the latest [BuildKit] technology, the Docker Build provider supports the newest features, enhances multi-architecture builds, and improves caching strategies. Moreover, its integration with [Docker Build Cloud](https://www.docker.com/products/build-cloud/) underscores our dedication to providing a cutting-edge toolset for developers. This launch is a testament to our ongoing efforts to modernize and improve how developers build images.

Check out our [documentation](https://www.pulumi.com/registry/packages/docker-build/) for more details on utilizing the Docker Build provider.

If you are still wondering, "Which provider should I use?" the answer depends on whether you are doing anything related to `docker build`.

| Provider               | Use cases                                                                                                                                                                                                                                                          |
| ----------------       | --------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                           |
| `@pulumi/docker-build` | Use this provider to build and push Docker images. Ideal for scenarios requiring automation of image creation with Docker, including setting up CI/CD pipelines for Docker image generation.                                                                |
| `@pulumi/docker`       | Use this provider for everything else, including managing local Docker containers, networks, and volumes on the host machine.                                                                                                                                      |

[buildx]: https://docs.docker.com/reference/cli/docker/buildx/build/
[BuildKit]: https://docs.docker.com/build/buildkit/
[Docker provider]: https://www.pulumi.com/registry/packages/docker/
[inline cache]: https://docs.docker.com/build/cache/backends/inline/
[Docker Build provider]: https://www.pulumi.com/registry/packages/docker-build/
