---
title_tag: Destroy the Stack | AWS
title: Destroy stack
h1: "Pulumi & AWS: Destroy stack"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an AWS project.
weight: 8
aliases:
- /docs/quickstart/aws/destroy-stack/
- /docs/get-started/aws/destroy-stack/
- /docs/clouds/aws/get-started/destroy-stack/
---

Now that you've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of your stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits until all resources are shut down and deleted before it considers the destroy operation to be complete.

```
Previewing destroy (dev):

     Type                                    Name                 Status
 -   pulumi:pulumi:Stack                     quickstart-dev       delete
 -   ├─ aws:s3:BucketObject                  index.html           delete
 -   ├─ aws:s3:BucketOwnershipControls       ownership-controls   delete
 -   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  delete
 -   ├─ aws:s3:BucketWebsiteConfigurationV2  website              delete
 -   └─ aws:s3:BucketV2                      my-bucket            delete

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                                    Name                 Status
 -   pulumi:pulumi:Stack                     quickstart-dev       deleted (0.31s)
 -   ├─ aws:s3:BucketObject                  index.html           deleted (1s)
 -   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  deleted (0.67s)
 -   ├─ aws:s3:BucketWebsiteConfigurationV2  website              deleted (0.88s)
 -   ├─ aws:s3:BucketOwnershipControls       ownership-controls   deleted (1s)
 -   └─ aws:s3:BucketV2                      my-bucket            deleted (0.58s)

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 deleted

Duration: 4s
```

> To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). Note that this removes the stack entirely from Pulumi Cloud, along with all of its update history.

Congratulations! You've successfully provisioned some cloud resources using Pulumi. By completing this guide you have successfully:

- Created a Pulumi new project.
- Provisioned a new S3 bucket.
- Added an `index.html` file to your bucket.
- Served the `index.html` as a static website.
- Destroyed the resources you've provisioned.

On the next page, we have a collection of examples and tutorials that you can deploy as they are or use them as a foundation for your own applications and infrastructure projects.

{{< get-started-stepper >}}
