---
title_tag: Review the Project | Google Cloud
title: Review the project files
h1: "Review the project files"
meta_desc: This page walks through the files in a newly created Google Cloud + Pulumi project.
weight: 5
menu:
    iac:
        name: Review the project
        identifier: gcp-get-started.review-project
        parent: gcp-get-started
        weight: 5
aliases:
    - /docs/get-started/gcp/review-project/
    - /docs/quickstart/gcp/review-project/
    - /docs/clouds/gcp/get-started/review-project/
---

Your new project includes a few key files:

{{% choosable language "typescript,python,go,csharp" %}}

- <span>{{< langfile >}}</span> contains your program, which declares a Cloud Storage bucket
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language java %}}

- `src/main/java/myproject` is the project's Java package root
- <span>{{< langfile >}}</span> contains your program, which declares a Cloud Storage bucket
- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}
{{% choosable language yaml %}}

- `Pulumi.yaml` is the [project file](/docs/iac/concepts/projects/project-file) with metadata like your project's name, as well as your program's resources
- `Pulumi.dev.yaml` holds configuration for the stack you just created

{{% /choosable %}}

Now open {{< langfile >}} and take a look:

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

return await Pulumi.Deployment.RunAsync(() =>
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

This program declares a Cloud Storage [Bucket](/registry/packages/gcp/api-docs/storage/bucket/) [resource](/docs/iac/concepts/resources) and exports the bucket's DNS name as a [stack output](/docs/iac/concepts/stacks/#outputs). Resources are just objects with [properties](/docs/iac/concepts/inputs-outputs) that capture their inputs and outputs. Exporting the bucket's name makes it easy to reference later.

{{< get-started-stepper >}}
