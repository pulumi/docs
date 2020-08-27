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

Now that your S3 Bucket is provisioned, let's add an object to your bucket. First let's create a new directory called `site`.

```bash
$ mkdir site
```

Next let's create an `index.html` file you will upload to your bucket.

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
$ touch site/index.html
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ touch site/index.html
```

{{% /choosable %}}

{{% choosable os windows %}}

```bash
$ type nul > site/index.html
```

{{% /choosable %}}

Once you've created your `index.html` file, let's add some content:

```html
<html>
    <body>
        <h1>Hello Pulumi</h1>
    </body>
</html>
```

Now that you have your new `index.html` with some content, let's modify your program to upload the file to your S3 Bucket. To successfully upload the file you need to give Pulumi the absolute path to your file. We can easily accomplish this by taking advantage of libraries native to your programming language of choice.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const path = require("path");
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```javascript
const filePath = path.join(__dirname, "site", "index.html");

const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    source: new pulumi.asset.FileAsset(filePath),
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as path from "path";
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```typescript
const filePath = path.join(__dirname, "site", "index.html");

const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    source: new pulumi.asset.FileAsset(filePath),
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import os
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```python
filepath = os.path.abspath('site/index.html')

bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket,
    source=pulumi.FileAsset(filepath)
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
    "path/filepath"
    // Existing imports...
)
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```go
filePath, err := filepath.Abs("./site/index.html")

_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket: bucket.ID(),
    Source: pulumi.NewFileAsset(filePath),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.IO;
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```csharp
var filePath = Path.GetFullPath("./site/index.html");

var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.BucketName,
    Source = new FileAsset(filePath),
});
```

{{% /choosable %}}

Notice how you provide the bucket you created earlier as an input to your new `BucketObject`. This is so Pulumi knows what S3 Bucket the object should live in. You can learn more about Inputs and Outputs [here](/docs/intro/concepts/programming-model/#outputs).

Next, you'll deploy the changes.

{{< get-started-stepper >}}
