---
title_tag: Destroy the Stack | Azure
meta_desc: This page provides an overview of how to destroy a Pulumi stack of an Azure project.
title: Destroy stack
h1: "Pulumi & Azure: Destroy stack"
block_external_search_index: true
---

Now that you've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of your stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits until all resources are shut down and deleted before it considers the destroy operation to be complete.

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

Do you want to perform this destroy? yes
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

To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). Note that this removes the stack
entirely from the Pulumi Cloud, along with all of its update history.

Congratulations! You've successfully provisioned some cloud resources using Pulumi. By completing this guide you have successfully:

- Created a Pulumi new project.
- Provisioned a new Azure storage account and container.
- Added an `index.html` file to your container.
- Served the `index.html` as a static website.
- Destroyed the resources you've provisioned.

On the next page, we have a collection of examples and tutorials that you can deploy as they are or use them as a foundation for your own applications and infrastructure projects.

<div class="mt-6">
    <a data-track="previous-step" class="btn btn-secondary" href="/docs/clouds/azure/get-started/deploy-changes-b/">&larr; Previous Step</a>
    <a data-track="next-step" class="btn" href="/docs/clouds/azure/get-started/next-steps/">Next Steps &rarr;</a>
</div>
