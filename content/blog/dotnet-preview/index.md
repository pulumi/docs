---
title: "Configure Infrastructure with .NET and Pulumi"
authors: ["sophia-parafina"]
tags: [". NET", "C#", "F#", "Visual Basic"]
meta_image: "microsoft_logo.jpg"
meta_desc: "Pulumi supports . NET languages for Infastructure as Code"
date: "2019-11-08"
---

We are excited to announce the preview of Pulumi . NET support. Pulumi lets you declare infrastructure using general purpose programming languages. Our goal is to automate applications at all layers and help developers and operators work better together by eliminating the silos that separate them.

Millions of . NET developers can now use their favorite languages and open source ecosystems to build modern, cloud native applications. We've added support for C#, F# and Visual Basic. Because the . NET framework is available on Windows, Linux and macOS you have a choice of platforms to use. You can create cloud resources by writing **Microsoft . NET Core** programs to build and deploy AKS Clusters, Functions, Azure App Services, Virtual Machines, Cosmos DBs, KeyVaults, and much, much more.

## What Does Pulumi Enable?

As a . NET developer you can:

* Declare infrastructure in C#, F#, or Visual Basic NET.
* Code with favorite IDEs, including Visual Studio, Visual Studio Code, and Rider, with auto-completion and refactoring tools.
* Catch mistakes early on with red markers and build errors.
* Allow package managers to reference any NuGet library compatible with . NET Core 3.0.
* Use the Pulumi CLI or CI/CD integrations to perform deployments predictably and reliably.
* Maintain your infrastructure in a repository and version it
* Build modern, reliable, and scalable applications using a multitude of cloud architectures, including containers, serverless functions, and static websites.

You can do all of this without having to learn a DSL or script CLI commands. With Pulumi, developers and operators have a shared foundation for building modern applications.

## How Pulumi . NET Works

Pulumi is declarative even though it uses general purpose programming languages. It does this by declaring a set of resources and the Pulumi engine orchestrates the CRUD operations to build and deploy infrastructure.

We use a . NET Core console application to declare infrastructure. Let's create an Azure App Service with a SQL database. The first step is make sure that your environment meets the prerequisites:

### Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/get-started/install/)

1. [Install . NET Core 3.0+](https://dotnet.microsoft.com/download)

1. [A Microsoft Azure account](https://azure.microsoft.com/en-us/free/)

1. [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

### Get the Examples

Pulumi provides a repository of examples to get you started. Clone the examples from GitHub.

``` bash
git clone https://github.com/pulumi/examples/
cd examples/
```

### Create a New Stack

Change the directory to `azure-cs-appservice` directory

``` bash
$ cd azure-cs-appservice
```

There are four files in the Pulumi project, the `Azure.Appservice.csproj` which sets the . NET SDK and the Pulumi packages for the project. `Pulumi.yaml` holds project parameters such as name, runtime and the database password. `SharedAccessSignature.cs` specifies the storage to hold code, which is the `wwwroot` directory in this project. `Program.cs` is the main program for declaring resources.

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

1. Define SQL Server password (make it complex enough to satisfy Azure policy):

    ``` bash
    pulumi config set --secret sqlPassword <value>
    ```

1. Run `pulumi up` to preview and deploy changes:

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
**NOTE**

> If you are using a free Azure account, some regions do not allow creation of services if they are too busy. You might have to try a different [Azure location](https://azure.microsoft.com/en-us/global-infrastructure/locations/).
>
> You must tear down the stack resources to update the project's location information.

``` bash
$ pulumi destroy --yes
$ pulumi stack rm --yes
```

### Test Your Stack

Check the deployed website endpoint:

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

## Recap

In this post we've shown how to use Pulumi to deploy a modern application to Azure. The example code performs a number of tasks.

First, we created a [resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview#resource-groups), a [storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy-lrs), and an [application service plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans) for our application:

   ```C#
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

We then package the `wwwroot` directory containing the `index.html` page into the storage account we created previously.

   ```C#
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

Using the configuration we set with the Pulumi CLI, the program creates a SQLServer deployment.

   ```C#
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

We deploy the app service which includes the website and the connection to the SQLServer instance.

   ```C#
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

In this example, we declared resources for a website and a database using C# and the Pulumi engine deployed them on Azure. To get started with infrastructure as code, download [Pulumi](https://www.pulumi.com/docs/get-started/install/) to build and deploy modern applications using .NET.