---
title: Package @pulumi/cloud-azure
---


Node.js:

```javascript
var cloudAzure = require("@pulumi/cloud-azure");
```

ES6 modules:

```typescript
import * as cloudAzure from "@pulumi/cloud-azure";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#API">class API</a>
* <a href="#Bucket">class Bucket</a>
* <a href="#HostPathVolume">class HostPathVolume</a>
* <a href="#HttpDeployment">class HttpDeployment</a>
* <a href="#HttpServer">class HttpServer</a>
* <a href="#Service">class Service</a>
* <a href="#SharedVolume">class SharedVolume</a>
* <a href="#Task">class Task</a>
* <a href="#Topic">class Topic</a>
* <a href="#defaultSubscriptionArgs">const defaultSubscriptionArgs</a>
* <a href="#globalResourceGroup">const globalResourceGroup</a>
* <a href="#globalResourceGroupName">const globalResourceGroupName</a>
* <a href="#location">const location</a>
* <a href="#createNameWithStackInfo">function createNameWithStackInfo</a>
* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#getGlobalInfrastructureResource">function getGlobalInfrastructureResource</a>
* <a href="#getGlobalStorageAccount">function getGlobalStorageAccount</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>

<a href="/api.ts">api.ts</a> <a href="/bucket.ts">bucket.ts</a> <a href="/httpServer.ts">httpServer.ts</a> <a href="/service.ts">service.ts</a> <a href="/shared.ts">shared.ts</a> <a href="/timer.ts">timer.ts</a> <a href="/topic.ts">topic.ts</a> 


<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="/api.ts#L20">class API</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L20">constructor</a>
</h3>

```typescript
new API(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L57">method all</a>
</h3>

```typescript
public all(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L61">method attachCustomDomain</a>
</h3>

```typescript
public attachCustomDomain(domain: cloud.Domain): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L49">method delete</a>
</h3>

```typescript
public delete(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L37">method get</a>
</h3>

```typescript
public get(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L53">method options</a>
</h3>

```typescript
public options(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L45">method post</a>
</h3>

```typescript
public post(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L29">method proxy</a>
</h3>

```typescript
public proxy(path: string, target: string | pulumi.Output<cloud.Endpoint>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L65">method publish</a>
</h3>

```typescript
public publish(): HttpDeployment
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L41">method put</a>
</h3>

```typescript
public put(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L33">method route</a>
</h3>

```typescript
public route(method: string, path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L25">method static</a>
</h3>

```typescript
public static(path: string, localPath: string, options?: cloud.ServeStaticOptions): void
```

<h2 class="pdoc-module-header" id="Bucket">
<a class="pdoc-member-name" href="/bucket.ts#L25">class Bucket</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L36">constructor</a>
</h3>

```typescript
public new Bucket(name: string, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L27">property container</a>
</h3>

```typescript
public container: azure.storage.Container;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L36">property delete</a>
</h3>

```typescript
public delete: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L34">property get</a>
</h3>

```typescript
public get: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L31">property onDelete</a>
</h3>

```typescript
public onDelete: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L30">property onPut</a>
</h3>

```typescript
public onPut: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L35">property put</a>
</h3>

```typescript
public put: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/bucket.ts#L26">property storageAccount</a>
</h3>

```typescript
public storageAccount: azure.storage.Account;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HostPathVolume">
<a class="pdoc-member-name" href="/service.ts#L409">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L411">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L410">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L411">property path</a>
</h3>

```typescript
public path: string;
```

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="/api.ts#L71">class HttpDeployment</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L73">constructor</a>
</h3>

```typescript
new HttpDeployment(name: string, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L73">property customDomainNames</a>
</h3>

```typescript
public customDomainNames: pulumi.Output<string>[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/api.ts#L72">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HttpServer">
<a class="pdoc-member-name" href="/httpServer.ts#L68">class HttpServer</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/httpServer.ts#L69">constructor</a>
</h3>

```typescript
public new HttpServer(name: string, createRequestListener: cloud.RequestListenerFactory, opts: pulumi.ComponentResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/httpServer.ts#L69">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="/service.ts#L29">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L36">constructor</a>
</h3>

```typescript
new Service(name: string, args: cloud.ServiceArguments, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L34">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<cloud.Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L33">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<cloud.Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L36">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L31">property group</a>
</h3>

```typescript
public group: azure.containerservice.Group;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L30">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedVolume">
<a class="pdoc-member-name" href="/service.ts#L398">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L400">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L399">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L400">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Task">
<a class="pdoc-member-name" href="/service.ts#L275">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as)
needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L276">constructor</a>
</h3>

```typescript
new Task(name: string, container: cloud.Container, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/service.ts#L276">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="/topic.ts#L22">class Topic</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L30">constructor</a>
</h3>

```typescript
new Topic(name: string, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L23">property namespace</a>
</h3>

```typescript
public namespace: azure.eventhub.Namespace;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L27">property publish</a>
</h3>

```typescript
public publish: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L30">property subscribe</a>
</h3>

```typescript
public subscribe: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L25">property subscriptions</a>
</h3>

```typescript
public subscriptions: serverless.eventhub.TopicEventSubscription[] =  [];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/topic.ts#L24">property topic</a>
</h3>

```typescript
public topic: azure.eventhub.Topic;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="defaultSubscriptionArgs">
<a class="pdoc-member-name" href="/shared.ts#L190">const defaultSubscriptionArgs</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L198">let appServicePlanId</a>
</h3>

```typescript
let appServicePlanId: Output<string> =  getGlobalAppServicePlan().id;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L192">let includePackages</a>
</h3>

```typescript
let includePackages: undefined | string[] =  config.functionIncludePackages;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L191">let includePaths</a>
</h3>

```typescript
let includePaths: undefined | string[] =  config.functionIncludePaths;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L195">let location</a>
</h3>

```typescript
let location: string =  location;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L194">let resourceGroupName</a>
</h3>

```typescript
let resourceGroupName: Output<string> =  globalResourceGroupName;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L196">let storageAccount</a>
</h3>

```typescript
let storageAccount: Account =  getGlobalStorageAccount();
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/shared.ts#L197">let storageContainer</a>
</h3>

```typescript
let storageContainer: Container =  getGlobalStorageContainer();
```

<h2 class="pdoc-module-header" id="globalResourceGroup">
<a class="pdoc-member-name" href="/shared.ts#L78">const globalResourceGroup</a>
</h2>

```typescript
const globalResourceGroup: Output<ResourceGroup> =  getGlobalResourceGroup();
```


The Azure Resource Group to use for all resources if a specific one is not specified. To use an
existing Resource Group provide the [cloud-azure:resourceGroupName] config value. Otherwise, a
new group will be created.

<h2 class="pdoc-module-header" id="globalResourceGroupName">
<a class="pdoc-member-name" href="/shared.ts#L79">const globalResourceGroupName</a>
</h2>

```typescript
const globalResourceGroupName: Output<string> =  globalResourceGroup.apply(g => g.name);
```

<h2 class="pdoc-module-header" id="location">
<a class="pdoc-member-name" href="/shared.ts#L69">const location</a>
</h2>

```typescript
const location: string =  config.location;
```

<h2 class="pdoc-module-header" id="createNameWithStackInfo">
<a class="pdoc-member-name" href="/shared.ts#L24">function createNameWithStackInfo</a>
</h2>

```typescript
createNameWithStackInfo(requiredInfo: string, maxLength: number, delim: string): string
```


Helper to create a name for resources with a name that should be unique to this stack.

<h2 class="pdoc-module-header" id="cron">
<a class="pdoc-member-name" href="/timer.ts#L150">function cron</a>
</h2>

```typescript
cron(name: string, cronTab: string, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="daily">
<a class="pdoc-member-name" href="/timer.ts#L105">function daily</a>
</h2>

```typescript
daily(name: string, scheduleOrHandler: timer.DailySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="getGlobalInfrastructureResource">
<a class="pdoc-member-name" href="/shared.ts#L61">function getGlobalInfrastructureResource</a>
</h2>

```typescript
getGlobalInfrastructureResource(): pulumi.Resource
```


Get's the resource that any global infrastructure resource for this stack can use as a parent.

<h2 class="pdoc-module-header" id="getGlobalStorageAccount">
<a class="pdoc-member-name" href="/shared.ts#L114">function getGlobalStorageAccount</a>
</h2>

```typescript
getGlobalStorageAccount(): Account
```


The Azure Storage Account to use for all resources that need to store data if not specific
account is specified. To use an existing Storage Account provide the
[cloud-azure:storageAccountId] config value. Otherwise, a new account will be created.

<h2 class="pdoc-module-header" id="hourly">
<a class="pdoc-member-name" href="/timer.ts#L129">function hourly</a>
</h2>

```typescript
hourly(name: string, scheduleOrHandler: timer.HourlySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="interval">
<a class="pdoc-member-name" href="/timer.ts#L31">function interval</a>
</h2>

```typescript
interval(name: string, options: timer.IntervalRate, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="/shared.ts#L182">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="/api.ts#L91">type HttpEndpoint</a>
</h2>

```typescript
type HttpEndpoint = API;
```

