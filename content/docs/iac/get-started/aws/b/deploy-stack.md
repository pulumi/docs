---
title_tag: Deploy the Stack | AWS
title: Deploy to AWS
h1: "Get started with Pulumi and AWS"
meta_desc: Learn how to deploy your stack to an AWS project in this guide.
weight: 5
menu:
    iac:
        name: Deploy
        parent: aws-b-get-started
        weight: 5

aliases:
- /docs/iac/get-started/aws/b/deploy-stack/
---

## Deploy to AWS

Now run `pulumi up` to start deploying your new S3 bucket:

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi up
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi up
```

{{% /choosable %}}

This command first shows you a **preview** of the changes that will be made:

```
Previewing update (dev):

     Type                 Name            Plan
 +   pulumi:pulumi:Stack  quickstart-dev  create
 +   └─ aws:s3:BucketV2   my-bucket       create

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

To proceed and deploy your new S3 bucket, select `yes`. This begins an **update**:

```
Do you want to perform this update? yes
Updating (dev):

     Type                 Name            Status
 +   pulumi:pulumi:Stack  quickstart-dev  created (4s)
 +   └─ aws:s3:BucketV2   my-bucket       created (2s)

Outputs:
    bucketName: "my-bucket-58ce361"

Resources:
    + 2 created

Duration: 5s
```

Updates can take some time since they wait for the cloud resources to finish being created. S3 buckets are quick,
however, so the update will finish in just a few seconds.

{{< auto-naming-note resource="bucket" suffix="58ce361" >}}

### Using stack outputs

The bucket ID can be accessed with the `pulumi stack output` command. You can use this to easily list
the contents of your new bucket -- which of course will be empty:

{{% choosable os "linux,macos" %}}

{{% choosable language "javascript,typescript,go,csharp,java,yaml" %}}

```bash
$ aws s3 ls s3://$(pulumi stack output bucketName)
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ aws s3 ls s3://$(pulumi stack output bucket_name)
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable os "windows" %}}

{{% choosable language "javascript,typescript,go,csharp,java,yaml" %}}

```powershell
$ aws s3 ls ("s3://" + (pulumi stack output bucketName))
```

{{% /choosable %}}

{{% choosable language python %}}

```powershell
$ aws s3 ls ("s3://" + (pulumi stack output bucket_name))
```

{{% /choosable %}}

{{% /choosable %}}

### View your update on Pulumi Cloud

If you are logged into [Pulumi Cloud](/docs/pulumi-cloud), you'll see "View Live" hyperlinks in the CLI output during your
update. These go to [a page](https://app.pulumi.com) with detailed information about your stack including resources,
configuration, a full history of updates, and more. Click on it to check it out:

<a href="/images/getting-started/console-update.png" target="_blank">
    <img src="/images/getting-started/console-update.png" alt="A stack update with console output, as shown in the Pulumi Service" />
</a>

Now that the S3 bucket has been provisioned, you'll update it to host a static website.

{{< get-started-stepper >}}
