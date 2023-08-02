---
title_tag: Deploy the Stack | Azure
meta_desc: Learn how to deploy your stack to an Azure project in this guide.
title: Deploy stack
h1: "Pulumi & Azure: Deploy stack"
block_external_search_index: true
---

### Configure Pulumi to access your Microsoft Azure account

Pulumi requires cloud credentials to manage and provision resources. Pulumi can authenticate to Azure using a user account or service principal that has **Programmatic access** with rights to deploy and manage your Azure resources.

{{% notes type="info" %}}
Pulumi relies on the Azure SDK to authenticate requests from your computer to Azure. Your credentials are never sent to pulumi.com.
{{% /notes %}}

You will need a user account with permissions to create and populate Blob storage containers and provide anonymous access to a Blob file.

When developing locally, we recommend that you install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and then authorize access with a user account.

```bash
az login
```

After successfully logging in, you are ready to go.

{{% notes type="info" %}}
The Azure CLI, and thus Pulumi, will use the default subscription for the account. You can change the active subscription with the [`az account set`](https://docs.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az_account_set) command.
{{% /notes %}}

For additional information on authenticating with Azure, or to login with a service principal, see [Azure Setup](/registry/packages/azure-native/installation-configuration/).

### Deploy stack

Let's go ahead and deploy your stack:

```bash
$ pulumi up
```

This command evaluates your program and determines the resource updates to make. First, a preview is shown that outlines the changes that will be made when you run the update:

```
Previewing update (dev):

    Type                                              Name             Plan
 +   pulumi:pulumi:Stack                              quickstart-dev   create
 +   ├─ azure-native:resources:ResourceGroup          resourceGroup    create
 +   └─ azure-native:storage:StorageAccount           sa               create

Resources:
    + 3 to create

Do you want to perform this update?
> yes
  no
  details
```

Once the preview has finished, you are given three options to choose from. Choosing `details` will show you a rich diff of the changes to be made. Choosing `yes` will create your new storage account in Azure. Choosing `no` will return you to the user prompt without performing the update operation.

```
Do you want to perform this update? yes
Updating (dev):

     Type                                             Name             Status
 +   pulumi:pulumi:Stack                              quickstart-dev   created
 +   ├─ azure-native:resources:ResourceGroup          resourceGroup    created
 +   └─ azure-native:storage:StorageAccount           sa               created

Outputs:
    primaryStorageKey: "<key_value>"

Resources:
    + 3 created

Duration: 26s
```

Remember the output you defined in the previous step? That [stack output](/docs/concepts/stack#outputs) can be seen in the `Outputs:` section of your update. You can access your outputs from the CLI by running the `pulumi stack output [property-name]` command. For example you can print the primary key of your bucket with the following command:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
$ pulumi stack output primaryStorageKey
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi stack output primary_storage_key
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ pulumi stack output primaryStorageKey
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ pulumi stack output primaryStorageKey
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ pulumi stack output primaryStorageKey
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ pulumi stack output primaryStorageKey
```

{{% /choosable %}}

Running that command will print out the storage account's primary key.

{{< console-note >}}

Now that your storage account has been provisioned, let's modify it to host a static website.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/azure/get-started/review-project-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/azure/get-started/modify-program-b/">Modify Program &rarr;</a>
</div>
