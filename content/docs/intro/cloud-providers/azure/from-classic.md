---
title: Migration from classic Azure to Azure-Native
meta_desc: How to migrate from the classic Azure provider to the native Azure provider.
---

Pulumi currently has two providers to manage resources in Microsoft Azure: [classic Pulumi Azure]({{< relref "/docs/reference/pkg/azure" >}}) and [native Pulumi Azure]({{< relref "./" >}}). This guide explains the differences between the two providers, our recommendations about using them, and a migration guide from the classic Azure provider to the native Azure provider.

## Key Difference between Azure and Azure-Native

The classic Pulumi Azure provider is based on the Terraform AzureRM provider. Every resource in this provider is manually implemented using the Azure Go SDK. The API of each resource is defined by its developer and doesn’t have to match the Microsoft Azure's API.

The native Pulumi Azure provider is based on the Open API specifications of Azure Resource Manager published by Microsoft. Pulumi generates resources automatically from those API specifications. This approach ensures higher quality and higher fidelity with the Azure platform. Every property of each resource is always represented in the SDKs.

Because of this difference, the SDKs of the two providers are not compatible with each other. This guide aims to help you understand and adopt the native provider in your Pulumi projects.

## Configuration

Configurations of the native Azure provider and the classic Azure provider are similar. However, for the new provider, each setting has to start with `azure-native` instead of `azure`. For instance, the active subscription is configured with `azure-native:subscriptionId` instead of `azure:subscriptionId`.

You can find all the configuration settings in the Configuration section of [Azure-Native]({{< relref "./" >}}).

## Use the native Azure provider for new projects

The native Azure provider for Pulumi is currently on its way to general availability. As of today, we recommend using the native Azure provider for any new Pulumi project targeting Microsoft Azure. We don’t expect to ship significant breaking changes before the 1.0 release planned for April 2021.

## Mix and match in the same project

It is possible to use both Azure and Azure-Native providers in the same Pulumi program. You can reference both packages, use a mix of resources from both of them, and flow outputs of any resource to any other resource.

For example, the following snippet defines a Resource Group with Pulumi Azure and a Storage Account with Pulumi Azure-Native. The snippets below are shown in TypeScript but the same process applies to all other runtimes.

```typescript
import * as azure from '@pulumi/azure';
import * as azure_native from '@pulumi/azure-native';

const rg = new azure.core.ResourceGroup("my-rg");

const account = new azure_native.storage.StorageAccount("sa", {
   resourceGroupName: rg.name,
   sku: {
       name: azure_native.storage.SkuName.Standard_LRS,
   },
   kind: azure_native.storage.Kind.StorageV2,
});
```

This approach is practical as the first step of adopting the native Azure provider in existing projects relying on the classic Azure provider. The classic Azure provider isn't deprecated, and we will keep supporting it indefinitely. You can keep using it in your existing infrastructure while embracing the native Azure provider for any newly created resources.

## Move resources from classic Azure to Azure-Native

As explained above, the two provider APIs are not compatible with each other. Therefore, there is no automatic way to migrate existing resources from classic Azure to Azure-Native.

In this section, we give an example of migrating a Pulumi program from Azure to Azure-Native. We start with two resources managed by the old provider and move them one-by-one to the new provider. The process is mostly manual, but it does not require any disruption in your actual Microsoft Azure cloud environment.

Let's start with the following existing program which defines two Azure resources. Imagine this is your existing stack with resources deployed to your cloud account.

```typescript
import * as azure from '@pulumi/azure';

const resourceGroup = new azure.core.ResourceGroup("my-rg");

const account = new azure.storage.Account("storage", {
   resourceGroupName: resourceGroup.name,
   accountTier: "Standard",
   accountReplicationType: "LRS",
});
```

### Reference Azure-Native

Begin the migration by referencing the Azure-Native package

```
npm install @pulumi/azure-native
```

Now, open your stack configuration file (e.g., Pulumi.dev.yaml). Copy all settings that start with azure: and redefine them with the `azure-native:` prefix. In a simple case, the result may look like this

```yaml
config:
 azure:location: westus
 azure-native:location: westus
```

### Migrate the Resource Group

Let's run through the steps to migrate our first resource: the resource group.

1. Identify the type of the new resource in the native provider. In our case, it’s going to be a ResourceGroup resource in the resources module. Note that both names can be different from the names in the Azure provider. We can find the new resource in the [API Reference docs](https://www.pulumi.com/docs/reference/pkg/azure-native/resources/resourcegroup/).

2. Scroll down the API Reference doc to the Import section and copy the import command:
`pulumi import azure-native:resources/latest:ResourceGroup my-resource-group /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/my-resource-group`

3. Run the command `pulumi stack export` and open the resulting JSON in a text editor. Find the entry with type `azure:core/resourceGroup:ResourceGroup` and note its `id` and `urn` property values. The `id` should look like this:
`/subscriptions/01234567-89ab-cdef-0123-456789abcdef/resourceGroups/my-rgca05c9f8`
and the `urn` should be like
`urn:pulumi:dev::ts::azure:core/resourceGroup:ResourceGroup::my-rg`

4. Use this ID and your desired logical resource name to compose the import command. For the example above, it will be
`pulumi import azure-native:resources/latest:ResourceGroup my-rg /subscriptions/01234567-89ab-cdef-0123-456789abcdef/resourceGroups/my-rgca05c9f8`

5. Run the command to start managing the existing resource group with the native Azure provider and confirm the import operation. The following output should be printed:

    ```
    Importing (dev)

      Type                                     Name      Status
      pulumi:pulumi:Stack                      ts-dev
    = └─ azure-native:resources:ResourceGroup  my-rg     imported

    Resources:
        = 1 imported
        4 unchanged

    Duration: 7s

    Please copy the following code into your Pulumi application. Not doing so will
    cause Pulumi to report that an update will happen on the next update command.

    Please note that the imported resources are marked as protected. To destroy
    them you will need to remove the `protect` option and run `pulumi update`
    *before* the destroy will take effect.

    import * as pulumi from "@pulumi/pulumi";
    import * as azure_native from "@pulumi/azure-native";

    const my_rg = new azure_native.resources.ResourceGroup("my-rg", {
        location: "westeurope",
        resourceGroupName: "my-rgca05c9f8",
    }, {
        protect: true,
    });
    ```

6. Copy the code from the output to your program. Now the resource is managed by the native Azure provider.

7. Adjust the program so that the Storage Account depends on the new resource `my_rg` instead of the old resource `resourceGroup`:

    ```typescript
    import * as azure from '@pulumi/azure';
    import * as azure_native from "@pulumi/azure-native";

    const resourceGroup = new azure.core.ResourceGroup("my-rg");

    const my_rg = new azure_native.resources.ResourceGroup("my-rg", {
      location: "westus",
      resourceGroupName: "my-rgca05c9f8",
    }, {
      protect: true,
    });

    const account = new azure.storage.Account("storage", {
      resourceGroupName: my_rg.name,
      accountTier: "Standard",
      accountReplicationType: "LRS",
    });
    ```

8. Run `pulumi up` and confirm the action, even though the preview shows no changes. This will override the dependency from the Storage Account to the new Resource Group resource definition.

9. Now, we are ready to remove the state of the resource group managed by the classic Azure provider. Run the following command with the `urn` noted at step 3:

    ```
    pulumi state delete urn:pulumi:dev::ts::azure:core/resourceGroup:ResourceGroup::my-rg
    warning: This command will edit your stack's state directly. Confirm? Yes
    Resource deleted successfully
    ```

10. Finally, remove the code for the old resourceGroup resource. You may also refactor the code to use the same name for the new resource and unprotect it. Feel free to remove the location attribute if it matches your stack configuration. The resulting code is shown below:

    ```typescript
    import * as azure from '@pulumi/azure';
    import * as azure_native from "@pulumi/azure-native";

    const resourceGroup = new azure_native.resources.ResourceGroup("my-rg", {
      resourceGroupName: "my-rgca05c9f9",
    });

    const account = new azure.storage.Account("storage", {
      resourceGroupName: resourceGroup.name,
      accountTier: "Standard",
      accountReplicationType: "LRS",
    });
    ```

### Migrate the Storage Account

Follow the same steps to migrate the storage account.

Locate the resource in the [API docs](https://www.pulumi.com/docs/reference/pkg/azure-native/storage/storageaccount/).

Compose and run the import command:

```
pulumi import azure-native:storage/latest:StorageAccount storage /subscriptions/01234567-89ab-cdef-0123-456789abcdef/resourceGroups/my-rgca05c9f8/providers/Microsoft.Storage/storageAccounts/storagea791686
```

and paste the code to your program.

Note that the printed code is quite verbose: Pulumi imports all properties reported by Azure explicitly.

```typescript
const storage = new azure_native.storage.StorageAccount("storage", {
   accessTier: "Hot",
   accountName: "storagea791686",
   allowBlobPublicAccess: false,
   enableHttpsTrafficOnly: true,
   encryption: {
       keySource: "Microsoft.Storage",
       services: {
           blob: {
               enabled: true,
               keyType: "Account",
           },
           file: {
               enabled: true,
               keyType: "Account",
           },
       },
   },
   isHnsEnabled: false,
   kind: "StorageV2",
   location: "westeurope",
   minimumTlsVersion: "TLS1_0",
   networkRuleSet: {
       bypass: "AzureServices",
       defaultAction: "Allow",
   },
   resourceGroupName: "my-rgca05c9f8",
   sku: {
       name: "Standard_LRS",
   },
}, {
   protect: true,
});
```

No other resource depends on this storage account in our program, so you can go ahead and remove the old resource from the state

```
pulumi state delete urn:pulumi:dev::ts::azure:storage/account:Account::storage
```

Finally, remove the old resource from the code, remove the reference to `@pulumi/azure`, and refactor the imported code be more concise and to reference the resource group resource explicitly:

```typescript
import * as native from "@pulumi/azure-native";

const resourceGroup = new native.resources.ResourceGroup("my-rg", {
   resourceGroupName: "my-rgca05c9f8",
});

const storage = new native.storage.StorageAccount("storage", {
   resourceGroupName: resourceGroup.name,
   accountName: "storagea791686",
   isHnsEnabled: false,
   kind: "StorageV2",
   sku: {
       name: "Standard_LRS",
   },
});
```

You have to run `pulumi up` to apply these changes to the Storage Account (without replacing it).

The migration is now complete!
