---
title: Deploy the Stack | GCP
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how to deploy a Google Cloud (GCP) project as a Pulumi Stack.
weight: 7
menu:
  getstarted:
    parent: gcp
    identifier: gcp-deploy-stack

aliases: ["/docs/quickstart/gcp/deploy-stack/"]
---

Let's go ahead and deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

```
$ pulumi up
Previewing update (dev):
     Type                   Name               Plan       Info
     pulumi:pulumi:Stack    quickstart-dev
 ~   └─ gcp:storage:Bucket  my-bucket          update     [diff: ~labels]

Outputs:
  ~ bucketName: "gs://my-bucket-d8d30a1" => output<string>

Resources:
    ~ 1 to update
    1 unchanged

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Choosing `yes` will create resources in Google Cloud. This may take a minute or two.

```
Do you want to perform this update? yes
Updating (dev):

     Type                   Name            Status
     pulumi:pulumi:Stack    quickstart-dev  created
 +   └─ gcp:storage:Bucket  my-bucket       created

Outputs:
  + bucketName: "gs://my-bucket-62f8bc7"

Resources:
    + 2 created

Duration: 3s
```

The bucket URL that we exported is shown as a [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
