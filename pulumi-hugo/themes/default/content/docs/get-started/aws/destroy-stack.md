---
title: Destroy the Stack | AWS
h1: Destroy the Stack
linktitle: Destroy the Stack
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an AWS project.
weight: 10
menu:
  getstarted:
    parent: aws
    identifier: aws-destroy-stack

aliases: ["/docs/quickstart/aws/destroy-stack/"]
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits until all resources are shut down and deleted before it considers the destroy operation to be complete.

```
Previewing destroy (dev):

     Type                 Name            Plan
 -   pulumi:pulumi:Stack  quickstart-dev  delete
 -   ├─ aws:s3:Bucket     my-bucket       delete
 -   └─ aws:kms:Key       my-key          delete

Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                 Name            Status
 -   pulumi:pulumi:Stack  quickstart-dev  deleted
 -   ├─ aws:s3:Bucket     my-bucket       deleted
 -   └─ aws:kms:Key       my-key          deleted

Resources:
    - 3 deleted

Duration: 26s
```

To delete the stack itself, run [`pulumi stack rm`]({{< relref
"/docs/reference/cli/pulumi_stack_rm" >}}). Note that this removes the stack
entirely from the Pulumi Service, along with all of its update history.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
