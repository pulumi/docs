---
title_tag: Review the New Project | Google Cloud
meta_desc: This page provides an overview on how to a review a new Google Cloud project.
title: Review project
h1: "Pulumi & Google Cloud: Review project"
weight: 4
menu:
  clouds:
    parent: google-cloud-get-started
    identifier: gcp-review-project

aliases:
- /docs/quickstart/gcp/review-project/
- /docs/get-started/gcp/review-project/
---

Let's review some of the generated project files:

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

- `Pulumi.yaml` defines the [project](/docs/concepts/projects/).

{{% /choosable %}}

{{% choosable language yaml %}}

- `Pulumi.yaml` defines both the [project](/docs/concepts/projects/) and the program that manages your stack resources.

{{% /choosable %}}

- `Pulumi.dev.yaml` contains [configuration](/docs/concepts/config/) values for the [stack](/docs/concepts/stack/) you initialized.

{{% choosable language java %}}

- `src/main/java/myproject` defines the project's Java package root.

{{% /choosable %}}

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

<!-- The wrapping spans are infortunately necessary here; without them, the renderer gets confused and generates invalid markup. -->
- <span>{{< langfile >}}</span> is the Pulumi program that defines your stack resources.

{{% /choosable %}}

Let's examine {{< langfile >}}.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

// Create a Google Cloud resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US"
});

// Export the DNS name of the bucket
exports.bucketName = bucket.url;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a Google Cloud resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
});

// Export the DNS name of the bucket
export const bucketName = bucket.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_gcp import storage

# Create a Google Cloud resource (Storage Bucket)
bucket = storage.Bucket("my-bucket", location="US")

# Export the DNS name of the bucket
pulumi.export("bucket_name", bucket.url)
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
		// Create a Google Cloud resource (Storage Bucket)
		bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
			Location: pulumi.String("US"),
		})
		if err != nil {
			return err
		}

		// Export the DNS name of the bucket
		ctx.Export("bucketName", bucket.Url)
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

return await Deployment.RunAsync(() =>
{
    // Create a Google Cloud resource (Storage Bucket).
    var bucket = new Bucket("my-bucket", new BucketArgs
    {
        Location = "US",
    });

    // Export the DNS name of the bucket.
    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Url,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.gcp.storage.Bucket;
import com.pulumi.gcp.storage.BucketArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a Google Cloud resource (Storage Bucket)
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .location("US")
                .build());

            // Export the DNS name of the bucket
            ctx.export("bucketName", bucket.url());
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
  # Create a Google Cloud resource (Storage Bucket)
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US

outputs:
  # Export the DNS name of the bucket
  bucketName: ${my-bucket.url}
```

{{% /choosable %}}

This Pulumi program creates a new storage bucket and exports the DNS name of the bucket.

{{% choosable language javascript %}}

```javascript
exports.bucketName = bucket.url;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const bucketName = bucket.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export("bucket_name", bucket.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("bucketName", bucket.Url)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return new Dictionary<string, object?>
{
    ["bucketName"] = bucket.Url,
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
ctx.export("bucketName", bucket.url());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  bucketName: ${my-bucket.url}
```

{{% /choosable %}}

Next, you'll deploy your stack, which will provision your storage bucket.

{{< get-started-stepper >}}
