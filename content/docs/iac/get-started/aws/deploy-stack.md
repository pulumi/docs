---
title_tag: Deploy the Stack | AWS
title: Deploy the stack
h1: "Deploy the stack"
meta_desc: Learn how to deploy your stack to an AWS project in this guide.
weight: 6
menu:
    iac:
        name: Deploy the stack
        parent: aws-get-started
        weight: 6

aliases:
    - /docs/iac/get-started/aws/b/deploy-stack/
    - /docs/quickstart/aws/deploy-stack/
    - /docs/clouds/aws/get-started/deploy-stack/
---

Now deploy the stack with `pulumi up`:

```bash
$ pulumi up
```

This command first shows you a preview of the changes to be made:

```
Previewing update (dev):

     Type                 Name            Plan
 +   pulumi:pulumi:Stack  quickstart-dev  create
 +   └─ aws:s3:Bucket     my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` proceeds with an update, which creates the resources in AWS:

```
Updating (dev):

     Type                 Name            Status
 +   pulumi:pulumi:Stack  quickstart-dev  created (4s)
 +   └─ aws:s3:Bucket     my-bucket       created (2s)

Outputs:
    bucketName: "my-bucket-58ce361"

Resources:
    + 2 created

Duration: 5s
```

The update completes when all resources are created. For an S3 bucket, this takes only a few seconds.

{{< auto-naming-note resource="bucket" suffix="58ce361" >}}

Notice the bucket's name was emitted as a [stack output](/docs/iac/concepts/stacks/#outputs). You can also retrieve an output's value directly with `pulumi stack output`:

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
