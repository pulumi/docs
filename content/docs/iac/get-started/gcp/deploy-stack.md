---
title_tag: Deploy the Stack | Google Cloud
title: Deploy the stack
h1: "Deploy the stack"
meta_desc: Learn how to deploy your stack to a Google Cloud project in this guide.
weight: 6
menu:
    iac:
        name: Deploy the stack
        identifier: gcp-get-started.deploy-stack
        parent: gcp-get-started
        weight: 6
aliases:
    - /docs/quickstart/gcp/deploy-stack/
    - /docs/clouds/gcp/get-started/deploy-stack/
---

Now deploy the stack with `pulumi up`:

```bash
$ pulumi up
```

This command first shows you a preview of the changes to be made:

```
Previewing update (dev):

     Type                   Name            Plan
 +   pulumi:pulumi:Stack    quickstart-dev  create
 +   └─ gcp:storage:Bucket  my-bucket       create

Outputs:
    bucketName: [unknown]

Resources:
    + 2 to create

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` proceeds with an update, which creates the resources in Google Cloud:

```
Updating (dev):

     Type                   Name            Status
 +   pulumi:pulumi:Stack    quickstart-dev  created (3s)
 +   └─ gcp:storage:Bucket  my-bucket       created (1s)

Outputs:
    bucketName: "gs://my-bucket-daa12be"

Resources:
    + 2 created

Duration: 4s
```

The update completes when all resources are created. For a storage bucket, this takes only a few seconds.

{{< auto-naming-note resource="bucket" suffix="daa12be" >}}

Notice the bucket's name was emitted as a [stack output](/docs/iac/concepts/stacks/#outputs). You can retrieve the output's value with `pulumi stack output`:

{{% choosable language "typescript,go,csharp,java,yaml" %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pulumi stack output bucket_name
```

{{% /choosable %}}

Next, you'll turn the bucket into a static website.

{{< get-started-stepper >}}
