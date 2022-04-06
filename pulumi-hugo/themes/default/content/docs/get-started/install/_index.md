---
title: "Download and Install"
meta_desc: This page contains detailed instructions for installing Pulumi.
no_on_this_page: true
menu:
  getstarted:
      weight: 10

aliases: ["/docs/reference/install/"]
---

<!--
NOTE: To update this page with a new binary release, do the following:
- Update `static/latest-version`
- Update `content/docs/get-started/install/versions.md`
-->

This page contains detailed instructions for [installing Pulumi](#installing-pulumi) on your machine. For links to detailed release notes, see the [Available Versions]({{< relref "versions" >}}) page.

{{< get-started-note >}}

## Installing Pulumi

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

macOS Sierra (10.12) or later is required.

### Homebrew

You can install Pulumi through the [Homebrew package manager](https://brew.sh/):

```bash
$ brew install pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
```

### MacPorts

You can install Pulumi through the [MacPorts package manager](https://www.macports.org/):

```bash
$ sudo port install pulumi
```

This will install the `pulumi` CLI to `/opt/local/bin/pulumi` and add it to your path.

Subsequent updates can be installed through the `upgrade outdated` command:

```bash
$ sudo port upgrade outdated
```

### Installation Script

Alternatively, you can run our installation script.

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.
See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

The installer script can be rerun to subsequently install new updates.

### Manual Installation

If you do not wish to use the previous options, you can install Pulumi manually.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz). For prior versions and release notes, see the [Available Versions]({{< relref "/docs/get-started/install/versions" >}}) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

{{% /choosable %}}

{{% choosable os linux %}}

### Installation Script

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.
See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

### Manual Installation

Alternatively, you can install Pulumi manually. We provide a prebuilt binary for Linux.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz). For prior versions and release notes, see the [Available Versions]({{< relref "/docs/get-started/install/versions" >}}) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

{{% /choosable %}}

{{% choosable os windows %}}

Windows 8 and later are supported.

### Chocolatey

You can install Pulumi using elevated permissions through the [Chocolatey package manager](https://chocolatey.org):

```powershell
> choco install pulumi
```

This will install the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`) and generate the [shims](https://docs.chocolatey.org/en-us/features/shim) (usually `$($env:ChocolateyInstall)\bin`) to add Pulumi your path.

Subsequent updates can be installed in the usual way:

```powershell
> choco upgrade pulumi
```

### Winget

Install Pulumi using the [winget-cli](https://github.com/microsoft/winget-cli/) package manager. This is built-in on Windows 11 and later.

```powershell
> winget install pulumi
```

To update Pulumi to a more recent version:

```powershell
> winget upgrade pulumi
```

### Standalone Installer

You can download the latest [Pulumi Installer for Windows x64](https://github.com/pulumi/pulumi-winget/releases) and run it like any other installer. It will automatically add Pulumi to the path and make it available machine-wide.

### Installation Script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script:

```bat
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

### Manual Installation

Alternatively, you can install Pulumi manually using binaries built for Windows x64.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} binaries for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip). For prior versions and release notes, see the [Available Versions]({{< relref "/docs/get-started/install/versions" >}}) page.
<!-- markdownlint-enable url -->

1. Unzip the file and extract the contents to a folder such as `C:\pulumi`.

1. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

{{% /choosable %}}

{{% /chooser %}}

## Verifying your Installation

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

### Pulumi Not Found Error

If you get an error that `pulumi` could not be found, it means your path has not been configured correctly. Verify that your system's `$PATH` contains the directory containing the `pulumi` CLI installed earlier.

### New Version Warning

If a new version of Pulumi is available, the CLI produces the following example warning when running any of the available commands:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

```
warning: A new version of Pulumi is available. To upgrade from version '0.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% choosable os linux %}}

```
warning: A new version of Pulumi is available. To upgrade from version '0.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% choosable os windows %}}

```
warning: A new version of Pulumi is available. To upgrade from version '0.17.26' to '{{< latest-version >}}', run
   > "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))"

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

{{% /choosable %}}

{{% /chooser %}}

{{< skip-version-check >}}

## Upgrading Pulumi

If you are upgrading to Pulumi 3.0, please see our [migration guide]({{< relref "/docs/get-started/install/migrating-3.0.md" >}}).

## Installing Betas and Previous Versions

You can find the list of versions on the [Available Versions]({{< relref "/docs/get-started/install/versions" >}}) page.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

### Installation Script

```bash
$ curl -fsSL https://get.pulumi.com | sh -s -- --version <version>
```

{{% /choosable %}}

{{% choosable os linux %}}

### Installation Script

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

### Installation Script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script (replace `<version>` with the version number):

```powershell
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $version = '<version>'; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1')).Replace('${Version}', $version)" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

{{% /choosable %}}

{{% /chooser %}}

## Uninstalling Pulumi

To uninstall Pulumi, remove the `.pulumi` folder from your home directory. If you installed Pulumi manually, you should
also remove the `pulumi` folder that was created.
