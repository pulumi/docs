---
title_tag: "Container Image Build Caching and Deployment Reproducibility | IaC Operations"
meta_desc: Build container images with Pulumi using digest-based tags, registry-backed layer caching, and a build/deploy stack split for fast, reproducible deployments.
title: Container Image Build Caching and Deployment Reproducibility
h1: Container image build caching and deployment reproducibility
menu:
    iac:
        name: Image Build & Caching
        parent: iac-operations
        weight: 47
        identifier: iac-operations-container-image-reproducibility
---

Building a container image as part of a Pulumi program gives you a single, versioned record of what was built, pushed, and deployed. Getting the most out of that record takes a few deliberate choices: how Pulumi decides an image needs rebuilding, how downstream resources reference the result, how CI reuses layers across runs, and how the Dockerfile itself is structured. This guide walks through each of those choices for the [Docker Build provider](/registry/packages/docker-build/) (`docker-build.Image`) and the [Docker provider](/registry/packages/docker/) (`docker.Image`), and shows a complete pattern for keeping image builds reproducible from a developer's laptop through to CI and into production.

## How Pulumi decides to rebuild an image

`docker-build.Image` computes a `contextHash` output, a preliminary hash of the build context (the Dockerfile and the files it references), and uses it during the diff calculation to determine whether an image *may* need to be rebuilt. This preliminary check lets `pulumi preview` report a likely change without invoking a full BuildKit build. It's a hash of your inputs to the build, not of the resulting image, so it only catches changes Pulumi can see: edits to the Dockerfile and files copied into the context. It cannot know if a `FROM` base image was updated upstream, since that's resolved at build time, not diff time. If your Dockerfile pulls `FROM node:20` and a new `20.x` patch lands, the context hash is unchanged and Pulumi does not report a pending rebuild — the next build picks up whatever `node:20` currently resolves to. Pin base images by digest (`FROM node:20@sha256:...`) when you need the build itself, not only Pulumi's plan, to be fully reproducible.

The classic `docker.Image` resource takes a different approach: it always invokes a Docker build on `pulumi up` and delegates the rebuild-avoidance decision entirely to the Docker daemon or BuildKit's own layer cache, rather than computing a context hash of its own. In practice this means `docker.Image` is more prone to appearing to "do work" on every update — the image is always rebuilt from Pulumi's perspective, even if BuildKit determines every layer is already cached and the build completes in milliseconds. `docker-build.Image`'s context hash gives Pulumi a better signal for `preview` output and change summaries, on top of whatever caching you configure for the underlying build.

Either way, a rebuild recalculating the same layers is not the expensive part — pushing a materially unchanged image to a registry and forcing every downstream resource that references it to redeploy is. That's where digest-based tagging matters.

## Prefer digest-based tags over `latest`

`docker-build.Image` exposes two outputs worth knowing the difference between:

- `ref` — a convenience output containing a fully qualified tag with digest, if the image was pushed to any registry (`repository:tag@sha256:...`). If multiple tags were pushed, `ref` picks one arbitrarily, so it isn't guaranteed to be stable when you're pushing to more than one tag or registry.
- `digest` — a SHA256 digest of the exported image, always a single stable value regardless of how many tags or registries were involved. This is the output to use when you need a precise, stable reference for downstream resources.

The classic `docker.Image` resource has an equivalent pair: `imageName` (a plain `repository:tag` string with no digest information) and `repoDigest` (`repository@<algorithm>:<hash>`, unique per build and push, available for local images since Docker provider v4.4).

The reason this distinction matters is `latest` — or any other mutable tag. A tag is just a pointer; pushing a new image with the same tag doesn't change the tag string itself, so nothing about the reference tells a downstream resource that the image changed. If an ECS task definition or a Kubernetes Deployment hard-codes `myapp:latest`, Pulumi sees no diff on that field between updates, and won't trigger a new deployment — you're relying on the orchestrator's own pull policy and restart behavior to eventually surface the new image, which is neither immediate nor guaranteed. Reference the image by digest instead, and every new build produces a genuinely different string. Pulumi's diff engine sees the change, and the task definition or Deployment update as part of the same `pulumi up`.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as docker_build from "@pulumi/docker-build";

const repository = new aws.ecr.Repository("app-repository");
const authToken = aws.ecr.getAuthorizationTokenOutput({
    registryId: repository.registryId,
});

const image = new docker_build.Image("app-image", {
    context: {
        location: "./app",
    },
    dockerfile: {
        location: "./app/Dockerfile",
    },
    push: true,
    registries: [{
        address: repository.repositoryUrl,
        username: authToken.userName,
        password: authToken.password,
    }],
    tags: [pulumi.interpolate`${repository.repositoryUrl}:latest`],
});

// image.digest is a stable sha256 digest, unlike the mutable "latest" tag above.
const taskDefinition = new aws.ecs.TaskDefinition("app-task", {
    family: "app",
    requiresCompatibilities: ["FARGATE"],
    networkMode: "awsvpc",
    cpu: "256",
    memory: "512",
    containerDefinitions: pulumi.jsonStringify([{
        name: "app",
        image: pulumi.interpolate`${repository.repositoryUrl}@${image.digest}`,
        essential: true,
        portMappings: [{ containerPort: 8080 }],
    }]),
});

export const imageDigest = image.digest;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_docker_build as docker_build

repository = aws.ecr.Repository("app-repository")
auth_token = aws.ecr.get_authorization_token_output(registry_id=repository.registry_id)

image = docker_build.Image("app-image",
    context={
        "location": "./app",
    },
    dockerfile={
        "location": "./app/Dockerfile",
    },
    push=True,
    registries=[{
        "address": repository.repository_url,
        "username": auth_token.user_name,
        "password": auth_token.password,
    }],
    tags=[repository.repository_url.apply(lambda url: f"{url}:latest")])

# image.digest is a stable sha256 digest, unlike the mutable "latest" tag above.
task_definition = aws.ecs.TaskDefinition("app-task",
    family="app",
    requires_compatibilities=["FARGATE"],
    network_mode="awsvpc",
    cpu="256",
    memory="512",
    container_definitions=pulumi.Output.json_dumps([{
        "name": "app",
        "image": pulumi.Output.all(repository.repository_url, image.digest).apply(
            lambda args: f"{args[0]}@{args[1]}"),
        "essential": True,
        "portMappings": [{"containerPort": 8080}],
    }]))

pulumi.export("image_digest", image.digest)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ecr"
    "github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ecs"
    "github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        repository, err := ecr.NewRepository(ctx, "app-repository", nil)
        if err != nil {
            return err
        }
        authToken := ecr.GetAuthorizationTokenOutput(ctx, ecr.GetAuthorizationTokenOutputArgs{
            RegistryId: repository.RegistryId,
        }, nil)

        image, err := dockerbuild.NewImage(ctx, "app-image", &dockerbuild.ImageArgs{
            Context: &dockerbuild.BuildContextArgs{
                Location: pulumi.String("./app"),
            },
            Dockerfile: &dockerbuild.DockerfileArgs{
                Location: pulumi.String("./app/Dockerfile"),
            },
            Push: pulumi.Bool(true),
            Registries: dockerbuild.RegistryArray{
                &dockerbuild.RegistryArgs{
                    Address:  repository.RepositoryUrl,
                    Username: authToken.UserName(),
                    Password: authToken.Password(),
                },
            },
            Tags: pulumi.StringArray{
                pulumi.Sprintf("%s:latest", repository.RepositoryUrl),
            },
        })
        if err != nil {
            return err
        }

        // image.Digest is a stable sha256 digest, unlike the mutable "latest" tag above.
        _, err = ecs.NewTaskDefinition(ctx, "app-task", &ecs.TaskDefinitionArgs{
            Family:                  pulumi.String("app"),
            RequiresCompatibilities: pulumi.StringArray{pulumi.String("FARGATE")},
            NetworkMode:             pulumi.String("awsvpc"),
            Cpu:                     pulumi.String("256"),
            Memory:                  pulumi.String("512"),
            ContainerDefinitions: pulumi.JSONMarshal([]interface{}{
                map[string]interface{}{
                    "name":      "app",
                    "image":     pulumi.Sprintf("%s@%s", repository.RepositoryUrl, image.Digest),
                    "essential": true,
                    "portMappings": []interface{}{
                        map[string]interface{}{"containerPort": 8080},
                    },
                },
            }),
        })
        if err != nil {
            return err
        }

        ctx.Export("imageDigest", image.Digest)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using DockerBuild = Pulumi.DockerBuild;

return await Deployment.RunAsync(() =>
{
    var repository = new Aws.Ecr.Repository("app-repository");

    var authToken = Aws.Ecr.GetAuthorizationToken.Invoke(new()
    {
        RegistryId = repository.RegistryId,
    });

    var image = new DockerBuild.Image("app-image", new()
    {
        Context = new DockerBuild.Inputs.BuildContextArgs
        {
            Location = "./app",
        },
        Dockerfile = new DockerBuild.Inputs.DockerfileArgs
        {
            Location = "./app/Dockerfile",
        },
        Push = true,
        Registries = new[]
        {
            new DockerBuild.Inputs.RegistryArgs
            {
                Address = repository.RepositoryUrl,
                Username = authToken.Apply(token => token.UserName),
                Password = authToken.Apply(token => token.Password),
            },
        },
        Tags = new[]
        {
            repository.RepositoryUrl.Apply(url => $"{url}:latest"),
        },
    });

    // image.Digest is a stable sha256 digest, unlike the mutable "latest" tag above.
    var taskDefinition = new Aws.Ecs.TaskDefinition("app-task", new()
    {
        Family = "app",
        RequiresCompatibilities = new[] { "FARGATE" },
        NetworkMode = "awsvpc",
        Cpu = "256",
        Memory = "512",
        ContainerDefinitions = Output.Tuple(repository.RepositoryUrl, image.Digest)
            .Apply(t => JsonSerializer.Serialize(new[]
            {
                new
                {
                    name = "app",
                    image = $"{t.Item1}@{t.Item2}",
                    essential = true,
                    portMappings = new[] { new { containerPort = 8080 } },
                },
            })),
    });

    return new Dictionary<string, object?>
    {
        ["imageDigest"] = image.Digest,
    };
});
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
import com.pulumi.aws.ecs.TaskDefinition;
import com.pulumi.aws.ecs.TaskDefinitionArgs;
import com.pulumi.dockerbuild.Image;
import com.pulumi.dockerbuild.ImageArgs;
import com.pulumi.dockerbuild.inputs.BuildContextArgs;
import com.pulumi.dockerbuild.inputs.DockerfileArgs;
import com.pulumi.dockerbuild.inputs.RegistryArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("app-repository");

        final var authToken = EcrFunctions.getAuthorizationToken(GetAuthorizationTokenArgs.builder()
            .registryId(repository.registryId())
            .build());

        var image = new Image("app-image", ImageArgs.builder()
            .context(BuildContextArgs.builder()
                .location("./app")
                .build())
            .dockerfile(DockerfileArgs.builder()
                .location("./app/Dockerfile")
                .build())
            .push(true)
            .registries(RegistryArgs.builder()
                .address(repository.repositoryUrl())
                .username(authToken.applyValue(token -> token.userName()))
                .password(authToken.applyValue(token -> token.password()))
                .build())
            .tags(repository.repositoryUrl().applyValue(url -> url + ":latest"))
            .build());

        // image.digest() is a stable sha256 digest, unlike the mutable "latest" tag above.
        var taskDefinition = new TaskDefinition("app-task", TaskDefinitionArgs.builder()
            .family("app")
            .requiresCompatibilities("FARGATE")
            .networkMode("awsvpc")
            .cpu("256")
            .memory("512")
            .containerDefinitions(Output.tuple(repository.repositoryUrl(), image.digest())
                .applyValue(t -> String.format(
                    "[{\"name\":\"app\",\"image\":\"%s@%s\",\"essential\":true,"
                        + "\"portMappings\":[{\"containerPort\":8080}]}]",
                    t.t1, t.t2)))
            .build());

        ctx.export("imageDigest", image.digest());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

The same principle applies to a Kubernetes `Deployment`: reference `image.digest` (or the equivalent `repoDigest` output on `docker.Image`) in the container spec's `image` field instead of a floating tag, and every `pulumi up` that produces a new image also produces a genuine spec change for Kubernetes to roll out.

## Cache CI builds against a registry

`docker-build.Image` delegates all caching to BuildKit through its `cacheFrom` and `cacheTo` inputs — the equivalents of Docker's `--cache-from` and `--cache-to` flags — rather than reimplementing caching logic itself. That matters for CI: a registry-backed cache (`type=registry` in Docker terms) lets any runner, on any CI system, pull the layers a previous run already built, without needing a persistent local disk or a CI-specific cache feature. The classic `docker.Image` resource's own `cacheFrom` parameter predates BuildKit-native caching and requires extra environment variables to behave correctly; `docker-build.Image`'s version is a thin, direct mapping onto Docker's own cache backends (registry, GitHub Actions, S3, Azure Blob, or local disk), so it behaves exactly the way `docker buildx build --cache-from=... --cache-to=...` would from the command line.

Push the cache to a dedicated tag in the same repository you're already pushing images to. Most registries — including Google Artifact Registry and Docker Hub — accept this as just another manifest push; Amazon ECR needs the OCI-manifest options shown below (`imageManifest` and `ociMediaTypes`) because it doesn't accept BuildKit's default image-index cache manifest.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as docker_build from "@pulumi/docker-build";

const repository = new aws.ecr.Repository("app-repository");
const authToken = aws.ecr.getAuthorizationTokenOutput({
    registryId: repository.registryId,
});

const image = new docker_build.Image("app-image", {
    context: {
        location: "./app",
    },
    push: true,
    registries: [{
        address: repository.repositoryUrl,
        username: authToken.userName,
        password: authToken.password,
    }],
    tags: [pulumi.interpolate`${repository.repositoryUrl}:latest`],
    cacheFrom: [{
        registry: {
            ref: pulumi.interpolate`${repository.repositoryUrl}:cache`,
        },
    }],
    cacheTo: [{
        registry: {
            ref: pulumi.interpolate`${repository.repositoryUrl}:cache`,
            imageManifest: true,
            ociMediaTypes: true,
        },
    }],
});

export const imageRef = image.ref;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_docker_build as docker_build

repository = aws.ecr.Repository("app-repository")
auth_token = aws.ecr.get_authorization_token_output(registry_id=repository.registry_id)

image = docker_build.Image("app-image",
    context={
        "location": "./app",
    },
    push=True,
    registries=[{
        "address": repository.repository_url,
        "username": auth_token.user_name,
        "password": auth_token.password,
    }],
    tags=[repository.repository_url.apply(lambda url: f"{url}:latest")],
    cache_from=[{
        "registry": {
            "ref": repository.repository_url.apply(lambda url: f"{url}:cache"),
        },
    }],
    cache_to=[{
        "registry": {
            "ref": repository.repository_url.apply(lambda url: f"{url}:cache"),
            "image_manifest": True,
            "oci_media_types": True,
        },
    }])

pulumi.export("image_ref", image.ref)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ecr"
    "github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        repository, err := ecr.NewRepository(ctx, "app-repository", nil)
        if err != nil {
            return err
        }
        authToken := ecr.GetAuthorizationTokenOutput(ctx, ecr.GetAuthorizationTokenOutputArgs{
            RegistryId: repository.RegistryId,
        }, nil)

        image, err := dockerbuild.NewImage(ctx, "app-image", &dockerbuild.ImageArgs{
            Context: &dockerbuild.BuildContextArgs{
                Location: pulumi.String("./app"),
            },
            Push: pulumi.Bool(true),
            Registries: dockerbuild.RegistryArray{
                &dockerbuild.RegistryArgs{
                    Address:  repository.RepositoryUrl,
                    Username: authToken.UserName(),
                    Password: authToken.Password(),
                },
            },
            Tags: pulumi.StringArray{
                pulumi.Sprintf("%s:latest", repository.RepositoryUrl),
            },
            CacheFrom: dockerbuild.CacheFromArray{
                &dockerbuild.CacheFromArgs{
                    Registry: &dockerbuild.CacheFromRegistryArgs{
                        Ref: pulumi.Sprintf("%s:cache", repository.RepositoryUrl),
                    },
                },
            },
            CacheTo: dockerbuild.CacheToArray{
                &dockerbuild.CacheToArgs{
                    Registry: &dockerbuild.CacheToRegistryArgs{
                        Ref:           pulumi.Sprintf("%s:cache", repository.RepositoryUrl),
                        ImageManifest: pulumi.Bool(true),
                        OciMediaTypes: pulumi.Bool(true),
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        ctx.Export("imageRef", image.Ref)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using DockerBuild = Pulumi.DockerBuild;

return await Deployment.RunAsync(() =>
{
    var repository = new Aws.Ecr.Repository("app-repository");

    var authToken = Aws.Ecr.GetAuthorizationToken.Invoke(new()
    {
        RegistryId = repository.RegistryId,
    });

    var image = new DockerBuild.Image("app-image", new()
    {
        Context = new DockerBuild.Inputs.BuildContextArgs
        {
            Location = "./app",
        },
        Push = true,
        Registries = new[]
        {
            new DockerBuild.Inputs.RegistryArgs
            {
                Address = repository.RepositoryUrl,
                Username = authToken.Apply(token => token.UserName),
                Password = authToken.Apply(token => token.Password),
            },
        },
        Tags = new[]
        {
            repository.RepositoryUrl.Apply(url => $"{url}:latest"),
        },
        CacheFrom = new[]
        {
            new DockerBuild.Inputs.CacheFromArgs
            {
                Registry = new DockerBuild.Inputs.CacheFromRegistryArgs
                {
                    Ref = repository.RepositoryUrl.Apply(url => $"{url}:cache"),
                },
            },
        },
        CacheTo = new[]
        {
            new DockerBuild.Inputs.CacheToArgs
            {
                Registry = new DockerBuild.Inputs.CacheToRegistryArgs
                {
                    Ref = repository.RepositoryUrl.Apply(url => $"{url}:cache"),
                    ImageManifest = true,
                    OciMediaTypes = true,
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["imageRef"] = image.Ref,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myapp;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ecr.Repository;
import com.pulumi.aws.ecr.EcrFunctions;
import com.pulumi.aws.ecr.inputs.GetAuthorizationTokenArgs;
import com.pulumi.dockerbuild.Image;
import com.pulumi.dockerbuild.ImageArgs;
import com.pulumi.dockerbuild.inputs.BuildContextArgs;
import com.pulumi.dockerbuild.inputs.CacheFromArgs;
import com.pulumi.dockerbuild.inputs.CacheFromRegistryArgs;
import com.pulumi.dockerbuild.inputs.CacheToArgs;
import com.pulumi.dockerbuild.inputs.CacheToRegistryArgs;
import com.pulumi.dockerbuild.inputs.RegistryArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("app-repository");

        final var authToken = EcrFunctions.getAuthorizationToken(GetAuthorizationTokenArgs.builder()
            .registryId(repository.registryId())
            .build());

        var image = new Image("app-image", ImageArgs.builder()
            .context(BuildContextArgs.builder()
                .location("./app")
                .build())
            .push(true)
            .registries(RegistryArgs.builder()
                .address(repository.repositoryUrl())
                .username(authToken.applyValue(token -> token.userName()))
                .password(authToken.applyValue(token -> token.password()))
                .build())
            .tags(repository.repositoryUrl().applyValue(url -> url + ":latest"))
            .cacheFrom(CacheFromArgs.builder()
                .registry(CacheFromRegistryArgs.builder()
                    .ref(repository.repositoryUrl().applyValue(url -> url + ":cache"))
                    .build())
                .build())
            .cacheTo(CacheToArgs.builder()
                .registry(CacheToRegistryArgs.builder()
                    .ref(repository.repositoryUrl().applyValue(url -> url + ":cache"))
                    .imageManifest(true)
                    .ociMediaTypes(true)
                    .build())
                .build())
            .build());

        ctx.export("imageRef", image.ref());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

`imageManifest` and `ociMediaTypes` on the cache-to side aren't strictly required for every registry, but setting both is a safe default — some registries (Amazon ECR among them) reject the non-OCI cache manifest format that BuildKit produces without them.

Because the build lives inside the Pulumi program rather than in a separate `docker build` CI step, the GitHub Actions workflow itself stays simple: it only needs to authenticate and run `pulumi up`.

```yaml
# .github/workflows/deploy.yml
name: Build and deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: infra/package.json
      - run: npm install
        working-directory: infra
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: acme
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Load the ESC environment
        uses: pulumi/esc-action@v3
        with:
          environment: acme/app/ci
      - uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/app/production
          work-dir: infra
```

The ESC environment referenced above supplies the ECR credentials the Pulumi program's AWS provider needs, following the same [OIDC pattern used elsewhere in Pulumi's GitHub Actions guide](/docs/iac/operations/continuous-delivery/github-actions/#authenticate-without-a-stored-token-using-oidc) — no long-lived AWS keys or Docker registry passwords are stored as repository secrets. Swap the `npm install` and `setup-node` steps for your program's language (`pip install -r requirements.txt` with `actions/setup-python@v5`, and so on); everything about the caching behavior above is identical regardless of the language the Pulumi program itself is written in. GitLab CI/CD, Jenkins, and other CI systems follow the same shape: a job that authenticates, installs dependencies, and runs `pulumi up` — the registry-backed cache works identically because it's a property of the registry, not the CI system.

BuildKit also supports a GitHub Actions-native cache backend (`gha`, exposed on `cacheFrom`/`cacheTo` as `{ gha: { scope: "..." } }`), which avoids a registry round trip entirely by using the GitHub Actions cache service. It needs the `ACTIONS_CACHE_URL` and `ACTIONS_RUNTIME_TOKEN` environment variables exported into the job, which the default `GITHUB_TOKEN` doesn't provide on its own — add a step like [`crazy-max/ghaction-github-runtime`](https://github.com/crazy-max/ghaction-github-runtime) before `pulumi up` to export them. Prefer the registry-backed cache shown above when your CI runs across multiple providers or self-hosted runners; reach for `gha` when you're committed to GitHub-hosted runners and want to avoid the extra registry pushes for cache layers.

## Structure the Dockerfile for cache efficiency

Registry and `gha` caching only help if the Dockerfile's layer order lets BuildKit reuse work. The most common anti-pattern is copying the entire application before installing dependencies:

```dockerfile
# Anti-pattern: any source change invalidates the dependency-install layer.
FROM node:20-slim
WORKDIR /app
COPY . .
RUN npm ci --omit=dev
CMD ["node", "server.js"]
```

Because `COPY . .` runs before `npm ci`, changing a single source file invalidates every layer after it, including the dependency install — the most expensive step in most builds. Reorder the Dockerfile so dependency manifests are copied and installed first, and application source is copied last:

```dockerfile
FROM node:20-slim AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

FROM node:20-slim AS runtime
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
CMD ["node", "server.js"]
```

Now a source-only change only invalidates the final `COPY . .` layer; the `deps` stage — and everything the registry cache pulled for it — is reused unchanged. This multi-stage structure also keeps the final image free of build-only tooling that isn't needed at runtime.

BuildKit's `RUN --mount=type=cache` is a complementary technique worth distinguishing from `cacheFrom`/`cacheTo`: it caches a directory (a package manager's download cache, for example) *across builds on the same builder*, without that cache becoming part of any image layer or requiring a registry push at all:

```dockerfile
FROM node:20-slim AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm npm ci --omit=dev
```

Use `--mount=type=cache` to speed up repeated local or single-runner builds by skipping re-downloads; use registry `cacheFrom`/`cacheTo` to share built layers across CI runs and machines that don't share a filesystem. The two are not mutually exclusive — most production Dockerfiles benefit from both.

## Separate the build from the deploy

A build that also deploys couples two concerns that scale differently: builds happen on every commit, deploys happen on a release cadence, and a team often wants different approval gates for each. Splitting them into two Pulumi stacks — a build stack that owns the `docker-build.Image` resource and exports its digest, and a deploy stack that consumes that digest through a `StackReference` — keeps both concerns independently testable and independently promotable across environments.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
// Build stack (acme/app-image/production)
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as docker_build from "@pulumi/docker-build";

const repository = new aws.ecr.Repository("app-repository");
const authToken = aws.ecr.getAuthorizationTokenOutput({
    registryId: repository.registryId,
});

const image = new docker_build.Image("app-image", {
    context: { location: "./app" },
    push: true,
    registries: [{
        address: repository.repositoryUrl,
        username: authToken.userName,
        password: authToken.password,
    }],
    tags: [pulumi.interpolate`${repository.repositoryUrl}:latest`],
});

export const repositoryUrl = repository.repositoryUrl;
export const digest = image.digest;
```

```typescript
// Deploy stack (acme/app-deploy/production)
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const build = new pulumi.StackReference("acme/app-image/production");
const repositoryUrl = build.requireOutput("repositoryUrl");
const digest = build.requireOutput("digest");
const pinnedImage = pulumi.interpolate`${repositoryUrl}@${digest}`;

const taskDefinition = new aws.ecs.TaskDefinition("app-task", {
    family: "app",
    requiresCompatibilities: ["FARGATE"],
    networkMode: "awsvpc",
    cpu: "256",
    memory: "512",
    containerDefinitions: pulumi.jsonStringify([{
        name: "app",
        image: pinnedImage,
        essential: true,
        portMappings: [{ containerPort: 8080 }],
    }]),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Build stack (acme/app-image/production)
import pulumi
import pulumi_aws as aws
import pulumi_docker_build as docker_build

repository = aws.ecr.Repository("app-repository")
auth_token = aws.ecr.get_authorization_token_output(registry_id=repository.registry_id)

image = docker_build.Image("app-image",
    context={"location": "./app"},
    push=True,
    registries=[{
        "address": repository.repository_url,
        "username": auth_token.user_name,
        "password": auth_token.password,
    }],
    tags=[repository.repository_url.apply(lambda url: f"{url}:latest")])

pulumi.export("repository_url", repository.repository_url)
pulumi.export("digest", image.digest)
```

```python
# Deploy stack (acme/app-deploy/production)
import pulumi
import pulumi_aws as aws

build = pulumi.StackReference("acme/app-image/production")
repository_url = build.require_output("repository_url")
digest = build.require_output("digest")
pinned_image = pulumi.Output.all(repository_url, digest).apply(
    lambda args: f"{args[0]}@{args[1]}")

task_definition = aws.ecs.TaskDefinition("app-task",
    family="app",
    requires_compatibilities=["FARGATE"],
    network_mode="awsvpc",
    cpu="256",
    memory="512",
    container_definitions=pulumi.Output.json_dumps([{
        "name": "app",
        "image": pinned_image,
        "essential": True,
        "portMappings": [{"containerPort": 8080}],
    }]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Build stack (acme/app-image/production)
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ecr"
    "github.com/pulumi/pulumi-docker-build/sdk/go/dockerbuild"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        repository, err := ecr.NewRepository(ctx, "app-repository", nil)
        if err != nil {
            return err
        }
        authToken := ecr.GetAuthorizationTokenOutput(ctx, ecr.GetAuthorizationTokenOutputArgs{
            RegistryId: repository.RegistryId,
        }, nil)

        image, err := dockerbuild.NewImage(ctx, "app-image", &dockerbuild.ImageArgs{
            Context: &dockerbuild.BuildContextArgs{
                Location: pulumi.String("./app"),
            },
            Push: pulumi.Bool(true),
            Registries: dockerbuild.RegistryArray{
                &dockerbuild.RegistryArgs{
                    Address:  repository.RepositoryUrl,
                    Username: authToken.UserName(),
                    Password: authToken.Password(),
                },
            },
            Tags: pulumi.StringArray{
                pulumi.Sprintf("%s:latest", repository.RepositoryUrl),
            },
        })
        if err != nil {
            return err
        }

        ctx.Export("repositoryUrl", repository.RepositoryUrl)
        ctx.Export("digest", image.Digest)
        return nil
    })
}
```

```go
// Deploy stack (acme/app-deploy/production)
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ecs"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        build, err := pulumi.NewStackReference(ctx, "acme/app-image/production", nil)
        if err != nil {
            return err
        }
        repositoryUrl := build.GetStringOutput(pulumi.String("repositoryUrl"))
        digest := build.GetStringOutput(pulumi.String("digest"))
        pinnedImage := pulumi.Sprintf("%s@%s", repositoryUrl, digest)

        _, err = ecs.NewTaskDefinition(ctx, "app-task", &ecs.TaskDefinitionArgs{
            Family:                  pulumi.String("app"),
            RequiresCompatibilities: pulumi.StringArray{pulumi.String("FARGATE")},
            NetworkMode:             pulumi.String("awsvpc"),
            Cpu:                     pulumi.String("256"),
            Memory:                  pulumi.String("512"),
            ContainerDefinitions: pulumi.JSONMarshal([]interface{}{
                map[string]interface{}{
                    "name":      "app",
                    "image":     pinnedImage,
                    "essential": true,
                    "portMappings": []interface{}{
                        map[string]interface{}{"containerPort": 8080},
                    },
                },
            }),
        })
        return err
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Build stack (acme/app-image/production)
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using DockerBuild = Pulumi.DockerBuild;

return await Deployment.RunAsync(() =>
{
    var repository = new Aws.Ecr.Repository("app-repository");

    var authToken = Aws.Ecr.GetAuthorizationToken.Invoke(new()
    {
        RegistryId = repository.RegistryId,
    });

    var image = new DockerBuild.Image("app-image", new()
    {
        Context = new DockerBuild.Inputs.BuildContextArgs
        {
            Location = "./app",
        },
        Push = true,
        Registries = new[]
        {
            new DockerBuild.Inputs.RegistryArgs
            {
                Address = repository.RepositoryUrl,
                Username = authToken.Apply(token => token.UserName),
                Password = authToken.Apply(token => token.Password),
            },
        },
        Tags = new[]
        {
            repository.RepositoryUrl.Apply(url => $"{url}:latest"),
        },
    });

    return new Dictionary<string, object?>
    {
        ["repositoryUrl"] = repository.RepositoryUrl,
        ["digest"] = image.Digest,
    };
});
```

```csharp
// Deploy stack (acme/app-deploy/production)
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var build = new StackReference("acme/app-image/production");
    var repositoryUrl = build.RequireOutput("repositoryUrl").Apply(v => (string)v);
    var digest = build.RequireOutput("digest").Apply(v => (string)v);

    var taskDefinition = new Aws.Ecs.TaskDefinition("app-task", new()
    {
        Family = "app",
        RequiresCompatibilities = new[] { "FARGATE" },
        NetworkMode = "awsvpc",
        Cpu = "256",
        Memory = "512",
        ContainerDefinitions = Output.Tuple(repositoryUrl, digest)
            .Apply(t => JsonSerializer.Serialize(new[]
            {
                new
                {
                    name = "app",
                    image = $"{t.Item1}@{t.Item2}",
                    essential = true,
                    portMappings = new[] { new { containerPort = 8080 } },
                },
            })),
    });
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Build stack (acme/app-image/production)
package myapp;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ecr.Repository;
import com.pulumi.aws.ecr.EcrFunctions;
import com.pulumi.aws.ecr.inputs.GetAuthorizationTokenArgs;
import com.pulumi.dockerbuild.Image;
import com.pulumi.dockerbuild.ImageArgs;
import com.pulumi.dockerbuild.inputs.BuildContextArgs;
import com.pulumi.dockerbuild.inputs.RegistryArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("app-repository");

        final var authToken = EcrFunctions.getAuthorizationToken(GetAuthorizationTokenArgs.builder()
            .registryId(repository.registryId())
            .build());

        var image = new Image("app-image", ImageArgs.builder()
            .context(BuildContextArgs.builder()
                .location("./app")
                .build())
            .push(true)
            .registries(RegistryArgs.builder()
                .address(repository.repositoryUrl())
                .username(authToken.applyValue(token -> token.userName()))
                .password(authToken.applyValue(token -> token.password()))
                .build())
            .tags(repository.repositoryUrl().applyValue(url -> url + ":latest"))
            .build());

        ctx.export("repositoryUrl", repository.repositoryUrl());
        ctx.export("digest", image.digest());
    }
}
```

```java
// Deploy stack (acme/app-deploy/production)
package myapp;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.ecs.TaskDefinition;
import com.pulumi.aws.ecs.TaskDefinitionArgs;
import com.pulumi.resources.StackReference;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var build = new StackReference("acme/app-image/production");
        var repositoryUrl = build.requireOutput(Output.of("repositoryUrl")).applyValue(String::valueOf);
        var digest = build.requireOutput(Output.of("digest")).applyValue(String::valueOf);

        var taskDefinition = new TaskDefinition("app-task", TaskDefinitionArgs.builder()
            .family("app")
            .requiresCompatibilities("FARGATE")
            .networkMode("awsvpc")
            .cpu("256")
            .memory("512")
            .containerDefinitions(Output.tuple(repositoryUrl, digest)
                .applyValue(t -> String.format(
                    "[{\"name\":\"app\",\"image\":\"%s@%s\",\"essential\":true,"
                        + "\"portMappings\":[{\"containerPort\":8080}]}]",
                    t.t1, t.t2)))
            .build());
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

This split only works cleanly when both stacks can reliably read and write state and each other's outputs regardless of which machine or CI runner is doing the reading — which is exactly what the [Pulumi Cloud state backend](/docs/iac/concepts/state-and-backends/) is built for. A self-managed backend (an S3 bucket or similar) can technically serve the same `StackReference` calls, but you take on the access control, availability, and durability of that storage yourself, on top of the infrastructure you actually set out to manage. Pulumi Cloud handles state locking, versioned state history, and encrypted output storage for you, and layers Pulumi ESC and Pulumi Deployments on top for exactly this build-stack/deploy-stack promotion workflow — it's the backend to default to for anything beyond a single-developer experiment.

## Choosing between `docker-build` and `docker`

Docker's own guidance is to migrate to `docker-build.Image` for the reasons that motivate most of this guide: it delegates directly to BuildKit rather than reimplementing caching logic, so `cacheFrom`/`cacheTo` behave exactly like the equivalent `docker buildx build` flags; it supports every BuildKit cache backend (registry, `gha`, S3, Azure Blob, local); and it produces multi-platform images and precise digest outputs (`ref`, `digest`) without the workarounds v3 and v4 of the classic provider needed for the same result. For a new Pulumi program that builds container images, start with `docker-build.Image`.

That doesn't make `docker.Image` a poor choice for programs already built on it. It remains fully supported, its `repoDigest` output gives you the same digest-pinning capability described earlier in this guide, and a working build pipeline isn't worth disrupting for its own sake. Migrate when you're already touching the build definition for another reason — adding registry caching, for example, is a natural prompt to move to `docker-build.Image` at the same time, since its caching model is the one this guide recommends.

## See also

- [Docker provider](/registry/packages/docker/) and [Docker Build provider](/registry/packages/docker-build/) — full resource and input reference for both providers covered in this guide.
- [Docker images](/docs/iac/operations/docker-images/) — Pulumi's own published CLI container images, for running Pulumi itself in CI/CD or Kubernetes.
- [Continuous delivery](/docs/iac/operations/continuous-delivery/) and [GitHub Actions](/docs/iac/operations/continuous-delivery/github-actions/) — CI/CD workflow patterns this guide builds on.
- [Stacks and stack references](/docs/iac/concepts/stacks/#stackreferences) — the mechanism behind the build/deploy split above.
- [State and backends](/docs/iac/concepts/state-and-backends/) — why Pulumi Cloud is the recommended backend for multi-stack workflows like this one.
- [AWS ECS](/docs/iac/guides/clouds/aws/ecs/) — deploying containerized applications to Amazon ECS with Pulumi.
