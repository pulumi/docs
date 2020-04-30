---
title: "How Pulumi Works"
meta_desc: This page provides an overview of how Pulumi works and interacts with different
           Cloud Providers.
menu:
  intro:
    parent: concepts
    weight: 7

aliases: ["/docs/reference/how/"]
---

Pulumi uses a desired state model for managing infrastructure. A Pulumi program is executed by a _language host_ to compute a desired state for a stack's infrastructure. The _deployment engine_ compares this desired state with the stack's current state and determines what resources need to be created, updated or deleted. The engine uses a set of _resource providers_ (such as [AWS]({{< prelref "/docs/get-started/aws" >}}), [Azure]({{< prelref "/docs/get-started/azure" >}}), [Kubernetes]({{< prelref "/docs/get-started/kubernetes" >}}), and so on.) in order to manage the individual resources.  As it operates, the engine updates the _state_ of your infrastructure with information about all resources that have been provisioned as well as any pending operations.

The following diagram illustrates the interaction between these parts of the system:

<img src="/images/docs/reference/engine-block-diagram.png" alt="Pulumi engine and providers" width="600">

In the next section, we will describe each of these components and see how they all fit together during an invocation of `pulumi up`.

## Language Hosts

The _language host_ is responsible for running a Pulumi program and setting up an environment where it can register resources with the _deployment engine_.  The language host is made up of two different pieces:

1. A language executor, which is a binary named `pulumi-language-<language-name>`, that Pulumi uses to launch the runtime for the the language your program is written in (e.g. Node or Python). This binary is distributed with the Pulumi CLI.
2. A language runtime, which is responsible for preparing your program to be executed and observes its execution in order to detect resource registrations.  When a resource is _registered_ (via `new Resource()` in JavaScript or `Resource(...)` in Python), the language runtime communicates the registration request back to the _deployment engine_. The language runtime is distributed as a regular package, just like any other code that might depend on your program.  For example, the Node runtime is contained in the [`@pulumi/pulumi`](https://www.npmjs.com/package/@pulumi/pulumi) package available on npm, and the Python runtime is contained in the [`pulumi`](https://pypi.org/project/pulumi/) package available on PyPI.

## Deployment Engine

The _deployment engine_ is responsible for computing the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program.  When a _resource registration_ is received from the language host, the engine consults the existing state to determine if that resource has been created before. If it has not, the engine uses a _resource provider_ in order to create it.  If it already exists, the engine works with the resource provider to determine what, if anything, has changed by comparing the old state of the resource with the new desired state of the resource as expressed by the program. If there are changes, the engine determines if it can _update_ the resource in place or if it must _replace_ it by _creating_ a new version and _deleting_ the old version. The decision depends on what properties of the resource are changing and the type of the resource itself.  When the language host communicates to the engine that it has completed execution of the Pulumi program, the engine looks for any existing resources that it did not see a new resource registration for and schedules these resources for deletion.

The deployment engine is embedded in the `pulumi` CLI itself.

## Resource Providers

A resource provider is made up of two different pieces:

1. A _resource plugin_, which is the binary used by the deployment engine to manage a resource. These plugins are stored in the _plugin cache_ (located in `~/.pulumi/plugins`) and can be managed using the [`pulumi plugin`]({{< prelref "/docs/reference/cli/pulumi_plugin" >}}) set of commands.
2. An _SDK_ which provides bindings for each type of resource the provider can manage.

Like the language runtime itself, the SDKs are available as regular packages.  For example, there is a [`@pulumi/aws`](https://www.npmjs.com/package/@pulumi/aws) package for Node available on npm and a [`pulumi_aws`](https://pypi.org/project/pulumi-aws) package for Python available on PyPI.  When these packages are added to your project, they run [`pulumi plugin install`]({{< prelref "/docs/reference/cli/pulumi_plugin_install" >}})  behind the scenes in order to download the resource plugin from pulumi.com.

## Putting it all together

Let's walk through a simple example. Suppose we have the following Pulumi program, which creates two S3 buckets:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mediaBucket = new aws.s3.Bucket("media-bucket");
const contentBucket = new aws.s3.Bucket("content-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const mediaBucket = new aws.s3.Bucket("media-bucket");
const contentBucket = new aws.s3.Bucket("content-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
media_bucket = s3.Bucket('media-bucket')
content_bucket = s3.Bucket('content-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
mediaBucket, _ := s3.NewBucket(ctx, "media-bucket", nil)
contentBucket, _ := s3.NewBucket(ctx, "content-bucket", nil)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Aws = Pulumi.Aws;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

public MyStack : Stack
{
    public MyStack()
    {
        var mediaBucket = new Aws.S3.Bucket("media-bucket");
        var contentBucket = new Aws.S3.Bucket("content-bucket");
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Now, we run `pulumi stack init mystack`. Since `mystack` is a new stack, the "last deployed state" has no resources.

Next, we run `pulumi up`. Since this program is written in JavaScript, the Pulumi CLI launches the Node language host and requests that it execute the program. When the first `aws.s3.Bucket` object is constructed, the language host sends a _resource registration_ request to the deployment engine and then continues executing the program. This is subtle, but important: _When the call to `new aws.s3.Bucket` returns, it does not mean that the actual S3 bucket has been created in AWS_, it just means the language host has expressed that this bucket is part of the desired state of your infrastructure.  The language host continues to execute your program concurrently with the engine processing this request.

In this case, since the last deployed state has no resources, the engine determines that it needs to create the `media-bucket` resource. It uses the AWS resource plugin in order to create the resource and the AWS resource plugin uses the AWS SDK in order to go create it.  Note that the engine does not talk directly to AWS, instead it just asks the AWS Resource Plugin to create a Bucket. As new resource types are added, you can simply update the version of a resource provider to gain access to these new resources without having to update the CLI itself. When the operation to create this bucket is complete, the engine records information about the newly created resource in its state file.

As the engine was creating the `media-bucket` bucket, the language host continued to execute the Pulumi program. This caused another resource registration to be generated (for `content-bucket`). Since there is no dependency between these two buckets, the engine is able to process that request in parallel with the creation of `media-bucket`.

After both operations have completed, the language host exits as the program has finished running. Then the engine and resource providers shutdown. The state for mystack now looks like the following:

```
stack mystack
   - aws.s3.Bucket "media-bucket653a4"
   - aws.s3.Bucket "content-bucket125ce"
```

Note the extra suffixes on the end of these bucket names. This is due to a process called [auto-naming]({{< prelref "/docs/intro/concepts/programming-model#autonaming" >}}), which Pulumi uses by default in order to allow you to deploy multiple copies of your infrastructure without creating name collisions for resources. This behavior can be disabled if desired.

Now, let's make a change to one of resources and run `pulumi up` again.  Since Pulumi operates on a desired state model, it will use the last deployed state to compute the minimal set of changes needed to update your deployed infrastructure. For example, imagine that we wanted to make the S3 `media-bucket` publicly readable.  We change our program to express this new desired state:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mediaBucket = new aws.s3.Bucket("media-bucket", {
    acl: "public-read",   // add acl
});
const contentBucket = new aws.s3.Bucket("content-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const mediaBucket = new aws.s3.Bucket("media-bucket", {
    acl: "public-read",   // add acl
});
const contentBucket = new aws.s3.Bucket("content-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
media_bucket = s3.Bucket('media-bucket', acl="public-read") # add acl
content_bucket = s3.Bucket('content-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
mediaBucket, _ := s3.NewBucket(ctx, "media-bucket", &s3.BucketArgs{Acl: "public-read"}) // add acl
contentBucket, _ := s3.NewBucket(ctx, "content-bucket", nil)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Aws = Pulumi.Aws;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

public MyStack : Stack
{
    public MyStack()
    {
        var mediaBucket = new Aws.S3.Bucket("media-bucket", new Aws.S3.BucketArgs
        {
            Acl = "public-read",   // add acl
        });
        var contentBucket = new Aws.S3.Bucket("content-bucket");
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

When you run `pulumi preview` or `pulumi up`, the entire process starts over.  The language host starts running your program and the call to aws.s3.Bucket causes a new resource registration request to be sent to the engine. This time, however, our state already contains a resource named `media-bucket`, so engine asks the resource provider to compare the existing state from our previous run of `pulumi up` with the desired state expressed by the program. The process detects that the `acl` property has changed from `private` (the default value) to `public-read`. By again consulting the resource provider the engine determines that it is able to update this property without creating a new bucket, and so it tells the provider to update the acl property to `public-read`. When this operation completes, the current state is updated to reflect the change that had been made.

The engine also receives a resource registration request for "content-bucket".  However, since there are no changes between the current state and the desired state, the engine does not need to make any changes to the resource.

Now, suppose we rename `content-bucket` to `app-bucket`.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mediaBucket = new aws.s3.Bucket("media-bucket", {
    acl: "public-read",   // add acl
});
const appBucket = new aws.s3.Bucket("app-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const mediaBucket = new aws.s3.Bucket("media-bucket", {
    acl: "public-read",   // add acl
});
const appBucket = new aws.s3.Bucket("app-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
media_bucket = s3.Bucket('media-bucket', acl="public-read") # add acl
app_bucket = s3.Bucket('app-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
mediaBucket, _ := s3.NewBucket(ctx, "media-bucket", &s3.BucketArgs{Acl: "public-read"}) // add acl
appBucket, _ := s3.NewBucket(ctx, "app-bucket", nil)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Aws = Pulumi.Aws;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

public MyStack : Stack
{
    public MyStack()
    {
        var mediaBucket = new Aws.S3.Bucket("media-bucket", new Aws.S3.BucketArgs
        {
            Acl = "public-read",   // add acl
        });
        var contentBucket = new Aws.S3.Bucket("app-bucket");
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

This time, the engine will not need to make any changes to `media-bucket` since its desired state matches its actual state. However, when the resource request for `app-bucket` is processed, the engine sees there's no existing resource named `app-bucket` in the current state and so it must create a new S3 bucket.  Once that process is complete and the language host has shut down, the engine looks for any resources in the current state which it did not see a resource registration for. In this case, since we removed the registration of `content-bucket` from our program, the engine calls the resource provider to delete the existing `content-bucket` bucket.

## Creation and Deletion Order

Pulumi executes resource operations in parallel whenever possible, but understands that some resources may have dependencies on other resources.  If an [output]({{< prelref "/docs/intro/concepts/programming-model#outputs" >}}) of one resource is provided as an input to another, the engine records the dependency between these two resources as part of the state and uses these when scheduling operations.  This list can also be augmented by using the [dependsOn]({{< prelref "/docs/intro/concepts/programming-model#dependson" >}}) resource option.

By default, if a resource must be replaced, Pulumi will attempt to create a new copy the the resource before destroying the old one. This is helpful because it allows updates to infrastructure to happen without downtime. This behavior can be controlled by the [deleteBeforeReplace]({{< prelref "/docs/intro/concepts/programming-model#deletebeforereplace" >}}) option. If you have disabled [auto-naming]({{< prelref "/docs/intro/concepts/programming-model#autonaming" >}}) by providing a specific name for a resource, it will be treated as if it was marked as `deleteBeforeReplace` automatically (otherwise the create operation for the new version would fail since the name is in use).
