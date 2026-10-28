---
title: "Faster Pulumi deployments, part 4: Use a prebuilt image"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-04
draft: true
meta_desc: "Build a custom Pulumi executor image with the program and provider plugins, while keeping stack configuration and ESC credentials outside the image."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - containers
    - esc
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

A container image provides another way to distribute the executable environment that a deployment needs. Instead of downloading an archive and installing its plugins in every job, prepare those files while building the image. The resulting image can contain the Pulumi CLI, the program, and the matching provider plugins, with the container runtime handling their distribution and layer reuse.

This approach works particularly well as a release model when many stacks use the same program, but only if their differences remain outside the image. Baking each environment's configuration into a separate image would require another build whenever those values changed. Keeping configuration in Git and ESC lets you reuse one executable release while each stack retains its own inputs.

<!--more-->

## Separate the executable release from configuration

Use the [verified release from part 3](/blog/version-pulumi-deployment-artifacts/) as the image's build input. Keep `Pulumi.yaml` and the stack configuration files in a Git repository connected to Pulumi Deployments. Use ESC for environment-specific values and credentials. The image supplies what executes; Git and ESC supply the inputs for the selected stack.

The repository can remain the existing program repository for this experiment. A separate, smaller configuration repository is an option later; changing repositories now would also change source-fetch time.

With this arrangement, the image digest and configuration revision identify different parts of the deployment. The digest specifies the executable release, while Git identifies the project and stack files that select its inputs. ESC supplies the values from the environments those files import. Record these relationships together so an operator can determine what ran without assuming that the configuration commit also identifies the program's source.

External configuration brings its own versioning decision. An ESC environment can change independently of Git, so recording the Git commit alone may not be enough to reproduce the inputs later. If your process requires that level of repeatability, record or pin the [ESC environment version](/docs/esc/concepts/versioning/) as well. Using current environment values may be appropriate, but it should be a deliberate choice rather than an assumption that Git has captured everything.

## Build an image from the verified release

Use the verified `bin/infra`, `plugins.txt`, and `plugins/` from part 3 as the build inputs. Keep the Pulumi CLI version unchanged from your previous experiment.

Create this Dockerfile in the build directory:

```dockerfile
ARG PULUMI_VERSION
FROM pulumi/pulumi-go:${PULUMI_VERSION} AS plugin-installer

ENV PULUMI_HOME=/opt/pulumi-home
WORKDIR /tmp/release
COPY plugins.txt ./plugins.txt
COPY plugins/ ./plugins/
RUN set -eu; \
    while read -r name version archive; do \
        pulumi plugin install resource "$name" "$version" \
            --exact --file "$archive"; \
    done < plugins.txt

FROM pulumi/pulumi-go:${PULUMI_VERSION}
ARG PROGRAM_REVISION
LABEL org.opencontainers.image.revision=${PROGRAM_REVISION}

ENV PULUMI_HOME=/opt/pulumi-home
COPY --from=plugin-installer /opt/pulumi-home/plugins/ /opt/pulumi-home/plugins/
COPY bin/infra /opt/pulumi-program/infra
RUN test -x /opt/pulumi-program/infra
```

Install plugins during the image build, then copy their installed files into the final image. This avoids repeating installation on every deployment and leaves the original archives out of the runtime image. The explicit `COPY` instructions also keep stack files and credentials out of the image.

Start with the language-specific Pulumi base image so you have a known execution environment, including the CLI and its runtime tools. Although removing unused build tools may eventually produce a smaller image, changing the base at this point introduces another variable into the comparison. First establish whether distributing the prepared release as an image helps; then investigate whether reducing that image's size improves the result further.

If the program reads runtime assets, add explicit `COPY` instructions for them. Resolve their paths from the image location or through configuration. The deployment's working directory will contain the checked-out configuration, not necessarily the directory containing the executable.

Build for the same platform used in part 3. Replace the CLI version, registry path, and release tag:

```bash
docker build --platform linux/amd64 \
    --build-arg PULUMI_VERSION="<tested-cli-version>" \
    --build-arg PROGRAM_REVISION="<program-source-commit>" \
    --tag "<registry>/<repository>:<release>" .
```

The program revision must identify the source used to build `bin/infra`. A separate image or configuration repository can have a different commit.

Inspect the installed plugins before publishing:

```bash
docker run --rm --platform linux/amd64 \
    --entrypoint pulumi \
    "<registry>/<repository>:<release>" plugin ls
```

Compare the output with `plugins.txt`, then push the image:

```bash
docker push "<registry>/<repository>:<release>"
```

Use the registry's digest in deployment settings: `<registry>/<repository>@sha256:<digest>`. Tags are useful for naming releases, but a tag can be moved to another image without changing the reference stored in a stack's settings. The digest gives the deployment a fixed executable input, which is the same property the immutable artifact path provided in the earlier approach.

## Point the project at the image's program

In the Git-backed `Pulumi.yaml`, preserve the existing project name and other settings. Change the binary path from the downloaded file to the image's absolute path:

```yaml
runtime:
  name: go
  options:
    binary: /opt/pulumi-program/infra
```

Keep the existing stack files in this repository. If you use ESC, a stack file can contain its environment import:

```yaml
environment:
  - fleet/bench-a
```

The other test stack imports `fleet/bench-b`. For a project named `fleet-infra`, the first ESC environment could supply:

```yaml
values:
  pulumiConfig:
    fleet-infra:environment: bench-a
```

Use your actual project name in the configuration key. Keep the configuration lookup and exported `environment` value from part 2. Remove any explicit stack value that would override the ESC value.

Let the compiled program read these values through the configuration API when Pulumi executes it. Avoid generating environment-specific binaries or images for values that can be supplied at runtime. Doing so would replace one reusable release with a collection of builds that must be maintained separately.

## Configure Pulumi Deployments to use the image

For each test stack, open **Settings** → **Deploy** and enable **Use a custom executor image**. Set **Image reference** to the digest you recorded.

Keep the Git source configured. The image contains executable code, but the runner still needs the project and stack files from Git. Selecting **None** would remove the source of those files rather than remove redundant work.

Keep **Skip package manager dependency installation** enabled, since the image supplies the compiled program and plugins. Remove the artifact-download pre-run command from part 3. Keep any other pre-run commands that your program requires.

Use the image's `PULUMI_HOME` consistently. Remove conflicting deployment settings that would point the Pulumi operation at another plugin directory. The execution user must be able to read the plugins and write to its Pulumi home.

Disable managed dependency caching for this experiment because the image supplies these dependencies. If caching remained enabled at the end of part 3, measure that change separately before comparing delivery methods.

Private image authentication happens earlier than the artifact authentication used in part 3. The runner must retrieve the image before it can execute a pre-run command inside that image, so an ESC-wrapped command cannot solve this earlier requirement. Configure [custom image registry credentials](/docs/deployments/concepts/settings/custom-executor-images/) for Pulumi-managed runners, or use the registry authentication configured for your customer-managed infrastructure.

## Prove that configuration can change independently

Deploy the same digest to `bench-a` and `bench-b`. Confirm that the logs show no release download or per-job plugin installation. Check that the two stacks export their own `environment` values.

Next, change only `fleet-infra:environment` in the ESC environment for `bench-a`. Trigger another deployment without changing the image reference or building a new image.

Confirm that `bench-a` reports the new value and `bench-b` retains its existing value. If you pinned an ESC revision, update that reference to select the new revision before deploying.

For Git-backed values, change the stack configuration file and deploy its new commit with the existing image digest. This tests the same property through a different configuration source: environment-specific behavior changes while the executable release stays constant.

Rebuild when the program, plugins, CLI, or included runtime tools change. Keep ordinary configuration changes in Git or ESC so they do not require image publication. This distinction becomes more useful as the same program serves more environments.

## Include cold image pulls in the comparison

Repeat the operations measured in part 3. Record image preparation time and total elapsed time. Check results on a fresh runner as well as a runner with cached layers; a repeated deployment is not proof of layer reuse.

The default executor image has an advantage worth accounting for: Pulumi-managed runners already cache it. Your custom image introduces a pull on a fresh runner, potentially transferring much more data than the program archive alone. Preinstalled plugins remove work inside the job, but that does not establish that the complete deployment is faster. Include image preparation in the comparison rather than measuring only what happens after the container starts.

Compare equivalent versions and include the one-time image build and push when measuring the full rollout. Across many stacks, reuse of the same image layers can reduce repeated preparation. The benefit depends on runner placement and cache lifetime.

Keep the image approach when its measured behavior fits your workload. Release consistency may also be useful, but report that separately from a speed improvement. Continue to [part 5](/blog/cache-pulumi-kubernetes-runners/) for customer-managed Kubernetes caches, or [part 6](/blog/reduce-pulumi-rollout-time/) to reduce queue time.
