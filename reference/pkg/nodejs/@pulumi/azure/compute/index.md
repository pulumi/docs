---
title: Module compute
---

<a href="../index.html">@pulumi/azure</a> &gt; compute

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AvailabilitySet">class AvailabilitySet</a>
* <a href="#Extension">class Extension</a>
* <a href="#Image">class Image</a>
* <a href="#ManagedDisk">class ManagedDisk</a>
* <a href="#ScaleSet">class ScaleSet</a>
* <a href="#Snapshot">class Snapshot</a>
* <a href="#VirtualMachine">class VirtualMachine</a>
* <a href="#getImage">function getImage</a>
* <a href="#getManagedDisk">function getManagedDisk</a>
* <a href="#getPlatformImage">function getPlatformImage</a>
* <a href="#getSnapshot">function getSnapshot</a>
* <a href="#AvailabilitySetArgs">interface AvailabilitySetArgs</a>
* <a href="#AvailabilitySetState">interface AvailabilitySetState</a>
* <a href="#ExtensionArgs">interface ExtensionArgs</a>
* <a href="#ExtensionState">interface ExtensionState</a>
* <a href="#GetImageArgs">interface GetImageArgs</a>
* <a href="#GetImageResult">interface GetImageResult</a>
* <a href="#GetManagedDiskArgs">interface GetManagedDiskArgs</a>
* <a href="#GetManagedDiskResult">interface GetManagedDiskResult</a>
* <a href="#GetPlatformImageArgs">interface GetPlatformImageArgs</a>
* <a href="#GetPlatformImageResult">interface GetPlatformImageResult</a>
* <a href="#GetSnapshotArgs">interface GetSnapshotArgs</a>
* <a href="#GetSnapshotResult">interface GetSnapshotResult</a>
* <a href="#ImageArgs">interface ImageArgs</a>
* <a href="#ImageState">interface ImageState</a>
* <a href="#ManagedDiskArgs">interface ManagedDiskArgs</a>
* <a href="#ManagedDiskState">interface ManagedDiskState</a>
* <a href="#ScaleSetArgs">interface ScaleSetArgs</a>
* <a href="#ScaleSetState">interface ScaleSetState</a>
* <a href="#SnapshotArgs">interface SnapshotArgs</a>
* <a href="#SnapshotState">interface SnapshotState</a>
* <a href="#VirtualMachineArgs">interface VirtualMachineArgs</a>
* <a href="#VirtualMachineState">interface VirtualMachineState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts">compute/availabilitySet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts">compute/extension.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts">compute/getImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts">compute/getManagedDisk.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts">compute/getPlatformImage.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts">compute/getSnapshot.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts">compute/image.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts">compute/managedDisk.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts">compute/scaleSet.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts">compute/snapshot.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts">compute/virtualMachine.ts</a> 


<h2 class="pdoc-module-header" id="AvailabilitySet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L9">class AvailabilitySet</a>
</h2>

Manages an availability set for virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L49">constructor</a>
</h3>

```typescript
new AvailabilitySet(name: string, args: AvailabilitySetArgs, opts?: pulumi.ResourceOptions)
```


Create a AvailabilitySet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AvailabilitySetState): AvailabilitySet
```


Get an existing AvailabilitySet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L29">property managed</a>
</h3>

```typescript
public managed: pulumi.Output<boolean | undefined>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L37">property platformFaultDomainCount</a>
</h3>

```typescript
public platformFaultDomainCount: pulumi.Output<number | undefined>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L41">property platformUpdateDomainCount</a>
</h3>

```typescript
public platformUpdateDomainCount: pulumi.Output<number | undefined>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L49">property tags</a>
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

<h2 class="pdoc-module-header" id="Extension">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L12">class Extension</a>
</h2>

Manages a new Virtual Machine Extension to provide post deployment configuration
and run automated tasks.

~> **Please Note:** The CustomScript extensions for Linux & Windows require that the `commandToExecute` returns a `0` exit code to be classified as successfully deployed. You can achieve this by appending `exit 0` to the end of your `commandToExecute`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L76">constructor</a>
</h3>

```typescript
new Extension(name: string, args: ExtensionArgs, opts?: pulumi.ResourceOptions)
```


Create a Extension resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ExtensionState): Extension
```


Get an existing Extension resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L29">property autoUpgradeMinorVersion</a>
</h3>

```typescript
public autoUpgradeMinorVersion: pulumi.Output<boolean | undefined>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L34">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L44">property protectedSettings</a>
</h3>

```typescript
public protectedSettings: pulumi.Output<string | undefined>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L49">property publisher</a>
</h3>

```typescript
public publisher: pulumi.Output<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L55">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L60">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<string | undefined>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L61">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L66">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L71">property typeHandlerVersion</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L76">property virtualMachineName</a>
</h3>

```typescript
public virtualMachineName: pulumi.Output<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="Image">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L9">class Image</a>
</h2>

Create a custom virtual machine image that can be used to create virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L52">constructor</a>
</h3>

```typescript
new Image(name: string, args: ImageArgs, opts?: pulumi.ResourceOptions)
```


Create a Image resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageState): Image
```


Get an existing Image resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L25">property dataDisks</a>
</h3>

```typescript
public dataDisks: pulumi.Output<{ ... }[] | undefined>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L39">property osDisk</a>
</h3>

```typescript
public osDisk: pulumi.Output<{ ... } | undefined>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L44">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L48">property sourceVirtualMachineId</a>
</h3>

```typescript
public sourceVirtualMachineId: pulumi.Output<string | undefined>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L52">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L9">class ManagedDisk</a>
</h2>

Create a managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L79">constructor</a>
</h3>

```typescript
new ManagedDisk(name: string, args: ManagedDiskArgs, opts?: pulumi.ResourceOptions)
```


Create a ManagedDisk resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagedDiskState): ManagedDisk
```


Get an existing ManagedDisk resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L25">property createOption</a>
</h3>

```typescript
public createOption: pulumi.Output<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L30">property diskSizeGb</a>
</h3>

```typescript
public diskSizeGb: pulumi.Output<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L34">property encryptionSettings</a>
</h3>

```typescript
public encryptionSettings: pulumi.Output<{ ... } | undefined>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L38">property imageReferenceId</a>
</h3>

```typescript
public imageReferenceId: pulumi.Output<string | undefined>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L43">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L53">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L62">property sourceResourceId</a>
</h3>

```typescript
public sourceResourceId: pulumi.Output<string | undefined>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L66">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L71">property storageAccountType</a>
</h3>

```typescript
public storageAccountType: pulumi.Output<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L75">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L79">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ScaleSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L12">class ScaleSet</a>
</h2>

Create a virtual machine scale set.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L114">constructor</a>
</h3>

```typescript
new ScaleSet(name: string, args: ScaleSetArgs, opts?: pulumi.ResourceOptions)
```


Create a ScaleSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScaleSetState): ScaleSet
```


Get an existing ScaleSet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L28">property bootDiagnostics</a>
</h3>

```typescript
public bootDiagnostics: pulumi.Output<{ ... } | undefined>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L32">property extensions</a>
</h3>

```typescript
public extensions: pulumi.Output<{ ... }[] | undefined>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L33">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L37">property licenseType</a>
</h3>

```typescript
public licenseType: pulumi.Output<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L49">property networkProfiles</a>
</h3>

```typescript
public networkProfiles: pulumi.Output<{ ... }[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L53">property osProfile</a>
</h3>

```typescript
public osProfile: pulumi.Output<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L57">property osProfileLinuxConfig</a>
</h3>

```typescript
public osProfileLinuxConfig: pulumi.Output<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L61">property osProfileSecrets</a>
</h3>

```typescript
public osProfileSecrets: pulumi.Output<{ ... }[] | undefined>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L65">property osProfileWindowsConfig</a>
</h3>

```typescript
public osProfileWindowsConfig: pulumi.Output<{ ... } | undefined>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L69">property overprovision</a>
</h3>

```typescript
public overprovision: pulumi.Output<boolean | undefined>;
```


Specifies whether the virtual machine scale set should be overprovisioned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L73">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... } | undefined>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L77">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<string | undefined>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L81">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L86">property singlePlacementGroup</a>
</h3>

```typescript
public singlePlacementGroup: pulumi.Output<boolean | undefined>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L90">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L94">property storageProfileDataDisks</a>
</h3>

```typescript
public storageProfileDataDisks: pulumi.Output<{ ... }[] | undefined>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L98">property storageProfileImageReference</a>
</h3>

```typescript
public storageProfileImageReference: pulumi.Output<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L102">property storageProfileOsDisk</a>
</h3>

```typescript
public storageProfileOsDisk: pulumi.Output<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L106">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L110">property upgradePolicyMode</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L114">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string[] | undefined>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="Snapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L9">class Snapshot</a>
</h2>

Manages a Disk Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L55">constructor</a>
</h3>

```typescript
new Snapshot(name: string, args: SnapshotArgs, opts?: pulumi.ResourceOptions)
```


Create a Snapshot resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SnapshotState): Snapshot
```


Get an existing Snapshot resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L25">property createOption</a>
</h3>

```typescript
public createOption: pulumi.Output<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L29">property diskSizeGb</a>
</h3>

```typescript
public diskSizeGb: pulumi.Output<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L30">property encryptionSettings</a>
</h3>

```typescript
public encryptionSettings: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L34">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L46">property sourceResourceId</a>
</h3>

```typescript
public sourceResourceId: pulumi.Output<string | undefined>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L50">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string | undefined>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L54">property storageAccountId</a>
</h3>

```typescript
public storageAccountId: pulumi.Output<string | undefined>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L55">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L9">class VirtualMachine</a>
</h2>

Create a virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L110">constructor</a>
</h3>

```typescript
new VirtualMachine(name: string, args: VirtualMachineArgs, opts?: pulumi.ResourceOptions)
```


Create a VirtualMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualMachineState): VirtualMachine
```


Get an existing VirtualMachine resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L25">property availabilitySetId</a>
</h3>

```typescript
public availabilitySetId: pulumi.Output<string>;
```


The Id of the Availability Set in which to create the virtual machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L29">property bootDiagnostics</a>
</h3>

```typescript
public bootDiagnostics: pulumi.Output<{ ... } | undefined>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L33">property deleteDataDisksOnTermination</a>
</h3>

```typescript
public deleteDataDisksOnTermination: pulumi.Output<boolean | undefined>;
```


Flag to enable deletion of storage data disk VHD blobs or managed disks when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L37">property deleteOsDiskOnTermination</a>
</h3>

```typescript
public deleteOsDiskOnTermination: pulumi.Output<boolean | undefined>;
```


Flag to enable deletion of the OS disk VHD blob or managed disk when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L41">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```


An identity block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L45">property licenseType</a>
</h3>

```typescript
public licenseType: pulumi.Output<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L49">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the data disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L57">property networkInterfaceIds</a>
</h3>

```typescript
public networkInterfaceIds: pulumi.Output<string[]>;
```


Specifies the list of resource IDs for the network interfaces associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L61">property osProfile</a>
</h3>

```typescript
public osProfile: pulumi.Output<{ ... } | undefined>;
```


An OS Profile block as documented below. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L65">property osProfileLinuxConfig</a>
</h3>

```typescript
public osProfileLinuxConfig: pulumi.Output<{ ... } | undefined>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L69">property osProfileSecrets</a>
</h3>

```typescript
public osProfileSecrets: pulumi.Output<{ ... }[] | undefined>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L73">property osProfileWindowsConfig</a>
</h3>

```typescript
public osProfileWindowsConfig: pulumi.Output<{ ... } | undefined>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L77">property plan</a>
</h3>

```typescript
public plan: pulumi.Output<{ ... } | undefined>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L81">property primaryNetworkInterfaceId</a>
</h3>

```typescript
public primaryNetworkInterfaceId: pulumi.Output<string | undefined>;
```


Specifies the resource ID for the primary network interface associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L86">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L90">property storageDataDisks</a>
</h3>

```typescript
public storageDataDisks: pulumi.Output<{ ... }[] | undefined>;
```


A list of Storage Data disk blocks as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L94">property storageImageReference</a>
</h3>

```typescript
public storageImageReference: pulumi.Output<{ ... }>;
```


A Storage Image Reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L98">property storageOsDisk</a>
</h3>

```typescript
public storageOsDisk: pulumi.Output<{ ... }>;
```


A Storage OS Disk block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L102">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L106">property vmSize</a>
</h3>

```typescript
public vmSize: pulumi.Output<string>;
```


Specifies the [size of the virtual machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L110">property zones</a>
</h3>

```typescript
public zones: pulumi.Output<string | undefined>;
```


A collection containing the availability zone to allocate the Virtual Machine in.

<h2 class="pdoc-module-header" id="getImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L9">function getImage</a>
</h2>

```typescript
getImage(args: GetImageArgs): Promise<GetImageResult>
```


Use this data source to access information about an Image.

<h2 class="pdoc-module-header" id="getManagedDisk">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L9">function getManagedDisk</a>
</h2>

```typescript
getManagedDisk(args: GetManagedDiskArgs): Promise<GetManagedDiskResult>
```


Use this data source to access the properties of an existing Azure Managed Disk.

<h2 class="pdoc-module-header" id="getPlatformImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L9">function getPlatformImage</a>
</h2>

```typescript
getPlatformImage(args: GetPlatformImageArgs): Promise<GetPlatformImageResult>
```


Use this data source to access the properties of an Azure Platform Image.

<h2 class="pdoc-module-header" id="getSnapshot">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L9">function getSnapshot</a>
</h2>

```typescript
getSnapshot(args: GetSnapshotArgs): Promise<GetSnapshotResult>
```


Use this data source to access the properties of a Snapshot of an Disk.

<h2 class="pdoc-module-header" id="AvailabilitySetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L127">interface AvailabilitySetArgs</a>
</h2>

The set of arguments for constructing a AvailabilitySet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L131">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L135">property managed</a>
</h3>

```typescript
managed?: pulumi.Input<boolean>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L143">property platformFaultDomainCount</a>
</h3>

```typescript
platformFaultDomainCount?: pulumi.Input<number>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L147">property platformUpdateDomainCount</a>
</h3>

```typescript
platformUpdateDomainCount?: pulumi.Input<number>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L151">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L155">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AvailabilitySetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L93">interface AvailabilitySetState</a>
</h2>

Input properties used for looking up and filtering AvailabilitySet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L97">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L101">property managed</a>
</h3>

```typescript
managed?: pulumi.Input<boolean>;
```


Specifies whether the availability set is managed or not. Possible values are `true` (to specify aligned) or `false` (to specify classic). Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L109">property platformFaultDomainCount</a>
</h3>

```typescript
platformFaultDomainCount?: pulumi.Input<number>;
```


Specifies the number of fault domains that are used. Defaults to 3.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L113">property platformUpdateDomainCount</a>
</h3>

```typescript
platformUpdateDomainCount?: pulumi.Input<number>;
```


Specifies the number of update domains that are used. Defaults to 5.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L117">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/availabilitySet.ts#L121">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ExtensionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L198">interface ExtensionArgs</a>
</h2>

The set of arguments for constructing a Extension resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L203">property autoUpgradeMinorVersion</a>
</h3>

```typescript
autoUpgradeMinorVersion?: pulumi.Input<boolean>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L208">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L213">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L218">property protectedSettings</a>
</h3>

```typescript
protectedSettings?: pulumi.Input<string>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L223">property publisher</a>
</h3>

```typescript
publisher: pulumi.Input<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L229">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L234">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<string>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L235">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L240">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L245">property typeHandlerVersion</a>
</h3>

```typescript
typeHandlerVersion: pulumi.Input<string>;
```


Specifies the version of the extension to
use, available versions can be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L250">property virtualMachineName</a>
</h3>

```typescript
virtualMachineName: pulumi.Input<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ExtensionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L140">interface ExtensionState</a>
</h2>

Input properties used for looking up and filtering Extension resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L145">property autoUpgradeMinorVersion</a>
</h3>

```typescript
autoUpgradeMinorVersion?: pulumi.Input<boolean>;
```


Specifies if the platform deploys
the latest minor version update to the `type_handler_version` specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L150">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The location where the extension is created. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the virtual machine extension peering. Changing
this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L160">property protectedSettings</a>
</h3>

```typescript
protectedSettings?: pulumi.Input<string>;
```


The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L165">property publisher</a>
</h3>

```typescript
publisher?: pulumi.Input<string>;
```


The publisher of the extension, available publishers
can be found by using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L171">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L176">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<string>;
```


The settings passed to the extension, these are
specified as a JSON object in a string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L177">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L182">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of extension, available types for a publisher can
be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L187">property typeHandlerVersion</a>
</h3>

```typescript
typeHandlerVersion?: pulumi.Input<string>;
```


Specifies the version of the extension to
use, available versions can be found using the Azure CLI.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/extension.ts#L192">property virtualMachineName</a>
</h3>

```typescript
virtualMachineName?: pulumi.Input<string>;
```


The name of the virtual machine. Changing
this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L21">interface GetImageArgs</a>
</h2>

A collection of arguments for invoking getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L25">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L29">property nameRegex</a>
</h3>

```typescript
nameRegex?: pulumi.Input<string>;
```


Regex pattern of the image to match.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L33">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The Name of the Resource Group where this Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L37">property sortDescending</a>
</h3>

```typescript
sortDescending?: pulumi.Input<boolean>;
```


By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.

<h2 class="pdoc-module-header" id="GetImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L43">interface GetImageResult</a>
</h2>

A collection of values returned by getImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L47">property dataDisks</a>
</h3>

```typescript
dataDisks: { ... }[];
```


a collection of `data_disk` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L51">property location</a>
</h3>

```typescript
location: string;
```


the Azure Location where this Image exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L55">property osDisks</a>
</h3>

```typescript
osDisks: { ... }[];
```


a `os_disk` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getImage.ts#L59">property tags</a>
</h3>

```typescript
tags: { ... };
```


a mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="GetManagedDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L21">interface GetManagedDiskArgs</a>
</h2>

A collection of arguments for invoking getManagedDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L25">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Specifies the name of the Managed Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L29">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the resource group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L30">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L31">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```

<h2 class="pdoc-module-header" id="GetManagedDiskResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L37">interface GetManagedDiskResult</a>
</h2>

A collection of values returned by getManagedDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L41">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb: number;
```


The size of the managed disk in gigabytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L45">property osType</a>
</h3>

```typescript
osType: string;
```


The operating system for managed disk. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L49">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId: string;
```


ID of an existing managed disk that the current resource was created from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L53">property sourceUri</a>
</h3>

```typescript
sourceUri: string;
```


The source URI for the managed disk

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L57">property storageAccountType</a>
</h3>

```typescript
storageAccountType: string;
```


The storage account type for the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L61">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getManagedDisk.ts#L65">property zones</a>
</h3>

```typescript
zones: string[];
```


(Optional) A collection containing the availability zone the managed disk is allocated in.

<h2 class="pdoc-module-header" id="GetPlatformImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L21">interface GetPlatformImageArgs</a>
</h2>

A collection of arguments for invoking getPlatformImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L25">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the Location to pull information about this Platform Image from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L29">property offer</a>
</h3>

```typescript
offer: pulumi.Input<string>;
```


Specifies the Offer associated with the Platform Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L33">property publisher</a>
</h3>

```typescript
publisher: pulumi.Input<string>;
```


Specifies the Publisher associated with the Platform Image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L37">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Specifies the SKU of the Platform Image.

<h2 class="pdoc-module-header" id="GetPlatformImageResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L43">interface GetPlatformImageResult</a>
</h2>

A collection of values returned by getPlatformImage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getPlatformImage.ts#L47">property version</a>
</h3>

```typescript
version: string;
```


The latest version of the Platform Image.

<h2 class="pdoc-module-header" id="GetSnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L19">interface GetSnapshotArgs</a>
</h2>

A collection of arguments for invoking getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Specifies the name of the Snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the resource group the Snapshot is located in.

<h2 class="pdoc-module-header" id="GetSnapshotResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L33">interface GetSnapshotResult</a>
</h2>

A collection of values returned by getSnapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L34">property creationOption</a>
</h3>

```typescript
creationOption: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L38">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb: string;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L39">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L40">property osType</a>
</h3>

```typescript
osType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L44">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId: string;
```


The reference to an existing snapshot.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L48">property sourceUri</a>
</h3>

```typescript
sourceUri: string;
```


The URI to a Managed or Unmanaged Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L52">property storageAccountId</a>
</h3>

```typescript
storageAccountId: string;
```


The ID of an storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/getSnapshot.ts#L53">property timeCreated</a>
</h3>

```typescript
timeCreated: string;
```

<h2 class="pdoc-module-header" id="ImageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L133">interface ImageArgs</a>
</h2>

The set of arguments for constructing a Image resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L137">property dataDisks</a>
</h3>

```typescript
dataDisks?: pulumi.Input<{ ... }[]>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L142">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L151">property osDisk</a>
</h3>

```typescript
osDisk?: pulumi.Input<{ ... }>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L156">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L160">property sourceVirtualMachineId</a>
</h3>

```typescript
sourceVirtualMachineId?: pulumi.Input<string>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L164">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ImageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L96">interface ImageState</a>
</h2>

Input properties used for looking up and filtering Image resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L100">property dataDisks</a>
</h3>

```typescript
dataDisks?: pulumi.Input<{ ... }[]>;
```


One or more `data_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L105">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L114">property osDisk</a>
</h3>

```typescript
osDisk?: pulumi.Input<{ ... }>;
```


One or more `os_disk` elements as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L119">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create
the image. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L123">property sourceVirtualMachineId</a>
</h3>

```typescript
sourceVirtualMachineId?: pulumi.Input<string>;
```


The Virtual Machine ID from which to create the image.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/image.ts#L127">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ManagedDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L205">interface ManagedDiskArgs</a>
</h2>

The set of arguments for constructing a ManagedDisk resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L209">property createOption</a>
</h3>

```typescript
createOption: pulumi.Input<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L214">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L218">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L222">property imageReferenceId</a>
</h3>

```typescript
imageReferenceId?: pulumi.Input<string>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L227">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L237">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L242">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L246">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L250">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L255">property storageAccountType</a>
</h3>

```typescript
storageAccountType: pulumi.Input<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L259">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L263">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ManagedDiskState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L141">interface ManagedDiskState</a>
</h2>

Input properties used for looking up and filtering ManagedDisk resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L145">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


The method to use when creating the managed disk. Possible values include:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L150">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


Specifies the size of the managed disk to create in gigabytes.
If `create_option` is `Copy` or `FromImage`, then the value must be equal to or greater than the source's size.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L154">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```


an `encryption_settings` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L158">property imageReferenceId</a>
</h3>

```typescript
imageReferenceId?: pulumi.Input<string>;
```


ID of an existing platform/marketplace disk image to copy when `create_option` is `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L163">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the managed disk. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L173">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


Specify a value when the source of an `Import` or `Copy`
operation targets a source that contains an operating system. Valid values are `Linux` or `Windows`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L178">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create
the managed disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L182">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


ID of an existing managed disk to copy when `create_option` is `Copy`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L186">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


URI to a valid VHD file to be used when `create_option` is `Import`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L191">property storageAccountType</a>
</h3>

```typescript
storageAccountType?: pulumi.Input<string>;
```


The type of storage to use for the managed disk.
Allowable values are `Standard_LRS` or `Premium_LRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L195">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/managedDisk.ts#L199">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>>;
```


A collection containing the availability zone to allocate the Managed Disk in.

<h2 class="pdoc-module-header" id="ScaleSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L301">interface ScaleSetArgs</a>
</h2>

The set of arguments for constructing a ScaleSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L305">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L309">property extensions</a>
</h3>

```typescript
extensions?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L310">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L314">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L318">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L322">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L326">property networkProfiles</a>
</h3>

```typescript
networkProfiles: pulumi.Input<{ ... }[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L330">property osProfile</a>
</h3>

```typescript
osProfile: pulumi.Input<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L334">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L338">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<{ ... }[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L342">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L346">property overprovision</a>
</h3>

```typescript
overprovision?: pulumi.Input<boolean>;
```


Specifies whether the virtual machine scale set should be overprovisioned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L350">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L354">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<string>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L358">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L363">property singlePlacementGroup</a>
</h3>

```typescript
singlePlacementGroup?: pulumi.Input<boolean>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L367">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L371">property storageProfileDataDisks</a>
</h3>

```typescript
storageProfileDataDisks?: pulumi.Input<{ ... }[]>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L375">property storageProfileImageReference</a>
</h3>

```typescript
storageProfileImageReference?: pulumi.Input<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L379">property storageProfileOsDisk</a>
</h3>

```typescript
storageProfileOsDisk: pulumi.Input<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L383">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L387">property upgradePolicyMode</a>
</h3>

```typescript
upgradePolicyMode: pulumi.Input<string>;
```


Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L391">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="ScaleSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L205">interface ScaleSetState</a>
</h2>

Input properties used for looking up and filtering ScaleSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L209">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L213">property extensions</a>
</h3>

```typescript
extensions?: pulumi.Input<{ ... }[]>;
```


Can be specified multiple times to add extension profiles to the scale set. Each `extension` block supports the fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L214">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L218">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L222">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L226">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the image from the marketplace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L230">property networkProfiles</a>
</h3>

```typescript
networkProfiles?: pulumi.Input<{ ... }[]>;
```


A collection of network profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L234">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


A Virtual Machine OS Profile block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L238">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L242">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<{ ... }[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L246">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L250">property overprovision</a>
</h3>

```typescript
overprovision?: pulumi.Input<boolean>;
```


Specifies whether the virtual machine scale set should be overprovisioned.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L254">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L258">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<string>;
```


Specifies the priority for the virtual machines in the scale set, defaults to `Regular`. Possible values are `Low` and `Regular`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L262">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L267">property singlePlacementGroup</a>
</h3>

```typescript
singlePlacementGroup?: pulumi.Input<boolean>;
```


Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a
new resource to be created. See [documentation](http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L271">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


Specifies the SKU of the image used to create the virtual machines.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L275">property storageProfileDataDisks</a>
</h3>

```typescript
storageProfileDataDisks?: pulumi.Input<{ ... }[]>;
```


A storage profile data disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L279">property storageProfileImageReference</a>
</h3>

```typescript
storageProfileImageReference?: pulumi.Input<{ ... }>;
```


A storage profile image reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L283">property storageProfileOsDisk</a>
</h3>

```typescript
storageProfileOsDisk?: pulumi.Input<{ ... }>;
```


A storage profile os disk block as documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L287">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L291">property upgradePolicyMode</a>
</h3>

```typescript
upgradePolicyMode?: pulumi.Input<string>;
```


Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, `Manual` or `Automatic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/scaleSet.ts#L295">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>[]>;
```


A collection of availability zones to spread the Virtual Machines over.

<h2 class="pdoc-module-header" id="SnapshotArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L148">interface SnapshotArgs</a>
</h2>

The set of arguments for constructing a Snapshot resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L152">property createOption</a>
</h3>

```typescript
createOption: pulumi.Input<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L156">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L157">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L161">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L165">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L169">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L173">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L177">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L181">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L182">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="SnapshotState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L108">interface SnapshotState</a>
</h2>

Input properties used for looking up and filtering Snapshot resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L112">property createOption</a>
</h3>

```typescript
createOption?: pulumi.Input<string>;
```


Indicates how the snapshot is to be created. Possible values are `Copy` or `Import`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L116">property diskSizeGb</a>
</h3>

```typescript
diskSizeGb?: pulumi.Input<number>;
```


The size of the Snapshotted Disk in GB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L117">property encryptionSettings</a>
</h3>

```typescript
encryptionSettings?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L121">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L129">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L133">property sourceResourceId</a>
</h3>

```typescript
sourceResourceId?: pulumi.Input<string>;
```


Specifies a reference to an existing snapshot, when `create_option` is `Copy`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L137">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L141">property storageAccountId</a>
</h3>

```typescript
storageAccountId?: pulumi.Input<string>;
```


Specifies the ID of an storage account. Used with `source_uri` to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/snapshot.ts#L142">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="VirtualMachineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L288">interface VirtualMachineArgs</a>
</h2>

The set of arguments for constructing a VirtualMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L292">property availabilitySetId</a>
</h3>

```typescript
availabilitySetId?: pulumi.Input<string>;
```


The Id of the Availability Set in which to create the virtual machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L296">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L300">property deleteDataDisksOnTermination</a>
</h3>

```typescript
deleteDataDisksOnTermination?: pulumi.Input<boolean>;
```


Flag to enable deletion of storage data disk VHD blobs or managed disks when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L304">property deleteOsDiskOnTermination</a>
</h3>

```typescript
deleteOsDiskOnTermination?: pulumi.Input<boolean>;
```


Flag to enable deletion of the OS disk VHD blob or managed disk when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L308">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An identity block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L312">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L316">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L320">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the data disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L324">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies the list of resource IDs for the network interfaces associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L328">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


An OS Profile block as documented below. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L332">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L336">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<{ ... }[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L340">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L344">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L348">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```


Specifies the resource ID for the primary network interface associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L353">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L357">property storageDataDisks</a>
</h3>

```typescript
storageDataDisks?: pulumi.Input<{ ... }[]>;
```


A list of Storage Data disk blocks as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L361">property storageImageReference</a>
</h3>

```typescript
storageImageReference?: pulumi.Input<{ ... }>;
```


A Storage Image Reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L365">property storageOsDisk</a>
</h3>

```typescript
storageOsDisk: pulumi.Input<{ ... }>;
```


A Storage OS Disk block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L369">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L373">property vmSize</a>
</h3>

```typescript
vmSize: pulumi.Input<string>;
```


Specifies the [size of the virtual machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L377">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>>;
```


A collection containing the availability zone to allocate the Virtual Machine in.

<h2 class="pdoc-module-header" id="VirtualMachineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L193">interface VirtualMachineState</a>
</h2>

Input properties used for looking up and filtering VirtualMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L197">property availabilitySetId</a>
</h3>

```typescript
availabilitySetId?: pulumi.Input<string>;
```


The Id of the Availability Set in which to create the virtual machine

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L201">property bootDiagnostics</a>
</h3>

```typescript
bootDiagnostics?: pulumi.Input<{ ... }>;
```


A boot diagnostics profile block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L205">property deleteDataDisksOnTermination</a>
</h3>

```typescript
deleteDataDisksOnTermination?: pulumi.Input<boolean>;
```


Flag to enable deletion of storage data disk VHD blobs or managed disks when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L209">property deleteOsDiskOnTermination</a>
</h3>

```typescript
deleteOsDiskOnTermination?: pulumi.Input<boolean>;
```


Flag to enable deletion of the OS disk VHD blob or managed disk when the VM is deleted, defaults to `false`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L213">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


An identity block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L217">property licenseType</a>
</h3>

```typescript
licenseType?: pulumi.Input<string>;
```


Specifies the Windows OS license type. If supplied, the only allowed values are `Windows_Client` and `Windows_Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L221">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L225">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the data disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L229">property networkInterfaceIds</a>
</h3>

```typescript
networkInterfaceIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies the list of resource IDs for the network interfaces associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L233">property osProfile</a>
</h3>

```typescript
osProfile?: pulumi.Input<{ ... }>;
```


An OS Profile block as documented below. Required when `create_option` in the `storage_os_disk` block is set to `FromImage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L237">property osProfileLinuxConfig</a>
</h3>

```typescript
osProfileLinuxConfig?: pulumi.Input<{ ... }>;
```


A Linux config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L241">property osProfileSecrets</a>
</h3>

```typescript
osProfileSecrets?: pulumi.Input<{ ... }[]>;
```


A collection of Secret blocks as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L245">property osProfileWindowsConfig</a>
</h3>

```typescript
osProfileWindowsConfig?: pulumi.Input<{ ... }>;
```


A Windows config block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L249">property plan</a>
</h3>

```typescript
plan?: pulumi.Input<{ ... }>;
```


A plan block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L253">property primaryNetworkInterfaceId</a>
</h3>

```typescript
primaryNetworkInterfaceId?: pulumi.Input<string>;
```


Specifies the resource ID for the primary network interface associated with the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L258">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the virtual machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L262">property storageDataDisks</a>
</h3>

```typescript
storageDataDisks?: pulumi.Input<{ ... }[]>;
```


A list of Storage Data disk blocks as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L266">property storageImageReference</a>
</h3>

```typescript
storageImageReference?: pulumi.Input<{ ... }>;
```


A Storage Image Reference block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L270">property storageOsDisk</a>
</h3>

```typescript
storageOsDisk?: pulumi.Input<{ ... }>;
```


A Storage OS Disk block as referenced below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L274">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L278">property vmSize</a>
</h3>

```typescript
vmSize?: pulumi.Input<string>;
```


Specifies the [size of the virtual machine](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/compute/virtualMachine.ts#L282">property zones</a>
</h3>

```typescript
zones?: pulumi.Input<pulumi.Input<string>>;
```


A collection containing the availability zone to allocate the Virtual Machine in.

