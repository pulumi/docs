---
title: Module storage
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#Blob">class Blob</a>
* <a href="#Container">class Container</a>
* <a href="#Queue">class Queue</a>
* <a href="#Share">class Share</a>
* <a href="#Table">class Table</a>
* <a href="#getAccount">function getAccount</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#BlobArgs">interface BlobArgs</a>
* <a href="#BlobState">interface BlobState</a>
* <a href="#ContainerArgs">interface ContainerArgs</a>
* <a href="#ContainerState">interface ContainerState</a>
* <a href="#GetAccountArgs">interface GetAccountArgs</a>
* <a href="#GetAccountResult">interface GetAccountResult</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#ShareArgs">interface ShareArgs</a>
* <a href="#ShareState">interface ShareState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableState">interface TableState</a>

<a href="/storage/account.ts">storage/account.ts</a> <a href="/storage/blob.ts">storage/blob.ts</a> <a href="/storage/container.ts">storage/container.ts</a> <a href="/storage/getAccount.ts">storage/getAccount.ts</a> <a href="/storage/queue.ts">storage/queue.ts</a> <a href="/storage/share.ts">storage/share.ts</a> <a href="/storage/table.ts">storage/table.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L9">class Account</a>
</h2>

Create an Azure Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L145">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Account(name: string, state?: AccountState, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L27">property accessTier</a>
</h3>

```typescript
public accessTier: pulumi.Output<string>;
```


Defines the access tier
for `BlobStorage` accounts. Valid options are `Hot` and `Cold`, defaults to
`Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L31">property accountEncryptionSource</a>
</h3>

```typescript
public accountEncryptionSource: pulumi.Output<string | undefined>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L37">property accountKind</a>
</h3>

```typescript
public accountKind: pulumi.Output<string | undefined>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L41">property accountReplicationType</a>
</h3>

```typescript
public accountReplicationType: pulumi.Output<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L45">property accountTier</a>
</h3>

```typescript
public accountTier: pulumi.Output<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L46">property accountType</a>
</h3>

```typescript
public accountType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L50">property customDomain</a>
</h3>

```typescript
public customDomain: pulumi.Output<{ ... } | undefined>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L56">property enableBlobEncryption</a>
</h3>

```typescript
public enableBlobEncryption: pulumi.Output<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L62">property enableFileEncryption</a>
</h3>

```typescript
public enableFileEncryption: pulumi.Output<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L67">property enableHttpsTrafficOnly</a>
</h3>

```typescript
public enableHttpsTrafficOnly: pulumi.Output<boolean | undefined>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L72">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L76">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L80">property primaryAccessKey</a>
</h3>

```typescript
public primaryAccessKey: pulumi.Output<string>;
```


The primary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L84">property primaryBlobConnectionString</a>
</h3>

```typescript
public primaryBlobConnectionString: pulumi.Output<string>;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L88">property primaryBlobEndpoint</a>
</h3>

```typescript
public primaryBlobEndpoint: pulumi.Output<string>;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L92">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L96">property primaryFileEndpoint</a>
</h3>

```typescript
public primaryFileEndpoint: pulumi.Output<string>;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L100">property primaryLocation</a>
</h3>

```typescript
public primaryLocation: pulumi.Output<string>;
```


The primary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L104">property primaryQueueEndpoint</a>
</h3>

```typescript
public primaryQueueEndpoint: pulumi.Output<string>;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L108">property primaryTableEndpoint</a>
</h3>

```typescript
public primaryTableEndpoint: pulumi.Output<string>;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L113">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L117">property secondaryAccessKey</a>
</h3>

```typescript
public secondaryAccessKey: pulumi.Output<string>;
```


The secondary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L121">property secondaryBlobConnectionString</a>
</h3>

```typescript
public secondaryBlobConnectionString: pulumi.Output<string>;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L125">property secondaryBlobEndpoint</a>
</h3>

```typescript
public secondaryBlobEndpoint: pulumi.Output<string>;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L129">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L133">property secondaryLocation</a>
</h3>

```typescript
public secondaryLocation: pulumi.Output<string>;
```


The secondary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L137">property secondaryQueueEndpoint</a>
</h3>

```typescript
public secondaryQueueEndpoint: pulumi.Output<string>;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L141">property secondaryTableEndpoint</a>
</h3>

```typescript
public secondaryTableEndpoint: pulumi.Output<string>;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L145">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Blob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L9">class Blob</a>
</h2>

Create an Azure Storage Blob.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L69">constructor</a>
</h3>

```typescript
new Blob(name: string, args: BlobArgs, opts?: pulumi.ResourceOptions)
```


Create a Blob resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Blob(name: string, state?: BlobState, opts?: pulumi.ResourceOptions)
```


Create a Blob resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BlobState): Blob
```


Get an existing Blob resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L25">property attempts</a>
</h3>

```typescript
public attempts: pulumi.Output<number | undefined>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L33">property parallelism</a>
</h3>

```typescript
public parallelism: pulumi.Output<number | undefined>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L42">property size</a>
</h3>

```typescript
public size: pulumi.Output<number | undefined>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L46">property source</a>
</h3>

```typescript
public source: pulumi.Output<string | undefined>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L51">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string | undefined>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L56">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L60">property storageContainerName</a>
</h3>

```typescript
public storageContainerName: pulumi.Output<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L65">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L69">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL of the blob

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L9">class Container</a>
</h2>

Create an Azure Storage Container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L43">constructor</a>
</h3>

```typescript
new Container(name: string, args: ContainerArgs, opts?: pulumi.ResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Container(name: string, state?: ContainerState, opts?: pulumi.ResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerState): Container
```


Get an existing Container resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L25">property containerAccessType</a>
</h3>

```typescript
public containerAccessType: pulumi.Output<string | undefined>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L33">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... }>;
```


Key-value definition of additional properties associated to the storage container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L43">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L9">class Queue</a>
</h2>

Create an Azure Storage Queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L35">constructor</a>
</h3>

```typescript
new Queue(name: string, args: QueueArgs, opts?: pulumi.ResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Queue(name: string, state?: QueueState, opts?: pulumi.ResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L30">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L35">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Share">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L9">class Share</a>
</h2>

Create an Azure Storage File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L43">constructor</a>
</h3>

```typescript
new Share(name: string, args: ShareArgs, opts?: pulumi.ResourceOptions)
```


Create a Share resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Share(name: string, state?: ShareState, opts?: pulumi.ResourceOptions)
```


Create a Share resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState): Share
```


Get an existing Share resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L29">property quota</a>
</h3>

```typescript
public quota: pulumi.Output<number | undefined>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default this is set to 0 which results in setting the quota to 5 TB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L39">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L43">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL of the share

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L9">class Table</a>
</h2>

Create an Azure Storage Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L35">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.ResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Table(name: string, state?: TableState, opts?: pulumi.ResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L30">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L35">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L9">function getAccount</a>
</h2>

```typescript
getAccount(args: GetAccountArgs): Promise<GetAccountResult>
```


Gets information about the specified Storage Account.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L371">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L377">property accessTier</a>
</h3>

```typescript
accessTier?: pulumi.Input<string>;
```


Defines the access tier
for `BlobStorage` accounts. Valid options are `Hot` and `Cold`, defaults to
`Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L381">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource?: pulumi.Input<string>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L387">property accountKind</a>
</h3>

```typescript
accountKind?: pulumi.Input<string>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L391">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType: pulumi.Input<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L395">property accountTier</a>
</h3>

```typescript
accountTier: pulumi.Input<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L396">property accountType</a>
</h3>

```typescript
accountType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L400">property customDomain</a>
</h3>

```typescript
customDomain?: pulumi.Input<{ ... }>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L406">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L412">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L417">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly?: pulumi.Input<boolean>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L422">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L426">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L431">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L435">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L241">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L247">property accessTier</a>
</h3>

```typescript
accessTier?: pulumi.Input<string>;
```


Defines the access tier
for `BlobStorage` accounts. Valid options are `Hot` and `Cold`, defaults to
`Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L251">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource?: pulumi.Input<string>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L257">property accountKind</a>
</h3>

```typescript
accountKind?: pulumi.Input<string>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L261">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType?: pulumi.Input<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L265">property accountTier</a>
</h3>

```typescript
accountTier?: pulumi.Input<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L266">property accountType</a>
</h3>

```typescript
accountType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L270">property customDomain</a>
</h3>

```typescript
customDomain?: pulumi.Input<{ ... }>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L276">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L282">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption
Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L287">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly?: pulumi.Input<boolean>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L292">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L296">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L300">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey?: pulumi.Input<string>;
```


The primary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L304">property primaryBlobConnectionString</a>
</h3>

```typescript
primaryBlobConnectionString?: pulumi.Input<string>;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L308">property primaryBlobEndpoint</a>
</h3>

```typescript
primaryBlobEndpoint?: pulumi.Input<string>;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L312">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L316">property primaryFileEndpoint</a>
</h3>

```typescript
primaryFileEndpoint?: pulumi.Input<string>;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L320">property primaryLocation</a>
</h3>

```typescript
primaryLocation?: pulumi.Input<string>;
```


The primary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L324">property primaryQueueEndpoint</a>
</h3>

```typescript
primaryQueueEndpoint?: pulumi.Input<string>;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L328">property primaryTableEndpoint</a>
</h3>

```typescript
primaryTableEndpoint?: pulumi.Input<string>;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L333">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L337">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey?: pulumi.Input<string>;
```


The secondary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L341">property secondaryBlobConnectionString</a>
</h3>

```typescript
secondaryBlobConnectionString?: pulumi.Input<string>;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L345">property secondaryBlobEndpoint</a>
</h3>

```typescript
secondaryBlobEndpoint?: pulumi.Input<string>;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L349">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L353">property secondaryLocation</a>
</h3>

```typescript
secondaryLocation?: pulumi.Input<string>;
```


The secondary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L357">property secondaryQueueEndpoint</a>
</h3>

```typescript
secondaryQueueEndpoint?: pulumi.Input<string>;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L361">property secondaryTableEndpoint</a>
</h3>

```typescript
secondaryTableEndpoint?: pulumi.Input<string>;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/account.ts#L365">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="BlobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L180">interface BlobArgs</a>
</h2>

The set of arguments for constructing a Blob resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L184">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L188">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L192">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L197">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L201">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L205">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L210">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L215">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L219">property storageContainerName</a>
</h3>

```typescript
storageContainerName: pulumi.Input<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L224">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h2 class="pdoc-module-header" id="BlobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L126">interface BlobState</a>
</h2>

Input properties used for looking up and filtering Blob resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L130">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L138">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L143">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L147">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L151">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L156">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L161">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L165">property storageContainerName</a>
</h3>

```typescript
storageContainerName?: pulumi.Input<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L170">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/blob.ts#L174">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL of the blob

<h2 class="pdoc-module-header" id="ContainerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L113">interface ContainerArgs</a>
</h2>

The set of arguments for constructing a Container resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L117">property containerAccessType</a>
</h3>

```typescript
containerAccessType?: pulumi.Input<string>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L126">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L131">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L85">interface ContainerState</a>
</h2>

Input properties used for looking up and filtering Container resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L89">property containerAccessType</a>
</h3>

```typescript
containerAccessType?: pulumi.Input<string>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L97">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


Key-value definition of additional properties associated to the storage container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/container.ts#L107">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L19">interface GetAccountArgs</a>
</h2>

A collection of arguments for invoking getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Specifies the name of the Storage Account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the resource group the Storage Account is located in.

<h2 class="pdoc-module-header" id="GetAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L33">interface GetAccountResult</a>
</h2>

A collection of values returned by getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L37">property accessTier</a>
</h3>

```typescript
accessTier: string;
```


Defines the access tier for `BlobStorage` accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L41">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource: string;
```


The Encryption Source for this Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L45">property accountKind</a>
</h3>

```typescript
accountKind: string;
```


Defines the Kind of account, either `BlobStorage` or `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L49">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType: string;
```


Defines the type of replication used for this storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L53">property accountTier</a>
</h3>

```typescript
accountTier: string;
```


Defines the Tier of this storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L57">property customDomain</a>
</h3>

```typescript
customDomain: { ... };
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L62">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption: boolean;
```


Are Encryption Services are enabled for Blob storage? See [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L67">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption: boolean;
```


Are Encryption Services are enabled for File storage? See [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L72">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly: boolean;
```


Is traffic only allowed via HTTPS? See [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L76">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the Storage Account exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L80">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey: string;
```


The primary access key for the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L84">property primaryBlobConnectionString</a>
</h3>

```typescript
primaryBlobConnectionString: string;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L88">property primaryBlobEndpoint</a>
</h3>

```typescript
primaryBlobEndpoint: string;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L92">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString: string;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L96">property primaryFileEndpoint</a>
</h3>

```typescript
primaryFileEndpoint: string;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L100">property primaryLocation</a>
</h3>

```typescript
primaryLocation: string;
```


The primary location of the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L104">property primaryQueueEndpoint</a>
</h3>

```typescript
primaryQueueEndpoint: string;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L108">property primaryTableEndpoint</a>
</h3>

```typescript
primaryTableEndpoint: string;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L112">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey: string;
```


The secondary access key for the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L116">property secondaryBlobConnectionString</a>
</h3>

```typescript
secondaryBlobConnectionString: string;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L120">property secondaryBlobEndpoint</a>
</h3>

```typescript
secondaryBlobEndpoint: string;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L124">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString: string;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L128">property secondaryLocation</a>
</h3>

```typescript
secondaryLocation: string;
```


The secondary location of the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L132">property secondaryQueueEndpoint</a>
</h3>

```typescript
secondaryQueueEndpoint: string;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L136">property secondaryTableEndpoint</a>
</h3>

```typescript
secondaryTableEndpoint: string;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/getAccount.ts#L140">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L93">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L107">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L73">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L77">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L82">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/queue.ts#L87">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ShareArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L113">interface ShareArgs</a>
</h2>

The set of arguments for constructing a Share resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L121">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<number>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default this is set to 0 which results in setting the quota to 5 TB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L126">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L131">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ShareState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L85">interface ShareState</a>
</h2>

Input properties used for looking up and filtering Share resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L93">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<number>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default this is set to 0 which results in setting the quota to 5 TB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L98">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L103">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/share.ts#L107">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL of the share

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L93">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L107">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L73">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L77">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L82">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/storage/table.ts#L87">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

