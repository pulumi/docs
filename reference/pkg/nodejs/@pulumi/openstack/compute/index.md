---
title: Module compute
---

<a href="../index.html">@pulumi/openstack</a> &gt; compute

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Flavor">class Flavor</a>
* <a href="#FloatingIP">class FloatingIP</a>
* <a href="#FloatingIpAssociate">class FloatingIpAssociate</a>
* <a href="#Instance">class Instance</a>
* <a href="#Keypair">class Keypair</a>
* <a href="#SecGroup">class SecGroup</a>
* <a href="#ServerGroup">class ServerGroup</a>
* <a href="#VolumeAttach">class VolumeAttach</a>
* <a href="#getFlavor">function getFlavor</a>
* <a href="#getKeypair">function getKeypair</a>
* <a href="#FlavorArgs">interface FlavorArgs</a>
* <a href="#FlavorState">interface FlavorState</a>
* <a href="#FloatingIPArgs">interface FloatingIPArgs</a>
* <a href="#FloatingIPState">interface FloatingIPState</a>
* <a href="#FloatingIpAssociateArgs">interface FloatingIpAssociateArgs</a>
* <a href="#FloatingIpAssociateState">interface FloatingIpAssociateState</a>
* <a href="#GetFlavorArgs">interface GetFlavorArgs</a>
* <a href="#GetFlavorResult">interface GetFlavorResult</a>
* <a href="#GetKeypairArgs">interface GetKeypairArgs</a>
* <a href="#GetKeypairResult">interface GetKeypairResult</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#KeypairArgs">interface KeypairArgs</a>
* <a href="#KeypairState">interface KeypairState</a>
* <a href="#SecGroupArgs">interface SecGroupArgs</a>
* <a href="#SecGroupState">interface SecGroupState</a>
* <a href="#ServerGroupArgs">interface ServerGroupArgs</a>
* <a href="#ServerGroupState">interface ServerGroupState</a>
* <a href="#VolumeAttachArgs">interface VolumeAttachArgs</a>
* <a href="#VolumeAttachState">interface VolumeAttachState</a>

<a href="/compute/flavor.ts">compute/flavor.ts</a> <a href="/compute/floatingIP.ts">compute/floatingIP.ts</a> <a href="/compute/floatingIpAssociate.ts">compute/floatingIpAssociate.ts</a> <a href="/compute/getFlavor.ts">compute/getFlavor.ts</a> <a href="/compute/getKeypair.ts">compute/getKeypair.ts</a> <a href="/compute/instance.ts">compute/instance.ts</a> <a href="/compute/keypair.ts">compute/keypair.ts</a> <a href="/compute/secGroup.ts">compute/secGroup.ts</a> <a href="/compute/serverGroup.ts">compute/serverGroup.ts</a> <a href="/compute/volumeAttach.ts">compute/volumeAttach.ts</a> 


<h2 class="pdoc-module-header" id="Flavor">
<a class="pdoc-member-name" href="/compute/flavor.ts#L9">class Flavor</a>
</h2>

Manages a V2 flavor resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L68">constructor</a>
</h3>

```typescript
new Flavor(name: string, args: FlavorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Flavor resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FlavorState): Flavor
```


Get an existing Flavor resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/flavor.ts#L26">property disk</a>
</h3>

```typescript
public disk: pulumi.Output<number>;
```


The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L27">property ephemeral</a>
</h3>

```typescript
public ephemeral: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L31">property extraSpecs</a>
</h3>

```typescript
public extraSpecs: pulumi.Output<{ ... }>;
```


Key/Value pairs of metadata for the flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L36">property isPublic</a>
</h3>

```typescript
public isPublic: pulumi.Output<boolean | undefined>;
```


Whether the flavor is public. Changing this creates
a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the flavor. Changing this creates a new
flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L46">property ram</a>
</h3>

```typescript
public ram: pulumi.Output<number>;
```


The amount of RAM to use, in megabytes. Changing this
creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L53">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L58">property rxTxFactor</a>
</h3>

```typescript
public rxTxFactor: pulumi.Output<number | undefined>;
```


RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L63">property swap</a>
</h3>

```typescript
public swap: pulumi.Output<number | undefined>;
```


The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L68">property vcpus</a>
</h3>

```typescript
public vcpus: pulumi.Output<number>;
```


The number of virtual CPUs to use. Changing this creates
a new flavor.

<h2 class="pdoc-module-header" id="FloatingIP">
<a class="pdoc-member-name" href="/compute/floatingIP.ts#L15">class FloatingIP</a>
</h2>

Manages a V2 floating IP resource within OpenStack Nova (compute)
that can be used for compute instances.

Please note that managing floating IPs through the OpenStack Compute API has
been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the [`openstack_networking_floatingip_v2`](networking_floatingip_v2.html)
resource instead, which uses the OpenStack Networking API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L52">constructor</a>
</h3>

```typescript
new FloatingIP(name: string, args: FloatingIPArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FloatingIP resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIPState): FloatingIP
```


Get an existing FloatingIP resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L31">property address</a>
</h3>

```typescript
public address: pulumi.Output<string>;
```


The actual floating IP address itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L35">property fixedIp</a>
</h3>

```typescript
public fixedIp: pulumi.Output<string>;
```


The fixed IP address corresponding to the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L39">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


UUID of the compute instance associated with the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L44">property pool</a>
</h3>

```typescript
public pool: pulumi.Output<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L52">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FloatingIpAssociate">
<a class="pdoc-member-name" href="/compute/floatingIpAssociate.ts#L10">class FloatingIpAssociate</a>
</h2>

Associate a floating IP to an instance. This can be used instead of the
`floating_ip` options in `openstack_compute_instance_v2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L48">constructor</a>
</h3>

```typescript
new FloatingIpAssociate(name: string, args: FloatingIpAssociateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FloatingIpAssociate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpAssociateState): FloatingIpAssociate
```


Get an existing FloatingIpAssociate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L26">property fixedIp</a>
</h3>

```typescript
public fixedIp: pulumi.Output<string | undefined>;
```


The specific IP address to direct traffic to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L30">property floatingIp</a>
</h3>

```typescript
public floatingIp: pulumi.Output<string>;
```


The floating IP to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L34">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The instance to associte the floating IP with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L41">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new floatingip_associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L48">property waitUntilAssociated</a>
</h3>

```typescript
public waitUntilAssociated: pulumi.Output<boolean | undefined>;
```


In cases where the OpenStack environment
does not automatically wait until the association has finished, set this
option to have Terraform poll the instance until the floating IP has been
associated. Defaults to false.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="/compute/instance.ts#L9">class Instance</a>
</h2>

Manages a V2 VM instance resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L152">constructor</a>
</h3>

```typescript
new Instance(name: string, args?: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/instance.ts#L26">property accessIpV4</a>
</h3>

```typescript
public accessIpV4: pulumi.Output<string>;
```


The first detected Fixed IPv4 address _or_ the
Floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L30">property accessIpV6</a>
</h3>

```typescript
public accessIpV6: pulumi.Output<string>;
```


The first detected Fixed IPv6 address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L35">property adminPass</a>
</h3>

```typescript
public adminPass: pulumi.Output<string | undefined>;
```


The administrative password to assign to the server.
Changing this changes the root password on the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L40">property allMetadata</a>
</h3>

```typescript
public allMetadata: pulumi.Output<{ ... }>;
```


Contains all instance metadata, even metadata not set
by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L45">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


The availability zone in which to create
the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L54">property blockDevices</a>
</h3>

```typescript
public blockDevices: pulumi.Output<{ ... }[] | undefined>;
```


Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following [reference](http://docs.openstack.org/developer/nova/block_device_mapping.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L59">property configDrive</a>
</h3>

```typescript
public configDrive: pulumi.Output<boolean | undefined>;
```


Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L64">property flavorId</a>
</h3>

```typescript
public flavorId: pulumi.Output<string>;
```


The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L69">property flavorName</a>
</h3>

```typescript
public flavorName: pulumi.Output<string>;
```


The name of the
desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L75">property forceDelete</a>
</h3>

```typescript
public forceDelete: pulumi.Output<boolean | undefined>;
```


Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L81">property imageId</a>
</h3>

```typescript
public imageId: pulumi.Output<string>;
```


(Optional; Required if `image_name` is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L87">property imageName</a>
</h3>

```typescript
public imageName: pulumi.Output<string>;
```


(Optional; Required if `image_id` is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L93">property keyPair</a>
</h3>

```typescript
public keyPair: pulumi.Output<string | undefined>;
```


The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L98">property metadata</a>
</h3>

```typescript
public metadata: pulumi.Output<{ ... } | undefined>;
```


Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L103">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The human-readable
name of the network. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L109">property networks</a>
</h3>

```typescript
public networks: pulumi.Output<{ ... }[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L115">property personalities</a>
</h3>

```typescript
public personalities: pulumi.Output<{ ... }[] | undefined>;
```


Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L122">property powerState</a>
</h3>

```typescript
public powerState: pulumi.Output<string | undefined>;
```


Provide the VM state. Only 'active' and 'shutoff'
are supported values. *Note*: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L128">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the server instance. If
omitted, the `region` argument of the provider is used. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L133">property schedulerHints</a>
</h3>

```typescript
public schedulerHints: pulumi.Output<{ ... }[] | undefined>;
```


Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L141">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[]>;
```


An array of one or more security group names
to associate with the server. Changing this results in adding/removing
security groups from the existing server. *Note*: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L147">property stopBeforeDestroy</a>
</h3>

```typescript
public stopBeforeDestroy: pulumi.Output<boolean | undefined>;
```


Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L152">property userData</a>
</h3>

```typescript
public userData: pulumi.Output<string | undefined>;
```


The user data to provide when launching the instance.
Changing this creates a new server.

<h2 class="pdoc-module-header" id="Keypair">
<a class="pdoc-member-name" href="/compute/keypair.ts#L15">class Keypair</a>
</h2>

Manages a V2 keypair resource within OpenStack.

~> **Important Security Notice** The private key generated by this resource will
be stored *unencrypted* in your Terraform state file. **Use of this resource
for production deployments is *not* recommended**. Instead, generate
a private key file outside of Terraform and distribute it securely
to the system where Terraform will be run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L59">constructor</a>
</h3>

```typescript
new Keypair(name: string, args?: KeypairArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Keypair resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeypairState): Keypair
```


Get an existing Keypair resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/keypair.ts#L31">property fingerprint</a>
</h3>

```typescript
public fingerprint: pulumi.Output<string>;
```


The fingerprint of the public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the keypair. Changing this creates a new
keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L40">property privateKey</a>
</h3>

```typescript
public privateKey: pulumi.Output<string>;
```


The generated private key when no public key is specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L48">property publicKey</a>
</h3>

```typescript
public publicKey: pulumi.Output<string>;
```


A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L55">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L59">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SecGroup">
<a class="pdoc-member-name" href="/compute/secGroup.ts#L15">class SecGroup</a>
</h2>

Manages a V2 security group resource within OpenStack.

Please note that managing security groups through the OpenStack Compute API
has been deprecated. Unless you are using an older OpenStack environment, it is
recommended to use the [`openstack_networking_secgroup_v2`](networking_secgroup_v2.html)
and [`openstack_networking_secgroup_rule_v2`](networking_secgroup_rule_v2.html)
resources instead, which uses the OpenStack Networking API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L51">constructor</a>
</h3>

```typescript
new SecGroup(name: string, args: SecGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SecGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecGroupState): SecGroup
```


Get an existing SecGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/compute/secGroup.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A description for the security group. Changing this
updates the `description` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the security group. Changing this
updates the `name` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L44">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L51">property rules</a>
</h3>

```typescript
public rules: pulumi.Output<{ ... }[]>;
```


A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ServerGroup">
<a class="pdoc-member-name" href="/compute/serverGroup.ts#L9">class ServerGroup</a>
</h2>

Manages a V2 Server Group resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L47">constructor</a>
</h3>

```typescript
new ServerGroup(name: string, args?: ServerGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ServerGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerGroupState): ServerGroup
```


Get an existing ServerGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L25">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```


The instances that are part of this server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the server group. Changing this creates
a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L37">property policies</a>
</h3>

```typescript
public policies: pulumi.Output<string[] | undefined>;
```


The set of policies for the server group. Only two
two policies are available right now, and both are mutually exclusive. See
the Policies section for more information. Changing this creates a new
server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L43">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used. Changing
this creates a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L47">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="VolumeAttach">
<a class="pdoc-member-name" href="/compute/volumeAttach.ts#L10">class VolumeAttach</a>
</h2>

Attaches a Block Storage Volume to an Instance using the OpenStack
Compute (Nova) v2 API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L46">constructor</a>
</h3>

```typescript
new VolumeAttach(name: string, args: VolumeAttachArgs, opts?: pulumi.CustomResourceOptions)
```


Create a VolumeAttach resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L31">property device</a>
</h3>

```typescript
public device: pulumi.Output<string>;
```


The device of the volume attachment (ex: `/dev/vdc`).
_NOTE_: Being able to specify a device is dependent upon the hypervisor in
use. There is a chance that the device specified in Terraform will not be
the same device the hypervisor chose. If this happens, Terraform will wish
to update the device upon subsequent applying which will cause the volume
to be detached and reattached indefinitely. Please use with caution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L35">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The ID of the Instance to attach the Volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L42">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
`region` argument of the provider is used. Changing this creates a
new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L46">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


The ID of the Volume to attach to an Instance.

<h2 class="pdoc-module-header" id="getFlavor">
<a class="pdoc-member-name" href="/compute/getFlavor.ts#L9">function getFlavor</a>
</h2>

```typescript
getFlavor(args?: GetFlavorArgs, opts?: pulumi.InvokeOptions): Promise<GetFlavorResult>
```


Use this data source to get the ID of an available OpenStack flavor.

<h2 class="pdoc-module-header" id="getKeypair">
<a class="pdoc-member-name" href="/compute/getKeypair.ts#L9">function getKeypair</a>
</h2>

```typescript
getKeypair(args: GetKeypairArgs, opts?: pulumi.InvokeOptions): Promise<GetKeypairResult>
```


Use this data source to get the ID and public key of an OpenStack keypair.

<h2 class="pdoc-module-header" id="FlavorArgs">
<a class="pdoc-member-name" href="/compute/flavor.ts#L174">interface FlavorArgs</a>
</h2>

The set of arguments for constructing a Flavor resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L179">property disk</a>
</h3>

```typescript
disk: pulumi.Input<number>;
```


The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L180">property ephemeral</a>
</h3>

```typescript
ephemeral?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L184">property extraSpecs</a>
</h3>

```typescript
extraSpecs?: pulumi.Input<{ ... }>;
```


Key/Value pairs of metadata for the flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L189">property isPublic</a>
</h3>

```typescript
isPublic?: pulumi.Input<boolean>;
```


Whether the flavor is public. Changing this creates
a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the flavor. Changing this creates a new
flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L199">property ram</a>
</h3>

```typescript
ram: pulumi.Input<number>;
```


The amount of RAM to use, in megabytes. Changing this
creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L206">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L211">property rxTxFactor</a>
</h3>

```typescript
rxTxFactor?: pulumi.Input<number>;
```


RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L216">property swap</a>
</h3>

```typescript
swap?: pulumi.Input<number>;
```


The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L221">property vcpus</a>
</h3>

```typescript
vcpus: pulumi.Input<number>;
```


The number of virtual CPUs to use. Changing this creates
a new flavor.

<h2 class="pdoc-module-header" id="FlavorState">
<a class="pdoc-member-name" href="/compute/flavor.ts#L121">interface FlavorState</a>
</h2>

Input properties used for looking up and filtering Flavor resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L126">property disk</a>
</h3>

```typescript
disk?: pulumi.Input<number>;
```


The amount of disk space in gigabytes to use for the root
(/) partition. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L127">property ephemeral</a>
</h3>

```typescript
ephemeral?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L131">property extraSpecs</a>
</h3>

```typescript
extraSpecs?: pulumi.Input<{ ... }>;
```


Key/Value pairs of metadata for the flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L136">property isPublic</a>
</h3>

```typescript
isPublic?: pulumi.Input<boolean>;
```


Whether the flavor is public. Changing this creates
a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the flavor. Changing this creates a new
flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L146">property ram</a>
</h3>

```typescript
ram?: pulumi.Input<number>;
```


The amount of RAM to use, in megabytes. Changing this
creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L153">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Flavors are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L158">property rxTxFactor</a>
</h3>

```typescript
rxTxFactor?: pulumi.Input<number>;
```


RX/TX bandwith factor. The default is 1. Changing
this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L163">property swap</a>
</h3>

```typescript
swap?: pulumi.Input<number>;
```


The amount of disk space in megabytes to use. If
unspecified, the default is 0. Changing this creates a new flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/flavor.ts#L168">property vcpus</a>
</h3>

```typescript
vcpus?: pulumi.Input<number>;
```


The number of virtual CPUs to use. Changing this creates
a new flavor.

<h2 class="pdoc-module-header" id="FloatingIPArgs">
<a class="pdoc-member-name" href="/compute/floatingIP.ts#L120">interface FloatingIPArgs</a>
</h2>

The set of arguments for constructing a FloatingIP resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L125">property pool</a>
</h3>

```typescript
pool: pulumi.Input<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L133">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).

<h2 class="pdoc-module-header" id="FloatingIPState">
<a class="pdoc-member-name" href="/compute/floatingIP.ts#L89">interface FloatingIPState</a>
</h2>

Input properties used for looking up and filtering FloatingIP resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L93">property address</a>
</h3>

```typescript
address?: pulumi.Input<string>;
```


The actual floating IP address itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L97">property fixedIp</a>
</h3>

```typescript
fixedIp?: pulumi.Input<string>;
```


The fixed IP address corresponding to the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L101">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


UUID of the compute instance associated with the floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L106">property pool</a>
</h3>

```typescript
pool?: pulumi.Input<string>;
```


The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIP.ts#L114">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).

<h2 class="pdoc-module-header" id="FloatingIpAssociateArgs">
<a class="pdoc-member-name" href="/compute/floatingIpAssociate.ts#L120">interface FloatingIpAssociateArgs</a>
</h2>

The set of arguments for constructing a FloatingIpAssociate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L124">property fixedIp</a>
</h3>

```typescript
fixedIp?: pulumi.Input<string>;
```


The specific IP address to direct traffic to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L128">property floatingIp</a>
</h3>

```typescript
floatingIp: pulumi.Input<string>;
```


The floating IP to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L132">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


The instance to associte the floating IP with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L139">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new floatingip_associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L146">property waitUntilAssociated</a>
</h3>

```typescript
waitUntilAssociated?: pulumi.Input<boolean>;
```


In cases where the OpenStack environment
does not automatically wait until the association has finished, set this
option to have Terraform poll the instance until the floating IP has been
associated. Defaults to false.

<h2 class="pdoc-module-header" id="FloatingIpAssociateState">
<a class="pdoc-member-name" href="/compute/floatingIpAssociate.ts#L88">interface FloatingIpAssociateState</a>
</h2>

Input properties used for looking up and filtering FloatingIpAssociate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L92">property fixedIp</a>
</h3>

```typescript
fixedIp?: pulumi.Input<string>;
```


The specific IP address to direct traffic to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L96">property floatingIp</a>
</h3>

```typescript
floatingIp?: pulumi.Input<string>;
```


The floating IP to associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L100">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The instance to associte the floating IP with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L107">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new floatingip_associate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/floatingIpAssociate.ts#L114">property waitUntilAssociated</a>
</h3>

```typescript
waitUntilAssociated?: pulumi.Input<boolean>;
```


In cases where the OpenStack environment
does not automatically wait until the association has finished, set this
option to have Terraform poll the instance until the floating IP has been
associated. Defaults to false.

<h2 class="pdoc-module-header" id="GetFlavorArgs">
<a class="pdoc-member-name" href="/compute/getFlavor.ts#L27">interface GetFlavorArgs</a>
</h2>

A collection of arguments for invoking getFlavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L31">property disk</a>
</h3>

```typescript
disk?: number;
```


The exact amount of disk (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L35">property minDisk</a>
</h3>

```typescript
minDisk?: number;
```


The minimum amount of disk (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L39">property minRam</a>
</h3>

```typescript
minRam?: number;
```


The minimum amount of RAM (in megabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L43">property name</a>
</h3>

```typescript
name?: string;
```


The name of the flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L47">property ram</a>
</h3>

```typescript
ram?: number;
```


The exact amount of RAM (in megabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L52">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L56">property rxTxFactor</a>
</h3>

```typescript
rxTxFactor?: number;
```


The `rx_tx_factor` of the flavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L60">property swap</a>
</h3>

```typescript
swap?: number;
```


The amount of swap (in gigabytes).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L64">property vcpus</a>
</h3>

```typescript
vcpus?: number;
```


The amount of VCPUs.

<h2 class="pdoc-module-header" id="GetFlavorResult">
<a class="pdoc-member-name" href="/compute/getFlavor.ts#L70">interface GetFlavorResult</a>
</h2>

A collection of values returned by getFlavor.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L79">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L74">property isPublic</a>
</h3>

```typescript
isPublic: boolean;
```


Whether the flavor is public or private.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getFlavor.ts#L75">property region</a>
</h3>

```typescript
region: string;
```

<h2 class="pdoc-module-header" id="GetKeypairArgs">
<a class="pdoc-member-name" href="/compute/getKeypair.ts#L19">interface GetKeypairArgs</a>
</h2>

A collection of arguments for invoking getKeypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getKeypair.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


The unique name of the keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getKeypair.ts#L28">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used.

<h2 class="pdoc-module-header" id="GetKeypairResult">
<a class="pdoc-member-name" href="/compute/getKeypair.ts#L34">interface GetKeypairResult</a>
</h2>

A collection of values returned by getKeypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getKeypair.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getKeypair.ts#L38">property publicKey</a>
</h3>

```typescript
publicKey: string;
```


The OpenSSH-formatted public key of the keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/getKeypair.ts#L42">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="/compute/instance.ts#L359">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L364">property accessIpV4</a>
</h3>

```typescript
accessIpV4?: pulumi.Input<string>;
```


The first detected Fixed IPv4 address _or_ the
Floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L368">property accessIpV6</a>
</h3>

```typescript
accessIpV6?: pulumi.Input<string>;
```


The first detected Fixed IPv6 address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L373">property adminPass</a>
</h3>

```typescript
adminPass?: pulumi.Input<string>;
```


The administrative password to assign to the server.
Changing this changes the root password on the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L378">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone in which to create
the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L387">property blockDevices</a>
</h3>

```typescript
blockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following [reference](http://docs.openstack.org/developer/nova/block_device_mapping.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L392">property configDrive</a>
</h3>

```typescript
configDrive?: pulumi.Input<boolean>;
```


Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L397">property flavorId</a>
</h3>

```typescript
flavorId?: pulumi.Input<string>;
```


The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L402">property flavorName</a>
</h3>

```typescript
flavorName?: pulumi.Input<string>;
```


The name of the
desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L408">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L414">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


(Optional; Required if `image_name` is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L420">property imageName</a>
</h3>

```typescript
imageName?: pulumi.Input<string>;
```


(Optional; Required if `image_id` is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L426">property keyPair</a>
</h3>

```typescript
keyPair?: pulumi.Input<string>;
```


The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L431">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L436">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The human-readable
name of the network. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L442">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L448">property personalities</a>
</h3>

```typescript
personalities?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L455">property powerState</a>
</h3>

```typescript
powerState?: pulumi.Input<string>;
```


Provide the VM state. Only 'active' and 'shutoff'
are supported values. *Note*: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L461">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the server instance. If
omitted, the `region` argument of the provider is used. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L466">property schedulerHints</a>
</h3>

```typescript
schedulerHints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L474">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more security group names
to associate with the server. Changing this results in adding/removing
security groups from the existing server. *Note*: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L480">property stopBeforeDestroy</a>
</h3>

```typescript
stopBeforeDestroy?: pulumi.Input<boolean>;
```


Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L485">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance.
Changing this creates a new server.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="/compute/instance.ts#L222">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L227">property accessIpV4</a>
</h3>

```typescript
accessIpV4?: pulumi.Input<string>;
```


The first detected Fixed IPv4 address _or_ the
Floating IP.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L231">property accessIpV6</a>
</h3>

```typescript
accessIpV6?: pulumi.Input<string>;
```


The first detected Fixed IPv6 address.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L236">property adminPass</a>
</h3>

```typescript
adminPass?: pulumi.Input<string>;
```


The administrative password to assign to the server.
Changing this changes the root password on the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L241">property allMetadata</a>
</h3>

```typescript
allMetadata?: pulumi.Input<{ ... }>;
```


Contains all instance metadata, even metadata not set
by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L246">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


The availability zone in which to create
the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L255">property blockDevices</a>
</h3>

```typescript
blockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following [reference](http://docs.openstack.org/developer/nova/block_device_mapping.html)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L260">property configDrive</a>
</h3>

```typescript
configDrive?: pulumi.Input<boolean>;
```


Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L265">property flavorId</a>
</h3>

```typescript
flavorId?: pulumi.Input<string>;
```


The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L270">property flavorName</a>
</h3>

```typescript
flavorName?: pulumi.Input<string>;
```


The name of the
desired flavor for the server. Changing this resizes the existing server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L276">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


Whether to force the OpenStack instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L282">property imageId</a>
</h3>

```typescript
imageId?: pulumi.Input<string>;
```


(Optional; Required if `image_name` is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L288">property imageName</a>
</h3>

```typescript
imageName?: pulumi.Input<string>;
```


(Optional; Required if `image_id` is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L294">property keyPair</a>
</h3>

```typescript
keyPair?: pulumi.Input<string>;
```


The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L299">property metadata</a>
</h3>

```typescript
metadata?: pulumi.Input<{ ... }>;
```


Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L304">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The human-readable
name of the network. Changing this creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L310">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L316">property personalities</a>
</h3>

```typescript
personalities?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L323">property powerState</a>
</h3>

```typescript
powerState?: pulumi.Input<string>;
```


Provide the VM state. Only 'active' and 'shutoff'
are supported values. *Note*: If the initial power_state is the shutoff
the VM will be stopped immediately after build and the provisioners like
remote-exec or files are not supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L329">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the server instance. If
omitted, the `region` argument of the provider is used. Changing this
creates a new server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L334">property schedulerHints</a>
</h3>

```typescript
schedulerHints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L342">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of one or more security group names
to associate with the server. Changing this results in adding/removing
security groups from the existing server. *Note*: When attaching the
instance to networks using Ports, place the security groups on the Port
and not the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L348">property stopBeforeDestroy</a>
</h3>

```typescript
stopBeforeDestroy?: pulumi.Input<boolean>;
```


Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/instance.ts#L353">property userData</a>
</h3>

```typescript
userData?: pulumi.Input<string>;
```


The user data to provide when launching the instance.
Changing this creates a new server.

<h2 class="pdoc-module-header" id="KeypairArgs">
<a class="pdoc-member-name" href="/compute/keypair.ts#L133">interface KeypairArgs</a>
</h2>

The set of arguments for constructing a Keypair resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the keypair. Changing this creates a new
keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L146">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L153">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L157">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="KeypairState">
<a class="pdoc-member-name" href="/compute/keypair.ts#L95">interface KeypairState</a>
</h2>

Input properties used for looking up and filtering Keypair resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L99">property fingerprint</a>
</h3>

```typescript
fingerprint?: pulumi.Input<string>;
```


The fingerprint of the public key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the keypair. Changing this creates a new
keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L108">property privateKey</a>
</h3>

```typescript
privateKey?: pulumi.Input<string>;
```


The generated private key when no public key is specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L116">property publicKey</a>
</h3>

```typescript
publicKey?: pulumi.Input<string>;
```


A pregenerated OpenSSH-formatted public key.
Changing this creates a new keypair. If a public key is not specified, then
a public/private key pair will be automatically generated. If a pair is
created, then destroying this resource means you will lose access to that
keypair forever.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L123">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new keypair.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/keypair.ts#L127">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="SecGroupArgs">
<a class="pdoc-member-name" href="/compute/secGroup.ts#L116">interface SecGroupArgs</a>
</h2>

The set of arguments for constructing a SecGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L121">property description</a>
</h3>

```typescript
description: pulumi.Input<string>;
```


A description for the security group. Changing this
updates the `description` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the security group. Changing this
updates the `name` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L133">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L140">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.

<h2 class="pdoc-module-header" id="SecGroupState">
<a class="pdoc-member-name" href="/compute/secGroup.ts#L86">interface SecGroupState</a>
</h2>

Input properties used for looking up and filtering SecGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L91">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the security group. Changing this
updates the `description` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the security group. Changing this
updates the `name` of an existing security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L103">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a security group. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/secGroup.ts#L110">property rules</a>
</h3>

```typescript
rules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A rule describing how the security group operates. The
rule object structure is documented below. Changing this updates the
security group rules. As shown in the example above, multiple rule blocks
may be used.

<h2 class="pdoc-module-header" id="ServerGroupArgs">
<a class="pdoc-member-name" href="/compute/serverGroup.ts#L113">interface ServerGroupArgs</a>
</h2>

The set of arguments for constructing a ServerGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the server group. Changing this creates
a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L125">property policies</a>
</h3>

```typescript
policies?: pulumi.Input<pulumi.Input<string>[]>;
```


The set of policies for the server group. Only two
two policies are available right now, and both are mutually exclusive. See
the Policies section for more information. Changing this creates a new
server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L131">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used. Changing
this creates a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L135">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="ServerGroupState">
<a class="pdoc-member-name" href="/compute/serverGroup.ts#L81">interface ServerGroupState</a>
</h2>

Input properties used for looking up and filtering ServerGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L85">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```


The instances that are part of this server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L90">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the server group. Changing this creates
a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L97">property policies</a>
</h3>

```typescript
policies?: pulumi.Input<pulumi.Input<string>[]>;
```


The set of policies for the server group. Only two
two policies are available right now, and both are mutually exclusive. See
the Policies section for more information. Changing this creates a new
server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L103">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
If omitted, the `region` argument of the provider is used. Changing
this creates a new server group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/serverGroup.ts#L107">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options.

<h2 class="pdoc-module-header" id="VolumeAttachArgs">
<a class="pdoc-member-name" href="/compute/volumeAttach.ts#L114">interface VolumeAttachArgs</a>
</h2>

The set of arguments for constructing a VolumeAttach resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L123">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device of the volume attachment (ex: `/dev/vdc`).
_NOTE_: Being able to specify a device is dependent upon the hypervisor in
use. There is a chance that the device specified in Terraform will not be
the same device the hypervisor chose. If this happens, Terraform will wish
to update the device upon subsequent applying which will cause the volume
to be detached and reattached indefinitely. Please use with caution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L127">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


The ID of the Instance to attach the Volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L134">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
`region` argument of the provider is used. Changing this creates a
new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L138">property volumeId</a>
</h3>

```typescript
volumeId: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

<h2 class="pdoc-module-header" id="VolumeAttachState">
<a class="pdoc-member-name" href="/compute/volumeAttach.ts#L84">interface VolumeAttachState</a>
</h2>

Input properties used for looking up and filtering VolumeAttach resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L93">property device</a>
</h3>

```typescript
device?: pulumi.Input<string>;
```


The device of the volume attachment (ex: `/dev/vdc`).
_NOTE_: Being able to specify a device is dependent upon the hypervisor in
use. There is a chance that the device specified in Terraform will not be
the same device the hypervisor chose. If this happens, Terraform will wish
to update the device upon subsequent applying which will cause the volume
to be detached and reattached indefinitely. Please use with caution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L97">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The ID of the Instance to attach the Volume to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L104">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
A Compute client is needed to create a volume attachment. If omitted, the
`region` argument of the provider is used. Changing this creates a
new volume attachment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/compute/volumeAttach.ts#L108">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


The ID of the Volume to attach to an Instance.

