---
title: Modify the Program | Alibaba Cloud
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update an Alibaba Cloud project from a Pulumi program.
weight: 8
menu:
  getstarted:
    parent: alicloud
    identifier: alicloud-modify-program

---

Now that we have an instance of our Pulumi program deployed, let's change the acl on our Oss bucket.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose csharp >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const alicloud = require("@pulumi/alicloud");

// Create an AliCloud resource (OSS Bucket)
const bucket = new alicloud.oss.Bucket("my-bucket", {
    acl: "public-read"
});

// Export the name of the bucket
exports.bucketName = bucket.id;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

// Create an AliCloud resource (OSS Bucket)
const bucket = new alicloud.oss.Bucket("my-bucket", {
    acl: "public-read"
});

// Export the name of the bucket
export const bucketName = bucket.id;
```

```python
import pulumi
from pulumi_alicloud import oss

# Create an AliCloud resource (OSS Bucket)
bucket = oss.Bucket('my-bucket',
    acl="public-read",
)

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

```go
package main

import (
    "github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/oss"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AliCloud resource (Oss Bucket)
        bucket, err := oss.NewBucket(ctx, "my-bucket", &oss.BucketArgs{
            Acl: "public-read",
        })
        if err != nil {
            return err
        }

        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        return nil
    })
}
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.AliCloud.Oss;

class Program
{
    static Task Main()
    {
        return Deployment.RunAsync(() =>
        {
            // Create an AliCloud resource (OSS Bucket)
            var bucket = new Bucket("my-bucket", new BucketArgs
            {
                Acl = "public-read"
            });

            // Export the name of the bucket
            return new Dictionary<string, object> {
                { "bucket_name", bucket.Id },
            };
        });
    }
}
```

Our program now changes the bucket to have an acl of `public-read`.

{{% lang go %}}
Recompile your project so the changes are picked up:

```bash
$ go build $(basename $(pwd))
```

{{% /lang %}}

Next, we'll deploy the changes.

{{< get-started-stepper >}}
