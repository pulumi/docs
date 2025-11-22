---
title_tag: Destroy the Stack | Azure
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an Azure project.
title: Destroy stack
h1: "Pulumi & Azure: Destroy stack"
weight: 8
menu:
    iac:
        name: Cleanup & destroy
        identifier: azure-get-started.destroy-stack
        parent: azure-get-started
        weight: 8
aliases:
    - /docs/quickstart/azure/destroy-stack/
    - /docs/clouds/azure/get-started/destroy-stack/
---

## Cleanup & destroy the stack

Our final step is to clean up all of the resources we've provisioned. This is as simple as running `pulumi destroy`:

{{% choosable os "linux,macos" %}}

```bash
$ pulumi destroy
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> pulumi destroy
```

{{% /choosable %}}

Just like `pulumi up`, `pulumi destroy` shows you a preview before performing any changes:

```
Previewing destroy (dev):

     Type                                                         Name                     Plan
 -   pulumi:pulumi:Stack                                          quickstart-dev           delete
 -   ├─ azure-native:storage:Blob                                 index.html               delete
 -   ├─ azure-native:storage:StorageAccountStaticWebsite          staticWebsite            delete
 -   ├─ azure-native:storage:StorageAccount                       sa                       delete
 -   └─ azure-native:resources:ResourceGroup                      resourceGroup            delete

Outputs:
  - primaryStorageKey: "<key_value>"
  - staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    - 5 to delete

Do you want to perform this destroy?
> yes
  no
  details
```

As with an update, we can choose `no` or `details`; select `yes` to proceed:

```
Destroying (dev):

     Type                                                   Name                Status
 -   pulumi:pulumi:Stack                                    quickstart-dev      deleted
 -   ├─ azure-native:storage:Blob                           index.html          deleted
 -   ├─ azure-native:storage:StorageAccountStaticWebsite    staticWebsite       deleted
 -   ├─ azure-native:storage:StorageAccount                 sa                  deleted
 -   └─ azure-native:resources:ResourceGroup                resourceGroup       deleted

Outputs:
  - primaryStorageKey: "<key_value>"
  - staticEndpoint   : "https://sa8dd8af62.z22.web.core.windows.net/"

Resources:
    - 5 deleted

Duration: 53s
```

At this stage, your stack still exists, but all cloud resources have been deleted from it.

## Remove the stack

The final step is to remove the stack itself. Destroy keeps the stack around so that you still have the full
history of what happened to the stack. Running [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm) will
delete it entirely, including all history and state snapshots. Be careful, this step cannot be undone!

{{% choosable "os" "macos,linux" %}}

```bash
$ pulumi stack rm
```

{{% /choosable %}}
{{% choosable "os" "windows" %}}

```powershell
> pulumi stack rm
```

{{% /choosable %}}

You'll be prompted to confirm the removal. Confirm it to successfully complete this tutorial.

{{< get-started-stepper >}}
