---
title: Package @pulumi/cloud-aws
---


Node.js:

```javascript
var cloudAws = require("@pulumi/cloud-aws");
```

ES6 modules:

```typescript
import * as cloudAws from "@pulumi/cloud-aws";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#API">class API</a>
* <a href="#Bucket">class Bucket</a>
* <a href="#Function">class Function</a>
* <a href="#HostPathVolume">class HostPathVolume</a>
* <a href="#HttpDeployment">class HttpDeployment</a>
* <a href="#HttpServer">class HttpServer</a>
* <a href="#Service">class Service</a>
* <a href="#SharedVolume">class SharedVolume</a>
* <a href="#Table">class Table</a>
* <a href="#Task">class Task</a>
* <a href="#Topic">class Topic</a>
* <a href="#createCallbackFunction">function createCallbackFunction</a>
* <a href="#createFactoryFunction">function createFactoryFunction</a>
* <a href="#createFunction">function createFunction</a>
* <a href="#createNameWithStackInfo">function createNameWithStackInfo</a>
* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getComputeIAMRolePolicies">function getComputeIAMRolePolicies</a>
* <a href="#getGlobalInfrastructureResource">function getGlobalInfrastructureResource</a>
* <a href="#getNetwork">function getNetwork</a>
* <a href="#getOrCreateNetwork">function getOrCreateNetwork</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#setComputeIAMRolePolicies">function setComputeIAMRolePolicies</a>
* <a href="#AWSDomain">interface AWSDomain</a>
* <a href="#CloudCluster">interface CloudCluster</a>
* <a href="#CloudNetwork">interface CloudNetwork</a>
* <a href="#Endpoint">interface Endpoint</a>
* <a href="#ProxyRoute">interface ProxyRoute</a>
* <a href="#Route">interface Route</a>
* <a href="#StaticRoute">interface StaticRoute</a>
* <a href="#Volume">interface Volume</a>
* <a href="#runLambdaInVPC">let runLambdaInVPC</a>
* <a href="#Domain">type Domain</a>
* <a href="#Endpoints">type Endpoints</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts">api.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts">bucket.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts">function.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpServer.ts">httpServer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts">service.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts">shared.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts">table.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts">timer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts">topic.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>

<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L61">class API</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L67">constructor</a>
</h3>

```typescript
new API(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L118">method all</a>
</h3>

```typescript
public all(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L122">method attachCustomDomain</a>
</h3>

```typescript
public attachCustomDomain(domain: Domain): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L110">method delete</a>
</h3>

```typescript
public delete(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L98">method get</a>
</h3>

```typescript
public get(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L114">method options</a>
</h3>

```typescript
public options(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L106">method post</a>
</h3>

```typescript
public post(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L84">method proxy</a>
</h3>

```typescript
public proxy(path: string, target: string | pulumi.Output<cloud.Endpoint>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L126">method publish</a>
</h3>

```typescript
public publish(): HttpDeployment
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L102">method put</a>
</h3>

```typescript
public put(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L91">method route</a>
</h3>

```typescript
public route(method: string, path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L77">method static</a>
</h3>

```typescript
public static(path: string, localPath: string, options?: cloud.ServeStaticOptions): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L67">property deployment</a>
</h3>

```typescript
public deployment?: HttpDeployment;
```

<h2 class="pdoc-module-header" id="Bucket">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L21">class Bucket</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L26">constructor</a>
</h3>

```typescript
new Bucket(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L93">method addHandler</a>
</h3>

```typescript
public addHandler(name: string, handler: cloud.BucketHandler, events: string[], filter?: cloud.BucketFilter): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L89">method onDelete</a>
</h3>

```typescript
public onDelete(name: string, handler: cloud.BucketHandler, filter?: cloud.BucketFilter): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L85">method onPut</a>
</h3>

```typescript
public onPut(name: string, handler: cloud.BucketHandler, filter?: cloud.BucketFilter): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L22">property bucket</a>
</h3>

```typescript
public bucket: aws.s3.Bucket;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L26">property delete</a>
</h3>

```typescript
public delete: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L24">property get</a>
</h3>

```typescript
public get: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/bucket.ts#L25">property put</a>
</h3>

```typescript
public put: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L68">class Function</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L70">constructor</a>
</h3>

```typescript
new Function(name: string, handler: aws.serverless.Handler | aws.serverless.HandlerFactory, isFactoryFunction: boolean, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L69">property handler</a>
</h3>

```typescript
public handler: aws.serverless.Handler;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L70">property lambda</a>
</h3>

```typescript
public lambda: aws.lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HostPathVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L854">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L856">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L867">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L863">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L855">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L856">property path</a>
</h3>

```typescript
public path: string;
```

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L138">class HttpDeployment</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L188">constructor</a>
</h3>

```typescript
new HttpDeployment(name: string, staticRoutes: StaticRoute[], proxyRoutes: ProxyRoute[], routes: Route[], customDomains: Domain[], opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L142">property api</a>
</h3>

```typescript
public api: x.API;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L144">property customDomainNames</a>
</h3>

```typescript
public customDomainNames: pulumi.Output<string>[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L145">property customDomains</a>
</h3>

```typescript
public customDomains: aws.apigateway.DomainName[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L139">property routes</a>
</h3>

```typescript
public routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L140">property staticRoutes</a>
</h3>

```typescript
public staticRoutes: StaticRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L143">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HttpServer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpServer.ts#L27">class HttpServer</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpServer.ts#L28">constructor</a>
</h3>

```typescript
public new HttpServer(name: string, createRequestListener: cloud.RequestListenerFactory, opts: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpServer.ts#L28">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L641">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L658">constructor</a>
</h3>

```typescript
new Service(name: string, args: cloud.ServiceArguments, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L656">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L645">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L643">property containers</a>
</h3>

```typescript
public containers: cloud.Containers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L649">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L646">property ecsService</a>
</h3>

```typescript
public ecsService: aws.ecs.Service;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L648">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L651">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L642">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L644">property replicas</a>
</h3>

```typescript
public replicas: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L821">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L823">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L841">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L835">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L822">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L823">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L31">class Table</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L40">constructor</a>
</h3>

```typescript
new Table(name: string, primaryKey?: pulumi.Input<string>, primaryKeyType?: pulumi.Input<cloud.PrimaryKeyType>, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L39">property delete</a>
</h3>

```typescript
public delete: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L34">property dynamodbTable</a>
</h3>

```typescript
public dynamodbTable: aws.dynamodb.Table;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L36">property get</a>
</h3>

```typescript
public get: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L37">property insert</a>
</h3>

```typescript
public insert: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L32">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L33">property primaryKeyType</a>
</h3>

```typescript
public primaryKeyType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L38">property scan</a>
</h3>

```typescript
public scan: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L40">property update</a>
</h3>

```typescript
public update: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Task">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L875">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L884">constructor</a>
</h3>

```typescript
new Task(name: string, container: cloud.Container, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L882">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L876">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L879">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L877">property taskDefinition</a>
</h3>

```typescript
public taskDefinition: aws.ecs.TaskDefinition;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L21">class Topic</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L26">constructor</a>
</h3>

```typescript
new Topic(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L52">method subscribe</a>
</h3>

```typescript
public subscribe(name: string, handler: { ... }): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L26">property publish</a>
</h3>

```typescript
public publish: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L24">property subscriptions</a>
</h3>

```typescript
public subscriptions: aws.sns.TopicSubscription[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L23">property topic</a>
</h3>

```typescript
public topic: aws.sns.Topic;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="createCallbackFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L30">function createCallbackFunction</a>
</h2>

```typescript
createCallbackFunction(name: string, handler: aws.serverless.Handler | aws.serverless.HandlerFactory, isFactoryFunction: boolean, opts?: pulumi.ResourceOptions): aws.lambda.CallbackFunction<any, any>
```

<h2 class="pdoc-module-header" id="createFactoryFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L25">function createFactoryFunction</a>
</h2>

```typescript
createFactoryFunction(name: string, handler: aws.serverless.HandlerFactory, opts?: pulumi.ResourceOptions): Function
```

<h2 class="pdoc-module-header" id="createFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L20">function createFunction</a>
</h2>

```typescript
createFunction(name: string, handler: aws.serverless.Handler, opts?: pulumi.ResourceOptions): Function
```

<h2 class="pdoc-module-header" id="createNameWithStackInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L41">function createNameWithStackInfo</a>
</h2>

```typescript
createNameWithStackInfo(requiredInfo: string): string
```

<h2 class="pdoc-module-header" id="cron">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L45">function cron</a>
</h2>

```typescript
cron(name: string, cronTab: string, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="daily">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L50">function daily</a>
</h2>

```typescript
daily(name: string, scheduleOrHandler: timer.DailySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L165">function getCluster</a>
</h2>

```typescript
getCluster(): CloudCluster | undefined
```

<h2 class="pdoc-module-header" id="getComputeIAMRolePolicies">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L106">function getComputeIAMRolePolicies</a>
</h2>

```typescript
getComputeIAMRolePolicies(): aws.ARN[]
```

<h2 class="pdoc-module-header" id="getGlobalInfrastructureResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L75">function getGlobalInfrastructureResource</a>
</h2>

```typescript
getGlobalInfrastructureResource(): pulumi.Resource
```

<h2 class="pdoc-module-header" id="getNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L152">function getNetwork</a>
</h2>

```typescript
getNetwork(): CloudNetwork
```

<h2 class="pdoc-module-header" id="getOrCreateNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L116">function getOrCreateNetwork</a>
</h2>

```typescript
getOrCreateNetwork(): CloudNetwork
```


Get or create the network to use for container and lambda compute.

<h2 class="pdoc-module-header" id="hourly">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L74">function hourly</a>
</h2>

```typescript
hourly(name: string, scheduleOrHandler: timer.HourlySchedule | timer.Action, handlerOrOptions?: timer.Action | pulumi.ResourceOptions, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="interval">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L21">function interval</a>
</h2>

```typescript
interval(name: string, options: timer.IntervalRate, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="setComputeIAMRolePolicies">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L97">function setComputeIAMRolePolicies</a>
</h2>

```typescript
setComputeIAMRolePolicies(policyARNs: string[]): void
```

<h2 class="pdoc-module-header" id="AWSDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L48">interface AWSDomain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L50">property certificateArn</a>
</h3>

```typescript
certificateArn: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L49">property domainName</a>
</h3>

```typescript
domainName: string;
```

<h2 class="pdoc-module-header" id="CloudCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L156">interface CloudCluster</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L160">property autoScalingGroupStack</a>
</h3>

```typescript
autoScalingGroupStack?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L157">property ecsClusterARN</a>
</h3>

```typescript
ecsClusterARN: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L159">property efsMountPath</a>
</h3>

```typescript
efsMountPath?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L158">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="CloudNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L21">interface CloudNetwork</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L33">property publicSubnetIds</a>
</h3>

```typescript
publicSubnetIds: pulumi.Output<string>[];
```


The public subnets for the VPC.  In case [usePrivateSubnets] == false, these are the same as [subnets].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L29">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds: pulumi.Output<string>[];
```


The security group IDs for the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/aws-infra/cluster.d.ts#L10">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<string>[];
```


The network subnets for the clusters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L25">property usePrivateSubnets</a>
</h3>

```typescript
usePrivateSubnets: boolean;
```


Whether the network includes private subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/aws-infra/cluster.d.ts#L6">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC id of the network for the cluster

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L635">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L242">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L636">property loadBalancer</a>
</h3>

```typescript
loadBalancer: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L243">property port</a>
</h3>

```typescript
port: number;
```

<h2 class="pdoc-module-header" id="ProxyRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L34">interface ProxyRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L35">property path</a>
</h3>

```typescript
path: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L36">property target</a>
</h3>

```typescript
target: string | pulumi.Output<cloud.Endpoint>;
```

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L40">interface Route</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L43">property handlers</a>
</h3>

```typescript
handlers: cloud.RouteHandler[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L41">property method</a>
</h3>

```typescript
method: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L42">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="StaticRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L27">interface StaticRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L29">property localPath</a>
</h3>

```typescript
localPath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L30">property options</a>
</h3>

```typescript
options: cloud.ServeStaticOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L28">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L808">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L810">method getHostPath</a>
</h3>

```typescript
getHostPath(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L809">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L180">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h2 class="pdoc-module-header" id="runLambdaInVPC">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/shared.ts#L84">let runLambdaInVPC</a>
</h2>

```typescript
let runLambdaInVPC: boolean =  config.usePrivateNetwork;
```

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L54">type Domain</a>
</h2>

```typescript
type Domain = cloud.Domain | AWSDomain;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L639">type Endpoints</a>
</h2>

```typescript
type Endpoints = { ... };
```

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L403">type HttpEndpoint</a>
</h2>

```typescript
type HttpEndpoint = API;
```

