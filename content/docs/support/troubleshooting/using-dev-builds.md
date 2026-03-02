---
title_tag: "Using Dev Builds for Unreleased Fixes"
meta_desc: "Learn how to install and use Pulumi dev builds to access bug fixes and features that have been merged but not yet released."
title: Using Dev Builds for Unreleased Fixes
h1: Using Dev Builds for Unreleased Fixes
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        parent: support-troubleshooting
        weight: 70
---

If you've reported a bug or requested a feature and the fix has been merged to the main branch of a Pulumi repository, you may want to use it before the next official release. Pulumi publishes dev builds automatically on every merge to the main branch, allowing you to access the latest changes immediately.

## When to use dev builds

Dev builds are useful when:

- A bug fix has been merged to main but hasn't been included in an official release yet
- You want to verify that a fix resolves your issue before the next release
- You need to test your infrastructure against the latest Pulumi changes
- A GitHub issue you've reported shows a merged PR, but the milestone indicates it hasn't been released

{{% notes type="warning" %}}
Dev builds contain the latest changes from the main branch and may not have undergone the same level of testing as official releases. While dev builds are suitable for development and testing environments, exercise caution if using them in production.
{{% /notes %}}

## Checking if a fix is available

When a GitHub issue is closed with a merged pull request:

1. Check the issue's milestone - if it shows a future version number or "needs-release" label, the fix is merged but not yet released
1. Look at the pull request to confirm it was merged to the main branch
1. Note when the PR was merged - dev builds are published within minutes of merging

## Installing dev builds

### Pulumi CLI

To install the latest dev build of the Pulumi CLI:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

```bash
curl -fsSL https://get.pulumi.com | sh -s -- --version dev
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com | sh -s -- --version dev
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; & ([ScriptBlock]::Create((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))) -Version dev" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
```

{{% /choosable %}}

{{% /chooser %}}

For more installation options, see the [download and install documentation](/docs/get-started/download-install/#installing-dev-releases).

### Language SDKs

If the fix is in a language SDK rather than the CLI, install the dev version of the SDK for your language:

- [TypeScript (Node.js)](/docs/iac/languages-sdks/javascript/#dev-versions)
- [Python](/docs/iac/languages-sdks/python/#dev-versions)
- [Go](/docs/iac/languages-sdks/go/#dev-versions)
- [.NET](/docs/iac/languages-sdks/dotnet/#dev-versions)
- **Java**: Dev versions are not currently published. You can build from source by cloning the [pulumi/pulumi-java](https://github.com/pulumi/pulumi-java) repository.
- **YAML**: YAML programs use the Pulumi CLI directly — no separate SDK installation is needed.

## Verifying the fix

After installing the dev build:

1. Run `pulumi version` to confirm you're using a dev version (it will show an alpha version number like `3.225.0-alpha.x3831727`)
1. Test your Pulumi program to verify the fix resolves your issue
1. If the issue persists, add a comment to the GitHub issue with details about your testing

## Returning to stable releases

Once an official release containing your fix is published:

1. Uninstall the dev build
1. Install the latest stable version using the standard [installation instructions](/docs/get-started/download-install/)
1. For SDKs, update your dependencies to the latest stable version

## Related resources

- [Download and install Pulumi](/docs/get-started/download-install/)
- [Pulumi CLI versions](/docs/get-started/download-install/versions/)
- [Filing GitHub issues](/docs/support/filing-issues/)
