---
title_tag: Deploy the Stack | AWS
title: Deploy stack
h1: "Pulumi & AWS: Deploy stack"
meta_desc: Learn how to deploy your stack to an AWS project in this guide.
weight: 5
menu:
  clouds:
    parent: aws-get-started
    identifier: aws-get-started-deploy-stack

aliases:
- /docs/quickstart/aws/deploy-stack/
- /docs/get-started/aws/deploy-stack/
---

Let's go ahead and deploy your stack:

```bash
$ pulumi up
```

This command evaluates your program and determines the resource updates to make. First, a preview is shown that outlines the changes that will be made when you run the update:

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

Once the preview has finished, you are given three options to choose from. Choosing `details` will show you a rich diff of the changes to be made. Choosing `yes` will create your new S3 bucket in AWS. Choosing `no` will return you to the user prompt without performing the update operation.

```
Do you want to perform this update? yes
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

Remember the output you defined in the previous step? That [stack output](/docs/concepts/stack#outputs) can be seen in the `Outputs:` section of your update. You can access your outputs from the CLI by running the `pulumi stack output [property-name]` command. For example you can print the name of your bucket with the following command:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi stack output bucket_name
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ pulumi stack output bucketName
```

{{% /choosable %}}

Running that command will print out the name of your bucket.

{{< auto-naming-note resource="bucket" suffix="58ce361" >}}

{{< console-note >}}

Now that the bucket has been provisioned, let's modify the program to host a static website.

{{< get-started-stepper >}}
