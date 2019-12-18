---
title: Deploy the Stack | AWS
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how deploy changes to an AWS project.
weight: 7
menu:
  getstarted:
    parent: aws
    identifier: aws-deploy-stack

aliases: ["/docs/quickstart/aws/deploy-stack/"]
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
 +   └─ aws:s3:Bucket     my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in AWS.

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status
 +   pulumi:pulumi:Stack  quickstart-dev  created
 +   └─ aws:s3:Bucket     my-bucket       created

Outputs:
    bucketName: "my-bucket-68e33ec"

Resources:
    + 2 created

Duration: 14s
```

The name of the bucket that we exported is shown as a [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
