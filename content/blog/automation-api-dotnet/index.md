---
title: "Automate Your Infrastructure with Automation API and C#"
date: 2021-03-08
meta_desc: "C# developers can programmatically build infrastructure (with out a CLI) using the Pulumi Automation API package. "
meta_image: automation_api.png
authors:
- joshua-studt
- sophia-parafina
tags:
- Automation API
- .NET
- guest-post
---

{{% notes type="info" %}}
Joshua Studt is a Solutions Architect at Financial Independence Group and a Pulumi Community member who contributed the C# package for Automation API.
{{% /notes %}}

Currently available in public preview, Pulumi's Automation API enables you to provision your infrastructure programmatically using the Pulumi engine. Today, we are excited to announce C# support for Automation API, enabling .NET developers to automate infrastructure deployments, create complex orchestration workflows, build custom ops tooling, and build cloud frameworks. Read more about the Automation API [here](/blog/automation-api/).

## Using Automation API in .NET

The `Pulumi.Automation` [NuGet package](https://www.nuget.org/packages/Pulumi.Automation) exposes a `LocalWorkspace` for  creating and managing Pulumi [Stacks](/docs/concepts/stack/), and a `WorkspaceStack` that is a programmatic representation of a Stack for updating, refreshing, previewing, and destroying cloud resources. The Automation API makes it trivial to run Pulumi programs inline:

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

You can use your existing Pulumi projects and invoke them from the Automation API:

```csharp
var stackArgs = new LocalProgramArgs("stackName", "C:\path\to\pulumi\project\dir");
using var stack = await LocalWorkspace.CreateOrSelectStackAsync(stackArgs);

await stack.UpAsync();
```

Since the Automation API can be invoked and debugged like any other code, it enables you to put together complex deployment workflows such as a blue-green deployment model:

```csharp
using var workspace = await LocalWorkspace.CreateAsync(new LocalWorkspaceOptions
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

See full Automation API examples in [C#](https://github.com/pulumi/automation-api-examples/tree/main/dotnet). Let us know if you're using Automation API on [Twitter](https://twitter.com/PulumiCorp) or in our [Community Slack](https://slack.pulumi.com/).
