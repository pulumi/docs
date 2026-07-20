---
title_tag: Modify the Program | Google Cloud
title: Modify the program
h1: "Modify the program"
meta_desc: This page provides an overview on how to update a Google Cloud project from a Pulumi program.
weight: 7
menu:
    iac:
        name: Modify the program
        identifier: gcp-get-started.modify-program
        parent: gcp-get-started
        weight: 7
aliases:
    - /docs/quickstart/gcp/modify-program/
    - /docs/clouds/gcp/get-started/modify-program/
---

Now you'll turn the bucket into a static website.

In your project directory, create a file named `index.html` with the following content:

```html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

To turn the bucket into a website, you'll configure it for web hosting and add two new resources:

- A [`BucketObject`](/registry/packages/gcp/api-docs/storage/bucketobject/) for the HTML file
- A [`BucketIAMBinding`](/registry/packages/gcp/api-docs/storage/bucketiambinding/) to make the bucket's contents publicly readable

Open {{< langfile >}} and replace it with the following code:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a storage bucket and configure it as a website
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    website: {
        mainPageSuffix: "index.html",
    },
    uniformBucketLevelAccess: true,
});

// Upload index.html to the bucket
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    name: "index.html",
    source: new pulumi.asset.FileAsset("index.html"),
});

// Make the bucket's contents publicly readable
const bucketBinding = new gcp.storage.BucketIAMBinding("my-bucket-binding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"],
});

// Export the bucket's name and website URL
export const bucketName = bucket.url;
export const url = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage

# Create a storage bucket and configure it as a website
bucket = storage.Bucket(
    "my-bucket",
    location="US",
    website={
        "main_page_suffix": "index.html",
    },
    uniform_bucket_level_access=True,
)

# Upload index.html to the bucket
bucket_object = storage.BucketObject(
    "index.html",
    bucket=bucket.name,
    name="index.html",
    source=pulumi.FileAsset("index.html"),
)

# Make the bucket's contents publicly readable
bucket_iam_binding = storage.BucketIAMBinding(
    "my-bucket-binding",
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)

# Export the bucket's name and website URL
pulumi.export("bucket_name", bucket.url)
pulumi.export(
    "url",
    pulumi.Output.concat("http://storage.googleapis.com/", bucket.id, "/", bucket_object.name),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-gcp/sdk/v7/go/gcp/storage"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a storage bucket and configure it as a website
		bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
			Location: pulumi.String("US"),
			Website: storage.BucketWebsiteArgs{
				MainPageSuffix: pulumi.String("index.html"),
			},
			UniformBucketLevelAccess: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Upload index.html to the bucket
		bucketObject, err := storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
			Bucket: bucket.Name,
			Name:   pulumi.String("index.html"),
			Source: pulumi.NewFileAsset("index.html"),
		})
		if err != nil {
			return err
		}

		// Make the bucket's contents publicly readable
		_, err = storage.NewBucketIAMBinding(ctx, "my-bucket-binding", &storage.BucketIAMBindingArgs{
			Bucket: bucket.Name,
			Role:   pulumi.String("roles/storage.objectViewer"),
			Members: pulumi.StringArray{
				pulumi.String("allUsers"),
			},
		})
		if err != nil {
			return err
		}

		// Export the bucket's name and website URL
		ctx.Export("bucketName", bucket.Url)
		ctx.Export("url", pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, bucketObject.Name))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Gcp.Storage;
using Pulumi.Gcp.Storage.Inputs;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Create a storage bucket and configure it as a website
    var bucket = new Bucket("my-bucket", new BucketArgs
    {
        Location = "US",
        Website = new BucketWebsiteArgs
        {
            MainPageSuffix = "index.html",
        },
        UniformBucketLevelAccess = true,
    });

    // Upload index.html to the bucket
    var bucketObject = new BucketObject("index.html", new BucketObjectArgs
    {
        Bucket = bucket.Name,
        Name = "index.html",
        Source = new FileAsset("./index.html"),
    });

    // Make the bucket's contents publicly readable
    var bucketBinding = new BucketIAMBinding("my-bucket-binding", new BucketIAMBindingArgs
    {
        Bucket = bucket.Name,
        Role = "roles/storage.objectViewer",
        Members = new[]
        {
            "allUsers",
        },
    });

    // Export the bucket's name and website URL
    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Url,
        ["url"] = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{bucketObject.Name}"),
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.asset.FileAsset;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;
import com.pulumi.gcp.storage.BucketIAMBinding;
import com.pulumi.gcp.storage.BucketIAMBindingArgs;
import com.pulumi.gcp.storage.BucketObject;
import com.pulumi.gcp.storage.BucketObjectArgs;
import com.pulumi.gcp.storage.inputs.BucketWebsiteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a storage bucket and configure it as a website
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .location("US")
                .website(BucketWebsiteArgs.builder()
                    .mainPageSuffix("index.html")
                    .build())
                .uniformBucketLevelAccess(true)
                .build());

            // Upload index.html to the bucket
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.name())
                .name("index.html")
                .source(new FileAsset("index.html"))
                .build());

            // Make the bucket's contents publicly readable
            var bucketBinding = new BucketIAMBinding("my-bucket-binding", BucketIAMBindingArgs.builder()
                .bucket(bucket.name())
                .role("roles/storage.objectViewer")
                .members("allUsers")
                .build());

            // Export the bucket's name and website URL
            ctx.export("bucketName", bucket.url());
            ctx.export("url", Output.format("http://storage.googleapis.com/%s/%s", bucket.name(), bucketObject.name()));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal Google Cloud Pulumi YAML program

resources:
  # Create a storage bucket and configure it as a website
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US
      website:
        mainPageSuffix: index.html
      uniformBucketLevelAccess: true

  # Upload index.html to the bucket
  index-html:
    type: gcp:storage:BucketObject
    properties:
      bucket: ${my-bucket.name}
      name: index.html
      source:
        fn::fileAsset: ./index.html

  # Make the bucket's contents publicly readable
  my-bucket-binding:
    type: gcp:storage:BucketIAMBinding
    properties:
      bucket: ${my-bucket.name}
      role: "roles/storage.objectViewer"
      members:
        - allUsers

outputs:
  # Export the bucket's name and website URL
  bucketName: ${my-bucket.url}
  url: http://storage.googleapis.com/${my-bucket.name}/${index-html.name}
```

{{% /choosable %}}

A few things to note:

- Property relationships between resources encode their dependencies. For example, the `BucketObject`'s reference to the bucket tells Pulumi that the `Bucket` should be created first.
- The `url` export uses an [output helper](/docs/iac/concepts/inputs-outputs/helpers/) to build the site's address because the bucket and object names are values computed by Google Cloud at deployment time, not raw strings, so their values aren't known in advance.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
