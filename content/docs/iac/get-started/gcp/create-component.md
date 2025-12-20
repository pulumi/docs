---
title_tag: Create a component | Google Cloud
title: Create a component
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview on how to create infrastructure abstractions with Pulumi.
weight: 7
menu:
    iac:
        name: Create a component
        identifier: gcp-get-started.create-component
        parent: gcp-get-started
        weight: 7

aliases:
    - /docs/quickstart/gcp/create-component/
    - /docs/clouds/gcp/get-started/create-component/
---

## Create a component

[**Components**](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate
complexity and enable sharing and reuse. Instead of copy-pasting common patterns, you can encode them as components.

You will now create your first component that packages up your Google Cloud Storage website so you can easily stamp out
entire websites in just a few lines of code:

{{% choosable language typescript %}}

```typescript
const website = new GcpStorageWebsite("my-website", {
    files: [ "index.html" ],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
website = GcpStorageWebsite('my-website', files=['index.html'])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
website, err := NewGcpStorageWebsite(ctx, "my-website", GcpStorageWebsiteArgs{
    Files: []string{"index.html"},
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var website = new GcpStorageWebsite("my-website", new GcpStorageWebsiteArgs()
{
    Files = new[] { "index.html" }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var website = new GcpStorageWebsite("my-website",
    new GcpStorageWebsiteArgs(new String[] { "index.html" }));
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/gcp/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

Using components here also has the benefit that, as the requirements for your static website change, you can
update the one component definition and have all uses of it benefit.

### Define a new component

To define a new component, create a class called `GcpStorageWebsite` that derives from `ComponentResource`. It'll have a mostly-empty
constructor to start with but you will add the Google Cloud Storage resources to it in the next step. You'll also define the inputs for the
component -- the `files` to add to the website -- and outputs -- a single property with the website `url`.

To get going, create a new file {{< compfile >}} alongside {{< langfile >}} and add the following:

{{% choosable language typescript %}}

```typescript
import * as gcp from "@pulumi/gcp";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the Google Cloud Storage static website component.
export interface GcpStorageWebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating a Google Cloud Storage hosted static website.
export class GcpStorageWebsite extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the website url.

    constructor(name: string, args: GcpStorageWebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:GcpStorageWebsite", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs({}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage
from typing import List

# A component that encapsulates creating a Google Cloud Storage hosted static website.
class GcpStorageWebsite(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:GcpStorageWebsite', name, { 'files': files }, opts)

        # Component initialization will go here next...

        self.register_outputs({}) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type GcpStorageWebsite struct {
    pulumi.ResourceState
    Url pulumi.StringOutput // the website url.
}

type GcpStorageWebsiteArgs struct {
    Files []string // a list of files to serve.
}

func NewGcpStorageWebsite(ctx *pulumi.Context, name string, args GcpStorageWebsiteArgs, opts ...pulumi.ResourceOption) (*GcpStorageWebsite, error) {
    self := &GcpStorageWebsite{}
    err := ctx.RegisterComponentResource("quickstart:index:GcpStorageWebsite", name, self, opts...)
    if err != nil {
        return nil, err
    }

    // Component initialization will go here next...

    ctx.RegisterResourceOutputs(self, pulumi.Map{}) // Signal component completion.
    return self, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;
using Pulumi.Gcp.Storage.Inputs;
using System.Collections.Generic;

public class GcpStorageWebsiteArgs
{
    public string[]? Files { get; set; }
}

public class GcpStorageWebsite : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public GcpStorageWebsite(string name, GcpStorageWebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:GcpStorageWebsite", name, opts)
    {
        // Component initialization will go here next...

        this.RegisterOutputs(new Dictionary<string, object>{}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.core.Output;

public class GcpStorageWebsiteArgs {
    public String[] files;
    public GcpStorageWebsiteArgs(String[] files) {
        this.files = files;
    }
}

public class GcpStorageWebsite extends ComponentResource {
    public Output<String> url;

    public GcpStorageWebsite(String name, GcpStorageWebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:GcpStorageWebsite", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs(java.util.Map.of());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/gcp/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

This defines a component but it doesn't do much yet.

### Refactor your code into the component

Next, make four changes:

1. Move all resources from {{< langfile >}} into the component's constructor
2. Change each resource to use the component [as the `parent`](/docs/iac/concepts/options/parent/)
3. Generalize the creation of bucket objects by looping over the list of `files`
4. Assign the resulting website URL to the `url` property of the component

The resulting {{< compfile >}} file will look like this; you can make each edit one at a time if preferred
to get a feel for things, or simply paste the contents of this into {{< compfile >}}:

{{% choosable language typescript %}}

```typescript
import * as gcp from "@pulumi/gcp";
import * as pulumi from "@pulumi/pulumi";

// Arguments for the Google Cloud Storage static website component.
export interface GcpStorageWebsiteArgs {
    files: string[]; // a list of files to serve.
}

// A component that encapsulates creating a Google Cloud Storage hosted static website.
export class GcpStorageWebsite extends pulumi.ComponentResource {
    public readonly url: pulumi.Output<string>; // the website url.

    constructor(name: string, args: GcpStorageWebsiteArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:GcpStorageWebsite", name, args, opts);

        // Create a Google Cloud resource (Storage Bucket) configured for website hosting
        const bucket = new gcp.storage.Bucket("my-bucket", {
            location: "US",
            website: {
                mainPageSuffix: "index.html",
            },
            uniformBucketLevelAccess: true,
        }, {
            parent: this,
        });

        // Allow public access to the objects
        const bucketBinding = new gcp.storage.BucketIAMBinding("my-bucket-binding", {
            bucket: bucket.name,
            role: "roles/storage.objectViewer",
            members: ["allUsers"],
        }, { parent: this });

        // Create a Bucket object for each file
        for (const file of args.files) {
            new gcp.storage.BucketObject(file, {
                bucket: bucket.name,
                name: file,
                source: new pulumi.asset.FileAsset(file),
            }, { parent: this, dependsOn: [bucketBinding] });
        }

        // Capture the URL and make it available as a component property and output:
        this.url = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", args.files[0]);
        this.registerOutputs({ url: this.url }); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage
from typing import List

# A component that encapsulates creating a Google Cloud Storage hosted static website.
class GcpStorageWebsite(pulumi.ComponentResource):
    def __init__(self, name: str, files: List[str] = None, opts = None):
        super().__init__('quickstart:index:GcpStorageWebsite', name, { 'files': files }, opts)

        # Create a Google Cloud resource (Storage Bucket) configured for website hosting
        bucket = storage.Bucket(
            'my-bucket',
            location="US",
            website=\{
                "main_page_suffix": "index.html"
            \},
            uniform_bucket_level_access=True,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Allow public access to the objects
        bucket_binding = storage.BucketIAMBinding(
            "my-bucket-binding",
            bucket=bucket.name,
            role="roles/storage.objectViewer",
            members=["allUsers"],
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create a Bucket object for each file
        for file in files or []:
            storage.BucketObject(
                file,
                bucket=bucket.name,
                name=file,
                source=pulumi.FileAsset(file),
                opts=pulumi.ResourceOptions(parent=self, depends_on=[bucket_binding]),
            )

        # Capture the URL and make it available as a component property and output
        self.url = pulumi.Output.concat(
            "http://storage.googleapis.com/", bucket.name, "/", files[0]
        )
        self.register_outputs({ 'url': self.url }) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type GcpStorageWebsite struct {
    pulumi.ResourceState
    Url pulumi.StringOutput // the website url.
}

type GcpStorageWebsiteArgs struct {
    Files []string // a list of files to serve.
}

func NewGcpStorageWebsite(ctx *pulumi.Context, name string, args GcpStorageWebsiteArgs, opts ...pulumi.ResourceOption) (*GcpStorageWebsite, error) {
    self := &GcpStorageWebsite{}
    err := ctx.RegisterComponentResource("quickstart:index:GcpStorageWebsite", name, self, opts...)
    if err != nil {
        return nil, err
    }

    // Create a Google Cloud resource (Storage Bucket) configured for website hosting
    bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
        Location: pulumi.String("US"),
        Website: storage.BucketWebsiteArgs{
            MainPageSuffix: pulumi.String("index.html"),
        },
        UniformBucketLevelAccess: pulumi.Bool(true),
    }, pulumi.Parent(self))
    if err != nil {
        return nil, err
    }

    // Allow public access to the objects
    bucketBinding, err := storage.NewBucketIAMBinding(ctx, "my-bucket-binding", &storage.BucketIAMBindingArgs{
        Bucket: bucket.Name,
        Role:   pulumi.String("roles/storage.objectViewer"),
        Members: pulumi.StringArray{
            pulumi.String("allUsers"),
        },
    }, pulumi.Parent(self))
    if err != nil {
        return nil, err
    }

    // Create a Bucket object for each file
    for _, file := range args.Files {
        _, err := storage.NewBucketObject(ctx, file, &storage.BucketObjectArgs{
            Bucket: bucket.Name,
            Name:   pulumi.String(file),
            Source: pulumi.NewFileAsset(file),
        }, pulumi.Parent(self), pulumi.DependsOn([]pulumi.Resource{bucketBinding}))
        if err != nil {
            return nil, err
        }
    }

    // Export the website URL
    self.Url = pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, args.Files[0])
    ctx.RegisterResourceOutputs(self, pulumi.Map{"url": self.Url}) // Signal component completion.
    return self, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;
using Pulumi.Gcp.Storage.Inputs;
using System.Collections.Generic;

public class GcpStorageWebsiteArgs
{
    public string[]? Files { get; set; }
}

public class GcpStorageWebsite : Pulumi.ComponentResource
{
    public Output<string> Url { get; private set; }

    public GcpStorageWebsite(string name, GcpStorageWebsiteArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:GcpStorageWebsite", name, opts)
    {
        // Create a Google Cloud resource (Storage Bucket) configured for website hosting
        var bucket = new Bucket("my-bucket", new BucketArgs
        {
            Location = "US",
            Website = new BucketWebsiteArgs
            {
                MainPageSuffix = "index.html"
            },
            UniformBucketLevelAccess = true,
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Allow public access to the objects
        var bucketBinding = new BucketIAMBinding("my-bucket-binding", new BucketIAMBindingArgs
        {
            Bucket = bucket.Name,
            Role = "roles/storage.objectViewer",
            Members = new[]
            {
                "allUsers",
            },
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        // Create a Bucket object for each file
        foreach (var file in args.Files ?? []) {
            new BucketObject(file, new BucketObjectArgs
            {
                Bucket = bucket.Name,
                Name = file,
                Source = new FileAsset(file),
            }, new CustomResourceOptions
            {
                Parent = this,
                DependsOn = { bucketBinding }
            });
        }

        // Capture the URL and make it available as a component property and output
        this.Url = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{args.Files?[0]}");
        this.RegisterOutputs(new Dictionary<string, object?>{
            ["url"] = this.Url
        });
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.asset.FileAsset;
import com.pulumi.resources.*;

import com.pulumi.gcp.storage.*;
import com.pulumi.gcp.storage.inputs.*;

import java.util.Map;

class GcpStorageWebsiteArgs extends ResourceArgs {
    public String[] files;
    public GcpStorageWebsiteArgs(String[] files) {
        this.files = files;
    }
}

class GcpStorageWebsite extends ComponentResource {
    public Output<String> url;

    public GcpStorageWebsite(String name, GcpStorageWebsiteArgs args) {
        this(name, args, null);
    }

    public GcpStorageWebsite(String name, GcpStorageWebsiteArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:GcpStorageWebsite", name, args, opts);

        // Create a Google Cloud resource (Storage Bucket) configured for website hosting
        var bucket = new Bucket("my-bucket", BucketArgs.builder()
            .location("US")
            .website(BucketWebsiteArgs.builder()
                .mainPageSuffix("index.html")
                .build())
            .uniformBucketLevelAccess(true)
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Allow public access to the objects
        var bucketBinding = new BucketIAMBinding("my-bucket-binding", BucketIAMBindingArgs.builder()
            .bucket(bucket.name())
            .role("roles/storage.objectViewer")
            .members("allUsers")
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Create a Bucket object for each file
        for (var file : args.files) {
            new BucketObject(file, BucketObjectArgs.builder()
                .bucket(bucket.name())
                .name(file)
                .source(new FileAsset(file))
                .build(), CustomResourceOptions.builder()
                    .parent(this)
                    .dependsOn(bucketBinding)
                    .build());
        }

        // Capture the URL and make it available as a component property and output
        this.url = Output.format("http://storage.googleapis.com/%s/%s", bucket.name(), args.files[0]);
        this.registerOutputs(Map.of("url", this.url));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/gcp/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Instantiate the component

Now go back to your original file {{< langfile >}}. Now that you have moved all of the resources, you can start over with a clean slate.
Ensure the file is empty and we will build it back up by simply importing and instantiating our new component.

Add this to your now-empty {{< langfile >}}:

{{% choosable language typescript %}}

```typescript
// Import from our new component module:
import { GcpStorageWebsite } from "./website";

// Create an instance of our component with the same files as before:
const website = new GcpStorageWebsite("my-website", {
    files: [ "index.html" ],
});

// And export its autoassigned URL:
export const url = website.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

# Import from our new component module:
from website import GcpStorageWebsite

# Create an instance of our component with the same files as before:
website = GcpStorageWebsite('my-website', files=['index.html'])

# And export its autoassigned URL:
pulumi.export("url", website.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an instance of our component with the same files as before:
        website, err := NewGcpStorageWebsite(ctx, "my-website", GcpStorageWebsiteArgs{
            Files: []string{"index.html"},
        })
        if err != nil {
            return err
        }

        // And export its autoassigned URL:
        ctx.Export("url", website.Url)
        return nil
    })
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Create an instance of our component with the same files as before:
    var website = new GcpStorageWebsite("my-website", new GcpStorageWebsiteArgs()
    {
        Files = new[] { "index.html" }
    });

   // And export its autoassigned URL:
   return new Dictionary<string, object?>
   {
      ["url"] = website.Url
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an instance of our component with the same files as before:
            var website = new GcpStorageWebsite("my-website",
                new GcpStorageWebsiteArgs(new String[] { "index.html" }));

            // And export its autoassigned URL:
            ctx.export("url", website.url);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/gcp/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Deploy the component

Now deploy the resulting component instantiation. To do so, run `pulumi up` as usual:

```
$ pulumi up
Previewing update (dev)

     Type                                   Name                  Plan
     pulumi:pulumi:Stack                    quickstart-dev
 +   ├─ quickstart:index:GcpStorageWebsite  my-website            create
 +   │  ├─ gcp:storage:Bucket               my-bucket             create
 +   │  ├─ gcp:storage:BucketObject         index.html            create
 +   │  └─ gcp:storage:BucketIAMBinding     my-bucket-binding     create
 -   ├─ gcp:storage:BucketIAMBinding        my-bucket-binding     delete
 -   ├─ gcp:storage:Bucket                  my-bucket             delete
 -   └─ gcp:storage:BucketObject            index.html            delete

Outputs:
  - bucketName: "gs://my-bucket-a2b3c4d"
  ~ url       : "http://storage.googleapis.com/my-bucket-a2b3c4d/index.html-07d2e19" => "http://storage.googleapis.com/my-bucket-297424e/index.html"

Resources:
    + 4 to create
    - 3 to delete
    7 changes. 1 unchanged

Do you want to perform this update?  [Use arrows to move, type to filter]
> yes
  no
  details
```

This preview shows you a few things. First, you'll see our `GcpStorageWebsite` component with all of its children resources neatly parented underneath it. This helps to see what resources relate to which components. Next, you'll see that your old resources are being destroyed.

{{% notes type="info" %}}

If you're wondering why Pulumi didn't simply update the resources in place, it's because certain changes -- like
refactoring resources into a component -- fundamentally change a resource's identity. Many changes like updating
properties or moving resources between files are not disruptive like this. It such cases, you can assign
[aliases](/docs/iac/concepts/options/aliases/) to prevent deletions from happening.

{{% /notes %}}

Accept the changes by selecting `yes` and the deployment will occur:

```
Updating (dev)

     Type                                   Name                  Status
     pulumi:pulumi:Stack                    quickstart-dev
 +   ├─ quickstart:index:GcpStorageWebsite  my-website            created (3s)
 +   │  ├─ gcp:storage:Bucket               my-bucket             created (1s)
 +   │  ├─ gcp:storage:BucketIAMBinding     my-bucket-binding     created (4s)
 +   │  └─ gcp:storage:BucketObject         index.html            created (0.74s)
 -   ├─ gcp:storage:BucketIAMBinding        my-bucket-binding     deleted (4s)
 -   ├─ gcp:storage:BucketObject            index.html            deleted (0.92s)
 -   └─ gcp:storage:Bucket                  my-bucket             deleted (1s)

Outputs:
  - bucketName: "gs://my-bucket-a2b3c4d"
  ~ url       : "http://storage.googleapis.com/my-bucket-a2b3c4d/index.html-07d2e19" => "http://storage.googleapis.com/my-bucket-297424e/index.html"

Resources:
    + 4 created
    - 3 deleted
    7 changes. 1 unchanged

Duration: 10s
```

Now test out your new website -- it works like before, just with a tidier codebase now!

{{% choosable os "linux,macos" %}}

```bash
$ curl $(pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> curl (pulumi stack output url)
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

{{% /choosable %}}

Once you are ready to move on, let's destroy everything we've spun up in this tutorial.

{{< get-started-stepper >}}
