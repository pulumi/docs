---
title_tag: Destroy the Stack | AWS
title: Destroy the stack
h1: "Destroy the stack"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an AWS project.
weight: 9
menu:
    iac:
        name: Destroy the stack
        parent: aws-get-started
        weight: 9

aliases:
    - /docs/iac/get-started/aws/b/destroy-stack/
    - /docs/quickstart/aws/destroy-stack/
    - /docs/clouds/aws/get-started/destroy-stack/
---

Now that you've seen how to provision and manage resources with Pulumi, you can clean up the resources you created. Run `pulumi destroy` to delete every cloud resource in the stack:

```bash
$ pulumi destroy
```

Once again, you'll see a preview before anything happens:

```
Previewing destroy (dev):

     Type                                    Name                 Plan
 -   pulumi:pulumi:Stack                     quickstart-dev       delete
 -   ├─ aws:s3:BucketObject                  index.html           delete
 -   ├─ aws:s3:BucketOwnershipControls       ownership-controls   delete
 -   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  delete
 -   ├─ aws:s3:BucketWebsiteConfiguration    website              delete
 -   └─ aws:s3:Bucket                        my-bucket            delete

Outputs:
  - bucketName: "my-bucket-dfd6bd0"
  - url        : "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"

Resources:
    - 5 to delete

Do you want to perform this destroy?
> yes
  no
  details
```

Choose `yes` to destroy the stack. When the operation completes, your cloud resources no longer exist, but the stack and its configuration settings still do. You can delete the stack, including all of its state and update history, with [`pulumi stack rm`](/docs/iac/cli/commands/pulumi_stack_rm/):

```bash
$ pulumi stack rm
```

Confirm the removal when prompted to complete the tutorial.

{{< get-started-stepper >}}
