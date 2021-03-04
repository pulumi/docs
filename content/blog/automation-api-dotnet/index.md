---
title: "Automate Your Infrastructure with Automation API and C#"
date: tbd
meta_desc: "tbd"
meta_image: automation_api.png
authors:
- joshua-studt
tags:
- Automation API
- C#
- csharp
- dotnet
- .NET
---

Currently available in public preview, Pulumi's Automation API enables you to programmatically call upon the Pulumi engine to provision your infrastructure. Today, we are excited to announce C# support for the API, so .NET developers can do just that. Read more about the Automation API [here.]({{< relref "/blog/automation-api" >}})

## Using Automation API in .NET

The `Pulumi.Automation` [NuGet package](https://github.com/pulumi/pulumi/tree/master/sdk/dotnet/Pulumi.Automation) exposes a `LocalWorkspace` that empowers you to create and manage [Stacks]({{< relref "/docs/intro/concepts/stack" >}}), as well as a `WorkspaceStack` that is your programmatic representation of a Stack use to perform infrastructure updates, refresh, previews, and destroy. The Automation API makes it trivial to run Pulumi programs inline:

```csharp
var program = PulumiFn.Create(() =>
{
    var bucket = new Pulumi.Aws.S3.Bucket("s3-website-bucket");

    return new Dictionary<string, object?>
    {
        ["bucket_name"] = bucket.BucketName,
    };
});

var stackArgs = new InlineProgramArgs("projectName", "stackName", program);
using var stack = await LocalWorkspace.CreateOrSelectStackAsync(stackArgs);

await stack.Workspace.InstallPluginAsync("aws", "v3.30.1");
var result = await stack.UpAsync();
var bucketName = result.Outputs["bucket_name"];
```

You can also continue to use your existing Pulumi projects, and invoke them from the Automation API:

```csharp
var stackArgs = new LocalProgramArgs("stackName", "C:\path\to\pulumi\project\dir");
using var stack = await LocalWorkspace.CreateOrSelectStackAsync(stackArgs);

await stack.UpAsync();
```

And since the Automation API can be invoked and debugged just like any other code that you write, it enables you put together complex deployment workflows such as a blue-green deployment model.

```csharp
var workspace = await LocalWorkspace.CreateAsync(new LocalWorkspaceOptions
{
    Program = PulumiFn.Create<ApplicationStack>(), // use your existing Pulumi.Stack implementation
    ProjectSettings = new ProjectSettings("projectName", ProjectRuntimeName.Dotnet),
});

// your "blue" production code is already running

var green = await WorkspaceStack.SelectAsync("green", workspace);
await green.UpAsync();

// do your cutover to "green" logic
// and then teardown "blue"

var blue = await WorkspaceStack.SelectAsync("blue", workspace);
await blue.DestroyAsync();
```

See the full Automation API examples in [C#](https://github.com/pulumi/automation-api-examples/tree/main/dotnet).