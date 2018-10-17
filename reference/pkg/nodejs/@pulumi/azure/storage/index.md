---
title: Module storage
---

<a href="../index.html">@pulumi/azure</a> &gt; storage

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#Blob">class Blob</a>
* <a href="#Container">class Container</a>
* <a href="#Queue">class Queue</a>
* <a href="#Share">class Share</a>
* <a href="#Table">class Table</a>
* <a href="#ZipBlob">class ZipBlob</a>
* <a href="#getAccount">function getAccount</a>
* <a href="#getAccountSAS">function getAccountSAS</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#BlobArgs">interface BlobArgs</a>
* <a href="#BlobState">interface BlobState</a>
* <a href="#ContainerArgs">interface ContainerArgs</a>
* <a href="#ContainerState">interface ContainerState</a>
* <a href="#GetAccountArgs">interface GetAccountArgs</a>
* <a href="#GetAccountResult">interface GetAccountResult</a>
* <a href="#GetAccountSASArgs">interface GetAccountSASArgs</a>
* <a href="#GetAccountSASResult">interface GetAccountSASResult</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#ShareArgs">interface ShareArgs</a>
* <a href="#ShareState">interface ShareState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableState">interface TableState</a>
* <a href="#ZipBlobArgs">interface ZipBlobArgs</a>
* <a href="#ZipBlobState">interface ZipBlobState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts">storage/account.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts">storage/blob.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts">storage/container.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts">storage/getAccount.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts">storage/getAccountSAS.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts">storage/queue.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts">storage/share.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts">storage/table.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts">storage/zipBlob.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L10">class Account</a>
</h2>

Manage an Azure Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L148">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L26">property accessTier</a>
</h3>

```typescript
public accessTier: pulumi.Output<string>;
```


Defines the access tier for `BlobStorage` and `StorageV2` accounts. Valid options are `Hot` and `Cool`, defaults to `Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L30">property accountEncryptionSource</a>
</h3>

```typescript
public accountEncryptionSource: pulumi.Output<string | undefined>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L36">property accountKind</a>
</h3>

```typescript
public accountKind: pulumi.Output<string | undefined>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L40">property accountReplicationType</a>
</h3>

```typescript
public accountReplicationType: pulumi.Output<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L44">property accountTier</a>
</h3>

```typescript
public accountTier: pulumi.Output<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L45">property accountType</a>
</h3>

```typescript
public accountType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L49">property customDomain</a>
</h3>

```typescript
public customDomain: pulumi.Output<{ ... } | undefined>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L53">property enableBlobEncryption</a>
</h3>

```typescript
public enableBlobEncryption: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls if Encryption Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L57">property enableFileEncryption</a>
</h3>

```typescript
public enableFileEncryption: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls if Encryption Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L62">property enableHttpsTrafficOnly</a>
</h3>

```typescript
public enableHttpsTrafficOnly: pulumi.Output<boolean | undefined>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L66">property identity</a>
</h3>

```typescript
public identity: pulumi.Output<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L71">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L79">property networkRules</a>
</h3>

```typescript
public networkRules: pulumi.Output<{ ... } | undefined>;
```


A `network_rules` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L83">property primaryAccessKey</a>
</h3>

```typescript
public primaryAccessKey: pulumi.Output<string>;
```


The primary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L87">property primaryBlobConnectionString</a>
</h3>

```typescript
public primaryBlobConnectionString: pulumi.Output<string>;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L91">property primaryBlobEndpoint</a>
</h3>

```typescript
public primaryBlobEndpoint: pulumi.Output<string>;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L95">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L99">property primaryFileEndpoint</a>
</h3>

```typescript
public primaryFileEndpoint: pulumi.Output<string>;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L103">property primaryLocation</a>
</h3>

```typescript
public primaryLocation: pulumi.Output<string>;
```


The primary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L107">property primaryQueueEndpoint</a>
</h3>

```typescript
public primaryQueueEndpoint: pulumi.Output<string>;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L111">property primaryTableEndpoint</a>
</h3>

```typescript
public primaryTableEndpoint: pulumi.Output<string>;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L116">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L120">property secondaryAccessKey</a>
</h3>

```typescript
public secondaryAccessKey: pulumi.Output<string>;
```


The secondary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L124">property secondaryBlobConnectionString</a>
</h3>

```typescript
public secondaryBlobConnectionString: pulumi.Output<string>;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L128">property secondaryBlobEndpoint</a>
</h3>

```typescript
public secondaryBlobEndpoint: pulumi.Output<string>;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L132">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L136">property secondaryLocation</a>
</h3>

```typescript
public secondaryLocation: pulumi.Output<string>;
```


The secondary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L140">property secondaryQueueEndpoint</a>
</h3>

```typescript
public secondaryQueueEndpoint: pulumi.Output<string>;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L144">property secondaryTableEndpoint</a>
</h3>

```typescript
public secondaryTableEndpoint: pulumi.Output<string>;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L148">property tags</a>
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

<h2 class="pdoc-module-header" id="Blob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L10">class Blob</a>
</h2>

Manage an Azure Storage Blob.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L74">constructor</a>
</h3>

```typescript
new Blob(name: string, args: BlobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Blob resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BlobState): Blob
```


Get an existing Blob resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L26">property attempts</a>
</h3>

```typescript
public attempts: pulumi.Output<number | undefined>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L30">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string | undefined>;
```


The content type of the storage blob. Cannot be defined if `source_uri` is defined. Defaults to `application/octet-stream`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L38">property parallelism</a>
</h3>

```typescript
public parallelism: pulumi.Output<number | undefined>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L43">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L47">property size</a>
</h3>

```typescript
public size: pulumi.Output<number | undefined>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L51">property source</a>
</h3>

```typescript
public source: pulumi.Output<string | undefined>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L56">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string | undefined>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L61">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L65">property storageContainerName</a>
</h3>

```typescript
public storageContainerName: pulumi.Output<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L70">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L74">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL of the blob

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Container">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L10">class Container</a>
</h2>

Manage an Azure Storage Container.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L44">constructor</a>
</h3>

```typescript
new Container(name: string, args: ContainerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Container resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerState): Container
```


Get an existing Container resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L26">property containerAccessType</a>
</h3>

```typescript
public containerAccessType: pulumi.Output<string | undefined>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L34">property properties</a>
</h3>

```typescript
public properties: pulumi.Output<{ ... }>;
```


Key-value definition of additional properties associated to the storage container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L39">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L44">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L10">class Queue</a>
</h2>

Manage an Azure Storage Queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L36">constructor</a>
</h3>

```typescript
new Queue(name: string, args: QueueArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L31">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L36">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Share">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L10">class Share</a>
</h2>

Manage an Azure Storage File Share.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L44">constructor</a>
</h3>

```typescript
new Share(name: string, args: ShareArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Share resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState): Share
```


Get an existing Share resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L30">property quota</a>
</h3>

```typescript
public quota: pulumi.Output<number | undefined>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L35">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L40">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L44">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The URL of the share

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L10">class Table</a>
</h2>

Manage an Azure Storage Table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L36">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L31">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L36">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ZipBlob">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L7">class ZipBlob</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L31">constructor</a>
</h3>

```typescript
new ZipBlob(name: string, args: ZipBlobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ZipBlob resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZipBlobState): ZipBlob
```


Get an existing ZipBlob resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L20">property attempts</a>
</h3>

```typescript
public attempts: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L26">property content</a>
</h3>

```typescript
public content: pulumi.Output<pulumi.asset.Archive | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L21">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string | undefined>;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L22">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L23">property parallelism</a>
</h3>

```typescript
public parallelism: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L24">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L25">property size</a>
</h3>

```typescript
public size: pulumi.Output<number | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L27">property sourceUri</a>
</h3>

```typescript
public sourceUri: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L28">property storageAccountName</a>
</h3>

```typescript
public storageAccountName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L29">property storageContainerName</a>
</h3>

```typescript
public storageContainerName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L30">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L31">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L10">function getAccount</a>
</h2>

```typescript
getAccount(args: GetAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetAccountResult>
```


Gets information about the specified Storage Account.

<h2 class="pdoc-module-header" id="getAccountSAS">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L15">function getAccountSAS</a>
</h2>

```typescript
getAccountSAS(args: GetAccountSASArgs, opts?: pulumi.InvokeOptions): Promise<GetAccountSASResult>
```


Use this data source to create a Shared Access Signature (SAS) for an Azure Storage Account.

Shared access signatures allow fine-grained, ephemeral access control to various aspects of an Azure Storage Account.

Note that this is an [Account SAS](https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-an-account-sas)
and *not* a [Service SAS](https://docs.microsoft.com/en-us/rest/api/storageservices/constructing-a-service-sas).

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L378">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L382">property accessTier</a>
</h3>

```typescript
accessTier?: pulumi.Input<string>;
```


Defines the access tier for `BlobStorage` and `StorageV2` accounts. Valid options are `Hot` and `Cool`, defaults to `Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L386">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource?: pulumi.Input<string>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L392">property accountKind</a>
</h3>

```typescript
accountKind?: pulumi.Input<string>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L396">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType: pulumi.Input<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L400">property accountTier</a>
</h3>

```typescript
accountTier: pulumi.Input<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L401">property accountType</a>
</h3>

```typescript
accountType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L405">property customDomain</a>
</h3>

```typescript
customDomain?: pulumi.Input<{ ... }>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L409">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L413">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L418">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly?: pulumi.Input<boolean>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L422">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L427">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L431">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L435">property networkRules</a>
</h3>

```typescript
networkRules?: pulumi.Input<{ ... }>;
```


A `network_rules` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L440">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L444">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L246">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L250">property accessTier</a>
</h3>

```typescript
accessTier?: pulumi.Input<string>;
```


Defines the access tier for `BlobStorage` and `StorageV2` accounts. Valid options are `Hot` and `Cool`, defaults to `Hot`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L254">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource?: pulumi.Input<string>;
```


The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L260">property accountKind</a>
</h3>

```typescript
accountKind?: pulumi.Input<string>;
```


Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L264">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType?: pulumi.Input<string>;
```


Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L268">property accountTier</a>
</h3>

```typescript
accountTier?: pulumi.Input<string>;
```


Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L269">property accountType</a>
</h3>

```typescript
accountType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L273">property customDomain</a>
</h3>

```typescript
customDomain?: pulumi.Input<{ ... }>;
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L277">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L281">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption?: pulumi.Input<boolean>;
```


Boolean flag which controls if Encryption Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L286">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly?: pulumi.Input<boolean>;
```


Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L290">property identity</a>
</h3>

```typescript
identity?: pulumi.Input<{ ... }>;
```


A Managed Service Identity block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L295">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L299">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L303">property networkRules</a>
</h3>

```typescript
networkRules?: pulumi.Input<{ ... }>;
```


A `network_rules` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L307">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey?: pulumi.Input<string>;
```


The primary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L311">property primaryBlobConnectionString</a>
</h3>

```typescript
primaryBlobConnectionString?: pulumi.Input<string>;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L315">property primaryBlobEndpoint</a>
</h3>

```typescript
primaryBlobEndpoint?: pulumi.Input<string>;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L319">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L323">property primaryFileEndpoint</a>
</h3>

```typescript
primaryFileEndpoint?: pulumi.Input<string>;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L327">property primaryLocation</a>
</h3>

```typescript
primaryLocation?: pulumi.Input<string>;
```


The primary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L331">property primaryQueueEndpoint</a>
</h3>

```typescript
primaryQueueEndpoint?: pulumi.Input<string>;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L335">property primaryTableEndpoint</a>
</h3>

```typescript
primaryTableEndpoint?: pulumi.Input<string>;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L340">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L344">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey?: pulumi.Input<string>;
```


The secondary access key for the storage account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L348">property secondaryBlobConnectionString</a>
</h3>

```typescript
secondaryBlobConnectionString?: pulumi.Input<string>;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L352">property secondaryBlobEndpoint</a>
</h3>

```typescript
secondaryBlobEndpoint?: pulumi.Input<string>;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L356">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L360">property secondaryLocation</a>
</h3>

```typescript
secondaryLocation?: pulumi.Input<string>;
```


The secondary location of the storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L364">property secondaryQueueEndpoint</a>
</h3>

```typescript
secondaryQueueEndpoint?: pulumi.Input<string>;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L368">property secondaryTableEndpoint</a>
</h3>

```typescript
secondaryTableEndpoint?: pulumi.Input<string>;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/account.ts#L372">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="BlobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L189">interface BlobArgs</a>
</h2>

The set of arguments for constructing a Blob resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L193">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L197">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The content type of the storage blob. Cannot be defined if `source_uri` is defined. Defaults to `application/octet-stream`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L201">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L205">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L210">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L214">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L218">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L223">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L228">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L232">property storageContainerName</a>
</h3>

```typescript
storageContainerName: pulumi.Input<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L237">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h2 class="pdoc-module-header" id="BlobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L131">interface BlobState</a>
</h2>

Input properties used for looking up and filtering Blob resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L135">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```


The number of attempts to make per page or block when uploading. Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L139">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


The content type of the storage blob. Cannot be defined if `source_uri` is defined. Defaults to `application/octet-stream`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage blob. Must be unique within the storage container the blob is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L147">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```


The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L152">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L156">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L160">property source</a>
</h3>

```typescript
source?: pulumi.Input<string>;
```


An absolute path to a file on the local system. Cannot be defined if `source_uri` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L165">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```


The URI of an existing blob, or a file in the Azure File service, to use as the source contents
for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `source` is defined.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L170">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L174">property storageContainerName</a>
</h3>

```typescript
storageContainerName?: pulumi.Input<string>;
```


The name of the storage container in which this blob should be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L179">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob,
this becomes required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/blob.ts#L183">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL of the blob

<h2 class="pdoc-module-header" id="ContainerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L112">interface ContainerArgs</a>
</h2>

The set of arguments for constructing a Container resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L116">property containerAccessType</a>
</h3>

```typescript
containerAccessType?: pulumi.Input<string>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L125">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L130">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ContainerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L84">interface ContainerState</a>
</h2>

Input properties used for looking up and filtering Container resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L88">property containerAccessType</a>
</h3>

```typescript
containerAccessType?: pulumi.Input<string>;
```


The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L92">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage container. Must be unique within the storage service the container is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L96">property properties</a>
</h3>

```typescript
properties?: pulumi.Input<{ ... }>;
```


Key-value definition of additional properties associated to the storage container

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/container.ts#L106">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L20">interface GetAccountArgs</a>
</h2>

A collection of arguments for invoking getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Storage Account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group the Storage Account is located in.

<h2 class="pdoc-module-header" id="GetAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L34">interface GetAccountResult</a>
</h2>

A collection of values returned by getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L38">property accessTier</a>
</h3>

```typescript
accessTier: string;
```


The access tier for `BlobStorage` accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L42">property accountEncryptionSource</a>
</h3>

```typescript
accountEncryptionSource: string;
```


The Encryption Source for this Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L46">property accountKind</a>
</h3>

```typescript
accountKind: string;
```


The Kind of account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L50">property accountReplicationType</a>
</h3>

```typescript
accountReplicationType: string;
```


The type of replication used for this storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L54">property accountTier</a>
</h3>

```typescript
accountTier: string;
```


The Tier of this storage account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L58">property customDomain</a>
</h3>

```typescript
customDomain: { ... };
```


A `custom_domain` block as documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L63">property enableBlobEncryption</a>
</h3>

```typescript
enableBlobEncryption: boolean;
```


Are Encryption Services are enabled for Blob storage? See [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L68">property enableFileEncryption</a>
</h3>

```typescript
enableFileEncryption: boolean;
```


Are Encryption Services are enabled for File storage? See [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L73">property enableHttpsTrafficOnly</a>
</h3>

```typescript
enableHttpsTrafficOnly: boolean;
```


Is traffic only allowed via HTTPS? See [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L145">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L77">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the Storage Account exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L81">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey: string;
```


The primary access key for the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L85">property primaryBlobConnectionString</a>
</h3>

```typescript
primaryBlobConnectionString: string;
```


The connection string associated with the primary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L89">property primaryBlobEndpoint</a>
</h3>

```typescript
primaryBlobEndpoint: string;
```


The endpoint URL for blob storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L93">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString: string;
```


The connection string associated with the primary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L97">property primaryFileEndpoint</a>
</h3>

```typescript
primaryFileEndpoint: string;
```


The endpoint URL for file storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L101">property primaryLocation</a>
</h3>

```typescript
primaryLocation: string;
```


The primary location of the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L105">property primaryQueueEndpoint</a>
</h3>

```typescript
primaryQueueEndpoint: string;
```


The endpoint URL for queue storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L109">property primaryTableEndpoint</a>
</h3>

```typescript
primaryTableEndpoint: string;
```


The endpoint URL for table storage in the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L113">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey: string;
```


The secondary access key for the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L117">property secondaryBlobConnectionString</a>
</h3>

```typescript
secondaryBlobConnectionString: string;
```


The connection string associated with the secondary blob location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L121">property secondaryBlobEndpoint</a>
</h3>

```typescript
secondaryBlobEndpoint: string;
```


The endpoint URL for blob storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L125">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString: string;
```


The connection string associated with the secondary location

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L129">property secondaryLocation</a>
</h3>

```typescript
secondaryLocation: string;
```


The secondary location of the Storage Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L133">property secondaryQueueEndpoint</a>
</h3>

```typescript
secondaryQueueEndpoint: string;
```


The endpoint URL for queue storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L137">property secondaryTableEndpoint</a>
</h3>

```typescript
secondaryTableEndpoint: string;
```


The endpoint URL for table storage in the secondary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccount.ts#L141">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assigned to the resource.

<h2 class="pdoc-module-header" id="GetAccountSASArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L30">interface GetAccountSASArgs</a>
</h2>

A collection of arguments for invoking getAccountSAS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L34">property connectionString</a>
</h3>

```typescript
connectionString: string;
```


The connection string for the storage account to which this SAS applies. Typically directly from the `primary_connection_string` attribute of a terraform created `azurerm_storage_account` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L38">property expiry</a>
</h3>

```typescript
expiry: string;
```


The expiration time and date of this SAS. Must be a valid ISO-8601 format time/date string.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L42">property httpsOnly</a>
</h3>

```typescript
httpsOnly?: boolean;
```


Only permit `https` access. If `false`, both `http` and `https` are permitted. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L46">property permissions</a>
</h3>

```typescript
permissions: { ... };
```


A `permissions` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L50">property resourceTypes</a>
</h3>

```typescript
resourceTypes: { ... };
```


A `resource_types` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L54">property services</a>
</h3>

```typescript
services: { ... };
```


A `services` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L58">property start</a>
</h3>

```typescript
start: string;
```


The starting time and date of validity of this SAS. Must be a valid ISO-8601 format time/date string.

<h2 class="pdoc-module-header" id="GetAccountSASResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L64">interface GetAccountSASResult</a>
</h2>

A collection of values returned by getAccountSAS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L72">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/getAccountSAS.ts#L68">property sas</a>
</h3>

```typescript
sas: string;
```


The computed Account Shared Access Signature (SAS).

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L92">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L106">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L72">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage queue. Must be unique within the storage account the queue is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L81">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/queue.ts#L86">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ShareArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L112">interface ShareArgs</a>
</h2>

The set of arguments for constructing a Share resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L120">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<number>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L125">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L130">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ShareState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L84">interface ShareState</a>
</h2>

Input properties used for looking up and filtering Share resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the share. Must be unique within the storage account where the share is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L92">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<number>;
```


The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L97">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the share. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L102">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the share.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/share.ts#L106">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL of the share

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L92">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L106">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L72">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the storage table. Must be unique within the storage account the table is located.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L81">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/table.ts#L86">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```


Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ZipBlobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L106">interface ZipBlobArgs</a>
</h2>

The set of arguments for constructing a ZipBlob resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L107">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L113">property content</a>
</h3>

```typescript
content?: pulumi.Input<pulumi.asset.Archive>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L108">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L110">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L111">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L112">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L114">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L115">property storageAccountName</a>
</h3>

```typescript
storageAccountName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L116">property storageContainerName</a>
</h3>

```typescript
storageContainerName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L117">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ZipBlobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L88">interface ZipBlobState</a>
</h2>

Input properties used for looking up and filtering ZipBlob resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L89">property attempts</a>
</h3>

```typescript
attempts?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L95">property content</a>
</h3>

```typescript
content?: pulumi.Input<pulumi.asset.Archive>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L90">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L92">property parallelism</a>
</h3>

```typescript
parallelism?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L93">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L94">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L96">property sourceUri</a>
</h3>

```typescript
sourceUri?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L97">property storageAccountName</a>
</h3>

```typescript
storageAccountName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L98">property storageContainerName</a>
</h3>

```typescript
storageContainerName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L99">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/storage/zipBlob.ts#L100">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```

