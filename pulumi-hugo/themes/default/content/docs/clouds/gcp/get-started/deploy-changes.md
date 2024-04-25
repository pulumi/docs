---
title_tag: Deploy the Changes | Google Cloud
meta_desc: This page provides an overview of how deploy changes to a Google Cloud project.
title: Deploy changes
h1: "Pulumi & Google Cloud: Deploy changes"
weight: 7
menu:
  clouds:
    parent: google-cloud-get-started
    identifier: gcp-deploy-changes

aliases:
- /docs/quickstart/gcp/deploy-changes/
- /docs/get-started/gcp/deploy-changes/
---

Now let's deploy your changes.

```bash
$ pulumi up
```

Pulumi will run the `preview` step of the update, which computes the minimally disruptive change to achieve the desired state described by the program:

```
Previewing update (dev)

     Type                             Name               Plan
     pulumi:pulumi:Stack              quickstart-dev
 +   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  create
 +   └─ gcp:storage:BucketObject      index.html         create

Resources:
    + 2 to create
    2 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` will proceed with the update and write the `index.html` file to the bucket:

```
Updating (dev)

     Type                             Name               Status
     pulumi:pulumi:Stack              quickstart-dev
 +   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  created (5s)
 +   └─ gcp:storage:BucketObject      index.html         created (0.76s)

Outputs:
    bucketName: "gs://my-bucket-daa12be"

Resources:
    + 2 created
    2 unchanged

Duration: 8s
```

Once the update has completed, you can verify the object was created by checking the Google Cloud Console or running the following `gsutil` command:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ gsutil ls $(pulumi stack output bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ gsutil ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{< /chooser >}}

Notice that your `index.html` file has been added to the bucket:

```bash
gs://my-bucket-daa12be/index.html-a52debd
```

{{% choosable language javascript %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `true`:

```javascript
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    website: {
        mainPageSuffix: "index.html"
    },
    uniformBucketLevelAccess: true
});
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```javascript
exports.bucketEndpoint = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language typescript %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `true`:

```typescript
const bucket = new gcp.storage.Bucket("my-bucket", {
    location: "US",
    website: {
        mainPageSuffix: "index.html"
    },
    uniformBucketLevelAccess: true
});
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```typescript
export const bucketEndpoint = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language python %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `True`:

```python
bucket = storage.Bucket(
    "my-bucket",
    location="US",
    website=storage.BucketWebsiteArgs(main_page_suffix="index.html"),
    uniform_bucket_level_access=True,
)
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```python
pulumi.export(
    "bucket_endpoint",
    pulumi.Output.concat(
        "http://storage.googleapis.com/", bucket.id, "/", bucket_object.name
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `Website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `true`:

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

Finally, at the end of the file, export the website's public URL to make it easy to access.

```go
ctx.Export("bucketEndpoint", pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, bucketObject.Name))
```

Be sure to change the variable name of the `BucketObject` from `_` to `bucketObject` in this step, or Go may fail to compile the program:

```go
bucketObject, err := storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket: bucket.Name,
    Source: pulumi.NewFileAsset("index.html"),
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `Website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access property to `true`:

```csharp
// Add this using statement
using Pulumi.Gcp.Storage.Inputs;
```

```csharp
var bucket = new Bucket("my-bucket", new BucketArgs
{
    Location = "US",
    Website = new BucketWebsiteArgs
    {
        MainPageSuffix = "index.html"
    },
    UniformBucketLevelAccess = true
});
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```csharp
return new Dictionary<string, object?>
{
    ["bucketName"] = bucket.Url,
    ["bucketEndpoint"] = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{bucketObject.Name}")
};
```

{{% /choosable %}}

{{% choosable language java %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, add the `BucketWebsiteArgs` class to the list of imports, then update the bucket definition to configure its `website` property. To align with Google Cloud Storage recommendations, also set its uniform bucket-level access property to `true`:

```java
// ...
import com.pulumi.gcp.storage.inputs.BucketWebsiteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                .location("US")
                .website(BucketWebsiteArgs.builder()
                    .mainPageSuffix("index.html")
                    .build())
                .build());
            //...
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```java
ctx.export("bucketEndpoint", Output.format("http://storage.googleapis.com/%s/%s", bucket.name(), bucketObject.name()));
```

{{% /choosable %}}

{{% choosable language yaml %}}

Now that `index.html` exists in the bucket, modify the program to have the bucket serve the file as a static website.

To do that, update the bucket definition to configure its `Website` property. Then, to align with Google Cloud Storage recommendations, set its uniform bucket-level access setting to `true`:

```yaml
resources:
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      location: US
      website:
        mainPageSuffix: index.html
      uniformBucketLevelAccess: true
```

Finally, at the end of the file, export the website's public URL to make it easy to access:

```yaml
# ...
outputs:
  # ...
  bucketEndpoint: http://storage.googleapis.com/${my-bucket.name}/${index-html.name}
  ```

{{% /choosable %}}

Give the stack one final update to apply these changes:

```bash
$ pulumi up
```

Again, you'll see a preview of the changes to be made:

```
Previewing update (dev)

     Type                   Name            Plan       Info
     pulumi:pulumi:Stack    quickstart-dev
 ~   └─ gcp:storage:Bucket  my-bucket       update     [diff: +website~uniformBucketLevelAccess]

Outputs:
  + bucketEndpoint: "http://storage.googleapis.com/my-bucket-daa12be/index.html-a52debd"

Resources:
    ~ 1 to update
    3 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to deploy them:

```
Updating (dev)

     Type                   Name            Status           Info
     pulumi:pulumi:Stack    quickstart-dev
 ~   └─ gcp:storage:Bucket  my-bucket       updated (1s)     [diff: +website~uniformBucketLevelAccess]

Outputs:
  + bucketEndpoint: "http://storage.googleapis.com/my-bucket-daa12be/index.html-a52debd"
    bucketName    : "gs://my-bucket-daa12be"

Resources:
    ~ 1 updated
    3 unchanged

Duration: 4s
```

When the deployment completes, you can check out your new static website at the URL under `Outputs`, or make a `curl` request and see the contents of `index.html` printed to the terminal:

{{% choosable language javascript %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ curl $(pulumi stack output bucket_endpoint)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ curl $(pulumi stack output bucketEndpoint)
```

{{% /choosable %}}

And you should see:

```bash
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Next you will destroy the resources.

{{< get-started-stepper >}}
