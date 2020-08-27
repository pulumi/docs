---
title: Deploy the Changes | AWS
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to an AWS project.
weight: 7
menu:
  getstarted:
    parent: aws
    identifier: aws-deploy-changes

aliases: ["/docs/quickstart/aws/deploy-changes/"]
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                    Name            Plan       Info
     pulumi:pulumi:Stack     quickstart-dev
 +   └─ aws:s3:BucketObject  index.html                 create

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

     Type                     Name            Status      Info
     pulumi:pulumi:Stack      quickstart-dev
  +   └─ aws:s3:BucketObject  index.html                  created

Outputs:
    bucketName: "my-bucket-68e33ec"

Resources:
    + 1 created
    2 unchanged

Duration: 6s
```

Once the update has completed, rerun the command to list the contents of your bucket.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ aws s3 ls $(pulumi stack output bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ aws s3 ls $(pulumi stack output BucketName)
```

{{% /choosable %}}

Notice that your index.html file has been added:

```bash
2020-08-27 12:30:24         68 index.html
```

Now that your `index.html` is in your bucket, let's modify the program to have the bucket serve the file as a static website. First we need to set the `website` property on our bucket.

{{% choosable language javascript %}}

```javascript
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html",
    },
});
```

Next, your `index.html` object will need two changes: an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML:

```javascript
const bucketObject = new aws.s3.BucketObject("index.html", {
    acl: "public-read",
    contentType: "text/html",
    bucket: bucket,
    source: new pulumi.asset.FileAsset(filePath),
});
```

Finally, at the bottom of your program export the resulting bucket’s endpoint URL so we can easily access it:

```javascript
exports.bucketEndpoint = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const bucket = new aws.s3.Bucket("my-bucket", {
    website: {
        indexDocument: "index.html",
    },
});
```

Next, your `index.html` object will need two changes: an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML:

```typescript
const bucketObject = new aws.s3.BucketObject("index.html", {
    acl: "public-read",
    contentType: "text/html",
    bucket: bucket,
    source: new pulumi.asset.FileAsset(filePath),
});
```

Finally, at the bottom of your program export the resulting bucket’s endpoint URL so we can easily access it:

```typescript
export const bucketEndpoint = pulumi.interpolate`http://${bucket.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket = s3.Bucket('my-bucket',
    website={
        'index_document': 'index.html',
    })
```

Next, your `index.html` object will need two changes: an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML:

```python
bucketObject = s3.BucketObject(
    'index.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket,
    source=pulumi.FileAsset(filepath)
)
```

Finally, at the bottom of your program export the resulting bucket’s endpoint URL so we can easily access it:

```python
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
    Website: s3.BucketWebsiteArgs{
        IndexDocument: pulumi.String("index.html"),
    },
})
```

Next, your `index.html` object will need two changes: an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML:

```go
_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Acl:         pulumi.String("public-read"),
    ContentType: pulumi.String("text/html"),
    Bucket:      bucket.ID(),
    Source:      pulumi.NewFileAsset(filePath),
})
```

Finally, at the bottom of your program export the resulting bucket’s endpoint URL so we can easily access it:

```go
ctx.Export("bucketEndpoint", pulumi.Sprintf("http://%s", bucket.WebsiteEndpoint))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Add this import
using Pulumi.Aws.S3.Inputs;
```

```csharp
var bucket = new Bucket("my-bucket", new BucketArgs
{
    Website = new BucketWebsiteArgs
    {
        IndexDocument = "index.html"
    }
});
```

Next, your `index.html` object will need two changes: an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML:

```csharp
var bucketObject = new BucketObject("index.html", new BucketObjectArgs
{
    Acl = "public-read",
    ContentType = "text/html",
    Bucket = bucket.BucketName,
    Source = new FileAsset(filePath),
});
```

Finally, at the bottom of your program export the resulting bucket’s endpoint URL so we can easily access it:

```csharp
// Export the name of the bucket
this.BucketName = bucket.Id;
this.BucketEndpoint = Output.Format($"http://{bucket.WebsiteEndpoint}");
```

```csharp
[Output] public Output<string> BucketName { get; set; }
[Output] public Output<string> BucketEndpoint { get; set; }
```

{{% /choosable %}}

Now let's update our stack to have our S3 Bucket serve our `index.html` file as a static website.

```bash
$ pulumi up
```

First we will see a preview of our changes:

```
Previewing update (dev):

     Type                    Name            Plan       Info
     pulumi:pulumi:Stack     quickstart-dev
 ~   ├─ aws:s3:Bucket        my-bucket           update     [diff: +website]
 ~   └─ aws:s3:BucketObject  index.html          update     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: output<string>

Resources:
    ~ 2 to update
    1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Select `yes` to deploy all of the updates:

```
Do you want to perform this update? yes
Updating (dev):

     Type                     Name            Status      Info
     pulumi:pulumi:Stack      quickstart-dev
~   ├─ aws:s3:Bucket        my-bucket           updated     [diff: +website]
~   └─ aws:s3:BucketObject  index.html          updated     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: "http://my-bucket-b9c2eaa.s3-website-us-east-1.amazonaws.com"
    bucketName    : "my-bucket-b9c2eaa"

Resources:
    ~ 2 updated
    1 unchanged

Duration: 12s
```

Finally, you can checkout your new static website at the URL in the `Outputs` section of your update or you can make a `curl` request and see the contents of your `index.html` printed out in your terminal.

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
        <h1>Hello Pulumi</h1>
    </body>
</html>
```

Next you will destroy the resources.

{{< get-started-stepper >}}
