---
title: "Converting Bicep code to Pulumi"
date: 2023-09-29
draft: false
meta_desc: In this article, we will look at a new language converter that takes Bicep code and converts it to any of supported Pulumi languages. 
meta_image: meta.png
authors: ["zaid-ajaj"]
tags: ["community", "bicep", "pulumi", "convert"]
---

Bicep is a DSL developed by Microsoft to simplify the authoring of ARM templates and deploy resources to Azure. Today I will be sharing with you a new Pulumi converter plugin that I have been working on that converts Bicep code to any of the supported Pulumi languages.

<!--more-->

The [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep) language is a domain-specific language for Infrastructure-As-Code built by Microsoft that uses declarative syntax to deploy Azure resources. It was made to address the shortcomings of authoring ARM templates that are written in JSON. Compared to ARM templates, Bicep is much more concise and readable. However, here at Pulumi we believe that using general-purpose programming languages that are familiar to developers is the best way to author Infrastructure-As-Code. Besides being able to use a general-purpose language, you and your team can benefit from using Pulumi Cloud as you scale to larger projects and teams with features such as [Pulumi Deployments](https://www.pulumi.com/blog/pulumi-deployments/), [Organization Access Tokens](https://www.pulumi.com/blog/organization-access-tokens/), [Review Stacks](https://www.pulumi.com/blog/review-stacks/) and more.

That is why I have been working on a new [Pulumi converter plugin](https://github.com/Zaid-Ajaj/pulumi-converter-bicep) that converts Bicep code to any of the supported Pulumi languages using the Pulumi CLI via `pulumi convert`.

## Installing and using the plugin

First, install the _converter_ plugin using the Pulumi CLI:

```bash
pulumi plugin install converter bicep --server github://api.github.com/Zaid-Ajaj
```

This command will install the plugin from the latest GitHub release of the [repository](https://github.com/Zaid-Ajaj/pulumi-converter-bicep).

Once installed, you can use it to convert Bicep code to Pulumi. For example, let's say we have the following Bicep code in a file called `example.bicep` which deploys a storage account:

```bicep
resource storage 'Microsoft.Storage/storageAccounts@2022-09-01' = {
  name: 'storageaccount'
  location: resourceGroup().location
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
}
```

Navigate to the directory where the file is located and run the following command. For example to generate TypeScript code from the Bicep code above, run:

```bash
pulumi convert --from bicep --language typescript --out output -- --entry example.bicep
```

This command will use the Bicep converter plugin we just installed to convert the code in `example.bicep` to TypeScript and place the generated code in the `output` directory.

You can change `typescript` to any of the supported languages such as `csharp`, `python`, `go`, `java` or `yaml` and you are good to go.

If you don't specify the `--entry` flag, the plugin will look for the first file with the `.bicep` extension in the current directory.

Let us look at the generated code from the example above:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure_native from "@pulumi/azure-native";

const config = new pulumi.Config();
// The name of the resource group to operate on
const resourceGroupName = config.require("resourceGroupName");
const currentResourceGroup = azure_native.resources.getResourceGroupOutput({
    resourceGroupName: resourceGroupName,
});
const storage = new azure_native.storage.StorageAccount("storageaccount", {
    accountName: "storageaccount",
    kind: "StorageV2",
    location: currentResourceGroup.apply(currentResourceGroup => currentResourceGroup.location),
    resourceGroupName: currentResourceGroup.apply(currentResourceGroup => currentResourceGroup.name),
    sku: {
        name: "Standard_LRS",
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_azure_native as azure_native

config = pulumi.Config()
# The name of the resource group to operate on
resource_group_name = config.require("resourceGroupName")
current_resource_group = azure_native.resources.get_resource_group_output(resource_group_name=resource_group_name)
storage = azure_native.storage.StorageAccount("storageaccount",
    account_name="storageaccount",
    kind="StorageV2",
    location=current_resource_group.location,
    resource_group_name=current_resource_group.name,
    sku=azure_native.storage.SkuArgs(
        name="Standard_LRS",
    ))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-azure-native-sdk/v2/resources"
	"github.com/pulumi/pulumi-azure-native-sdk/v2/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		// The name of the resource group to operate on
		resourceGroupName := cfg.Require("resourceGroupName")
		currentResourceGroup, err := resources.LookupResourceGroup(ctx, &resources.LookupResourceGroupArgs{
			ResourceGroupName: resourceGroupName,
		}, nil)
		if err != nil {
			return err
		}
		_, err = storage.NewStorageAccount(ctx, "storageaccount", &storage.StorageAccountArgs{
			AccountName:       pulumi.String("storageaccount"),
			Kind:              pulumi.String("StorageV2"),
			Location:          *pulumi.String(currentResourceGroup.Location),
			ResourceGroupName: *pulumi.String(currentResourceGroup.Name),
			Sku: &storage.SkuArgs{
				Name: pulumi.String("Standard_LRS"),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using AzureNative = Pulumi.AzureNative;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    // The name of the resource group to operate on
    var resourceGroupName = config.Require("resourceGroupName");
    var currentResourceGroup = AzureNative.Resources.GetResourceGroup.Invoke(new()
    {
        ResourceGroupName = resourceGroupName,
    });

    var storage = new AzureNative.Storage.StorageAccount("storageaccount", new()
    {
        AccountName = "storageaccount",
        Kind = "StorageV2",
        Location = currentResourceGroup.Apply(getResourceGroupResult => getResourceGroupResult.Location),
        ResourceGroupName = currentResourceGroup.Apply(getResourceGroupResult => getResourceGroupResult.Name),
        Sku = new AzureNative.Storage.Inputs.SkuArgs
        {
            Name = "Standard_LRS",
        },
    });

});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.azurenative.resources.ResourcesFunctions;
import com.pulumi.azurenative.resources.inputs.GetResourceGroupArgs;
import com.pulumi.azurenative.storage.StorageAccount;
import com.pulumi.azurenative.storage.StorageAccountArgs;
import com.pulumi.azurenative.storage.inputs.SkuArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var config = ctx.config();
        final var resourceGroupName = config.get("resourceGroupName");
        final var currentResourceGroup = ResourcesFunctions.getResourceGroup(GetResourceGroupArgs.builder()
            .resourceGroupName(resourceGroupName)
            .build());

        var storage = new StorageAccount("storage", StorageAccountArgs.builder()
            .accountName("storageaccount")
            .kind("StorageV2")
            .location(currentResourceGroup.applyValue(getResourceGroupResult -> getResourceGroupResult.location()))
            .resourceGroupName(currentResourceGroup.applyValue(getResourceGroupResult -> getResourceGroupResult.name()))
            .sku(SkuArgs.builder()
                .name("Standard_LRS")
                .build())
            .build());

    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
configuration:
  resourceGroupName:
    type: string
resources:
  storageaccount:
    type: azure-native:storage:StorageAccount
    properties:
      accountName: storageaccount
      kind: StorageV2
      location: ${currentResourceGroup.location}
      resourceGroupName: ${currentResourceGroup.name}
      sku:
        name: Standard_LRS
variables:
  currentResourceGroup:
    fn::invoke:
      Function: azure-native:resources:getResourceGroup
      Arguments:
        resourceGroupName: ${resourceGroupName}
```

{{% /choosable %}}
{{< /chooser >}}

Notice how the in the original Bicep code, we reference the location of the _implicit_ resource group via `resourceGroup().location`. When the converter generates code for the target language, it replaces this _implicit_ resource group with an explicit one by parameterizing the program by a resource group name and using that resource group when deploying the resources.

## Early days for the converter

Currently the converter supports most of the features of Bicep such as parameters, variables, modules, resources, outputs and a number of built-in functions. That said, the converter plugin is still in its early days and it's not yet tested against many real-world Bicep programs. I am actively working on improving it and making it support most of the Bicep language features. The source code is available on this [GitHub repository](https://github.com/Zaid-Ajaj/pulumi-converter-bicep). If you find any issues or have any feedback, please open an issue on the repository.

## How does it work?

The converter plugin is a native binary built using .NET in [F#](https://dotnet.microsoft.com/en-us/languages/fsharp) and new Pulumi Converter SDK. Using the core [Pulumi](https://www.nuget.org/packages/Pulumi) nuget package, we shipped an experimental API that allows you to easily build converter plugins that can extend the functionality of `pulumi convert`.

Building a language converter plugin involves taking the source language, in this case Bicep, and converting it to the our internal Pulumi Configuration Language or PCL for short. The converter implements a function of the following shape:

```fsharp
let convertProgram (request: ConvertProgramRequest): ConvertProgramResponse =
    let sourceDirectory = request.SourceDirectory
    let targetDirectory = request.TargetDirectory
    let args = request.Args
    // conversion logic here
```

In our case, we read the Bicep code from the source directory, convert it to PCL and write out the PCL code in the target directory. Then, Pulumi uses the built-in program generation facilities to take care of the rest of the work of generating the target language code from the PCL code so that we don't have to worry about language-specific details. The converter only needs to know how to generate PCL.

To build the actual transformation from Bicep to PCL, I made use the of the [Azure.Bicep.Core](https://www.nuget.org/packages/Azure.Bicep.Core) package available for .NET which allowed me to parse the Bicep code and generate a typed Abstract Syntax Tree (AST) from it. Building an AST from the source language allows us to easily traverse the tree, analyze it and symbolically rewrite pieces of it. Working at the AST level alse makes it easy to test source code transformation using structure rather than text. Once we have obtained the Bicep AST, we transform it into a Pulumi AST that represents a PCL program. Finally we print out the Pulumi AST to a string and write it to the target directory.

If you are curious about the specification of the AST that represents Bicep programs, head over to [this file](https://github.com/Zaid-Ajaj/pulumi-converter-bicep/blob/master/src/Converter/BicepParser.fs) from the source code. You will find types such as `BicepProgram` and `BicepSyntax` that model almost every aspect of Bicep code. As for the AST of PCL programs, you can find the type definitions [here](https://github.com/Zaid-Ajaj/pulumi-converter-bicep/blob/master/src/Converter/PulumiTypes.fs).

The F# language is great for almost everything but is especially amazing for writing language converters because of its powerful pattern matching capabilities, and the ability to write code in a functional style. Many of us working at Pulumi are big fans of F#!

Here is a snippet of the transformation pipeline written in F# that takes the input Bicep program and converts it to the final PCL text

```fsharp
bicepProgram
|> BicepProgram.dropResourceUnknowns
|> BicepProgram.reduceScopeParameter
|> BicepProgram.parameterizeByTenantAndSubscriptionId
|> BicepProgram.addResourceGroupNameParameterToModules
|> BicepProgram.parameterizeByResourceGroup
|> Transform.bicepProgramToPulumi
|> Transform.modifyComponentPaths rewriteComponentPath
|> Printer.printProgram
```

You can learn more on the implementation of these functions from the source code on GitHub. I've written it in a way that is easy to follow, understand and contribute to. Most of these functions are fully [unit-tested](https://github.com/Zaid-Ajaj/pulumi-converter-bicep/blob/master/src/Tests/Program.fs) and I am working on adding more tests to cover more of the Bicep language features.

## Bonus converter: ARM to Pulumi

Those who are familiar with the Bicep CLI, know that it has a built-in _decompiler_ that converts ARM templates to Bicep. I thought it would be fun to build another converter that takes ARM templates to Pulumi but without writing any conversion logic for it. Instead, I would decompile the ARM template to Bicep, then use the logic from the Bicep converter to generate the final PCL code. Fortunately, the decompiler code is embedded in the nuget package [Azure.Bicep.Core](https://www.nuget.org/packages/Azure.Bicep.Core) so we don't have to rely on the existence of the Bicep CLI in order to make this converter work.

From all of this, I created another converter `pulumi-converter-arm` that works exactly like the Bicep converter but takes ARM templates as input. Head over to the [repository](https://github.com/Zaid-Ajaj/pulumi-converter-arm) to learn more about how to install it and how to use it.

Depending on how well this ARM converter does its job, we might consider deprecating [arm2pulumi](https://www.pulumi.com/arm2pulumi/) in favor of it. However we first need to test it against more templates and iron out the rough edges. It would be the ideal situation because there are virtually zero maintenance costs, any improvements to the Bicep converter would automatically get picked up here. Also improvements to the decompiler from the [Azure.Bicep.Core](https://www.nuget.org/packages/Azure.Bicep.Core) nuget package would benefit the converter as well.

## Building your own Pulumi language converter

Converter plugins are a great way to extend the Pulumi CLI with `pulumi convert` to support new languages. When we shipped support for [Converting full Terraform Programs To Pulumi](https://www.pulumi.com/blog/converting-full-terraform-programs-to-pulumi/), we extended the `pulumi convert` command to allow installing and using converter plugins that are shipped independently from the Pulumi CLI.

In essense, those plugins are executable binaries that can be written in any language which serves up a gRPC server that implements the `Converter` contract:

```protobuf
// Converter is a service for converting between other ecosystems and Pulumi.
// This is currently unstable and experimental.
service Converter {
    // ConvertState converts state from the target ecosystem into a form that can be imported into Pulumi.
    rpc ConvertState(ConvertStateRequest) returns (ConvertStateResponse) {}

    // ConvertProgram converts a program from the target ecosystem into a form that can be used with Pulumi.
    rpc ConvertProgram(ConvertProgramRequest) returns (ConvertProgramResponse) {}
}
```

> This Converter interface is considered experimental and is subject to change in the future.

Now, learning how to setup gRPC servers and implement the `Converter` contract is not an easy task unless you are familiar with it. For .NET, we shipped the _experimental_ Pulumi converter SDK to the main Pulumi nuget package that makes it extremely easy to build converter plugins.

A bare-bones converter plugin which does nothing looks like this in F#:

```fsharp
open Pulumi.Experimental.Converter
open Pulumi.Codegen

let convertProgram (request: ConvertProgramRequest): ConvertProgramResponse =
    // TODO: Implement the conversion logic here
    ConvertProgramResponse.Empty

convertProgram
|> Converter.CreateSimple
|> Converter.Serve
|> Async.AwaitTask
|> Async.RunSynchronously
```

This will spin up a gRPC server that implements the `Converter` contract and will serve it on a random port assigned during startup. The Pulumi converter SDK automatically implements gRPC reflection which allows tools such as [Postman](https://www.postman.com/) to discover the available gRPC services and methods and send example requests to them. See [Postman with gRPC](https://blog.postman.com/postman-now-supports-grpc/).

## Publishing converter plugins

The easiest way to make your converter plugin available to others is to publish it on GitHub releases. The Pulumi CLI expects a naming convention `pulumi-converter-<name>` and will automatically download the plugin from the latest GitHub release of the repository when given the `--server` flag during `pulumi plugin install converter <name> --server <url>`.

Converter plugins written in .NET are simple console applications that are compiled to native binaries for each target platform. To see how this is done, refer to this [createAndPublishArtifacts](https://github.com/Zaid-Ajaj/pulumi-converter-bicep/blob/master/build/Program.fs#L197) function written for the Bicep converter that does the heavy lifting of building the native binaries for each platform, putting them in an archive then publishing them to GitHub releases.

> Note: when publishing native binaries for macOS, the Github Action executing the publishing process must be using a macOS runner so that the generated binary from `dotnet publish` gets _signed_ with a developer certificate. This is required for the binary to be executable on macOS.

## Final thoughts

I hope you enjoyed this article and learned something new about the Pulumi converter plugins and Pulumi internals. I am very excited about the Bicep converter plugin and I am looking forward to hearing your feedback on it from the community. It was a lot of fun writing this in F# and made writing complex pieces of code very trivial.

If you have any questions or feedback, don't hesitate to reach out!
