---
title_tag: "Download & Install Pulumi"
meta_desc: This page contains detailed instructions for downloading and installing
  Pulumi.
title: "Download & install"
h1: Download & install Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    parent: iac-home
    weight: 10
    identifier: iac-install
  install:
    name: Overview
    weight: 1

aliases:
  - /get-started/install/
  - /docs/reference/install/
  - /docs/get-started/install/
  - /install/
  - /docs/install

search:
  boost: true
  keywords:
    - install
    - homebrew
    - msi
    - cli
    - instructions
    - download
    - downloading
    - class
    - installing
    - accordion
---

The latest version of Pulumi is **{{< latest-version >}}**. For previous versions, see [Available versions](/docs/install/versions/). For a list of features, bug fixes, and more see the [CHANGELOG](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md).

## Choose an operating system

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

<h3 class="no-anchor pt-4"><i class="fas fa-box pr-2"></i>Homebrew Package Manager</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos">$ brew install pulumi/tap/pulumi</code></pre>
</div>

<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>macOS Binary Download</h3>

<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz">amd64</a>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-arm64.tar.gz">arm64</a></p>

macOS Ventura (13) or later is required.

{{< get-started-note >}}

{{% /choosable %}}

{{% choosable os linux %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4"><i class="fas fa-box pr-2"></i>Install Script</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

</div>
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Linux Binary Download</h3>
<p><a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz">amd64</a></p>
</div>
</div>

{{< get-started-note >}}

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

{{< get-started-note >}}

{{% /choosable %}}

{{% /chooser %}}

## More installation methods

In addition, there are many ways to install Pulumi:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}
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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-official">$ brew install pulumi/tap/pulumi</code></pre>
</div>

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-upgrade">$ brew upgrade pulumi</code></pre>
</div>

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-community">$ brew install pulumi</code></pre>
</div>

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port">$ sudo port install pulumi</code></pre>
</div>

This will install the `pulumi` CLI to `/opt/local/bin/pulumi` and add it to your path.

Subsequent updates can be installed through the `upgrade outdated` command:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port-update">$ sudo port upgrade outdated</code></pre>
</div>

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

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
1. Download [Pulumi {{< latest-version >}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz). For prior versions and release notes, see the [Available versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

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
1. Download [Pulumi {{< latest-version >}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz). For prior versions and release notes, see the [Available versions](/docs/install/versions/) page.
<!-- markdownlint-enable url -->

1. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

</div>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco">&gt; choco install pulumi</code></pre>
</div>

This will install the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`) and generate the [shims](https://docs.chocolatey.org/en-us/features/shim) (usually `$($env:ChocolateyInstall)\bin`) to add Pulumi your path.

Subsequent updates can be installed in the usual way:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco-upgrade">&gt; choco upgrade pulumi</code></pre>
</div>

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-winget">&gt; winget install pulumi</code></pre>
</div>

To update Pulumi to a more recent version:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-winget-upgrade">&gt; winget upgrade pulumi</code></pre>
</div>

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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bat" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

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
1. Download [Pulumi {{< latest-version >}} binaries for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip). For prior versions and release notes, see the [Available versions](/docs/install/versions/) page.
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

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-version">$ pulumi version</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-version">$ pulumi version</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-windows-version">&gt; pulumi version</code></pre>
</div>

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

Most installation methods choose the latest version by default. To install a specific version, use the following commands. You can find the list of versions on the [Available versions](/docs/install/versions/) page.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

<h3 class="no-anchor pt-4">macOS Installation Script</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version <version></code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<h3 class="no-anchor pt-4">Linux Installation Script</h3>

To install, run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version <version></code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<h3 class="no-anchor pt-4">Chocolatey</h3>

You can specify a specific version with [Chocolatey package manager](https://chocolatey.org):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco">&gt; choco install pulumi --version</code></pre>
</div>

<h3 class="no-anchor pt-4">Windows Installation Script</h3>

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script (replace `<version>` with the version number):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $version = '<version>'; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1')).Replace('${Version}', $version)" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Installing dev releases

In addition to installing a specific version, the latest dev version can also be installed automatically.  This version contains the latest changes that have been merged to the main development branch.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

### macOS Installation Script

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

### Linux Installation Script

To install, run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

### Windows Installation Script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString</code></pre>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Minimum system requirements

<!--
## Rationale for Minimum System Requirements

Please see https://github.com/pulumi/pulumi-benchmarking where we have a benchmarking codebase to represent typical pulumi actions.

The results from this benchmark were 10% CPU utilization on a Apple M1 Pro for the apply and 20% CPU utilization for the destroy.
The memory usage for both was 1.5GB.

So the following recommendations were made to add some headroom for the typical pulumi actions, espciailly for larger projects.
-->

The following are general recommendations for minimum system requirements when using Pulumi. Actual performance may vary based on the SDK runtime, providers used, operating system and the size and complexity of your infrastructure deployments. However, the following requirements should be considered a minimum to account for typical usage.

| Component      | Recommendation                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| **CPU**        | 2 GHz or faster processor (or equivalent vCPUs for cloud environments)                                                      |
| **RAM**        | 4 GB or more                                                                                                                |
| **Disk Space** | 1 GB or more free disk space (additional space may be required when using multiple runtimes, providers, or large codebases) |

{{% notes "info" %}}
System requirements can vary significantly depending on the providers used and how packages/plugins are managed. Using multiple providers or large plugins may require additional disk space. Performance may also be impacted by the runtime for the SDK you are using (e.g., Node.js, Python, Go), the operating system, and how packages are managed in your development environment. Additionally, CPU and RAM requirements can be influenced by the complexity of your infrastructure, the runtimes, and the packages/plugins used, as well as the ability to take advantage of parallel processing during `pulumi plan` and `pulumi apply` operations.
{{% /notes %}}

## Uninstalling Pulumi

To uninstall Pulumi, use your installation method's command of choice. If you installed Pulumi manually, delete the `pulumi` directory that you created. Afterwards, remove the `.pulumi` folder from your home directory which contains plugins and other cached metadata.
