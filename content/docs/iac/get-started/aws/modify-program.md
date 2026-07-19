---
title_tag: Modify the Program | AWS
title: Modify the program
h1: "Modify the program"
meta_desc: This page provides an overview on how to modify a program in Pulumi when starting an AWS project.
weight: 7
menu:
    iac:
        name: Modify the program
        parent: aws-get-started
        weight: 7

aliases:
    - /docs/iac/get-started/aws/b/modify-program/
    - /docs/quickstart/aws/modify-program/
    - /docs/get-started/aws/modify-program/
    - /docs/clouds/aws/get-started/modify-program/
---

Now you'll turn the S3 bucket into a static website.

In your project directory, create a file named `index.html` with the following content:

```html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

To turn the bucket into a website, you'll need four new resources:

- A [`BucketWebsiteConfiguration`](/registry/packages/aws/api-docs/s3/bucketwebsiteconfiguration/) to configure your bucket as a website
- A [`BucketOwnershipControls`](/registry/packages/aws/api-docs/s3/bucketownershipcontrols/) resource to make its access controls configurable
- A [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/) to allow public access to the bucket, which AWS disables by default
- A [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) for the HTML file

Open {{< langfile >}} and replace it with the following code:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket:
const bucket = new aws.s3.Bucket("my-bucket");

// Configure the bucket as a website:
const website = new aws.s3.BucketWebsiteConfiguration("website", {
    bucket: bucket.id,
    indexDocument: {
        suffix: "index.html",
    },
});

// Configure ownership controls for the bucket:
const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter",
    },
});

// Enable public access to the bucket:
const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});

// Upload index.html to the bucket:
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("index.html"),
    contentType: "text/html",
    acl: "public-read",
}, { dependsOn: [ownershipControls, publicAccessBlock] });

// Export the bucket's name and website URL:
export const bucketName = bucket.id;
export const url = pulumi.interpolate`http://${website.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3

# Create an S3 bucket:
bucket = s3.Bucket('my-bucket')

# Configure the bucket as a website:
website = s3.BucketWebsiteConfiguration("website",
    bucket=bucket.id,
    index_document={
        "suffix": "index.html",
    })

# Configure ownership controls for the bucket:
ownership_controls = s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule={
        "object_ownership": 'ObjectWriter',
    },
)

# Enable public access to the bucket:
public_access_block = s3.BucketPublicAccessBlock(
    'public-access-block', bucket=bucket.id, block_public_acls=False
)

# Upload index.html to the bucket:
bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[ownership_controls, public_access_block]),
)

# Export the bucket's name and website URL:
pulumi.export('bucket_name', bucket.id)
pulumi.export('url', pulumi.Output.concat('http://', website.website_endpoint))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an S3 bucket:
        bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
        if err != nil {
            return err
        }

        // Configure the bucket as a website:
        website, err := s3.NewBucketWebsiteConfiguration(ctx, "website", &s3.BucketWebsiteConfigurationArgs{
            Bucket: bucket.ID(),
            IndexDocument: &s3.BucketWebsiteConfigurationIndexDocumentArgs{
                Suffix: pulumi.String("index.html"),
            },
        })
        if err != nil {
            return err
        }

        // Configure ownership controls for the bucket:
        ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
            Bucket: bucket.ID(),
            Rule: &s3.BucketOwnershipControlsRuleArgs{
                ObjectOwnership: pulumi.String("ObjectWriter"),
            },
        })
        if err != nil {
            return err
        }

        // Enable public access to the bucket:
        publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
            Bucket:          bucket.ID(),
            BlockPublicAcls: pulumi.Bool(false),
        })
        if err != nil {
            return err
        }

        // Upload index.html to the bucket:
        _, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
            Bucket:      bucket.ID(),
            Source:      pulumi.NewFileAsset("index.html"),
            ContentType: pulumi.String("text/html"),
            Acl:         pulumi.String("public-read"),
        }, pulumi.DependsOn([]pulumi.Resource{ownershipControls, publicAccessBlock}))
        if err != nil {
            return err
        }

        // Export the bucket's name and website URL:
        ctx.Export("bucketName", bucket.ID())
        ctx.Export("url", website.WebsiteEndpoint.ApplyT(func(websiteEndpoint string) (string, error) {
            return fmt.Sprintf("http://%v", websiteEndpoint), nil
        }).(pulumi.StringOutput))
        return nil
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Create an S3 bucket:
    var bucket = new Bucket("my-bucket");

    // Configure the bucket as a website:
    var website = new BucketWebsiteConfiguration("website", new()
    {
        Bucket = bucket.Id,
        IndexDocument = new BucketWebsiteConfigurationIndexDocumentArgs
        {
            Suffix = "index.html",
        },
    });

    // Configure ownership controls for the bucket:
    var ownershipControls = new BucketOwnershipControls("ownership-controls", new()
    {
        Bucket = bucket.Id,
        Rule = new BucketOwnershipControlsRuleArgs
        {
            ObjectOwnership = "ObjectWriter",
        },
    });

    // Enable public access to the bucket:
    var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", new()
    {
        Bucket = bucket.Id,
        BlockPublicAcls = false,
    });

    // Upload index.html to the bucket:
    var bucketObject = new BucketObject("index.html", new()
    {
        Bucket = bucket.Id,
        Source = new FileAsset("index.html"),
        ContentType = "text/html",
        Acl = "public-read",
    }, new CustomResourceOptions
    {
        DependsOn = new Resource[]
        {
            ownershipControls,
            publicAccessBlock,
        },
    });

    // Export the bucket's name and website URL:
    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Id,
        ["url"] = website.WebsiteEndpoint.Apply(websiteEndpoint => $"http://{websiteEndpoint}"),
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.asset.FileAsset;
import com.pulumi.resources.*;

import com.pulumi.aws.s3.*;
import com.pulumi.aws.s3.inputs.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an S3 bucket:
            var bucket = new Bucket("my-bucket");

            // Configure the bucket as a website:
            var website = new BucketWebsiteConfiguration("website", BucketWebsiteConfigurationArgs.builder()
                .bucket(bucket.id())
                .indexDocument(BucketWebsiteConfigurationIndexDocumentArgs.builder()
                    .suffix("index.html")
                    .build())
                .build());

            // Configure ownership controls for the bucket:
            var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
                .bucket(bucket.id())
                .rule(BucketOwnershipControlsRuleArgs.builder()
                    .objectOwnership("ObjectWriter")
                    .build())
                .build());

            // Enable public access to the bucket:
            var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
                .bucket(bucket.id())
                .blockPublicAcls(false)
                .build());

            // Upload index.html to the bucket:
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.id())
                .source(new FileAsset("index.html"))
                .contentType("text/html")
                .acl("public-read")
                .build(), CustomResourceOptions.builder()
                    .dependsOn(
                        ownershipControls,
                        publicAccessBlock)
                    .build());

            // Export the bucket's name and website URL:
            ctx.export("bucketName", bucket.bucket());
            ctx.export("url", website.websiteEndpoint().applyValue(
                websiteEndpoint -> String.format("http://%s", websiteEndpoint)));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal AWS Pulumi YAML program

resources:
  # Create an S3 bucket:
  my-bucket:
    type: aws:s3:Bucket

  # Configure the bucket as a website:
  website:
    type: aws:s3:BucketWebsiteConfiguration
    properties:
      bucket: ${my-bucket.id}
      indexDocument:
        suffix: index.html

  # Configure ownership controls for the bucket:
  ownership-controls:
    type: aws:s3:BucketOwnershipControls
    properties:
      bucket: ${my-bucket.id}
      rule:
        objectOwnership: ObjectWriter

  # Enable public access to the bucket:
  public-access-block:
    type: aws:s3:BucketPublicAccessBlock
    properties:
      bucket: ${my-bucket.id}
      blockPublicAcls: false

  # Upload index.html to the bucket:
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket.id}
      source:
        fn::fileAsset: index.html
      contentType: text/html
      acl: public-read
    options:
      dependsOn:
        - ${ownership-controls}
        - ${public-access-block}

outputs:
  # Export the bucket's name and website URL:
  bucketName: ${my-bucket.id}
  url: http://${website.websiteEndpoint}
```

{{% /choosable %}}

A few things to note:

- Property relationships between resources encode their dependencies. For example, the `BucketWebsiteConfiguration`'s reference to the bucket's ID tells Pulumi that the `Bucket` should be created first.
- The HTML file depends on the bucket as well — but since the file can't be uploaded until the bucket's permissions are set, the `BucketObject` uses [`dependsOn`](/docs/iac/concepts/resources/options/dependson/) to declare a dependency on those resources so they're created before it. (By default, Pulumi runs resource options in parallel.)
- The `url` export uses an [output helper](/docs/iac/concepts/inputs-outputs/helpers/) to prepend `http://` because the website endpoint is a value computed by AWS at deployment time, not a raw string, so its value isn't known in advance.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
