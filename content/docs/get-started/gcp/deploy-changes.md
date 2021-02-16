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

First, Pulumi will run the `preview` step of the update, which computes the minimally disruptive change to achieve the desired state described by the program.

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

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
$ gsutil ls $(pulumi stack output BucketName)
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
    content: fs.readFileSync("site/index.html").toString(),
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
    content: fs.readFileSync("site/index.html").toString(),
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
    bucket=bucket,
    role="roles/storage.objectViewer",
    members=["allUsers"]
)
```

Also, change the content type of your `index.html` object so that it is served as HTML.

```python
bucketObject = storage.BucketObject(
    'index.html',
    bucket=bucket,
    content_type='text/html',
    content=open('site/index.html').read(),
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
    Bucket:  bucket.Name,
    Content: pulumi.String(string(htmlContent)),
})
if err != nil {
    return err
}
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```go
ctx.Export("bucketEndpoint", pulumi.Sprintf("http://storage.googleapis.com/%s/%s", bucket.Name, bucketObject.Name))
```

{{% /choosable %}}

{{% choosable language csharp %}}
Now that `index.html` is in your bucket, modify the program file to have the bucket serve `index.html` as a static website.

First, set the `website` property on your bucket. And, to align with Google Cloud Storage recommendations, set uniform bucket-level access on the bucket to `true`.

```csharp
// Add this import
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
    Content = htmlString,
});
```

Finally, at the end of the program file, export the resulting bucket’s endpoint URL so you can easily access it:

```csharp
this.BucketEndpoint = Output.Format($"http://storage.googleapis.com/{bucket.Name}/{bucketObject.Name}");
```

```csharp
[Output] public Output<string> BucketEndpoint { get; set; }
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

Outputs:
  + BucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"

Resources:
    ~ 2 to update
    1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Select `yes` to deploy both changes:

```
Do you want to perform this update? yes
Updating (dev):

     Type                     Name            Status      Info
    pulumi:pulumi:Stack              quickstart-dev
 ~   ├─ gcp:storage:Bucket            my-bucket              updated     [diff: +website]
 +   └─ gcp:storage:BucketIAMBinding  my-bucket-IAMBinding   created

Outputs:
  + BucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"
    BucketName    : "gs://my-bucket-0167228"

Resources:
    + 1 created
    ~ 1 updated
    2 changes. 2 unchanged

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
$ curl $(pulumi stack output BucketEndpoint)
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
