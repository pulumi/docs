---
title_tag: Download & Install Pulumi ESC
meta_desc: Detailed instructions for downloading and installing Pulumi ESC (Environments, Secrets and Configuration).
title: Pulumi ESC
h1: Download & install Pulumi ESC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  install:
    weight: 2
search:
   boost: true
   keywords:
      - install
      - homebrew
      - cli
---

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

## Package manager

```bash
$ brew install pulumi/tap/esc
```

### MacOS binary download

<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v0.5.1-darwin-x64.tar.gz">amd64</a>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v0.5.1-darwin-arm64.tar.gz">arm64</a></p>

macOS Sierra (10.12) or later is required.

The latest version of Pulumi ESC is 0.5.1.

{{% notes type="info" %}}
For a streamlined Pulumi ESC walkthrough, including language runtime installation and cloud configuration, see the [Get Started](/docs/pulumi-cloud/esc/getting-started) guides.
{{% /notes %}}

## Other installation methods

In addition, there are many ways to install Pulumi ESC:

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

You can install Pulumi ESC through the [Homebrew package manager](https://brew.sh/) and using our official
[Pulumi Homebrew Tap](https://github.com/pulumi/homebrew-tap/)

```bash
$ brew install pulumi/tap/esc
```

This will install the `esc` CLI to the usual place (often `/usr/local/bin/esc`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade esc
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
still install Pulumi ESC from homebrew using the command:

```bash
$ brew install esc
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
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh
```

This will install the `esc` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `esc` to your path, you will be prompted to add it manually.

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
1. Download [Pulumi ESC 0.5.1 for macOS](https://get.pulumi.com/esc/releases/esc-v0.5.1-darwin-x64.tar.gz).
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `esc` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4"><i class="fas fa-box pr-2"></i>Install Script</h3>

```bash
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh
```

</div>
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Linux Binary Download</h3>
<p><a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v0.5.1-linux-x64.tar.gz">amd64</a></p>
</div>
</div>

The latest version of Pulumi ESC is 0.5.1.

{{< get-started-note >}}

## Other installation methods

In addition, there are many ways to install Pulumi ESC:

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
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh
```

This will install the `esc` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `esc` to your path, you will be prompted to add it manually.

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

Alternatively, you can install Pulumi ESC manually. We provide a prebuilt binary for Linux.

<!-- markdownlint-disable url -->
1. Download [Pulumi ESC 0.5.1 for Linux x64](https://get.pulumi.com/esc/releases/esc-v0.5.1-linux-x64.tar.gz).
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `esc` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Windows Binary Download</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v0.5.1-windows-x64.zip">amd64</a>
</p>
</div>
</div>

Windows 8 and later are supported.

The latest version of Pulumi ESC is 0.5.1. For older versions, see [Available Versions](/docs/install/versions/).

{{< get-started-note >}}

## Other installation methods

In addition, there are many ways to install Pulumi ESC:

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
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/esc/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `esc.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

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

Alternatively, you can install Pulumi ESC manually using binaries built for Windows x64.

<!-- markdownlint-disable url -->
1. Download [Pulumi ESC 0.5.1 binaries for Windows x64](https://get.pulumi.com/esc/releases/esc-v0.5.1-windows-x64.zip). For prior versions and release notes, see the [Available Versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Unzip the file and extract the contents to a folder such as `C:\esc`.

1. Add `C:\esc\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

</div>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Verify installation

After installing Pulumi ESC, verify everything is in working order by running the `esc` CLI:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

```bash
$ esc version
v0.5.1
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ esc version
v0.5.1
```

{{% /choosable %}}

{{% choosable os windows %}}

```bash
> esc version
v0.5.1
```

{{% /choosable %}}

{{% /chooser %}}

### Common errors and warnings

These are common installation-related errors or warnings you may encounter.

#### Pulumi ESC not found error

If you get an error that `esc` could not be found, it means your path has not been configured correctly. Verify that your system's `$PATH` contains the directory containing the `esc` CLI installed earlier.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

### Installation script

```bash
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh -s -- --version <version>
```

{{% /choosable %}}

{{% choosable os linux %}}

### Installation script

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com/esc/install.sh | sh -s -- --version <version>
```

{{% /choosable %}}

{{% choosable os windows %}}

### Installation script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script (replace `<version>` with the version number):

```powershell
> @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $version = '<version>'; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/esc/install.ps1')).Replace('${Version}', $version)" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

{{% /choosable %}}

{{% /chooser %}}

## Uninstalling Pulumi ESC

To uninstall Pulumi ESC, use your installation method's command of choice. If you installed Pulumi ESC manually, delete the `esc` directory that you created. Afterwards, remove the `.pulumi` folder from your home directory which contains plugins and other cached metadata.
