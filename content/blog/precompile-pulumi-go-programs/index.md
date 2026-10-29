---
title: "Faster Pulumi deployments, part 2: Build once"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-02
draft: true
meta_desc: "Prepare Pulumi programs once in TypeScript, Python, Go, C#, or Java, then reuse the output across stacks with runtime configuration."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - platform-engineering
    - esc
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

Once a program revision has been built and tested, preparing it again for every environment adds another step to each deployment. The form of that preparation depends on the language: compilation for some programs, dependency installation for others. The platform-engineering opportunity is the same in each case. Prepare what can be shared, then supply the selected stack's configuration when the program executes.

The [cache from part 1](/blog/speed-up-pulumi-deployments/) reduces repeated work within a stack. A release artifact goes further by giving other stacks something explicit to reuse. Your team can keep its existing language while changing where compilation or dependency preparation happens.

<!--more-->

## Prepare an artifact that fits your language

The [companion's build lab](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/labs/02-build-once) contains complete programs in TypeScript, Python, Go, C#, and Java. Each implements the same small provider-backed workload and reads the same configuration key. This lets you test the release mechanics before applying them to a larger infrastructure program.

| Language | Prepared output | What remains at execution time |
| --- | --- | --- |
| TypeScript | JavaScript and installed runtime packages | Node.js and the prepared packages |
| Python | Locked requirements and compatible wheels | Python and an environment installed at its destination |
| Go | Native executable containing imported Go packages | A compatible operating system and architecture |
| C#/.NET | Published assembly and dependency files | A compatible .NET runtime |
| Java | Runnable JAR containing its dependencies | A compatible JVM |

Every row also needs the Pulumi CLI, provider plugins, and configuration. A prebuilt program does not contain the entire deployment system.

TypeScript compilation removes runtime transpilation, but the emitted JavaScript still loads packages and runs under Node.js. The companion sets `typescript: false` and points Pulumi at the JavaScript entry point. It preserves the package metadata and runtime dependencies instead of assuming that an arbitrary single-file bundle will work.

For .NET and Java, Pulumi's `binary` option selects the published DLL or runnable JAR. The companion preserves the .NET publish directory and packages Java dependencies with the JAR. These are managed-runtime artifacts; neither example depends on Native AOT or a Java native-image toolchain.

Go provides a convenient native executable model, particularly when designing a new shared program. It is an optional choice, not a reason to rewrite a working program before optimizing its deployment. Python takes a different approach: prepare the wheels, then install them at the destination without downloading them again. Copying an existing virtual environment between machines would introduce path and platform assumptions that this workflow avoids.

## Build the selected track

From the companion directory, choose your language:

```bash
make build LANGUAGE=typescript
make config LANGUAGE=typescript
```

The [build script](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/scripts/build.sh) contains the complete commands for each track. It writes prepared files under `dist/<language>` and creates a separate workspace for stack configuration. Rebuilding the artifact does not remove that configuration or include it in a release.

Use the toolchain and dependency resolution files committed with your program. For Go executables and Python wheels, the output must match the deployment platform. Native dependencies can impose the same requirement on Node.js programs. A successful build on a Mac does not establish that its output will run in a Linux container; the image lab builds within the target Linux environment.

The Python track includes an additional destination-installation command in its lab instructions. That step creates the virtual environment where it will actually run and installs from the prepared wheel directory. It removes package retrieval from execution, while preserving the interpreter and installation work the program still requires.

## Keep environment differences outside the artifact

All five programs use their language's Pulumi configuration API to read `environment`. Create two disposable stacks in the external configuration workspace and set different values:

```bash
pulumi config set environment development --stack <org>/faster-pulumi-deployments/bench-a
pulumi config set environment production --stack <org>/faster-pulumi-deployments/bench-b
```

Deploy both stacks using the same prepared output. Their exported environment values should differ even though you did not rebuild between deployments. Apply the same separation to resource inputs such as region or capacity, and use the appropriate secret configuration methods for sensitive values.

The [ESC examples](https://github.com/pulumi/workshops/tree/workshop/faster-pulumi-deployments/faster-pulumi-deployments/esc) supply those values through `pulumiConfig`. Each stack can import a different environment while continuing to run the same program. Remove conflicting explicit stack values when moving configuration into ESC, since local stack configuration takes precedence.

The companion records which build and execution paths have been tested in its [validation notes](https://github.com/pulumi/workshops/blob/workshop/faster-pulumi-deployments/faster-pulumi-deployments/VALIDATION.md). The examples establish that these artifacts can execute with different configuration; their small workload does not establish comparative performance between languages.

## Count preparation once and retrieval for every deployment

Include the initial build when comparing the complete rollout. Moving a build into another job does not remove its cost. The saving comes from reusing its output across enough stacks to justify the build, publication, and retrieval process.

A warm dependency cache may already make preparation inexpensive for a frequently updated stack. An artifact can be more useful when the same revision is deployed to many new stacks, each of which would otherwise start cold. Measure both cases before deciding how much of the release process to centralize.

Once the prepared program works, make its required provider plugins part of the same release. [Part 3](/blog/version-pulumi-deployment-artifacts/) addresses that separate dependency boundary.
