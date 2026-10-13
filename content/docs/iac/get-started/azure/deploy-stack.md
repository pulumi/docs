---
title_tag: Deploy the Stack | Azure
title: Deploy to Azure
h1: "Get started with Pulumi and Azure"
meta_desc: Learn how to deploy your stack to Azure in this guide.
weight: 5
menu:
    iac:
        name: Deploy
        identifier: azure-get-started.deploy-stack
        parent: azure-get-started
        weight: 5
aliases:
    - /docs/quickstart/azure/deploy-stack/
    - /docs/clouds/azure/get-started/deploy-stack/
---

## Deploy to Azure

Now run `pulumi up` to start deploying your new storage account:

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

```output
Previewing update (dev):

    Type                                              Name             Plan
 +   pulumi:pulumi:Stack                              quickstart-dev   create
 +   ├─ azure-native:resources:ResourceGroup          resourceGroup    create
 +   └─ azure-native:storage:StorageAccount           sa               create

Outputs:
    storageAccountName: [unknown]

Resources:
    + 3 to create

Do you want to perform this update?
> yes
  no
  details
```

No changes have been made yet. To cancel, select `no`. To see more information about the proposed update, such as
your storage account's properties, select `details`.

### Performing the update

To proceed and deploy your new storage account, select `yes`. This begins an **update**:

```output
Do you want to perform this update? yes
Updating (dev):

View in Browser (Ctrl+O): https://app.pulumi.com/your-org-name/quickstart/dev/updates/1

     Type                                     Name             Status
 +   pulumi:pulumi:Stack                      quickstart-dev   created (25s)
 +   ├─ azure-native:resources:ResourceGroup  resourceGroup    created (2s)
 +   └─ azure-native:storage:StorageAccount   sa               created (20s)

Outputs:
    storageAccountName: "sa8deefa78"

Resources:
    + 3 created

Duration: 27s
```

Updates can take some time since they wait for the cloud resources to finish being created.

{{< auto-naming-note resource="storage account" suffix="8deefa78" >}}

### Using stack outputs

The storage account name is available as a stack output. To view it:

{{% choosable os "linux,macos" %}}

{{% choosable language "typescript,go,csharp,java,yaml" %}}

```bash
$ pulumi stack output storageAccountName
```

{{% /choosable %}}

{{% choosable language "python,hcl" %}}

```bash
$ pulumi stack output storage_account_name
```

{{% /choosable %}}

{{% /choosable %}}

{{% choosable os "windows" %}}

{{% choosable language "typescript,go,csharp,java,yaml" %}}

```powershell
> pulumi stack output storageAccountName
```

{{% /choosable %}}

{{% choosable language "python,hcl" %}}

```powershell
> pulumi stack output storage_account_name
```

{{% /choosable %}}

{{% /choosable %}}

The command prints the storage account's name.

### View your update on Pulumi Cloud

If you are logged in to [Pulumi Cloud](/docs/iac/concepts/pulumi-cloud/), you'll see "View Live" hyperlinks in the CLI output during your update. Each one opens your stack in the [Pulumi Cloud console](https://app.pulumi.com/), which shows detailed information about your stack including resources, configuration, a full history of updates, and more. Navigate to it to review the details of your update:

<a href="/images/getting-started/console-update.png" target="_blank">
    <img src="/images/getting-started/console-update.png" alt="A stack update with console output in the Pulumi Cloud console" />
</a>

Now that the storage account has been provisioned, you'll update it to host a static website.

{{< get-started-stepper >}}
