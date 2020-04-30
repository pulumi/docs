---
title: Deploy the Stack | Azure
h1: Deploy the Stack
linktitle: Deploy the Stack
meta_desc: This page provides an overview of how deploy changes to an Azure project.
weight: 7
menu:
  getstarted:
    parent: azure
    identifier: azure-deploy-stack

aliases: ["/docs/quickstart/azure/deploy-stack/"]
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
    connectionString: "DefaultEndpointsProtocol=https;AccountName=storage1b3018e9;AccountKey=...;EndpointSuffix=core.windows.net"

Resources:
    + 3 created

Duration: 26s
```

The storage account's connection string that we exported is shown as a [stack output]({{< prelref "/docs/intro/concepts/stack#outputs" >}}).

Next, we'll make some modifications to the program.

{{< get-started-stepper >}}
