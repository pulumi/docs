---
title: "Installation and Setup"
installer_version: "0.11.0"
---

<!-- 
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above. 
- Update changelog.md with the latest fixes in the release
-->

## Pulumi SDK 

The current version is **{{ page.installer_version }}**.

<table class="card-table" width="100%">
    <tr>
        <td align="center" valign="center" width="33%">
            <div class="mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title">
                    <h2 class="mdl-card__title-text">
                        <i class="material-icons">get_app</i>
                        &nbsp;
                        <a href="/install">macOS x64</a>
                    </h2>
                </div>
                <div class="mdl-card__supporting-text">
                    macOS Sierra 10.12 or later is required.
                    See <a href="#mac">below</a> for detailed installation instructions.
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
        </td>
        <td align="center" valign="center" width="33%">
            <div class="mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title">
                    <h2 class="mdl-card__title-text">
                        <i class="material-icons">get_app</i>
                        &nbsp;
                        <a href="/install">Linux x64</a>
                    </h2>
                </div>
                <div class="mdl-card__supporting-text">
                    Ubuntu Trusty 14.04 LTS builds available.
                    See <a href="#linux">below</a> for detailed installation instructions.
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
        </td>
        <td align="center" valign="center" width="33%">
            <div class="mdl-card mdl-shadow--2dp">
                <div class="mdl-card__title">
                    <h2 class="mdl-card__title-text">
                        <i class="material-icons">get_app</i>
                        &nbsp;
                        <a href="/install">Windows x64</a>
                    </h2>
                </div>
                <div class="mdl-card__supporting-text">
                    Windows 8 or 10 are required.
                    See <a href="#windows">below</a> for detailed installation instructions.
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
        </td>
    </tr>
</table>

For older SDK versions, please see <a href="./changelog.html#all-versions">Previous SDK Versions</a>.

## Installation instructions

- [macOS](#mac)
- [Windows](#windows)
- [Linux](#linux)

### macOS install {#mac}

macOS Sierra (10.12) or later is required. 

1.  Install [Node.js 6.10.2 (LTS)](https://nodejs.org/dist/v6.10.2/node-v6.10.2.pkg). This exact version is required, to match the version supported by AWS Lambda and other public cloud implementations. You can use [Node Version Manager (nvm)](https://github.com/creationix/nvm) to manage multiple Node versions.

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

1.  Install [Node.js 6.10.2 (LTS)](https://nodejs.org/dist/v6.10.2/node-v6.10.2-x64.msi). This exact version is required, to match the version supported by AWS Lambda and other public cloud implementations. You can use [Node Version Manager (nvm)](https://github.com/creationix/nvm) to manage multiple Node versions.

2.  Download [Pulumi {{page.installer_version}} for Windows x64](/releases/pulumi-v{{page.installer_version}}-windows.x64.zip).

3.  Extract the zipfile to `%SystemRoot%\Program Files` or another directory and run `install.cmd` from either the command prompt or PowerShell.

4. Add `%SystemRoot%\Program Files\Pulumi` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

### Linux install {#linux}

We provide a pre-built binary for Ubuntu Trusty 14.04 LTS.

1.  Install [Node.js 6.10.2 (LTS)](https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.gz). This exact version is required, to match the version supported by AWS Lambda and other public cloud implementations. You can use [Node Version Manager (nvm)](https://github.com/creationix/nvm) to manage multiple Node versions.

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
