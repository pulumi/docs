---
title: Destroy the Stack | GCP
h1: Destroy the Stack
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
     Type                   Name       Plan
 -   pulumi:pulumi:Stack    quickstart-dev  delete
 -   └─ gcp:storage:Bucket  my-bucket  delete

Outputs:
  - BucketName: "gs://my-bucket-b93323e"

Resources:
    - 2 to delete

Do you want to perform this destroy? yes
Destroying (dev):
     Type                   Name       Status
 -   pulumi:pulumi:Stack    quickstart-dev  deleted
 -   └─ gcp:storage:Bucket  my-bucket  deleted

Outputs:
  - BucketName: "gs://my-bucket-b93323e"

Resources:
    - 2 deleted

Duration: 2s
```

To delete the stack itself, run [`pulumi stack rm`]({{< prelref "/docs/reference/cli/pulumi_stack_rm" >}}).
Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
