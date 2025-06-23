---
title_tag: "Getting Started with Automation API"
meta_desc: This page contains a getting started guide for Automation API.
title: Get started
h1: Get started with Automation API
weight: 1
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Getting Started
        parent: iac-automation-api
        weight: 1
aliases:
- /docs/guides/automation-api/getting-started-automation-api/
- /docs/using-pulumi/automation-api/getting-started-automation-api/
- /docs/iac/packages-and-automation/automation-api/getting-started-automation-api/
- /docs/iac/using-pulumi/automation-api/getting-started-automation-api/
---

Pulumi’s Automation API enables you to provision your infrastructure programmatically using the Pulumi engine by exposing Pulumi programs and stacks as strongly-typed and composable building blocks.

In this guide, you will deploy an inline Pulumi program to create a static website using Automation API.

## Prerequisites

### Install Pulumi

{{< install-pulumi />}}

Install the required language runtime, if you have not already.

### Install language runtime

#### Choose your language

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language "javascript,typescript" %}}
{{< install-node >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< install-go >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{% choosable language "java,fsharp,visualbasic" %}}
{{< install-java >}}
{{% /choosable %}}
{{< /chooser >}}

### Obtain a Pulumi access token

You'll need a [Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens) so that your programs can store the resulting state in the Pulumi Cloud. The easiest way to obtain a token is to run `pulumi login` from the command line.

## Define your Pulumi program

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

First, define the Pulumi program you want to run as a function within your overall program. Note how it looks like a standard Pulumi program.

{{% choosable language "javascript,typescript" %}}

{{% notes type="info" %}}
This tutorial is based on the [`inlineProgram-ts` example](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/inlineProgram-ts), which is a complete example of how to construct a simple Automation API program.
{{% /notes %}}

```typescript
const pulumiProgram = async () => {
    // Create a bucket and expose a website index document.
    const siteBucket = new s3.BucketV2("s3-website-bucket", {});

    const indexContent = `<html><head>
<title>Hello S3</title><meta charset="UTF-8">
</head>
<body><p>Hello, world!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
</body></html>
`

    const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
        bucket: siteBucket.id,
        rule: {
            objectOwnership: "ObjectWriter",
        },
    });

    const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
        bucket: siteBucket.id,
        blockPublicAcls: false,
    });

    const website = new aws.s3.BucketWebsiteConfigurationV2("website", {
        bucket: siteBucket.id,
        indexDocument: {
            suffix: "index.html",
        },
    });

    // Write our index.html into the site bucket.
    const object = new s3.BucketObject("index", {
        bucket: siteBucket.id,
        content: indexContent,
        contentType: "text/html; charset=utf-8",
        key: "index.html",
        acl: "public-read"
    }, {
        dependsOn: [
            publicAccessBlock,
            ownershipControls,
            website,
        ],
    });

    return {
        websiteUrl: website.websiteEndpoint,
    };
};
```

{{% /choosable %}}

{{% choosable language python %}}

{{% notes type="info" %}}
This tutorial is based on the [`inline_program` example](https://github.com/pulumi/automation-api-examples/tree/main/python/inline_program), which is a complete example of how to construct a simple Automation API program.
{{% /notes %}}

```python
def pulumi_program():
    # Create a bucket and expose a website index document.
    site_bucket = s3.BucketV2("s3-website-bucket")

    index_content = """
    <html>
        <head><title>Hello S3</title><meta charset="UTF-8"></head>
        <body>
            <p>Hello, world!</p>
            <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
        </body>
    </html>
    """

    ownership_controls = s3.BucketOwnershipControls("ownership-controls",
        bucket=site_bucket.id,
        rule={
            "object_ownership": "ObjectWriter",
        })

    public_access_block = s3.BucketPublicAccessBlock("public-access-block",
        bucket=site_bucket.id,
        block_public_acls=False)

    website = aws.s3.BucketWebsiteConfigurationV2("website",
        bucket=site_bucket.id,
        index_document={
            "suffix": "index.html",
        })

    # Write our index.html into the site bucket.
    s3.BucketObject("index",
                    bucket=site_bucket.id,  # Reference to the s3.Bucket object.
                    content=index_content,
                    acl="public-read",
                    key="index.html",  # Set the key of the object.
                    content_type="text/html; charset=utf-8", # Set the MIME type of the file.
                    opts=pulumi.ResourceOptions(depends_on=[
                        public_access_block,
                        ownership_controls,
                        website,
                    ]))

    # Export the website URL.
    pulumi.export("website_url", website.website_endpoint)
```

{{% /choosable %}}

{{% choosable language go %}}

{{% notes type="info" %}}
This tutorial is based on the [`inline_program` example](https://github.com/pulumi/automation-api-examples/tree/main/go/inline_program), which is a complete example of how to construct a simple Automation API program.
{{% /notes %}}

```go
deployFunc := func(ctx *pulumi.Context) error {
    // Similar go git_repo_program, our program defines a s3 website.
    // Here we create the bucket.
    siteBucket, err := s3.NewBucketV2(ctx, "s3-website-bucket", nil)
    if err != nil {
        return err
    }

    // We define and upload our HTML inline.
    indexContent := `<html><head>
<title>Hello S3</title><meta charset="UTF-8">
</head>
<body><p>Hello, world!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
</body></html>
`

    ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
        Bucket: siteBucket.ID(),
        Rule: &s3.BucketOwnershipControlsRuleArgs{
            ObjectOwnership: pulumi.String("ObjectWriter"),
        },
    })
    if err != nil {
        return err
    }

    publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
        Bucket:          siteBucket.ID(),
        BlockPublicAcls: pulumi.Bool(false),
    })
    if err != nil {
        return err
    }

    website, err := s3.NewBucketWebsiteConfigurationV2(ctx, "website", &s3.BucketWebsiteConfigurationV2Args{
        Bucket: siteBucket.ID(),
        IndexDocument: &s3.BucketWebsiteConfigurationV2IndexDocumentArgs{
            Suffix: pulumi.String("index.html"),
        },
    })
    if err != nil {
        return err
    }
    // Upload our index.html.
    if _, err := s3.NewBucketObject(ctx, "index", &s3.BucketObjectArgs{
        Bucket:      siteBucket.ID(), // Reference to the s3.Bucket object.
        Content:     pulumi.String(indexContent),
        Acl:         pulumi.String("public-read"),
        Key:         pulumi.String("index.html"),               // Set the key of the object.
        ContentType: pulumi.String("text/html; charset=utf-8"), // Set the MIME type of the file.
    }, pulumi.DependsOn([]pulumi.Resource{
        publicAccessBlock,
        ownershipControls,
        website,
    })); err != nil {
        return err
    }

    // Export the website URL.
    ctx.Export("websiteUrl", website.WebsiteEndpoint)
    return nil
}
```

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

{{% notes type="info" %}}
This tutorial is based on the [`InlineProgram` example](https://github.com/pulumi/automation-api-examples/tree/main/dotnet/InlineProgram), which is a complete example of how to construct a simple Automation API program.
{{% /notes %}}

```csharp
var program = PulumiFn.Create(() =>
{
    // Create a bucket and expose a website index document.
    var siteBucket = new Pulumi.Aws.S3.Bucket("s3-website-bucket");

    const string indexContent = @"
<html>
    <head><title>Hello S3</title><meta charset=""UTF-8""></head>
    <body>
        <p>Hello, world!</p>
        <p>Made with ❤️ with <a href=""https://pulumi.com"">Pulumi</a></p>
    </body>
</html>";

    var ownershipControls = new Aws.S3.BucketOwnershipControls("ownership-controls", new()
    {
        Bucket = siteBucket.Id,
        Rule = new Aws.S3.Inputs.BucketOwnershipControlsRuleArgs
        {
            ObjectOwnership = "ObjectWriter",
        },
    });

    var publicAccessBlock = new Aws.S3.BucketPublicAccessBlock("public-access-block", new()
    {
        Bucket = siteBucket.Id,
        BlockPublicAcls = false,
    });

    var website = new Aws.S3.BucketWebsiteConfigurationV2("website", new()
    {
        Bucket = siteBucket.Id,
        IndexDocument = new Aws.S3.Inputs.BucketWebsiteConfigurationV2IndexDocumentArgs
        {
            Suffix = "index.html",
        },
    });

    // Write our index.html into the site bucket.
    var @object = new Pulumi.Aws.S3.BucketObject("index", new Pulumi.Aws.S3.BucketObjectArgs
    {
        Bucket = siteBucket.BucketName, // Reference to the s3 bucket object.
        Content = indexContent,
        Acl = "public-read",
        Key = "index.html", // Set the key of the object.
        ContentType = "text/html; charset=utf-8", // Set the MIME type of the file.
    }, new CustomResourceOptions
    {
        DependsOn =
        {
            publicAccessBlock,
            ownershipControls,
            website,
        },
    });

    // Export the website url.
    return new Dictionary<string, object?>
    {
        ["website_url"] = website.WebsiteEndpoint
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

{{% notes type="info" %}}
This tutorial is based on the [`InlineProgram` example](https://github.com/pulumi/automation-api-examples/tree/main/java/InlineProgram), which is a complete example of how to construct a simple Automation API program.
{{% /notes %}}

```java
private static void pulumiProgram(Context ctx) {

    // Create an AWS resource (S3 Bucket)
    var siteBucket = new BucketV2("s3-website-bucket");

    var website = new BucketWebsiteConfigurationV2("website", BucketWebsiteConfigurationV2Args.builder()
            .bucket(siteBucket.id())
            .indexDocument(BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
                    .suffix("index.html")
                    .build())
            .build());

    var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
            .bucket(siteBucket.id())
            .rule(BucketOwnershipControlsRuleArgs.builder()
                    .objectOwnership("ObjectWriter")
                    .build())
            .build());

    var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
            .bucket(siteBucket.id())
            .blockPublicAcls(false)
            .build());

    String indexContent = """
            <html>
                <head><title>Hello S3</title><meta charset="UTF-8"></head>
                <body>
                    <p>Hello, world!</p>
                    <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
                </body>
            </html>
            """;

    var indexHtml = new BucketObject("index.html", BucketObjectArgs.builder()
            .bucket(siteBucket.id())
            .content(indexContent)
            .contentType("text/html")
            .acl("public-read")
            .build(),
            CustomResourceOptions.builder()
                    .dependsOn(
                            publicAccessBlock,
                            ownershipControls,
                            website)
                    .build());

    // Export the name of the bucket
    ctx.export("website_url",
            website.websiteEndpoint().applyValue(websiteEndpoint -> String.format("http://%s", websiteEndpoint)));
}
```

{{% /choosable %}}
{{< /chooser >}}

## Associate with a stack

As with executing Pulumi programs through the CLI, you need to associate your Pulumi program with a `Stack`. Automation API provides methods to create or select stacks.

Here's a convenient method to select an existing `Stack` or create one if none exists:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const args: InlineProgramArgs = {
    stackName: "dev",
    projectName: "inlineNode",
    program: pulumiProgram
};

const stack = await LocalWorkspace.createOrSelectStack(args);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
project_name = "inline_s3_project"
stack_name = "dev"

stack = auto.create_or_select_stack(stack_name=stack_name,
                                    project_name=project_name,
                                    program=pulumi_program)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
projectName := "inlineS3Project"
stackName := "dev"
s, err := auto.UpsertStackInlineSource(ctx, stackName, projectName, deployFunc)
```

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

```csharp
var projectName = "inline_s3_project";
var stackName = "dev";

var stackArgs = new InlineProgramArgs(projectName, stackName, program);
var stack = await LocalWorkspace.CreateOrSelectStackAsync(stackArgs);
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
var projectName = "inline_s3_project_java";
var stackName = "dev";
var stack = LocalWorkspace.createOrSelectStack(projectName, stackName, App::pulumiProgram);
```

{{% /choosable %}}
{{< /chooser >}}

A `Stack` object operates within the context of a `Workspace`. A `Workspace` is the execution context containing a single Pulumi project, a program, and multiple stacks. Workspaces are used to manage the execution environment, providing various utilities such as plugin installation, environment configuration (`$PULUMI_HOME`), and creation, deletion, and listing of stacks. Because you are deploying AWS resources in this tutorial, you must install the AWS provider plugin within your `Workspace` so that your Pulumi program will have it available during execution.

## Configure your provider plugins

The AWS plugin also needs configuration. You can provide that configuration just as you would with other Pulumi programs: either through [stack configuration](/docs/concepts/config/) or environment variables. In this tutorial, you'll use the `Stack` object to set the AWS region for the AWS provider plugin.

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}
{{% choosable language "javascript,typescript" %}}

```typescript
await stack.workspace.installPlugin("aws", "v4.0.0");
await stack.setConfig("aws:region", { value: "us-west-2" });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
stack.workspace.install_plugin("aws", "v4.0.0")
stack.set_config("aws:region", auto.ConfigValue(value="us-west-2"))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
err = w.InstallPlugin(ctx, "aws", "v4.0.0")
if err != nil {
  fmt.Printf("Failed to install program plugins: %v\n", err)
  os.Exit(1)
}

s.SetConfig(ctx, "aws:region", auto.ConfigValue{Value: "us-west-2"})
```

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

```csharp
await stack.Workspace.InstallPluginAsync("aws", "v4.0.0");
await stack.SetConfigAsync("aws:region", new ConfigValue("us-west-2"));
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
stack.getWorkspace().installPlugin("aws", "v5.41.0");
stack.setConfig("aws:region", new ConfigValue("us-west-2"));
```

{{% /choosable %}}

{{< /chooser >}}

## Invoke Pulumi commands against the stack

You're now ready to execute commands against the `Stack`, including update, preview, refresh, destroy, import, and export.
If you want to update the stack, invoke the update method (`up`) against the `Stack` object:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}
{{% choosable language "javascript,typescript" %}}

```typescript
const upRes = await stack.up({ onOutput: console.info });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
up_res = stack.up(on_output=print)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
res, err := s.Up(ctx, stdoutStreamer)
if err != nil {
  fmt.Printf("Failed to update stack: %v\n\n", err)
  os.Exit(1)
}
```

{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}

```csharp
var result = await stack.UpAsync(new UpOptions { OnStandardOutput = Console.WriteLine });
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
var result = stack.up(UpOptions.builder().onStandardOutput(System.out::println).build());
```

{{% /choosable %}}

{{< /chooser >}}

Notice how you can choose to have a callback function for standard output. In addition, the command returns a result of the update, which you can programmatically use to drive decisions within your program. For example, the result includes the stack outputs as well as a summary of the changes. This means you could choose to take different actions if there were no resources updated. Conversely, you could use the stack outputs to drive another Pulumi program within the same Automation program.

By now, you've hopefully gained a clearer understanding of how to utilize the Automation API. For additional ideas, see the [Automation API examples](https://github.com/pulumi/automation-api-examples).
