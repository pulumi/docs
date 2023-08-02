---
title_tag: Deploy the Stack | AWS
title: Deploy stack
h1: "Pulumi & AWS: Deploy stack"
meta_desc: Learn how to deploy your stack to an AWS project in this guide.
block_external_search_index: true
---

### Configure Pulumi to access your AWS account

Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user account that has **Programmatic access** with rights to deploy and manage resources handled through Pulumi.

If you have previously <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html" target="_blank">installed</a> and <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html" target="_blank">configured</a> the AWS CLI, Pulumi will respect and use your configuration settings.

If you do not have the AWS CLI installed or plan on using Pulumi from within a CI/CD pipeline, <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">retrieve your access key ID and secret access key</a> and then set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables on your workstation.

{{< chooser os "linux,macos,windows" >}}
{{% choosable os linux %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os macos %}}

```bash
$ export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}
{{< /chooser >}}

For additional information on setting and using AWS credentials, see [AWS Setup](/registry/packages/aws/installation-configuration/).

### Deploy stack

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

{{< console-note >}}

Now that the bucket has been provisioned, let's modify the program to host a static website.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/aws/get-started/review-project-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/aws/get-started/modify-program-b/">Modify Program &rarr;</a>
</div>
