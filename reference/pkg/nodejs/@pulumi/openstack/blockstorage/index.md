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
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L9">class Volume</a>
</h2>

Manages a V3 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L92">constructor</a>
</h3>

```typescript
new Volume(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Volume resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L27">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L32">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L37">property consistencyGroupId</a>
</h3>

```typescript
public consistencyGroupId: pulumi.Output<string | undefined>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L42">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L48">property enableOnlineResize</a>
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
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L53">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L58">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L63">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L69">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L73">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L78">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L82">property sourceReplica</a>
</h3>

```typescript
public sourceReplica: pulumi.Output<string | undefined>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L87">property sourceVolId</a>
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
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L92">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeAttach">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L21">class VolumeAttach</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L103">constructor</a>
</h3>

```typescript
new VolumeAttach(name: string, args: VolumeAttachArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttach resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L30">method get</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L39">property attachMode</a>
</h3>

```typescript
public attachMode: pulumi.Output<string | undefined>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L45">property data</a>
</h3>

```typescript
public data: pulumi.Output<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L51">property device</a>
</h3>

```typescript
public device: pulumi.Output<string | undefined>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L55">property driverVolumeType</a>
</h3>

```typescript
public driverVolumeType: pulumi.Output<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L59">property hostName</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L63">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string | undefined>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L67">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string | undefined>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L71">property mountPointBase</a>
</h3>

```typescript
public mountPointBase: pulumi.Output<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L75">property multipath</a>
</h3>

```typescript
public multipath: pulumi.Output<boolean | undefined>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L79">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L83">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string | undefined>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L90">property region</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L94">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L98">property wwnn</a>
</h3>

```typescript
public wwnn: pulumi.Output<string | undefined>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L103">property wwpns</a>
</h3>

```typescript
public wwpns: pulumi.Output<string[] | undefined>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L21">class VolumeAttachV2</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L103">constructor</a>
</h3>

```typescript
new VolumeAttachV2(name: string, args: VolumeAttachV2Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttachV2 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L30">method get</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L39">property attachMode</a>
</h3>

```typescript
public attachMode: pulumi.Output<string | undefined>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L45">property data</a>
</h3>

```typescript
public data: pulumi.Output<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L51">property device</a>
</h3>

```typescript
public device: pulumi.Output<string | undefined>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L55">property driverVolumeType</a>
</h3>

```typescript
public driverVolumeType: pulumi.Output<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L59">property hostName</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L63">property initiator</a>
</h3>

```typescript
public initiator: pulumi.Output<string | undefined>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L67">property ipAddress</a>
</h3>

```typescript
public ipAddress: pulumi.Output<string | undefined>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L71">property mountPointBase</a>
</h3>

```typescript
public mountPointBase: pulumi.Output<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L75">property multipath</a>
</h3>

```typescript
public multipath: pulumi.Output<boolean | undefined>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L79">property osType</a>
</h3>

```typescript
public osType: pulumi.Output<string | undefined>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L83">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string | undefined>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L90">property region</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L94">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L98">property wwnn</a>
</h3>

```typescript
public wwnn: pulumi.Output<string | undefined>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L103">property wwpns</a>
</h3>

```typescript
public wwpns: pulumi.Output<string[] | undefined>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeV1">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L9">class VolumeV1</a>
</h2>

Manages a V1 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L78">constructor</a>
</h3>

```typescript
new VolumeV1(name: string, args: VolumeV1Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeV1 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L27">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L32">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L37">property description</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L42">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L47">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L58">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L63">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L68">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L73">property sourceVolId</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L78">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L9">class VolumeV2</a>
</h2>

Manages a V2 volume resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L87">constructor</a>
</h3>

```typescript
new VolumeV2(name: string, args: VolumeV2Args, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeV2 resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L27">property attachments</a>
</h3>

```typescript
public attachments: pulumi.Output<{ ... }[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L32">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L37">property consistencyGroupId</a>
</h3>

```typescript
public consistencyGroupId: pulumi.Output<string | undefined>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L42">property description</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L47">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string | undefined>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L52">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L63">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L68">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L73">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L77">property sourceReplica</a>
</h3>

```typescript
public sourceReplica: pulumi.Output<string | undefined>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L82">property sourceVolId</a>
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
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L87">property volumeType</a>
</h3>

```typescript
public volumeType: pulumi.Output<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeArgs">
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L224">interface VolumeArgs</a>
</h2>

The set of arguments for constructing a Volume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L229">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L234">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L239">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L245">property enableOnlineResize</a>
</h3>

```typescript
enableOnlineResize?: pulumi.Input<boolean>;
```


When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L250">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L255">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L260">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L266">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L270">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L275">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L279">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L284">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L289">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeAttachArgs">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L239">interface VolumeAttachArgs</a>
</h2>

The set of arguments for constructing a VolumeAttach resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L245">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L251">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L255">property hostName</a>
</h3>

```typescript
hostName: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L259">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L263">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L267">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L271">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L275">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L282">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L286">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L290">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L295">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachState">
<a class="pdoc-member-name" href="/blockstorage/volumeAttach.ts#L163">interface VolumeAttachState</a>
</h2>

Input properties used for looking up and filtering VolumeAttach resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L169">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L175">property data</a>
</h3>

```typescript
data?: pulumi.Input<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L181">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L185">property driverVolumeType</a>
</h3>

```typescript
driverVolumeType?: pulumi.Input<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L189">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L193">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L197">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L201">property mountPointBase</a>
</h3>

```typescript
mountPointBase?: pulumi.Input<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L205">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L209">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L213">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L220">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V3 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L224">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L228">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttach.ts#L233">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2Args">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L239">interface VolumeAttachV2Args</a>
</h2>

The set of arguments for constructing a VolumeAttachV2 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L245">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L251">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L255">property hostName</a>
</h3>

```typescript
hostName: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L259">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L263">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L267">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L271">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L275">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L282">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L286">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L290">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L295">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeAttachV2State">
<a class="pdoc-member-name" href="/blockstorage/volumeAttachV2.ts#L163">interface VolumeAttachV2State</a>
</h2>

Input properties used for looking up and filtering VolumeAttachV2 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L169">property attachMode</a>
</h3>

```typescript
attachMode?: pulumi.Input<string>;
```


Specify whether to attach the volume as Read-Only
(`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
If left unspecified, the Block Storage API will apply a default of `rw`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L175">property data</a>
</h3>

```typescript
data?: pulumi.Input<{ ... }>;
```


This is a map of key/value pairs that contain the connection
information. You will want to pass this information to a provisioner
script to finalize the connection. See below for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L181">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device to tell the Block Storage service this
volume will be attached as. This is purely for informational purposes.
You can specify `auto` or a device such as `/dev/vdc`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L185">property driverVolumeType</a>
</h3>

```typescript
driverVolumeType?: pulumi.Input<string>;
```


The storage driver that the volume is based on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L189">property hostName</a>
</h3>

```typescript
hostName?: pulumi.Input<string>;
```


The host to attach the volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L193">property initiator</a>
</h3>

```typescript
initiator?: pulumi.Input<string>;
```


The iSCSI initiator string to make the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L197">property ipAddress</a>
</h3>

```typescript
ipAddress?: pulumi.Input<string>;
```


The IP address of the `host_name` above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L201">property mountPointBase</a>
</h3>

```typescript
mountPointBase?: pulumi.Input<string>;
```


A mount point base name for shared storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L205">property multipath</a>
</h3>

```typescript
multipath?: pulumi.Input<boolean>;
```


Whether to connect to this volume via multipath.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L209">property osType</a>
</h3>

```typescript
osType?: pulumi.Input<string>;
```


The iSCSI initiator OS type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L213">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The iSCSI initiator platform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L220">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Block Storage
client. A Block Storage client is needed to create a volume attachment.
If omitted, the `region` argument of the provider is used. Changing this
creates a new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L224">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L228">property wwnn</a>
</h3>

```typescript
wwnn?: pulumi.Input<string>;
```


A wwnn name. Used for Fibre Channel connections.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeAttachV2.ts#L233">property wwpns</a>
</h3>

```typescript
wwpns?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of wwpn strings. Used for Fibre Channel
connections.

<h2 class="pdoc-module-header" id="VolumeState">
<a class="pdoc-member-name" href="/blockstorage/volume.ts#L147">interface VolumeState</a>
</h2>

Input properties used for looking up and filtering Volume resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L153">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L158">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L163">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L174">property enableOnlineResize</a>
</h3>

```typescript
enableOnlineResize?: pulumi.Input<boolean>;
```


When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L179">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L184">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L189">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L195">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L199">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L204">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L208">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L213">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volume.ts#L218">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV1Args">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L190">interface VolumeV1Args</a>
</h2>

The set of arguments for constructing a VolumeV1 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L195">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L200">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L205">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L210">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L215">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L221">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L226">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L231">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L236">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L241">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV1State">
<a class="pdoc-member-name" href="/blockstorage/volumeV1.ts#L127">interface VolumeV1State</a>
</h2>

Input properties used for looking up and filtering VolumeV1 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L133">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L138">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L143">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L148">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L153">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L164">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L169">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L174">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L179">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV1.ts#L184">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2Args">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L212">interface VolumeV2Args</a>
</h2>

The set of arguments for constructing a VolumeV2 resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L217">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L222">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L227">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L232">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L237">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L242">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L248">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L253">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L258">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L262">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L267">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L272">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

<h2 class="pdoc-module-header" id="VolumeV2State">
<a class="pdoc-member-name" href="/blockstorage/volumeV2.ts#L140">interface VolumeV2State</a>
</h2>

Input properties used for looking up and filtering VolumeV2 resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L146">property attachments</a>
</h3>

```typescript
attachments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


If a volume is attached to an instance, this attribute will
display the Attachment ID, Instance ID, and the Device as the Instance
sees it.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L151">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone for the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L156">property consistencyGroupId</a>
</h3>

```typescript
consistencyGroupId?: pulumi.Input<string>;
```


The consistency group to place the volume
in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L161">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the volume. Changing this updates
the volume's description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L166">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


The image ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L171">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the volume. Changing this updates the
volume's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L182">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L187">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the volume to create (in gigabytes). Changing
this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L192">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L196">property sourceReplica</a>
</h3>

```typescript
sourceReplica?: pulumi.Input<string>;
```


The volume ID to replicate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L201">property sourceVolId</a>
</h3>

```typescript
sourceVolId?: pulumi.Input<string>;
```


The volume ID from which to create the volume.
Changing this creates a new volume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/blockstorage/volumeV2.ts#L206">property volumeType</a>
</h3>

```typescript
volumeType?: pulumi.Input<string>;
```


The type of volume to create.
Changing this creates a new volume.

