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

Now that your S3 bucket is provisioned, let's add an object to it. First, create a new directory called `site`.

```bash
mkdir site
```

Next, create a new `index.html` file with some content in it.

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
cat <<EOT > site/index.html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
EOT
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
cat <<EOT > site/index.html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
EOT
```

{{% /choosable %}}

{{% choosable os windows %}}

```batch
(
@echo.^<html^>
@echo.  ^<body^>
@echo.      ^<h1^>Hello, Pulumi!^</h1^>
@echo.  ^</body^>
@echo.^</html^>
) > site/index.html
```

{{% /choosable %}}

Now that you have your new `index.html` with some content, open your IDE or text editor and modify your program to add the contents of your `index.html` file to your S3 bucket.

To accomplish this, we will take advantage of your chosen programming language's native libraries to read the content of the file and assign it as an input to a new  `BucketObject`.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const fs = require("fs");
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```javascript
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    content: fs.readFileSync("site/index.html").toString(),
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as fs from "fs";
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```typescript
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket,
    content: fs.readFileSync("site/index.html").toString(),
});
```

{{% /choosable %}}

{{% choosable language python %}}

Next you will create a new bucket object on the lines right after creating the bucket itself.

```python
bucketObject = s3.BucketObject(
    'index.html',
    bucket=bucket,
    content=open('site/index.html').read(),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
    "io/ioutil"
    // Existing imports...
)
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```go
htmlContent, err := ioutil.ReadFile("site/index.html")
if err != nil {
    return err
}

_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:  bucket.ID(),
    Content: pulumi.String(string(htmlContent)),
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
var htmlString = File.ReadAllText(filePath);

var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.BucketName,
    Content = htmlString,
});
```

{{% /choosable %}}

Notice how you provide the bucket you created earlier as an input to your new `BucketObject`. This is so Pulumi knows what S3 bucket the object should live in.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
