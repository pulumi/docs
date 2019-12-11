---
title: "Infrastructure as Code with .NET and Pulumi"
date: 2019-11-13T11:23:04-06:00
draft: false
meta_desc: "Pulumi launches supports .NET Core languages for Infrastructure as Code"
meta_image: "meta.png"
authors:
    - sophia-parafina
tags:
    - ".NET"
    - "C#"
    - "F#"
    - "Visual Basic"
---
With the release of [Pulumi for .NET preview](https://www.pulumi.com/blog/pulumi-dotnet-core/), we've open the doors to infrastructure as code to even more developers and operators. Millions of .NET developers can now use their favorite languages and open source ecosystems to build modern, cloud native applications. We've added support for C#, F#, and Visual Basic. Because .NET Core is available on Windows, Linux, and macOS, you have a choice of platforms to use.

You can create cloud resources by writing Microsoft .NET Core programs to build and deploy cloud resources to a wide variety of clouds, including Azure, AWS, GCP and more.  On Azure, you can manage resources like AKS Clusters, Functions, Azure App Services, Virtual Machines, Cosmos DBs, KeyVaults, and much, much more. Let's take a first look at Pulumi for .NET by deploying an application on Azure.

## What Does Pulumi Enable?

With Pulumi, .NET developers can create, deploy and manage cloud infrastructure using C#, F#, or Visual Basic .NET. This results in increased productivity for developers because they can use the features of their IDEs such as auto-completion, error checking with red markers, build error messages, refactoring tools, and package managers. Developers can reference any NuGet library compatible with .NET Core 3.0.

Operators can use the `pulumi` CLI or CI/CD integrations to maintain and version infrastructure in a repository resulting in predictable and reliable deployments. Regardless of your cloud architecture, whether it includes containers, serverless function or static websites, Pulumi lets you build modern, reliable, and scalable applications. Your pipeline is part of your product.

You can accomplish all of this without having to learn a JSON or YAML DSL or script low-level CLI commands. With Pulumi, developers and operators have a shared foundation for building modern applications.

## How Pulumi for .NET Works

Pulumi is declarative even though it uses general purpose programming languages. It does this by specifying a set of resources, and the Pulumi engine orchestrates the CRUD operations to build and deploy infrastructure.

A Pulumi project uses a .NET Core console application to build infrastructure. To illustrate how this is accomplished, let's create an Azure App Service with an SQL database. The first step is to make sure that your environment meets the prerequisites:

### Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)

1. [Install .NET Core SDK 3.0+](https://dotnet.microsoft.com/download)

1. [Configure a Microsoft Azure account](https://azure.microsoft.com/en-us/free/)

1. [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

### Get the Examples

Pulumi provides a repository of examples to get you started. Clone the examples from GitHub.

``` bash
$ git clone https://github.com/pulumi/examples/
$ cd examples/
```

### Create a New Stack

Change the directory to `azure-cs-appservice` directory

``` bash
$ cd azure-cs-appservice
```

There are four files in the Pulumi project, the `Azure.Appservice.csproj` which sets the .NET SDK and the Pulumi packages for the project. `Pulumi.yaml` holds project parameters such as name and runtime. The `Pulumi.dev.yaml` file holds the database password. `SharedAccessSignature.cs` contains a helper function to generate storage blob access URLs with SAS tokens in them. It demonstrates that you can add custom code inside your Pulumi program. `Program.cs` is the main program for declaring resources.

1. Create a new stack:

    ``` bash
    $ pulumi stack init dev
    ```

1. Login to Azure CLI (you will be prompted to do this during deployment if you forget this step):

    ``` bash
    $ az login
    ```

1. Configure the location to deploy the resources to:

    ``` bash
    $ pulumi config set azure:location centralus
    ```

1. Define the SQL Server password (make it complex enough to satisfy [Azure policy](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy#password-policies-that-only-apply-to-cloud-user-accounts)):

    ``` bash
    pulumi config set --secret sqlPassword <value>
    ```

1. Run `pulumi up`. Pulumi will display a preview of the updates to the stack and ask if you would like to deploy by updating.

    ``` bash
    $ pulumi up
    Previewing changes:
    ...

    Performing changes:
    ...
    info: 10 changes performed:

        + 10 resources created

    Update duration: 1m14.59910109s
    ```

___
**NOTE:**

> If you are using a free Azure account, some regions do not allow creating services if they are too busy. You might have to try a different [Azure location](https://azure.microsoft.com/en-us/global-infrastructure/locations/). You must tear down the stack resources to update the project's location information.
___

### Test Your Stack

The endpoint is one of the outputs that the stack returns. Check the deployed website endpoint by querying the stack and using curl to retrieve the web page.

``` bash
$ pulumi stack output endpoint
https://azpulumi-as0ef47193.azurewebsites.net

$ curl "$(pulumi stack output endpoint)"
<html>
  <body>
     <h1>Greetings from Azure App Service!</h1>
  </body>
</html>
```

From there, feel free to experiment. Simply making edits and running `pulumi up` will incrementally update your stack. Once finished, tear down your stack's resources by destroying and removing it:

``` bash
$ pulumi destroy --yes
$ pulumi stack rm --yes
```

## Code Review

In this post, we've shown how to use Pulumi to deploy a modern application to Azure. The example code performs a number of tasks.

First, we created a [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview#resource-groups), a [storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy-lrs), and an [application service plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans) for our application:

```csharp
var resourceGroup = new ResourceGroup("appservice-rg");

var storageAccount = new Account("sa", new AccountArgs
{

   ResourceGroupName = resourceGroup.Name,
   AccountReplicationType = "LRS",
   AccountTier = "Standard",

});

var appServicePlan = new Plan("asp", new PlanArgs
{

   ResourceGroupName = resourceGroup.Name,
   Kind = "App",
   Sku = new PlanSkuArgs
   {
       Tier = "Basic",
       Size = "B1",
    },

});
```

The `wwwroot` directory containing the `index.html` page into is added to the storage account we created previously. The `SharedAccessSignature.cs` code is a helper function to generate storage blob access URLs with [SAS tokens](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview). This shows how you can add custom code inside your Pulumi program.

```csharp
var container = new Container("zips", new ContainerArgs
{
   StorageAccountName = storageAccount.Name,
   ContainerAccessType = "private",
});

var blob = new ZipBlob("zip", new ZipBlobArgs
{
   StorageAccountName = storageAccount.Name,
   StorageContainerName = container.Name,
   Type = "block",
   Content = new FileArchive("wwwroot"),
});

var codeBlobUrl = SharedAccessSignature.SignedBlobReadUrl(blob, storageAccount);
```

Using the configuration we set with the Pulumi CLI, the program creates a SQL Server deployment.

```csharp
var config = new Config();
var username = config.Get("sqlAdmin") ?? "pulumi";
var password = config.RequireSecret("sqlPassword");
var sqlServer = new SqlServer("sql", new SqlServerArgs
{
   ResourceGroupName = resourceGroup.Name,
   AdministratorLogin = username,
   AdministratorLoginPassword = password,
   Version = "12.0",
});

var database = new Database("db", new DatabaseArgs
{
   ResourceGroupName = resourceGroup.Name,
   ServerName = sqlServer.Name,
   RequestedServiceObjectiveName = "S0",
});
```

We deploy the App Service which includes the website and the connection to the SQL Server instance.

```csharp
var app = new AppService("app", new AppServiceArgs
{
   ResourceGroupName = resourceGroup.Name,
   AppServicePlanId = appServicePlan.Id,
   AppSettings =
   {
       { "WEBSITE_RUN_FROM_PACKAGE", codeBlobUrl },
   },
   ConnectionStrings =
       {
           new AppServiceConnectionStringsArgs
           {
                Name = "db",
               Type = "SQLAzure",
               Value = Output.Tuple<string, string, string>(sqlServer.Name, database.Name, password).Apply(t =>
               {
                   (string server, string database, string pwd) = t;
                   return $"Server= tcp:{server}.database.windows.net;initial catalog={database};userID={username};password={pwd};Min Pool Size=0;Max Pool Size=30;Persist Security Info=true;";
               }),
           },
       },
});
```

## Summary

In this example, we declared resources for a website and a database using C# and the Pulumi engine deployed them to Azure. To get started with infrastructure as code, download [Pulumi](https://www.pulumi.com/docs/get-started/install/) to build and deploy modern applications using .NET Core.
