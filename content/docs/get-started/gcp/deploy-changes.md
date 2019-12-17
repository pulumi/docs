---
title: Deploy the Changes | GCP
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
Previewing update (dev):

     Type                   Name            Plan       Info
     pulumi:pulumi:Stack    gcp-bucket-dev
 +   ├─ gcp:kms:KeyRing     my-keyring      create
 +   ├─ gcp:kms:CryptoKey   my-cryptokey    create
 ~   └─ gcp:storage:Bucket  my-bucket       update     [diff: +encryption]

Resources:
    + 2 to create
    ~ 1 to update
    3 changes. 1 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will create two new resources, and then update the previously created bucket with the new encryption settings we defined.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                   Name            Status      Info
     pulumi:pulumi:Stack    gcp-bucket-dev
 +   ├─ gcp:kms:KeyRing     my-keyring      created
 +   ├─ gcp:kms:CryptoKey   my-cryptokey    created
 ~   └─ gcp:storage:Bucket  my-bucket       updated     [diff: +encryption]

Outputs:
    bucketName: "gs://my-bucket-6cea6b4"

Resources:
    + 2 created
    ~ 1 updated
    3 changes. 1 unchanged

Duration: 4s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
