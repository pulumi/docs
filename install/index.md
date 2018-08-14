---
title: "Installation and Setup"
installer_version: "0.15.0"
---

<!--
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above.
- Update changelog.md with the latest fixes in the release
-->

To install Pulumi, run the following command from a terminal:

**On macOS or Linux**:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path.

**On Windows** (in a cmd.exe shell):

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

The installer script downloads and installs Pulumi, or upgrades to the latest version if you've already installed it.

## Cloud Configuration

After installation, you will want to configure Pulumi for your cloud provider:

* [AWS](./aws.html)
* [Azure](./azure.html)
* [GCP](./gcp.html)
* [Kubernetes](./kubernetes.html)

## Verifying the Installation

After installing, verify everything is in working order by running the `pulumi` CLI:

```bash
$ pulumi version
v{{page.installer_version}}
```

If you get an error that `pulumi` could not be found, it means your `PATH` environment variable has not been configured
correctly. Please go back and ensure your `PATH` contains the directory containing the `pulumi` CLI installed earlier.

## Older Versions

The current Pulumi SDK version is {{ page.installer_version }}. For a full history of past SDK versions, including
release notes, please visit <a href="./changelog.html">the Change Log</a>.

## Manual Installation {#instructions}

Packages are available for all major operating systems if you prefer to install them manually.

### Manual macOS Install {#mac}

macOS Sierra (10.12) or later is required.

1. Download [Pulumi {{page.installer_version}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-darwin-x64.tar.gz).

2. Unzip the tarball and run the install script. After installation, you may delete the extracted folder.

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-darwin-x64.tar.gz
    $ ./pulumi/install.sh
    ```

3. Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

### Manual Linux Install {#linux}

We provide a pre-built binary for Linux.

1. Download [Pulumi {{page.installer_version}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-linux-x64.tar.gz).

2. Unzip the tarball and run the install script. After installation, you may delete the extracted folder.

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-linux-x64.tar.gz
    $ ./pulumi/install.sh
    ```

3. Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

### Manual Windows Install {#windows}

Windows 8 and 10 are supported.

1. Download [Pulumi {{page.installer_version}} for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-windows-x64.zip).

2. Copy the extracted zipfile contents to a folder such as `C:\pulumi`.

3. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

## Uninstalling Pulumi

To uninstall Pulumi, delete the `.pulumi` folder in your home directory. If you used the manual installer, you should
also delete the `pulumi` folder that was created.
