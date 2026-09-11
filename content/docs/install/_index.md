---
title_tag: "Download & Install Pulumi"
meta_desc: This page contains detailed instructions for downloading and installing Pulumi.
title: "Download & Install Pulumi"
h1: Download & Install Pulumi
menu:
    install:
        name: "Download & Install Pulumi"
        identifier: install-home
        weight: 1

aliases:
  - /docs/iac/download-install/
  - /get-started/install/
  - /docs/reference/install/
  - /install/
  - /docs/install
  - /docs/get-started/install/
  - /docs/get-started/download-install/
  - /docs/install/migrating-3.0/
  - /docs/install/migrating-2.0
  - /docs/iac/download-install/migrating-3.0/
  - /docs/get-started/install/migrating-3.0/
  - /docs/get-started/install/migrating-2.0/
  - /docs/get-started/download-install/migrating-3.0/
  - /docs/iac/install

search:
   boost: true
   keywords:
      - install
      - homebrew
      - msi
      - cli
---

The latest version of Pulumi is **{{< latest-version >}}**. For previous versions, see [Available versions](/docs/install/versions/). For a list of features, bug fixes, and more see the [CHANGELOG](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md).

By default, the Pulumi CLI stores state in [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/), our free, hosted state-management backend. Pulumi Cloud is free for individuals and is the recommended backend when you're learning Pulumi — no credit card required. If you'd rather host state yourself (S3, Azure Blob, GCS, or local), see [self-managed state backends](/docs/iac/concepts/state-and-backends/).

{{% notes type="info" %}}
You don't need a Pulumi Cloud account to install the CLI. You'll be prompted to sign in (or to pick a self-managed backend) the first time you run `pulumi login`.
{{% /notes %}}

## Choose an operating system

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

<h3 class="no-anchor pt-4">{{< icon name="package" class="pr-2" >}}Homebrew package manager</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos">$ brew install pulumi/tap/pulumi</code></pre>
</div>

<h3 class="no-anchor pt-4">{{< icon name="download-simple" class="pr-2" >}}macOS binary download</h3>

<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz">amd64</a>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-arm64.tar.gz">arm64</a>

macOS Ventura (13) or later is required.

{{< get-started-note >}}

{{% /choosable %}}

{{% choosable os linux %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4">{{< icon name="package" class="pr-2" >}}Install script</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

</div>
<div class="w-full">
<h3 class="no-anchor pt-4">{{< icon name="download-simple" class="pr-2" >}}Linux binary download</h3>
<p><a class="btn btn-secondary mx-2" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz">amd64</a></p>
</div>
</div>

{{< get-started-note >}}

{{% /choosable %}}

{{% choosable os windows %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full md:w-3/4">
<h3 class="no-anchor pt-4">{{< icon name="package" class="pr-2" >}}Installer (MSI)</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://github.com/pulumi/pulumi-winget/releases/download/v{{< latest-version >}}/pulumi-{{< latest-version >}}-windows-x64.msi">amd64</a>
</p>
</div>
<div class="w-full">
<h3 class="no-anchor pt-4">{{< icon name="download-simple" class="pr-2" >}}Windows binary download</h3>
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

Pulumi also supports these installation methods:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}
<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-official-homebrew-tap" />
<label for="macos-official-homebrew-tap" class="accordion-label">
<h5 class="mt-2 w-2/3">Official Pulumi Homebrew tap</h5>
<div class="flex flex-grow justify-end items-center">
<span class="closed-accordion">+</span>
<span class="open-accordion hidden">-</span>
</div>
</label>
<div class="accordion-item-body-no-animation text-base">

You can install Pulumi through the [Homebrew package manager](https://brew.sh/) using our official
[Pulumi Homebrew tap](https://github.com/pulumi/homebrew-tap/).

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-official">$ brew install pulumi/tap/pulumi</code></pre>
</div>

This installs the `pulumi` CLI into your Homebrew prefix — `/opt/homebrew/bin/pulumi` on Apple silicon, `/usr/local/bin/pulumi` on Intel Macs — and adds it to your path.

Install subsequent updates the same way you update any other formula:

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

A Pulumi formula is also available from the community Homebrew repository. If you do not have the Pulumi tap
installed, you can still install Pulumi with Homebrew:

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

This installs the `pulumi` CLI to `/opt/local/bin/pulumi` and adds it to your path.

Install subsequent updates with the `upgrade outdated` command:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port-update">$ sudo port upgrade outdated</code></pre>
</div>

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="macos-installation-script" />
<label for="macos-installation-script" class="accordion-label">
<h5 class="mt-2 w-2/3">Installation script</h5>
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

This installs the `pulumi` CLI to `~/.pulumi/bin` and adds it to your path. When it can't add `pulumi` to your path automatically, it prompts you to add it manually.

See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

Rerun the installer script to install later updates.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="macos-manual-installation" />
<label for="macos-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual installation</h5>
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
<h5 class="mt-2 w-2/3">Installation script</h5>
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

This installs the `pulumi` CLI to `~/.pulumi/bin` and adds it to your path. When it can't add `pulumi` to your path automatically, it prompts you to add it manually.

See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="linux-manual-installation" />
<label for="linux-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual installation</h5>
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

This installs the `pulumi` CLI to the usual place (often `$($env:ChocolateyInstall)\lib\pulumi`) and generates the [shims](https://docs.chocolatey.org/en-us/features/shim) (usually `$($env:ChocolateyInstall)\bin`) that add Pulumi to your path.

Install subsequent updates the usual way:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco-upgrade">&gt; choco upgrade pulumi</code></pre>
</div>

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2">
<input type="checkbox" class="absolute hidden" id="windows-winget" />
<label for="windows-winget" class="accordion-label">
<h5 class="mt-2 w-2/3">Windows Package Manager (winget)</h5>
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
<h5 class="mt-2 w-2/3">Standalone installer (MSI)</h5>
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
<h5 class="mt-2 w-2/3">Installation script</h5>
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

This installs the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and adds it to your path.

</div>
</div>

<div class="accordion-item text-2xl py-3 border-t-2 border-b-2">
<input type="checkbox" class="absolute hidden" id="windows-manual-installation" />
<label for="windows-manual-installation" class="accordion-label">
<h5 class="mt-2 w-2/3">Manual installation</h5>
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

If a new version of Pulumi is available, the CLI prints a warning like this one when you run any command:

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

## Installing betas and previous versions

Most installation methods choose the latest version by default. To install a specific version, use the following commands. You can find the list of versions on the [Available versions](/docs/install/versions/) page.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

<h3 class="no-anchor pt-4">macOS installation script</h3>

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version &lt;version&gt;</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<h3 class="no-anchor pt-4">Linux installation script</h3>

To install, run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version &lt;version&gt;</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<h3 class="no-anchor pt-4">Chocolatey</h3>

You can specify a specific version with [Chocolatey package manager](https://chocolatey.org):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco">&gt; choco install pulumi --version</code></pre>
</div>

<h3 class="no-anchor pt-4">Windows installation script</h3>

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script (replace `<version>` with the version number):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $version = '<version>'; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1')).Replace('${Version}', $version)" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Installing dev releases

Besides a specific version, you can also install the latest dev version automatically. This version contains the latest changes merged to the main development branch.

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

### macOS installation script

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

### Linux installation script

To install, run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script">$ curl -fsSL https://get.pulumi.com | sh -s -- --version dev</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

### Windows installation script

1. Open a new command prompt window (**WIN+R**: `cmd.exe`):

1. Run our installation script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; &amp; ([ScriptBlock]::Create((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))) -Version dev" &amp;&amp; SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

{{% /choosable %}}

{{% /chooser %}}

## Minimum system requirements

<!--
## Rationale for Minimum System Requirements

Please see https://github.com/pulumi/pulumi-benchmarking where we have a benchmarking codebase to represent typical pulumi actions.

The results from this benchmark were 10% CPU utilization on a Apple M1 Pro for the apply and 20% CPU utilization for the destroy.
The memory usage for both was 1.5GB.

So the following recommendations were made to add some headroom for the typical pulumi actions, especially for larger projects.
-->

The following are general recommendations for minimum system requirements when using Pulumi. Actual performance varies with the SDK runtime, the providers you use, your operating system, and the size and complexity of your infrastructure deployments — but treat these figures as a floor for typical usage.

| Component      | Recommendation                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| **CPU**        | 2 GHz or faster processor (or equivalent vCPUs for cloud environments)                                                      |
| **RAM**        | 4 GB or more                                                                                                                |
| **Disk Space** | 1 GB or more free disk space (additional space may be required when using multiple runtimes, providers, or large codebases) |

{{% notes type="info" %}}
System requirements vary widely with the providers you use and how you manage packages and plugins. Using multiple providers or large plugins may require additional disk space. Your SDK runtime (for example, Node.js, Python, or Go), your operating system, and how you manage packages in your development environment also affect performance. CPU and RAM requirements depend on the complexity of your infrastructure, the runtimes, the packages and plugins used, and how much of a `pulumi preview` or `pulumi up` operation can run in parallel.
{{% /notes %}}

## Enhance your AI coding assistant with agent skills

Skills are structured knowledge packages that follow the open [Agent Skills](https://agentskills.io) specification. They work across multiple AI coding platforms including Claude Code, GitHub Copilot, Cursor, VS Code, Codex, and Gemini CLI. When you install Pulumi skills, your AI assistant gains access to detailed workflows, code patterns, and decision trees for common infrastructure tasks.

### Claude Code plugin marketplace

For Claude Code users, the plugin system provides the simplest installation experience:

```bash
claude plugin marketplace add pulumi/agent-skills
claude plugin install pulumi-migration      # Install migration skills
claude plugin install pulumi                # Install Pulumi skills (overview + specialized)
claude plugin install pulumi-delegation     # Install delegation skills (Neo handoff)
```

You can install all plugin groups or choose only the ones you need.

### Universal installation

For Cursor, GitHub Copilot, VS Code, Codex, Gemini, and other platforms, use the universal [Agent Skills](https://agentskills.io) CLI. The universal installer does not read plugin marketplace manifests, so install each end-user skill group:

```bash
npx skills add pulumi/agent-skills/pulumi --skill '*'
npx skills add pulumi/agent-skills/migration --skill '*'
npx skills add pulumi/agent-skills/delegation --skill '*'
```

You can also connect your assistant to the [Pulumi MCP server](/docs/ai/mcp-server/) for live access to your Pulumi Cloud stacks, resources, and the Pulumi Registry.

## Uninstalling Pulumi

To uninstall Pulumi, use the uninstall command for the method you installed it with. If you installed Pulumi manually, delete the `pulumi` directory that you created. Then remove the `.pulumi` folder from your home directory, which holds plugins and other cached metadata.
