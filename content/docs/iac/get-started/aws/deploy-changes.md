---
title_tag: Deploy the Changes | AWS
title: Deploy changes
h1: "Pulumi & AWS: Deploy changes"
meta_desc: Learn how to deploy changes to an AWS project in this guide.
weight: 7
aliases:
  - /docs/quickstart/aws/deploy-changes/
  - /docs/get-started/aws/deploy-changes/
  - /docs/clouds/aws/get-started/deploy-changes/
search:
  keywords:
    - AWS
    - Bucket
    - deploy changes
    - bucket object
    - public access
---

Now let's deploy your changes.

```bash
$ pulumi up
```

Pulumi will run the [`preview`](/docs/iac/cli/commands/pulumi_preview/) step of the update, which computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                    Name            Plan
     pulumi:pulumi:Stack     quickstart-dev
 +   └─ aws:s3:BucketObject  index.html      create

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` will proceed with the update and upload the `index.html` file to your bucket:

```
Do you want to perform this update? yes
Updating (dev):

     Type                    Name            Status
     pulumi:pulumi:Stack     quickstart-dev
 +   └─ aws:s3:BucketObject  index.html      created (0.98s)


Outputs:
    bucketName: "my-bucket-58ce361"

Resources:
    + 1 created
    2 unchanged

Duration: 3s
```

Once the update has completed, you can verify the object was created in your bucket by checking the AWS Console or by running the following AWS CLI command:

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
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

Notice that your `index.html` file has been added to the bucket:

```bash
2023-04-20 17:01:06        118 index.html
```

Now that `index.html` is in the bucket, update the program to turn the bucket into a website.

## Update the program

Add a new [`BucketWebsiteConfiguration`](/registry/packages/aws/api-docs/s3/bucketwebsiteconfigurationv2/) resource to make `index.html` the home page of the website:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const website = new aws.s3.BucketWebsiteConfigurationV2("website", {
    bucket: bucket.id,
    indexDocument: {
        suffix: "index.html",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
website = s3.BucketWebsiteConfigurationV2("website",
    bucket=bucket.id,
    index_document={
        "suffix": "index.html",
    })
```

{{% /choosable %}}

{{% choosable language go %}}

```go
website, err := s3.NewBucketWebsiteConfigurationV2(ctx, "website", &s3.BucketWebsiteConfigurationV2Args{
    Bucket: bucket.ID(),
    IndexDocument: &s3.BucketWebsiteConfigurationV2IndexDocumentArgs{
        Suffix: pulumi.String("index.html"),
    },
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var website = new Aws.S3.BucketWebsiteConfigurationV2("website", new()
{
    Bucket = bucket.Id,
    IndexDocument = new Aws.S3.Inputs.BucketWebsiteConfigurationV2IndexDocumentArgs
    {
        Suffix = "index.html",
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.aws.s3.BucketWebsiteConfigurationV2;
import com.pulumi.aws.s3.BucketWebsiteConfigurationV2Args;
import com.pulumi.aws.s3.inputs.BucketWebsiteConfigurationV2IndexDocumentArgs;

var website = new BucketWebsiteConfigurationV2("website", BucketWebsiteConafigurationV2Args.builder()
    .bucket(bucket.id())
    .indexDocument(BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
        .suffix("index.html")
        .build())
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
website:
  type: aws:s3:BucketWebsiteConfigurationV2
  properties:
    bucket: ${my-bucket.id}
    indexDocument:
      suffix: index.html
```

{{% /choosable %}}

Lastly, you'll make a few adjustments to make these resources accessible on the Internet.

For the bucket itself, you'll need two new resources: a [`BucketOwnershipControls`](/registry/packages/aws/api-docs/s3/bucketownershipcontrols/) resource, to define the bucket's file-ownership settings, and a [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/) resource to allow the bucket to be accessed publicly.

For the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobjectv2/), you'll need an access-control (ACL) setting of `public-read` to allow the page to be accessed anonymously (e.g., in a browser) and a content type of `text/html` to tell AWS to serve the file as a web page. Add the following lines to your program, updating the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobjectv2/) in place:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}

```typescript
const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter"
    }
});

const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});

const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("./index.html"),
    contentType: "text/html",
    acl: "public-read",
}, { dependsOn: [publicAccessBlock,ownershipControls,website] });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
ownership_controls = s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule={
        "object_ownership": 'ObjectWriter',
    },
)

public_access_block = s3.BucketPublicAccessBlock(
    'public-access-block', bucket=bucket.id, block_public_acls=False
)

bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[public_access_block, ownership_controls, website]),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
	"fmt"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
    Bucket: bucket.ID(),
    Rule: &s3.BucketOwnershipControlsRuleArgs{
        ObjectOwnership: pulumi.String("ObjectWriter"),
    },
})
if err != nil {
    return err
}

publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
    Bucket:          bucket.ID(),
    BlockPublicAcls: pulumi.Bool(false),
})
if err != nil {
    return err
}

_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:      bucket.ID(),
    Source:      pulumi.NewFileAsset("index.html"),
    ContentType: pulumi.String("text/html"),
    Acl:         pulumi.String("public-read"),
}, pulumi.DependsOn([]pulumi.Resource{
			publicAccessBlock,
			ownershipControls,
			website,
}))
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var ownershipControls = new BucketOwnershipControls("ownership-controls", new()
{
    Bucket = bucket.Id,
    Rule = new BucketOwnershipControlsRuleArgs
    {
        ObjectOwnership = "ObjectWriter",
    },
});

var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", new()
{
    Bucket = bucket.Id,
    BlockPublicAcls = false,
});

var indexHtml = new BucketObject("index.html", new()
{
    Bucket = bucket.Id,
    Source = new FileAsset("./index.html"),
    ContentType = "text/html",
    Acl = "public-read",
}, new CustomResourceOptions
{
    DependsOn = new Resource[]
    {
        publicAccessBlock,
        ownershipControls,
        website,
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.aws.s3.BucketOwnershipControls;
import com.pulumi.aws.s3.BucketOwnershipControlsArgs;
import com.pulumi.aws.s3.inputs.BucketOwnershipControlsRuleArgs;
import com.pulumi.aws.s3.BucketPublicAccessBlock;
import com.pulumi.aws.s3.BucketPublicAccessBlockArgs;
import com.pulumi.resources.CustomResourceOptions;
import com.pulumi.asset.FileAsset;

var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
    .bucket(bucket.id())
    .rule(BucketOwnershipControlsRuleArgs.builder()
        .objectOwnership("ObjectWriter")
        .build())
    .build());

var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
    .bucket(bucket.id())
    .blockPublicAcls(false)
    .build());

var indexHtml = new BucketObject("index.html", BucketObjectArgs.builder()
    .bucket(bucket.id())
    .source(new FileAsset("./index.html"))
    .contentType("text/html")
    .acl("public-read")
    .build(), CustomResourceOptions.builder()
        .dependsOn(
            publicAccessBlock,
            ownershipControls,
            website)
        .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml

resources:
  # ...

  ownership-controls:
    type: aws:s3:BucketOwnershipControls
    properties:
      bucket: ${my-bucket.id}
      rule:
        objectOwnership: ObjectWriter

  public-access-block:
    type: aws:s3:BucketPublicAccessBlock
    properties:
      bucket: ${my-bucket.id}
      blockPublicAcls: false

  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket.id}
      source:
        fn::fileAsset: ./index.html
      contentType: text/html
      acl: public-read
    options:
      dependsOn:
        - ${public-access-block}
        - ${ownership-controls}
        - ${website}
```

{{% /choosable %}}

Note that the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobjectv2/) also includes the Pulumi resource option [`dependsOn`](/docs/concepts/options/dependson/). This setting tells Pulumi that the [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobjectv2/) relies indirectly on the [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/), which is responsible for enabling public access to its contents. If you omitted this setting, the attempt to grant `public-read` access to `index.html` would fail, as all S3 buckets and their objects are blocked from public access by default.

Finally, at the end of the program, export the resulting bucket’s endpoint URL so you can browse to it easily:

{{% choosable language javascript %}}

```javascript
exports.bucketEndpoint = pulumi.interpolate`http://${website.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
export const bucketEndpoint = pulumi.interpolate`http://${website.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', website.website_endpoint))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("bucketEndpoint", website.WebsiteEndpoint.ApplyT(func(websiteEndpoint string) (string, error) {
    return fmt.Sprintf("http://%v", websiteEndpoint), nil
}).(pulumi.StringOutput))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return new Dictionary<string, object?>
{
    // ...
    ["bucketEndpoint"] = website.WebsiteEndpoint.Apply(websiteEndpoint => $"http://{websiteEndpoint}"),
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// ...
ctx.export("bucketEndpoint", website.websiteEndpoint().applyValue(websiteEndpoint -> String.format("http://%s", websiteEndpoint)));
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  # ...
  bucketEndpoint: http://${website.websiteEndpoint}
```

{{% /choosable %}}

## Deploy the website

{{% notes type="warning" %}}

You may need to grant permissions to your S3 object, `index.html`. Ensure it has public read access if intended.

{{% /notes %}}

Update your stack to deploy these changes to AWS:

```bash
$ pulumi up
```

Again, you'll see a preview of the changes before they're deployed:

```
Previewing update (dev):

     Type                                    Name                 Plan       Info
     pulumi:pulumi:Stack                     quickstart-dev
 +   ├─ aws:s3:BucketWebsiteConfigurationV2  website              create
 +   ├─ aws:s3:BucketOwnershipControls       ownership-controls   create
 +   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  create
 ~   └─ aws:s3:BucketObject                  index.html           update     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: output<string>

Resources:
    + 2 to create
    ~ 2 to update
    4 changes. 1 unchanged

Do you want to perform this update?
> yes
  no
  details
```

Choose `yes` to perform the deployment:

```
Do you want to perform this update? yes
Updating (dev):

     Type                                    Name                 Status              Info
     pulumi:pulumi:Stack.                    quickstart-dev
 +   ├─ aws:s3:BucketWebsiteConfigurationV2  website              created (0.51s)
 +   ├─ aws:s3:BucketOwnershipControls.      ownership-controls   created (0.84s)
 +   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  created (1s)
 ~   └─ aws:s3:BucketObject                  index.html           updated (0.53s)     [diff: ~acl,contentType]

Outputs:
  + bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
    bucketName    : "my-bucket-dfd6bd0"

Resources:
    + 2 created
    ~ 2 updated
    4 changes. 1 unchanged

Duration: 8s
```

When the deployment completes, you can check out your new website at the URL in the [`Outputs`](/docs/iac/concepts/inputs-outputs/#outputs) section of your update or make a `curl` request and see the contents of `index.html` in your terminal:

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

Next, you'll destroy the resources.

{{< get-started-stepper >}}
