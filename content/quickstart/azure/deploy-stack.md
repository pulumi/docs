---
title: Deploy the Stack
weight: 6
menu:
  quickstart:
    parent: azure
    identifier: azure-deploy-stack
---

Let's go ahead and deploy the stack:

```bash
$ pulumi up
```

This command instructs Pulumi to determine the resources needed to create the stack. First, a preview is shown of the changes that will be made:

```
Previewing update (dev):

     Type                         Name            Plan
 +   pulumi:pulumi:Stack          quickstart-dev  create
 +   ├─ azure:core:ResourceGroup  resourceGroup   create
 +   └─ azure:storage:Account     storage         create

Resources:
    + 3 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in Azure.

```
Do you want to perform this update? yes
Updating (dev):

     Type                         Name            Status
 +   pulumi:pulumi:Stack          quickstart-dev  created
 +   ├─ azure:core:ResourceGroup  resourceGroup   created
 +   └─ azure:storage:Account     storage         created

Outputs:
    connectionString: "DefaultEndpointsProtocol=https;AccountName=storagec10b9cad;AccountKey=f5JxKN8M7mECDlzdB9zTwfJWSplo8jFTFFKRTzGAldscILf1ftrJPaspSA69tzLe24WBbWJ9yTu+mzjaqmPEew==;EndpointSuffix=core.windows.net"

Resources:
    + 3 created

Duration: 26s
```

The storage account's connection string, that we exported, is shown as a [stack output]({{< relref "/reference/stack.md#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
