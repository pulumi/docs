---
title: Destroy the Stack
weight: 10
menu:
  quickstart:
    parent: azure
    identifier: azure-destroy-stack
---

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. Pulumi deletes the storage account and the resource group before it considers the destroy operation to be complete.

```
Previewing destroy (dev):

     Type                         Name                     Plan       
 -   pulumi:pulumi:Stack          update-az-templates-dev  delete     
 -   ├─ azure:storage:Account     storage                  delete     
 -   └─ azure:core:ResourceGroup  resourceGroup            delete     
 
Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                         Name                     Status      
 -   pulumi:pulumi:Stack          update-az-templates-dev  deleted     
 -   ├─ azure:storage:Account     storage                  deleted     
 -   └─ azure:core:ResourceGroup  resourceGroup            deleted     
 
Resources:
    - 3 deleted

Duration: 53s
```

To delete the stack itself, run `pulumi stack rm`.

Next, we'll look at some next steps.

{{< get-started-stepper >}}
