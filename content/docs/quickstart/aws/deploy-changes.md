---
title: Deploy the Changes
weight: 9
menu:
  quickstart:
    parent: aws
    identifier: aws-deploy-changes
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
 +   ├─ aws:kms:Key       my-key          create
 ~   └─ aws:s3:Bucket     my-bucket       update     [diff: +serverSideEncryptionConfiguration]

Resources:
    + 1 to create
    ~ 1 to update
    2 changes. 1 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will create the KMS key and update the bucket with the new encryption configuration.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status      Info
     pulumi:pulumi:Stack  quickstart-dev
 +   ├─ aws:kms:Key       my-key          created
 ~   └─ aws:s3:Bucket     my-bucket       updated     [diff: +serverSideEncryptionConfiguration]

Outputs:
    bucket_name: "my-bucket-de014a8"

Resources:
    + 1 created
    ~ 1 updated
    2 changes. 1 unchanged

Duration: 10s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
