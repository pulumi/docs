---
title: Deploy the Changes | AWS
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to an AWS project.
weight: 7
menu:
  getstarted:
    parent: aws
    identifier: aws-deploy-changes

aliases: ["/docs/quickstart/aws/deploy-changes/"]
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                    Name                Plan       Info
     pulumi:pulumi:Stack     quickstart-dev
 ~   ├─ aws:s3:Bucket        my-bucket           update     [diff: +website]
 +   └─ aws:s3:BucketObject  index.html          create

Outputs:
  + websiteEndpoint: output<string>

Resources:
    + 1 to create
    ~ 1 to update
    2 changes. 1 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will create the home page and update the bucket with the new website configuration.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):
     Type                    Name                Status      Info
     pulumi:pulumi:Stack     get-started-ts-dev
 ~   ├─ aws:s3:Bucket        my-bucket           updated     [diff: +website]
 +   └─ aws:s3:BucketObject  index.html          created

Outputs:
    bucketName     : "my-bucket-de014a8"
  + websiteEndpoint: "http://my-bucket-de014a8.s3-website-us-west-2.amazonaws.com"

Resources:
    + 1 created
    ~ 1 updated
    2 changes. 1 unchanged

Duration: 8s
```

You can browse to the page either by copying the `websiteEndpoint` value and pasting it into your browser or by using `pulumi stack export`:

```
open "http://$(pulumi stack output websiteEndpoint)"
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
