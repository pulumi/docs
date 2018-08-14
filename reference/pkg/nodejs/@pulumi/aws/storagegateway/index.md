---
title: Module storagegateway
---

<a href="../index.html">@pulumi/aws</a> &gt; storagegateway

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Gateway">class Gateway</a>
* <a href="#NfsFileShare">class NfsFileShare</a>
* <a href="#UploadBuffer">class UploadBuffer</a>
* <a href="#WorkingStorage">class WorkingStorage</a>
* <a href="#getLocalDisk">function getLocalDisk</a>
* <a href="#GatewayArgs">interface GatewayArgs</a>
* <a href="#GatewayState">interface GatewayState</a>
* <a href="#GetLocalDiskArgs">interface GetLocalDiskArgs</a>
* <a href="#GetLocalDiskResult">interface GetLocalDiskResult</a>
* <a href="#NfsFileShareArgs">interface NfsFileShareArgs</a>
* <a href="#NfsFileShareState">interface NfsFileShareState</a>
* <a href="#UploadBufferArgs">interface UploadBufferArgs</a>
* <a href="#UploadBufferState">interface UploadBufferState</a>
* <a href="#WorkingStorageArgs">interface WorkingStorageArgs</a>
* <a href="#WorkingStorageState">interface WorkingStorageState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts">storagegateway/gateway.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts">storagegateway/getLocalDisk.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts">storagegateway/nfsFileShare.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts">storagegateway/uploadBuffer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts">storagegateway/workingStorage.ts</a> 


<h2 class="pdoc-module-header" id="Gateway">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L11">class Gateway</a>
</h2>

Manages an AWS Storage Gateway file, tape, or volume gateway in the provider region.

~> NOTE: The Storage Gateway API requires the gateway to be connected to properly return information after activation. If you are receiving `The specified gateway is not connected` errors during resource creation (gateway activation), ensure your gateway instance meets the [Storage Gateway requirements](https://docs.aws.amazon.com/storagegateway/latest/userguide/Requirements.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L56">constructor</a>
</h3>

```typescript
new Gateway(name: string, args: GatewayArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Gateway resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L27">property activationKey</a>
</h3>

```typescript
public activationKey: pulumi.Output<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L35">property gatewayId</a>
</h3>

```typescript
public gatewayId: pulumi.Output<string>;
```


Identifier of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L39">property gatewayIpAddress</a>
</h3>

```typescript
public gatewayIpAddress: pulumi.Output<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L43">property gatewayName</a>
</h3>

```typescript
public gatewayName: pulumi.Output<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L47">property gatewayTimezone</a>
</h3>

```typescript
public gatewayTimezone: pulumi.Output<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L51">property gatewayType</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L52">property mediumChangerType</a>
</h3>

```typescript
public mediumChangerType: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L56">property tapeDriveType</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L9">class NfsFileShare</a>
</h2>

Manages an AWS Storage Gateway NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L81">constructor</a>
</h3>

```typescript
new NfsFileShare(name: string, args: NfsFileShareArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NfsFileShare resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L29">property clientLists</a>
</h3>

```typescript
public clientLists: pulumi.Output<string[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L33">property defaultStorageClass</a>
</h3>

```typescript
public defaultStorageClass: pulumi.Output<string | undefined>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L37">property fileshareId</a>
</h3>

```typescript
public fileshareId: pulumi.Output<string>;
```


ID of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L41">property gatewayArn</a>
</h3>

```typescript
public gatewayArn: pulumi.Output<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L45">property guessMimeTypeEnabled</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L49">property kmsEncrypted</a>
</h3>

```typescript
public kmsEncrypted: pulumi.Output<boolean | undefined>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L53">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string | undefined>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L57">property locationArn</a>
</h3>

```typescript
public locationArn: pulumi.Output<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L61">property nfsFileShareDefaults</a>
</h3>

```typescript
public nfsFileShareDefaults: pulumi.Output<{ ... } | undefined>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L65">property objectAcl</a>
</h3>

```typescript
public objectAcl: pulumi.Output<string | undefined>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L69">property readOnly</a>
</h3>

```typescript
public readOnly: pulumi.Output<boolean | undefined>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L73">property requesterPays</a>
</h3>

```typescript
public requesterPays: pulumi.Output<boolean | undefined>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L77">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L81">property squash</a>
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

<h2 class="pdoc-module-header" id="UploadBuffer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L11">class UploadBuffer</a>
</h2>

Manages an AWS Storage Gateway upload buffer.

~> **NOTE:** The Storage Gateway API provides no method to remove an upload buffer disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L31">constructor</a>
</h3>

```typescript
new UploadBuffer(name: string, args: UploadBufferArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UploadBuffer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L27">property diskId</a>
</h3>

```typescript
public diskId: pulumi.Output<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L31">property gatewayArn</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L11">class WorkingStorage</a>
</h2>

Manages an AWS Storage Gateway working storage.

~> **NOTE:** The Storage Gateway API provides no method to remove a working storage disk. Destroying this Terraform resource does not perform any Storage Gateway actions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L31">constructor</a>
</h3>

```typescript
new WorkingStorage(name: string, args: WorkingStorageArgs, opts?: pulumi.CustomResourceOptions)
```


Create a WorkingStorage resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L27">property diskId</a>
</h3>

```typescript
public diskId: pulumi.Output<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L31">property gatewayArn</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L9">function getLocalDisk</a>
</h2>

```typescript
getLocalDisk(args: GetLocalDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetLocalDiskResult>
```


Retrieve information about a Storage Gateway local disk. The disk identifier is useful for adding the disk as a cache or upload buffer to a gateway.

<h2 class="pdoc-module-header" id="GatewayArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L143">interface GatewayArgs</a>
</h2>

The set of arguments for constructing a Gateway resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L147">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L151">property gatewayIpAddress</a>
</h3>

```typescript
gatewayIpAddress?: pulumi.Input<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L155">property gatewayName</a>
</h3>

```typescript
gatewayName: pulumi.Input<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L159">property gatewayTimezone</a>
</h3>

```typescript
gatewayTimezone: pulumi.Input<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L163">property gatewayType</a>
</h3>

```typescript
gatewayType?: pulumi.Input<string>;
```


Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L164">property mediumChangerType</a>
</h3>

```typescript
mediumChangerType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L168">property tapeDriveType</a>
</h3>

```typescript
tapeDriveType?: pulumi.Input<string>;
```


Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

<h2 class="pdoc-module-header" id="GatewayState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L104">interface GatewayState</a>
</h2>

Input properties used for looking up and filtering Gateway resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L108">property activationKey</a>
</h3>

```typescript
activationKey?: pulumi.Input<string>;
```


Gateway activation key during resource creation. Conflicts with `gateway_ip_address`. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L112">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L116">property gatewayId</a>
</h3>

```typescript
gatewayId?: pulumi.Input<string>;
```


Identifier of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L120">property gatewayIpAddress</a>
</h3>

```typescript
gatewayIpAddress?: pulumi.Input<string>;
```


Gateway IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. Gateway must be accessible on port 80 from where Terraform is running. Additional information is available in the [Storage Gateway User Guide](https://docs.aws.amazon.com/storagegateway/latest/userguide/get-activation-key.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L124">property gatewayName</a>
</h3>

```typescript
gatewayName?: pulumi.Input<string>;
```


Name of the gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L128">property gatewayTimezone</a>
</h3>

```typescript
gatewayTimezone?: pulumi.Input<string>;
```


Time zone for the gateway. The time zone is of the format "GMT", "GMT-hr:mm", or "GMT+hr:mm". For example, `GMT-4:00` indicates the time is 4 hours behind GMT. The time zone is used, for example, for scheduling snapshots and your gateway's maintenance schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L132">property gatewayType</a>
</h3>

```typescript
gatewayType?: pulumi.Input<string>;
```


Type of the gateway. The default value is `STORED`. Valid values: `CACHED`, `FILE_S3`, `STORED`, `VTL`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L133">property mediumChangerType</a>
</h3>

```typescript
mediumChangerType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/gateway.ts#L137">property tapeDriveType</a>
</h3>

```typescript
tapeDriveType?: pulumi.Input<string>;
```


Type of tape drive to use for tape gateway. Terraform cannot detect drift of this argument. Valid values: `IBM-ULT3580-TD5`.

<h2 class="pdoc-module-header" id="GetLocalDiskArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L19">interface GetLocalDiskArgs</a>
</h2>

A collection of arguments for invoking getLocalDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L23">property diskPath</a>
</h3>

```typescript
diskPath: string;
```


The device path of the local disk to retrieve. For example, `/dev/sdb` or `/dev/xvdb`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L27">property gatewayArn</a>
</h3>

```typescript
gatewayArn: string;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="GetLocalDiskResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L33">interface GetLocalDiskResult</a>
</h2>

A collection of values returned by getLocalDisk.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L37">property diskId</a>
</h3>

```typescript
diskId: string;
```


The disk identifier. e.g. `pci-0000:03:00.0-scsi-0:0:0:0`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/getLocalDisk.ts#L41">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="NfsFileShareArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L213">interface NfsFileShareArgs</a>
</h2>

The set of arguments for constructing a NfsFileShare resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L217">property clientLists</a>
</h3>

```typescript
clientLists: pulumi.Input<pulumi.Input<string>[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L221">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L225">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L229">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L233">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L237">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L241">property locationArn</a>
</h3>

```typescript
locationArn: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L245">property nfsFileShareDefaults</a>
</h3>

```typescript
nfsFileShareDefaults?: pulumi.Input<{ ... }>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L249">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L253">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L257">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L261">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L265">property squash</a>
</h3>

```typescript
squash?: pulumi.Input<string>;
```


Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)

<h2 class="pdoc-module-header" id="NfsFileShareState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L147">interface NfsFileShareState</a>
</h2>

Input properties used for looking up and filtering NfsFileShare resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L151">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L155">property clientLists</a>
</h3>

```typescript
clientLists?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L159">property defaultStorageClass</a>
</h3>

```typescript
defaultStorageClass?: pulumi.Input<string>;
```


The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L163">property fileshareId</a>
</h3>

```typescript
fileshareId?: pulumi.Input<string>;
```


ID of the NFS File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L167">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) of the file gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L171">property guessMimeTypeEnabled</a>
</h3>

```typescript
guessMimeTypeEnabled?: pulumi.Input<boolean>;
```


Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L175">property kmsEncrypted</a>
</h3>

```typescript
kmsEncrypted?: pulumi.Input<boolean>;
```


Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L179">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L183">property locationArn</a>
</h3>

```typescript
locationArn?: pulumi.Input<string>;
```


The ARN of the backed storage used for storing file data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L187">property nfsFileShareDefaults</a>
</h3>

```typescript
nfsFileShareDefaults?: pulumi.Input<{ ... }>;
```


Nested argument with file share default values. More information below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L191">property objectAcl</a>
</h3>

```typescript
objectAcl?: pulumi.Input<string>;
```


Access Control List permission for S3 bucket objects. Defaults to `private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L195">property readOnly</a>
</h3>

```typescript
readOnly?: pulumi.Input<boolean>;
```


Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L199">property requesterPays</a>
</h3>

```typescript
requesterPays?: pulumi.Input<boolean>;
```


Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L203">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/nfsFileShare.ts#L207">property squash</a>
</h3>

```typescript
squash?: pulumi.Input<string>;
```


Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)

<h2 class="pdoc-module-header" id="UploadBufferArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L79">interface UploadBufferArgs</a>
</h2>

The set of arguments for constructing a UploadBuffer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L83">property diskId</a>
</h3>

```typescript
diskId: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L87">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="UploadBufferState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L65">interface UploadBufferState</a>
</h2>

Input properties used for looking up and filtering UploadBuffer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L69">property diskId</a>
</h3>

```typescript
diskId?: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/uploadBuffer.ts#L73">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="WorkingStorageArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L79">interface WorkingStorageArgs</a>
</h2>

The set of arguments for constructing a WorkingStorage resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L83">property diskId</a>
</h3>

```typescript
diskId: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L87">property gatewayArn</a>
</h3>

```typescript
gatewayArn: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

<h2 class="pdoc-module-header" id="WorkingStorageState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L65">interface WorkingStorageState</a>
</h2>

Input properties used for looking up and filtering WorkingStorage resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L69">property diskId</a>
</h3>

```typescript
diskId?: pulumi.Input<string>;
```


Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/storagegateway/workingStorage.ts#L73">property gatewayArn</a>
</h3>

```typescript
gatewayArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the gateway.

