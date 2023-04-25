---
title: Deploy the Stack | Azure
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: Learn how to deploy your stack to an Azure project in this guide.
weight: 5
menu:
  getstarted:
    parent: azure
    identifier: azure-deploy-stack

aliases: ["/docs/quickstart/azure/deploy-stack/"]
---

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
  yes
> no
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

Remember the output you defined in the previous step? That [stack output](/docs/intro/concepts/stack#outputs) can be seen in the `Outputs:` section of your update. You can access your outputs from the CLI by running the `pulumi stack output [property-name]` command. For example you can print the primary key of your bucket with the following command:

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

{{< get-started-stepper >}}
