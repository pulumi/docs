---
title: "Faster Pulumi deployments, part 3: Prepare plugins"
# TODO: Replace the series placeholder dates before publication.
date: 2099-01-03
draft: true
meta_desc: "Package matching provider plugins with a compiled Pulumi program, install them from release artifacts, and skip redundant dependency installation."
feature_image:
authors:
    - jonathan-davenport
tags:
    - pulumi-deployments
    - go
    - providers
category: tutorials
series: faster-pulumi-deployments
schema_type: auto
social:
    twitter:
    linkedin:
    bluesky:
---

A compiled Pulumi program is only part of the executable software involved in a deployment. The program declares resources through provider SDKs, while separate provider processes perform the corresponding operations. If the runner has the program but lacks those providers, it must still retrieve them before it can complete the deployment.

The next step is to make those provider executables part of the [release prepared in part 2](/blog/precompile-pulumi-go-programs/). This gives you an explicit record of the plugin versions that belong with the program, rather than relying on preparation during every deployment. Once the release supplies everything the program needs, the remaining package-manager installation can be removed.

<!--more-->

## Match plugins to the SDKs used in the build

A provider SDK gives your program Go types and resource constructors. The provider plugin implements the corresponding resource operations in a separate process. Both belong to the deployment, but compiling the SDK does not embed the plugin. Prepare them as related parts of the release.

For each provider, use the version requested by the SDK compiled into the program, accounting for any explicit provider-version override in the code. It is tempting to treat the Pulumi version as one number that applies to the entire deployment, but these components have separate release histories. The CLI version identifies the engine and tools; it does not tell you which AWS or custom provider version your program requires.

Existing stacks add a qualification to this rule. During upgrades or resource removal, resources recorded in state may require a plugin that the new program no longer uses. A release that deploys successfully to an empty stack can therefore still be incomplete for an update. If your process supports both cases, test both rather than treating a successful new-stack deployment as proof that all dependencies are present.

Create a release manifest named `plugins.txt`. Each line contains the plugin name, version, and archive path. For a custom provider named `acme`, it could contain:

```text
acme 1.2.3 plugins/pulumi-resource-acme-v1.2.3-linux-amd64.tar.gz
```

Replace this illustrative entry with your program's actual providers. Add one line per required plugin version, without a header or comments. Keep the manifest alongside the source so changes receive review.

For the Random-provider project suggested in part 1, inspect the SDK version with:

```bash
go list -m github.com/pulumi/pulumi-random/sdk/v4
```

The validation example used `v4.18.2`, so its manifest entry was:

```text
random 4.18.2 plugins/pulumi-resource-random-v4.18.2-linux-amd64.tar.gz
```

Use the version returned for your project rather than replacing it with this example's version. End the manifest with a newline so the shell loop below reads its final entry.

## Publish the program and plugins as one release

Download the provider archives from their release pipeline or your approved artifact store. Each archive must match the runner's operating system and architecture. For custom providers, follow the [executable plugin archive layout](/docs/iac/guides/building-extending/packages/executable-plugin/#binary-naming-and-archive-layout): the executable belongs at the archive root.

For the example Random provider version, the Linux archive can be retrieved with:

```bash
mkdir -p plugins
curl --fail --location \
    https://get.pulumi.com/releases/plugins/pulumi-resource-random-v4.18.2-linux-amd64.tar.gz \
    --output plugins/pulumi-resource-random-v4.18.2-linux-amd64.tar.gz
```

In the Linux build job from part 2, place the archives under `plugins/`. Replace the archive creation command with:

```bash
tar -czf infra.tar.gz bin/infra plugins.txt plugins/
sha256sum infra.tar.gz > SHA256SUMS
```

Publish both files under the new source revision using the same S3 upload commands. Preserve any runtime files your program requires when extending this archive.

S3 is a hosting choice, not a requirement of the release model. If you use Artifactory, publish the same versioned files there and replace the download client in the preparation script. Keep one authoritative plugin manifest so the storage service does not determine which versions are deployed.

## Install plugins from the downloaded release

After the extraction step in `scripts/prepare-program.sh`, add:

```bash
while read -r name version archive; do
    pulumi plugin install resource "$name" "$version" \
        --exact \
        --file "$archive"
done < plugins.txt
```

[`pulumi plugin install --file`](/docs/iac/cli/commands/pulumi_plugin_install/) installs a local archive instead of downloading it from the provider's default host. `--exact` requires that specific version for installation. Ensure the manifest agrees with the versions requested by the program; installing a plugin does not rewrite those requests.

Run preparation with the same user and `PULUMI_HOME` as the Pulumi operation. The operation will not find a plugin installed in another home directory.

Validate the release on a clean runner, where an existing plugin cache cannot compensate for an incomplete manifest. A development machine often has dependencies left over from earlier work, making it possible to test a release without noticing what it omits. Check the actual plugin versions in the logs and investigate any unexpected download before removing automatic installation from the process.

## Skip installation only after the release is complete

Once release preparation supplies every dependency, enable **Skip package manager dependency installation** in each test stack's **Settings** → **Deploy** page.

Run `bench-a` again. The runner retrieves the release, installs its plugins locally, and executes the Go binary. Downloading Go modules would prepare for a compilation that no longer happens, so that work can be removed.

Keep managed caching enabled for this first comparison. Measure its restore and save costs, then run a separate comparison with caching disabled. If the complete release makes the managed cache redundant, removing cache transfer can reduce preparation time further.

### Include dependencies of component providers

A native Go component compiles into its caller. A TypeScript component consumed through a Pulumi package runs through its component provider and can still need Node.js and npm dependencies.

This is an important exception to the idea that a Go deployment needs only its compiled program and binary providers. A Go program can call a component whose implementation still runs in TypeScript, so the top-level language does not describe every runtime involved. Include that component's dependencies in the preparation strategy before disabling installation. Otherwise, compilation has removed one build step while leaving another runtime unprepared.

For a Go-authored component package, the [Pulumi Go Provider SDK](/docs/iac/guides/building-extending/packages/pulumi-go-provider-sdk/) supports an executable provider model. Build the plugin and generate consumer SDKs during the package release. Consumers can then install published SDKs rather than generate them during deployment.

Set `pluginDownloadURL` in your package schema to its binary host. For an existing mirror, [`PULUMI_PLUGIN_DOWNLOAD_URL_OVERRIDES`](/docs/iac/cli/environment-variables/) can redirect plugin requests. Neither setting configures npm authentication.

The [private registry](/docs/idp/concepts/private-registry/) can provide discovery and documentation while your artifact store supplies the executable files. These are related responsibilities, but choosing where to list a package does not by itself determine how quickly it will execute. Usage tracking also depends on how the component is consumed, since importing local source does not create the package provider resource used for registry matching. Test the package-based consumption path you intend to deploy rather than assuming a local import exercises the same mechanism.

## Verify the release on both clean and existing stacks

Compare this run with part 2 using the same operation and test conditions. The archive is larger now, and its plugins still need local installation. Count those costs before claiming a saving from removing external downloads and package-manager work.

Deploy the same release to `bench-b` without rebuilding it. Confirm the executable checksum and provider versions match, while each stack still receives its own configuration. If you also support existing stacks, repeat the test against a representative earlier release and check that the update finds every required plugin.

Next, put the program and installed plugins in a custom executor image while keeping stack configuration outside it. Continue to [part 4: Use a prebuilt image](/blog/prebuilt-pulumi-executor-images/) to compare image pulls with artifact download and extraction.
