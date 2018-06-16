---
title: "Installation and Setup"
installer_version: "0.14.0"
---

<!-- 
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above. 
- Update changelog.md with the latest fixes in the release
-->

The current Pulumi SDK version is <a href="./changelog.html#{{ page.installer_version }}">{{ page.installer_version }}</a>.  For older SDK versions, please see <a href="./changelog.html#all-versions">Previous SDK Versions</a>.

## Easy Install

### macOS and Linux

Run the following command to install the latest version of Pulumi:

```bash
curl -fsSL https://get.pulumi.com | sh
```

### Windows

Run the following command (in `cmd.exe`) to install the latest version of Pulumi:

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

### Cloud Configuration

After running this command, Pulumi is installed, and you can move on to configuring Pulumi for your cloud provider:

* [AWS](./aws.html)
* [Azure](./azure.html)
* [GCP](./gcp.html)
* [Kubernetes](./kubernetes.html)

## Manual Installation {#instructions}

If you prefer, you can download and install Pulumi manually.

<div class="downloads-container">
    <div class="download-card">
        <h2>macOS x64</h2>
        <p>macOS Sierra 10.12 or later is required. More information is <a href="#mac">below</a>.</p>
        <a
                id="macos-download-link"
                class="download-button"
                role="button"
                href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-darwin-x64.tar.gz">
            <button class="button">DOWNLOAD</button>
        </a>
    </div>
    <div class="download-card">
        <h2>Linux x64</h2>
        <p>Pre-built binaries for most Linux distros. More information is <a href="#linux">below</a>.</p>
        <a
                id="linux-download-link"
                class="download-button"
                role="button"
                href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-linux-x64.tar.gz">
            <button class="button">DOWNLOAD</button>
        </a>
    </div>
    <div class="download-card">
        <h2>Windows x64</h2>
        <p>Windows 8 or 10 are supported. More information is <a href="#windows">below</a>.</p>
        <a
                id="windows-download-link"
                class="download-button"
                role="button"
                href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-windows-x64.zip">
            <button class="button">DOWNLOAD</button>
        </a>
    </div>
</div>

### Windows install {#windows}

Windows 8 and 10 are supported.

1.  Download [Pulumi {{page.installer_version}} for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-windows-x64.zip).

1.  Copy the extracted zipfile contents to a folder such as `C:\pulumi`.

1. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

### macOS install {#mac}

macOS Sierra (10.12) or later is required. 

1.  Download [Pulumi {{page.installer_version}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-darwin-x64.tar.gz).

1.  Unzip the tarball and run the install script. After installation, you may delete the extracted folder. 

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-darwin-x64.tar.gz
    $ ./pulumi/install.sh 
    ```

1.  Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

### Linux install {#linux}

We provide a pre-built binary for Linux.

1.  Download [Pulumi {{page.installer_version}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-linux-x64.tar.gz).

1.  Unzip the tarball and run the install script. After installation, you may delete the extracted folder. 

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-linux-x64.tar.gz
    $ ./pulumi/install.sh
    ```

1.  Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

## Verify the install

After installing Pulumi, verify the tool is on your path: 

```bash
$ pulumi version
v{{page.installer_version}}
```

## Uninstalling Pulumi

To uninstall Pulumi, delete the `.pulumi` folder in your home directory. If you used the manual installer, you should also delete the `pulumi` folder that was created.
