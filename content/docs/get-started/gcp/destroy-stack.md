---
title: Destroy the Stack | GCP
linktitle: Destroy the Stack
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Google Cloud (GCP) project.
weight: 10
menu:
  getstarted:
    parent: gcp
    identifier: gcp-destroy-stack

aliases: ["/docs/quickstart/gcp/destroy-stack/"]
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources.

```
Previewing destroy (dev):

     Type                   Name            Plan
 -   pulumi:pulumi:Stack    gcp-bucket-dev  delete
 -   ├─ gcp:storage:Bucket  my-bucket       delete
 -   ├─ gcp:kms:CryptoKey   my-cryptokey    delete
 -   └─ gcp:kms:KeyRing     my-keyring      delete

Resources:
    - 4 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                   Name            Status
 -   pulumi:pulumi:Stack    gcp-bucket-dev  deleted
 -   ├─ gcp:storage:Bucket  my-bucket       deleted
 -   ├─ gcp:kms:CryptoKey   my-cryptokey    deleted
 -   └─ gcp:kms:KeyRing     my-keyring      deleted

Resources:
    - 4 deleted

Duration: 3s
```

To delete the stack itself, run [`pulumi stack rm`]({{< relref "/docs/reference/cli/pulumi_stack_rm" >}}).
Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
