---
title_tag: Deploy the Stack | Google Cloud
title: Deploy to Google Cloud
h1: "Get started with Pulumi and Google Cloud"
meta_desc: Learn how to deploy your stack to a Google Cloud project in this guide.
weight: 5
menu:
    iac:
        name: Deploy
        identifier: gcp-get-started.deploy-stack
        parent: gcp-get-started
        weight: 5

aliases:
    - /docs/quickstart/gcp/deploy-stack/
    - /docs/clouds/gcp/get-started/deploy-stack/
---

## Deploy to Google Cloud

Now run `pulumi up` to start deploying your new storage bucket:

```bash
$ pulumi up
```

This command first shows you a **preview** of the changes that will be made:

```
Previewing update (dev)

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

No changes have been made yet. You may decline to proceed by selecting `no` or choose `details` to
see more information about the proposed update like your bucket's properties.

### Performing the update

To proceed and deploy your new storage bucket, select `yes`. This begins an **update**:

```
Do you want to perform this update? yes
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

Updates can take some time since they wait for the cloud resources to finish being created. Storage buckets
are quick, however, so the update will finish in just a few seconds.

{{< auto-naming-note resource="bucket" suffix="daa12be" >}}

### Using stack outputs

The bucket name is available as a stack output. To view it:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

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

### View your update on Pulumi Cloud

If you are logged into [Pulumi Cloud](/docs/pulumi-cloud), you'll see "View Live" hyperlinks in the CLI output during your update. These go to [a page](https://app.pulumi.com) with detailed information about your stack including resources, configuration, a full history of updates, and more. Navigate to it to review the details of your update:

<a href="/images/getting-started/console-update.png" target="_blank">
    <img src="/images/getting-started/console-update.png" alt="A stack update with console output, as shown in the Pulumi Service" />
</a>

Now that the storage bucket has been provisioned, you'll update it to host a static website.

{{< get-started-stepper >}}
