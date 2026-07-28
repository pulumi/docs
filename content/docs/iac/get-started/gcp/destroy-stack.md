---
title_tag: Destroy the Stack | Google Cloud
title: Destroy the stack
h1: "Destroy the stack"
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Google Cloud project.
weight: 9
menu:
    iac:
        name: Destroy the stack
        identifier: gcp-get-started.destroy-stack
        parent: gcp-get-started
        weight: 9
aliases:
    - /docs/quickstart/gcp/destroy-stack/
    - /docs/clouds/gcp/get-started/destroy-stack/
---

Now that you've seen how to provision and manage resources with Pulumi, you can clean up the resources you created. Run `pulumi destroy` to delete every cloud resource in the stack:

```bash
$ pulumi destroy
```

Once again, you'll see a preview before anything happens:

```
Previewing destroy (dev):

     Type                             Name               Plan
 -   pulumi:pulumi:Stack              quickstart-dev     delete
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  delete
 -   ├─ gcp:storage:BucketObject      index.html         delete
 -   └─ gcp:storage:Bucket            my-bucket          delete

Outputs:
  - bucketName: "gs://my-bucket-daa12be"
  - url       : "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    - 4 to delete

Do you want to perform this destroy?
> yes
  no
  details
```

Choose `yes` to destroy the stack. When the operation completes, your cloud resources no longer exist, but the stack and its configuration settings still do. You can delete the stack, including all of its state and update history, with [`pulumi stack rm`](/docs/iac/cli/commands/pulumi_stack_rm/):

```bash
$ pulumi stack rm
```

Confirm the removal when prompted, and you're done.

{{< get-started-stepper >}}
