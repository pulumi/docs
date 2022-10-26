---
title: Migrating to Pulumi 2.0
meta_desc: This page provides instructions for migrating to Pulumi 2.0
no_on_this_page: true
---

Upgrading to 2.0 is simple. First, you will [install the 2.0 CLI](/docs/get-started/install/). Then, update each of your Pulumi programs to utilize the new SDK. If you're using JavaScript or TypeScript, you'll also need to ensure you're using invokes asynchronously. We provide detailed instructions on each of these steps below.

## Update CLI Scripts

Previously, the Pulumi CLI would assume `--yes` when used in non-interactive mode (i.e. when `pulumi` had its output piped to another process). You will now need to explicitly pass in `--yes` in those scenarios. This affects:

* `pulumi destroy`
* `pulumi new`
* `pulumi refresh`
* `pulumi up`

## Update Your Pulumi Programs

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language "javascript,typescript" %}}

### Update Dependencies

```bash
npm install @pulumi/pulumi@^2.0.0
```

### Remove synchronous invokes

Due to [inconsistent support between versions of NodeJS](https://github.com/pulumi/pulumi/issues/4462#issuecomment-617367272), Pulumi 2.0 no longer supports synchronous invokes. As a result, the return value of all `getSomething` operations are now `Promise<Something>` values, instead of `Something` values, and should be processed using `.then`, `async/await` or by passing the results to `pulumi.output()`. Similarly, the `StackReference` operations `getOutputSync` and `requireOutputSync` are no longer supported and you should move to using the `Output`-based versions of `getOutput` and `requireOutput`.

```javascript
//Before:
const version: string = gcp.container.getEngineVersions().latestMasterVersion;

//After w/ Promise:
const version: Promise<string> = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);

//After w/ Output:
const version: Output<string> = pulumi.output(gcp.container.getEngineVersions()).latestMasterVersion;
```

Optionally, you can use an `async` function [entrypoint](/docs/intro/languages/javascript#entrypoint) to more easily write `async/await` code throughout the rest of your program.

{{% /choosable %}}

{{% choosable language python %}}

### Update Dependencies

Modify your `requirements.txt` file to update the Pulumi SDK and related providers as below:

```
pulumi>=2.0.0
pulumi-aws>=2.0.0
```

Then run `pip install`:

```bash
pip install -r requirements.txt
```

{{% /choosable %}}
{{% choosable language go %}}

### Update Dependencies

Pulumi 2.0 now supports Go modules. In `go.mod`, you can depend on the Pulumi SDK and related providers as below:

```
require (
    github.com/pulumi/pulumi/sdk/v2 v2.0.0
    github.com/pulumi/pulumi-aws/sdk/v2/go/aws v2.0.0
)
```

Then run `go mod download`

{{% /choosable %}}
{{% choosable language csharp %}}

### Update Dependencies

Update your package reference to the latest version of the SDK:

```csharp
<PackageReference Include="Pulumi" Version="2.*" />
```

### Update Invokes

Functions in the `Invokes` namespace are now obsolete. Instead, use `InvokeAsync` which hangs off a static class named for the method being invoked.

For example, the following:

```csharp
var clientConfig = await Pulumi.Azure.Core.Invokes.GetClientConfig();
```

becomes:

```csharp
var clientConfig = await Pulumi.Azure.Core.GetClientConfig.InvokeAsync();
```

{{% /choosable %}}

{{< /chooser >}}

## Remaining on Pulumi 1.0

We recommend switching to Pulumi 2.0 if possible. We will only push critical security and bug fixes into the `1.x` branch. Other fixes, feature enhancements, and
new functionality will not be supported in the `1.x` branch. In addition, provider updates will only be built against Pulumi 2.0.

If you wish to remain on the `1.x` CLI, you can continue to download the CLI by referring to [the manual installation instructions](/docs/get-started/install#manual-installation) and [choosing a specific version](/docs/get-started/install/versions/).

`pulumi new` will attempt to use the latest versions of the templates, which pull in the `2.0` SDK. You can continue to use the `1.x` templates by running `pulumi new https://github.com/pulumi/templates/tree/1.x`.

Note that previous `1.x` templates for Python had `>=1.0.0` in `requirements.txt`. As a result, you may accidentally end up on the `2.x` SDK when updating dependencies from the `1.x` template.  We encourage updating to `>=1.0.0,<2.0.0` if you intend to remain on the `1.x` releases.
