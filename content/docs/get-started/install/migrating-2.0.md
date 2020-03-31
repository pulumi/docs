---
title: Migrating to Pulumi 2.0
meta_desc: This page provides instructions for migrating to Pulumi 2.0
no_on_this_page: true
data:
  node_invokes_text: Pulumi 2.0 no longer supports synchronous invokes. As a result, using the return values of any resource `get` operations will need to be made asynchronous. Similarly, the use of `getOutputSync` and `requireOutputSync` are no longer supported and you should move to using the `Output`-based versions of `getOutput` and `requireOutput`.
---

## Migrating to 2.0

Upgrading to 2.0 is simple. First, you will download the 2.0 CLI, which is required to use the 2.0 SDK. Then, update each of your Pulumi programs to utilize the new SDK. If you're using Javascript or Typescript, you'll also need to ensure you're using invokes asynchronously. We provide detailed instructions on each of these steps below.

## Install Pulumi 2.0 CLI

If you are upgrading to a beta release, obtain the latest binaries from the [versions]({{< relref "versions" >}}) page. Then, follow the [manual installation]({{< relref "./#manual-installation" >}}) steps for your operating system.

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

{{< param "data.node_invokes_text" >}}

```javascript
const engineVersion = gcp.container.getEngineVersions().latestMasterVersion;
```

becomes

```javascript
const engineVersion = gcp.container.getEngineVersions().then(v => v.latestMasterVersion);
```

{{% /choosable %}}

{{% choosable language python %}}

### Update Dependencies

Modify your `requirements.txt` file:

```
pulumi>=2.0.0
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
	github.com/pulumi/pulumi/sdk/v2 v2.0.0-beta.1
    github.com/pulumi/pulumi-aws/sdk/v2/go/aws v2.0.0-beta.1
)
```

Then run `go mod download`

{{% /choosable %}}
{{% choosable language csharp %}}

### Update Dependencies

Update your package reference to the latest version of the SDK:

```csharp
<PackageReference Include="Pulumi" Version="2.0.0-beta.1" />
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
