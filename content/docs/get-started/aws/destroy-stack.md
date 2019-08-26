---
title: Destroy the Stack
weight: 10
menu:
  quickstart:
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

<<<<<<< HEAD:content/docs/get-started/aws/destroy-stack.md
To delete the stack itself, run [`pulumi stack rm`]({{< relref "/docs/reference/cli/pulum_stack_rm" >}}).
Note that this removes the stack entirely from `pulumi.com`, along with all of its update history.
=======
To delete the stack itself, run [`pulumi stack rm`]({{< relref
"/docs/reference/cli/pulumi_stack_rm" >}}). Note that this removes the stack
entirely from `pulumi.com`, along with all of its update history.
>>>>>>> 84b42daf... Address feedback:content/docs/quickstart/aws/destroy-stack.md

Next, we'll look at some next steps.

{{< get-started-stepper >}}
