---
title_tag: Modify the Program | AWS
title: Modify program
h1: "Pulumi & AWS: Modify program"
meta_desc: This page provides an overview on how to update an AWS project from a Pulumi
  program.
weight: 6
aliases:
  - /docs/quickstart/aws/modify-program/
  - /docs/get-started/aws/modify-program/
  - /docs/clouds/aws/get-started/modify-program/
search:
  keywords:
    - program
    - modify
    - bucket
    - aws
    - bucketobject
    - overview
    - provides
---

Now that your S3 bucket is provisioned, let's add a file to it. First, from within your project directory, create a new file called `index.html` along with some content:

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
echo '<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>' > index.html
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
echo '<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>' > index.html
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
@"
<html>
  <body>
    <h1>Hello, Pulumi!</h1>
  </body>
</html>
"@ | Out-File -FilePath index.html
```

{{% /choosable %}}

Now, open the program and add this file to the S3 bucket. To do this, you'll use Pulumi's [`FileAsset`](/docs/iac/concepts/assets-archives/#assets) to assign the content of the file to a new  [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/):

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

In `index.js`, create the `BucketObject` right after creating the bucket itself:

```javascript
// Create an S3 Bucket object
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

In `index.ts`, create the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself:

```typescript
// Create an S3 Bucket object
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language python %}}

In `__main__.py`, create a new bucket object by adding the following right after creating the bucket itself:

```python
# Create an S3 Bucket object
bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('./index.html')
)
```

{{% /choosable %}}

{{% choosable language go %}}

In `main.go`, create the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself:

```go
// Create an S3 Bucket object
_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket: bucket.ID(),
    Source: pulumi.NewFileAsset("./index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

In `Program.cs`, create a new [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself.

```csharp
// Create an S3 Bucket object
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.Id,
    Source = new FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language java %}}

In {{< langfile >}}, import the [`FileAsset`](/docs/iac/concepts/assets-archives/#assets), [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/), and `BucketObjectArgs` classes, then create the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself.

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.s3.BucketV2;
import com.pulumi.aws.s3.BucketObject;
import com.pulumi.aws.s3.BucketObjectArgs;
import com.pulumi.asset.FileAsset;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Create an AWS resource (S3 Bucket)
            var bucket = new BucketV2("my-bucket");

            // Create an S3 Bucket object
            new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.bucket())
                .source(new FileAsset("./index.html"))
                .build()
            );

            // Export the name of the bucket
            ctx.export("bucketName", bucket.bucket());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

In {{< langfile >}}, create the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right below the bucket itself.

```yaml
name: quickstart
runtime: yaml
description: A minimal AWS Pulumi YAML program

resources:
  # Create an AWS resource (S3 Bucket)
  my-bucket:
    type: aws:s3:BucketV2

  # Create an S3 Bucket object
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket.bucket}
      source:
        fn::fileAsset: ./index.html

outputs:
  # Export the name of the bucket
  bucketName: ${my-bucket.bucket}
```

{{% /choosable %}}

This bucket object is part of the [`Bucket`](/registry/packages/aws/api-docs/s3/bucket/) that we deployed earlier because we _reference_ the bucket name in the properties of the bucket object.

We refer to this relationship as the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) being a _child_ resource of the S3 `Bucket` that is the _parent_ resource. This is how Pulumi knows what S3 bucket the object should live in.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
