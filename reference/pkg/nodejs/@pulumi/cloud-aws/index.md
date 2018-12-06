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
* <a href="#Function">class Function</a>
* <a href="#HostPathVolume">class HostPathVolume</a>
* <a href="#HttpDeployment">class HttpDeployment</a>
* <a href="#Service">class Service</a>
* <a href="#SharedVolume">class SharedVolume</a>
* <a href="#Table">class Table</a>
* <a href="#Task">class Task</a>
* <a href="#Topic">class Topic</a>
* <a href="#apply">function apply</a>
* <a href="#createCallbackFunction">function createCallbackFunction</a>
* <a href="#createFactoryFunction">function createFactoryFunction</a>
* <a href="#createFunction">function createFunction</a>
* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#liftResource">function liftResource</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#AWSDomain">interface AWSDomain</a>
* <a href="#Endpoint">interface Endpoint</a>
* <a href="#ProxyRoute">interface ProxyRoute</a>
* <a href="#Route">interface Route</a>
* <a href="#ServiceArguments">interface ServiceArguments</a>
* <a href="#StaticRoute">interface StaticRoute</a>
* <a href="#Volume">interface Volume</a>
* <a href="#Domain">type Domain</a>
* <a href="#Endpoints">type Endpoints</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts">api.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts">function.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts">service.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts">table.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts">timer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts">topic.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts">utils.ts</a> 

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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L834">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L836">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L847">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L843">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L835">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L836">property path</a>
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

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L620">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L637">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArguments, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L635">method getTaskRole</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L624">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L622">property containers</a>
</h3>

```typescript
public containers: cloud.Containers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L628">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L625">property ecsService</a>
</h3>

```typescript
public ecsService: aws.ecs.Service;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L627">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L630">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L621">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L623">property replicas</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L801">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L803">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L821">method getHostPath</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L815">method getVolumeName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L802">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L803">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L855">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L864">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L862">method getTaskRole</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L856">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L859">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L857">property taskDefinition</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L51">method subscribe</a>
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

<h2 class="pdoc-module-header" id="apply">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L27">function apply</a>
</h2>

```typescript
apply<T,U>(val: Record<string, T>, func: { ... }): Record<string, U>
```

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

<h2 class="pdoc-module-header" id="liftResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L38">function liftResource</a>
</h2>

```typescript
liftResource<T>(resource: T): pulumi.Output<T>
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L19">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
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

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L606">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L242">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L607">property loadBalancer</a>
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

<h2 class="pdoc-module-header" id="ServiceArguments">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L612">interface ServiceArguments</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L35">property build</a>
</h3>

```typescript
build?: string | ContainerBuild;
```


Either a path to a folder in which a Docker build should be run to construct the image for this
Container, or a ContainerBuild object with more detailed build instructions.  If `image` is also specified, the
built container will be tagged with that name, but otherwise will get an auto-generated image name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L95">property command</a>
</h3>

```typescript
command?: pulumi.Input<string[]>;
```


The command line that is passed to the container. This parameter maps to
`Cmd` in the [Create a
container](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/#create-a-container)
section of the [Docker Remote
API](https://docs.docker.com/engine/reference/api/docker_remote_api_v1.19/)
and the `COMMAND` parameter to [docker run](https://docs.docker.com/engine/reference/commandline/run/). For more
information about the Docker `CMD` parameter, go to
https://docs.docker.com/engine/reference/builder/#cmd.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L224">property containers</a>
</h3>

```typescript
containers?: Containers;
```


A collection of containers that will be deployed as part of this Service, if there are multiple.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L52">property cpu</a>
</h3>

```typescript
cpu?: pulumi.Input<number>;
```


Number of CPUs for the container to use. Maps to the Docker `--cpus` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L102">property dockerLabels</a>
</h3>

```typescript
dockerLabels?: pulumi.Input<{ ... }>;
```


A key/value map of labels to add to the container. This parameter maps to Labels in the [Create a
container](https://docs.docker.com/engine/api/v1.27/#operation/ContainerCreate) section of the [Docker Remote
API](https://docs.docker.com/engine/api/v1.27/) and the --label option to [docker
run](https://docs.docker.com/engine/reference/run/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L45">property environment</a>
</h3>

```typescript
environment?: undefined | { ... };
```


Optional environment variables to set and make available to the container
as it is running.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L40">property function</a>
</h3>

```typescript
function?: undefined | { ... };
```


The function code to use as the implementation of the contaner.  If `function` is specified,
neither `image` nor `build` are legal.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L617">property healthCheckGracePeriodSeconds</a>
</h3>

```typescript
healthCheckGracePeriodSeconds?: pulumi.Input<number>;
```


Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent
premature shutdown, up to 7200. Only valid for services configured to use load balancers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L233">property host</a>
</h3>

```typescript
host?: HostProperties;
```


The properties of the host where this service can run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L29">property image</a>
</h3>

```typescript
image?: pulumi.Input<string>;
```


The image to use for the container.  If `image` is specified, but not `build`, the image will be
pulled from the Docker Hub.  If `image` *and* `build` are specified, the `image` controls the
resulting image tag for the build image that gets pushed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L60">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<number>;
```


The maximum amount of memory the container will be allowed to use. Maps to the Docker
`--memory` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L70">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: pulumi.Input<number>;
```


The amount of memory to reserve for the container, but the container will
be allowed to use more memory if it's available.  At least one of
`memory` and `memoryReservation` must be specified.  Maps to the Docker
`--memory-reservation` option - see
https://docs.docker.com/engine/reference/commandline/run.

This should be supplied in MB. i.e. A value of 1024 would equal one gigabyte.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L77">property ports</a>
</h3>

```typescript
ports?: ContainerPort[];
```


An array of ports to publish from the container.  Ports are exposed using the TCP protocol.  If the [external]
flag is true, the port will be exposed to the Internet even if the service is running in a private network.
Maps to the Docker `--publish` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L229">property replicas</a>
</h3>

```typescript
replicas?: undefined | number;
```


The number of copies of this Service's containers to deploy and maintain
as part of the running service.  Defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L84">property volumes</a>
</h3>

```typescript
volumes?: ContainerVolumeMount[];
```


An array of volume mounts, indicating a volume to mount and a path within
the container at which to moung the volume.  Maps to the Docker
`--volume` option - see
https://docs.docker.com/engine/reference/commandline/run.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L239">property waitForSteadyState</a>
</h3>

```typescript
waitForSteadyState?: undefined | false | true;
```


Determines whether the service should wait to fully transition to a new steady state on creation and updates. If
set to false, the service may complete its deployment before it is fully ready to be used. Defaults to 'true'.

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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L788">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L790">method getHostPath</a>
</h3>

```typescript
getHostPath(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L789">method getVolumeName</a>
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

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L54">type Domain</a>
</h2>

```typescript
type Domain = cloud.Domain | AWSDomain;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L610">type Endpoints</a>
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

