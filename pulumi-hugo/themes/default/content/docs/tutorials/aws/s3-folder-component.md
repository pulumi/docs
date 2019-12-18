---
title: S3 Folder Pulumi Component
meta_desc: This tutorial will teach you how to create a simple, reusable AWS S3 Folder component.
aliases: ["/docs/reference/component-tutorial/"]
---

It's easy to turn the [S3 website example] into a reusable [Component] that you share with your team or the community. A component is a logical container for physical cloud resources and controls how resources are grouped in the CLI and pulumi.com Console. To create a component in JavaScript, simply subclass [pulumi.ComponentResource].

In this tutorial, we'll create a simplified version of the example above, that just creates an S3 bucket. For a working end-to-end version that serves a stack website, see the [full source in the Pulumi examples repo][s3-folder-component].

## Create an S3 folder component

1. In your project directory, create a new file `s3folder.js` with the following contents:

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

    The call to `super` specifies the string name for the component, which is typically in the form `namespace:className`. This name is shown in `pulumi up` command as well as at pulumi.com. The second parameter to the `super` call is the name of the resource. In this case, we use the `bucketName` constructor parameter.

    Since the `path` parameter is not used, we just log its value via `console.log`. During `pulumi up`, this log message is shown.

    When creating a resource within a component, add a parent property as the last argument to the constructor, as in the definition of `siteBucket`. When resources are created at the top level, they do not need an explicit parent; the Pulumi stack resource is the parent of all top-level resources and components.

    A component should create output properties to expose any useful properties of the resources it created. In this example, we define a `bucketName` property. Then, this property is registered a component output so that consumers of `S3Folder` can correctly chain dependencies.

1. Use a component as you would any Node module. Replace `index.js` with the following:

    ```javascript
    const s3folder = require("./s3folder.js");

    // Create an instance of the S3Folder component
    let folder = new s3folder.S3Folder("s3-website-bucket", "./www");

    // Export output property of `folder` as a stack output
    exports.bucketName = folder.bucketName;
    ```

    Since we want a stack output for `bucketName`, we create a stack output of the component output property `folder.bucketName`.

1. Run `pulumi up`. The output of `console.log` is printed in the "Diagnostics" section. Note the parent-child relationship between the resources that have been created.

1. Verify the bucket exists by using the AWS Console or CLI:

    ```bash
    $ aws s3 ls | grep $(pulumi stack output bucketName)
    2018-04-19 18:40:04 s3-website-bucket-82616a0
    ```

<!-- markdownlint-disable url -->
[pulumi.ComponentResource]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#ComponentResource" >}}
[Component]: {{< relref "/docs/intro/concepts/programming-model.md#components" >}}
[s3-folder]: https://github.com/pulumi/examples/tree/master/aws-js-s3-folder
[s3-folder-component]: https://github.com/pulumi/examples/tree/master/aws-js-s3-folder-component
[S3 website example]: {{< relref "/docs/tutorials/aws/s3-website" >}}
<!-- markdownlint-enable url -->
