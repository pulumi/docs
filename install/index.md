---
title: "Installation and Setup"
installer_version: "0.12.2"
---

<!-- 
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above. 
- Update changelog.md with the latest fixes in the release
-->

The current Pulumi SDK version is <a href="./changelog.html#{{ page.installer_version }}">{{ page.installer_version }}</a>.  For older SDK versions, please see <a href="./changelog.html#all-versions">Previous SDK Versions</a>.

## Mac and Linux easy install

Run the following command to install the latest version of Pulumi:

```bash
curl -fsSL https://get.pulumi.com | sh
```

After running this command, Pulumi is installed, and you can move on to [Configure Pulumi for AWS](./aws.html).

To install Pulumi manually, follow the steps below for your platform.

## Pulumi SDK installation

<div class="card-table">
    <div class="mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title">
            <h2 class="mdl-card__title-text">
                <i class="material-icons">get_app</i>
                &nbsp;
                <a href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-darwin-x64.tar.gz">macOS x64</a>
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
                    href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-darwin-x64.tar.gz" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised">
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
                <a href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-linux-x64.tar.gz">Linux x64</a>
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
                    href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-linux-x64.tar.gz" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised">
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
                <a href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-windows-x64.zip">Windows x64</a>
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
                    href="https://get.pulumi.com/releases/sdk/pulumi-v{{page.installer_version}}-windows-x64.zip" role="button">
                <button class="mdl-button mdl-js-button mdl-button--raised">
                    {% octicon cloud-download height:24 %} DOWNLOAD
                </button>
            </a>
        </div>
    </div>
</div>

## Manual installation {#instructions}

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
