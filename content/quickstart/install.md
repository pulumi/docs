---
title: "Download and Install"
installer_version: "0.17.16"
aliases:
    - install.html
    - /install/
menu:
  quickstart:
    weight: 2
---

<!--
NOTE: To update this page with a new binary release, do the following:
- Update `installer_version` in the YAML front matter above.
- Update changelog.md with the latest fixes in the release
-->

First things first, let's install the Pulumi CLI on your machine.

<script>
    var oses = [ "unknown", "linux", "macos", "windows", "other" ];

    function showInstall(os) {
        // Show the div and select it in the dropdown.
        var e = document.getElementById(os + "_installation");
        if (e) {
            e.style.display = "block";
            var s = document.getElementById("os");
            if (s) {
                for (var i = 0; i < s.options.length; i++) {
                    if (s.options[i].value === os) {
                        s.selectedIndex = i;
                        break;
                     }
                }
            }

            // If this is a real installation step, show the post-install markup too.
            var post = document.getElementById("installation_post");
            if (post) {
                post.style.display = os === oses[0] ? "none" : "block";
            }
        }
    }

    function hideInstall(os) {
        // Hide the installation div for this OS.
        var e = document.getElementById(os + "_installation");
        if (e) e.style.display = "none";
    }

    function selectOs(os) {
        // Select this OS by showing its div and selecting it in the dropdown.
        var found;
        for (var i = 0; i < oses.length; i++) {
            if (os === oses[i]) {
                showInstall(oses[i]);
                found = true;
            } else {
                hideInstall(oses[i]);
            }
        }
        if (!found) {
            showInstall(oses[0]);
        }
    }

    function selectCurrentOs(os) {
        var e = document.getElementById("os");
        if (e) {
            selectOs(e.value);
        }
    }
</script>

<label for="os">Operating system:</label>
<select id="os" onchange="selectCurrentOs()">
    <option value="unknown">(choose one)</option>
    <option value="linux">Linux</option>
    <option value="macos">macOS</option>
    <option value="windows">Windows</option>
    <option value="other">Manual Install</option>
</select>

<div id="unknown_installation">
    <p>Please select your operating system.</p>
</div>

<div id="macos_installation">
{{% md %}}
## macOS

You can install Pulumi through the [Homebrew package manager](https://brew.sh/):

```bash
$ brew install pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
```

### (Alternative) Installation script

Alternatively, our installation script can be run:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path.

The installer script can be rerun to subsequently install new updates.
{{% /md %}}
</div>

<div id="linux_installation">
{{% md %}}
## Linux

To install on Linux, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path.

If you prefer to download and manually install the tarball, please select "Manual Install" in the above dropdown.
{{% /md %}}
</div>

<div id="windows_installation">
{{% md %}}
## Windows

To install on Windows, run our installation script from a `cmd.exe` window:

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.
{{% /md %}}
</div>

<div id="other_installation">
{{% md %}}
## Manual Installation

Raw binaries are available for all major operating systems if you prefer to install them manually.

### macOS Binaries

macOS Sierra (10.12) or later is required.

1. Download [Pulumi {{< param installer_version >}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{< param installer_version >}}-darwin-x64.tar.gz).

2. Unzip the tarball and either copy the binaries in the `pulumi` directory on your `$PATH`.

### Linux Binaries

We provide a pre-built binary for Linux.

1. Download [Pulumi {{< param installer_version >}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< param installer_version >}}-linux-x64.tar.gz).

2. Unzip the tarball and either copy the binaries in the `pulumi` directory on your `$PATH`.

### Windows Binaries

Windows 8 and 10 are supported.

1. Download [Pulumi {{< param installer_version >}} for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< param installer_version >}}-windows-x64.zip).

2. Copy the extracted zipfile contents to a folder such as `C:\pulumi`.

3. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.

### Uninstalling Pulumi

To uninstall Pulumi, delete the `.pulumi` folder in your home directory. If you used the manual installer, you should
also delete the `pulumi` folder that was created.

The current stable version is **{{< param installer_version >}}**. For a full history of prior versions, including
release notes, please visit <a href="{{< relref "/reference/changelog.md" >}}">the Change Log</a>.

{{% /md %}}
</div>

<script>
    if (navigator.appVersion.indexOf("Win") !== -1) {
        selectOs("windows");
    } else if (navigator.appVersion.indexOf("Mac") !== -1) {
        selectOs("macos");
    } else if (navigator.appVersion.indexOf("Linux") !== -1) {
        selectOs("linux");
    } else {
        selectOs("unknown");
    }
</script>

<div id="installation_post">
{{% md %}}
## Ensuring It Worked
After installing, verify everything is in working order by running the `pulumi` CLI:

```bash
$ pulumi version
v{{< param installer_version >}}
```

If you get an error that `pulumi` could not be found, it means your path has not been configured correctly. Please go
back and ensure your path contains the directory containing the `pulumi` CLI installed earlier.

## Next Steps

After installation, choose a cloud to get started:

{{< quickstart-clouds >}}

{{% /md %}}
</div>
