---
title_tag: Destroy the Stack | Google Cloud
meta_desc: This page provides an overview of how to destroy a Pulumi stack of a Google Cloud (GCP) project.
title: Destroy stack
h1: "Pulumi & Google Cloud: Destroy stack"
weight: 8
menu:
  clouds:
    parent: google-cloud-get-started
    identifier: gcp-destroy-stack

aliases:
- /docs/quickstart/gcp/destroy-stack/
- /docs/get-started/gcp/destroy-stack/
---

Now that you've seen how to deploy and manage cloud resources with Pulumi, let's clean up by tearing down all of the resources that belong to this stack.

To do so, run the following:

```bash
$ pulumi destroy
```

Again you'll be presented with a preview of the changes to be made. Choose `yes`. The destroy operation may take few moments, as Pulumi waits for all resources are to be deleted before considering the operation complete:

```
Previewing destroy (dev)

     Type                             Name               Plan
 -   pulumi:pulumi:Stack              quickstart-dev     delete
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  delete
 -   ├─ gcp:storage:BucketObject      index.html         delete
 -   └─ gcp:storage:Bucket            my-bucket          delete

Outputs:
  - bucketEndpoint: "http://storage.googleapis.com/my-bucket-daa12be/index.html-a52debd"
  - bucketName    : "gs://my-bucket-daa12be"

Resources:
    - 4 to delete

Do you want to perform this destroy? yes
Destroying (dev)

     Type                             Name               Status
 -   pulumi:pulumi:Stack              quickstart-dev     deleted
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  deleted (6s)
 -   ├─ gcp:storage:BucketObject      index.html         deleted (0.78s)
 -   └─ gcp:storage:Bucket            my-bucket          deleted (1s)

Outputs:
  - bucketEndpoint: "http://storage.googleapis.com/my-bucket-daa12be/index.html-a52debd"
  - bucketName    : "gs://my-bucket-daa12be"

Resources:
    - 4 deleted

Duration: 9s
```

Optionally, to delete the stack itself, you can also run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). Doing so removes the stack entirely from the Pulumi Cloud, along with all of its update history.

Congratulations! You've successfully provisioned some cloud resources using Pulumi. By completing this guide you have successfully:

- Created a Pulumi new project.
- Provisioned a new storage bucket.
- Added an `index.html` file to your bucket.
- Served the file as a static website.
- Destroyed the resources you've provisioned.

On the next page, we have a collection of examples and tutorials that you can deploy as they are or use them as a foundation for your own applications and infrastructure projects.

{{< get-started-stepper >}}
