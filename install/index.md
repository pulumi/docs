---
title: "Installation and Setup"
installer_version: "0.12.1"
---

<!-- 
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above. 
- Update changelog.md with the latest fixes in the release
-->

## Mac and Linux easy install

Run the following command to install the latest version of Pulumi.

```bash
curl -fsSL https://get.pulumi.com | sh
```

After running this command, Pulumi is installed, and you can skip the rest of these instructions.  If you would like to install Pulumi manually, please follow the steps below for your platform.

## Pulumi SDK 

The current SDK version is <a href="./changelog.html#{{ page.installer_version }}">{{ page.installer_version }}</a>.

<div class="card-table">
    <div class="mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title">
            <h2 class="mdl-card__title-text">
                <i class="material-icons">get_app</i>
                &nbsp;
                <a href="/releases/pulumi-v{{page.installer_version}}-darwin.x64.tar.gz">macOS x64</a>
            </h2>
        </div>
        <div class="mdl-card__supporting-text">
            <span class="card-text">
                macOS Sierra 10.12 or later is required.
                More information is <a href="#mac">below</a>.
            </span>
        </div>
        <div class="mdl-card__actions mdl-card--border">
            <a
                    id="macos-download-link"
                    href="/releases/pulumi-v{{page.installer_version}}-darwin.x64.tar.gz" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                    {% octicon cloud-download height:24 %} DOWNLOAD
                </button>
            </a>
        </div>
    </div>
    <div class="mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title">
            <h2 class="mdl-card__title-text">
                <i class="material-icons">get_app</i>
                &nbsp;
                <a href="/releases/pulumi-v{{page.installer_version}}-linux.x64.tar.gz">Linux x64</a>
            </h2>
        </div>
        <div class="mdl-card__supporting-text">
            <span class="card-text">
                More information is <a href="#linux">below</a>.
            </span>
        </div>
        <div class="mdl-card__actions mdl-card--border">
            <a
                    id="linux-download-link"
                    href="/releases/pulumi-v{{page.installer_version}}-linux.x64.tar.gz" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                    {% octicon cloud-download height:24 %} DOWNLOAD
                </button>
            </a>
        </div>
    </div>
    <div class="mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title">
            <h2 class="mdl-card__title-text">
                <i class="material-icons">get_app</i>
                &nbsp;
                <a href="/releases/pulumi-v{{page.installer_version}}-windows.x64.zip">Windows x64</a>
            </h2>
        </div>
        <div class="mdl-card__supporting-text">
            <span class="card-text">
                Windows 8 or 10 are supported.
                More information is <a href="#windows">below</a>.
            </span>
        </div>
        <div class="mdl-card__actions mdl-card--border">
            <a
                    id="windows-download-link"
                    href="/releases/pulumi-v{{page.installer_version}}-windows.x64.zip" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
                    {% octicon cloud-download height:24 %} DOWNLOAD
                </button>
            </a>
        </div>
    </div>
</div>

For older SDK versions, please see <a href="./changelog.html#all-versions">Previous SDK Versions</a>.

## Installation instructions {#instructions}

- [macOS](#mac)
- [Windows](#windows)
- [Linux](#linux)

### macOS install {#mac}

macOS Sierra (10.12) or later is required. 

2.  Download [Pulumi {{page.installer_version}} for macOS](/releases/pulumi-v{{page.installer_version}}-darwin.x64.tar.gz).

3.  Unzip the tarball and run the install script. After installation, you may delete the extracted folder. 

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-darwin.x64.tar.gz
    $ ./pulumi/install.sh 
    ```

4.  Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

### Windows install {#windows}

Windows 8 and 10 are supported.

<!-- 
The below known issue is tracked by https://github.com/pulumi/home/issues/156. Not linked in the doc, since "home" will not be OSS in its current form.
-->

> **Note:** Due to a known issue, the SDK must be installed in a path that has no spaces. For instance, the path `C:\Program Files` will not work correctly. 

2.  Download [Pulumi {{page.installer_version}} for Windows x64](/releases/pulumi-v{{page.installer_version}}-windows.x64.zip).

3.  Copy the extracted zipfile contents to a folder such as `C:\pulumi`.

4. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

### Linux install {#linux}

We provide a pre-built binary for Linux.

2.  Download [Pulumi {{page.installer_version}} for Linux x64](/releases/pulumi-v{{page.installer_version}}-linux.x64.tar.gz).

3.  Unzip the tarball and run the install script. After installation, you may delete the extracted folder. 

    ```bash
    $ tar -xzf pulumi-v{{page.installer_version}}-linux.x64.tar.gz
    $ ./pulumi/install.sh
    ```

4.  Add `/usr/local/pulumi/bin` to your path:

    ```
    echo "export PATH=\$PATH:/usr/local/pulumi/bin" >> ~/.profile
    ```

## Verify the install

After installing Pulumi, verify the tool is on your path: 

```bash
$ pulumi version
v{{page.installer_version}}
```

## Configure provider credentials

Configure the credentials for your cloud provider of choice:
-   [Configure Pulumi for AWS](./aws-config.html)
-   Configure Pulumi for Azure
-   Configure Pulumi for Kubernetes

## Configure NPM client

If you're using Pulumi with JavaScript or TypeScript, follow the instructions in [Configure your NPM client](./configure-npm.html).
