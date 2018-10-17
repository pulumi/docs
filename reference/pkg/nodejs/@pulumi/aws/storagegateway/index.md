---
title: Module storagegateway
---

<a href="../index.html">@pulumi/aws</a> &gt; storagegateway

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cache">class Cache</a>
* <a href="#CachesIscsiVolume">class CachesIscsiVolume</a>
* <a href="#Gateway">class Gateway</a>
* <a href="#NfsFileShare">class NfsFileShare</a>
* <a href="#SmbFileShare">class SmbFileShare</a>
* <a href="#UploadBuffer">class UploadBuffer</a>
* <a href="#WorkingStorage">class WorkingStorage</a>
* <a href="#getLocalDisk">function getLocalDisk</a>
* <a href="#CacheArgs">interface CacheArgs</a>
* <a href="#CacheState">interface CacheState</a>
* <a href="#CachesIscsiVolumeArgs">interface CachesIscsiVolumeArgs</a>
* <a href="#CachesIscsiVolumeState">interface CachesIscsiVolumeState</a>
* <a href="#GatewayArgs">interface GatewayArgs</a>
* <a href="#GatewayState">interface GatewayState</a>
* <a href="#GetLocalDiskArgs">interface GetLocalDiskArgs</a>
* <a href="#GetLocalDiskResult">interface GetLocalDiskResult</a>
* <a href="#NfsFileShareArgs">interface NfsFileShareArgs</a>
* <a href="#NfsFileShareState">interface NfsFileShareState</a>
* <a href="#SmbFileShareArgs">interface SmbFileShareArgs</a>
* <a href="#SmbFileShareState">interface SmbFileShareState</a>
* <a href="#UploadBufferArgs">interface UploadBufferArgs</a>
* <a href="#UploadBufferState">interface UploadBufferState</a>
* <a href="#WorkingStorageArgs">interface WorkingStorageArgs</a>
* <a href="#WorkingStorageState">interface WorkingStorageState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts">storagegateway/cache.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts">storagegateway/cachesIscsiVolume.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts">storagegateway/gateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts">storagegateway/getLocalDisk.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts">storagegateway/nfsFileShare.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts">storagegateway/smbFileShare.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts">storagegateway/uploadBuffer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts">storagegateway/workingStorage.ts</a> 


<h2 class="pdoc-module-header" id="Cache">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L12">class Cache</a>
</h2>

Manages an AWS Storage Gateway cache.

~> **NOTE:** The Storage Gateway API provides no method to remove a cache disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L32">constructor</a>
</h3>

```typescript
new Cache(name: string, args: CacheArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cache resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CacheState): Cache
```


Get an existing Cache resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L28">property diskId</a>
</h3>

```typescript
public diskId: pulumi.Output<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L32">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CachesIscsiVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L14">class CachesIscsiVolume</a>
</h2>

Manages an AWS Storage Gateway cached iSCSI volume.

~> **NOTE:** The gateway must have cache added (e.g. via the [`aws_storagegateway_cache`](https://www.terraform.io/docs/providers/aws/r/storagegateway_cache.html) resource) before creating volumes otherwise the Storage Gateway API will return an error.

~> **NOTE:** The gateway must have an upload buffer added (e.g. via the [`aws_storagegateway_upload_buffer`](https://www.terraform.io/docs/providers/aws/r/storagegateway_upload_buffer.html) resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as `UPLOAD BUFFER NOT CONFIGURED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L78">constructor</a>
</h3>

```typescript
new CachesIscsiVolume(name: string, args: CachesIscsiVolumeArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CachesIscsiVolume resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CachesIscsiVolumeState): CachesIscsiVolume
```


Get an existing CachesIscsiVolume resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L34">property chapEnabled</a>
</h3>

```typescript
public chapEnabled: pulumi.Output<boolean>;
```


Whether mutual CHAP is enabled for the iSCSI target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L38">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L42">property lunNumber</a>
</h3>

```typescript
public lunNumber: pulumi.Output<number>;
```


Logical disk number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L46">property networkInterfaceId</a>
</h3>

```typescript
public networkInterfaceId: pulumi.Output<string>;
```


The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L50">property networkInterfacePort</a>
</h3>

```typescript
public networkInterfacePort: pulumi.Output<number>;
```


The port used to communicate with iSCSI targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L54">property snapshotId</a>
</h3>

```typescript
public snapshotId: pulumi.Output<string | undefined>;
```


The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L58">property sourceVolumeArn</a>
</h3>

```typescript
public sourceVolumeArn: pulumi.Output<string | undefined>;
```


The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L62">property targetArn</a>
</h3>

```typescript
public targetArn: pulumi.Output<string>;
```


Target Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L66">property targetName</a>
</h3>

```typescript
public targetName: pulumi.Output<string>;
```


The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L70">property volumeArn</a>
</h3>

```typescript
public volumeArn: pulumi.Output<string>;
```


Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L74">property volumeId</a>
</h3>

```typescript
public volumeId: pulumi.Output<string>;
```


Volume ID, e.g. `vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L78">property volumeSizeInBytes</a>
</h3>

```typescript
public volumeSizeInBytes: pulumi.Output<number>;
```


The size of the volume in bytes.

<h2 class="pdoc-module-header" id="Gateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L12">class Gateway</a>
</h2>

Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.

~> NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving `The specified gateway is not connected` errors during resource creation (gateway activation), ensure your gateway instance meets the [Storage Gateway requirements](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L65">constructor</a>
</h3>

```typescript
new Gateway(name: string, args: GatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Gateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayState): Gateway
```


Get an existing Gateway resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L28">property activationKey</a>
</h3>

```typescript
public activationKey: pulumi.Output<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L32">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L36">property gatewayId</a>
</h3>

```typescript
public gatewayId: pulumi.Output<string>;
```


Identifier of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L40">property gatewayIpAddress</a>
</h3>

```typescript
public gatewayIpAddress: pulumi.Output<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L44">property gatewayName</a>
</h3>

```typescript
public gatewayName: pulumi.Output<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L48">property gatewayTimezone</a>
</h3>

```typescript
public gatewayTimezone: pulumi.Output<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L52">property gatewayType</a>
</h3>

```typescript
public gatewayType: pulumi.Output<string | undefined>;
```


Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L53">property mediumChangerType</a>
</h3>

```typescript
public mediumChangerType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L57">property smbActiveDirectorySettings</a>
</h3>

```typescript
public smbActiveDirectorySettings: pulumi.Output<{ ... } | undefined>;
```


Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L61">property smbGuestPassword</a>
</h3>

```typescript
public smbGuestPassword: pulumi.Output<string | undefined>;
```


Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. Terraform can only detect drift of the existence of a guest password, not its actual value from the gateway. Terraform can however update the password with changing the argument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L65">property tapeDriveType</a>
</h3>

```typescript
public tapeDriveType: pulumi.Output<string | undefined>;
```


Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NfsFileShare">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L10">class NfsFileShare</a>
</h2>

Manages an AWS Storage Gateway NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L82">constructor</a>
</h3>

```typescript
new NfsFileShare(name: string, args: NfsFileShareArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NfsFileShare resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NfsFileShareState): NfsFileShare
```


Get an existing NfsFileShare resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L30">property clientLists</a>
</h3>

```typescript
public clientLists: pulumi.Output<string[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L34">property defaultStorageClass</a>
</h3>

```typescript
public defaultStorageClass: pulumi.Output<string | undefined>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L38">property fileshareId</a>
</h3>

```typescript
public fileshareId: pulumi.Output<string>;
```


ID of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L42">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L46">property guessMimeTypeEnabled</a>
</h3>

```typescript
public guessMimeTypeEnabled: pulumi.Output<boolean | undefined>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L50">property kmsEncrypted</a>
</h3>

```typescript
public kmsEncrypted: pulumi.Output<boolean | undefined>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L54">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string | undefined>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L58">property locationArn</a>
</h3>

```typescript
public locationArn: pulumi.Output<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L62">property nfsFileShareDefaults</a>
</h3>

```typescript
public nfsFileShareDefaults: pulumi.Output<{ ... } | undefined>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L66">property objectAcl</a>
</h3>

```typescript
public objectAcl: pulumi.Output<string | undefined>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L70">property readOnly</a>
</h3>

```typescript
public readOnly: pulumi.Output<boolean | undefined>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L74">property requesterPays</a>
</h3>

```typescript
public requesterPays: pulumi.Output<boolean | undefined>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L78">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L82">property squash</a>
</h3>

```typescript
public squash: pulumi.Output<string | undefined>;
```


Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SmbFileShare">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L10">class SmbFileShare</a>
</h2>

Manages an AWS Storage Gateway SMB File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L82">constructor</a>
</h3>

```typescript
new SmbFileShare(name: string, args: SmbFileShareArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SmbFileShare resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmbFileShareState): SmbFileShare
```


Get an existing SmbFileShare resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the SMB File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L30">property authentication</a>
</h3>

```typescript
public authentication: pulumi.Output<string | undefined>;
```


The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L34">property defaultStorageClass</a>
</h3>

```typescript
public defaultStorageClass: pulumi.Output<string | undefined>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L38">property fileshareId</a>
</h3>

```typescript
public fileshareId: pulumi.Output<string>;
```


ID of the SMB File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L42">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L46">property guessMimeTypeEnabled</a>
</h3>

```typescript
public guessMimeTypeEnabled: pulumi.Output<boolean | undefined>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L50">property invalidUserLists</a>
</h3>

```typescript
public invalidUserLists: pulumi.Output<string[] | undefined>;
```


A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L54">property kmsEncrypted</a>
</h3>

```typescript
public kmsEncrypted: pulumi.Output<boolean | undefined>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L58">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string | undefined>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L62">property locationArn</a>
</h3>

```typescript
public locationArn: pulumi.Output<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L66">property objectAcl</a>
</h3>

```typescript
public objectAcl: pulumi.Output<string | undefined>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L70">property readOnly</a>
</h3>

```typescript
public readOnly: pulumi.Output<boolean | undefined>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L74">property requesterPays</a>
</h3>

```typescript
public requesterPays: pulumi.Output<boolean | undefined>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L78">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L82">property validUserLists</a>
</h3>

```typescript
public validUserLists: pulumi.Output<string[] | undefined>;
```


A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h2 class="pdoc-module-header" id="UploadBuffer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L12">class UploadBuffer</a>
</h2>

Manages an AWS Storage Gateway upload buffer.

~> **NOTE:** The Storage Gateway API provides no method to remove an upload buffer disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L32">constructor</a>
</h3>

```typescript
new UploadBuffer(name: string, args: UploadBufferArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UploadBuffer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UploadBufferState): UploadBuffer
```


Get an existing UploadBuffer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L28">property diskId</a>
</h3>

```typescript
public diskId: pulumi.Output<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L32">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="WorkingStorage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L12">class WorkingStorage</a>
</h2>

Manages an AWS Storage Gateway working storage.

~> **NOTE:** The Storage Gateway API provides no method to remove a working storage disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L32">constructor</a>
</h3>

```typescript
new WorkingStorage(name: string, args: WorkingStorageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a WorkingStorage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkingStorageState): WorkingStorage
```


Get an existing WorkingStorage resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L28">property diskId</a>
</h3>

```typescript
public diskId: pulumi.Output<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L32">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getLocalDisk">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L10">function getLocalDisk</a>
</h2>

```typescript
getLocalDisk(args: GetLocalDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetLocalDiskResult>
```


Retrieve information about a Storage Gateway local disk. The disk identifier is useful for adding the disk as a cache or upload buffer to a gateway.

<h2 class="pdoc-module-header" id="CacheArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L80">interface CacheArgs</a>
</h2>

The set of arguments for constructing a Cache resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L84">property diskId</a>
</h3>

```typescript
diskId: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L88">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="CacheState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L66">interface CacheState</a>
</h2>

Input properties used for looking up and filtering Cache resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L70">property diskId</a>
</h3>

```typescript
diskId?: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cache.ts#L74">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="CachesIscsiVolumeArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L198">interface CachesIscsiVolumeArgs</a>
</h2>

The set of arguments for constructing a CachesIscsiVolume resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L202">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L206">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId: pulumi.Input<string>;
```


The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L210">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L214">property sourceVolumeArn</a>
</h3>

```typescript
sourceVolumeArn?: pulumi.Input<string>;
```


The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L218">property targetName</a>
</h3>

```typescript
targetName: pulumi.Input<string>;
```


The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L222">property volumeSizeInBytes</a>
</h3>

```typescript
volumeSizeInBytes: pulumi.Input<number>;
```


The size of the volume in bytes.

<h2 class="pdoc-module-header" id="CachesIscsiVolumeState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L140">interface CachesIscsiVolumeState</a>
</h2>

Input properties used for looking up and filtering CachesIscsiVolume resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L144">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L148">property chapEnabled</a>
</h3>

```typescript
chapEnabled?: pulumi.Input<boolean>;
```


Whether mutual CHAP is enabled for the iSCSI target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L152">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L156">property lunNumber</a>
</h3>

```typescript
lunNumber?: pulumi.Input<number>;
```


Logical disk number.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L160">property networkInterfaceId</a>
</h3>

```typescript
networkInterfaceId?: pulumi.Input<string>;
```


The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L164">property networkInterfacePort</a>
</h3>

```typescript
networkInterfacePort?: pulumi.Input<number>;
```


The port used to communicate with iSCSI targets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L168">property snapshotId</a>
</h3>

```typescript
snapshotId?: pulumi.Input<string>;
```


The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L172">property sourceVolumeArn</a>
</h3>

```typescript
sourceVolumeArn?: pulumi.Input<string>;
```


The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L176">property targetArn</a>
</h3>

```typescript
targetArn?: pulumi.Input<string>;
```


Target Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L180">property targetName</a>
</h3>

```typescript
targetName?: pulumi.Input<string>;
```


The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L184">property volumeArn</a>
</h3>

```typescript
volumeArn?: pulumi.Input<string>;
```


Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L188">property volumeId</a>
</h3>

```typescript
volumeId?: pulumi.Input<string>;
```


Volume ID, e.g. `vol-12345678`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/cachesIscsiVolume.ts#L192">property volumeSizeInBytes</a>
</h3>

```typescript
volumeSizeInBytes?: pulumi.Input<number>;
```


The size of the volume in bytes.

<h2 class="pdoc-module-header" id="GatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L164">interface GatewayArgs</a>
</h2>

The set of arguments for constructing a Gateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L168">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L172">property gatewayIpAddress</a>
</h3>

```typescript
gatewayIpAddress?: pulumi.Input<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L176">property gatewayName</a>
</h3>

```typescript
gatewayName: pulumi.Input<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L180">property gatewayTimezone</a>
</h3>

```typescript
gatewayTimezone: pulumi.Input<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L184">property gatewayType</a>
</h3>

```typescript
gatewayType?: pulumi.Input<string>;
```


Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L185">property mediumChangerType</a>
</h3>

```typescript
mediumChangerType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L189">property smbActiveDirectorySettings</a>
</h3>

```typescript
smbActiveDirectorySettings?: pulumi.Input<{ ... }>;
```


Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L193">property smbGuestPassword</a>
</h3>

```typescript
smbGuestPassword?: pulumi.Input<string>;
```


Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. Terraform can only detect drift of the existence of a guest password, not its actual value from the gateway. Terraform can however update the password with changing the argument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L197">property tapeDriveType</a>
</h3>

```typescript
tapeDriveType?: pulumi.Input<string>;
```


Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

<h2 class="pdoc-module-header" id="GatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L117">interface GatewayState</a>
</h2>

Input properties used for looking up and filtering Gateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L121">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L125">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L129">property gatewayId</a>
</h3>

```typescript
gatewayId?: pulumi.Input<string>;
```


Identifier of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L133">property gatewayIpAddress</a>
</h3>

```typescript
gatewayIpAddress?: pulumi.Input<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L137">property gatewayName</a>
</h3>

```typescript
gatewayName?: pulumi.Input<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L141">property gatewayTimezone</a>
</h3>

```typescript
gatewayTimezone?: pulumi.Input<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L145">property gatewayType</a>
</h3>

```typescript
gatewayType?: pulumi.Input<string>;
```


Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L146">property mediumChangerType</a>
</h3>

```typescript
mediumChangerType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L150">property smbActiveDirectorySettings</a>
</h3>

```typescript
smbActiveDirectorySettings?: pulumi.Input<{ ... }>;
```


Nested argument with Active Directory domain join information for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `ActiveDirectory` authentication SMB file shares. More details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L154">property smbGuestPassword</a>
</h3>

```typescript
smbGuestPassword?: pulumi.Input<string>;
```


Guest password for Server Message Block (SMB) file shares. Only valid for `FILE_S3` gateway type. Must be set before creating `GuestAccess` authentication SMB file shares. Terraform can only detect drift of the existence of a guest password, not its actual value from the gateway. Terraform can however update the password with changing the argument.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L158">property tapeDriveType</a>
</h3>

```typescript
tapeDriveType?: pulumi.Input<string>;
```


Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

<h2 class="pdoc-module-header" id="GetLocalDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L21">interface GetLocalDiskArgs</a>
</h2>

A collection of arguments for invoking getLocalDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L25">property diskNode</a>
</h3>

```typescript
diskNode?: string;
```


The device node of the local disk to retrieve. For example, `/dev/sdb`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L29">property diskPath</a>
</h3>

```typescript
diskPath?: string;
```


The device path of the local disk to retrieve. For example, `/dev/xvdb` or `/dev/nvme1n1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L33">property gatewayArn</a>
</h3>

```typescript
gatewayArn: string;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="GetLocalDiskResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L39">interface GetLocalDiskResult</a>
</h2>

A collection of values returned by getLocalDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L43">property diskId</a>
</h3>

```typescript
diskId: string;
```


The disk identifier. e.g. `pci-0000:03:00.0-scsi-0:0:0:0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L47">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="NfsFileShareArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L214">interface NfsFileShareArgs</a>
</h2>

The set of arguments for constructing a NfsFileShare resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L218">property clientLists</a>
</h3>

```typescript
clientLists: pulumi.Input<pulumi.Input<string>[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L222">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L226">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L230">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L234">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L238">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L242">property locationArn</a>
</h3>

```typescript
locationArn: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L246">property nfsFileShareDefaults</a>
</h3>

```typescript
nfsFileShareDefaults?: pulumi.Input<{ ... }>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L250">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L254">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L258">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L262">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L266">property squash</a>
</h3>

```typescript
squash?: pulumi.Input<string>;
```


Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)

<h2 class="pdoc-module-header" id="NfsFileShareState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L148">interface NfsFileShareState</a>
</h2>

Input properties used for looking up and filtering NfsFileShare resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L152">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L156">property clientLists</a>
</h3>

```typescript
clientLists?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L160">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L164">property fileshareId</a>
</h3>

```typescript
fileshareId?: pulumi.Input<string>;
```


ID of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L168">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L172">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L176">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L180">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L184">property locationArn</a>
</h3>

```typescript
locationArn?: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L188">property nfsFileShareDefaults</a>
</h3>

```typescript
nfsFileShareDefaults?: pulumi.Input<{ ... }>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L192">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L196">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L200">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L204">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L208">property squash</a>
</h3>

```typescript
squash?: pulumi.Input<string>;
```


Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)

<h2 class="pdoc-module-header" id="SmbFileShareArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L211">interface SmbFileShareArgs</a>
</h2>

The set of arguments for constructing a SmbFileShare resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L215">property authentication</a>
</h3>

```typescript
authentication?: pulumi.Input<string>;
```


The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L219">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L223">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L227">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L231">property invalidUserLists</a>
</h3>

```typescript
invalidUserLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L235">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L239">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L243">property locationArn</a>
</h3>

```typescript
locationArn: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L247">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L251">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L255">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L259">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L263">property validUserLists</a>
</h3>

```typescript
validUserLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h2 class="pdoc-module-header" id="SmbFileShareState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L145">interface SmbFileShareState</a>
</h2>

Input properties used for looking up and filtering SmbFileShare resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L149">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the SMB File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L153">property authentication</a>
</h3>

```typescript
authentication?: pulumi.Input<string>;
```


The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L157">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L161">property fileshareId</a>
</h3>

```typescript
fileshareId?: pulumi.Input<string>;
```


ID of the SMB File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L165">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L169">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L173">property invalidUserLists</a>
</h3>

```typescript
invalidUserLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L177">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L181">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L185">property locationArn</a>
</h3>

```typescript
locationArn?: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L189">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L193">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L197">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L201">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/smbFileShare.ts#L205">property validUserLists</a>
</h3>

```typescript
validUserLists?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

<h2 class="pdoc-module-header" id="UploadBufferArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L80">interface UploadBufferArgs</a>
</h2>

The set of arguments for constructing a UploadBuffer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L84">property diskId</a>
</h3>

```typescript
diskId: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L88">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="UploadBufferState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L66">interface UploadBufferState</a>
</h2>

Input properties used for looking up and filtering UploadBuffer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L70">property diskId</a>
</h3>

```typescript
diskId?: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L74">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="WorkingStorageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L80">interface WorkingStorageArgs</a>
</h2>

The set of arguments for constructing a WorkingStorage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L84">property diskId</a>
</h3>

```typescript
diskId: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L88">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="WorkingStorageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L66">interface WorkingStorageState</a>
</h2>

Input properties used for looking up and filtering WorkingStorage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L70">property diskId</a>
</h3>

```typescript
diskId?: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L74">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

