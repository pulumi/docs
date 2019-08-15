---
title: "Download and Install"
no_on_this_page: true
---

<!--
NOTE: To update this page with a new binary release, do the following:
- Update `static/latest-version`
- Update `content/reference/changelog.md`
-->

This page contains detailed instructions for [installing Pulumi](#install-pulumi) on your machine.

{{< get-started-note >}}

## Install Pulumi

<script>
    var oses = [ "unknown", "linux", "macos", "windows" ];

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
</select>

<div id="unknown_installation">
    <p>Please select your operating system.</p>
</div>

<div id="macos_installation" class="mt-8">
{{% md %}}


### Homebrew

macOS Sierra (10.12) or later is required.

You can install Pulumi through the [Homebrew package manager](https://brew.sh/):

```bash
$ brew install pulumi
```

This will install the `pulumi` CLI to the usual place (often `/usr/local/bin/pulumi`) and add it to your path.

Subsequent updates can be installed in the usual way:

```bash
$ brew upgrade pulumi
```

### Installation Script

Alternatively, you can run our installation script.

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.
See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.


The installer script can be rerun to subsequently install new updates.

### Manual Installation

If you do not wish to use the previous options, you can install Pulumi manually.

1. Download [Pulumi {{< latest-version >}} for macOS](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-darwin-x64.tar.gz). For prior versions and release notes, see the [Changelog]({{< relref "/docs/reference/changelog" >}}) page.

2. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

{{% /md %}}
</div>

<div id="linux_installation" class="mt-8">
{{% md %}}

### Installation Script

To install, run our installation script:

```bash
$ curl -fsSL https://get.pulumi.com | sh
```

This will install the `pulumi` CLI to `~/.pulumi/bin` and add it to your path. When it can't automatically add `pulumi` to your path, you will be prompted to add it manually.
See [How to permanently set $PATH on Unix](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix) for guidance.


### Manual Installation

Alternatively, you can install Pulumi manually. We provide a prebuilt binary for Linux.

1. Download [Pulumi {{< latest-version >}} for Linux x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-linux-x64.tar.gz). For prior versions and release notes, see the [Changelog]({{< relref "/docs/reference/changelog" >}}) page.

2. Extract the tarball and move the binaries in the `pulumi` directory to a directory included in your system's `$PATH`.

{{% /md %}}
</div>

<div id="windows_installation" class="mt-8">
{{% md %}}

### Installation Script

Windows 8 and 10 are supported.

To install, run our installation script from a `cmd.exe` window:

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

This will install the `pulumi.exe` CLI to `%USERPROFILE%\.pulumi\bin` and add it to your path.

### Manual Installation

Alternatively, you can install Pulumi manually.

1. Download [Pulumi {{< latest-version >}} for Windows x64](https://get.pulumi.com/releases/sdk/pulumi-v{{< latest-version >}}-windows-x64.zip). For prior versions and release notes, see the [Changelog]({{< relref "/docs/reference/changelog" >}}) page.

2. Unzip the file and extract the contents to a folder such as `C:\pulumi`.

3. Add `C:\pulumi\bin` to your path via **System Properties** -> **Advanced** -> **Environment Variables** -> **User Variables** -> **Path** -> **Edit**.
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

<div id="installation_post" class="mt-8">
{{% md %}}
## Verify your Installation

After installing Pulumi, verify everything is in working order by running the `pulumi` CLI:

```bash
$ pulumi version
v{{< latest-version >}}
```

### Pulumi Not Found Error

If you get an error that `pulumi` could not be found, it means your path has not been configured correctly. Verify that your system's `$PATH` contains the directory containing the `pulumi` CLI installed earlier.

### New Version Warning

If a new version of Pulumi is available, the CLI produces the following example warning when running any of the available commands:

```
warning: A new version of Pulumi is available. To upgrade from version '0.17.26' to '{{< latest-version >}}', run
   $ curl -sSL https://get.pulumi.com | sh

or visit https://pulumi.com/docs/reference/install/ for manual instructions and release notes.
```

<div class="note note-warning" role="alert">
    <p>
        <span>Skip version check.</span> If you're in an environment with no internet access, you may skip the Pulumi version update check by setting the environment variable <code>PULUMI_SKIP_UPDATE_CHECK</code> to <code>1</code> or <code>true</code>.
    </p>
</div>


## Uninstall Pulumi

To uninstall Pulumi, remove the `.pulumi` folder from your home directory. If you installed Pulumi manually, you should
also remove the `pulumi` folder that was created.
{{% /md %}}
</div>
