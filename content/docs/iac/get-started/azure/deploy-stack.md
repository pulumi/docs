---
title_tag: Deploy the Stack | Azure
title: Deploy the stack
h1: "Deploy the stack"
meta_desc: Learn how to deploy your stack to an Azure project in this guide.
weight: 6
menu:
    iac:
        name: Deploy the stack
        identifier: azure-get-started.deploy-stack
        parent: azure-get-started
        weight: 6
aliases:
    - /docs/quickstart/azure/deploy-stack/
    - /docs/clouds/azure/get-started/deploy-stack/
---

Now deploy the stack with `pulumi up`:

```bash
$ pulumi up
```

This command first shows you a preview of the changes to be made:

```
Previewing update (dev):

     Type                                     Name             Plan
 +   pulumi:pulumi:Stack                      quickstart-dev   create
 +   ├─ azure-native:resources:ResourceGroup  resourceGroup    create
 +   └─ azure-native:storage:StorageAccount   sa               create

Outputs:
    storageAccountName: [unknown]

Resources:
    + 3 to create

Do you want to perform this update?
> yes
  no
  details
```

Choosing `yes` proceeds with an update, which creates the resources in Azure:

```
Updating (dev):

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

The update completes when all resources are created. Storage accounts take a bit longer, so this may take 20-30 seconds.

{{< auto-naming-note resource="storage account" suffix="8deefa78" >}}

Notice the storage account's name was emitted as a [stack output](/docs/iac/concepts/stacks/#outputs). You can retrieve the output's value with `pulumi stack output`:

{{% choosable language "typescript,go,csharp,java,yaml" %}}

```bash
$ pulumi stack output storageAccountName
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pulumi stack output storage_account_name
```

{{% /choosable %}}

Next, you'll turn the storage account into a static website.

{{< get-started-stepper >}}
