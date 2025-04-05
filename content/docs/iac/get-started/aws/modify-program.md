---
title_tag: Make an Update | AWS
title: Make an update
h1: "Get started with Pulumi and AWS"
meta_desc: This page provides an overview on how to update an AWS project from a Pulumi program.
weight: 6
menu:
    iac:
        name: Make an update
        parent: aws-get-started
        weight: 5

aliases:
- /docs/quickstart/aws/modify-program/
- /docs/get-started/aws/modify-program/
- /docs/clouds/aws/get-started/modify-program/
- /docs/quickstart/aws/deploy-changes/
- /docs/get-started/aws/deploy-changes/
- /docs/iac/get-started/aws/deploy-changes/
- /docs/clouds/aws/get-started/deploy-changes/
---

## Make an update

Now you will update your project to serve a static website out of your AWS S3 bucket. You will change
your code and then re-run `pulumi up` which will update your infrastructure.

### Add new resources

Pulumi knows how to evolve your current infrastructure to your project, both for the first deployment
as well as subseuqent updates.

To turn your bucket into a static website, start by adding three new AWS S3 resources:

1. [`BucketWebsiteConfigurationV2`](/registry/packages/aws/api-docs/s3/bucketwebsiteconfigurationv2/):
    configures your bucket as a website
2. [`BucketOwnershipControls`](/registry/packages/aws/api-docs/s3/bucketownershipcontrols/):
    allows bucket access controls to be configured
3. [`BucketPublicAccessBlock`](/registry/packages/aws/api-docs/s3/bucketpublicaccessblock/): permits
    public access to your bucket; this is disabled by default so you don't allow access over the Internet by accident

Open up {{< langfile >}} in your editor and add them right after your S3 bucket:

{{% choosable language "javascript,typescript" %}}

```typescript
// Bucket...

// Turn the bucket into a website:
const website = new aws.s3.BucketWebsiteConfigurationV2("website", {
    bucket: bucket.id,
    indexDocument: {
        suffix: "index.html",
    },
});

// Permit access control configuration:
const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter"
    }
});

// Enable public access to the website:
const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Bucket ...

# Turn the bucket into a website:
website = s3.BucketWebsiteConfigurationV2("website",
    bucket=bucket.id,
    index_document={
        "suffix": "index.html",
    })

# Permit access control configuration:
ownership_controls = s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule={
        "object_ownership": 'ObjectWriter',
    },
)

# Enable public access to the website:
public_access_block = s3.BucketPublicAccessBlock(
    'public-access-block', bucket=bucket.id, block_public_acls=False
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Bucket ...

// Turn the bucket into a website:
website, err := s3.NewBucketWebsiteConfigurationV2(ctx, "website", &s3.BucketWebsiteConfigurationV2Args{
    Bucket: bucket.ID(),
    IndexDocument: &s3.BucketWebsiteConfigurationV2IndexDocumentArgs{
        Suffix: pulumi.String("index.html"),
    },
})
if err != nil {
    return err
}

// Permit access control configuration:
ownershipControls, err := s3.NewBucketOwnershipControls(ctx, "ownership-controls", &s3.BucketOwnershipControlsArgs{
    Bucket: bucket.ID(),
    Rule: &s3.BucketOwnershipControlsRuleArgs{
        ObjectOwnership: pulumi.String("ObjectWriter"),
    },
})
if err != nil {
    return err
}

// Enable public access to the website:
publicAccessBlock, err := s3.NewBucketPublicAccessBlock(ctx, "public-access-block", &s3.BucketPublicAccessBlockArgs{
    Bucket:          bucket.ID(),
    BlockPublicAcls: pulumi.Bool(false),
})
if err != nil {
    return err
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Bucket ...

// Turn the bucket into a website:
var website = new BucketWebsiteConfigurationV2("website", new()
{
    Bucket = bucket.Id,
    IndexDocument = new BucketWebsiteConfigurationV2IndexDocumentArgs
    {
        Suffix = "index.html",
    },
});

// Permit access control configuration:
var ownershipControls = new BucketOwnershipControls("ownership-controls", new()
{
    Bucket = bucket.Id,
    Rule = new BucketOwnershipControlsRuleArgs
    {
        ObjectOwnership = "ObjectWriter",
    },
});

// Enable public access to the website:
var publicAccessBlock = new BucketPublicAccessBlock("public-access-block", new()
{
    Bucket = bucket.Id,
    BlockPublicAcls = false,
});
```

Also make sure you've imported the additional types being used at the top of the file:

```csharp
using Pulumi.Aws.S3.Inputs;
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Bucket ...

// Turn the bucket into a website:
var website = new BucketWebsiteConfigurationV2("website", BucketWebsiteConfigurationV2Args.builder()
    .bucket(bucket.id())
    .indexDocument(BucketWebsiteConfigurationV2IndexDocumentArgs.builder()
        .suffix("index.html")
        .build())
    .build());

// Permit access control configuration:
var ownershipControls = new BucketOwnershipControls("ownershipControls", BucketOwnershipControlsArgs.builder()
    .bucket(bucket.id())
    .rule(BucketOwnershipControlsRuleArgs.builder()
        .objectOwnership("ObjectWriter")
        .build())
    .build());

// Enable public access to the website:
var publicAccessBlock = new BucketPublicAccessBlock("publicAccessBlock", BucketPublicAccessBlockArgs.builder()
    .bucket(bucket.id())
    .blockPublicAcls(false)
    .build());
```

Also replace the imports at the top with this so you have access to all the new types:

```java
import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.asset.FileAsset;
import com.pulumi.resources.*;

import com.pulumi.aws.s3.*;
import com.pulumi.aws.s3.inputs.*;

import java.util.Map;
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# ...
resources:
  # Bucket ...

  # Turn the bucket into a website:
  website:
    type: aws:s3:BucketWebsiteConfigurationV2
    properties:
      bucket: ${my-bucket.id}
      indexDocument:
        suffix: index.html

  # Permit access control configuration:
  ownership-controls:
    type: aws:s3:BucketOwnershipControls
    properties:
      bucket: ${my-bucket.id}
      rule:
        objectOwnership: ObjectWriter

  # Enable public access to the website:
  public-access-block:
    type: aws:s3:BucketPublicAccessBlock
    properties:
      bucket: ${my-bucket.id}
      blockPublicAcls: false
```

{{% /choosable %}}

Notice that resources can reference each other, which forms automatic dependencies between them.
Pulumi uses this information to parallelize deployments safely.

### Add an index.html

Next, add a new file called `index.html` to your current directory with these contents:

```html
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Then open {{< langfile >}} and create a [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) after the three other new resources:

{{% choosable language "javascript,typescript" %}}

```typescript
// Other resources ...

// Create an S3 Bucket object
const bucketObject = new aws.s3.BucketObject("index.html", {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset("index.html"),
    contentType: "text/html",
    acl: "public-read",
}, { dependsOn: [ownershipControls, publicAccessBlock] });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Other resources ...

# Create an S3 Bucket object
bucket_object = s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[ownership_controls, public_access_block]),
)
```

{{% /choosable %}}

{{% choosable language go %}}

Create a new [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself:

```go
// Other resources ...

// Create an S3 Bucket object
_, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
    Bucket:      bucket.ID(),
    Source:      pulumi.NewFileAsset("index.html"),
    ContentType: pulumi.String("text/html"),
    Acl:         pulumi.String("public-read"),
}, pulumi.DependsOn([]pulumi.Resource{ownershipControls,publicAccessBlock}))
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

Create a new [`BucketObject`](/registry/packages/aws/api-docs/s3/bucketobject/) right after creating the bucket itself:

```csharp
// Other resources ...

// Create an S3 Bucket object
var bucketObject = new BucketObject("index.html", new()
{
    Bucket = bucket.Id,
    Source = new FileAsset("index.html"),
    ContentType = "text/html",
    Acl = "public-read",
}, new CustomResourceOptions
{
    DependsOn = new Resource[]
    {
        ownershipControls,
        publicAccessBlock,
    },
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Other resources ...

// Create an S3 Bucket object
var bucketObject = new BucketObject("index.html", BucketObjectArgs.builder()
    .bucket(bucket.id())
    .source(new FileAsset("index.html"))
    .contentType("text/html")
    .acl("public-read")
    .build(), CustomResourceOptions.builder()
        .dependsOn(
            ownershipControls,
            publicAccessBlock)
        .build());
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
# ...
resources:
  # Other resources ...

  # Create an S3 Bucket object
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket.id}
      source:
        fn::fileAsset: index.html
      contentType: text/html
      acl: public-read
    options:
      dependsOn:
        - ${ownership-controls}
        - ${public-access-block}
```

{{% /choosable %}}

This uploads the `index.html` file to your bucket using a Pulumi concept called an [asset](/docs/iac/concepts/assets-archives/#assets).

The bucket object also declares that it [`dependsOn`](/docs/concepts/options/dependson/) the other resources. That is because
those other resources need to be created first so that AWS permits the object's `public-acl` grant. Pulumi usually tracks dependencies
automatically but these ones are invisible to Pulumi because those specific resources cause side-effects within AWS.

### Export the website URL

Now to export the website's URL for easy access add this to the end of your program:

{{% choosable language javascript %}}

```javascript
// Export the bucket's autoassigned URL:
exports.url = pulumi.interpolate`http://${website.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
// Export the bucket's autoassigned URL:
export const url = pulumi.interpolate`http://${website.websiteEndpoint}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Export the bucket's autoassigned URL:
pulumi.export('url', pulumi.Output.concat('http://', website.website_endpoint))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Export the bucket's autoassigned URL:
ctx.Export("url", website.WebsiteEndpoint.ApplyT(func(websiteEndpoint string) (string, error) {
    return fmt.Sprintf("http://%v", websiteEndpoint), nil
}).(pulumi.StringOutput))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Export the bucket's autoassigned URL:
return new Dictionary<string, object?>
{
    // ...
    ["url"] = website.WebsiteEndpoint.Apply(websiteEndpoint => $"http://{websiteEndpoint}"),
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Export the bucket's autoassigned URL:
ctx.export("url", website.websiteEndpoint().applyValue(
    websiteEndpoint -> String.format("http://%s", websiteEndpoint)));
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# ...
outputs:
  # ...
  url: http://${website.websiteEndpoint}
```

{{% /choosable %}}

We prepend `http://` using a helper because `websiteEndpoint` is [an output property](/docs/iac/concepts/inputs-outputs/#outputs)
that AWS assigns at deployment time, not a raw string, meaning its value isn't known in advance.

### Deploy the changes

To deploy the changes, run `pulumi up` again and it will figure out the deltas:

```bash
$ pulumi up
```

Just like the first time you will see a preview of the changes before they happen:

```
Previewing update (dev):

     Type                                    Name                 Plan       Info
     pulumi:pulumi:Stack                     quickstart-dev
 +   ├─ aws:s3:BucketWebsiteConfigurationV2  website              create
 +   ├─ aws:s3:BucketOwnershipControls       ownership-controls   create
 +   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  create
 +   └─ aws:s3:BucketObject                  index.html           create

Outputs:
  + url: output<string>

Resources:
    + 4 to create
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
 +   └─ aws:s3:BucketObject                  index.html           created (0.53s)

Outputs:
  + url: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
    bucketName    : "my-bucket-dfd6bd0"

Resources:
    + 4 created
    4 changes. 1 unchanged

Duration: 8s
```

In just a few seconds, your new website will be ready. Curl the endpoint to see it live:

```bash
$ curl $(pulumi stack output url)
```

This will reveal your new website!

```bash
<html>
    <body>
        <h1>Hello, Pulumi!</h1>
    </body>
</html>
```

Feel free to experiment, such as changing the contents of `index.html` and redeploying.

Next, let's wrap this website up into an infrastructure abstraction.

{{< get-started-stepper >}}
