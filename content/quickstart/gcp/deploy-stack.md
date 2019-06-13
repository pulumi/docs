---
title: Deploy the Stack
weight: 6
menu:
  quickstart:
    parent: gcp
    identifier: gcp-deploy-stack
---

Let's go ahead and deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

```
Previewing update (dev):

     Type                   Name            Plan
 +   pulumi:pulumi:Stack    quickstart-dev  create
 +   └─ gcp:storage:Bucket  my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in Google Cloud. This may take a minute or two.

```
Do you want to perform this update? yes
Updating (dev):

     Type                   Name            Status
     pulumi:pulumi:Stack    quickstart-dev
 +   └─ gcp:storage:Bucket  my-bucket       created

Outputs:
  + bucketName: "gs://my-bucket-62f8bc7"

Resources:
    + 1 created
    1 unchanged

Duration: 3s
```

The bucket URL, that we exported, is shown as a [stack output]({{< relref "/reference/stack.md#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
