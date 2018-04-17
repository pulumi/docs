---
title: Part 2. Infrastructure as Software
---

<!-- Common links -->
[@pulumi/aws]: /packages/pulumi-aws/index.html
[aws.s3.Bucket]: /packages/pulumi-aws/classes/_s3_bucket_.bucket.html
[aws.s3.BucketObject]: /packages/pulumi-aws/classes/_s3_bucketobject_.bucketobject.html
[pulumi.asset.FileAsset]: /packages/pulumi/classes/_asset_asset_.fileasset.html
[aws.s3.BucketPolicy]: /packages/pulumi-aws/classes/_s3_bucketpolicy_.bucketpolicy.html
[aws.s3.Bucket.websites]: /packages/pulumi-aws/classes/_s3_bucket_.bucket.html#websites
[pulumi.Output]: /packages/pulumi/classes/_resource_.output.html
[pulumi.Output.apply]: /packages/pulumi/classes/_resource_.output.html#apply
[pulumi.Input]: /packages/pulumi/modules/_resource_.html#input

<!-- End common links -->

Now that you've created your [first Pulumi program on AWS](./part1.html), let's explore the benefits of using a programming language to define infrastructure. You can write regular JavaScript code (with conditionals, loops, and functions) and use NPM packages. You can then convert your code into a reusable component that you share with your team or the community. 

In this section, we'll create a simple website hosted on AWS S3 and show how to convert it into a reusable component.

{% include aws-resource-note.md %}

## Setup

1.  Create a folder `s3website`:

    ```bash
    $ mkdir s3website
    $ cd s3website
    ```

1.  Create an empty project with `pulumi new`:

    ```
    $ pulumi new javascript
    ```

1.  Initialize a Pulumi repository with `pulumi init`, using your GitHub username. (Note: this step will be removed in the future.)

    ```
    $ pulumi init --owner gitHubUsername
    ```

## A static website hosted on S3

In this example, we'll create a simple static website in a local `www` folder and write a Pulumi program to create an S3 bucket and objects. 

### Create a bucket and upload files 

First, we'll create a program that uploads files to S3; in the next section, we'll configure the bucket to serve a website.

1.  Edit `index.js` and replace with the following. The code creates a new S3 bucket, then iterates over the files in the `www` folder to create an S3 Object for each file.

    In order to serve the files to a browser, the content type for each S3 Object must be set. For this, we use the [NPM `mime` package](https://www.npmjs.com/package/mime). Just like a regular Node program, Pulumi programs can use any Node.js package.

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

    exports.bucketName = siteBucket.bucketName; // create a stack export for bucket name
    ```

    Here, we're again using the [@pulumi/aws] package to create an [aws.s3.Bucket]. For each file in `www`, we create an [aws.s3.BucketObject], using the helper [pulumi.asset.FileAsset] to reference a local file.

1.  Create some files in `www`:
    - Create a subfolder of `s3website` called `www`.
    - Download [favicon.png](/examples/favicon.png) and save it to `www`.
    - In `www`, save the following as `index.html`:

      ```html
      <html><head>
          <title>Hello S3</title><meta charset="UTF-8">
          <link rel="shortcut icon" href="/favicon.png" type="image/png">
      </head>
      <body><p>Hello, world!</p><p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
      </body></html>
      ```

1.  Add and install the NPM dependencies:

    ```bash
    $ npm install --save @pulumi/pulumi @pulumi/aws mime
    ```

1.  Create a new [stack](../reference/stack.html) via `pulumi stack init website-testing`.

1.  Configure the AWS region to deploy to, such as `us-west-2`. After this step, a new file `Pulumi.website-testing.yaml` is created, next to your [Pulumi.yaml project file](../reference/project.html). See [Defining and setting stack settings](../reference/config.html) for more information about this file.

    ```bash
    $ pulumi config set aws:region us-west-2
    ```

1.  Run `pulumi preview` to see what AWS resources will be created. As expected, a stack virtual component would be created, along with a new Bucket and two S3 Objects --- one for each file in the `www` folder.

    ```
    $ pulumi preview
    Previewing stack 'website-testing' in the Pulumi Cloud ☁️
    Previewing changes:

    pulumi:Stack("s3website-website-testing"): Completed
    aws:Bucket("s3-website-bucket"):           + Would create
    aws:BucketObject("favicon.png"):           + Would create
    aws:BucketObject("index.html"):            + Would create
    info: 4 changes previewed:
        + 4 resources to create
    ```

1.  Now, provision resources via `pulumi update`:

    ```
    $ pulumi update
    Updating stack 'website-testing' in the Pulumi Cloud ☁️
    Performing changes:

    pulumi:Stack("s3website-website-testing"): Completed
    aws:Bucket("s3-website-bucket"):           + Created
    aws:BucketObject("favicon.png"):           + Created
    aws:BucketObject("index.html"):            + Created
    info: 4 changes performed:
        + 4 resources created
    Update duration: 7.206358082s

    Permalink: https://pulumi.com/lindydonna/s3website/s3website/website-testing/updates/1
    ```

1.  To see the name of the bucket that was created, run `pulumi stack export`. Note that an extra 7-digit identifier is appended to the name. All Pulumi resources add this identifier automatically, so that you don't have to manually create unique names.

    ```
    $ pulumi stack output
    Current stack outputs (1):
        OUTPUT                                           VALUE
        bucketName                                       s3-website-bucket2-c198168
    ```

1.  To see that the S3 objects exist, you can either use the AWS Console or the AWS CLI:

    ```bash
    $ aws s3api list-objects --bucket $(pulumi stack output bucketName)
    ```

### Add S3 website support

In this section, we configure the S3 bucket to serve the files to a browser. To do this, we use the [aws.s3.Bucket.websites] property and attach a [aws.s3.BucketPolicy] object. 

1.  Change the declaration of `siteBucket` to specify an `indexDocument`:

    ```javascript
    // Create a bucket and expose a website index document
    let siteBucket = new aws.s3.Bucket("s3-website-bucket", {
        websites: [{                      // <-- ADD THESE LINES  
            indexDocument: "index.html",  
        }],
    });
    ```

1.  To create a reusable function that applies the [S3 public read policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html) to all objects in a bucket, add the following definition. Since the IAM policy requires an ARN that includes the bucket name, the function takes `bucketName` as a parameter.

    ```javascript
    // Create an S3 Bucket Policy to allow public read of all objects in bucket
    function publicReadPolicyForBucket(bucketName) {
        return JSON.stringify({
            Version: "2012-10-17",
            Statement: [{
                // Sid: "PublicReadGetObject",
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
    ```

1.  To apply the policy to an object, we'll create an instance of [aws.s3.BucketPolicy]. Here, there is dependency between the bucket policy and the bucket itself:  the AWS resource `siteBucket` must be created _before_ the bucket policy object is applied. Dependencies between cloud resources are expressed using object [output properties](../reference/programming-model.html#outputs). For example, in [aws.s3.Bucket], most properties return an object of type [pulumi.Output], a marker class that encodes the relationship between resources in a Pulumi program. 

    There is a corresponding class [pulumi.Input] that accepts a value of type [pulumi.Output], and most input properties on resources have this type. So, the use of pulumi.Output is transparent to most Pulumi programs.

    To directly read the value of an output property, use the [pulumi.Output.apply] method. In this example, the function `publicReadPolicyForBucket` requires a bucket name as a string. Since Pulumi generates a unique name for the bucket, its name is not known before creation. So, the code below uses `siteBucket.bucket.apply` to transform the output using `publicReadPolicyForBucket`.

    Add the following code to create a bucket policy:
    
    ```javascript
    // ADD THIS  // Set the access policy for the bucket so all objects are readable
    let bucketPolicy = new aws.s3.BucketPolicy("bucketPolicy", {
        bucket: siteBucket.bucket, // refer to the bucket created earlier
        policy: siteBucket.bucket.apply(publicReadPolicyForBucket) // use output property `siteBucket.bucket`
    });
    ```

1.  Finally, add a new stack output for the website URL:

    ```javascript
    exports.websiteUrl = siteBucket.websiteEndpoint; // <-- ADD THIS LINE
    ```

1.  Now, run the preview operation, which shows the planned change to update the Bucket resource and create a new BucketPolicy resource:

    ```
    $ pulumi preview
    Previewing stack 'website-testing' in the Pulumi Cloud ☁️
    Previewing changes:

    pulumi:Stack("s3website-website-testing"): Completed
    aws:Bucket("s3-website-bucket"):           ~ Would update. Changes: + websites
    aws:BucketPolicy("bucketPolicy"):          + Would create
    info: 2 changes previewed:
        + 1 resource to create
        ~ 1 resource to update
          3 resources unchanged
    ```

1.  Run `pulumi update` to deploy the changes:

    ```
    $ pulumi update
    Updating stack 'website-testing' in the Pulumi Cloud ☁️
    Performing changes:

    pulumi:Stack("s3website-website-testing"): Completed
    aws:Bucket("s3-website-bucket"):           ~ Updated. Changes: + websites
    aws:BucketPolicy("bucketPolicy"):          + Created
    info: 2 changes performed:
        + 1 resource created
        ~ 1 resource updated
          3 resources unchanged
    Update duration: 4.289355841s

    Permalink: https://pulumi.com/lindydonna/s3website/s3website/website-testing/updates/17
    ```

1.  Retrieve the site URL and open in a browser, to see both the rendered HTML and the favicon:

    ```
    $ pulumi stack output websiteUrl
    s3-website-bucket-8533d8b.s3-website-us-west-2.amazonaws.com
    ```

    ![Hello S3 example](images/part2-website.png){:width="700px"}

## Create a Pulumi component 🚧

- TODO: Packages and components

## Clean up

## Next steps 🚧

TODO finish