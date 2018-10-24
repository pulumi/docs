---
title: Module devtest
---

<a href="../index.html">@pulumi/azure</a> &gt; devtest

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Lab">class Lab</a>
* <a href="#LinuxVirtualMachine">class LinuxVirtualMachine</a>
* <a href="#Policy">class Policy</a>
* <a href="#VirtualNetwork">class VirtualNetwork</a>
* <a href="#WindowsVirtualMachine">class WindowsVirtualMachine</a>
* <a href="#getLab">function getLab</a>
* <a href="#GetLabArgs">interface GetLabArgs</a>
* <a href="#GetLabResult">interface GetLabResult</a>
* <a href="#LabArgs">interface LabArgs</a>
* <a href="#LabState">interface LabState</a>
* <a href="#LinuxVirtualMachineArgs">interface LinuxVirtualMachineArgs</a>
* <a href="#LinuxVirtualMachineState">interface LinuxVirtualMachineState</a>
* <a href="#PolicyArgs">interface PolicyArgs</a>
* <a href="#PolicyState">interface PolicyState</a>
* <a href="#VirtualNetworkArgs">interface VirtualNetworkArgs</a>
* <a href="#VirtualNetworkState">interface VirtualNetworkState</a>
* <a href="#WindowsVirtualMachineArgs">interface WindowsVirtualMachineArgs</a>
* <a href="#WindowsVirtualMachineState">interface WindowsVirtualMachineState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts">devtest/getLab.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts">devtest/lab.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts">devtest/linuxVirtualMachine.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts">devtest/policy.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts">devtest/virtualNetwork.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts">devtest/windowsVirtualMachine.ts</a> 


<h2 class="pdoc-module-header" id="Lab">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L10">class Lab</a>
</h2>

Manages a Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L66">constructor</a>
</h3>

```typescript
new Lab(name: string, args: LabArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Lab resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LabState): Lab
```


Get an existing Lab resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L26">property artifactsStorageAccountId</a>
</h3>

```typescript
public artifactsStorageAccountId: pulumi.Output<string>;
```


The ID of the Storage Account used for Artifact Storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L30">property defaultPremiumStorageAccountId</a>
</h3>

```typescript
public defaultPremiumStorageAccountId: pulumi.Output<string>;
```


The ID of the Default Premium Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L34">property defaultStorageAccountId</a>
</h3>

```typescript
public defaultStorageAccountId: pulumi.Output<string>;
```


The ID of the Default Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L38">property keyVaultId</a>
</h3>

```typescript
public keyVaultId: pulumi.Output<string>;
```


The ID of the Key used for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L42">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L50">property premiumDataDiskStorageAccountId</a>
</h3>

```typescript
public premiumDataDiskStorageAccountId: pulumi.Output<string>;
```


The ID of the Storage Account used for Storage of Premium Data Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L58">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string | undefined>;
```


The type of storage used by the Dev Test Lab. Possible values are `Standard` and `Premium`. Defaults to `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L62">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L66">property uniqueIdentifier</a>
</h3>

```typescript
public uniqueIdentifier: pulumi.Output<string>;
```


The unique immutable identifier of the Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LinuxVirtualMachine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L10">class LinuxVirtualMachine</a>
</h2>

Manages a Linux Virtual Machine within a Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L98">constructor</a>
</h3>

```typescript
new LinuxVirtualMachine(name: string, args: LinuxVirtualMachineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LinuxVirtualMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LinuxVirtualMachineState): LinuxVirtualMachine
```


Get an existing LinuxVirtualMachine resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L26">property allowClaim</a>
</h3>

```typescript
public allowClaim: pulumi.Output<boolean | undefined>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L30">property disallowPublicIpAddress</a>
</h3>

```typescript
public disallowPublicIpAddress: pulumi.Output<boolean | undefined>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L34">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L38">property galleryImageReference</a>
</h3>

```typescript
public galleryImageReference: pulumi.Output<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L42">property inboundNatRules</a>
</h3>

```typescript
public inboundNatRules: pulumi.Output<{ ... }[] | undefined>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L46">property labName</a>
</h3>

```typescript
public labName: pulumi.Output<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L50">property labSubnetName</a>
</h3>

```typescript
public labSubnetName: pulumi.Output<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L54">property labVirtualNetworkId</a>
</h3>

```typescript
public labVirtualNetworkId: pulumi.Output<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L58">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L66">property notes</a>
</h3>

```typescript
public notes: pulumi.Output<string | undefined>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L70">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L74">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L78">property size</a>
</h3>

```typescript
public size: pulumi.Output<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L82">property sshKey</a>
</h3>

```typescript
public sshKey: pulumi.Output<string | undefined>;
```


The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L86">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L90">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L94">property uniqueIdentifier</a>
</h3>

```typescript
public uniqueIdentifier: pulumi.Output<string>;
```


The unique immutable identifier of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L98">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="Policy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L10">class Policy</a>
</h2>

Manages a Policy within a Dev Test Policy Set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L58">constructor</a>
</h3>

```typescript
new Policy(name: string, args: PolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Policy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState): Policy
```


Get an existing Policy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L30">property evaluatorType</a>
</h3>

```typescript
public evaluatorType: pulumi.Output<string>;
```


The Evaluation Type used for this Policy. Possible values include: 'AllowedValuesPolicy', 'MaxValuePolicy'. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L34">property factData</a>
</h3>

```typescript
public factData: pulumi.Output<string | undefined>;
```


The Fact Data for this Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L38">property labName</a>
</h3>

```typescript
public labName: pulumi.Output<string>;
```


Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Dev Test Policy. Possible values are `GalleryImage`, `LabPremiumVmCount`, `LabTargetCost`, `LabVmCount`, `LabVmSize`, `UserOwnedLabPremiumVmCount`, `UserOwnedLabVmCount` and `UserOwnedLabVmCountInSubnet`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L46">property policySetName</a>
</h3>

```typescript
public policySetName: pulumi.Output<string>;
```


Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L54">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L58">property threshold</a>
</h3>

```typescript
public threshold: pulumi.Output<string>;
```


The Threshold for this Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="VirtualNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L10">class VirtualNetwork</a>
</h2>

Manages a Virtual Network within a Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L50">constructor</a>
</h3>

```typescript
new VirtualNetwork(name: string, args: VirtualNetworkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VirtualNetwork resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkState): VirtualNetwork
```


Get an existing VirtualNetwork resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for the Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L30">property labName</a>
</h3>

```typescript
public labName: pulumi.Output<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L42">property subnet</a>
</h3>

```typescript
public subnet: pulumi.Output<{ ... }>;
```


A `subnet` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L46">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L50">property uniqueIdentifier</a>
</h3>

```typescript
public uniqueIdentifier: pulumi.Output<string>;
```


The unique immutable identifier of the Dev Test Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="WindowsVirtualMachine">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L10">class WindowsVirtualMachine</a>
</h2>

Manages a Windows Virtual Machine within a Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L94">constructor</a>
</h3>

```typescript
new WindowsVirtualMachine(name: string, args: WindowsVirtualMachineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a WindowsVirtualMachine resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WindowsVirtualMachineState): WindowsVirtualMachine
```


Get an existing WindowsVirtualMachine resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L26">property allowClaim</a>
</h3>

```typescript
public allowClaim: pulumi.Output<boolean | undefined>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L30">property disallowPublicIpAddress</a>
</h3>

```typescript
public disallowPublicIpAddress: pulumi.Output<boolean | undefined>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L34">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L38">property galleryImageReference</a>
</h3>

```typescript
public galleryImageReference: pulumi.Output<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L42">property inboundNatRules</a>
</h3>

```typescript
public inboundNatRules: pulumi.Output<{ ... }[] | undefined>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L46">property labName</a>
</h3>

```typescript
public labName: pulumi.Output<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L50">property labSubnetName</a>
</h3>

```typescript
public labSubnetName: pulumi.Output<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L54">property labVirtualNetworkId</a>
</h3>

```typescript
public labVirtualNetworkId: pulumi.Output<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L58">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L62">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L66">property notes</a>
</h3>

```typescript
public notes: pulumi.Output<string | undefined>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L70">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L74">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L78">property size</a>
</h3>

```typescript
public size: pulumi.Output<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L82">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L86">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L90">property uniqueIdentifier</a>
</h3>

```typescript
public uniqueIdentifier: pulumi.Output<string>;
```


The unique immutable identifier of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L94">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="getLab">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L10">function getLab</a>
</h2>

```typescript
getLab(args: GetLabArgs, opts?: pulumi.InvokeOptions): Promise<GetLabResult>
```


Use this data source to access information about an existing Dev Test Lab.

<h2 class="pdoc-module-header" id="GetLabArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L20">interface GetLabArgs</a>
</h2>

A collection of arguments for invoking getLab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where the Dev Test Lab exists.

<h2 class="pdoc-module-header" id="GetLabResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L34">interface GetLabResult</a>
</h2>

A collection of values returned by getLab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L38">property artifactsStorageAccountId</a>
</h3>

```typescript
artifactsStorageAccountId: string;
```


The ID of the Storage Account used for Artifact Storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L42">property defaultPremiumStorageAccountId</a>
</h3>

```typescript
defaultPremiumStorageAccountId: string;
```


The ID of the Default Premium Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L46">property defaultStorageAccountId</a>
</h3>

```typescript
defaultStorageAccountId: string;
```


The ID of the Default Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L74">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L50">property keyVaultId</a>
</h3>

```typescript
keyVaultId: string;
```


The ID of the Key used for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L54">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the Dev Test Lab exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L58">property premiumDataDiskStorageAccountId</a>
</h3>

```typescript
premiumDataDiskStorageAccountId: string;
```


The ID of the Storage Account used for Storage of Premium Data Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L62">property storageType</a>
</h3>

```typescript
storageType: string;
```


The type of storage used by the Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L66">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/getLab.ts#L70">property uniqueIdentifier</a>
</h3>

```typescript
uniqueIdentifier: string;
```


The unique immutable identifier of the Dev Test Lab.

<h2 class="pdoc-module-header" id="LabArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L168">interface LabArgs</a>
</h2>

The set of arguments for constructing a Lab resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L172">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L180">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L184">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The type of storage used by the Dev Test Lab. Possible values are `Standard` and `Premium`. Defaults to `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L188">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="LabState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L118">interface LabState</a>
</h2>

Input properties used for looking up and filtering Lab resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L122">property artifactsStorageAccountId</a>
</h3>

```typescript
artifactsStorageAccountId?: pulumi.Input<string>;
```


The ID of the Storage Account used for Artifact Storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L126">property defaultPremiumStorageAccountId</a>
</h3>

```typescript
defaultPremiumStorageAccountId?: pulumi.Input<string>;
```


The ID of the Default Premium Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L130">property defaultStorageAccountId</a>
</h3>

```typescript
defaultStorageAccountId?: pulumi.Input<string>;
```


The ID of the Default Storage Account for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L134">property keyVaultId</a>
</h3>

```typescript
keyVaultId?: pulumi.Input<string>;
```


The ID of the Key used for this Dev Test Lab.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L138">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L146">property premiumDataDiskStorageAccountId</a>
</h3>

```typescript
premiumDataDiskStorageAccountId?: pulumi.Input<string>;
```


The ID of the Storage Account used for Storage of Premium Data Disk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L150">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L154">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The type of storage used by the Dev Test Lab. Possible values are `Standard` and `Premium`. Defaults to `Premium`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L158">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/lab.ts#L162">property uniqueIdentifier</a>
</h3>

```typescript
uniqueIdentifier?: pulumi.Input<string>;
```


The unique immutable identifier of the Dev Test Lab.

<h2 class="pdoc-module-header" id="LinuxVirtualMachineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L269">interface LinuxVirtualMachineArgs</a>
</h2>

The set of arguments for constructing a LinuxVirtualMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L273">property allowClaim</a>
</h3>

```typescript
allowClaim?: pulumi.Input<boolean>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L277">property disallowPublicIpAddress</a>
</h3>

```typescript
disallowPublicIpAddress?: pulumi.Input<boolean>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L281">property galleryImageReference</a>
</h3>

```typescript
galleryImageReference: pulumi.Input<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L285">property inboundNatRules</a>
</h3>

```typescript
inboundNatRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L289">property labName</a>
</h3>

```typescript
labName: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L293">property labSubnetName</a>
</h3>

```typescript
labSubnetName: pulumi.Input<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L297">property labVirtualNetworkId</a>
</h3>

```typescript
labVirtualNetworkId: pulumi.Input<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L301">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L305">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L309">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L313">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L317">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L321">property size</a>
</h3>

```typescript
size: pulumi.Input<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L325">property sshKey</a>
</h3>

```typescript
sshKey?: pulumi.Input<string>;
```


The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L329">property storageType</a>
</h3>

```typescript
storageType: pulumi.Input<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L333">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L337">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="LinuxVirtualMachineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L187">interface LinuxVirtualMachineState</a>
</h2>

Input properties used for looking up and filtering LinuxVirtualMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L191">property allowClaim</a>
</h3>

```typescript
allowClaim?: pulumi.Input<boolean>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L195">property disallowPublicIpAddress</a>
</h3>

```typescript
disallowPublicIpAddress?: pulumi.Input<boolean>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L199">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L203">property galleryImageReference</a>
</h3>

```typescript
galleryImageReference?: pulumi.Input<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L207">property inboundNatRules</a>
</h3>

```typescript
inboundNatRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L211">property labName</a>
</h3>

```typescript
labName?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L215">property labSubnetName</a>
</h3>

```typescript
labSubnetName?: pulumi.Input<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L219">property labVirtualNetworkId</a>
</h3>

```typescript
labVirtualNetworkId?: pulumi.Input<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L223">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L227">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L231">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L235">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L239">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L243">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L247">property sshKey</a>
</h3>

```typescript
sshKey?: pulumi.Input<string>;
```


The SSH Key associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L251">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L255">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L259">property uniqueIdentifier</a>
</h3>

```typescript
uniqueIdentifier?: pulumi.Input<string>;
```


The unique immutable identifier of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/linuxVirtualMachine.ts#L263">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L157">interface PolicyArgs</a>
</h2>

The set of arguments for constructing a Policy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L161">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L165">property evaluatorType</a>
</h3>

```typescript
evaluatorType: pulumi.Input<string>;
```


The Evaluation Type used for this Policy. Possible values include: 'AllowedValuesPolicy', 'MaxValuePolicy'. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L169">property factData</a>
</h3>

```typescript
factData?: pulumi.Input<string>;
```


The Fact Data for this Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L173">property labName</a>
</h3>

```typescript
labName: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L177">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Policy. Possible values are `GalleryImage`, `LabPremiumVmCount`, `LabTargetCost`, `LabVmCount`, `LabVmSize`, `UserOwnedLabPremiumVmCount`, `UserOwnedLabVmCount` and `UserOwnedLabVmCountInSubnet`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L181">property policySetName</a>
</h3>

```typescript
policySetName: pulumi.Input<string>;
```


Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L185">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L189">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L193">property threshold</a>
</h3>

```typescript
threshold: pulumi.Input<string>;
```


The Threshold for this Policy.

<h2 class="pdoc-module-header" id="PolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L115">interface PolicyState</a>
</h2>

Input properties used for looking up and filtering Policy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L119">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L123">property evaluatorType</a>
</h3>

```typescript
evaluatorType?: pulumi.Input<string>;
```


The Evaluation Type used for this Policy. Possible values include: 'AllowedValuesPolicy', 'MaxValuePolicy'. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L127">property factData</a>
</h3>

```typescript
factData?: pulumi.Input<string>;
```


The Fact Data for this Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L131">property labName</a>
</h3>

```typescript
labName?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Policy. Possible values are `GalleryImage`, `LabPremiumVmCount`, `LabTargetCost`, `LabVmCount`, `LabVmSize`, `UserOwnedLabPremiumVmCount`, `UserOwnedLabVmCount` and `UserOwnedLabVmCountInSubnet`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L139">property policySetName</a>
</h3>

```typescript
policySetName?: pulumi.Input<string>;
```


Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L143">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L147">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/policy.ts#L151">property threshold</a>
</h3>

```typescript
threshold?: pulumi.Input<string>;
```


The Threshold for this Policy.

<h2 class="pdoc-module-header" id="VirtualNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L128">interface VirtualNetworkArgs</a>
</h2>

The set of arguments for constructing a VirtualNetwork resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L136">property labName</a>
</h3>

```typescript
labName: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L148">property subnet</a>
</h3>

```typescript
subnet?: pulumi.Input<{ ... }>;
```


A `subnet` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L152">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VirtualNetworkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L94">interface VirtualNetworkState</a>
</h2>

Input properties used for looking up and filtering VirtualNetwork resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the Virtual Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L102">property labName</a>
</h3>

```typescript
labName?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L110">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L114">property subnet</a>
</h3>

```typescript
subnet?: pulumi.Input<{ ... }>;
```


A `subnet` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L118">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/virtualNetwork.ts#L122">property uniqueIdentifier</a>
</h3>

```typescript
uniqueIdentifier?: pulumi.Input<string>;
```


The unique immutable identifier of the Dev Test Virtual Network.

<h2 class="pdoc-module-header" id="WindowsVirtualMachineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L262">interface WindowsVirtualMachineArgs</a>
</h2>

The set of arguments for constructing a WindowsVirtualMachine resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L266">property allowClaim</a>
</h3>

```typescript
allowClaim?: pulumi.Input<boolean>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L270">property disallowPublicIpAddress</a>
</h3>

```typescript
disallowPublicIpAddress?: pulumi.Input<boolean>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L274">property galleryImageReference</a>
</h3>

```typescript
galleryImageReference: pulumi.Input<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L278">property inboundNatRules</a>
</h3>

```typescript
inboundNatRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L282">property labName</a>
</h3>

```typescript
labName: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L286">property labSubnetName</a>
</h3>

```typescript
labSubnetName: pulumi.Input<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L290">property labVirtualNetworkId</a>
</h3>

```typescript
labVirtualNetworkId: pulumi.Input<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L294">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L298">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L302">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L306">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L310">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L314">property size</a>
</h3>

```typescript
size: pulumi.Input<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L318">property storageType</a>
</h3>

```typescript
storageType: pulumi.Input<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L322">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L326">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="WindowsVirtualMachineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L184">interface WindowsVirtualMachineState</a>
</h2>

Input properties used for looking up and filtering WindowsVirtualMachine resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L188">property allowClaim</a>
</h3>

```typescript
allowClaim?: pulumi.Input<boolean>;
```


Can this Virtual Machine be claimed by users? Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L192">property disallowPublicIpAddress</a>
</h3>

```typescript
disallowPublicIpAddress?: pulumi.Input<boolean>;
```


Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L196">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L200">property galleryImageReference</a>
</h3>

```typescript
galleryImageReference?: pulumi.Input<{ ... }>;
```


A `gallery_image_reference` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L204">property inboundNatRules</a>
</h3>

```typescript
inboundNatRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `inbound_nat_rule` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L208">property labName</a>
</h3>

```typescript
labName?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L212">property labSubnetName</a>
</h3>

```typescript
labSubnetName?: pulumi.Input<string>;
```


The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L216">property labVirtualNetworkId</a>
</h3>

```typescript
labVirtualNetworkId?: pulumi.Input<string>;
```


The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L220">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L224">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L228">property notes</a>
</h3>

```typescript
notes?: pulumi.Input<string>;
```


Any notes about the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L232">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The Password associated with the `username` used to login to this Virtual Machine. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L236">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L240">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The Machine Size to use for this Virtual Machine, such as `Standard_F2`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L244">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The type of Storage to use on this Virtual Machine. Possible values are `Standard` and `Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L248">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L252">property uniqueIdentifier</a>
</h3>

```typescript
uniqueIdentifier?: pulumi.Input<string>;
```


The unique immutable identifier of the Virtual Machine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/devtest/windowsVirtualMachine.ts#L256">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.

