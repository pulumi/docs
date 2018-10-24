---
title: Module compute
---

<a href="../index.html">@pulumi/azure</a> &gt; compute

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AvailabilitySet">class AvailabilitySet</a>
* <a href="#DataDiskAttachment">class DataDiskAttachment</a>
* <a href="#Extension">class Extension</a>
* <a href="#Image">class Image</a>
* <a href="#ManagedDisk">class ManagedDisk</a>
* <a href="#ScaleSet">class ScaleSet</a>
* <a href="#SharedImage">class SharedImage</a>
* <a href="#SharedImageGallery">class SharedImageGallery</a>
* <a href="#SharedImageVersion">class SharedImageVersion</a>
* <a href="#Snapshot">class Snapshot</a>
* <a href="#VirtualMachine">class VirtualMachine</a>
* <a href="#getImage">function getImage</a>
* <a href="#getManagedDisk">function getManagedDisk</a>
* <a href="#getPlatformImage">function getPlatformImage</a>
* <a href="#getSharedImage">function getSharedImage</a>
* <a href="#getSharedImageGallery">function getSharedImageGallery</a>
* <a href="#getSharedImageVersion">function getSharedImageVersion</a>
* <a href="#getSnapshot">function getSnapshot</a>
* <a href="#AvailabilitySetArgs">interface AvailabilitySetArgs</a>
* <a href="#AvailabilitySetState">interface AvailabilitySetState</a>
* <a href="#DataDiskAttachmentArgs">interface DataDiskAttachmentArgs</a>
* <a href="#DataDiskAttachmentState">interface DataDiskAttachmentState</a>
* <a href="#ExtensionArgs">interface ExtensionArgs</a>
* <a href="#ExtensionState">interface ExtensionState</a>
* <a href="#GetImageArgs">interface GetImageArgs</a>
* <a href="#GetImageResult">interface GetImageResult</a>
* <a href="#GetManagedDiskArgs">interface GetManagedDiskArgs</a>
* <a href="#GetManagedDiskResult">interface GetManagedDiskResult</a>
* <a href="#GetPlatformImageArgs">interface GetPlatformImageArgs</a>
* <a href="#GetPlatformImageResult">interface GetPlatformImageResult</a>
* <a href="#GetSharedImageArgs">interface GetSharedImageArgs</a>
* <a href="#GetSharedImageGalleryArgs">interface GetSharedImageGalleryArgs</a>
* <a href="#GetSharedImageGalleryResult">interface GetSharedImageGalleryResult</a>
* <a href="#GetSharedImageResult">interface GetSharedImageResult</a>
* <a href="#GetSharedImageVersionArgs">interface GetSharedImageVersionArgs</a>
* <a href="#GetSharedImageVersionResult">interface GetSharedImageVersionResult</a>
* <a href="#GetSnapshotArgs">interface GetSnapshotArgs</a>
* <a href="#GetSnapshotResult">interface GetSnapshotResult</a>
* <a href="#ImageArgs">interface ImageArgs</a>
* <a href="#ImageState">interface ImageState</a>
* <a href="#ManagedDiskArgs">interface ManagedDiskArgs</a>
* <a href="#ManagedDiskState">interface ManagedDiskState</a>
* <a href="#ScaleSetArgs">interface ScaleSetArgs</a>
* <a href="#ScaleSetState">interface ScaleSetState</a>
* <a href="#SharedImageArgs">interface SharedImageArgs</a>
* <a href="#SharedImageGalleryArgs">interface SharedImageGalleryArgs</a>
* <a href="#SharedImageGalleryState">interface SharedImageGalleryState</a>
* <a href="#SharedImageState">interface SharedImageState</a>
* <a href="#SharedImageVersionArgs">interface SharedImageVersionArgs</a>
* <a href="#SharedImageVersionState">interface SharedImageVersionState</a>
* <a href="#SnapshotArgs">interface SnapshotArgs</a>
* <a href="#SnapshotState">interface SnapshotState</a>
* <a href="#VirtualMachineArgs">interface VirtualMachineArgs</a>
* <a href="#VirtualMachineState">interface VirtualMachineState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts">compute/availabilitySet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts">compute/dataDiskAttachment.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts">compute/extension.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts">compute/getImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts">compute/getManagedDisk.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts">compute/getPlatformImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts">compute/getSharedImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts">compute/getSharedImageGallery.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts">compute/getSharedImageVersion.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts">compute/getSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts">compute/image.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts">compute/managedDisk.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts">compute/scaleSet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts">compute/sharedImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts">compute/sharedImageGallery.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts">compute/sharedImageVersion.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts">compute/snapshot.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts">compute/virtualMachine.ts</a> 


<h2 class="pdoc-module-header" id="AvailabilitySet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L10">class AvailabilitySet</a>
</h2>

Manages an availability set for virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L50">constructor</a>
</h3>

```typescript
new AvailabilitySet(name: string, args: AvailabilitySetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AvailabilitySet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AvailabilitySetState): AvailabilitySet
```


Get an existing AvailabilitySet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L30">property managed</a>
</h3>

```typescript
public managed: pulumi.Output<boolean | undefined>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L38">property platformFaultDomainCount</a>
</h3>

```typescript
public platformFaultDomainCount: pulumi.Output<number | undefined>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L42">property platformUpdateDomainCount</a>
</h3>

```typescript
public platformUpdateDomainCount: pulumi.Output<number | undefined>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DataDiskAttachment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L14">class DataDiskAttachment</a>
</h2>

Manages attaching a Disk to a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `azurerm_virtual_machine` resource, or using the `azurerm_virtual_machine_data_disk_attachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

-> **Please Note:** only Managed Disks are supported via this separate resource, Unmanaged Disks can be attached using the `storage_data_disk` block in the `azurerm_virtual_machine` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L50">constructor</a>
</h3>

```typescript
new DataDiskAttachment(name: string, args: DataDiskAttachmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DataDiskAttachment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataDiskAttachmentState): DataDiskAttachment
```


Get an existing DataDiskAttachment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L30">property caching</a>
</h3>

```typescript
public caching: pulumi.Output<string>;
```


Specifies the caching requirements for this Data Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L34">property createOption</a>
</h3>

```typescript
public createOption: pulumi.Output<string | undefined>;
```


The Create Option of the Data Disk, such as `Empty` or `Attach`. Defaults to `Attach`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L38">property lun</a>
</h3>

```typescript
public lun: pulumi.Output<number>;
```


The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L42">property managedDiskId</a>
</h3>

```typescript
public managedDiskId: pulumi.Output<string>;
```


The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L46">property virtualMachineId</a>
</h3>

```typescript
public virtualMachineId: pulumi.Output<string>;
```


The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L50">property writeAcceleratorEnabled</a>
</h3>

```typescript
public writeAcceleratorEnabled: pulumi.Output<boolean | undefined>;
```


Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.

<h2 class="pdoc-module-header" id="Extension">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L15">class Extension</a>
</h2>

Manages a Virtual Machine Extension to provide post deployment configuration
and run automated tasks.

~> **NOTE:** Custom Script Extensions for Linux & Windows require that the `commandToExecute` returns a `0` exit code to be classified as successfully deployed. You can achieve this by appending `exit 0` to the end of your `commandToExecute`.

-> **NOTE:** Custom Script Extensions require that the Azure Virtual Machine Guest Agent is running on the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L79">constructor</a>
</h3>

```typescript
new Extension(name: string, args: ExtensionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Extension resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExtensionState): Extension
```


Get an existing Extension resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L32">property autoUpgradeMinorVersion</a>
</h3>

```typescript
public autoUpgradeMinorVersion: pulumi.Output<boolean | undefined>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L37">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L47">property protectedSettings</a>
</h3>

```typescript
public protectedSettings: pulumi.Output<string | undefined>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L52">property publisher</a>
</h3>

```typescript
public publisher: pulumi.Output<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L63">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<string | undefined>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L64">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L69">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L74">property typeHandlerVersion</a>
</h3>

```typescript
public typeHandlerVersion: pulumi.Output<string>;
```


Specifies the version of the extension to
use, available versions can be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L79">property virtualMachineName</a>
</h3>

```typescript
public virtualMachineName: pulumi.Output<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="Image">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L10">class Image</a>
</h2>

Manage a custom virtual machine image that can be used to create virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L53">constructor</a>
</h3>

```typescript
new Image(name: string, args: ImageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Image resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageState): Image
```


Get an existing Image resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L26">property dataDisks</a>
</h3>

```typescript
public dataDisks: pulumi.Output<{ ... }[] | undefined>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L31">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L40">property osDisk</a>
</h3>

```typescript
public osDisk: pulumi.Output<{ ... } | undefined>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L49">property sourceVirtualMachineId</a>
</h3>

```typescript
public sourceVirtualMachineId: pulumi.Output<string | undefined>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L53">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ManagedDisk">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L10">class ManagedDisk</a>
</h2>

Manage a managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L80">constructor</a>
</h3>

```typescript
new ManagedDisk(name: string, args: ManagedDiskArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ManagedDisk resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagedDiskState): ManagedDisk
```


Get an existing ManagedDisk resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L26">property createOption</a>
</h3>

```typescript
public createOption: pulumi.Output<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L31">property diskSizeGb</a>
</h3>

```typescript
public diskSizeGb: pulumi.Output<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L35">property encryptionSettings</a>
</h3>

```typescript
public encryptionSettings: pulumi.Output<{ ... } | undefined>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L39">property imageReferenceId</a>
</h3>

```typescript
public imageReferenceId: pulumi.Output<string | undefined>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L44">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L54">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L59">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L63">property sourceResourceId</a>
</h3>

```typescript
public sourceResourceId: pulumi.Output<string | undefined>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L67">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L72">property storageAccountType</a>
</h3>

```typescript
public storageAccountType: pulumi.Output<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L76">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L80">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ScaleSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L13">class ScaleSet</a>
</h2>

Manage a virtual machine scale set.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L115">constructor</a>
</h3>

```typescript
new ScaleSet(name: string, args: ScaleSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ScaleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScaleSetState): ScaleSet
```


Get an existing ScaleSet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L29">property bootDiagnostics</a>
</h3>

```typescript
public bootDiagnostics: pulumi.Output<{ ... } | undefined>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L33">property extensions</a>
</h3>

```typescript
public extensions: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L34">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L38">property licenseType</a>
</h3>

```typescript
public licenseType: pulumi.Output<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L42">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L50">property networkProfiles</a>
</h3>

```typescript
public networkProfiles: pulumi.Output<{ ... }[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L54">property osProfile</a>
</h3>

```typescript
public osProfile: pulumi.Output<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L58">property osProfileLinuxConfig</a>
</h3>

```typescript
public osProfileLinuxConfig: pulumi.Output<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L62">property osProfileSecrets</a>
</h3>

```typescript
public osProfileSecrets: pulumi.Output<{ ... }[] | undefined>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L66">property osProfileWindowsConfig</a>
</h3>

```typescript
public osProfileWindowsConfig: pulumi.Output<{ ... } | undefined>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L70">property overprovision</a>
</h3>

```typescript
public overprovision: pulumi.Output<boolean | undefined>;
```


Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L74">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... } | undefined>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L78">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<string | undefined>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L82">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L87">property singlePlacementGroup</a>
</h3>

```typescript
public singlePlacementGroup: pulumi.Output<boolean | undefined>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L91">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L95">property storageProfileDataDisks</a>
</h3>

```typescript
public storageProfileDataDisks: pulumi.Output<{ ... }[] | undefined>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L99">property storageProfileImageReference</a>
</h3>

```typescript
public storageProfileImageReference: pulumi.Output<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L103">property storageProfileOsDisk</a>
</h3>

```typescript
public storageProfileOsDisk: pulumi.Output<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L107">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L111">property upgradePolicyMode</a>
</h3>

```typescript
public upgradePolicyMode: pulumi.Output<string>;
```


Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L115">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string[] | undefined>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="SharedImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L12">class SharedImage</a>
</h2>

Manages a Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L65">constructor</a>
</h3>

```typescript
new SharedImage(name: string, args: SharedImageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SharedImage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedImageState): SharedImage
```


Get an existing SharedImage resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L32">property eula</a>
</h3>

```typescript
public eula: pulumi.Output<string | undefined>;
```


The End User Licence Agreement for the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L36">property galleryName</a>
</h3>

```typescript
public galleryName: pulumi.Output<string>;
```


Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L37">property identifier</a>
</h3>

```typescript
public identifier: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Shared Image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L49">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string>;
```


The type of Operating System present in this Shared Image. Possible values are `Linux` and `Windows`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L53">property privacyStatementUri</a>
</h3>

```typescript
public privacyStatementUri: pulumi.Output<string | undefined>;
```


The URI containing the Privacy Statement associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L57">property releaseNoteUri</a>
</h3>

```typescript
public releaseNoteUri: pulumi.Output<string | undefined>;
```


The URI containing the Release Notes associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L61">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L65">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedImageGallery">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L12">class SharedImageGallery</a>
</h2>

Manages a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L45">constructor</a>
</h3>

```typescript
new SharedImageGallery(name: string, args: SharedImageGalleryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SharedImageGallery resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedImageGalleryState): SharedImageGallery
```


Get an existing SharedImageGallery resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L28">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L32">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L40">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L44">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L45">property uniqueName</a>
</h3>

```typescript
public uniqueName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedImageVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L12">class SharedImageVersion</a>
</h2>

Manages a Version of a Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L60">constructor</a>
</h3>

```typescript
new SharedImageVersion(name: string, args: SharedImageVersionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SharedImageVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SharedImageVersionState): SharedImageVersion
```


Get an existing SharedImageVersion resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L28">property excludeFromLatest</a>
</h3>

```typescript
public excludeFromLatest: pulumi.Output<boolean | undefined>;
```


Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L32">property galleryName</a>
</h3>

```typescript
public galleryName: pulumi.Output<string>;
```


The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L36">property imageName</a>
</h3>

```typescript
public imageName: pulumi.Output<string>;
```


The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L44">property managedImageId</a>
</h3>

```typescript
public managedImageId: pulumi.Output<string>;
```


The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L52">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L56">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A collection of tags which should be applied to this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L60">property targetRegions</a>
</h3>

```typescript
public targetRegions: pulumi.Output<{ ... }[]>;
```


One or more `target_region` blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Snapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L10">class Snapshot</a>
</h2>

Manages a Disk Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L56">constructor</a>
</h3>

```typescript
new Snapshot(name: string, args: SnapshotArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Snapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState): Snapshot
```


Get an existing Snapshot resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L26">property createOption</a>
</h3>

```typescript
public createOption: pulumi.Output<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L30">property diskSizeGb</a>
</h3>

```typescript
public diskSizeGb: pulumi.Output<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L31">property encryptionSettings</a>
</h3>

```typescript
public encryptionSettings: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L35">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L43">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L47">property sourceResourceId</a>
</h3>

```typescript
public sourceResourceId: pulumi.Output<string | undefined>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L51">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string | undefined>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L55">property storageAccountId</a>
</h3>

```typescript
public storageAccountId: pulumi.Output<string | undefined>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L56">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VirtualMachine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L12">class VirtualMachine</a>
</h2>

Manages a Virtual Machine.

~> **NOTE:** Data Disks can be attached either directly on the `azurerm_virtual_machine` resource, or using the `azurerm_virtual_machine_data_disk_attachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L112">constructor</a>
</h3>

```typescript
new VirtualMachine(name: string, args: VirtualMachineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualMachineState): VirtualMachine
```


Get an existing VirtualMachine resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L28">property availabilitySetId</a>
</h3>

```typescript
public availabilitySetId: pulumi.Output<string>;
```


The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L32">property bootDiagnostics</a>
</h3>

```typescript
public bootDiagnostics: pulumi.Output<{ ... } | undefined>;
```


A `boot_diagnostics` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L36">property deleteDataDisksOnTermination</a>
</h3>

```typescript
public deleteDataDisksOnTermination: pulumi.Output<boolean | undefined>;
```


Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L40">property deleteOsDiskOnTermination</a>
</h3>

```typescript
public deleteOsDiskOnTermination: pulumi.Output<boolean | undefined>;
```


Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L44">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```


A `identity` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L48">property licenseType</a>
</h3>

```typescript
public licenseType: pulumi.Output<string>;
```


Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L52">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L56">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L60">property networkInterfaceIds</a>
</h3>

```typescript
public networkInterfaceIds: pulumi.Output<string[]>;
```


A list of Network Interface ID's which should be associated with the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L64">property osProfile</a>
</h3>

```typescript
public osProfile: pulumi.Output<{ ... } | undefined>;
```


An `os_profile` block. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L68">property osProfileLinuxConfig</a>
</h3>

```typescript
public osProfileLinuxConfig: pulumi.Output<{ ... } | undefined>;
```


A `os_profile_linux_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L72">property osProfileSecrets</a>
</h3>

```typescript
public osProfileSecrets: pulumi.Output<{ ... }[] | undefined>;
```


One or more `os_profile_secrets` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L76">property osProfileWindowsConfig</a>
</h3>

```typescript
public osProfileWindowsConfig: pulumi.Output<{ ... } | undefined>;
```


A `os_profile_windows_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L80">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... } | undefined>;
```


A `plan` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L84">property primaryNetworkInterfaceId</a>
</h3>

```typescript
public primaryNetworkInterfaceId: pulumi.Output<string | undefined>;
```


The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L88">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L92">property storageDataDisks</a>
</h3>

```typescript
public storageDataDisks: pulumi.Output<{ ... }[]>;
```


One or more `storage_data_disk` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L96">property storageImageReference</a>
</h3>

```typescript
public storageImageReference: pulumi.Output<{ ... }>;
```


A `storage_image_reference` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L100">property storageOsDisk</a>
</h3>

```typescript
public storageOsDisk: pulumi.Output<{ ... }>;
```


A `storage_os_disk` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L104">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L108">property vmSize</a>
</h3>

```typescript
public vmSize: pulumi.Output<string>;
```


Specifies the [size of the Virtual Machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L112">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.

<h2 class="pdoc-module-header" id="getImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L10">function getImage</a>
</h2>

```typescript
getImage(args: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult>
```


Use this data source to access information about an existing Image.

<h2 class="pdoc-module-header" id="getManagedDisk">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L10">function getManagedDisk</a>
</h2>

```typescript
getManagedDisk(args: GetManagedDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetManagedDiskResult>
```


Use this data source to access information about an existing Managed Disk.

<h2 class="pdoc-module-header" id="getPlatformImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L10">function getPlatformImage</a>
</h2>

```typescript
getPlatformImage(args: GetPlatformImageArgs, opts?: pulumi.InvokeOptions): Promise<GetPlatformImageResult>
```


Use this data source to access information about a Platform Image.

<h2 class="pdoc-module-header" id="getSharedImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L12">function getSharedImage</a>
</h2>

```typescript
getSharedImage(args: GetSharedImageArgs, opts?: pulumi.InvokeOptions): Promise<GetSharedImageResult>
```


Use this data source to access information about an existing Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h2 class="pdoc-module-header" id="getSharedImageGallery">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L12">function getSharedImageGallery</a>
</h2>

```typescript
getSharedImageGallery(args: GetSharedImageGalleryArgs, opts?: pulumi.InvokeOptions): Promise<GetSharedImageGalleryResult>
```


Use this data source to access information about an existing Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h2 class="pdoc-module-header" id="getSharedImageVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L12">function getSharedImageVersion</a>
</h2>

```typescript
getSharedImageVersion(args: GetSharedImageVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetSharedImageVersionResult>
```


Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.

-> **NOTE** Shared Image Galleries are currently in Public Preview. You can find more information, including [how to register for the Public Preview here](https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/).

<h2 class="pdoc-module-header" id="getSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L10">function getSnapshot</a>
</h2>

```typescript
getSnapshot(args: GetSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetSnapshotResult>
```


Use this data source to access information about an existing Snapshot.

<h2 class="pdoc-module-header" id="AvailabilitySetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L128">interface AvailabilitySetArgs</a>
</h2>

The set of arguments for constructing a AvailabilitySet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L136">property managed</a>
</h3>

```typescript
managed?: pulumi.Input<boolean>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L144">property platformFaultDomainCount</a>
</h3>

```typescript
platformFaultDomainCount?: pulumi.Input<number>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L148">property platformUpdateDomainCount</a>
</h3>

```typescript
platformUpdateDomainCount?: pulumi.Input<number>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L152">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L156">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AvailabilitySetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L94">interface AvailabilitySetState</a>
</h2>

Input properties used for looking up and filtering AvailabilitySet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L98">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L102">property managed</a>
</h3>

```typescript
managed?: pulumi.Input<boolean>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L110">property platformFaultDomainCount</a>
</h3>

```typescript
platformFaultDomainCount?: pulumi.Input<number>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L114">property platformUpdateDomainCount</a>
</h3>

```typescript
platformUpdateDomainCount?: pulumi.Input<number>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L118">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DataDiskAttachmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L128">interface DataDiskAttachmentArgs</a>
</h2>

The set of arguments for constructing a DataDiskAttachment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L132">property caching</a>
</h3>

```typescript
caching: pulumi.Input<string>;
```


Specifies the caching requirements for this Data Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L136">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


The Create Option of the Data Disk, such as `Empty` or `Attach`. Defaults to `Attach`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L140">property lun</a>
</h3>

```typescript
lun: pulumi.Input<number>;
```


The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L144">property managedDiskId</a>
</h3>

```typescript
managedDiskId: pulumi.Input<string>;
```


The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L148">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId: pulumi.Input<string>;
```


The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L152">property writeAcceleratorEnabled</a>
</h3>

```typescript
writeAcceleratorEnabled?: pulumi.Input<boolean>;
```


Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.

<h2 class="pdoc-module-header" id="DataDiskAttachmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L98">interface DataDiskAttachmentState</a>
</h2>

Input properties used for looking up and filtering DataDiskAttachment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L102">property caching</a>
</h3>

```typescript
caching?: pulumi.Input<string>;
```


Specifies the caching requirements for this Data Disk. Possible values include `None`, `ReadOnly` and `ReadWrite`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L106">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


The Create Option of the Data Disk, such as `Empty` or `Attach`. Defaults to `Attach`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L110">property lun</a>
</h3>

```typescript
lun?: pulumi.Input<number>;
```


The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L114">property managedDiskId</a>
</h3>

```typescript
managedDiskId?: pulumi.Input<string>;
```


The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L118">property virtualMachineId</a>
</h3>

```typescript
virtualMachineId?: pulumi.Input<string>;
```


The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/dataDiskAttachment.ts#L122">property writeAcceleratorEnabled</a>
</h3>

```typescript
writeAcceleratorEnabled?: pulumi.Input<boolean>;
```


Specifies if Write Accelerator is enabled on the disk. This can only be enabled on `Premium_LRS` managed disks with no caching and [M-Series VMs](https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator). Defaults to `false`.

<h2 class="pdoc-module-header" id="ExtensionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L201">interface ExtensionArgs</a>
</h2>

The set of arguments for constructing a Extension resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L206">property autoUpgradeMinorVersion</a>
</h3>

```typescript
autoUpgradeMinorVersion?: pulumi.Input<boolean>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L211">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L221">property protectedSettings</a>
</h3>

```typescript
protectedSettings?: pulumi.Input<string>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L226">property publisher</a>
</h3>

```typescript
publisher: pulumi.Input<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L232">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L237">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<string>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L238">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L243">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L248">property typeHandlerVersion</a>
</h3>

```typescript
typeHandlerVersion: pulumi.Input<string>;
```


Specifies the version of the extension to
use, available versions can be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L253">property virtualMachineName</a>
</h3>

```typescript
virtualMachineName: pulumi.Input<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExtensionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L143">interface ExtensionState</a>
</h2>

Input properties used for looking up and filtering Extension resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L148">property autoUpgradeMinorVersion</a>
</h3>

```typescript
autoUpgradeMinorVersion?: pulumi.Input<boolean>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L153">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L163">property protectedSettings</a>
</h3>

```typescript
protectedSettings?: pulumi.Input<string>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L168">property publisher</a>
</h3>

```typescript
publisher?: pulumi.Input<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L174">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L179">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<string>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L180">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L185">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L190">property typeHandlerVersion</a>
</h3>

```typescript
typeHandlerVersion?: pulumi.Input<string>;
```


Specifies the version of the extension to
use, available versions can be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L195">property virtualMachineName</a>
</h3>

```typescript
virtualMachineName?: pulumi.Input<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L22">interface GetImageArgs</a>
</h2>

A collection of arguments for invoking getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L26">property name</a>
</h3>

```typescript
name?: string;
```


The name of the Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L30">property nameRegex</a>
</h3>

```typescript
nameRegex?: string;
```


Regex pattern of the image to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L34">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where this Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L38">property sortDescending</a>
</h3>

```typescript
sortDescending?: boolean;
```


By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.

<h2 class="pdoc-module-header" id="GetImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L44">interface GetImageResult</a>
</h2>

A collection of values returned by getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L48">property dataDisks</a>
</h3>

```typescript
dataDisks: { ... }[];
```


a collection of `data_disk` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L64">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L52">property location</a>
</h3>

```typescript
location: string;
```


the Azure Location where this Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L56">property osDisks</a>
</h3>

```typescript
osDisks: { ... }[];
```


a `os_disk` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L60">property tags</a>
</h3>

```typescript
tags: { ... };
```


a mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="GetManagedDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L22">interface GetManagedDiskArgs</a>
</h2>

A collection of arguments for invoking getManagedDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Managed Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L30">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L31">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L32">property zones</a>
</h3>

```typescript
zones?: string[];
```

<h2 class="pdoc-module-header" id="GetManagedDiskResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L38">interface GetManagedDiskResult</a>
</h2>

A collection of values returned by getManagedDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L42">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb: number;
```


The size of the managed disk in gigabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L70">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L46">property osType</a>
</h3>

```typescript
osType: string;
```


The operating system for managed disk. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L50">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId: string;
```


ID of an existing managed disk that the current resource was created from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L54">property sourceUri</a>
</h3>

```typescript
sourceUri: string;
```


The source URI for the managed disk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L58">property storageAccountType</a>
</h3>

```typescript
storageAccountType: string;
```


The storage account type for the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L62">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L66">property zones</a>
</h3>

```typescript
zones: string[];
```


(Optional) A collection containing the availability zone the managed disk is allocated in.

<h2 class="pdoc-module-header" id="GetPlatformImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L22">interface GetPlatformImageArgs</a>
</h2>

A collection of arguments for invoking getPlatformImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L26">property location</a>
</h3>

```typescript
location: string;
```


Specifies the Location to pull information about this Platform Image from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L30">property offer</a>
</h3>

```typescript
offer: string;
```


Specifies the Offer associated with the Platform Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L34">property publisher</a>
</h3>

```typescript
publisher: string;
```


Specifies the Publisher associated with the Platform Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L38">property sku</a>
</h3>

```typescript
sku: string;
```


Specifies the SKU of the Platform Image.

<h2 class="pdoc-module-header" id="GetPlatformImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L44">interface GetPlatformImageResult</a>
</h2>

A collection of values returned by getPlatformImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L52">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L48">property version</a>
</h3>

```typescript
version: string;
```


The latest version of the Platform Image.

<h2 class="pdoc-module-header" id="GetSharedImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L23">interface GetSharedImageArgs</a>
</h2>

A collection of arguments for invoking getSharedImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L27">property galleryName</a>
</h3>

```typescript
galleryName: string;
```


The name of the Shared Image Gallery in which the Shared Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L31">property name</a>
</h3>

```typescript
name: string;
```


The name of the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L35">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Shared Image Gallery exists.

<h2 class="pdoc-module-header" id="GetSharedImageGalleryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L22">interface GetSharedImageGalleryArgs</a>
</h2>

A collection of arguments for invoking getSharedImageGallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


The name of the Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L30">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Shared Image Gallery exists.

<h2 class="pdoc-module-header" id="GetSharedImageGalleryResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L36">interface GetSharedImageGalleryResult</a>
</h2>

A collection of values returned by getSharedImageGallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L40">property description</a>
</h3>

```typescript
description: string;
```


A description for the Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L53">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L41">property location</a>
</h3>

```typescript
location: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L45">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags which are assigned to the Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageGallery.ts#L49">property uniqueName</a>
</h3>

```typescript
uniqueName: string;
```


The unique name assigned to the Shared Image Gallery.

<h2 class="pdoc-module-header" id="GetSharedImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L41">interface GetSharedImageResult</a>
</h2>

A collection of values returned by getSharedImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L45">property description</a>
</h3>

```typescript
description: string;
```


The description of this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L49">property eula</a>
</h3>

```typescript
eula: string;
```


The End User Licence Agreement for the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L74">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L50">property identifiers</a>
</h3>

```typescript
identifiers: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L54">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the Shared Image Gallery exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L58">property osType</a>
</h3>

```typescript
osType: string;
```


The type of Operating System present in this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L62">property privacyStatementUri</a>
</h3>

```typescript
privacyStatementUri: string;
```


The URI containing the Privacy Statement for this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L66">property releaseNoteUri</a>
</h3>

```typescript
releaseNoteUri: string;
```


The URI containing the Release Notes for this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImage.ts#L70">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Shared Image.

<h2 class="pdoc-module-header" id="GetSharedImageVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L24">interface GetSharedImageVersionArgs</a>
</h2>

A collection of arguments for invoking getSharedImageVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L28">property galleryName</a>
</h3>

```typescript
galleryName: string;
```


The name of the Shared Image in which the Shared Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L32">property imageName</a>
</h3>

```typescript
imageName: string;
```


The name of the Shared Image in which this Version exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L36">property name</a>
</h3>

```typescript
name: string;
```


The name of the Image Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L40">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Shared Image Gallery exists.

<h2 class="pdoc-module-header" id="GetSharedImageVersionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L46">interface GetSharedImageVersionResult</a>
</h2>

A collection of values returned by getSharedImageVersion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L50">property excludeFromLatest</a>
</h3>

```typescript
excludeFromLatest: boolean;
```


Is this Image Version excluded from the `latest` filter?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L70">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L54">property location</a>
</h3>

```typescript
location: string;
```


The supported Azure location where the Shared Image Gallery exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L58">property managedImageId</a>
</h3>

```typescript
managedImageId: string;
```


The ID of the Managed Image which was the source of this Shared Image Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L62">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSharedImageVersion.ts#L66">property targetRegions</a>
</h3>

```typescript
targetRegions: { ... }[];
```


One or more `target_region` blocks as documented below.

<h2 class="pdoc-module-header" id="GetSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L20">interface GetSnapshotArgs</a>
</h2>

A collection of arguments for invoking getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Snapshot is located in.

<h2 class="pdoc-module-header" id="GetSnapshotResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L34">interface GetSnapshotResult</a>
</h2>

A collection of values returned by getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L35">property creationOption</a>
</h3>

```typescript
creationOption: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L39">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb: string;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L40">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L58">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L41">property osType</a>
</h3>

```typescript
osType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L45">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId: string;
```


The reference to an existing snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L49">property sourceUri</a>
</h3>

```typescript
sourceUri: string;
```


The URI to a Managed or Unmanaged Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L53">property storageAccountId</a>
</h3>

```typescript
storageAccountId: string;
```


The ID of an storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L54">property timeCreated</a>
</h3>

```typescript
timeCreated: string;
```

<h2 class="pdoc-module-header" id="ImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L134">interface ImageArgs</a>
</h2>

The set of arguments for constructing a Image resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L138">property dataDisks</a>
</h3>

```typescript
dataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L143">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L148">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L152">property osDisk</a>
</h3>

```typescript
osDisk?: pulumi.Input<{ ... }>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L157">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L161">property sourceVirtualMachineId</a>
</h3>

```typescript
sourceVirtualMachineId?: pulumi.Input<string>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L165">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ImageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L97">interface ImageState</a>
</h2>

Input properties used for looking up and filtering Image resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L101">property dataDisks</a>
</h3>

```typescript
dataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L106">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L115">property osDisk</a>
</h3>

```typescript
osDisk?: pulumi.Input<{ ... }>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L120">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L124">property sourceVirtualMachineId</a>
</h3>

```typescript
sourceVirtualMachineId?: pulumi.Input<string>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ManagedDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L206">interface ManagedDiskArgs</a>
</h2>

The set of arguments for constructing a ManagedDisk resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L210">property createOption</a>
</h3>

```typescript
createOption: pulumi.Input<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L215">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L219">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L223">property imageReferenceId</a>
</h3>

```typescript
imageReferenceId?: pulumi.Input<string>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L228">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L233">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L238">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L243">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L247">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L251">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L256">property storageAccountType</a>
</h3>

```typescript
storageAccountType: pulumi.Input<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L260">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L264">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ManagedDiskState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L142">interface ManagedDiskState</a>
</h2>

Input properties used for looking up and filtering ManagedDisk resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L146">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L151">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L155">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L159">property imageReferenceId</a>
</h3>

```typescript
imageReferenceId?: pulumi.Input<string>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L164">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L174">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L179">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L183">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L187">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L192">property storageAccountType</a>
</h3>

```typescript
storageAccountType?: pulumi.Input<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L196">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L200">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ScaleSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L302">interface ScaleSetArgs</a>
</h2>

The set of arguments for constructing a ScaleSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L306">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L310">property extensions</a>
</h3>

```typescript
extensions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L311">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L315">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L319">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L323">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L327">property networkProfiles</a>
</h3>

```typescript
networkProfiles: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L331">property osProfile</a>
</h3>

```typescript
osProfile: pulumi.Input<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L335">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L339">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L343">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L347">property overprovision</a>
</h3>

```typescript
overprovision?: pulumi.Input<boolean>;
```


Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L351">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L355">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<string>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L359">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L364">property singlePlacementGroup</a>
</h3>

```typescript
singlePlacementGroup?: pulumi.Input<boolean>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L368">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L372">property storageProfileDataDisks</a>
</h3>

```typescript
storageProfileDataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L376">property storageProfileImageReference</a>
</h3>

```typescript
storageProfileImageReference?: pulumi.Input<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L380">property storageProfileOsDisk</a>
</h3>

```typescript
storageProfileOsDisk: pulumi.Input<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L384">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L388">property upgradePolicyMode</a>
</h3>

```typescript
upgradePolicyMode: pulumi.Input<string>;
```


Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L392">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="ScaleSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L206">interface ScaleSetState</a>
</h2>

Input properties used for looking up and filtering ScaleSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L210">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L214">property extensions</a>
</h3>

```typescript
extensions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L215">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L219">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L223">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L227">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L231">property networkProfiles</a>
</h3>

```typescript
networkProfiles?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L235">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L239">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L243">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L247">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L251">property overprovision</a>
</h3>

```typescript
overprovision?: pulumi.Input<boolean>;
```


Specifies whether the virtual machine scale set should be overprovisioned. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L255">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L259">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<string>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L263">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L268">property singlePlacementGroup</a>
</h3>

```typescript
singlePlacementGroup?: pulumi.Input<boolean>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Defaults to `true`. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L272">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L276">property storageProfileDataDisks</a>
</h3>

```typescript
storageProfileDataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L280">property storageProfileImageReference</a>
</h3>

```typescript
storageProfileImageReference?: pulumi.Input<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L284">property storageProfileOsDisk</a>
</h3>

```typescript
storageProfileOsDisk?: pulumi.Input<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L288">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L292">property upgradePolicyMode</a>
</h3>

```typescript
upgradePolicyMode?: pulumi.Input<string>;
```


Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L296">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="SharedImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L173">interface SharedImageArgs</a>
</h2>

The set of arguments for constructing a SharedImage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L177">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L181">property eula</a>
</h3>

```typescript
eula?: pulumi.Input<string>;
```


The End User Licence Agreement for the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L185">property galleryName</a>
</h3>

```typescript
galleryName: pulumi.Input<string>;
```


Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L186">property identifier</a>
</h3>

```typescript
identifier: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L190">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Shared Image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L198">property osType</a>
</h3>

```typescript
osType: pulumi.Input<string>;
```


The type of Operating System present in this Shared Image. Possible values are `Linux` and `Windows`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L202">property privacyStatementUri</a>
</h3>

```typescript
privacyStatementUri?: pulumi.Input<string>;
```


The URI containing the Privacy Statement associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L206">property releaseNoteUri</a>
</h3>

```typescript
releaseNoteUri?: pulumi.Input<string>;
```


The URI containing the Release Notes associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L210">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L214">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Shared Image.

<h2 class="pdoc-module-header" id="SharedImageGalleryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L114">interface SharedImageGalleryArgs</a>
</h2>

The set of arguments for constructing a SharedImageGallery resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L118">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L122">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Shared Image Gallery.

<h2 class="pdoc-module-header" id="SharedImageGalleryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L87">interface SharedImageGalleryState</a>
</h2>

Input properties used for looking up and filtering SharedImageGallery resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L91">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L95">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L107">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Shared Image Gallery.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageGallery.ts#L108">property uniqueName</a>
</h3>

```typescript
uniqueName?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="SharedImageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L126">interface SharedImageState</a>
</h2>

Input properties used for looking up and filtering SharedImage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L130">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L134">property eula</a>
</h3>

```typescript
eula?: pulumi.Input<string>;
```


The End User Licence Agreement for the Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L138">property galleryName</a>
</h3>

```typescript
galleryName?: pulumi.Input<string>;
```


Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L139">property identifier</a>
</h3>

```typescript
identifier?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L143">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Shared Image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L151">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The type of Operating System present in this Shared Image. Possible values are `Linux` and `Windows`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L155">property privacyStatementUri</a>
</h3>

```typescript
privacyStatementUri?: pulumi.Input<string>;
```


The URI containing the Privacy Statement associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L159">property releaseNoteUri</a>
</h3>

```typescript
releaseNoteUri?: pulumi.Input<string>;
```


The URI containing the Release Notes associated with this Shared Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L163">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImage.ts#L167">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Shared Image.

<h2 class="pdoc-module-header" id="SharedImageVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L162">interface SharedImageVersionArgs</a>
</h2>

The set of arguments for constructing a SharedImageVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L166">property excludeFromLatest</a>
</h3>

```typescript
excludeFromLatest?: pulumi.Input<boolean>;
```


Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L170">property galleryName</a>
</h3>

```typescript
galleryName: pulumi.Input<string>;
```


The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L174">property imageName</a>
</h3>

```typescript
imageName: pulumi.Input<string>;
```


The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L178">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L182">property managedImageId</a>
</h3>

```typescript
managedImageId: pulumi.Input<string>;
```


The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L186">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L190">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L194">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A collection of tags which should be applied to this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L198">property targetRegions</a>
</h3>

```typescript
targetRegions: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `target_region` blocks as documented below.

<h2 class="pdoc-module-header" id="SharedImageVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L120">interface SharedImageVersionState</a>
</h2>

Input properties used for looking up and filtering SharedImageVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L124">property excludeFromLatest</a>
</h3>

```typescript
excludeFromLatest?: pulumi.Input<boolean>;
```


Should this Image Version be excluded from the `latest` filter? If set to `true` this Image Version won't be returned for the `latest` version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L128">property galleryName</a>
</h3>

```typescript
galleryName?: pulumi.Input<string>;
```


The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L132">property imageName</a>
</h3>

```typescript
imageName?: pulumi.Input<string>;
```


The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L136">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L140">property managedImageId</a>
</h3>

```typescript
managedImageId?: pulumi.Input<string>;
```


The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The version number for this Image Version, such as `1.0.0`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L148">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L152">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A collection of tags which should be applied to this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/sharedImageVersion.ts#L156">property targetRegions</a>
</h3>

```typescript
targetRegions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `target_region` blocks as documented below.

<h2 class="pdoc-module-header" id="SnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L149">interface SnapshotArgs</a>
</h2>

The set of arguments for constructing a Snapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L153">property createOption</a>
</h3>

```typescript
createOption: pulumi.Input<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L157">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L158">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L162">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L166">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L170">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L174">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L178">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L182">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L183">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="SnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L109">interface SnapshotState</a>
</h2>

Input properties used for looking up and filtering Snapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L113">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L117">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L118">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L122">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L134">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L138">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L142">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L143">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="VirtualMachineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L289">interface VirtualMachineArgs</a>
</h2>

The set of arguments for constructing a VirtualMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L293">property availabilitySetId</a>
</h3>

```typescript
availabilitySetId?: pulumi.Input<string>;
```


The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L297">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A `boot_diagnostics` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L301">property deleteDataDisksOnTermination</a>
</h3>

```typescript
deleteDataDisksOnTermination?: pulumi.Input<boolean>;
```


Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L305">property deleteOsDiskOnTermination</a>
</h3>

```typescript
deleteOsDiskOnTermination?: pulumi.Input<boolean>;
```


Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L309">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A `identity` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L313">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L317">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L321">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L325">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Network Interface ID's which should be associated with the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L329">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


An `os_profile` block. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L333">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A `os_profile_linux_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L337">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `os_profile_secrets` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L341">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A `os_profile_windows_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L345">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A `plan` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L349">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```


The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L353">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L357">property storageDataDisks</a>
</h3>

```typescript
storageDataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `storage_data_disk` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L361">property storageImageReference</a>
</h3>

```typescript
storageImageReference?: pulumi.Input<{ ... }>;
```


A `storage_image_reference` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L365">property storageOsDisk</a>
</h3>

```typescript
storageOsDisk: pulumi.Input<{ ... }>;
```


A `storage_os_disk` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L369">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L373">property vmSize</a>
</h3>

```typescript
vmSize: pulumi.Input<string>;
```


Specifies the [size of the Virtual Machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L377">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.

<h2 class="pdoc-module-header" id="VirtualMachineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L195">interface VirtualMachineState</a>
</h2>

Input properties used for looking up and filtering VirtualMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L199">property availabilitySetId</a>
</h3>

```typescript
availabilitySetId?: pulumi.Input<string>;
```


The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L203">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A `boot_diagnostics` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L207">property deleteDataDisksOnTermination</a>
</h3>

```typescript
deleteDataDisksOnTermination?: pulumi.Input<boolean>;
```


Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L211">property deleteOsDiskOnTermination</a>
</h3>

```typescript
deleteOsDiskOnTermination?: pulumi.Input<boolean>;
```


Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L215">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A `identity` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L219">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L223">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L227">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L231">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Network Interface ID's which should be associated with the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L235">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


An `os_profile` block. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L239">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A `os_profile_linux_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L243">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `os_profile_secrets` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L247">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A `os_profile_windows_config` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L251">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A `plan` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L255">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```


The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L259">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L263">property storageDataDisks</a>
</h3>

```typescript
storageDataDisks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `storage_data_disk` blocks.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L267">property storageImageReference</a>
</h3>

```typescript
storageImageReference?: pulumi.Input<{ ... }>;
```


A `storage_image_reference` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L271">property storageOsDisk</a>
</h3>

```typescript
storageOsDisk?: pulumi.Input<{ ... }>;
```


A `storage_os_disk` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L275">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L279">property vmSize</a>
</h3>

```typescript
vmSize?: pulumi.Input<string>;
```


Specifies the [size of the Virtual Machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L283">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<string>;
```


A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.

