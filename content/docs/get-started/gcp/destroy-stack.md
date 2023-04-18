---
title: Destroy the Stack | GCP
h1: Destroy the Stack
linktitle: Destroy the Stack
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Google Cloud (GCP) project.
weight: 8
menu:
  getstarted:
    parent: gcp
    identifier: gcp-destroy-stack

aliases: ["/docs/quickstart/gcp/destroy-stack/"]
---

Now that you've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of your stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits until all resources are shut down and deleted before it considers the destroy operation complete.

```
Previewing destroy (dev):

 -   pulumi:pulumi:Stack              quickstart-dev         delete
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-IAMBinding   delete
 -   ├─ gcp:storage:BucketObject      index.html             delete
 -   └─ gcp:storage:Bucket            my-bucket              delete

Outputs:
  - bucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"
  - bucketName    : "gs://my-bucket-0167228"

Resources:
    - 4 to delete

Do you want to perform this destroy? yes
Destroying (dev):

 -   pulumi:pulumi:Stack              quickstart-dev         deleted
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-IAMBinding   deleted
 -   ├─ gcp:storage:BucketObject      index.html             deleted
 -   └─ gcp:storage:Bucket            my-bucket              deleted

Outputs:
  - bucketEndpoint: "http://storage.googleapis.com/my-bucket-0167228/index.html-50b2ce9"
  - bucketName    : "gs://my-bucket-0167228"

Resources:
    - 4 deleted

Duration: 7s
```

> To delete the stack itself, run [`pulumi stack rm`](/docs/reference/cli/pulumi_stack_rm).
Note that this removes the stack entirely from the Pulumi Cloud, along with all of its update history.

Congratulations! You've successfully provisioned some cloud resources using Pulumi. By completing this guide you have successfully:

- Created a Pulumi new project.
- Provisioned a new storage bucket.
- Added an `index.html` file to your bucket.
- Served the `index.html` as a static website.
- Destroyed the resources you've provisioned.

On the next page, we have a collection of examples and tutorials that you can deploy as they are or use them as a foundation for your own applications and infrastructure projects.

{{< get-started-stepper >}}
