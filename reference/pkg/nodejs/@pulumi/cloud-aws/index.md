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
* <a href="#createSubscription">function createSubscription</a>
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
* <a href="#SNSItem">interface SNSItem</a>
* <a href="#SNSMessageAttribute">interface SNSMessageAttribute</a>
* <a href="#StaticRoute">interface StaticRoute</a>
* <a href="#Volume">interface Volume</a>
* <a href="#Domain">type Domain</a>
* <a href="#Endpoints">type Endpoints</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts">api.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts">function.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts">service.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts">sns.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts">table.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts">timer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts">topic.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts">utils.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>

<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L65">class API</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L71">constructor</a>
</h3>

```typescript
new API(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L122">method all</a>
</h3>

```typescript
public all(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L126">method attachCustomDomain</a>
</h3>

```typescript
public attachCustomDomain(domain: Domain): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L114">method delete</a>
</h3>

```typescript
public delete(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L102">method get</a>
</h3>

```typescript
public get(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L118">method options</a>
</h3>

```typescript
public options(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L110">method post</a>
</h3>

```typescript
public post(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L88">method proxy</a>
</h3>

```typescript
public proxy(path: string, target: string | pulumi.Output<cloud.Endpoint>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L130">method publish</a>
</h3>

```typescript
public publish(): HttpDeployment
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L106">method put</a>
</h3>

```typescript
public put(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L95">method route</a>
</h3>

```typescript
public route(method: string, path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L81">method static</a>
</h3>

```typescript
public static(path: string, localPath: string, options?: cloud.ServeStaticOptions): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L71">property deployment</a>
</h3>

```typescript
public deployment?: HttpDeployment;
```

<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L25">class Function</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L27">constructor</a>
</h3>

```typescript
new Function(name: string, handler: aws.serverless.Handler, opts?: pulumi.ResourceOptions)
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L26">property handler</a>
</h3>

```typescript
public handler: aws.serverless.Handler;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L27">property lambda</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L789">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L791">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L802">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L798">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L790">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L791">property path</a>
</h3>

```typescript
public path: string;
```

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L142">class HttpDeployment</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L404">constructor</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L146">property customDomainNames</a>
</h3>

```typescript
public customDomainNames: pulumi.Output<string>[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L147">property customDomains</a>
</h3>

```typescript
public customDomains: aws.apigateway.DomainName[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L143">property routes</a>
</h3>

```typescript
public routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L144">property staticRoutes</a>
</h3>

```typescript
public staticRoutes: StaticRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L145">property url</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L575">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L592">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L590">method getTaskRole</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L579">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L577">property containers</a>
</h3>

```typescript
public containers: cloud.Containers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L583">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L580">property ecsService</a>
</h3>

```typescript
public ecsService: aws.ecs.Service;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L582">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L585">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L576">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L578">property replicas</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L756">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L758">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L776">method getHostPath</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L770">method getVolumeName</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L757">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L758">property name</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L810">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L819">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L817">method getTaskRole</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L811">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L814">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L812">property taskDefinition</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L20">class Topic</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L25">constructor</a>
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
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L47">method subscribe</a>
</h3>

```typescript
public subscribe(name: string, handler: { ... }): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L25">property publish</a>
</h3>

```typescript
public publish: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L23">property subscriptions</a>
</h3>

```typescript
public subscriptions: aws.sns.TopicSubscription[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L22">property topic</a>
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

<h2 class="pdoc-module-header" id="createSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L49">function createSubscription</a>
</h2>

```typescript
createSubscription(resName: string, topic: aws.sns.Topic, handler: { ... }): aws.sns.TopicSubscription
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L52">interface AWSDomain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L54">property certificateArn</a>
</h3>

```typescript
certificateArn: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L53">property domainName</a>
</h3>

```typescript
domainName: string;
```

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L569">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L233">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L570">property loadBalancer</a>
</h3>

```typescript
loadBalancer: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L234">property port</a>
</h3>

```typescript
port: number;
```

<h2 class="pdoc-module-header" id="ProxyRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L38">interface ProxyRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L39">property path</a>
</h3>

```typescript
path: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L40">property target</a>
</h3>

```typescript
target: string | pulumi.Output<cloud.Endpoint>;
```

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L44">interface Route</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L47">property handlers</a>
</h3>

```typescript
handlers: cloud.RouteHandler[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L45">property method</a>
</h3>

```typescript
method: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L46">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="SNSItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L29">interface SNSItem</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L35">property Message</a>
</h3>

```typescript
Message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L36">property MessageAttributes</a>
</h3>

```typescript
MessageAttributes: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L34">property MessageId</a>
</h3>

```typescript
MessageId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L32">property Signature</a>
</h3>

```typescript
Signature: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L30">property SignatureVersion</a>
</h3>

```typescript
SignatureVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L33">property SigningCertUrl</a>
</h3>

```typescript
SigningCertUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L40">property Subject</a>
</h3>

```typescript
Subject: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L31">property Timestamp</a>
</h3>

```typescript
Timestamp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L39">property TopicArn</a>
</h3>

```typescript
TopicArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L37">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L38">property UnsubscribeUrl</a>
</h3>

```typescript
UnsubscribeUrl: string;
```

<h2 class="pdoc-module-header" id="SNSMessageAttribute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L43">interface SNSMessageAttribute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L44">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L45">property Value</a>
</h3>

```typescript
Value: string;
```

<h2 class="pdoc-module-header" id="StaticRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L31">interface StaticRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L33">property localPath</a>
</h3>

```typescript
localPath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L34">property options</a>
</h3>

```typescript
options: cloud.ServeStaticOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L32">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L743">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L745">method getHostPath</a>
</h3>

```typescript
getHostPath(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L744">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L171">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L58">type Domain</a>
</h2>

```typescript
type Domain = cloud.Domain | AWSDomain;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L573">type Endpoints</a>
</h2>

```typescript
type Endpoints = { ... };
```

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L957">type HttpEndpoint</a>
</h2>

```typescript
type HttpEndpoint = API;
```

