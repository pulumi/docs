---
title_tag: Deploy the Stack | Google Cloud
meta_desc: This page provides an overview of how to deploy changes to a Google Cloud project.
title: Deploy stack
h1: "Pulumi & Google Cloud: Deploy stack"
block_external_search_index: true
---

### Configure Pulumi to access your Google Cloud account

Pulumi requires cloud credentials to manage and provision resources. You must use an IAM user or service account that has **Programmatic access** with rights to deploy and manage your Google Cloud resources.

You will need an IAM user account with permissions that can create and populate a Cloud Storage bucket, such as those in the predefined Storage Admin (`roles/storage.admin`) or the Storage Legacy Bucket Owner (`roles/storage.legacyBucketOwner`) roles.

When developing locally, we recommend that you install the [Google Cloud SDK](https://cloud.google.com/sdk/install) and then [authorize access with a user account](https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_user_account).

If `gcloud` is not configured to interact with your Google Cloud project, set it with the `config` command using the project's ID:

```bash
gcloud config set project <YOUR_GCP_PROJECT_ID>
```

Next, Pulumi requires default application credentials to interact with your Google Cloud resources, so run `auth application-default login` command to obtain those credentials.

```bash
gcloud auth application-default login
```

For additional information on setting and using Google Cloud credentials, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/).

### Deploy stack

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

Now that your bucket has been provisioned, let's modify the bucket to host a static website.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/gcp/get-started/review-project-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/gcp/get-started/modify-program-b/">Modify Program &rarr;</a>
</div>
