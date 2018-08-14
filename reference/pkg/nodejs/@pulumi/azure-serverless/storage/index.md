---
title: Module storage
---

<a href="../index.html">@pulumi/azure-serverless</a> &gt; storage

<h2 class="pdoc-module-header">Index</h2>

* <a href="#BlobEventSubscription">class BlobEventSubscription</a>
* <a href="#onBlobEvent">function onBlobEvent</a>
* <a href="#BlobContext">interface BlobContext</a>
* <a href="#BlobEventSubscriptionArgs">interface BlobEventSubscriptionArgs</a>
* <a href="#BlobCallback">type BlobCallback</a>

<a href="/storage/account.ts">storage/account.ts</a> 


<h2 class="pdoc-module-header" id="BlobEventSubscription">
<a class="pdoc-member-name" href="/storage/account.ts#L181">class BlobEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L182">constructor</a>
</h3>

```typescript
new BlobEventSubscription(name: string, account: azure.storage.Account, callback: BlobCallback, bindings: pulumi.Output<BlobBinding[]>, args: subscription.EventSubscriptionArgs, options?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L182">property account</a>
</h3>

```typescript
account: azure.storage.Account;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L237">property appServicePlan</a>
</h3>

```typescript
appServicePlan: azure.appservice.Plan;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L244">property functionApp</a>
</h3>

```typescript
functionApp: azure.appservice.FunctionApp;
```


The FunctionApp instance created to respond to the specific Binding triggers.  The
code for it will be produced by serializing out the 'callback' parameter using pulumi
serialization.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L234">property resourceGroup</a>
</h3>

```typescript
resourceGroup: pulumi.Output<azure.core.ResourceGroup>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L235">property storageAccount</a>
</h3>

```typescript
storageAccount: azure.storage.Account;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L236">property storageContainer</a>
</h3>

```typescript
storageContainer: azure.storage.Container;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="onBlobEvent">
<a class="pdoc-member-name" href="/storage/account.ts#L131">function onBlobEvent</a>
</h2>

```typescript
onBlobEvent(name: string, account: azure.storage.Account, callback: BlobCallback, args: BlobEventSubscriptionArgs, opts?: pulumi.ResourceOptions): Promise<BlobEventSubscription>
```


Creates a new subscription to the given blob using the callback provided, along with optional
options to control the behavior of the subscription.

<h2 class="pdoc-module-header" id="BlobContext">
<a class="pdoc-member-name" href="/storage/account.ts#L59">interface BlobContext</a>
</h2>

Data that will be passed along in the context object to the BlobCallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L18">method bind</a>
</h3>

```typescript
bind(args: Array<any>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L19">method done</a>
</h3>

```typescript
done(err?: Error | undefined, propertyBag?: undefined | { ... }): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L66">property bindingData</a>
</h3>

```typescript
bindingData: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L6">property bindings</a>
</h3>

```typescript
bindings?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L60">property executionContext</a>
</h3>

```typescript
executionContext: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L4">property invocationId</a>
</h3>

```typescript
invocationId?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L24">property log</a>
</h3>

```typescript
log: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L7">property req</a>
</h3>

```typescript
req?: HttpRequest;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/azure-functions-ts-essentials/models/context.d.ts#L9">property res</a>
</h3>

```typescript
res?: HttpResponse;
```

<h2 class="pdoc-module-header" id="BlobEventSubscriptionArgs">
<a class="pdoc-member-name" href="/storage/account.ts#L101">interface BlobEventSubscriptionArgs</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L67">property appServicePlan</a>
</h3>

```typescript
appServicePlan?: azure.appservice.Plan;
```


The consumption plan to put the FunctionApp in.  If not provided, a 'Dynamic', 'Y1' plan will
be used.  See https://social.msdn.microsoft.com/Forums/azure/en-US/665c365d-2b86-4a77-8cea-72ccffef216c for
additional details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L72">property appSettings</a>
</h3>

```typescript
appSettings?: pulumi.Output<Record<string, string>>;
```


A key-value map to use as the 'App Settings' for this function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L114">property containerName</a>
</h3>

```typescript
containerName?: pulumi.Input<string>;
```


The name of the container to listen to events for.  Must be provided if [path]
is not provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L123">property filterPrefix</a>
</h3>

```typescript
filterPrefix?: pulumi.Input<string>;
```


An optional prefix or suffix to filter down notifications.  See
https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob#trigger---blob-name-patterns
for more details.

Only valid with [containerName]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L124">property filterSuffix</a>
</h3>

```typescript
filterSuffix?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/storage/account.ts#L108">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


A full path specifying which blob to register events for.  For more information on this see:
https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob

If provided, [containerName], [filterPrefix] and [filterSuffix] should not be provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L47">property resourceGroup</a>
</h3>

```typescript
resourceGroup: pulumi.Input<azure.core.ResourceGroup>;
```


The resource group to create the serverless FunctionApp within.  If not provided, a new
resource group will be created with the same name as the pulumi resource. It will be created
in the region specified by the config variable "azure:region"

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L54">property storageAccount</a>
</h3>

```typescript
storageAccount?: azure.storage.Account;
```


The storage account to use where the zip-file blob for the FunctionApp will be located. If
not provided, a new storage account will create. It will be a 'Standard', 'LRS', 'StorageV2'
account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L60">property storageContainer</a>
</h3>

```typescript
storageContainer?: azure.storage.Container;
```


The container to use where the zip-file blob for the FunctionApp will be located. If not
provided, the root container of the storage account will be used.

<h2 class="pdoc-module-header" id="BlobCallback">
<a class="pdoc-member-name" href="/storage/account.ts#L99">type BlobCallback</a>
</h2>

```typescript
type BlobCallback = subscription.Callback<BlobContext, Buffer>;
```


Signature of the callback that can receive blob notifications.

