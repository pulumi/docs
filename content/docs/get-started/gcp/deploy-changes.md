---
title: Deploy the Changes | GCP
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to a Google Cloud project.
weight: 7
menu:
  getstarted:
    parent: gcp
    identifier: gcp-deploy-changes

aliases: ["/docs/quickstart/gcp/deploy-changes/"]
---

Now let's deploy your changes.

```bash
$ pulumi up
```

Pulumi will run the `preview` step of the update, which computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                         Name                   Plan
     pulumi:pulumi:Stack          quickstart-dev
 +   └─ gcp:storage:BucketObject  index.html             create


Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` will proceed with the update and upload your `index.html` file to your bucket.

```
Do you want to perform this update? yes
Updating (dev):

     Type                         Name                   Status
     pulumi:pulumi:Stack          quickstart-dev
 +   └─ gcp:storage:BucketObject  index.html             created


Outputs:
    bucketName: "gs://my-bucket-11a9046"

Resources:
    + 1 created
    2 unchanged

Duration: 3s
```

Once the update has completed, you can verify the object was created in your bucket by checking the Google Cloud Console or by running the following `gsutil` command:

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
gs://my-bucket-11a9046/index.html-77a5d80
```

{{% choosable language javascript %}}

Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```javascript
const bucket = new gcp.storage.Bucket("my-bucket", {
    website: {
        mainPageSuffix: "index.html"
    },
    uniformBucketLevelAccess: true
});
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```javascript
const bucketIAMBinding = new gcp.storage.BucketIAMBinding("my-bucket-IAMBinding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"]
});
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```javascript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    contentType: "text/html",
    source: new pulumi.asset.FileAsset("index.html")
});
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```javascript
exports.bucketEndpoint = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language typescript %}}

Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```typescript
const bucket = new gcp.storage.Bucket("my-bucket", {
    website: {
        mainPageSuffix: "index.html"
    },
    uniformBucketLevelAccess: true
});
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```typescript
const bucketIAMBinding = new gcp.storage.BucketIAMBinding("my-bucket-IAMBinding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"]
});
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```typescript
const bucketObject = new gcp.storage.BucketObject("index.html", {
    bucket: bucket.name,
    contentType: "text/html",
    source: new pulumi.asset.FileAsset("index.html")
});
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```typescript
export const bucketEndpoint = pulumi.concat("http://storage.googleapis.com/", bucket.name, "/", bucketObject.name);
```

{{% /choosable %}}

{{% choosable language python %}}

Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `True`.

```python
bucket = storage.Bucket('my-bucket',
    website=storage.BucketWebsiteArgs(
        main_page_suffix='index.html'),
    uniform_bucket_level_access=True,
)
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```python
bucketIAMBinding = storage.BucketIAMBinding('my-bucket-IAMBinding',
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"]
)
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```python
bucketObject = storage.BucketObject(
    'index.html',
    bucket=bucket.name,
    content_type='text/html',
    source=pulumi.FileAsset('index.html')
)
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```python
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://storage.googleapis.com/', bucket.id, "/", bucketObject.name))
```

{{% /choosable %}}

{{% choosable language go %}}
Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```go
bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
    Website: storage.BucketWebsiteArgs{
        MainPageSuffix: pulumi.String("index.html"),
    },
    UniformBucketLevelAccess: pulumi.Bool(true),
})
if err != nil {
    return err
}
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```go
_, err = storage.NewBucketIAMBinding(ctx, "my-bucket-IAMBinding", &storage.BucketIAMBindingArgs{
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

Also, change the content type of your `index.html` object so that it is served as HTML.

```go
bucketObject, err := storage.NewBucketObject(ctx, "index.html", &storage.BucketObjectArgs{
    Bucket:      bucket.Name,
    ContentType: pulumi.String("text/html"),
    Source:      pulumi.NewFileAsset("index.html"),
})
if err != nil {
    return err
}
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```go
bucketEndpoint := pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, bucketObject.Name)
ctx.Export("bucketEndpoint", bucketEndpoint)
```

{{% /choosable %}}

{{% choosable language csharp %}}

Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```csharp
// Add this using statement
using Pulumi.Gcp.Storage.Inputs;
```

```csharp
var bucket = new Bucket("my-bucket", new BucketArgs
{
    Website = new BucketWebsiteArgs
    {
        MainPageSuffix = "index.html"
    },
    UniformBucketLevelAccess = true
});
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```csharp
var bucketIAMBinding = new BucketIAMBinding("my-bucket-IAMBinding", new BucketIAMBindingArgs
{
    Bucket = bucket.Name,
    Role = "roles/storage.objectViewer",
    Members = "allUsers"
});
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```csharp
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Bucket = bucket.Name,
    ContentType = "text/html",
    Source = new FileAsset("./index.html")
});
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```csharp
return new Dictionary<string, object?>
{
    ["bucketName"] = bucket.Url,
    ["bucketEndpoint"] = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{bucketObject.Name}")
};
```

{{% /choosable %}}

{{% choosable language java %}}

Now that your `index.html` is in your bucket, modify the program to have the bucket serve `index.html` as a static website.

First, add the `BucketArgs`,  `BucketWebsiteArgs`, `BucketIAMBinding`, and `BucketIAMBindingArgs` classes to the list of imports.

```java
// ...
import com.pulumi.gcp.storage.BucketArgs;
import com.pulumi.gcp.storage.inputs.BucketWebsiteArgs;
import com.pulumi.gcp.storage.BucketIAMBinding;
import com.pulumi.gcp.storage.BucketIAMBindingArgs;
```

Next, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`:

```java
// ...
public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create an AWS resource (S3 Bucket)
            var bucket = new Bucket("my-bucket",
                    BucketArgs.builder()
                            .location("US")
                            .website(BucketWebsiteArgs.builder()
                                    .mainPageSuffix("index.html")
                                    .build())
                            .uniformBucketLevelAccess(true)
                            .build());
            //...
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```java
// ...
public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // var bucket = ...
            var binding = new BucketIAMBinding("my-bucket-IAMBinding",
                    BucketIAMBindingArgs.builder()
                            .bucket(bucket.name())
                            .role("roles/storage.objectViewer")
                            .members("allUsers")
                            .build());
            // Create an S3 Bucket object ...
```

Also, change the content type of your index.html object so that it is served as HTML.

```java
// ...
public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // var bucket = ...
            // var binding = ...
            // Create an S3 Bucket object
            var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
                    .bucket(bucket.name())
                    .contentType("text/html")
                    .source(new FileAsset("index.html"))
                    .build());
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can access it easily. You can do that by importing the Pulumi `Output` class:

```java
// ...
import com.pulumi.core.Output;
```

And adding a line to read the endpoint from the `Bucket` instance:

```java
// ...
public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // ...
            ctx.export("bucketEndpoint", Output.format("http://storage.googleapis.com/%s/%s", bucket.name(), bucketObject.name()));
        });
```

{{% /choosable %}}

{{% choosable language yaml %}}

Now that your `index.html` is in your bucket, modify the program to have the bucket serve `index.html` as a static website. To do that, set the bucket's `website` property, passing the filename to use as an `mainPageSuffix`. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```yaml
resources:
  my-bucket:
    type: gcp:storage:Bucket
    properties:
      website:
        mainPageSuffix: index.html
      location: US
      uniformBucketLevelAccess: true
```

Next, allow the contents of your bucket to be viewed anonymously over the Internet.

```yaml
resources:
  # ...
  my-bucket-binding:
    type: gcp:storage:BucketIAMBinding
    properties:
      bucket: ${my-bucket.name}
      role: "roles/storage.objectViewer"
      members: ["allUsers"]
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```yaml
resources:
  # ...
  index-object:
    type: gcp:storage:BucketObject
    properties:
      bucket: ${my-bucket}
      contentType: "text/html"
      source:
        Fn::FileAsset: ./index.html
```

Finally, at the end of the file, export the resulting bucket’s endpoint URL so you can access it easily:

```yaml
# ...
outputs:
  bucketName: ${my-bucket.url}
  bucketEndpoint: http://storage.googleapis.com/${my-bucket.name}/${index-object.name}
  ```

{{% /choosable %}}

Now update your stack to have your storage bucket serve your `index.html` file as a static website.

```bash
$ pulumi up
```

First, you will see a preview of your changes:

```
Previewing update (dev):

     Type                    Name            Plan       Info
     pulumi:pulumi:Stack              quickstart-dev
 ~   ├─ gcp:storage:Bucket            my-bucket              update     [diff: +website]
 +   └─ gcp:storage:BucketIAMBinding  my-bucket-IAMBinding   create
 +-  └─ gcp:storage:BucketObject      index.html             replace    [diff: ~contentType]

Outputs:
  + bucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"

Resources:
    + 1 to create
    ~ 1 to update
    +-1 to replace
    3 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Select `yes` to deploy the changes:

```
Do you want to perform this update? yes
Updating (dev):

     Type                     Name            Status      Info
    pulumi:pulumi:Stack              quickstart-dev
 ~   ├─ gcp:storage:Bucket            my-bucket              updated     [diff: +website]
 +   └─ gcp:storage:BucketIAMBinding  my-bucket-IAMBinding   created
 +-  └─ gcp:storage:BucketObject      index.html             replaced    [diff: ~contentType];
Outputs:
  + bucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"
    bucketName    : "gs://my-bucket-0167228"

Resources:
    + 1 created
    ~ 1 updated
    +-1 replaced
    3 changes. 1 unchanged

Duration: 8s
```

Finally, you can check out your new static website at the URL in the `Outputs` section of your update or you can make a `curl` request and see the contents of your `index.html` object printed out in your terminal.

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
