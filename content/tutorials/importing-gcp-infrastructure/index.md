---
title: "Importing Google Cloud Infrastructure"
title_tag: "Importing Google Cloud Infrastructure"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to import existing cloud resources into your Pulumi programs in this tutorial.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to import existing cloud resources into your Pulumi programs in this tutorial.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    Most infrastructure as code projects require working with existing cloud resources, whether those resources were originally created with another Infrastructure as Code (IaC) tool or manually provisioned with a cloud provider console or CLI. In this tutorial, you will learn how to import your existing Google Cloud resources to bring it under the management of Pulumi.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to import resources using the CLI
    - How to import resources in bulk
    - How to import resources in code

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - A [Google Cloud account](https://cloud.google.com/cloud-console/)
    - The [Google Cloud](https://cloud.google.com/sdk/docs/install)
    - Your desired [language runtime installed](/docs/iac/get-started/gcp/begin/#install-language-runtime)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - gcp
---

## Create initial resources

To start, login to the [Google Cloud Console](https://console.cloud.google.com/) and follow the instructions in the official Google Cloud documentation to [create a new Cloud Storage bucket](https://cloud.google.com/storage/docs/creating-buckets#create-bucket#console).

![Example Storage Bucket](storage-bucket.png)

Then, login to the [Pulumi CLI](/tutorials/cli-authentication/) and ensure it is [configured to use your Google Cloud account](/docs/iac/get-started/gcp/begin/#configure-pulumi-to-access-your-google-cloud-account). Next, [create a new project and stack](/docs/iac/get-started/gcp/create-project/) that will be used to hold the resource definition for your imported resources.

```bash
# Example using Python
$ mkdir pulumi-tutorial-import
$ cd pulumi-tutorial-import
$ pulumi new python
```

This tutorial will define resources using the Google Cloud Classic provider, so you will also need to make sure to [install the Google Cloud Classic dependency into your project](/registry/packages/gcp/installation-configuration/).

## Importing a resource

In Pulumi, there are three paths to take when importing resources:

- the `pulumi import` CLI command for individual resources
- the `pulumi import` CLI command with a special JSON file for bulk import
- an import option in your Pulumi program code.

### Import using the CLI

The `pulumi import` command looks up the resource using the specified type token and resource identifier, adds the resource to the stack's current state, and emits the code required to manage the resource with Pulumi from that point forward. This option requires the least manual effort, so it is generally recommended and best suited to projects consisting consisting of only one stack.

To import an existing cloud resource with the Pulumi CLI, use the following syntax:

```bash
$ pulumi import <type> <name> <id>
```

- The first argument, `type`, is the Pulumi type token to use for the imported resource. You can find the type token for a given resource by navigating to the Import section of the resource's API documentation in the [Pulumi Registry](/registry/). For example, the type token of an [Google Cloud Storage Bucket](/registry/packages/gcp/api-docs/storage/bucket/#import) resource is `gcp:storage/bucket:Bucket`.

  ![Import section of API documentation](pulumi-storage-bucket-import-section.png)

- The second argument, `name`, is the [resource name](/docs/concepts/resources/names) to apply to the resource once it's imported.

- The third argument, `id`, corresponds to the value you would use in Pulumi to lookup the resource in the cloud provider. This value should correspond to the designated `lookup property` specified in the **Import** section of the resource's API documentation in the Registry. In the case of an Google Cloud Storage Bucket, this would be `bucket_name` or `project_id/bucket_name`.

{{< notes type="info" >}}

If the project ID is not passed to the import command, it will be inferred from the provider block or environment variables.

{{< /notes >}}

When put all together, the `import` command should look something like the following example, where `imported-storage-bucket` is the resource name that will be applied to the Storage Bucket once imported.

```bash
$ pulumi import gcp:storage/bucket:Bucket imported-storage-bucket pulumi-tutorial-storage-bucket
```

The output should look something like the following:

```bash
$ pulumi import gcp:storage/bucket:Bucket imported-storage-bucket pulumi-tutorial-storage-bucket

Previewing import (dev)

     Type                   Name                     Plan
 +   pulumi:pulumi:Stack    dev                      create
 =   └─ gcp:storage:Bucket  imported-storage-bucket  import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this import?  [Use arrows to move, type to filter]
> yes
  no
  details
```

Notice the equals sign (`=`) instead of our usual plus sign (`+`) in the resource table and in the details. This is Pulumi’s way of telling you that it’s adding something to the state without modifying it.

Choose `yes` to complete the import. This will immediately add the resource to the current stack’s state and will emit a block of code to `STDOUT` to be added to your Pulumi program. If the current program were written in Python, for example, the resulting CLI output would resemble the following:

```bash
...
Importing (dev)

     Type                   Name                     Status
 +   pulumi:pulumi:Stack    dev                      created
 =   └─ gcp:storage:Bucket  imported-storage-bucket  imported (0.42s)

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 4s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

import pulumi
import pulumi_gcp as gcp

imported_storage_bucket = gcp.storage.Bucket("imported-storage-bucket",
    location="US",
    name="pulumi-tutorial-storage-bucket",
    project="pulumi-devrel",
    public_access_prevention="enforced",
    rpo="DEFAULT",
    uniform_bucket_level_access=True,
    opts = pulumi.ResourceOptions(protect=True))
```

Next, copy the emitted code snippet and replace the contents of your Pulumi program file with it. Then, save the file and run `pulumi up`. You should see that the update produces no changes:

```bash
$ pulumi up

Previewing update (dev)

     Type                 Name                     Plan
     pulumi:pulumi:Stack  dev

Resources:
    2 unchanged

Do you want to perform this update? yes

Updating (dev)

     Type                 Name                     Status
     pulumi:pulumi:Stack  dev

Resources:
    2 unchanged

Duration: 2s
```

The resource is now under management with Pulumi!

{{< notes type="info" >}}

Resources imported with the CLI are marked as __protected__ to guard against accidental deletion. If, for example, you forgot to append the generated code to your program before running another `pulumi up`, Pulumi would first interpret the missing code as an intention to delete the resource. The `protect` property will prevent this from happening, leaving the resource intact. If you ever want to delete this resource, you will have to set the `protect` property to `false` in the code. You can learn more by visiting the [Resource option: protect documentation](/docs/concepts/options/protect/).

{{< /notes >}}

### Import in bulk

The `pulumi import` command also enables you to import resources in bulk for scenarios in which you need to bring multiple resources under management with Pulumi. To do so, you will need to create a JSON file that has all of the required information for each resource: a `type`, a desired `name`, and an `id`.

To start, return to the Google Cloud console and create two additional Storage Buckets. Next, return to your program folder and create a new file called `resources.json`. Inside of this file, copy and paste the following JSON object, making sure to replace the values of the `id` parameters with the actual values for your environment:

```json
{
    "resources": [
        {
            "type": "gcp:storage/bucket:Bucket",
            "name": "second-imported-storage-bucket",
            "id": "tutorial-storage-bucket-2" # REPLACE
        },
        {
            "type": "gcp:storage/bucket:Bucket",
            "name": "third-imported-storage-bucket",
            "id": "tutorial-storage-bucket-3" # REPLACE
        }
    ]
}
```

To import these resources, save the file and then run the `pulumi import` command with the `-f` flag, passing in the path to the `resources.json` file:

```bash
$ pulumi import -f ./resources.json

Previewing import (dev)

     Type                   Name                            Plan
 +   pulumi:pulumi:Stack    dev                             create
 =   ├─ gcp:storage:Bucket  second-imported-storage-bucket  import
 =   └─ gcp:storage:Bucket  third-imported-storage-bucket   import

Resources:
    = 2 to import
    2 unchanged

Do you want to perform this import? yes

Importing (dev)

     Type                   Name                              Status
     pulumi:pulumi:Stack    dev
 =   ├─ gcp:storage:Bucket  second-imported-storage-bucket    imported (1s)
 =   └─ gcp:storage:Bucket  third-imported-storage-bucket     imported (2s)

Resources:
    = 2 imported
    2 unchanged

Duration: 6s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.

# Code begins here...
```

Just like when running the command against a single resource, the `pulumi import` command will import the resources into your stack's state file and will generate the code snippets for all of the resources in the JSON file. Once again, copy the generated code for the two new resources into your existing program file, save the file, and run the `pulumi up` command to bring these new resources under the management of Pulumi.

{{< notes type="info" >}}

You only need to copy over the resource definitions of the two Storage Buckets and not the import statements again.

{{< /notes >}}

### Import using code

The third method to import existing cloud resources into a Pulumi project is by defining the resource code yourself and configuring the [`import` resource option](/docs/iac/concepts/options/import/) in the resource's definition. This approach may be better suited for scenarios that require importing multiple resources of the same type across multiple stacks and/or deployment environments as part of an automation workflow.

To demonstrate, you will start by [creating a simple Service Account](https://cloud.google.com/iam/docs/service-accounts-create#iam-service-accounts-create-console) in the Google Cloud portal. Once that is complete, you will need to identify the lookup property of the Service Account resource. To do so, navigate to the **Import** section of the [Google Cloud Service Account resource page](/registry/packages/gcp/api-docs/serviceaccount/account/#import) in the Pulumi documentation. You will notice that the lookup property is the following, where `{{project_id}}` refers to the ID of your Google Cloud project, and `{{email}}` refers to the email address of the Service Account:

```
projects/{{project_id}}/serviceAccounts/{{email}}
```

Now, navigate to your program code file and update the code with the following resource definition, making sure to replace the values of the `service account display name` and `service account email prefix` variables with the values of your own Service Account:

{{< example-program path="gcp-import-service-account" >}}

As you can see, the lookup property of the Resource Goup resource has been provided as the value of the `import` option in the resource definition.

At this point, the definition for the imported resources has only been written, meaning it has not yet been imported into your project's state and is therefore not yet under management by Pulumi. To complete the import process using this method, you will need to save your file and run the `pulumi up` command. You should see output resembling the following example:

```bash
$ pulumi up -y
Previewing update (dev)

     Type                           Name                               Plan
 +   pulumi:pulumi:Stack            dev                                create
 =   └─ gcp:serviceaccount:Account  imported-tutorial-service-account  import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Updating (dev)

     Type                           Name                               Status
 +   pulumi:pulumi:Stack            dev                                created (5s)
 =   └─ gcp:serviceaccount:Account  imported-tutorial-service-account  imported (0.71s)

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 6s
```

It is important to note that when defining resources that you want to import using the `import` resource option method, the resource definition must match all properties of the existing resource. If you fail to include all of the existing properties, you will run into an error similar to the following:

```bash {hl_lines=[5]}
Previewing update (dev)

     Type                           Name                      Plan       Info
 +   pulumi:pulumi:Stack            dev                       create
 =   └─ gcp:serviceaccount:Account  imported-service-acct     import     [diff: -tags]; 1 warning

Diagnostics:
  gcp:serviceaccount:Account (imported-service-acct):
    warning: inputs to import do not match the existing resource; importing this resource will fail

Resources:
    + 1 to create
    = 1 to import
    2 changes

Updating (dev)

     Type                           Name                     Status                       Info
 +   pulumi:pulumi:Stack            dev                      **creating failed (5s)**     1 error
 =   └─ gcp:serviceaccount:Account  imported-service-acct    **importing failed**         1 error

Diagnostics:
  gcp:serviceaccount:Account (imported-service-acct):
    error: inputs to import do not match the existing resource

  pulumi:pulumi:Stack (dev):
    error: update failed

Resources:
    + 1 created

Duration: 7s
```

The highlighted line in the preview section of the output indicates which property of the existing resource is missing in the resource definition. You can use this to correct your resource definition before re-deploying. Once a resource is successfully imported, make sure to remove the `import` option from your code because Pulumi is now managing the resource.

## Clean-up

{{< cleanup >}}

{{< notes type="warning" >}}

With the resources you imported via the CLI command, make sure to set the `protect` property to `false` in the code and run `pulumi up` to make the change before running the `pulumi destroy` command. Otherwise the deletion will fail.

{{< /notes >}}

## Next steps

In this tutorial, you imported existing cloud resources via the CLI and updated the program code to include the definition of those imported resources. You also imported existing cloud resources by manually defining the resource definition using the `import` resource option method.

To learn more about creating and managing resources in Pulumi, take a look a the following resources:

- Learn more about importing resources in Pulumi in the [Adopting Pulumi -> Import resources documentation](/docs/iac/adopting-pulumi/import/).
- Learn more about migrating to Pulumi in the [Migrating from other solutions to Pulumi documentation](/docs/iac/adopting-pulumi/migrating-to-pulumi/).
- Learn more about other useful Pulumi CLI commands in the [Pulumi CLI overview documentation](/docs/iac/cli/).
