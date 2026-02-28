---
title_tag: "Resolving macOS Architecture Mismatch Issues"
meta_desc: "Learn how to diagnose and fix Pulumi crashes or hangs on Apple Silicon Macs caused by x86_64 binaries running under Rosetta 2."
title: macOS architecture mismatch
h1: macOS architecture mismatch
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: macOS Architecture Mismatch
        parent: support-troubleshooting-common-issues
        weight: 60
aliases:
    - /docs/iac/troubleshooting/common-issues/architecture-mismatch/
---

On Apple Silicon Macs (M1, M2, M3, and later), Pulumi crashes or hangs when x86_64-compiled binaries are present and are being run under Rosetta 2. Pulumi ships native arm64 binaries for Apple Silicon and does not require or support Rosetta 2. The most common cause is a Homebrew installation that was set up to run in x86_64 emulation mode, which silently installs x86_64 builds of both the Pulumi CLI and its provider plugins.

## Symptoms

The most recognizable symptom is a crash during `pulumi up`, `pulumi preview`, or `pulumi destroy` with an error resembling the following:

```
Diagnostics:
  pulumi:pulumi:Stack (my-stack):
    assertion failed [arm_interval().contains(address)]: code fragment does not contain the given arm address
    (CodeFragmentMetadata.cpp:48 instruction_extents_for_arm_address)
```

You may also encounter the CLI appearing to hang indefinitely with output like this:

```
     Type                 Name        Status      Info
     pulumi:pulumi:Stack  my-stack    running     (CodeFragmentMetadata.cpp:48 instruction_extents_for_arm_address)
```

`CodeFragmentMetadata.cpp` is an internal component of Rosetta 2, Apple's x86-to-arm64 binary translator. Seeing it in Pulumi output means the process is running under Rosetta 2 rather than natively. This is triggered by a known incompatibility between Go binaries compiled for x86_64 and Rosetta 2 on macOS 14.5 and later.

{{% notes type="info" %}}
The output of `pulumi about` reports the architecture of the host operating system, not the Pulumi binary itself. Even on an Apple Silicon Mac, `pulumi about` will show `Arch: arm64`, which can mislead you into thinking the binaries are correct. You need to inspect the binaries directly as shown below.
{{% /notes %}}

## Diagnosing the problem

### Check the Pulumi CLI binary

Run `file` against the Pulumi CLI binary to determine its architecture:

```bash
file "$(which pulumi)"
```

A native arm64 build produces output like:

```
/opt/homebrew/bin/pulumi: Mach-O 64-bit executable arm64
```

If you instead see `x86_64`, the CLI is being run under Rosetta 2 and must be replaced.

### Check your Homebrew installation

If you installed Pulumi via Homebrew, check whether Homebrew itself is running in x86_64 emulation mode:

```bash
brew config
```

In the output, look for the `Rosetta 2` field. A value of `true` means Homebrew is running under emulation and will install x86_64 binaries by default:

```
CPU: arm64_apple_m1
Rosetta 2: true
```

### Check provider plugins

Even if the CLI binary is correct, provider plugins installed previously may still be x86_64. Run the following command to list any plugins in your Pulumi home directory that are not arm64:

```bash
find "${PULUMI_HOME:-$HOME/.pulumi}" -type f -name 'pulumi-resource-*' \
  -exec file {} \; | grep --invert-match arm64
```

Any files listed in the output are x86_64 plugins that need to be replaced.

## Resolving the problem

### 1. Reinstall Homebrew in native arm64 mode

If `brew config` showed `Rosetta 2: true`, your Homebrew installation is running in x86_64 emulation mode. You will need to install a native arm64 instance of Homebrew. Refer to the [Homebrew discussion on running natively on Apple Silicon](https://github.com/orgs/Homebrew/discussions/545) for step-by-step guidance on migrating your Homebrew installation.

Native arm64 Homebrew installs to `/opt/homebrew`. If your `which brew` output points elsewhere (for example, `/usr/local/bin/brew`), you are likely using the x86_64 installation.

### 2. Reinstall the Pulumi CLI

Once Homebrew is running natively, reinstall Pulumi:

```bash
brew reinstall pulumi
```

Verify the binary is now arm64:

```bash
file "$(which pulumi)"
# Expected: /opt/homebrew/bin/pulumi: Mach-O 64-bit executable arm64
```

Alternatively, you can install Pulumi directly [from the official install script](/docs/install/) or download an arm64 binary directly from the [GitHub releases page](https://github.com/pulumi/pulumi/releases).

### 3. Clear the plugin cache and reinstall plugins

Replacing the CLI binary is not sufficient on its own. Any provider plugins that were previously installed as x86_64 binaries remain cached and will continue to cause the problem. Remove the plugin cache entirely:

```bash
rm -rf "${PULUMI_HOME:-$HOME/.pulumi}/plugins"
```

Then reinstall the plugins your project needs. If your project uses a `package.json`, `requirements.txt`, or similar dependency manifest, run:

```bash
pulumi install
```

Otherwise, plugins are downloaded automatically the next time you run `pulumi preview` or `pulumi up`.

## Temporary workaround

If you cannot immediately switch to native arm64 binaries, you can work around the Rosetta 2 incompatibility by disabling asynchronous preemption in the Go runtime:

```bash
GODEBUG=asyncpreemptoff=1 pulumi up
```

This is not a permanent fix. The underlying issue is that x86_64 binaries are running under an unsupported configuration, and the workaround may not be reliable across all scenarios. Migrating to native arm64 binaries is the correct resolution.

