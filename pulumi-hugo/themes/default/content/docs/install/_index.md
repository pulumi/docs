---
title_tag: "Download & Install Pulumi"
meta_desc: This page contains detailed instructions for downloading and installing Pulumi.
title: "Download & install"
h1: Download & install Pulumi
menu:
  install:
    name: Overview
    weight: 1

aliases:
- /docs/reference/install/
- /docs/get-started/install/
---

<!--
NOTE: To update this page with a new binary release, do the following:
- Update `static/latest-version`
- Update `content/docs/install/versions.md`
-->

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

## Package manager

```bash
$ brew install pulumi/tap/pulumi
```

### MacOS binary download

<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz">amd64</a>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-arm64.tar.gz">arm64</a></p>

macOS Sierra (10.12) or later is required.

The latest version of Pulumi is {{< latest-version >}}. For older versions, see [Available Versions](/docs/install/versions/).

{{< get-started-note >}}

## Other installation methods

In addition, there are many ways to install Pulumi:

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-official-homebrew-tap" />
<label for="macos-official-homebrew-tap" class="accordion-label">
<h5 class="mt-2 w-2/3">Official Pulumi Homebrew Tap</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

You can install Pulumi through the [Homebrew package manager](https://brew.sh/) and using our official
[Pulumi Homebrew Tap](https://github.com/pulumi/homebrew-tap/)

```bash
$ brew install pulumi/tap/pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
```

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-community-homebrew-tap" />
<label for="macos-community-homebrew-tap" class="accordion-label">
<h5 class="mt-2 w-2/3">Community Homebrew</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

A Pulumi formula is available on the Community Homebrew. If you do not have the Pulumi tap installed, then you can
still install Pulumi from homebrew using the command:

```bash
$ brew install pulumi
```

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-macports" />
<label for="macos-macports" class="accordion-label">
<h5 class="mt-2 w-2/3">MacPorts</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

You can install Pulumi through the [MacPorts package manager](https://www.macports.org/):

```bash
$ sudo port install pulumi
```

This will install the `pulumi` CLI to `/opt/local/bin/pulumi` and add it to your path.

Subsequent updates can be installed through the `upgrade outdated` command:

```bash
$ sudo port upgrade outdated
```

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-installation-script" />
<label for="macos-installation-script" class="accordion-label">
<h5 class="mt-2 w-2/3">Installation Script</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

Alternatively, you can run our installation script.

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.

See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

The installer script can be rerun to subsequently install new updates.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="macos-manual-installation" />
<label for="macos-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual Installation</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

If you do not wish to use the previous options, you can install Pulumi manually.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz). For prior versions and release notes, see the [Available Versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4"><i class="fas fa-box pr-2"></i>Install Script</h3>

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

</div>
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Linux Binary Download</h3>
<p><a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz">amd64</a></p>
</div>
</div>

The latest version of Pulumi is {{< latest-version >}}. For older versions, see [Available Versions](/docs/install/versions/).

{{< get-started-note >}}

## Other installation methods

In addition, there are many ways to install Pulumi:

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="linux-installation-script" />
<label for="linux-installation-script" class="accordion-label">
<h5 class="mt-2 w-2/3">Installation Script</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.

See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="linux-manual-installation" />
<label for="linux-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual Installation</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

Alternatively, you can install Pulumi manually. We provide a prebuilt binary for Linux.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz). For prior versions and release notes, see the [Available Versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4"><i class="fas fa-box pr-2"></i>Installer (MSI)</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://github.com/pulumi/pulumi-winget/releases/download/v{{< latest-version >}}/pulumi-{{< latest-version >}}-windows-x64.msi">amd64</a>
</p>
</div>
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Windows Binary Download</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip">amd64</a>
</p>
</div>
</div>

Windows 8 and later are supported.

The latest version of Pulumi is {{< latest-version >}}. For older versions, see [Available Versions](/docs/install/versions/).

{{< get-started-note >}}

## Other installation methods

In addition, there are many ways to install Pulumi:

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="windows-chocolatey" />
<label for="windows-chocolatey" class="accordion-label">
<h5 class="mt-2 w-2/3">Chocolatey</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

You can install Pulumi using elevated permissions through the [Chocolatey package manager](https://chocolatey.org):

```powershell
> choco install pulumi
```

This will install the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`) and generate the [shims](https://docs.chocolatey.org/en-us/features/shim) (usually `$($env:ChocolateyInstall)\bin`) to add Pulumi your path.

Subsequent updates can be installed in the usual way:

```powershell
> choco upgrade pulumi
```

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="windows-winget" />
<label for="windows-winget" class="accordion-label">
<h5 class="mt-2 w-2/3">Windows Package Manager (Winget)</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

Install Pulumi using the Windows Package Manager [`winget`](https://github.com/microsoft/winget-cli/) CLI. This is built-in on Windows 11 and later.

```powershell
> winget install pulumi
```

To update Pulumi to a more recent version:

```powershell
> winget upgrade pulumi
```

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="windows-standalone-installer" />
<label for="windows-standalone-installer" class="accordion-label">
<h5 class="mt-2 w-2/3">Standalone Installer (MSI)</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

<!-- markdownlint-disable url -->
Download the latest [Pulumi Installer for Windows x64](https://github.com/pulumi/pulumi-winget/releases/download/v{{< latest-version >}}/pulumi-{{< latest-version >}}-windows-x64.msi) and run it like any other installer. It will automatically add Pulumi to the path and make it available machine-wide.
<!-- markdownlint-enable url -->

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="windows-installation-script" />
<label for="windows-installation-script" class="accordion-label">
<h5 class="mt-2 w-2/3">Installation Script</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script:

```bat
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="windows-manual-installation" />
<label for="windows-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual Installation</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

Alternatively, you can install Pulumi manually using binaries built for Windows x64.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} binaries for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip). For prior versions and release notes, see the [Available Versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Unzip the file and extract the contents to a folder such as `C:\pulumi`.

1. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

</div>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Verify installation

After installing Pulumi, verify everything is in working order by running the `pulumi` CLI:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

```bash
$ pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{% choosable os windows %}}

```bash
> pulumi version
v{{< latest-version >}}
```

{{% /choosable %}}

{{% /chooser %}}

### Common errors and warnings

These are common installation-related errors or warnings you may encounter.

#### Pulumi not found error

If you get an error that `pulumi` could not be found, it means your path has not been configured correctly. Verify that your system's `$PATH` contains the directory containing the `pulumi` CLI installed earlier.

#### New version warning

If a new version of Pulumi is available, the CLI produces the following example warning when running any of the available commands:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

```
warning: A new version of Pulumi is available. To upgrade from version '2.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% choosable os linux %}}

```
warning: A new version of Pulumi is available. To upgrade from version '2.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% choosable os windows %}}

```
warning: A new version of Pulumi is available. To upgrade from version '2.17.26' to '{{< latest-version >}}', run
   > "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))"

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% /chooser %}}

{{< skip-version-check >}}

## Upgrading Pulumi

If you are upgrading from Pulumi 2.0 to 3.0, please see our [migration guide](/docs/install/migrating-3.0).

## Installing betas and previous versions

Most installation methods choose the latest version by default. To install a specific version, use the following commands. You can find the list of versions on the [Available Versions](/docs/install/versions/) page.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

### Installation script

```bash
$ curl -fsSL https://get.pulumi.com | sh -s -- --version <version>
```

{{% /choosable %}}

{{% choosable os linux %}}

### Installation script

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh -s -- --version <version>
```

{{% /choosable %}}

{{% choosable os windows %}}

### Chocolatey

You can specify a specific version with [Chocolatey package manager](https://chocolatey.org):

```powershell
> choco install pulumi --version <version>
```

### Installation script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script (replace `<version>` with the version number):

```powershell
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $version = '<version>'; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1')).Replace('${Version}', $version)" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

{{% /choosable %}}

{{% /chooser %}}

## Uninstalling Pulumi

To uninstall Pulumi, use your installation method's command of choice. If you installed Pulumi manually, delete the `pulumi` directory that you created. Afterwards, remove the `.pulumi` folder from your home directory which contains plugins and other cached metadata.
