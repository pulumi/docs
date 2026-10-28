---
title: "Faster Pulumi deployments, part 2: Compile Go once"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-02
draft: true
meta_desc: "Build a Pulumi Go program once, retrieve it through ESC, and deploy the same executable to multiple stacks with runtime configuration."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - go
    - esc
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

Once a program revision has been built and tested, rebuilding it for each environment adds another preparation step to every deployment. Go lets you publish the executable instead, and Pulumi can run that executable while continuing to supply configuration for the selected stack. This gives the deployment process a specific artifact to promote, rather than a set of instructions for reconstructing it each time.

The [cache from part 1](/blog/speed-up-pulumi-deployments/) already reduces repeated compilation work, so a separate build pipeline needs to improve on that result. Its strongest use case is a program deployed repeatedly across many environments, where the initial build can be reused instead of repeated.

<!--more-->

## Give each executable an immutable release path

For this experiment, keep the source repository connected to Pulumi Deployments and let it supply the project files and executable-retrieval script. The executable itself will live in an existing private S3 bucket, under a path containing the source commit that produced it. Using the commit in the path establishes a relationship between the source selected for deployment and the code the runner retrieves.

You need a build environment, permission to publish to that bucket, and an executor image containing the AWS CLI. This example targets Linux on `amd64`; use the platform of your runner.

Create an [ESC environment with AWS credentials](/docs/esc/providers/login/aws-login/) for artifact retrieval. It must expose credentials through `environmentVariables` and grant access to the release objects. Give the deployment identity permission to open that environment.

Use separate permissions for publishing artifacts, retrieving artifacts, and changing infrastructure. A deployment runner needs read access to its executable release, not permission to replace it. Keep your existing infrastructure credentials unchanged during this experiment.

## Tell Pulumi to use the executable

In `Pulumi.yaml`, preserve your existing project name and other settings. Replace `runtime: go` with:

```yaml
runtime:
  name: go
  options:
    binary: ./bin/infra
```

Use the [`binary` option](/docs/iac/languages-sdks/go/#program-entrypoint) to tell Pulumi which executable to run. The Pulumi CLI still supplies the execution context and manages stack state and resource operations. Only compilation moves out of the deployment.

Add `scripts/prepare-program.sh` to the program repository with this content:

```bash
#!/usr/bin/env bash
set -euo pipefail

: "${ARTIFACT_BUCKET:?Set ARTIFACT_BUCKET in deployment settings}"
revision="$(git rev-parse HEAD)"
release="s3://${ARTIFACT_BUCKET}/releases/${revision}/linux-amd64"

aws s3 cp "${release}/infra.tar.gz" ./infra.tar.gz
aws s3 cp "${release}/SHA256SUMS" ./SHA256SUMS
sha256sum --check SHA256SUMS
tar -xzf infra.tar.gz
test -x ./bin/infra
```

This script runs in the Pulumi project directory and expects Linux tools, including `sha256sum`. The checksum detects transfer corruption; control writes to the release objects so an unauthorized publisher cannot replace both files.

Commit the runtime setting and preparation script. Add `bin/` and generated release files to your project's ignore rules.

## Publish before you deploy

In a clean Linux build environment, check out the commit you will deploy. Authenticate to the artifact bucket using your build system's credentials. Set `ARTIFACT_BUCKET` to its name, then run:

```bash
set -euo pipefail
: "${ARTIFACT_BUCKET:?Set ARTIFACT_BUCKET}"
revision="$(git rev-parse HEAD)"
release="s3://${ARTIFACT_BUCKET}/releases/${revision}/linux-amd64"

go mod download
GOOS=linux GOARCH=amd64 go build -trimpath -o bin/infra .
tar -czf infra.tar.gz bin/infra
sha256sum infra.tar.gz > SHA256SUMS
aws s3 cp infra.tar.gz "${release}/infra.tar.gz"
aws s3 cp SHA256SUMS "${release}/SHA256SUMS"
```

Use a compatible toolchain if your program uses `cgo` or native libraries. The archive above contains only the executable. Include any runtime files your program reads, such as manifests or templates, at their expected paths.

Once published, treat the revision path as immutable. If a build overwrites it, two stacks can request the same release and receive different executables, undermining the repeatability this process is intended to provide. Keep the published artifact for later stacks and record its Go toolchain and module versions. If the build inputs need to change, publish a new release rather than silently replacing the old one.

The release process must also establish an order between publication and deployment. A source commit can trigger a runner before its executable has been uploaded, even when both jobs eventually succeed. For this experiment, disable push-triggered updates on the test stacks and trigger deployments manually after publication completes. The automated pipeline should enforce the same dependency: only a successfully published release is eligible for deployment.

## Retrieve the program with an ESC pre-run command

Set `ARTIFACT_BUCKET` in each stack's deployment environment variables. Add this [pre-run command](/docs/deployments/concepts/settings/pre-run-commands/), replacing the ESC environment path:

```bash
pulumi env run <org>/build/artifact-reader -- bash scripts/prepare-program.sh
```

Credential access depends on when each step runs. An ESC environment imported by stack configuration is not automatically open when the pre-run command retrieves the executable. Opening the artifact-reader environment explicitly gives the script credentials at the point where it needs them. Since separate pre-run commands execute in separate shells, keep the related operations in that script rather than relying on an earlier `export`.

Keep dependency installation and caching unchanged from part 1. This isolates the effect of running a compiled program. Part 3 will supply plugins explicitly and remove the remaining package-manager installation step.

Deploy the built commit to `bench-a`, then `bench-b`. Confirm that each preparation step retrieves the same revision path and verifies the archive successfully.

## Keep environment-specific values in runtime configuration

A compiled program remains parameterizable because configuration lookup is part of executing the program, not compiling it. The binary contains the code that requests a value; the Pulumi CLI supplies that value for the selected stack when the program runs. Consequently, changing a region or capacity setting does not require recompiling the configuration API or the resource constructors that use it. Keep those environment differences in configuration so every environment can use the same tested executable.

For a visible check, add a configuration lookup inside your existing `pulumi.Run` callback, using the `github.com/pulumi/pulumi/sdk/v3/go/pulumi/config` package:

```go
cfg := config.New(ctx, "")
ctx.Export("environment", pulumi.String(cfg.Require("environment")))
```

Build and publish this program revision once. Set `environment` to different values in the two test stacks, using each stack's fully qualified name:

```bash
pulumi config set environment bench-a --stack <org>/<project>/bench-a
pulumi config set environment bench-b --stack <org>/<project>/bench-b
```

Commit the resulting stack configuration files if your deployment reads them from Git, then build and publish that final commit before deploying it. Both stacks must deploy that same commit and artifact.

You can also supply the values through an [ESC environment's `pulumiConfig`](/docs/esc/guides/pulumi-iac/). For a project named `fleet-infra`, the first environment would contain:

```yaml
values:
  pulumiConfig:
    fleet-infra:environment: bench-a
```

Import that environment in the corresponding stack file:

```yaml
environment:
  - fleet/bench-a
```

Create the equivalent environment for `bench-b`. If you move a value into ESC, remove the corresponding local stack value; explicit stack configuration takes precedence.

Check the stack outputs after both deployments. The `environment` output should differ even though the executable checksum is identical. This verifies the property the release process depends on: the code can remain constant while environment-specific behavior changes. Apply the same pattern to resource arguments such as capacity or region, and use secret configuration methods for sensitive values.

ESC lets you change runtime configuration without recompiling. In this example, release paths follow the Git commit, so a Git-only configuration change still needs an artifact at the selected revision path. A later pipeline can explicitly map multiple configuration revisions to one verified program artifact.

## Count the build once and retrieval for every deployment

Repeat the same operations measured in part 1. Record artifact download and extraction as preparation time. Compare them with the compilation work removed from the Pulumi operation.

Include the release build when measuring the total cost across environments. Moving a build to another job does not eliminate its cost. The saving comes from reusing its result instead of paying that cost for every stack.

For a program deployed once, publishing and retrieving a separate artifact may cost more than compiling it on the runner. With many deployments of the same revision, however, the initial build serves every stack while each deployment pays only the retrieval cost. The useful comparison is therefore the complete rollout, including its build, rather than an individual job with the build moved elsewhere.

The Go executable includes its SDK dependencies, but provider plugins remain separate. [Part 3](/blog/version-pulumi-deployment-artifacts/) makes those plugins part of the same versioned release.
