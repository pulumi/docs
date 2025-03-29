---
title: "Improving Pulumi’s Docker Images"
date: 2024-09-27
draft: false
meta_desc: New versioned images for Pulumi Docker Containers and support for setting
  Node.js and Python versions in Pulumi Deployments.
meta_image: meta.png
authors:
  - julien-poissonnier
tags:
  - docker
search:
  keywords:
    - Docker
    - Images
    - versioned images
    - language runtimes
---

The [Pulumi Docker Containers](https://github.com/pulumi/pulumi-docker-containers) provide a convenient way for running Pulumi in CI/CD pipelines, or for running Pulumi in environments where you don't want to install the Pulumi CLI directly. These images also power [Pulumi Deployments](/product/pulumi-deployments/). We provide several flavors of images, including the [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi/tags) image that includes all supported language runtimes in a single image, as well as slim images for each language runtime, for example [pulumi/pulumi-python](https://hub.docker.com/r/pulumi/pulumi-python/tags) or [pulumi/pulumi-nodejs](https://hub.docker.com/r/pulumi/pulumi-nodejs/tags).

To provide more flexibility for choosing the version of the programming language to use, we have added versioned images for the language specific images covering [all of our supported languages](https://github.com/pulumi/pulumi?tab=readme-ov-file#languages). We now also support setting the version of the Node.js and Python runtimes used in Pulumi Deployments by using `.node-version` and `.python-version` files.

<!--more-->

For Python we provide images for [Python 3.9 to 3.12](https://hub.docker.com/u/pulumi?page=1&search=pulumi-python), for Node.js we have images for [Node.js 18, 20 and 22](https://hub.docker.com/u/pulumi?page=1&search=pulumi-nodejs), and for .NET we have images for [.NET 6.0 and 8.0](https://hub.docker.com/u/pulumi?page=1&search=pulumi-dotnet). These versioned images include the language version in the image name, for example [pulumi/pulumi-python-3.12](https://hub.docker.com/r/pulumi/pulumi-python-3.12/tags) or [pulumi/pulumi-nodejs-22](https://hub.docker.com/r/pulumi/pulumi-nodejs-22/tags).

{{% notes type="info" %}}
The Go image is not versioned, as the Go runtime natively supports multiple versions via its [Go Toolchains](https://go.dev/doc/toolchain) feature. The `go` statement in your Pulumi project's `go.mod` file determines the Go version used to compile your program.
{{% /notes %}}

### Updating the Default Language Versions

In **November 2024** the images without a version suffix, like [pulumi/pulumi-python](https://hub.docker.com/r/pulumi/pulumi-python/tags), and the [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi) image, will be updated to use the latest versions for each of the language runtimes by default:

| Language Runtime | Current Version | New Version |
| ---------------- | --------------- | ----------- |
| .NET             | 6.0             | 8.0         |
| Go               | 1.21            | 1.23        |
| Node.js          | 18              | 22          |
| Python           | 3.9             | 3.13        |
| Java             | 17              | 21          |

The default versions will be updated as new versions of the language runtimes are released, matching the [versions supported by the Pulumi CLI](https://github.com/pulumi/pulumi?tab=readme-ov-file#languages).  This will enable the unversioned [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi/tags) image to stay evergreen as new runtimes come into and out of support.

{{% notes type="info" %}}
The [pulumi-provider-build-environment](https://hub.docker.com/r/pulumi/pulumi-provider-build-environment/tags) image, which is useful for building Pulumi providers, will also be updated with the latest language runtimes, as well as upgrading [GoReleaser](https://github.com/goreleaser/goreleaser) from v1 to v2. See the [upgrade instructions](https://goreleaser.com/blog/goreleaser-v2/#upgrading) on how to migrate your configuration to v2.
{{% /notes %}}

If you require a specific version of a language runtime, you can use the versioned images. If you want to use the latest versions of the language runtimes, you can use the images without a version suffix.

### Setting the Language Version in Pulumi Deployments

When developing Node.js and Python programs, it is common to use a tool like [nvm](https://github.com/nvm-sh/nvm) or [pyenv](https://github.com/pyenv/pyenv) to manage the version of the runtime used in your development environment. These tools use a `.node-version` or `.python-version` file to specify the version of the runtime to use in the current directory.

Using the latest version of the [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi/tags) image, Pulumi Deployments now supports these files to set the version of the Node.js and Python runtimes used in the Deployment environment. For example, to use Node.js 22 in a Deployment, you can add a `.node-version` file to your project with the content `22`. The Deployment will then use Node.js 22 to run your Pulumi program.

{{% notes type="info" %}}
The [pulumi/pulumi](https://hub.docker.com/r/pulumi/pulumi/tags) image ships with Node.js 18, 20 and 22 pre-installed, as well as Python 3.9, 3.10, 3.11 and 3.12. Only the latest patch release of these versions is pre-installed, and it is therefore recommended you only specify the major version in the `.node-version` and `.python-version` files. If you provide a more specific version that does not match any of the pre-installed versions, it will be downloaded and installed on demand for each Deployment run.
{{% /notes %}}

To support more flexibility for .NET versions, the default image now also ships both .NET 6.0 and 8.0, allowing you to specify the version of .NET used in a deployment in the `TargetFramework` property in your project's `.csproj` or `.fsproj` file.

```xml
﻿<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    ...
```

If you want to use one of the language specific images, or your own custom built image, you can [set a custom executor image](https://www.pulumi.com/docs/pulumi-cloud/deployments/reference/#customizing-the-deployment-environment) in the Deployment settings.

### Additional Tools

We recently added [native Poetry support](/blog/pulumi-loves-python/#native-support-for-poetry) to Pulumi, and all of our images that include Python now ship with Poetry pre-installed. Images that include Node.js now ship with pnpm pre-installed.

To use Poetry set the [`toolchain` runtime option](/docs/iac/concepts/projects/project-file/#runtime-options) to `poetry`:

```yaml
name: pulumi-and-poetry-are-best-friends
runtime:
  name: python
  options:
    toolchain: poetry
```

To use pnpm set the [`packagemanager` runtime option](/docs/iac/concepts/projects/project-file/#runtime-options) to `pnpm`:

```yaml
name: pulumi-and-pnpm-sitting-in-a-tree
runtime:
  name: nodejs
  options:
    packagemanager: pnpm
```

These options work everywhere you run Pulumi, be it by directly running the Pulumi CLI locally, in CI/CD pipelines using our docker images, in GitHub Actions using the [Pulumi Action](https://github.com/pulumi/actions), or in Pulumi Deployments.

### Conclusion

These updates ensure that you get the latest version of the language runtimes by default, and provide more flexibility for choosing a specific version of the language runtime in your Pulumi projects and Deployments when required. Pulumi Deployments now also ship with Poetry and pnpm pre-installed, making it easier to use these tools in your Pulumi projects.
