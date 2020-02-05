---
title: Deploy the Stack | Alibaba Cloud
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how deploy changes to an Alibaba Cloud project.
weight: 7
menu:
  getstarted:
    parent: alicloud
    identifier: alicloud-deploy-stack

---

Let's go ahead and deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

```
Previewing update (dev):

     Type                 Name            Plan
 +   pulumi:pulumi:Stack  quickstart-dev  create
 +   └─ alicloud:oss:Bucket     my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in Alibaba Cloud.

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status
 +   pulumi:pulumi:Stack  quickstart-dev  created
 +   └─ alicloud:oss:Bucket     my-bucket       created

Outputs:
    bucketName: "my-bucket-68e33ec"

Resources:
    + 2 created

Duration: 14s
```

The name of the bucket that we exported is shown as a [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
