---
title: Modify the Program | AWS
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update an AWS project from a Pulumi program.
weight: 6
menu:
  getstarted:
    parent: aws
    identifier: aws-modify-program

aliases: ["/docs/quickstart/aws/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's turn our bucket into a simple static website.

Replace the entire contents of {{< langfile >}} with the following:

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html"
    }
});

// Create a home page for the website
const homepage = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    acl: aws.s3.PublicReadAcl,
    contentType: "text/html",
    content: `<html>
        <body>
            <h1>Hello, Pulumi!</h1>
        </body>
    </html>`,
});

// Export the name of the bucket
exports.bucketName = bucket.id;

// Export the URL of the website
exports.websiteEndpoint = bucket.websiteEndpoint;

```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html"
    }
});

// Create a home page for the website
const homepage = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    acl: aws.s3.PublicReadAcl,
    contentType: "text/html",
    content: `<html>
        <body>
            <h1>Hello, Pulumi!</h1>
        </body>
    </html>`,
});

// Export the name of the bucket
export const bucketName = bucket.id;

// Export the URL of the website
export const websiteEndpoint = bucket.websiteEndpoint;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket',
    website={
        'index_document': 'index.html'
    })

homepage = s3.BucketObject('index.html',
    bucket=bucket,
    acl='public-read',
    content_type='text/html',
    content="""<html>
        <body>
            <h1>Hello, Pulumi!</h1>
        </body>
    </html>""")

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('website_endpoint', pulumi.Output.concat("http://", bucket.website_endpoint))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
			Website: s3.BucketWebsiteArgs{
				IndexDocument: pulumi.String("index.html"),
			},
		})
		if err != nil {
			return err
		}

		// Create a homepage for the website
		_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
			Bucket:      bucket.ID(),
			Acl:         pulumi.String("public-read"),
			ContentType: pulumi.String("text/html"),
			Content: pulumi.String(`<html>
							<body>
								<h1>Hello, Pulumi!</h1>
							</body>
						</html>`),
		})
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())

		// Export the URL of the website
		ctx.Export("websiteEndpoint", bucket.WebsiteEndpoint.ApplyString(func(endpoint string) string {
			return "http://" + endpoint
		}))

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an AWS resource (S3 Bucket)
        var bucket = new Aws.S3.Bucket("my-bucket", new Aws.S3.BucketArgs
        {
            Website = new Aws.S3.Inputs.BucketWebsiteArgs
            {
                IndexDocument = "index.html"
            }
        });

        // Create a home page for the website
        var homepage = new Aws.S3.BucketObject("index.html", new Aws.S3.BucketObjectArgs {
            Acl = "public-read",
            Bucket = bucket.BucketName,
            ContentType = "text/html",
            Content = @"<html>
                <body>
                    <h1>Hello, Pulumi!</h1>
                </body>
            </html>",
        });

        // Export the name of the bucket
        this.BucketName = bucket.Id;

        this.WebsiteEndpoint = Output.Format($"http://{bucket.WebsiteEndpoint}");
    }

    [Output]
    public Output<string> BucketName { get; set; }

    [Output]
    public Output<string> WebsiteEndpoint { get; set; }
}
```

{{% /choosable %}}

Our program now creates a home page for our website and updates the S3 bucket to configure it as a website and set a default document.

Next, we'll deploy the changes.

{{< get-started-stepper >}}
