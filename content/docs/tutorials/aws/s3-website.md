---
title: "Host a Static Website on Amazon S3"
meta_desc: This tutorial will teach you to serve a static website hosted in a Amazon S3 bucket.
aliases: ["/docs/reference/tutorials/aws/tutorial-s3-website/"]
---

{{< github-buttons "aws-js-s3-folder" "aws-py-s3-folder" >}}

In this tutorial, we'll show you how to provision raw resources in AWS using the [@pulumi/aws] package. First, we'll create a Pulumi program that uploads files from the `www` directory to S3. Then, we'll configure the bucket to serve a website. We'll be using JavaScript in this tutorial, but you can also run through this example [in Python].

{{< aws-js-prereqs >}}

## Deploy the App

### Step 1: Create a new project from a template

Create a project directory, `s3website`, and change into it. Run [`pulumi new javascript --name myproject`]({{< relref "/docs/reference/cli/pulumi_new" >}}) to create a new project using the JavaScript template. Replace `myproject` with your desired project name.

```bash
$ mkdir s3website && cd s3website
$ pulumi new javascript --name myproject
```

### Step 2: Create a bucket and upload files

Open up `index.js` using your preferred text editor and add the following code. This creates a new S3 bucket, then iterates over the files in the `www` folder to create an S3 Object for each file.

```javascript
const aws = require("@pulumi/aws");
const pulumi = require("@pulumi/pulumi");
const mime = require("mime");

// Create an S3 bucket
let siteBucket = new aws.s3.Bucket("s3-website-bucket");

let siteDir = "www"; // directory for content files

// For each file in the directory, create an S3 object stored in `siteBucket`
for (let item of require("fs").readdirSync(siteDir)) {
    let filePath = require("path").join(siteDir, item);
    let object = new aws.s3.BucketObject(item, {
      bucket: siteBucket,
      source: new pulumi.asset.FileAsset(filePath),     // use FileAsset to point to a file
      contentType: mime.getType(filePath) || undefined, // set the MIME type of the file
    });
}

exports.bucketName = siteBucket.bucket; // create a stack export for bucket name
```

Notice how we are using the [@pulumi/aws] npm package to create an Amazon S3 bucket with [aws.s3.Bucket]. This uses the s3 module and the Bucket resource for the package. For each file in `www`, an [aws.s3.BucketObject] gets created, using the helper [pulumi.asset.FileAsset] to reference a local file.

In order to serve the files to a browser, the content type for each S3 object must be set. For this, the [NPM `mime` package](https://www.npmjs.com/package/mime) is used. Just like a regular Node program, Pulumi programs can use any Node.js package.

### Step 3: Create your website files

Create a subfolder of `s3website` called `www`. Download [favicon.png](/images/docs/examples/favicon.png) and save it to `www`.

Also save the following as `index.html`:

```html
<html>
  <head>
    <title>Hello S3</title><meta charset="UTF-8">
    <link rel="shortcut icon" href="/favicon.png" type="image/png">
  </head>
  <body>
    <p>Hello, world!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
  </body>
</html>
```

### Step 4: Install npm dependencies

Add and install the NPM dependencies:

```bash
$ npm install --save @pulumi/aws mime
```

### Step 5: Set your AWS region

Configure the AWS region to deploy to, such as `us-west-2`.

```bash
$ pulumi config set aws:region us-west-2
```

Notice how a new file, `Pulumi.website-testing.yaml`, got created in the root directory for your project next to your [Pulumi.yaml project file]({{< relref "/docs/intro/concepts/project.md" >}}). See [Defining and setting stack settings]({{< relref "/docs/intro/concepts/config.md#config-stack" >}}) for more information about this file.

### Step 6: Preview and deploy your resources

To preview your Pulumi program, run [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}). The command shows a preview of the resources that will be created and prompts you to proceed with the deployment. Select `yes` to create a stack component, a Bucket and two S3 Objects (one for each file in the `www` folder).

### Step 7: View your stack resources

#### **Pulumi Console**

To see the full details of the deployment and the resources that are now part of the stack, open the update link in a browser. The **Resources** tab on the Pulumi Console has a link to the AWS console for the provisioned EC2 instance.

#### **Pulumi CLI**

To see the name of the bucket that was created, run `pulumi stack output`. Note that an extra 7-digit identifier is appended to the name. All Pulumi resources add this identifier automatically, so that you don't have to manually create unique names.

```bash
$ pulumi stack output
Current stack outputs (1):
    OUTPUT                                           VALUE
    bucketName                                     s3-website-bucket-8533d8b
```

To see that the S3 bucket objects exist, you can either use the AWS Console (which is accessible from the Pulumi Console) or the AWS CLI:

```bash
$ aws s3 ls $(pulumi stack output bucketName)
2019-09-26 17:12:22      13731 favicon.png
2019-09-26 17:12:22        264 index.html
```

### Step 8: Add S3 website support

Next, configure the S3 bucket to serve the files on a browser. To do this, you use the [aws.s3.Bucket.websites] property and attach an [aws.s3.BucketPolicy] object.

Change the declaration of `siteBucket` to specify an `indexDocument`:

```javascript
...
// Update your siteBucket declaration to this
let siteBucket = new aws.s3.Bucket("s3-website-bucket", {
  website: {
    indexDocument: "index.html",
  },
});
...
```

Add the following code, which defines the S3 public read policy, applies it to the bucket, and defines a new stack output:

```javascript
// Create an S3 Bucket Policy to allow public read of all objects in bucket
// This reusable function can be pulled out into its own module
function publicReadPolicyForBucket(bucketName) {
  return JSON.stringify({
    Version: "2012-10-17",
    Statement: [{
      Effect: "Allow",
      Principal: "*",
      Action: [
        "s3:GetObject"
      ],
      Resource: [
        `arn:aws:s3:::${bucketName}/*` // policy refers to bucket name explicitly
      ]
    }]
  })
}

// Set the access policy for the bucket so all objects are readable
let bucketPolicy = new aws.s3.BucketPolicy("bucketPolicy", {
› bucket: siteBucket.bucket, // depends on siteBucket -- see explanation below
› policy: siteBucket.bucket.apply(publicReadPolicyForBucket)•
› › › › › // transform the siteBucket.bucket output property -- see explanation below
});

exports.websiteUrl = siteBucket.websiteEndpoint; // output the endpoint as a stack output
```

To make [all objects in the bucket publicly readable](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html), you'll need to create a [BucketPolicy][aws.s3.BucketPolicy] object. The definition of `bucketPolicy` illustrates how Pulumi tracks dependencies between resources. The property [aws.s3.Bucket.bucket] is an output property of type [pulumi.Output]---a marker class that encodes the relationship between resources in a Pulumi program. An object of type `Output` can be passed directly to the inputs of a resource constructor, such as the `bucket` property.

For the `policy` property, the IAM policy must include the target bucket name. Since the value of output properties are not known until the underlying resource is created (such as the generated name for the S3 bucket), you need to use the `apply` method of [pulumi.Output] rather than directly calling `publicReadPolicyForBucket`.

Whenever you need to create a dependency between resources, use the output property of one resource as the input to another one. Pulumi uses this information to create physical resources in the correct order.

### Step 9: Run your update

Run `pulumi up`, which shows the change to **update** the `Bucket` resource and **create** a new `BucketPolicy` resource. Select `yes` to confirm the changes. You should see an output similar to the following:

```bash
$ pulumi up
...

    Type                    Name               Status      Info
    pulumi:pulumi:Stack     s3-website-dev
~   ├─ aws:s3:Bucket        s3-website-bucket      updated     [diff: +website]
+   └─ aws:s3:BucketPolicy  bucketPolicy           created

Outputs:
    bucketName: "s3-website-bucket-8533d8b"
  + websiteUrl: "s3-website-bucket-8533d8b.s3-website-us-west-2.amazonaws.com"

Resources:
    + 1 created
    ~ 1 updated
    2 changes. 3 unchanged
```

### Step 10: View your static website

Open the site URL in a browser to see both the rendered HTML and the favicon:

```bash
$ pulumi stack output websiteUrl
s3-website-bucket-8533d8b.s3-website-us-west-2.amazonaws.com
```

<img src="/images/docs/quickstart/s3-website.png" alt="Hello S3 example" width="700">

## Clean Up

{{< cleanup >}}

## Summary

In this tutorial, we showed you how to use the `@pulumi/aws` package for fine-grain control over AWS resources.

You also learned how to work with the Pulumi CLI. To recap:

- Run `pulumi new javascript --name myproject` to create a new project using a JavaScript template.
- Run `pulumi up` to preview and update your infrastructure.
- Run `pulumi destroy` to clean up your resources.
- Run `pulumi stack rm` to delete your stack.

## Next steps

- [S3 Folder Pulumi Component](https://www.pulumi.com/docs/tutorials/aws/s3-folder-component/)
- [EC2 Linux WebServer Instance]({{< relref "/docs/tutorials/aws/ec2-webserver" >}})
- [Containers on ECS Fargate]({{< relref "/docs/tutorials/aws/ecs-fargate" >}})
- [API Gateways and Lambda]({{< relref "/docs/tutorials/aws/rest-api" >}})

<!-- markdownlint-disable url -->
[@pulumi/aws]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}
[aws.s3.Bucket]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3#Bucket" >}}
[aws.s3.Bucket.bucket]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3#Bucket" >}}
[aws.s3.BucketObject]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3#BucketObject" >}}
[pulumi.asset.FileAsset]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/asset#FileAsset" >}}
[aws.s3.BucketPolicy]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3#BucketPolicy" >}}
[aws.s3.Bucket.websites]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws/s3#Bucket" >}}
[pulumi.Output]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Output" >}}
[pulumi.Output.apply]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Output" >}}
[pulumi.Input]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Input" >}}
[pulumi.ComponentResource]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#ComponentResource" >}}
[Component]: {{< relref "/docs/intro/concepts/programming-model#components" >}}
[Pulumi Cloud]: {{< relref "/docs/tutorials/cloudfx" >}}
[in Python]: https://github.com/pulumi/examples/tree/master/aws-py-s3-folder
<!-- markdownlint-enable url -->
