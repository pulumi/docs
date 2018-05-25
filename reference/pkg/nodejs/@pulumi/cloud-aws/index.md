---
title: Package @pulumi/cloud-aws
---


Node.js:

```javascript
var cloud-aws = require("@pulumi/cloud-aws");
```

ES6 modules:

```typescript
import * as cloud-aws from "@pulumi/cloud-aws";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#HostPathVolume">class HostPathVolume</a>
* <a href="#HttpDeployment">class HttpDeployment</a>
* <a href="#HttpEndpoint">class HttpEndpoint</a>
* <a href="#Service">class Service</a>
* <a href="#SharedVolume">class SharedVolume</a>
* <a href="#Table">class Table</a>
* <a href="#Task">class Task</a>
* <a href="#Topic">class Topic</a>
* <a href="#createSubscription">function createSubscription</a>
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

<a href="/function.ts">function.ts</a> <a href="/httpEndpoint.ts">httpEndpoint.ts</a> <a href="/service.ts">service.ts</a> <a href="/sns.ts">sns.ts</a> <a href="/table.ts">table.ts</a> <a href="/topic.ts">topic.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>
* <a href="timer">timer</a>

<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L13">class Function</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L15">constructor</a>
</h3>

```typescript
new Function(name: string, handler: aws.serverless.Handler, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L14">property handler</a>
</h3>

```typescript
public handler: aws.serverless.Handler;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts#L15">property lambda</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L765">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L767">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L778">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L774">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L766">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L767">property path</a>
</h3>

```typescript
public path: string;
```

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L129">class HttpDeployment</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L391">constructor</a>
</h3>

```typescript
new HttpDeployment(name: string, staticRoutes: StaticRoute[], proxyRoutes: ProxyRoute[], routes: Route[], customDomains: Domain[], opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L352">method registerCustomDomains</a>
</h3>

```typescript
private static registerCustomDomains(parent: pulumi.Resource, apiName: string, api: aws.apigateway.RestApi, domains: Domain[]): aws.apigateway.DomainName[]
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L265">method registerProxyRoutes</a>
</h3>

```typescript
private static registerProxyRoutes(parent: pulumi.Resource, apiName: string, proxyRoutes: ProxyRoute[], swagger: SwaggerSpec): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L309">method registerRoutes</a>
</h3>

```typescript
private static registerRoutes(parent: pulumi.Resource, apiName: string, routes: Route[], swagger: SwaggerSpec): { ... }
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L136">method registerStaticRoutes</a>
</h3>

```typescript
private static registerStaticRoutes(parent: pulumi.Resource, apiName: string, staticRoutes: StaticRoute[], swagger: SwaggerSpec): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L133">property customDomainNames</a>
</h3>

```typescript
public customDomainNames: pulumi.Output<string>[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L134">property customDomains</a>
</h3>

```typescript
public customDomains: aws.apigateway.DomainName[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L130">property routes</a>
</h3>

```typescript
public routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L131">property staticRoutes</a>
</h3>

```typescript
public staticRoutes: StaticRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L132">property url</a>
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

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L52">class HttpEndpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L58">constructor</a>
</h3>

```typescript
new HttpEndpoint(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L109">method all</a>
</h3>

```typescript
public all(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L113">method attachCustomDomain</a>
</h3>

```typescript
public attachCustomDomain(domain: Domain): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L101">method delete</a>
</h3>

```typescript
public delete(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L89">method get</a>
</h3>

```typescript
public get(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L105">method options</a>
</h3>

```typescript
public options(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L97">method post</a>
</h3>

```typescript
public post(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L75">method proxy</a>
</h3>

```typescript
public proxy(path: string, target: string | pulumi.Output<cloud.Endpoint>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L117">method publish</a>
</h3>

```typescript
public publish(): HttpDeployment
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L93">method put</a>
</h3>

```typescript
public put(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L82">method route</a>
</h3>

```typescript
public route(method: string, path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L68">method static</a>
</h3>

```typescript
public static(path: string, localPath: string, options?: cloud.ServeStaticOptions): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L57">property customDomains</a>
</h3>

```typescript
private customDomains: Domain[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L58">property deployment</a>
</h3>

```typescript
public deployment?: HttpDeployment;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L53">property name</a>
</h3>

```typescript
private name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L55">property proxyRoutes</a>
</h3>

```typescript
private proxyRoutes: ProxyRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L56">property routes</a>
</h3>

```typescript
private routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L54">property staticRoutes</a>
</h3>

```typescript
private staticRoutes: StaticRoute[];
```

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L565">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L582">constructor</a>
</h3>

```typescript
new Service(name: string, args: cloud.ServiceArguments, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L580">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L569">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L567">property containers</a>
</h3>

```typescript
public containers: cloud.Containers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L573">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L570">property ecsService</a>
</h3>

```typescript
public ecsService: aws.ecs.Service;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L572">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L575">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L566">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L568">property replicas</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L732">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L734">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L752">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L746">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L733">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L734">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L19">class Table</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L28">constructor</a>
</h3>

```typescript
new Table(name: string, primaryKey?: pulumi.Input<string>, primaryKeyType?: pulumi.Input<cloud.PrimaryKeyType>, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L27">property delete</a>
</h3>

```typescript
public delete: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L22">property dynamodbTable</a>
</h3>

```typescript
public dynamodbTable: aws.dynamodb.Table;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L24">property get</a>
</h3>

```typescript
public get: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L25">property insert</a>
</h3>

```typescript
public insert: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L20">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L21">property primaryKeyType</a>
</h3>

```typescript
public primaryKeyType: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L26">property scan</a>
</h3>

```typescript
public scan: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L28">property update</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L786">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L795">constructor</a>
</h3>

```typescript
new Task(name: string, container: cloud.Container, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L793">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L787">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L790">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L788">property taskDefinition</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L8">class Topic</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L13">constructor</a>
</h3>

```typescript
new Topic(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L103">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L35">method subscribe</a>
</h3>

```typescript
public subscribe(name: string, handler: { ... }): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L9">property name</a>
</h3>

```typescript
private name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L13">property publish</a>
</h3>

```typescript
public publish: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L11">property subscriptions</a>
</h3>

```typescript
public subscriptions: aws.sns.TopicSubscription[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L10">property topic</a>
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

<h2 class="pdoc-module-header" id="createSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L37">function createSubscription</a>
</h2>

```typescript
createSubscription(resName: string, topic: aws.sns.Topic, handler: { ... }): aws.sns.TopicSubscription
```

<h2 class="pdoc-module-header" id="AWSDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L39">interface AWSDomain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L41">property certificateArn</a>
</h3>

```typescript
certificateArn: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L40">property domainName</a>
</h3>

```typescript
domainName: string;
```

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L559">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L199">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L560">property loadBalancer</a>
</h3>

```typescript
loadBalancer: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L200">property port</a>
</h3>

```typescript
port: number;
```

<h2 class="pdoc-module-header" id="ProxyRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L26">interface ProxyRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L27">property path</a>
</h3>

```typescript
path: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L28">property target</a>
</h3>

```typescript
target: string | pulumi.Output<cloud.Endpoint>;
```

<h2 class="pdoc-module-header" id="Route">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L32">interface Route</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L35">property handlers</a>
</h3>

```typescript
handlers: cloud.RouteHandler[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L33">property method</a>
</h3>

```typescript
method: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L34">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="SNSItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L17">interface SNSItem</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L23">property Message</a>
</h3>

```typescript
Message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L24">property MessageAttributes</a>
</h3>

```typescript
MessageAttributes: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L22">property MessageId</a>
</h3>

```typescript
MessageId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L20">property Signature</a>
</h3>

```typescript
Signature: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L18">property SignatureVersion</a>
</h3>

```typescript
SignatureVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L21">property SigningCertUrl</a>
</h3>

```typescript
SigningCertUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L28">property Subject</a>
</h3>

```typescript
Subject: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L19">property Timestamp</a>
</h3>

```typescript
Timestamp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L27">property TopicArn</a>
</h3>

```typescript
TopicArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L25">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L26">property UnsubscribeUrl</a>
</h3>

```typescript
UnsubscribeUrl: string;
```

<h2 class="pdoc-module-header" id="SNSMessageAttribute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L31">interface SNSMessageAttribute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L32">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L33">property Value</a>
</h3>

```typescript
Value: string;
```

<h2 class="pdoc-module-header" id="StaticRoute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L19">interface StaticRoute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L21">property localPath</a>
</h3>

```typescript
localPath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L22">property options</a>
</h3>

```typescript
options: cloud.ServeStaticOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L20">property path</a>
</h3>

```typescript
path: string;
```

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L719">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L721">method getHostPath</a>
</h3>

```typescript
getHostPath(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L720">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L144">property kind</a>
</h3>

```typescript
kind: VolumeKind;
```

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/httpEndpoint.ts#L45">type Domain</a>
</h2>

```typescript
type Domain = cloud.Domain | AWSDomain;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L563">type Endpoints</a>
</h2>

```typescript
type Endpoints = { ... };
```

