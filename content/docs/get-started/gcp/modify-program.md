---
title: Modify the Program | GCP
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update Google Cloud (GCP) project from a Pulumi program.
weight: 6
menu:
  getstarted:
    parent: gcp
    identifier: gcp-modify-program

aliases: ["/docs/quickstart/gcp/modify-program/"]
---

Now that your storage bucket is provisioned, let's add an object to it. First, create a new directory called `site`.

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

```powershell
@"
<html>
  <body>
    <h1>Hello, Pulumi!</h1>
  </body>
</html>
"@ | Out-File -FilePath site\index.html
```

{{% /choosable %}}

Now that you have your new `index.html` with some content, open your IDE or text editor and modify your program to add the contents of your `index.html` file to your storage bucket.

To accomplish this, we will take advantage of your chosen programming language's native libraries to read the content of the file and assign it as an input to a new  `BucketObject`.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
const fs = require("fs");
```

Next you will create a new bucket object on the lines right after creating the bucket itself.

```javascript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
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
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    content: fs.readFileSync("site/index.html").toString(),
});
```

{{% /choosable %}}

{{% choosable language python %}}

Next you will create a new bucket object on the lines right after creating the bucket itself.

```python
bucketObject = storage.BucketObject(
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

bucketObject, err := storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket:  bucket.Name,
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
    Bucket = bucket.Name,
    Content = htmlString,
});
```

{{% /choosable %}}

Notice how you provide the bucket you created earlier as an input to your new `BucketObject`. This is so Pulumi knows what storage bucket the object should live in.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
