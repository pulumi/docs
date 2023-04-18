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

Now that your storage bucket is provisioned, let's add an object to it. First, from within your project directory, create a new `index.html` file with some content in it.

{{< chooser os "macos,linux,windows" / >}}

{{% choosable os macos %}}

```bash
cat <<EOT > index.html
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
cat <<EOT > index.html
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
"@ | Out-File -FilePath index.html
```

{{% /choosable %}}

Now that you have your new `index.html` with some content, open your program file and modify it to add the contents of your `index.html` file to your storage bucket.

To accomplish this, you will use Pulumi's `FileAsset` class to assign the content of the file to a new  `BucketObject`.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

In `index.js`, create the `BucketObject` right after creating the bucket itself.

```javascript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    source: new pulumi.asset.FileAsset("index.html")
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

In `index.ts`, create the `BucketObject` right after creating the bucket itself.

```typescript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    source: new pulumi.asset.FileAsset("index.html")
});
```

{{% /choosable %}}

{{% choosable language python %}}

In `__main__.py`, create a new bucket object by adding the following right after creating the bucket itself:

```python
bucketObject = storage.BucketObject(
    'index.html',
    bucket=bucket.name,
    source=pulumi.FileAsset('index.html')
)
```

{{% /choosable %}}

{{% choosable language go %}}

In `main.go`, create the `BucketObject` right after creating the bucket itself.

```go
bucketObject, err := storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket: bucket.Name,
    Source: pulumi.NewFileAsset("index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

In `Program.cs`, create the `BucketObject` right after creating the bucket itself.

```csharp
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.Name,
    Source = new FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language java %}}

In {{< langfile >}}, import the `FileAsset`, `BucketObject`, and `BucketObjectArgs` classes, then create the `BucketObject` right after creating the bucket itself.

```java
// ...
import com.pulumi.asset.FileAsset;
import com.pulumi.gcp.storage.BucketObject;
import com.pulumi.gcp.storage.BucketObjectArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // var bucket = ...

            // Create a Bucket object
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.name())
                .source(new FileAsset("index.html"))
                .build()
            );

            // ctx.export(...
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

In {{< langfile >}}, create the `BucketObject` right below the bucket itself.

```yaml
resources:
  # ...
  index-object:
    type: gcp:storage:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        Fn::FileAsset: ./index.html
```

{{% /choosable %}}

Notice how you provide the bucket you created earlier as an input to your new `BucketObject`. This is so Pulumi knows what storage bucket the object should live in.

Next, you'll deploy your changes.

{{< get-started-stepper >}}
