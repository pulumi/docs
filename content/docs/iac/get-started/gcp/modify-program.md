---
title_tag: Make an Update | Google Cloud
title: Make an update
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview on how to update a Google Cloud project from a Pulumi program.
weight: 6
menu:
    iac:
        name: Make an update
        identifier: gcp-get-started.modify-program
        parent: gcp-get-started
        weight: 6

aliases:
    - /docs/quickstart/gcp/modify-program/
    - /docs/clouds/gcp/get-started/modify-program/
    - /docs/quickstart/gcp/deploy-changes/
    - /docs/clouds/gcp/get-started/deploy-changes/
---

## Make an update

Now you will update your project to serve a static website out of your Google Cloud Storage bucket. You will change
your code and then re-run `pulumi up` which will update your infrastructure.

### Add new resources

Pulumi knows how to evolve your current infrastructure to your project's new desired state, both for
the first deployment as well as subsequent updates.

To turn your bucket into a static website, you will add two new Google Cloud Storage resources:

1. [`BucketObject`](/registry/packages/gcp/api-docs/storage/bucketobject/):
    uploads your website content to the bucket
2. [`BucketIAMBinding`](/registry/packages/gcp/api-docs/storage/bucketiambinding/):
    makes the bucket publicly accessible

### Add an index.html

First, from within your project directory, create a new `index.html` file with some content in it.

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

{{% choosable language typescript %}}

In `index.ts`, create the `BucketObject` by adding this code immediately following the bucket definition:

```typescript
// Upload the file
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    name: "index.html",
    source: new pulumi.asset.FileAsset("index.html")
});
```

{{% /choosable %}}

{{% choosable language python %}}

In `__main__.py`, create a new bucket object by adding this code immediately following the bucket definition:

```python
# Upload the file
bucket_object = storage.BucketObject(
    "index.html",
    bucket=bucket.name,
    name="index.html",
    source=pulumi.FileAsset("index.html")
)
```

{{% /choosable %}}

{{% choosable language go %}}

In `main.go`, create the `BucketObject` by adding this code immediately following the bucket definition:

```go
// Upload the file
_, err = storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket: bucket.Name,
    Name:   pulumi.String("index.html"),
    Source: pulumi.NewFileAsset("index.html"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

In `Program.cs`, create the `BucketObject` by adding this code immediately following the bucket definition:

```csharp
// Upload the file
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.Name,
    Name = "index.html",
    Source = new FileAsset("./index.html")
});
```

{{% /choosable %}}

{{% choosable language java %}}

In {{< langfile >}}, import the following additional classes, then create the `BucketObject` immediately following the bucket definition by adding this code:

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
            // Create a Google Cloud resource (Storage Bucket)
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                // existing bucket configuration
                .build());

            // Upload the file
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                .bucket(bucket.name())
                .name("index.html")
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
# Upload the file
index-html:
    type: gcp:storage:BucketObject
    properties:
        bucket: ${my-bucket}
        name: index.html
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

{{% notes type="info" %}}

If you encounter permission errors when uploading files, the IAM binding may still be propagating. The component
examples later in this tutorial show how to add explicit dependencies between resources to ensure proper ordering.

{{% /notes %}}

Now that `index.html` exists in the bucket, modify the bucket to serve the file as a static website.

To do that, update the bucket definition to configure its website property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `true`:

{{% choosable language typescript %}}

```typescript
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    website: {
        mainPageSuffix: "index.html"
    },
    uniformBucketLevelAccess: true
});
```

### Export the website URL

Now to export the website's public URL for easy access, add the `url` export as shown in this example:

```typescript
// Export the DNS name of the bucket
export const bucketName = bucket.url;

// Export the bucket's public URL
export const url = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket = storage.Bucket(
    "my-bucket",
    location="US",
    website={
        "main_page_suffix": "index.html"
    },
    uniform_bucket_level_access=True,
)
```

### Export the website URL

Now to export the website's public URL for easy access, add the `url` export as shown in this example:

```python
# Export the DNS name of the bucket
pulumi.export("bucket_name", bucket.url)

# Export the bucket's public URL
pulumi.export(
    "url",
    pulumi.Output.concat(
        "http://storage.googleapis.com/", bucket.id, "/", bucket_object.name
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
    Location: pulumi.String("US"),
    Website: storage.BucketWebsiteArgs{
        MainPageSuffix: pulumi.String("index.html"),
    },
    UniformBucketLevelAccess: pulumi.Bool(true),
})
if err != nil {
    return err
}
```

### Export the website URL

Now to export the website's public URL for easy access, add the `url` export as shown in this example:

```go
// Export the DNS name of the bucket
ctx.Export("bucketName", bucket.Url)

// Export the bucket's public URL
ctx.Export("url", pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, bucketObject.Name))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var bucket = new Bucket("my-bucket", new BucketArgs
{
    Location = "US",
    Website = new Pulumi.Gcp.Storage.Inputs.BucketWebsiteArgs
    {
        MainPageSuffix = "index.html"
    },
    UniformBucketLevelAccess = true
});
```

### Export the website URL

Now to export the website's public URL for easy access, add the `url` export to your return `Dictionary` as shown in this example:

```csharp
return new Dictionary<string, object?>
{
    ["bucketName"] = bucket.Url,
    ["url"] = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{bucketObject.Name}")
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var bucket = new Bucket("my-bucket", BucketArgs.builder()
    .location("US")
    .website(BucketWebsiteArgs.builder()
        .mainPageSuffix("index.html")
        .build())
    .uniformBucketLevelAccess(true)
    .build());
```

### Export the website URL

Now to export the website's public URL for easy access, add the `url` export as shown in this example:

```java
// Export the DNS name of the bucket
ctx.export("bucketName", bucket.url());

// Export the bucket's public URL
ctx.export("url", Output.format("http://storage.googleapis.com/%s/%s", bucket.name(), bucketObject.name()));
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US
      website:
        mainPageSuffix: index.html
      uniformBucketLevelAccess: true

outputs:
  bucketName: ${my-bucket.url}
  url: http://storage.googleapis.com/${my-bucket.name}/${index-html.name}
```

{{% /choosable %}}

We prepend `http://` using a helper because the bucket's URL is [an output property](/docs/iac/concepts/inputs-outputs/#outputs)
that Google Cloud assigns at deployment time, not a raw string, meaning its value is not known in advance.

### Deploy the changes

To deploy the changes, run `pulumi up` again and it will figure out the deltas:

{{% choosable os "linux,macos" %}}

```bash
$ pulumi up
```

{{% /choosable %}}
{{% choosable os "windows" %}}

```powershell
> pulumi up
```

{{% /choosable %}}

Just like the first time you will see a preview of the changes before they happen:

```
Previewing update (dev):

     Type                         Name             Plan
     pulumi:pulumi:Stack          quickstart-dev
 +   ├─ gcp:storage:BucketObject  index.html       create
 +   └─ gcp:storage:BucketIAMBinding  my-bucket-binding  create
 ~   └─ gcp:storage:Bucket        my-bucket        update

Outputs:
  + url: "http://storage.googleapis.com/my-bucket-a2b3c4d/index.html"

Resources:
    + 2 to create
    ~ 1 to update
    3 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to perform the deployment:

```
Do you want to perform this update? yes
Updating (dev):

     Type                         Name             Status
     pulumi:pulumi:Stack          quickstart-dev
 +   ├─ gcp:storage:BucketObject  index.html       created
 +   └─ gcp:storage:BucketIAMBinding  my-bucket-binding  created
 ~   └─ gcp:storage:Bucket        my-bucket        updated

Outputs:
    bucketName: "gs://my-bucket-a2b3c4d"
  + url       : "http://storage.googleapis.com/my-bucket-a2b3c4d/index.html"

Resources:
    + 2 created
    ~ 1 updated
    2 unchanged

Duration: 8s
```

In just a few seconds, your new website will be ready. Curl the endpoint to see it live:

```bash
$ curl $(pulumi stack output url)
```

This will reveal your new website!

```
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Feel free to experiment, such as changing the contents of `index.html` and redeploying.

Next, let's wrap this website up into an infrastructure abstraction.

{{< get-started-stepper >}}
