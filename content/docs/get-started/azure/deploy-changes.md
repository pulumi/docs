---
title: Deploy the Changes | Azure
h1: Deploy the Changes
linktitle: Deploy the Changes
meta_desc: This page provides an overview of how deploy changes to an Azure project.
weight: 9
menu:
  getstarted:
    parent: azure
    identifier: azure-deploy-changes

aliases: ["/docs/quickstart/azure/deploy-changes/"]
---

Now let's deploy our changes.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                      Name                     Plan       Info
     pulumi:pulumi:Stack       update-az-templates-dev
 ~   └─ azure:storage:Account  storage                  update     [diff: ~enableHttpsTrafficOnly]

Resources:
    ~ 1 to update
    2 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will update the storage account to enable the HTTPS-only enforcement. The resource group hasn't changed so it remains as-is.

Choosing `yes` will proceed with the update.

```
Do you want to perform this update? yes
Updating (dev):

     Type                      Name                     Status      Info
     pulumi:pulumi:Stack       update-az-templates-dev
 ~   └─ azure:storage:Account  storage                  updated     [diff: ~enableHttpsTrafficOnly]

Outputs:
    connectionString: "DefaultEndpointsProtocol=https;AccountName=storagefeda4143;AccountKey=...;EndpointSuffix=core.windows.net"

Resources:
    ~ 1 updated
    2 unchanged

Duration: 4s
```

Next, we'll destroy the stack.

{{< get-started-stepper >}}
