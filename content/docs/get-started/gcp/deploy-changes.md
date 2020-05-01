---
title: Deploy the Changes | GCP
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to a Google Cloud (GCP) project.
weight: 9
menu:
  getstarted:
    parent: gcp
    identifier: gcp-deploy-changes

aliases: ["/docs/quickstart/gcp/deploy-changes/"]
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

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

Pulumi will create two new resources, and then update the previously created bucket with the new encryption settings we defined.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):
     Type                   Name               Status      Info
     pulumi:pulumi:Stack    quickstart-dev
 ~   └─ gcp:storage:Bucket  my-bucket          updated     [diff: ~labels]

Outputs:
    bucketName: "gs://my-bucket-d8d30a1"

Resources:
    ~ 1 updated
    1 unchanged

Duration: 4s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
