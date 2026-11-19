---
title_tag: "Download & install Pulumi"
meta_desc: Install the Pulumi CLI on macOS, Windows, or Linux with Homebrew, winget, or the install script, then create your first project.
title: "Download & install Pulumi"
h1: Download & install Pulumi
menu:
    install:
        name: "Download & install Pulumi"
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
      - winget
      - msi
      - cli
---

The latest version of Pulumi is **{{< latest-version >}}**. See [available versions](/docs/install/versions/) for earlier releases and the [changelog](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md) for what's new.

## Install Pulumi

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

Install Pulumi with [Homebrew](https://brew.sh/):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos">$ brew install pulumi/tap/pulumi</code></pre>
</div>

Check that it worked:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-version">$ pulumi version</code></pre>
</div>

If your shell can't find `pulumi`, open a new terminal. If that doesn't help, see [`pulumi: command not found`](#pulumi-command-not-found).

{{< details "Other ways to install on macOS" >}}

**Manual installation**

1. Download the archive for your Mac: <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-arm64.tar.gz">Apple silicon (arm64)</a> <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz">Intel (x64)</a>
1. From the directory you downloaded it to, extract the archive and move its files to `~/.pulumi/bin`:

   ```bash
   $ tar -xzf pulumi-*.tar.gz
   $ mkdir -p ~/.pulumi/bin
   $ mv pulumi/* ~/.pulumi/bin/
   ```

1. Add `~/.pulumi/bin` to your `PATH` in your shell profile, which is `~/.zshrc` for the default macOS shell:

   ```bash
   $ echo 'export PATH=$PATH:$HOME/.pulumi/bin' >> ~/.zshrc
   ```

1. Open a new terminal and run `pulumi version`.

**Homebrew core formula:** Use Homebrew's own `pulumi` formula if you'd rather not add the Pulumi tap:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-community">$ brew install pulumi</code></pre>
</div>

**[MacPorts](https://www.macports.org/)**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port">$ sudo port install pulumi</code></pre>
</div>

**Install script:** The script installs Pulumi to `~/.pulumi/bin` and adds it to your `PATH`, or tells you how when it can't:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

{{< /details >}}

{{% /choosable %}}

{{% choosable os windows %}}

Install Pulumi with the [Windows Package Manager](https://learn.microsoft.com/windows/package-manager/winget/) (winget), which comes with Windows 11 and recent versions of Windows 10:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows">&gt; winget install --exact --id Pulumi.Pulumi</code></pre>
</div>

This runs the Pulumi installer (MSI), which installs Pulumi for all users and adds it to your `PATH`. Windows asks you to approve the installation. If you don't have administrator rights, use the install script under **Other ways to install on Windows** instead.

Check that it worked:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-windows-version">&gt; pulumi version</code></pre>
</div>

If your shell can't find `pulumi`, open a new terminal. If that doesn't help, see [`pulumi: command not found`](#pulumi-command-not-found).

{{< details "Other ways to install on Windows" >}}

**Installer (MSI):** Download the installer and run it. It installs Pulumi for all users and adds it to your `PATH`.

<p>
<a class="btn btn-secondary" href="https://github.com/pulumi/pulumi-winget/releases/download/v{{< latest-version >}}/pulumi-{{< latest-version >}}-windows-x64.msi">x64</a>
<a class="btn btn-secondary" href="https://github.com/pulumi/pulumi-winget/releases/download/v{{< latest-version >}}/pulumi-{{< latest-version >}}-windows-arm64.msi">arm64</a>
</p>

**[Chocolatey](https://chocolatey.org):** Run this from an administrator shell:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco">&gt; choco install pulumi</code></pre>
</div>

**Install script:** The script installs Pulumi to `%USERPROFILE%\.pulumi\bin` for your user account only, so it doesn't need administrator rights. Run it from a command prompt (`cmd.exe`):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bat" data-track="install-pulumi-windows-install-script">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

**Manual installation**

1. Download the zip file: <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip">x64</a> <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-arm64.zip">arm64</a>
1. From the folder you downloaded it to, extract it to `C:\` in PowerShell. The zip contains a `pulumi` folder, so this creates `C:\pulumi\bin`:

   ```powershell
   > Expand-Archive pulumi-*.zip -DestinationPath C:\
   ```

1. Add `C:\pulumi\bin` to your `PATH`. In **System Properties** > **Advanced** > **Environment Variables**, select **Path** under **User variables**, then select **Edit** > **New**.
1. Open a new terminal and run `pulumi version`.

{{< /details >}}

{{% /choosable %}}

{{% choosable os linux %}}

Install Pulumi with the install script:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

The script installs Pulumi to `~/.pulumi/bin` and adds it to your `PATH`, or tells you how when it can't.

Check that it worked:

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-version">$ pulumi version</code></pre>
</div>

If your shell can't find `pulumi`, open a new terminal. If that doesn't help, see [`pulumi: command not found`](#pulumi-command-not-found).

{{< details "Other ways to install on Linux" >}}

**Manual installation**

1. Download the archive: <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz">x64</a> <a class="btn btn-secondary" href="https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-arm64.tar.gz">arm64</a>
1. From the directory you downloaded it to, extract the archive and move its files to `~/.pulumi/bin`:

   ```bash
   $ tar -xzf pulumi-*.tar.gz
   $ mkdir -p ~/.pulumi/bin
   $ mv pulumi/* ~/.pulumi/bin/
   ```

1. Add `~/.pulumi/bin` to your `PATH` in your shell profile. For bash:

   ```bash
   $ echo 'export PATH=$PATH:$HOME/.pulumi/bin' >> ~/.bashrc
   ```

1. Open a new terminal and run `pulumi version`.

{{< /details >}}

{{% /choosable %}}

{{< /chooser >}}

<hr class="my-10">

## Next steps

Create your first project. In an empty directory, run `pulumi new` and pick a template for your cloud and language. Templates need that language's runtime installed, such as Node.js or Python. See [Languages & SDKs](/docs/iac/languages-sdks/) for what each one needs.

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-next-steps-new">mkdir my-project
cd my-project
pulumi new</code></pre>
</div>

`pulumi new` asks you to log in to [Pulumi Cloud](/docs/iac/guides/basics/pulumi-cloud-vs-oss/) first, which stores your stack's [state](/docs/iac/concepts/state-and-backends/). You can start on the Free edition without a credit card. To keep state somewhere else, such as your local disk or an S3 bucket, [log in to a DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/) before you run `pulumi new`.

### Guides and resources

{{< link-cards >}}
{{< link-card title="Follow the get-started guide" href="/up/" icon="rocket-launch" wide="true" >}}Pick a template, set up your language and cloud credentials, and deploy it step by step, or hand the steps to your coding agent.{{< /link-card >}}
{{< link-card title="Browse templates" href="/dev/templates/" icon="blueprint" >}}Start from a ready-made project for your cloud and language.{{< /link-card >}}
{{< link-card title="Find a provider" href="/registry/" icon="package" >}}Resources for AWS, Azure, Google Cloud, Kubernetes, and more, with credential setup for each.{{< /link-card >}}
{{< link-card title="Follow a tutorial" href="/dev/tutorials/" icon="list-checks" >}}Build and deploy real infrastructure step by step on your cloud.{{< /link-card >}}
{{< link-card title="Explore Pulumi Cloud" href="/docs/iac/concepts/pulumi-cloud/" icon="cloud" >}}Manage state, secrets, access control, policies, and drift detection for your team.{{< /link-card >}}
{{< /link-cards >}}

<hr class="my-10">

## Upgrade Pulumi

Upgrade Pulumi the same way you installed it.

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

**Homebrew**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-upgrade">$ brew update && brew upgrade pulumi</code></pre>
</div>

**MacPorts**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port-update">$ sudo port selfupdate && sudo port upgrade pulumi</code></pre>
</div>

**Install script or manual installation:** Run the install script again, or repeat the manual installation steps with the new archive.

{{% /choosable %}}

{{% choosable os windows %}}

**winget**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-winget-upgrade">&gt; winget upgrade --exact --id Pulumi.Pulumi</code></pre>
</div>

**Chocolatey**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco-upgrade">&gt; choco upgrade pulumi</code></pre>
</div>

**Installer, install script, or manual installation:** Run the new installer or the install script again, or repeat the manual installation steps with the new zip file.

{{% /choosable %}}

{{% choosable os linux %}}

**Install script**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-upgrade">$ curl -fsSL https://get.pulumi.com | sh</code></pre>
</div>

**Manual installation:** Repeat the manual installation steps with the new archive.

{{% /choosable %}}

{{< /chooser >}}

<hr class="my-10">

## Install a specific version or a dev build

To install a specific version, replace `<version>` with a version number from [available versions](/docs/install/versions/). To install the latest dev build, which includes every change merged to the main branch of [pulumi/pulumi](https://github.com/pulumi/pulumi), use `dev` as the version.

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

**Install script**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-install-script-pinned">$ curl -fsSL https://get.pulumi.com | sh -s -- --version &lt;version&gt;</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

winget and Chocolatey only have released versions. For a dev build, use the install script.

**winget**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-winget-pinned">&gt; winget install --exact --id Pulumi.Pulumi --version &lt;version&gt;</code></pre>
</div>

**Chocolatey**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco-pinned">&gt; choco install pulumi --version &lt;version&gt;</code></pre>
</div>

**Install script:** Run it from a command prompt (`cmd.exe`):

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-install-script-pinned">&gt; @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; &amp; ([ScriptBlock]::Create((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))) -Version &lt;version&gt;" &amp;&amp; SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

**Install script**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-install-script-pinned">$ curl -fsSL https://get.pulumi.com | sh -s -- --version &lt;version&gt;</code></pre>
</div>

{{% /choosable %}}

{{< /chooser >}}

<hr class="my-10">

## Install Pulumi skills for your coding agent

[Pulumi skills](/docs/ai/concepts/agent-skills/) are structured knowledge packages that follow the open [Agent Skills](https://agentskills.io) specification. They work with most coding agents, including Claude Code, GitHub Copilot, Cursor, VS Code, Codex, and Gemini CLI. Once they're installed, your coding agent can follow Pulumi's workflows and code patterns for common infrastructure tasks.

### Claude Code plugin marketplace

In Claude Code, the plugin marketplace is the quickest way to install:

```bash
claude plugin marketplace add pulumi/agent-skills
claude plugin install pulumi-migration      # Install migration skills
claude plugin install pulumi                # Install Pulumi skills (overview + specialized)
claude plugin install pulumi-delegation     # Install delegation skills (Neo handoff)
```

You can install all plugin groups or choose only the ones you need.

### Other coding agents

For Cursor, GitHub Copilot, VS Code, Codex, Gemini CLI, and other coding agents, use the universal [Agent Skills](https://agentskills.io) CLI. The universal installer does not read plugin marketplace manifests, so install each end-user skill group:

```bash
npx skills add pulumi/agent-skills/pulumi --skill '*'
npx skills add pulumi/agent-skills/migration --skill '*'
npx skills add pulumi/agent-skills/delegation --skill '*'
```

You can also connect your coding agent to the [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/) for live access to your Pulumi Cloud stacks, resources, and the Pulumi Registry.

<hr class="my-10">

## Troubleshooting

### `pulumi: command not found`

If your shell can't find `pulumi` after you install it, open a new terminal so it picks up the updated `PATH`. If it still isn't found, add the directory Pulumi was installed to your `PATH`:

| Install method | Directory |
|----------------|-----------|
| Homebrew | `/opt/homebrew/bin` on Apple silicon, `/usr/local/bin` on Intel Macs |
| MacPorts | `/opt/local/bin` |
| Install script (macOS and Linux) | `~/.pulumi/bin` |
| Install script (Windows) | `%USERPROFILE%\.pulumi\bin` |
| winget or the installer (MSI) | Added to your `PATH` automatically. Open a new terminal. |
| Chocolatey | `$($env:ChocolateyInstall)\lib\pulumi\tools\Pulumi\bin` |
| Manual installation | `~/.pulumi/bin` on macOS and Linux, `C:\pulumi\bin` on Windows |

### New version warning

When a newer version is available, the CLI prints a warning like this one:

```
warning: A new version of Pulumi is available. To upgrade from version '3.200.0' to '{{< latest-version >}}', run
   $ brew update && brew upgrade pulumi
or visit https://pulumi.com/docs/install/ for manual instructions and release notes.
```

The command in the warning depends on how you installed Pulumi. When the CLI can't tell, it links to this page. See [Upgrade Pulumi](#upgrade-pulumi).

{{< skip-version-check >}}

<hr class="my-10">

## Minimum system requirements

<!--
## Rationale for Minimum System Requirements

Please see https://github.com/pulumi/pulumi-benchmarking where we have a benchmarking codebase to represent typical pulumi actions.

The results from this benchmark were 10% CPU utilization on a Apple M1 Pro for the apply and 20% CPU utilization for the destroy.
The memory usage for both was 1.5GB.

So the following recommendations were made to add some headroom for the typical pulumi actions, especially for larger projects.
-->

These are the minimums for typical use. Larger programs and programs that use many providers need more.

| Component            | Recommendation                                                                                       |
|----------------------|------------------------------------------------------------------------------------------------------|
| **Operating system** | macOS 13 (Ventura) or later, Windows 10 or Windows Server 2016 or later, or Linux; on x64 or arm64   |
| **CPU**              | 2 GHz or faster processor (or equivalent vCPUs for cloud environments)                               |
| **RAM**              | 4 GB or more                                                                                         |
| **Disk space**       | 1 GB or more free disk space, plus room for language runtimes and provider plugins                   |

<hr class="my-10">

## Uninstall Pulumi

Uninstall Pulumi the same way you installed it.

{{% notes type="warning" %}}
If you use a local DIY backend at its default location, the `.pulumi` folder in your home directory holds your stack state. Back it up before you delete the folder.
{{% /notes %}}

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

**Homebrew**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-brew-uninstall">$ brew uninstall pulumi</code></pre>
</div>

**MacPorts**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-port-uninstall">$ sudo port uninstall pulumi</code></pre>
</div>

**Install script:** Delete the `.pulumi` folder in your home directory. Then remove the `# add Pulumi to the PATH` line and the `export PATH` line after it from your shell profile, such as `~/.zshrc` or `~/.bashrc`.

**Manual installation:** Delete the `.pulumi` folder in your home directory, and remove the `export PATH` line you added to your shell profile.

{{% /choosable %}}

{{% choosable os windows %}}

**winget**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-winget-uninstall">&gt; winget uninstall --exact --id Pulumi.Pulumi</code></pre>
</div>

**Chocolatey**

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="powershell" data-track="install-pulumi-windows-choco-uninstall">&gt; choco uninstall pulumi</code></pre>
</div>

**Installer (MSI):** Uninstall Pulumi from **Settings** > **Apps** > **Installed apps**.

**Install script:** Delete the `.pulumi` folder in your home directory. Then remove `%USERPROFILE%\.pulumi\bin` from your user `PATH` in **System Properties** > **Advanced** > **Environment Variables**.

**Manual installation:** Delete `C:\pulumi`, and remove `C:\pulumi\bin` from your user `PATH`.

{{% /choosable %}}

{{% choosable os linux %}}

**Install script:** Delete the `.pulumi` folder in your home directory. Then remove the `# add Pulumi to the PATH` line and the `export PATH` line after it from your shell profile, such as `~/.zshrc` or `~/.bashrc`.

**Manual installation:** Delete the `.pulumi` folder in your home directory, and remove the `export PATH` line you added to your shell profile.

{{% /choosable %}}

{{< /chooser >}}

Whichever method you used, delete the `.pulumi` folder in your home directory too. It holds plugins, credentials, and the install script's copy of the CLI.
