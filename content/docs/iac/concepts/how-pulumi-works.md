---
title_tag: How Pulumi Works
meta_desc: This page provides an overview of how Pulumi works and interacts with different Cloud Providers like AWS, Azure, Kubernetes, and more.
title: How Pulumi works
h1: How Pulumi works
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: How Pulumi works
        weight: 10
        parent: iac-concepts
    concepts:
        weight: 1
aliases:
    - /docs/reference/how/
    - /docs/tour/basics-programs/
    - /docs/tour/programs-packages/
    - /docs/tour/programs-properties/
    - /docs/tour/programs-resources/
    - /docs/tour/programs-stacks/
    - /docs/intro/concepts/how-pulumi-works/
    - /docs/concepts/how-pulumi-works/
---

Pulumi uses a desired state (declarative) model for orchestrating and managing infrastructure with the flexibility to author your infrastructure code using programming languages you know such as TypeScript, Javascript, Python, Go, C#, and Java. This model provides the advantages of programming structures like loops, conditionals and functions as well as your IDE with autocomplete, type checking, and documentation. When you author a Pulumi program the end result will be the state you declare, regardless of the current state of your infrastructure.

A Pulumi program is executed by a _language host_ to compute a desired state for a stack's infrastructure. The _deployment engine_ compares this desired state with the stack's current state and determines what resources need to be created, updated or deleted. The engine uses a set of _resource providers_ (such as [AWS](/docs/clouds/aws/get-started/), [Azure](/docs/clouds/azure/get-started/), [Kubernetes](/docs/iac/get-started/kubernetes/), and [+150 more](/registry/)) in order to manage the individual resources.  As it operates, the engine updates the _state_ of your infrastructure with information about all resources that have been provisioned as well as any pending operations.

The following diagram illustrates the interaction between these parts of the system:

<img src="/images/docs/reference/engine-block-diagram.png" alt="Pulumi IaC system architecture, the Pulumi engine and providers" width="600">

In the next section, we will describe each of these components and see how they all fit together during an invocation of `pulumi up`.

## Language hosts

The _language host_ is responsible for running a Pulumi program and setting up an environment where it can register resources with the _deployment engine_. The language host consists of two different pieces:

1. A language executor, which is a binary named `pulumi-language-<language-name>`, that Pulumi uses to launch the runtime for the language your program is written in (e.g. Node or Python). This binary is distributed with the Pulumi CLI.
2. A language SDK is responsible for preparing your program to be executed and observing its execution in order to detect resource registrations. When a resource is _registered_ (via `new Resource()` in JavaScript or `Resource(...)` in Python), the language SDK communicates the registration request back to the _deployment engine_. The language SDK is distributed as a regular package, just like any other code that might depend on your program. For example, the Node SDK is contained in the [`@pulumi/pulumi`](https://www.npmjs.com/package/@pulumi/pulumi) package available on npm, and the Python SDK is contained in the [`pulumi`](https://pypi.org/project/pulumi/) package available on PyPI.

## Deployment engine

The _deployment engine_ is responsible for computing the set of operations needed to drive the current state of your infrastructure into the desired state expressed by your program. When a _resource registration_ is received from the language host, the engine consults the existing state to determine if that resource has been created before. If it has not, the engine uses a _resource provider_ to create it. If it already exists, the engine works with the resource provider to determine what, if anything, has changed by comparing the old state of the resource with the new desired state of the resource as expressed by the program. If there are changes, the engine determines if it can _update_ the resource in place or if it must _replace_ it by _creating_ a new version and _deleting_ the old version. The decision depends on what properties of the resource are changing and the type of the resource itself. When the language host communicates to the engine that it has completed the execution of the Pulumi program, the engine looks for any existing resources that it did not see a new resource registration and schedules these resources for deletion.

The deployment engine is embedded in the `pulumi` CLI itself.

## Resource providers

A resource provider is made up of two different pieces:

1. A _resource plugin_ is the binary used by the deployment engine to manage a resource. These plugins are stored in the _plugin cache_ (located in `~/.pulumi/plugins`) and can be managed using the [`pulumi plugin`](/docs/cli/commands/pulumi_plugin) set of commands.
2. An _SDK_ which provides bindings for each type of resource the provider can manage.

Like the language runtime itself, the SDKs are available as regular packages. For example, there is a [`@pulumi/aws`](https://www.npmjs.com/package/@pulumi/aws) package for Node available on npm and a [`pulumi_aws`](https://pypi.org/project/pulumi-aws) package for Python available on PyPI.  When these packages are added to your project, they run [`pulumi plugin install`](/docs/cli/commands/pulumi_plugin_install) behind the scenes to download the resource plugin from Pulumi.com.

## Putting it all together

Let's walk through a simple example. Suppose we have the following Pulumi program, which creates two S3 buckets:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const aws = require("@pulumi/aws");

const mediaBucket = new aws.s3.BucketV2("media-bucket");
const contentBucket = new aws.s3.BucketV2("content-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const mediaBucket = new aws.s3.BucketV2("media-bucket");
const contentBucket = new aws.s3.BucketV2("content-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_aws import s3

media_bucket = s3.BucketV2('media-bucket')
content_bucket = s3.BucketV2('content-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		mediaBucket, err := s3.NewBucketV2(ctx, "media-bucket", nil)
		if err != nil {
			return err
		}
		contentBucket, err := s3.NewBucketV2(ctx, "content-bucket", nil)
		if err != nil {
			return err
		}
		ctx.Export("contentBucket", contentBucket.ID())
		ctx.Export("mediaBucket", mediaBucket.ID())
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var mediaBucket = new Aws.S3.BucketV2("media-bucket");
    var contentBucket = new Aws.S3.BucketV2("content-bucket");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.s3.BucketV2;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var mediaBucket = new BucketV2("media-bucket");
            var contentBucket = new BucketV2("content-bucket");
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: my-yaml-project
runtime: yaml
resources:
    mediaBucket:
        type: aws:s3:BucketV2
    contentBucket:
        type: aws:s3:BucketV2
```

{{% /choosable %}}

{{< /chooser >}}

Now, we run `pulumi stack init mystack`. Since `mystack` is a new stack, the "last deployed state" has no resources.

Next, we run `pulumi up`. Since this program is written in {{% pulumi-language %}}, the Pulumi CLI launches the {{% pulumi-host %}} language host and requests that it execute the program. When the first {{% pulumi-bucket %}} object is constructed, the language host sends a _resource registration_ request to the deployment engine and then continues executing the program. This is subtle, but important: _When the call to_ {{% pulumi-new-bucket %}} _returns, it does not mean that the actual S3 bucket has been created in AWS_, it just means the language host has expressed that this bucket is part of the desired state of your infrastructure.  The language host continues to execute your program concurrently with the engine processing this request.

In this case, since the last deployed state has no resources, the engine determines that it needs to create the `media-bucket` resource. It uses the AWS resource plugin in order to create the resource and the AWS resource plugin uses the AWS SDK in order to go create it.  Note that the engine does not talk directly to AWS, instead it just asks the AWS Resource Plugin to create a Bucket. As new resource types are added, you can update the version of a resource provider to gain access to these new resources without having to update the CLI itself. When the operation to create this bucket is complete, the engine records information about the newly created resource in its state file.

As the engine was creating the `media-bucket` bucket, the language host continued to execute the Pulumi program. This caused another resource registration to be generated (for `content-bucket`). Since there is no dependency between these two buckets, the engine is able to process that request in parallel with the creation of `media-bucket`.

After both operations have completed, the language host exits as the program has finished running. Then the engine and resource providers shutdown. The state for mystack now looks like the following:

```
stack mystack
   - aws.s3.BucketV2 "media-bucket653a4"
   - aws.s3.BucketV2 "content-bucket125ce"
```

Note the extra suffixes on the end of these bucket names. This is due to a process called [auto-naming](/docs/concepts/resources/names/#autonaming), which Pulumi uses by default in order to allow you to deploy multiple copies of your infrastructure without creating name collisions for resources. This behavior can be disabled if desired.

Now, let's make a change to one of resources and run `pulumi up` again.  Since Pulumi operates on a desired state model, it will use the last deployed state to compute the minimal set of changes needed to update your deployed infrastructure. For example, imagine that we wanted to add tags to the S3 `media-bucket`.  We change our program to express this new desired state:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const aws = require("@pulumi/aws");

const mediaBucket = new aws.s3.BucketV2("media-bucket", {
    tags: {"owner": "media-team"},
});
const contentBucket = new aws.s3.BucketV2("content-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const mediaBucket = new aws.s3.BucketV2("media-bucket", {
    tags: {"owner": "media-team"},
});
const contentBucket = new aws.s3.BucketV2("content-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_aws import s3

media_bucket = s3.BucketV2('media-bucket', tags={'owner': 'media-team'})
content_bucket = s3.BucketV2('content-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		mediaBucket, err := s3.NewBucketV2(ctx, "mediaBucket", &s3.BucketV2Args{
			Tags: pulumi.StringMap{
				"owner": pulumi.String("media-team"),
			},
		})
		if err != nil {
			return err
		}
		contentBucket, err := s3.NewBucketV2(ctx, "contentBucket", nil)
		if err != nil {
			return err
		}
		ctx.Export("contentBucket", contentBucket.ID())
		ctx.Export("mediaBucket", mediaBucket.ID())
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var mediaBucket = new Aws.S3.BucketV2("media-bucket", new()
    {
        Tags =
        {
            { "owner", "media-team" },
        },
    }););
    var contentBucket = new Aws.S3.BucketV2("content-bucket");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import java.util.Map;
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.aws.s3.BucketV2Args;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var mediaBucket = new BucketV2("mediaBucket", BucketV2Args.builder()
                .tags(Map.of("owner", "media-team"))
                .build());
            var contentBucket = new BucketV2("content-bucket");
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: my-yaml-project
runtime: yaml
resources:
  mediaBucket:
    type: aws:s3:BucketV2
    properties:
      tags:
        owner: media-team
  contentBucket:
    type: aws:s3:BucketV2
```

{{% /choosable %}}

{{< /chooser >}}

When you run `pulumi preview` or `pulumi up`, the entire process starts over.  The language host starts running your program and the call to aws.s3.BucketV2 causes a new resource registration request to be sent to the engine. This time, however, our state already contains a resource named `media-bucket`, so engine asks the resource provider to compare the existing state from our previous run of `pulumi up` with the desired state expressed by the program. The process detects that the `tags` property has changed from empty to a map assigning the `owner` tag. By again consulting the resource provider the engine determines that it is able to update this property without creating a new bucket, and so it tells the provider to update the `tags` property to set the `owner` tag. When this operation completes, the current state is updated to reflect the change that had been made.

The engine also receives a resource registration request for "content-bucket".  However, since there are no changes between the current state and the desired state, the engine does not need to make any changes to the resource.

Now, suppose we rename `content-bucket` to `app-bucket`.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const aws = require("@pulumi/aws");
const mediaBucket = new aws.s3.BucketV2("media-bucket", {
    tags: {"owner": "media-team"},
});
const appBucket = new aws.s3.BucketV2("app-bucket");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const mediaBucket = new aws.s3.BucketV2("media-bucket", {
    tags: {"owner": "media-team"},
});
const appBucket = new aws.s3.BucketV2("app-bucket");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_aws import s3

media_bucket = s3.BucketV2('media-bucket', tags={'owner': 'media-team'})
app_bucket = s3.BucketV2('app-bucket')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		mediaBucket, err := s3.NewBucketV2(ctx, "mediaBucket", &s3.BucketV2Args{
			Tags: pulumi.StringMap{
				"owner": pulumi.String("media-team"),
			},
		})
		if err != nil {
			return err
		}
		appBucket, err := s3.NewBucketV2(ctx, "appBucket", nil)
		if err != nil {
			return err
		}
		ctx.Export("appBucket", appBucket.ID())
		ctx.Export("mediaBucket", mediaBucket.ID())
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var mediaBucket = new Aws.S3.BucketV2("media-bucket", new()
    {
        Tags =
        {
            { "owner", "media-team" },
        },
    }););
    var appBucket = new Aws.S3.BucketV2("app-bucket");
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import java.util.Map;
import com.pulumi.Pulumi;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.aws.s3.BucketV2Args;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var mediaBucket = new BucketV2("mediaBucket", BucketV2Args.builder()
                .tags(Map.of("owner", "media-team"))
                .build());
            var appBucket = new BucketV2("appBucket");
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: my-yaml-project
runtime: yaml
resources:
  mediaBucket:
    type: aws:s3:BucketV2
    properties:
      tags:
        owner: media-team
  appBucket:
    type: aws:s3:BucketV2
```

{{% /choosable %}}

{{< /chooser >}}

This time, the engine will not need to make any changes to `media-bucket` since its desired state matches its actual state. However, when the resource request for `app-bucket` is processed, the engine sees there's no existing resource named `app-bucket` in the current state so it must create a new S3 bucket. Once that process is complete and the language host has shut down, the engine looks for any resources in the current state which it did not see a resource registration for. In this case, since we removed the registration of `content-bucket` from our program, the engine calls the resource provider to delete the existing `content-bucket` bucket.

## Creation and deletion order

Pulumi executes resource operations in parallel whenever possible, but understands that some resources may have dependencies on other resources. If an [output](/docs/concepts/inputs-outputs/) of one resource is provided as an input to another, the engine records the dependency between these two resources as part of the state and uses these when scheduling operations. This list can also be augmented by using the [dependsOn](/docs/concepts/resources#dependson) resource option.

By default, if a resource must be replaced, Pulumi will attempt to create a new copy of the resource before destroying the old one. This is helpful because it allows updates to infrastructure to happen without downtime. This behavior can be controlled by the [deleteBeforeReplace](/docs/concepts/resources#deletebeforereplace) option. If you have disabled [auto-naming](/docs/concepts/resources/names/#autonaming) using configuration or by providing a specific name for a resource, it will be treated as if it was marked as `deleteBeforeReplace` automatically (otherwise the create operation for the new version would fail since the name is in use).

## Declarative and imperative approach

With Pulumi, you author your infrastructure in your preferred programming language. When you run `pulumi up`, the Pulumi CLI starts both language host for your selected programming language as well as the required providers (via the Pulumi engine). The providers, coordinated by the Pulumi engine, are the ones that perform the actual creation, modification, or deletion of your infrastructure. The separation of language support from the engine is what makes Pulumi so powerful, providing the best of both imperative and declarative approaches for your infrastructure as code solutions.

Here is a breakdown of each component of Pulumi's architecture:

* Language host: `imperative` (JavaScript/TypeScript, Go, Python, C#/F#/.NET, Java) and declarative (YAML)
* Pulumi engine: `declarative`
* Providers: `imperative`
