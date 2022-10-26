---
title: Deploy the Stack | GCP
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how to deploy changes to a Google Cloud project.
weight: 5
menu:
  getstarted:
    parent: gcp
    identifier: gcp-deploy-stack

aliases: ["/docs/quickstart/gcp/deploy-stack/"]
---

Let's go ahead and deploy your stack:

```bash
$ pulumi up
```

This command evaluates your program and determines the resource updates to make. First, a preview is shown that outlines the changes that will be made when you run the update:

```
Previewing update (dev):
     Type                   Name            Plan
 +   pulumi:pulumi:Stack    quickstart-dev  create
 +   └─ gcp:storage:Bucket  my-bucket       create

Resources:
    + 2 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Once the preview has finished, you are given three options to choose from. Choosing `details` will show you a rich diff of the changes to be made. Choosing `yes` will create your new storage bucket in Google Cloud. Choosing `no` will return you to the user prompt without performing the update operation.

```
Do you want to perform this update? yes
Updating (dev):

     Type                   Name            Status
     pulumi:pulumi:Stack    quickstart-dev  created
 +   └─ gcp:storage:Bucket  my-bucket       created

Outputs:
  + bucketName: "gs://my-bucket-62f8bc7"

Resources:
    + 2 created

Duration: 3s
```

Remember the output you defined in the previous step? That [stack output](/docs/intro/concepts/stack#outputs) can be seen in the `Outputs:` section of your update. You can access your outputs from the CLI by running the `pulumi stack output [property-name]` command. For example you can print the name of your bucket with the following command:

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

{{< console-note >}}

Now that your bucket has been provisioned, let's modify the bucket to host a static website.

{{< get-started-stepper >}}
