---
title_tag: Modify the Program | Google Cloud
meta_desc: This page provides an overview on how to update Google Cloud (GCP) project from a Pulumi program.
title: Modify program
h1: "Pulumi & Google Cloud: Modify program"
weight: 6
menu:
  clouds:
    parent: google-cloud-get-started
    identifier: gcp-modify-program

aliases:
- /docs/quickstart/gcp/modify-program/
- /docs/get-started/gcp/modify-program/
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

Now that you have an `index.html` file with some content, open {{< langfile >}} and modify it to add that file to your storage bucket.

For this, you'll use Pulumi's `FileAsset` class to assign the content of the file to a new `BucketObject`.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

In `index.js`, create the `BucketObject` right after creating the bucket itself:

```javascript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    source: new pulumi.asset.FileAsset("index.html")
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

In `index.ts`, create the `BucketObject` right after creating the bucket itself:

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
bucket_object = storage.BucketObject(
    "index.html", bucket=bucket.name, source=pulumi.FileAsset("index.html")
)
```

{{% /choosable %}}

{{% choosable language go %}}

In `main.go`, create the `BucketObject` right after creating the bucket itself:

```go
_, err = storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket: bucket.Name,
    Source: pulumi.NewFileAsset("index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

In `Program.cs`, create the `BucketObject` right after creating the bucket itself:

```csharp
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.Name,
    Source = new FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language java %}}

In {{< langfile >}}, import the following additional classes, then create the `BucketObject` right after creating the bucket itself:

```java
// ...
import com.pulumi.asset.FileAsset;
import com.pulumi.gcp.storage.BucketIAMBinding;
import com.pulumi.gcp.storage.BucketIAMBindingArgs;
import com.pulumi.gcp.storage.BucketObject;
import com.pulumi.gcp.storage.BucketObjectArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // ...

            // Create a Bucket object
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.name())
                .source(new FileAsset("index.html"))
                .build()
            );

            // ...
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
  index-html:
    type: gcp:storage:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        fn::fileAsset: ./index.html
```

{{% /choosable %}}

Notice how you provide the name of the bucket you created earlier as an input for the `BucketObject`. This tells Pulumi which bucket the object should live in.

Below the `BucketObject`, add an IAM binding allowing the contents of the bucket to be viewed anonymously over the Internet:

{{% choosable language typescript %}}

```typescript
const bucketBinding = new gcp.storage.BucketIAMBinding("my-bucket-binding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"]
});
```

{{% /choosable %}}

{{% choosable language javascript %}}

```javascript
const bucketBinding = new gcp.storage.BucketIAMBinding("my-bucket-binding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"]
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket_iam_binding = storage.BucketIAMBinding(
    "my-bucket-binding",
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
_, err = storage.NewBucketIAMBinding(ctx, "my-bucket-binding", &storage.BucketIAMBindingArgs{
    Bucket: bucket.Name,
    Role:   pulumi.String("roles/storage.objectViewer"),
    Members: pulumi.StringArray{
        pulumi.String("allUsers"),
    },
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var bucketBinding = new BucketIAMBinding("my-bucket-binding", new BucketIAMBindingArgs
{
    Bucket = bucket.Name,
    Role = "roles/storage.objectViewer",
    Members = new[]
    {
        "allUsers",
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var bucketBinding = new BucketIAMBinding("my-bucket-binding", BucketIAMBindingArgs.builder()
    .bucket(bucket.name())
    .role("roles/storage.objectViewer")
    .members("allUsers")
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
my-bucket-binding:
  type: gcp:storage:BucketIAMBinding
  properties:
    bucket: ${my-bucket.name}
    role: "roles/storage.objectViewer"
    members:
      - allUsers
```

{{% /choosable %}}

Next, you'll deploy your changes.

{{< get-started-stepper >}}
