---
title: Part 2. Infrastructure as Software
---

<!-- Common links -->
[@pulumi/aws]: /packages/pulumi-aws/index.html
[aws.s3.Bucket]: /packages/pulumi-aws/classes/_s3_bucket_.bucket.html
[aws.s3.Bucket.bucket]: /packages/pulumi-aws/classes/_s3_bucket_.bucket.html#bucket
[aws.s3.BucketObject]: /packages/pulumi-aws/classes/_s3_bucketobject_.bucketobject.html
[pulumi.asset.FileAsset]: /packages/pulumi/classes/_asset_asset_.fileasset.html
[aws.s3.BucketPolicy]: /packages/pulumi-aws/classes/_s3_bucketpolicy_.bucketpolicy.html
[aws.s3.Bucket.websites]: /packages/pulumi-aws/classes/_s3_bucket_.bucket.html#websites
[pulumi.Output]: /packages/pulumi/classes/_resource_.output.html
[pulumi.Output.apply]: /packages/pulumi/classes/_resource_.output.html#apply
[pulumi.Input]: /packages/pulumi/modules/_resource_.html#input
[pulumi.ComponentResource]: /packages/pulumi/classes/_resource_.componentresource.html
[Component]: ../reference/programming-model.html#components
[s3-folder]: https://github.com/pulumi/examples/tree/master/aws-js-s3-folder
[s3-folder-component]: https://github.com/pulumi/examples/tree/master/aws-js-s3-folder-component

<!-- End common links -->

Now that you've created your [first Pulumi program on AWS](./part1.html), let's explore the benefits of using a programming language to define infrastructure. You can write regular JavaScript code (with conditionals, loops, and functions) and use NPM packages. You can then convert your code into a reusable component that you share with your team or the community. 

In this section, we'll create a static website hosted on AWS S3 and show how to convert it into a reusable component.

{% include aws-resource-note.md %}

## Setup

1.  Create a folder `s3website`:

    ```bash
    $ mkdir s3website
    $ cd s3website
    ```

1.  Create an empty project with `pulumi new`:

    ```bash
    $ pulumi new javascript
    ```

## A static website hosted on S3

First, we'll create a Pulumi program that uploads files from the `www` directory to S3. Then, we'll configure the bucket to serve a website.

### Create a bucket and upload files 

1.  Edit `index.js` and replace with the following. The code creates a new S3 bucket, then iterates over the files in the `www` folder to create an S3 Object for each file.

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

    Here, we're again using the [@pulumi/aws] package to create an [aws.s3.Bucket]. For each file in `www`, we create an [aws.s3.BucketObject], using the helper [pulumi.asset.FileAsset] to reference a local file.

    In order to serve the files to a browser, the content type for each S3 Object must be set. For this, we use the [NPM `mime` package](https://www.npmjs.com/package/mime). Just like a regular Node program, Pulumi programs can use any Node.js package.

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

1.  Configure the AWS region to deploy to, such as `us-west-2`. After this step, a new file `Pulumi.website-testing.yaml` is created, next to your [Pulumi.yaml project file](../reference/project.html). See [Defining and setting stack settings](../reference/config.html#config-stack) for more information about this file.

    ```bash
    $ pulumi config set aws:region us-west-2
    ```

1.  Run `pulumi update` preview and deploy AWS resources. As expected, a stack component is creataed, along with a new Bucket and two S3 Objects --- one for each file in the `www` folder.

    ```bash
    $ pulumi update
    Previewing stack 'website-testing'
    Previewing changes:

    #: Resource Type        Name                       Plan      Extra Info
    1: pulumi:pulumi:Stack  s3website-website-testing  + create
    2: aws:s3:Bucket        s3-website-bucket          + create
    3: aws:s3:BucketObject  favicon.png                + create
    4: aws:s3:BucketObject  index.html                 + create

    info: 4 changes previewed:
        + 4 resources to create

    Do you want to proceed? yes
    Updating stack 'website-testing'
    Performing changes:

    #: Resource Type        Name                       Status     Extra Info
    1: pulumi:pulumi:Stack  s3website-website-testing  + created
    2: aws:s3:Bucket        s3-website-bucket          + created
    3: aws:s3:BucketObject  favicon.png                + created
    4: aws:s3:BucketObject  index.html                 + created

    info: 4 changes performed:
        + 4 resources created
    Update duration: 5.792898385s

    Permalink: https://pulumi.com/lindydonna/-/-/website-testing/updates/1
    ```

1.  To see the name of the bucket that was created, run `pulumi stack output`. Note that an extra 7-digit identifier is appended to the name. All Pulumi resources add this identifier automatically, so that you don't have to manually create unique names.

    ```bash
    $ pulumi stack output
    Current stack outputs (1):
        OUTPUT                                           VALUE
        bucketName                                       s3-website-bucket2-c198168
    ```

1.  To see that the S3 objects exist, you can either use the AWS Console or the AWS CLI:

    ```bash
    $ aws s3 ls $(pulumi stack output bucketName)
    2018-04-17 15:40:47      13731 favicon.png
    2018-04-17 15:40:48        249 index.html
    ```

### Add S3 website support

In this section, we configure the S3 bucket to serve the files to a browser. To do this, we use the [aws.s3.Bucket.websites] property and attach an [aws.s3.BucketPolicy] object. 

1.  Change the declaration of `siteBucket` to specify an `indexDocument`:

    ```javascript
    ...

    // REMOVE previous declaration and add this
    let siteBucket = new aws.s3.Bucket("s3-website-bucket", {  
      websites: [{                       
        indexDocument: "index.html",  
      }],
    });

    ...
    ```

1.  Add the following code, which defines the S3 public read policy, applies it to the bucket, and defines a new stack output:

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
      bucket: siteBucket.bucket, // depends on siteBucket -- see explanation below
      policy: siteBucket.bucket.apply(publicReadPolicyForBucket) 
              // transform the siteBucket.bucket output property -- see explanation below
    });

    exports.websiteUrl = siteBucket.websiteEndpoint; // output the endpoint as a stack output
    ```

    To make [all objects in the bucket publicly readable](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html), we create a [BucketPolicy][aws.s3.BucketPolicy] object. The definition of `bucketPolicy` illustrates how Pulumi tracks dependencies between resources. The property [aws.s3.Bucket.bucket] is an output property of type [pulumi.Output] --- a marker class that encodes the relationship between resources in a Pulumi program. An object of type `Output` can be passed directly to the inputs of a resource constructor, such as the `bucket` property. 
    
    For the `policy` property, the IAM policy must include the target bucket name. Since the value of output properties are not known until the underlying resource is created (such as the generated name for the S3 bucket), we use the `apply` method of [pulumi.Output] rather than directly calling `publicReadPolicyForBucket`. 

    Whenever you need to create a dependency between resources, simply use the output property of one resource as the input to another one. Pulumi uses this information to create physical resources in the correct order. In fact, we have been using this feature all along: when constructing a `BucketObject`, the line `bucket: siteBucket` ensures that the physical AWS bucket exists before S3 objects are created. Similarly, in [Part 1 of the quickstart](./part1.html#webserver), output properties established the dependency between the security group and EC2 instance.  

1.  Run `pulumi update`, which shows the change to **update** the `Bucket` resource and **create** a new `BucketPolicy` resource:

    ```bash
    $ pulumi update
    Previewing stack 'website-testing'
    Previewing changes:

    #: Resource Type        Name                       Plan         Extra Info
    1: pulumi:pulumi:Stack  s3website-website-testing  * no change
    2: aws:s3:Bucket        s3-website-bucket          ~ update     changes: + websites
    3: aws:s3:BucketPolicy  bucketPolicy               + create

    info: 2 changes previewed:
        + 1 resource to create
        ~ 1 resource to update
          3 resources unchanged

    Do you want to proceed? yes
    Updating stack 'website-testing'
    Performing changes:

    #: Resource Type        Name                       Status     Extra Info
    1: pulumi:pulumi:Stack  s3website-website-testing  done
    2: aws:s3:Bucket        s3-website-bucket          ~ updated  changes: + websites
    3: aws:s3:BucketPolicy  bucketPolicy               + created

    info: 2 changes performed:
        + 1 resource created
        ~ 1 resource updated
          3 resources unchanged
    Update duration: 4.882755297s

    Permalink: https://pulumi.com/lindydonna/-/-/website-testing/updates/2    
    ```

1.  Open the site URL in a browser to see both the rendered HTML and the favicon:

    ```bash
    $ pulumi stack output websiteUrl
    s3-website-bucket-8533d8b.s3-website-us-west-2.amazonaws.com
    ```

    ![Hello S3 example](images/part2-website.png){:width="700px"}

## Create a Pulumi component 

In this example, we defined a function `publicReadPolicyForBucket`. Since it is just a plain JavaScript function, it can be put into a shared library. In Pulumi, you can even create libraries and NPM packages for infrastructure definitions.

It's easy to turn the S3 website example into a reusable [Component] that you share with your team or the community. A component is a logical container for physical cloud resources and controls how resources are grouped in the CLI and pulumi.com Console. To create a component in JavaScript, simply subclass [pulumi.ComponentResource]. 

In this section, we'll create a simplified version of the example above, that just creates an S3 bucket. For a working end-to-end version that serves a stack website, see the [full source in the Pulumi examples repo][s3-folder-component].

1.  In your project directory, create a new file `s3folder.js` with the following contents:

    ```javascript
    const aws = require("@pulumi/aws");
    const pulumi = require("@pulumi/pulumi");

    // Define a component for serving a static website on S3
    class S3Folder extends pulumi.ComponentResource {

        constructor(bucketName, path, opts) {
            // Register this component with name examples:S3Folder
            super("examples:S3Folder", bucketName, {}, opts); 
            console.log(`Path where files would be uploaded: ${path}`);

            // Create a bucket and expose a website index document
            let siteBucket = new aws.s3.Bucket(bucketName, {}, 
                { parent: this } ); // specify resource parent

            // Create a property for the bucket name that was created
            this.bucketName = siteBucket.bucket,

            // For dependency tracking, register output properties for this component
            this.registerOutputs({
                bucketName: this.bucketName,
            });
        }
    }

    module.exports.S3Folder = S3Folder;
    ```

    The call to `super` specifies the string name for the component, which is typically in the form `namespace:className`. This name is shown in `pulumi update` command as well as at pulumi.com. The second parameter to the `super` call is the name of the resource. In this case, we use the `bucketName` constructor parameter.

    Since the `path` parameter is not used, we just log its value via `console.log`. During `pulumi update`, this log message is shown.

    When creating a resource within a component, add a parent property as the last argument to the constructor, as in the definition of `siteBucket`. When resources are created at the top level, they do not need an explicit parent; the Pulumi stack resource is the parent of all top-level resources and components.

    A component should create output properties to expose any useful properties of the resources it created. In this example, we define a `bucketName` property. Then, this property is registered a component output so that consumers of `S3Folder` can correctly chain dependencies.

1.  Use a component as you would any Node module. Replace `index.js` with the following:

    ```javascript
    const s3folder = require("./s3folder.js");

    // Create an instance of the S3Folder component
    let folder = new s3folder.S3Folder("s3-website-bucket", "./www");

    // Export output property of `folder` as a stack output
    exports.bucketName = folder.bucketName;
    ```

    Since we still want a stack output for `bucketName`, we create a stack output of the component output property `folder.bucketName`.

1.  Run `pulumi update`. Because the program no longer creates S3 objects and does not apply a bucket policy, those resources will be deleted. The bucket Bucket will also be re-created: the parent of a resource is part of its identity and the parent of `s3-website-bucket` has changed from the stack to an instance of `S3Folder`. Note that the output of `console.log` is printed in the "Diagnostics" section below.

    ```bash
    $ pulumi update
    Previewing stack 'website-testing'
    Previewing changes:
    [... details omitted ...]

    Do you want to proceed? yes
    Updating stack 'website-testing'
    Performing changes:

    #: Resource Type        Name                       Status     Extra Info
    1: pulumi:pulumi:Stack  s3website-website-testing  done       1 info message
    2: examples:S3Folder    s3-website-bucket          + created
    3: aws:s3:Bucket        s3-website-bucket          + created
    4: aws:s3:BucketObject  index.html                 - deleted
    5: aws:s3:BucketObject  favicon.png                - deleted
    6: aws:s3:BucketPolicy  bucketPolicy               - deleted
    7: aws:s3:Bucket        s3-website-bucket          - deleted

    Diagnostics:
      pulumi:pulumi:Stack: s3website-website-testing
        info: Path where files would be uploaded: ./www

    info: 6 changes performed:
        + 2 resources created
        - 4 resources deleted
          1 resource unchanged
    Update duration: 7.047243828s

    Permalink: https://pulumi.com/lindydonna/-/-/website-testing/updates/3
    ```

1.  Verify the bucket exists by using the AWS Console or CLI:

    ```bash
    $ aws s3 ls | grep $(pulumi stack output bucketName)
    2018-04-19 18:40:04 s3-website-bucket-82616a0
    ```  

## Clean up

Let's remove the cloud resources that have been provisioned.

1.  Run `pulumi destroy` to tear down all resources:

    ```
    $ pulumi destroy
    This will permanently destroy all resources in the 'website-testing' stack!
    Please confirm that this is what you'd like to do by typing ("website-testing"): website-testing
    Previewing stack 'website-testing'
    Previewing changes:
    [... details omitted ...]

    Do you want to proceed? yes
    Destroying stack 'website-testing'
    Performing changes:

    #: Resource Type        Name                       Status     Extra Info
    1: aws:s3:Bucket        s3-website-bucket          - deleted
    2: examples:S3Folder    s3-website-bucket          - deleted
    3: pulumi:pulumi:Stack  s3website-website-testing  - deleted

    info: 3 changes performed:
        - 3 resources deleted
    Update duration: 1.021430968s

    Permalink: https://pulumi.com/lindydonna/-/-/website-testing/updates/4
    ```

1.  To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Console.

## Summary

In this part, we saw the benefits of using a programming language to define infrastructure:
-  You can use standard programming language constructs, such as loops, conditionals, and functions.
-  You can use any Node packages in your program. For instance, the initial example did not recurse into subdirectories of `www`. Adding this new feature is just a matter using a new NPM package.
-  Pulumi programs are repeatable and production-ready by default. To stand up a "staging" or "production" instance of the website --- with the exact same files --- simply create a new stack and deploy.
-  Infrastructure code and content can be seamlessly versioned together, using the same tools and workflow.
-  You can create reusable packages for your infrastructure by creating a [component][Component]. These components can be shared with your team or published on NPM.

The full source of the examples are available in the [Pulumi examples repo](https://github.com/pulumi/examples) on GitHub:
- [S3 website][s3-folder]
- [S3 website as component][s3-folder-component]

## Next steps

Continue with [part 3 of the quickstart](./part3.html) to learn how to create programs that contain both infrastructure and application code, using serverless functions and containers.

