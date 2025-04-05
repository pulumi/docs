---
title_tag: Destroy the Stack | AWS
title: Destroy stack
h1: "Get started with Pulumi and AWS"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an AWS project.
weight: 8
menu:
    iac:
        name: Cleanup & destroy
        parent: aws-get-started
        weight: 8

aliases:
- /docs/quickstart/aws/destroy-stack/
- /docs/get-started/aws/destroy-stack/
- /docs/clouds/aws/get-started/destroy-stack/
---

## Cleanup & destroy the stack

Our final step is to clean up all of the resources we've allocated in this tutorial.

Run the `pulumi destroy` command to delete all cloud resources in this project/stack:

{{% choosable os "linux,macos" %}}

```bash
$ pulumi destroy
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> pulumi destroy
```

{{% /choosable %}}

Just like `pulumi up`, you'll be shown a preview to ensure that you want to proceed:

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

Do you want to perform this destroy?
> yes
  no
  details
```

As with an update, we can choose `no` or `details`; select `yes` to proceed:

```
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

At this stage, your stack still exists, but all cloud resources have been deleted from it.

## Remove the stack

The final step is to remove the stack itself. Destroy keeps the stack around so that you still have the full
history of what happened to the stack. Running [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm) will
delete it entirely, including all history and state snapshots. Be careful, this step cannot be undone!

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi stack rm
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi stack rm
```

{{% /choosable %}}

You'll be prompted to confirm the removal. Confirm it to successfully complete this tutorial.

{{< get-started-stepper >}}
