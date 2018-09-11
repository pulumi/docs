---
title: Module blockstorage
---

<a href="../index.html">@pulumi/openstack</a> &gt; blockstorage

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Volume">class Volume</a>
* <a href="#VolumeAttach">class VolumeAttach</a>
* <a href="#VolumeAttachV2">class VolumeAttachV2</a>
* <a href="#VolumeV1">class VolumeV1</a>
* <a href="#VolumeV2">class VolumeV2</a>
* <a href="#VolumeArgs">interface VolumeArgs</a>
* <a href="#VolumeAttachArgs">interface VolumeAttachArgs</a>
* <a href="#VolumeAttachState">interface VolumeAttachState</a>
* <a href="#VolumeAttachV2Args">interface VolumeAttachV2Args</a>
* <a href="#VolumeAttachV2State">interface VolumeAttachV2State</a>
* <a href="#VolumeState">interface VolumeState</a>
* <a href="#VolumeV1Args">interface VolumeV1Args</a>
* <a href="#VolumeV1State">interface VolumeV1State</a>
* <a href="#VolumeV2Args">interface VolumeV2Args</a>
* <a href="#VolumeV2State">interface VolumeV2State</a>

<a href="/blockstorage/volume.ts">blockstorage/volume.ts</a> <a href="/blockstorage/volumeAttach.ts">blockstorage/volumeAttach.ts</a> <a href="/blockstorage/volumeAttachV2.ts">blockstorage/volumeAttachV2.ts</a> <a href="/blockstorage/volumeV1.ts">blockstorage/volumeV1.ts</a> <a href="/blockstorage/volumeV2.ts">blockstorage/volumeV2.ts</a> 


<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L10">class Volume</a>
</h2>

Manages a V3 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L93">constructor</a>
</h3>

```typescript
new Volume(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Volume resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState): Volume
```


Get an existing Volume resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L28">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L33">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L38">property consistencyGroupId</a>
</h3>

```typescript
public consistencyGroupId: pulumi.Output<string | undefined>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L43">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L49">property enableOnlineResize</a>
</h3>

```typescript
public enableOnlineResize: pulumi.Output<boolean | undefined>;
```


When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L54">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L59">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L64">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L70">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L74">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L79">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L83">property sourceReplica</a>
</h3>

```typescript
public sourceReplica: pulumi.Output<string | undefined>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L88">property sourceVolId</a>
</h3>

```typescript
public sourceVolId: pulumi.Output<string | undefined>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L93">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeAttach">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L22">class VolumeAttach</a>
</h2>

This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.

Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v3 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.

This does not actually attach a volume to an instance. Please use
the `openstack_compute_volume_attach_v3` resource for that.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L104">constructor</a>
</h3>

```typescript
new VolumeAttach(name: string, args: VolumeAttachArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttach resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeAttachState): VolumeAttach
```


Get an existing VolumeAttach resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L40">property attachMode</a>
</h3>

```typescript
public attachMode: pulumi.Output<string | undefined>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L46">property data</a>
</h3>

```typescript
public data: pulumi.Output<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L52">property device</a>
</h3>

```typescript
public device: pulumi.Output<string | undefined>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L56">property driverVolumeType</a>
</h3>

```typescript
public driverVolumeType: pulumi.Output<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L60">property hostName</a>
</h3>

```typescript
public hostName: pulumi.Output<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L64">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string | undefined>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L68">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string | undefined>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L72">property mountPointBase</a>
</h3>

```typescript
public mountPointBase: pulumi.Output<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L76">property multipath</a>
</h3>

```typescript
public multipath: pulumi.Output<boolean | undefined>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L80">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L84">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string | undefined>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L91">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L95">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L99">property wwnn</a>
</h3>

```typescript
public wwnn: pulumi.Output<string | undefined>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L104">property wwpns</a>
</h3>

```typescript
public wwpns: pulumi.Output<string[] | undefined>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L22">class VolumeAttachV2</a>
</h2>

This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.

Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v2 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.

This does not actually attach a volume to an instance. Please use
the `openstack_compute_volume_attach_v2` resource for that.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L104">constructor</a>
</h3>

```typescript
new VolumeAttachV2(name: string, args: VolumeAttachV2Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttachV2 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeAttachV2State): VolumeAttachV2
```


Get an existing VolumeAttachV2 resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L40">property attachMode</a>
</h3>

```typescript
public attachMode: pulumi.Output<string | undefined>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L46">property data</a>
</h3>

```typescript
public data: pulumi.Output<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L52">property device</a>
</h3>

```typescript
public device: pulumi.Output<string | undefined>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L56">property driverVolumeType</a>
</h3>

```typescript
public driverVolumeType: pulumi.Output<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L60">property hostName</a>
</h3>

```typescript
public hostName: pulumi.Output<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L64">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string | undefined>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L68">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string | undefined>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L72">property mountPointBase</a>
</h3>

```typescript
public mountPointBase: pulumi.Output<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L76">property multipath</a>
</h3>

```typescript
public multipath: pulumi.Output<boolean | undefined>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L80">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L84">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string | undefined>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L91">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L95">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L99">property wwnn</a>
</h3>

```typescript
public wwnn: pulumi.Output<string | undefined>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L104">property wwpns</a>
</h3>

```typescript
public wwpns: pulumi.Output<string[] | undefined>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeV1">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L10">class VolumeV1</a>
</h2>

Manages a V1 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L79">constructor</a>
</h3>

```typescript
new VolumeV1(name: string, args: VolumeV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeV1State): VolumeV1
```


Get an existing VolumeV1 resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L28">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L33">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L38">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L43">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L48">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L59">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L64">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L69">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L74">property sourceVolId</a>
</h3>

```typescript
public sourceVolId: pulumi.Output<string | undefined>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L79">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L10">class VolumeV2</a>
</h2>

Manages a V2 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L88">constructor</a>
</h3>

```typescript
new VolumeV2(name: string, args: VolumeV2Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeV2 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeV2State): VolumeV2
```


Get an existing VolumeV2 resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L28">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L33">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L38">property consistencyGroupId</a>
</h3>

```typescript
public consistencyGroupId: pulumi.Output<string | undefined>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L43">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L48">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L53">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L64">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L69">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L74">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L78">property sourceReplica</a>
</h3>

```typescript
public sourceReplica: pulumi.Output<string | undefined>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L83">property sourceVolId</a>
</h3>

```typescript
public sourceVolId: pulumi.Output<string | undefined>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L88">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeArgs">
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L225">interface VolumeArgs</a>
</h2>

The set of arguments for constructing a Volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L230">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L235">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L240">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L246">property enableOnlineResize</a>
</h3>

```typescript
enableOnlineResize?: pulumi.Input<boolean>;
```


When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L251">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L256">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L261">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L267">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L271">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L276">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L280">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L285">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L290">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeAttachArgs">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L240">interface VolumeAttachArgs</a>
</h2>

The set of arguments for constructing a VolumeAttach resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L246">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L252">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L256">property hostName</a>
</h3>

```typescript
hostName: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L260">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L264">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L268">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L272">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L276">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L283">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L287">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L291">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L296">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachState">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L164">interface VolumeAttachState</a>
</h2>

Input properties used for looking up and filtering VolumeAttach resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L170">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L176">property data</a>
</h3>

```typescript
data?: pulumi.Input<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L182">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L186">property driverVolumeType</a>
</h3>

```typescript
driverVolumeType?: pulumi.Input<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L190">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L194">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L198">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L202">property mountPointBase</a>
</h3>

```typescript
mountPointBase?: pulumi.Input<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L206">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L210">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L214">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L221">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L225">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L229">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L234">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2Args">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L240">interface VolumeAttachV2Args</a>
</h2>

The set of arguments for constructing a VolumeAttachV2 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L246">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L252">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L256">property hostName</a>
</h3>

```typescript
hostName: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L260">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L264">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L268">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L272">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L276">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L283">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L287">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L291">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L296">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2State">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L164">interface VolumeAttachV2State</a>
</h2>

Input properties used for looking up and filtering VolumeAttachV2 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L170">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L176">property data</a>
</h3>

```typescript
data?: pulumi.Input<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L182">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L186">property driverVolumeType</a>
</h3>

```typescript
driverVolumeType?: pulumi.Input<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L190">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L194">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L198">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L202">property mountPointBase</a>
</h3>

```typescript
mountPointBase?: pulumi.Input<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L206">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L210">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L214">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L221">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L225">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L229">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L234">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeState">
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L148">interface VolumeState</a>
</h2>

Input properties used for looking up and filtering Volume resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L154">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L159">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L164">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L169">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L175">property enableOnlineResize</a>
</h3>

```typescript
enableOnlineResize?: pulumi.Input<boolean>;
```


When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L180">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L185">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L196">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L200">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L205">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L209">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L214">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L219">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV1Args">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L191">interface VolumeV1Args</a>
</h2>

The set of arguments for constructing a VolumeV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L196">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L201">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L206">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L211">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L222">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L227">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L232">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L237">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L242">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV1State">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L128">interface VolumeV1State</a>
</h2>

Input properties used for looking up and filtering VolumeV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L134">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L139">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L144">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L149">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L154">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L165">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L170">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L175">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L180">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L185">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2Args">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L213">interface VolumeV2Args</a>
</h2>

The set of arguments for constructing a VolumeV2 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L218">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L223">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L228">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L233">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L238">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L243">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L249">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L254">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L259">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L263">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L268">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L273">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2State">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L141">interface VolumeV2State</a>
</h2>

Input properties used for looking up and filtering VolumeV2 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L147">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L152">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L157">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L162">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L167">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L172">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L177">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L183">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L188">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L193">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L197">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L202">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L207">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

