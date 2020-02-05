---
title: Deploy the Changes | Alibaba Cloud
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to an Alibaba Cloud project.
weight: 9
menu:
  getstarted:
    parent: alicloud
    identifier: alicloud-deploy-changes

---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                 Name            Plan       Info
     pulumi:pulumi:Stack  quickstart-dev
 ~   ├─ alicloud:oss:Bucket       my-bucket          update

Resources:
    + 1 to update
    1 changes

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will update the OSS Bucket.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status      Info
     pulumi:pulumi:Stack  quickstart-dev
 ~   ├─ alicloud:oss:Bucket       my-bucket          updated

Outputs:
    bucket_name: "my-bucket-de014a8"

Resources:
    + 1 updated
    1 changes. 1 unchanged

Duration: 10s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
