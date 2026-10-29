---
title: "Faster Pulumi deployments, part 4: Use a prebuilt image"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-04
draft: true
meta_desc: "Package a prepared Pulumi program and matching plugins in an executor image while keeping stack configuration and credentials outside it."
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

A container image provides another way to distribute the executable environment that a deployment needs. Instead of downloading an archive and installing its plugins in every job, prepare those files while building the image. The resulting image contains the Pulumi CLI, the program's runtime dependencies, and the matching provider plugins.

For a platform engineer managing deployments across hundreds of accounts, the image can become one reusable release of the execution environment. Keep account-specific configuration outside that release so changes to an environment do not require rebuilding the code it runs.

<!--more-->

## Build the image for the selected language

The [companion image lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/04-executor-images) provides a shared Dockerfile and a builder that selects the appropriate runtime base. From the workshop directory:

```bash
PLATFORM=linux/amd64 make image LANGUAGE=typescript
```

Select `typescript`, `python`, `go`, `dotnet`, or `java`, and match the platform to your runner. The build happens inside Linux, avoiding accidental inclusion of a host-platform Go executable or Python wheel set.

The [Dockerfile](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/images/Dockerfile) prepares the language-specific artifact in a build stage and installs the matching plugins. Its final stage contains the runtime files and CLI, but excludes the project file and stack configuration. Python's virtual environment is created at its final path inside the image instead of being relocated from another machine.

These examples retain SDK and build tools in the base image. That gives you a working comparison before trying to minimize the runtime image. Removing tools can reduce transfer size, but it is a separate change that needs testing; it should not obscure whether prebuilding the program helped.

## Keep the executable release separate from configuration

The image builder creates an external project configuration workspace under `workspaces/image/<language>`. Its `Pulumi.yaml` selects the program inside the image: the Go executable, .NET DLL, Java JAR, JavaScript entry point, or Python program directory.

Keep that project definition and the stack files in Git. Use stack configuration or ESC to supply the environment-specific values. The example programs all use the standard configuration API, so the selected account or environment does not have to be compiled into the program.

This arrangement gives the deployment two independently versioned inputs. The image digest identifies the executable release, and the Git revision identifies the project and stack files. If those files import ESC environments that can change independently, record or pin the environment revisions when exact configuration replay matters.

A fixed image digest does not freeze values fetched from an unversioned environment. That flexibility can be useful, but it should be deliberate rather than an assumption that the image or Git commit captured every deployment input.

## Configure Pulumi Deployments

Publish the image to a registry your runner can access and record its digest. In **Settings** → **Deploy**, select **Use a custom executor image** and use the digest-qualified reference. A mutable tag can move to a different image; a digest identifies the release you tested.

Keep Git configured as the source of the project and stack files. The companion includes a `Pulumi.image.yaml` for each program directory. Its lab shows how to select that definition while preserving the external stack configuration.

Skip automatic package-manager dependency installation once the image contains everything the selected program requires. Remove the artifact-download command from part 3, since retrieving another copy would repeat preparation the image already provides. Keep the image's plugin location consistent with the `PULUMI_HOME` used by the operation.

Private registry authentication must work before the container starts. A pre-run command inside the container cannot authenticate the earlier image pull. Use [registry credentials supported by Pulumi-managed runners](/docs/deployments/concepts/settings/custom-executor-images/) or the authentication mechanism configured for customer-managed runners.

## Test configuration changes without rebuilding

Deploy the same image digest to two disposable stacks with different `environment` values. Both should execute the prepared program and report their own configuration. Check the logs for unexpected compilation, dependency installation, or provider downloads.

Next, change only one stack's ESC value and redeploy with the existing image reference. Confirm that the selected stack changes while the other retains its value. If the stack pins an ESC revision, select the new revision before deploying.

Repeat the exercise with a Git stack-file change and the same image digest. These tests establish the property the multi-account release process depends on: the executable can remain constant while the selected environment's inputs change.

Rebuild when the program, plugins, CLI, or included runtime tools change. Ordinary configuration changes should remain in Git or ESC so that adding another environment does not also require another image build.

## Include cold image pulls in the comparison

Measure image preparation and the complete operation, not only the time after the container starts. Pulumi-managed runners already cache the default executor image; a fresh runner must pull your custom image. A large image can therefore cost more to transfer than the smaller artifact from part 3.

Include the initial image build and publication when comparing a rollout across many stacks. Layer reuse can reduce repeated transfer, but its benefit depends on runner placement and cache lifetime. A second deployment is not proof that it reached a runner with the image cached.

Keep the image approach when it improves the measured workload or provides useful release consistency, and distinguish those two outcomes. Continue to [part 5](/blog/cache-pulumi-kubernetes-runners/) for persistent customer-managed runner caches, or [part 6](/blog/reduce-pulumi-rollout-time/) for scheduling improvements.
