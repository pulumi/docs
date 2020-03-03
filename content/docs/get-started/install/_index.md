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

This page contains detailed instructions for [installing Pulumi](#install-pulumi) on your machine. For links to detailed release notes, see the [Available Versions]({{< relref "versions" >}}) page.

{{< get-started-note >}}

## Install Pulumi

{{< oschoose >}}

<div class="os-prologue-macos"></div>
<div class="mt-8">
{{% md %}}

### Homebrew

macOS Sierra (10.12) or later is required.

You can install Pulumi through the [Homebrew package manager](https://brew.sh/):

```bash
$ brew install pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
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

{{% /md %}}
</div>

<div class="os-prologue-linux"></div>
<div class="mt-8">
{{% md %}}

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

{{% /md %}}
</div>

<div class="os-prologue-windows"></div>
<div class="mt-8">
{{% md %}}

### Chocolatey

You can install Pulumi through the [Chocolatey package manager](https://chocolatey.org):

```powershell
choco install pulumi
```

This will install the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`), will generate [shims](https://chocolatey.org/docs/features-shim) (usually `$($env:ChocolateyInstall)\bin`) that is added to your path.

Subsequent updates can be installed in the usual way:

```powershell
choco upgrade pulumi
```

### Installation Script

Windows 8 and 10 are supported.

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script:

   ```bat
   @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
   ```

   This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

### Manual Installation

Alternatively, you can install Pulumi manually.

<!-- markdownlint-disable url -->
1. Download [Pulumi {{< latest-version >}} for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip). For prior versions and release notes, see the [Available Versions]({{< relref "/docs/get-started/install/versions" >}}) page.
<!-- markdownlint-enable url -->

1. Unzip the file and extract the contents to a folder such as `C:\pulumi`.

1. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

{{% /md %}}
</div>

## Verify your Installation

After installing Pulumi, verify everything is in working order by running the `pulumi` CLI:

```bash
$ pulumi version
v{{< latest-version >}}
```

### Pulumi Not Found Error

If you get an error that `pulumi` could not be found, it means your path has not been configured correctly. Verify that your system's `$PATH` contains the directory containing the `pulumi` CLI installed earlier.

### New Version Warning

If a new version of Pulumi is available, the CLI produces the following example warning when running any of the available commands:

```
warning: A new version of Pulumi is available. To upgrade from version '0.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/install/ for manual instructions and release notes.
```

{{< skip-version-check >}}

## Uninstall Pulumi

To uninstall Pulumi, remove the `.pulumi` folder from your home directory. If you installed Pulumi manually, you should
also remove the `pulumi` folder that was created.
