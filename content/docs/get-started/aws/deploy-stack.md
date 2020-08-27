---
title: Deploy the Stack | AWS
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how deploy changes to an AWS project.
weight: 5
menu:
  getstarted:
    parent: aws
    identifier: aws-deploy-stack

aliases: ["/docs/quickstart/aws/deploy-stack/"]
---

Let's go ahead and run our first update:

```bash
$ pulumi up
```

This command evaluates your program and determines the resource updates to make. First, a preview is shown that outlines the changes that will be made:

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

Once the preview has finished you are given three options to choose from:

- `yes` will run your update.
- `no` will not run the update.
- `details` will show you the diff for the full set of properties within the stack.

Select `yes` to create your bucket.

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

Remember the output we defined in the previous step? That [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}) can be seen in the `Outputs:` section of our update. For example, the name of the bucket created above is `my-bucket-68e33ec`. To confirm our bucket has been created, let's list the contents of our bucket.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ aws s3 ls $(pulumi stack output bucket_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ aws s3 ls $(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ aws s3 ls $(pulumi stack output BucketName)
```

{{% /choosable %}}

Running that command should result in no output as our bucket is currently empty. Let's change that by modifying our bucket to host a static website.

{{< get-started-stepper >}}
