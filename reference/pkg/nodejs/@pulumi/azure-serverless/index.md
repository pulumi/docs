---
title: Package @pulumi/azure-serverless
---


Node.js:

```javascript
var azureServerless = require("@pulumi/azure-serverless");
```

ES6 modules:

```typescript
import * as azureServerless from "@pulumi/azure-serverless";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#EventSubscription">class EventSubscription</a>
* <a href="#HttpFunction">class HttpFunction</a>
* <a href="#signedBlobReadUrl">function signedBlobReadUrl</a>
* <a href="#Binding">interface Binding</a>
* <a href="#EventSubscriptionArgs">interface EventSubscriptionArgs</a>
* <a href="#AzureFunctionHandler">type AzureFunctionHandler</a>
* <a href="#Callback">type Callback</a>
* <a href="#Context">type Context</a>
* <a href="#HttpRequest">type HttpRequest</a>

<a href="/functionApp.ts">functionApp.ts</a> <a href="/subscription.ts">subscription.ts</a> <a href="/util.ts">util.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="storage">storage</a>

<h2 class="pdoc-module-header" id="EventSubscription">
<a class="pdoc-member-name" href="/subscription.ts#L233">class EventSubscription</a>
</h2>

Base type for all subscription types.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L244">constructor</a>
</h3>

```typescript
new EventSubscription(type: string, name: string, callback: Callback<C, Data>, bindings: pulumi.Input<Binding[]>, args: EventSubscriptionArgs, options?: pulumi.ResourceOptions)
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

<h2 class="pdoc-module-header" id="HttpFunction">
<a class="pdoc-member-name" href="/functionApp.ts#L56">class HttpFunction</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L67">constructor</a>
</h3>

```typescript
new HttpFunction(name: string, handler: AzureFunctionHandler, options?: pulumi.ResourceOptions)
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
<a class="pdoc-child-name" href="/functionApp.ts#L63">property appServicePlan</a>
</h3>

```typescript
appServicePlan: azure.appservice.Plan;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L61">property blob</a>
</h3>

```typescript
blob: azure.storage.ZipBlob;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L66">property codeBlobUrl</a>
</h3>

```typescript
codeBlobUrl: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L67">property endpoint</a>
</h3>

```typescript
endpoint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L64">property functionApp</a>
</h3>

```typescript
functionApp: azure.appservice.FunctionApp;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L57">property resourceGroup</a>
</h3>

```typescript
resourceGroup: azure.core.ResourceGroup;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L59">property storageAccount</a>
</h3>

```typescript
storageAccount: azure.storage.Account;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/functionApp.ts#L60">property storageContainer</a>
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

<h2 class="pdoc-module-header" id="signedBlobReadUrl">
<a class="pdoc-member-name" href="/util.ts#L19">function signedBlobReadUrl</a>
</h2>

```typescript
signedBlobReadUrl(blob: azure.storage.Blob | azure.storage.ZipBlob, account: azure.storage.Account, container: azure.storage.Container): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="Binding">
<a class="pdoc-member-name" href="/subscription.ts#L79">interface Binding</a>
</h2>

Represents a Binding that will be emitted into the function.json config file for the FunctionApp.
Individual services will have more specific information they will define in their own bindings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L81">property direction</a>
</h3>

```typescript
direction: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L82">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/subscription.ts#L80">property type</a>
</h3>

```typescript
type: string;
```

<h2 class="pdoc-module-header" id="EventSubscriptionArgs">
<a class="pdoc-member-name" href="/subscription.ts#L41">interface EventSubscriptionArgs</a>
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

<h2 class="pdoc-module-header" id="AzureFunctionHandler">
<a class="pdoc-member-name" href="/functionApp.ts#L25">type AzureFunctionHandler</a>
</h2>

```typescript
type AzureFunctionHandler = { ... };
```

<h2 class="pdoc-module-header" id="Callback">
<a class="pdoc-member-name" href="/subscription.ts#L39">type Callback</a>
</h2>

```typescript
type Callback = { ... };
```


A synchronous function that can be converted into an Azure FunctionApp. This callback should
return nothing, and should signal that it is done by calling `context.Done()`. Errors can be
signified by calling `context.Done(err)`

<h2 class="pdoc-module-header" id="Context">
<a class="pdoc-member-name" href="/functionApp.ts#L21">type Context</a>
</h2>

```typescript
type Context = azurefunctions.Context;
```

<h2 class="pdoc-module-header" id="HttpRequest">
<a class="pdoc-member-name" href="/functionApp.ts#L22">type HttpRequest</a>
</h2>

```typescript
type HttpRequest = azurefunctions.HttpRequest;
```

