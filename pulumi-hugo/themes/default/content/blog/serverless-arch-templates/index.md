---
title: "Serverless Arch Templates"
date: 2022-11-07
meta_desc: The cloud is complicated enough. With Architecture Templates, Pulumi takes on some of the work involved in deploying your application to the cloud.
meta_image: meta.png
authors:
    - kat-cosgrove
tags:
    - templates
    - serverless
    - arch-templates
---

Whether you're building a new application or moving an existing application over from another provider, the basic framework of your infrastructure probably isn't something you want to worry about if you don't have to. The cloud is complicated enough as it is. With Architecture Templates, Pulumi takes on some of the work involved in deploying your application to the cloud provider of your choice. Let's take a tour of the new Serverless Templates for AWS, GCP, and Azure!

<!--more-->

### Serverless on any Cloud, in any Language

If you need a serverless application, whether that's AWS Lambda, Google Cloud Functions, or Azure Functions, one of these templates can give you the starting point you need in any language Pulumi supports. Each template deploys a serverless function for you, with all necessary permissions to make it publicly available. While each of them does deploy a small sample function, these are designed to be extensible; we give you all the necessary tools to begin building your own application, without having to fuss around standing up the infrastructure yourself.

Generating the necessary starter code happens with a single CLI command, regardless of which cloud and language you choose:

#### AWS

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-aws-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-aws-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-aws-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-aws-csharp
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-aws-yaml
```

{{% /choosable %}}

#### GCP

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-gcp-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-gcp-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-gcp-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-gcp-csharp
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-gcp-yaml
```

{{% /choosable %}}

#### Azure

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-azure-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-azure-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-azure-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-azure-csharp
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir my-serverless-app && cd my-serverless-app
$ pulumi new serverless-azure-yaml
```

{{% /choosable %}}

## Pulumi to the Cloud

Each of these commands will generate some boilerplate for you, and includes defaults you can accept or modify (such as the name of the project, or the application directory). Run `pulumi up` from this directory, ensuring that you've connected the [Pulumi CLI](/docs/get-started/) to your preferred cloud provider, and your starting point is online, ready for you to sub in your own application code. For the purposes of this demonstration, I've accepted the defaults. I've also left the provided application and function code in place. Let's examine what Pulumi creates for us here, using Python for AWS, Go for GCP, and Typescript for Azure.

{{% chooser cloud "aws,gcp,azure" / %}}

{{% choosable cloud aws %}}

```python
import json
import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

# An execution role to use for the Lambda function
role = aws.iam.Role("role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
        }],
    }),
    managed_policy_arns=[aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE])

# A Lambda function to invoke
fn = aws.lambda_.Function("fn",
    runtime="python3.9",
    handler="handler.handler",
    role=role.arn,
    code=pulumi.FileArchive("./function"))

# A REST API to route requests to HTML content and the Lambda function
api = apigateway.RestAPI("api",
  routes=[
    apigateway.RouteArgs(path="/", local_path="www"),
    apigateway.RouteArgs(path="/date", method=apigateway.Method.GET, event_handler=fn)
  ])

# The URL at which the REST API will be served.
pulumi.export("url", api.url)
```

Here Pulumi has provided an IAM execution role to use for the Lambda function, the Lambda function itself, and a REST API gateway to handle request routing. The Lambda function is pointed at an included `./function` directory, which contains a Python function that returns the latest datetime. This can be replaced with your own code, or you can change the directory the Pulumi code is pointed at to your own. Similarly, the API gateway is pointed at a `www` directory containing a simple website to display the current datetime, ready to be replaced with your own content.

{{% /choosable %}}

{{% choosable cloud gcp %}}

```golang
package main

import (
    "fmt"

    "github.com/pulumi/pulumi-gcp/sdk/v6/go/gcp/cloudfunctions"
    "github.com/pulumi/pulumi-gcp/sdk/v6/go/gcp/storage"
    synced "github.com/pulumi/pulumi-synced-folder/sdk/go/synced-folder"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {

        // Import the program's configuration settings.
        cfg := config.New(ctx, "")
        sitePath := "./www"
        if param := cfg.Get("sitePath"); param != "" {
            sitePath = param
        }
        appPath := "./app"
        if param := cfg.Get("appPath"); param != "" {
            appPath = param
        }
        indexDocument := "index.html"
        if param := cfg.Get("indexDocument"); param != "" {
            indexDocument = param
        }
        errorDocument := "error.html"
        if param := cfg.Get("errorDocument"); param != "" {
            errorDocument = param
        }

        // Create a storage bucket and configure it as a website.
        siteBucket, err := storage.NewBucket(ctx, "site-bucket", &storage.BucketArgs{
            Location: pulumi.String("US"),
            Website: &storage.BucketWebsiteArgs{
                MainPageSuffix: pulumi.String(indexDocument),
                NotFoundPage:   pulumi.String(errorDocument),
            },
        })
        if err != nil {
            return err
        }

        // Create an IAM binding to allow public read access to the bucket.
        _, err = storage.NewBucketIAMBinding(ctx, "site-bucket-iam-binding", &storage.BucketIAMBindingArgs{
            Bucket: siteBucket.Name,
            Role:   pulumi.String("roles/storage.objectViewer"),
            Members: pulumi.StringArray{
                pulumi.String("allUsers"),
            },
        })
        if err != nil {
            return err
        }

        // Use a synced folder to manage the files of the website.
        _, err = synced.NewGoogleCloudFolder(ctx, "synced-folder", &synced.GoogleCloudFolderArgs{
            Path:       pulumi.String(sitePath),
            BucketName: siteBucket.Name,
        })
        if err != nil {
            return err
        }

        // Create another storage bucket for the serverless app.
        appBucket, err := storage.NewBucket(ctx, "app-bucket", &storage.BucketArgs{
            Location: pulumi.String("US"),
        })
        if err != nil {
            return err
        }

        // Upload the serverless app to the storage bucket.
        appArchive, err := storage.NewBucketObject(ctx, "app-archive", &storage.BucketObjectArgs{
            Bucket: appBucket.Name,
            Source: pulumi.NewFileArchive(appPath),
        })
        if err != nil {
            return err
        }

        // Create a Cloud Function that returns some data.
        dataFunction, err := cloudfunctions.NewFunction(ctx, "data-function", &cloudfunctions.FunctionArgs{
            SourceArchiveBucket: appBucket.Name,
            SourceArchiveObject: appArchive.Name,
            Runtime:             pulumi.String("go116"),
            EntryPoint:          pulumi.String("Data"),
            TriggerHttp:         pulumi.Bool(true),
        })
        if err != nil {
            return err
        }

        // Create an IAM member to invoke the function.
        _, err = cloudfunctions.NewFunctionIamMember(ctx, "data-function-invoker", &cloudfunctions.FunctionIamMemberArgs{
            Project:       dataFunction.Project,
            Region:        dataFunction.Region,
            CloudFunction: dataFunction.Name,
            Role:          pulumi.String("roles/cloudfunctions.invoker"),
            Member:        pulumi.String("allUsers"),
        })
        if err != nil {
            return err
        }

        // Create a JSON configuration file for the website.
        _, err = storage.NewBucketObject(ctx, "site-config", &storage.BucketObjectArgs{
            Name:        pulumi.String("config.json"),
            Bucket:      siteBucket.Name,
            ContentType: pulumi.String("application/json"),
            Source: dataFunction.HttpsTriggerUrl.ApplyT(func(url string) pulumi.AssetOrArchiveOutput {
                config := fmt.Sprintf(`{ "api": "%s" }`, url)
                return pulumi.NewStringAsset(config).ToAssetOrArchiveOutput()
            }).(pulumi.AssetOrArchiveOutput),
        })
        if err != nil {
            return err
        }

        // Export the URLs of the website and serverless endpoint.
        ctx.Export("siteURL", pulumi.Sprintf("https://storage.googleapis.com/%s/index.html", siteBucket.Name))
        ctx.Export("apiURL", dataFunction.HttpsTriggerUrl)

        return nil
    })
}
```

Here Pulumi is defining your application's initial configuration values, including the directories it should be checking for your serverless application code and the index and error pages for the website it stands up. It then creates two storage buckets, each with appropriate IAM roles for access, one containing your serverless function and another configured to act like a website. We also have the Cloud Function declaration itself, and all configurations necessary for it, followed by exporting the URL for you.

{{% /choosable %}}

{{% choosable cloud azure %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure-native";
import * as synced from "@pulumi/synced-folder";

// Import the program's configuration settings.
const config = new pulumi.Config();
const sitePath = config.get("sitePath") || "./www";
const appPath = config.get("appPath") || "./app";
const indexDocument = config.get("indexDocument") || "index.html";
const errorDocument = config.get("errorDocument") || "error.html";

// Create a resource group for the website.
const resourceGroup = new azure.resources.ResourceGroup("resource-group", {});

// Create a blob storage account.
const account = new azure.storage.StorageAccount("account", {
    resourceGroupName: resourceGroup.name,
    kind: azure.storage.Kind.StorageV2,
    sku: {
        name: azure.storage.SkuName.Standard_LRS,
    },
});

// Create a storage container for the pages of the website.
const website = new azure.storage.StorageAccountStaticWebsite("website", {
    accountName: account.name,
    resourceGroupName: resourceGroup.name,
    indexDocument: indexDocument,
    error404Document: errorDocument,
});

// Use a synced folder to manage the files of the website.
const syncedFolder = new synced.AzureBlobFolder("synced-folder", {
    path: sitePath,
    resourceGroupName: resourceGroup.name,
    storageAccountName: account.name,
    containerName: website.containerName,
});

// Create a storage container for the serverless app.
const appContainer = new azure.storage.BlobContainer("app-container", {
    accountName: account.name,
    resourceGroupName: resourceGroup.name,
    publicAccess: azure.storage.PublicAccess.None,
});

// Upload the serverless app to the storage container.
const appBlob = new azure.storage.Blob("app-blob", {
    accountName: account.name,
    resourceGroupName: resourceGroup.name,
    containerName: appContainer.name,
    source: new pulumi.asset.FileArchive(appPath),
});

// Create a shared access signature to give the Function App access to the code.
const signature = azure.storage.listStorageAccountServiceSASOutput({
    resourceGroupName: resourceGroup.name,
    accountName: account.name,
    protocols: azure.storage.HttpProtocol.Https,
    sharedAccessStartTime: "2022-01-01",
    sharedAccessExpiryTime: "2030-01-01",
    resource: azure.storage.SignedResource.C,
    permissions: azure.storage.Permissions.R,
    contentType: "application/json",
    cacheControl: "max-age=5",
    contentDisposition: "inline",
    contentEncoding: "deflate",
    canonicalizedResource: pulumi.interpolate`/blob/${account.name}/${appContainer.name}`,
});

// Create an App Service plan for the Function App.
const plan = new azure.web.AppServicePlan("plan", {
    resourceGroupName: resourceGroup.name,
    sku: {
        name: "Y1",
        tier: "Dynamic",
    },
});

// Create the Function App.
const functionApp = new azure.web.WebApp("function-app", {
    resourceGroupName: resourceGroup.name,
    serverFarmId: plan.id,
    kind: "FunctionApp",
    siteConfig: {
        appSettings: [
            {
                name: "FUNCTIONS_WORKER_RUNTIME",
                value: "node",
            },
            {
                name: "WEBSITE_NODE_DEFAULT_VERSION",
                value: "~14",
            },
            {
                name: "FUNCTIONS_EXTENSION_VERSION",
                value: "~3",
            },
            {
                name: "WEBSITE_RUN_FROM_PACKAGE",
                value: pulumi.all([account.name, appContainer.name, appBlob.name, signature])
                    .apply(([accountName, containerName, blobName, signature]) => `https://${accountName}.blob.core.windows.net/${containerName}/${blobName}?${signature.serviceSasToken}`),
            },
        ],
        cors: {
            allowedOrigins: [
                "*"
            ],
        },
    },
});

// Create a JSON configuration file for the website.
const configFile = new azure.storage.Blob("config.json", {
    source: functionApp.defaultHostName
        .apply(host => new pulumi.asset.StringAsset(JSON.stringify({ api: `https://${host}/api` }))),
    contentType: "application/json",
    accountName: account.name,
    resourceGroupName: resourceGroup.name,
    containerName: website.containerName,
});

// Export the URLs of the website and serverless endpoint.
export const siteURL = account.primaryEndpoints.apply(primaryEndpoints => primaryEndpoints.web);
export const apiURL = pulumi.interpolate`https://${functionApp.defaultHostName}/api`;
```

Here, Pulumi first defines the configuration options for your project, including the directories to look at for your application code and your website, as well as what the index and error documents should be. It then goes on to set up your blob storage account and containers for your website and serverless function, before uploading the serverless function itself with all permissions and configurations necessary to operate.

{{% /choosable %}}

## Extending Templates

In addition to the Pulumi code above, each template includes a simple website that utilizes a provided serverless function to display the current time and date, constantly updating. With only two CLI commands, you have deployed the core infrastructure necessary to get your serverless application online in the cloud, without writing a single line of code yourself.

From here, you're ready to drop in your own application code. Pulumi has already handled the boring work for you, complying with best practices from the beginning so you only have to worry about building your own application, not how to get the infrastructure online!

[Pulumi Architecture Templates](/templates/) exist for a variety of applications and common use-cases, including containerized applications and kubernetes, with more being added over time. Keep an eye out for new additions and ways to make engineering for the cloud less painful!
