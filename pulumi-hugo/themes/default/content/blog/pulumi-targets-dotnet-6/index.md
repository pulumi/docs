---
title: "Improved Pulumi experience with .NET 6"
authors: ["zaid-ajaj"]
tags: ["dotnet", "csharp", "fsharp", "vb.net"]
meta_desc: "Pulumi projects default to .NET 6 with simplified program structure and leaner generated C# code"
meta_image: thumbnail.png
date: "2022-07-22"
---

In this blog post, we will talk about how Pulumi is now using [.NET 6](https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-6), the latest Long-Term Support version of .NET, as our default across the ecosystem. We will discuss the changes applied to templates, program structure and code generation. We also explain how Pulumi C# projects can benefit from the latest features in .NET 6 and how it simplifies your programs overall. Let's dive in, shall we?

<!--more-->

### Templates

We updated all of our .NET templates to use `net6.0` as the target framework. This means that projects created with `pulumi new` require at least the [.NET 6 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) to build and run the projects. The templates also simplified the program structure quite a bit and not longer use `MyStack` classes to define resources in case of C# and VB.NET templates. F# templates didn't change that much because these already didn't use the class approach to define infrastructure.

### Simplified program structure

Let us examine a new C# template. Create a new project using `pulumi new aws-csharp` in a new directory and notice that there is no longer a `MyStack.cs` file, only `Program.cs`. Open the latter in an editor and you should see the following:

```cs
using Pulumi;
using Pulumi.Aws.S3;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
   // Create an AWS resource (S3 Bucket)
   var bucket = new Bucket("my-bucket");

   // Export the name of the bucket
   return new Dictionary<string, object?>
   {
      ["bucketName"] = bucket.Id
   };
});
```

This is how a stack with resource definitions and outputs now looks. The [Get Started guide](https://www.pulumi.com/docs/get-started/) has been updated to follow this pattern as well.

Targeting .NET 6 means that we can use features from C# 10 and here we see them in action: using [top-level statements](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/tutorials/top-level-statements) that greatly simplify the entry point of the project and reduce it down to a single function call to `Deployment.RunAsync`. Inside this function is where we define our resources and return outputs for the stack. Top-level statements also allow us to `await` asynchronous functions without having an explicit `Main(string[] args)` function or a `Program` class.

Notice how you no longer have to define the types of your stack outputs upfront. Instead, you simply return a dictionary of key-valued outputs. In fact, the function `Deployment.RunAsync` is very flexible. When you don't want to return outputs, don't!

```cs
return await Deployment.RunAsync(() =>
{
   var bucket = new Bucket("my-bucket");
});
```

Moreover, when you want to `await` asynchronous functions alongside your resource definitions, just mark the lambda as `async`. Here is an example where we await function invokes and work with their results.

```cs
using Pulumi;
using Pulumi.Aws;
using Pulumi.Aws.Ec2;
using System.Linq;

return await Deployment.RunAsync(async() =>
{
    var vpc = await GetVpc.InvokeAsync(new()
    {
        Default = true  
    });

    var zones = await GetAvailabilityZones.InvokeAsync();

    foreach (var range in zones.Names.Select((zone, index) => new { Value = zone, Key = index }))
    {
        var subent = new Subnet($"vpcSubnet-{range.Key}", new()
        {
            AssignIpv6AddressOnCreation = false,
            VpcId = vpc.Id,
            MapPublicIpOnLaunch = true,
            CidrBlock = $"10.100.{range.Key}.0/24",
            AvailabilityZone = range.Value,
            Tags =
            {
               ["Name"] = $"pulumi-sn-{range.Value}",
            },
        });
    }
});
```

The cherry on top is that you can use [target-typed `new` expressions](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-9.0/target-typed-new) when instantiating resource or function invoke argument types. Basically instead of writing `new Bucket("my-bucket", new BucketArgs { ... })`, you can write `new Bucket("my-bucket", new () { ... })`.

### Backward-compatibility

It is worth mentioning that although the new templates and the accompanying getting-started guides are updating to .NET 6, the main `Pulumi` SDK NuGet package and cloud provider packages are still targeting `netcoreapp3.1`. This mean that if users are still using .NET SDK v3.1 or v5.0 to build and run your projects, everything will continue to work as always.

### Code generation

Pulumi provides tools to translate from several IaC languages. These tools will generate Pulumi programs in any of our supported languages. This includes:

- Translating [Pulumi YAML](https://www.pulumi.com/docs/languages-sdks/yaml/) with the Pulumi CLI using `pulumi convert`
- Translating [Azure Resource Manager (ARM)](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/overview) templates using [arm2pulumi](https://www.pulumi.com/arm2pulumi/)
- Translating Terraform code using [tf2pulumi](https://www.pulumi.com/tf2pulumi/)
- Translating Kubernetes YAML using [kube2pulumi](https://www.pulumi.com/kube2pulumi/)

These tools take their source language as input, convert it into the Pulumi intermediate language, then translate it into one of our supported languages. In the case of C#, the code generation has been updated to produce code that uses the latest features from .NET 6. We've also fixed minor issues that were present in the translation logic.

> The code generation update has landed in the Pulumi CLI and `pulumi convert`, the other tools however will pick up these updates soon.

Let us take an example from Pulumi YAML and convert it to C#.

Generate a new Pulumi YAML project using `pulumi new azure-yaml`, it should give you this YAML program:

```yaml
name: azure-yaml
runtime: yaml
description: A minimal Azure Native Pulumi YAML program

resources:
  # Create an Azure Resource Group
  resourceGroup:
    type: azure-native:resources:ResourceGroup
  # Create an Azure resource (Storage Account)
  storageAccount:
    type: azure-native:storage:StorageAccount
    properties:
      resourceGroupName: ${resourceGroup.name}
      sku:
        name: Standard_LRS
      kind: StorageV2

variables:
  storageAccountKeys:
    Fn::Invoke:
      Function: azure-native:storage:listStorageAccountKeys
      Arguments:
        resourceGroupName: ${resourceGroup.name}
        accountName: ${storageAccount.name}

outputs:
  # Export the primary key of the Storage Account
  primaryStorageKey: ${storageAccountKeys.keys[0].value}
```

Now you can take this program and convert it to C# using

```
pulumi convert --language csharp --out csharp-from-yaml
```

This command generates a full C# project from the YAML program into the directory `./csharp-from-yaml`, then restores the dependencies and builds the project. Now if you examine `Program.cs`, it contains the converted program and follows the succinct C# 10 syntax that targets .NET 6:

```csharp
using System.Collections.Generic;
using Pulumi;
using AzureNative = Pulumi.AzureNative;

return await Deployment.RunAsync(() =>
{
    var resourceGroup = new AzureNative.Resources.ResourceGroup("resourceGroup");

    var storageAccount = new AzureNative.Storage.StorageAccount("storageAccount", new()
    {
        ResourceGroupName = resourceGroup.Name,
        Sku = new AzureNative.Storage.Inputs.SkuArgs
        {
            Name = "Standard_LRS",
        },
        Kind = "StorageV2",
    });

    var storageAccountKeys = AzureNative.Storage.ListStorageAccountKeys.Invoke(new()
    {
        ResourceGroupName = resourceGroup.Name,
        AccountName = storageAccount.Name,
    });

    return new Dictionary<string, object?>
    {
        ["primaryStorageKey"] = storageAccountKeys.Apply(listStorageAccountKeysResult => listStorageAccountKeysResult.Keys[0]?.Value),
    };
});
```

## Summary

.NET 6 is the latest Long-Term Support version in the Microsoft ecosystem. Our new .NET 6 support makes for simpler and easier to write Pulumi programs. You can give it a try by [installing .NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) and using one of the templates with `pulumi new`, then follow our updated [Get Started guide](https://www.pulumi.com/docs/get-started/) to get up and running quickly. Our code generation tools have been upgraded to emit code that targets the latest features of C# and fixes minor correctness issues in the translation logic.
