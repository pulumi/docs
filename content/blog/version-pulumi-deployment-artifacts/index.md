---
title: "Faster Pulumi deployments, part 3: Prepare plugins"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-03
draft: true
meta_desc: "Package matching provider plugins with a prepared Pulumi program, publish a versioned release, and remove repeated dependency retrieval."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - platform-engineering
    - providers
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

A prepared Pulumi program is only part of the executable software involved in a deployment. The program declares resources through provider SDKs, while separate provider processes perform the corresponding operations. If the runner has the program but lacks those providers, it must still retrieve them before completing the deployment.

For a platform team distributing one program across many accounts, those provider executables belong in the same controlled release process as the program. Extend the [artifact from part 2](/blog/precompile-pulumi-go-programs/) with the matching plugins so the release describes what will execute, regardless of the language used to write the program.

<!--more-->

## Match plugins to the SDKs used in the build

The Pulumi CLI, core SDK, and resource providers have separate version histories. The CLI version does not tell you which AWS or custom provider version your program requires. Record each provider version requested by the SDK, including any explicit override in the program.

The companion uses a shared [provider manifest](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/provider-plugins.txt). Its [version check](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/scripts/check-versions.py) compares that manifest with the SDK dependency declared in each of the five example programs:

```bash
make check
```

That check is specific to the sample's Random provider. Apply the same principle to your actual provider set rather than assuming that one manually selected plugin version covers every program.

Existing stacks require an additional check. During upgrades or resource removal, resources already in state may need a plugin that the new program no longer uses. A release that works against an empty stack may therefore still be incomplete for an update. Test both when your process supports both.

## Publish a complete release

The [release lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/03-release-artifacts) contains the complete packaging, publication, and retrieval steps. From the companion root:

```bash
make package LANGUAGE=typescript
```

The builder prepares the selected program, downloads matching provider archives, and creates a release archive with a SHA-256 checksum. The archive includes the prebuilt project definition and dependencies, but excludes stack configuration. Python environments are installed at the destination rather than copied from the build machine.

Use the same operating system and architecture for the program and plugins. The companion's local packaging path targets the build machine, while its image path builds inside the selected Linux environment. Mixing a macOS executable with Linux provider archives does not produce a usable Linux release.

Publish under a new immutable path that identifies the source revision, language, and platform. The companion demonstrates S3, but Artifactory or another controlled artifact store can serve the same role. Keep one authoritative manifest and promote the same artifact instead of overwriting a release after some environments have already consumed it.

## Retrieve the release with ESC credentials

The runner needs artifact credentials before the Pulumi operation starts. Stack-imported ESC environments are not automatically open at this point, so explicitly open the reader environment around the preparation script:

```bash
pulumi env run <org>/build/artifact-reader -- bash ../../scripts/prepare-release.sh
```

This command assumes the deployment's project directory is the selected program directory in the companion. The lab specifies the exact source path, required runtime tools, and `RELEASE_URI` setting. The [preparation script](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/scripts/prepare-release.sh) verifies and extracts the artifact, then installs its plugins from local archives.

Keep publication credentials separate from retrieval credentials. The runner needs access to the selected release, not permission to replace it. A checksum detects changed content in transit; it does not establish publisher identity when an attacker can replace both the artifact and checksum.

For Artifactory, replace the storage client and test its authentication independently. An npm registry token does not automatically authenticate separate provider-plugin downloads.

## Skip preparation only after its replacement is complete

Once the release supplies everything required at execution, enable **Skip package manager dependency installation** in deployment settings. Test with a fresh runner so an existing cache cannot hide an omitted dependency. Check the logs for unexpected downloads and verify the provider versions used by the operation.

A language SDK and a component implementation may have different runtime requirements. A Go program can consume a component whose implementation runs in TypeScript; compiling the caller does not package that implementation into Go. Include remote component providers and their dependencies in the release design.

If you maintain your own Pulumi packages, generate and publish consumer SDKs as part of their release process. Component discovery and documentation in the private registry are separate from the storage and preparation of executable artifacts. Test the consumption path you intend to use, including usage tracking, rather than relying on local source imports as an equivalent test.

## Compare transfer costs with preparation saved

The complete archive is larger than the program alone, and installing plugins from it still takes time. Measure those costs alongside the downloads and package-manager work removed from each deployment. Also test an existing stack update before promoting the release across environments.

The next option is to install the program and plugins during an image build, letting the container runtime distribute the prepared filesystem. [Part 4](/blog/prebuilt-pulumi-executor-images/) compares that approach while keeping stack configuration external.
