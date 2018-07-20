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
* <a href="#Timer">class Timer</a>
* <a href="#Topic">class Topic</a>
* <a href="#apigatewayAssumeRolePolicyDocument">const apigatewayAssumeRolePolicyDocument</a>
* <a href="#buildImageCache">const buildImageCache</a>
* <a href="#consistentRead">const consistentRead</a>
* <a href="#repositories">const repositories</a>
* <a href="#stageName">const stageName</a>
* <a href="#taskRolePolicy">const taskRolePolicy</a>
* <a href="#thisShape">const thisShape</a>
* <a href="#volumeNames">const volumeNames</a>
* <a href="#apiGatewayToRequestResponse">function apiGatewayToRequestResponse</a>
* <a href="#apply">function apply</a>
* <a href="#buildAndPushImage">function buildAndPushImage</a>
* <a href="#buildImageAsync">function buildImageAsync</a>
* <a href="#computeContainerDefinitions">function computeContainerDefinitions</a>
* <a href="#computeImage">function computeImage</a>
* <a href="#createBaseSpec">function createBaseSpec</a>
* <a href="#createLoadBalancer">function createLoadBalancer</a>
* <a href="#createPathSpecLambda">function createPathSpecLambda</a>
* <a href="#createPathSpecObject">function createPathSpecObject</a>
* <a href="#createPathSpecProxy">function createPathSpecProxy</a>
* <a href="#createScheduledEvent">function createScheduledEvent</a>
* <a href="#createSubscription">function createSubscription</a>
* <a href="#createSwaggerString">function createSwaggerString</a>
* <a href="#createTaskDefinition">function createTaskDefinition</a>
* <a href="#cron">function cron</a>
* <a href="#daily">function daily</a>
* <a href="#dockerBuild">function dockerBuild</a>
* <a href="#getEndpointHelper">function getEndpointHelper</a>
* <a href="#getEndpoints">function getEndpoints</a>
* <a href="#getExecutionRole">function getExecutionRole</a>
* <a href="#getImageName">function getImageName</a>
* <a href="#getOrCreateRepository">function getOrCreateRepository</a>
* <a href="#getTaskRole">function getTaskRole</a>
* <a href="#hourly">function hourly</a>
* <a href="#interval">function interval</a>
* <a href="#isCloudDomain">function isCloudDomain</a>
* <a href="#liftResource">function liftResource</a>
* <a href="#localStageImageName">function localStageImageName</a>
* <a href="#loginToRegistry">function loginToRegistry</a>
* <a href="#makeServiceEnvName">function makeServiceEnvName</a>
* <a href="#parseDockerEngineUpdatesFromBuffer">function parseDockerEngineUpdatesFromBuffer</a>
* <a href="#placementConstraintsForHost">function placementConstraintsForHost</a>
* <a href="#pullCacheAsync">function pullCacheAsync</a>
* <a href="#pulumiKeyTypeToDynamoKeyType">function pulumiKeyTypeToDynamoKeyType</a>
* <a href="#pushImageAsync">function pushImageAsync</a>
* <a href="#runCLICommand">function runCLICommand</a>
* <a href="#safeS3BucketName">function safeS3BucketName</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#swaggerMethod">function swaggerMethod</a>
* <a href="#taskMemoryAndCPUForContainers">function taskMemoryAndCPUForContainers</a>
* <a href="#APIGatewayIdentity">interface APIGatewayIdentity</a>
* <a href="#APIGatewayRequest">interface APIGatewayRequest</a>
* <a href="#APIGatewayRequestContext">interface APIGatewayRequestContext</a>
* <a href="#APIGatewayResponse">interface APIGatewayResponse</a>
* <a href="#AWSDomain">interface AWSDomain</a>
* <a href="#ApigatewayIntegration">interface ApigatewayIntegration</a>
* <a href="#ApigatewayIntegrationAsync">interface ApigatewayIntegrationAsync</a>
* <a href="#ApigatewayIntegrationBase">interface ApigatewayIntegrationBase</a>
* <a href="#BuildResult">interface BuildResult</a>
* <a href="#CommandResult">interface CommandResult</a>
* <a href="#ContainerPortLoadBalancer">interface ContainerPortLoadBalancer</a>
* <a href="#Endpoint">interface Endpoint</a>
* <a href="#ExposedPort">interface ExposedPort</a>
* <a href="#ExposedPorts">interface ExposedPorts</a>
* <a href="#ImageOptions">interface ImageOptions</a>
* <a href="#ProxyRoute">interface ProxyRoute</a>
* <a href="#Registry">interface Registry</a>
* <a href="#RequestResponse">interface RequestResponse</a>
* <a href="#Route">interface Route</a>
* <a href="#SNSEvent">interface SNSEvent</a>
* <a href="#SNSItem">interface SNSItem</a>
* <a href="#SNSMessageAttribute">interface SNSMessageAttribute</a>
* <a href="#SNSRecord">interface SNSRecord</a>
* <a href="#StaticRoute">interface StaticRoute</a>
* <a href="#SwaggerAPIGatewayIntegrationResponse">interface SwaggerAPIGatewayIntegrationResponse</a>
* <a href="#SwaggerHeader">interface SwaggerHeader</a>
* <a href="#SwaggerInfo">interface SwaggerInfo</a>
* <a href="#SwaggerItems">interface SwaggerItems</a>
* <a href="#SwaggerOperation">interface SwaggerOperation</a>
* <a href="#SwaggerOperationAsync">interface SwaggerOperationAsync</a>
* <a href="#SwaggerResponse">interface SwaggerResponse</a>
* <a href="#SwaggerSchema">interface SwaggerSchema</a>
* <a href="#SwaggerSpec">interface SwaggerSpec</a>
* <a href="#TaskDefinition">interface TaskDefinition</a>
* <a href="#Volume">interface Volume</a>
* <a href="#apiShape">let apiShape</a>
* <a href="#cachedDockerVersionString">let cachedDockerVersionString</a>
* <a href="#dockerPasswordStdin">let dockerPasswordStdin</a>
* <a href="#executionRole">let executionRole</a>
* <a href="#taskRole">let taskRole</a>
* <a href="#Domain">type Domain</a>
* <a href="#Endpoints">type Endpoints</a>
* <a href="#HttpEndpoint">type HttpEndpoint</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts">api.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts">docker.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/function.ts">function.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/index.ts">index.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts">service.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts">sns.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts">table.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts">timer.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts">topic.ts</a> <a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts">utils.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="config">config</a>

<h2 class="pdoc-module-header" id="API">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L64">class API</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L70">constructor</a>
</h3>

```typescript
new API(name: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L121">method all</a>
</h3>

```typescript
public all(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L125">method attachCustomDomain</a>
</h3>

```typescript
public attachCustomDomain(domain: Domain): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L113">method delete</a>
</h3>

```typescript
public delete(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L101">method get</a>
</h3>

```typescript
public get(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L117">method options</a>
</h3>

```typescript
public options(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L109">method post</a>
</h3>

```typescript
public post(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L87">method proxy</a>
</h3>

```typescript
public proxy(path: string, target: string | pulumi.Output<cloud.Endpoint>): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L129">method publish</a>
</h3>

```typescript
public publish(): HttpDeployment
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L105">method put</a>
</h3>

```typescript
public put(path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L94">method route</a>
</h3>

```typescript
public route(method: string, path: string, handlers: cloud.RouteHandler[]): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L80">method static</a>
</h3>

```typescript
public static(path: string, localPath: string, options?: cloud.ServeStaticOptions): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L69">property customDomains</a>
</h3>

```typescript
private customDomains: Domain[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L70">property deployment</a>
</h3>

```typescript
public deployment?: HttpDeployment;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L65">property name</a>
</h3>

```typescript
private name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L67">property proxyRoutes</a>
</h3>

```typescript
private proxyRoutes: ProxyRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L68">property routes</a>
</h3>

```typescript
private routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L66">property staticRoutes</a>
</h3>

```typescript
private staticRoutes: StaticRoute[];
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="HostPathVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L778">class HostPathVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L780">constructor</a>
</h3>

```typescript
new HostPathVolume(path: string)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L791">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L787">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L779">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L780">property path</a>
</h3>

```typescript
public path: string;
```

<h2 class="pdoc-module-header" id="HttpDeployment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L141">class HttpDeployment</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L403">constructor</a>
</h3>

```typescript
new HttpDeployment(name: string, staticRoutes: StaticRoute[], proxyRoutes: ProxyRoute[], routes: Route[], customDomains: Domain[], opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L364">method registerCustomDomains</a>
</h3>

```typescript
private static registerCustomDomains(parent: pulumi.Resource, apiName: string, api: aws.apigateway.RestApi, domains: Domain[]): aws.apigateway.DomainName[]
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L277">method registerProxyRoutes</a>
</h3>

```typescript
private static registerProxyRoutes(parent: pulumi.Resource, apiName: string, proxyRoutes: ProxyRoute[], swagger: SwaggerSpec): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L321">method registerRoutes</a>
</h3>

```typescript
private static registerRoutes(parent: pulumi.Resource, apiName: string, routes: Route[], swagger: SwaggerSpec): { ... }
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L148">method registerStaticRoutes</a>
</h3>

```typescript
private static registerStaticRoutes(parent: pulumi.Resource, apiName: string, staticRoutes: StaticRoute[], swagger: SwaggerSpec): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L145">property customDomainNames</a>
</h3>

```typescript
public customDomainNames: pulumi.Output<string>[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L146">property customDomains</a>
</h3>

```typescript
public customDomains: aws.apigateway.DomainName[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L142">property routes</a>
</h3>

```typescript
public routes: Route[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L143">property staticRoutes</a>
</h3>

```typescript
public staticRoutes: StaticRoute[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L144">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L578">class Service</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L595">constructor</a>
</h3>

```typescript
new Service(name: string, args: cloud.ServiceArguments, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L593">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L582">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L580">property containers</a>
</h3>

```typescript
public containers: cloud.Containers;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L586">property defaultEndpoint</a>
</h3>

```typescript
public defaultEndpoint: pulumi.Output<Endpoint>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L583">property ecsService</a>
</h3>

```typescript
public ecsService: aws.ecs.Service;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L585">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<Endpoints>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L588">property getEndpoint</a>
</h3>

```typescript
public getEndpoint: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L579">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L581">property replicas</a>
</h3>

```typescript
public replicas: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SharedVolume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L745">class SharedVolume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L747">constructor</a>
</h3>

```typescript
new SharedVolume(name: string, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L765">method getHostPath</a>
</h3>

```typescript
getHostPath(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L759">method getVolumeName</a>
</h3>

```typescript
getVolumeName(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L746">property kind</a>
</h3>

```typescript
public kind: cloud.VolumeKind;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L747">property name</a>
</h3>

```typescript
public name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Task">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L799">class Task</a>
</h2>

A Task represents a container which can be [run] dynamically whenever (and as many times as) needed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L808">constructor</a>
</h3>

```typescript
new Task(name: string, container: cloud.Container, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L806">method getTaskRole</a>
</h3>

```typescript
public static getTaskRole(): aws.iam.Role
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L800">property cluster</a>
</h3>

```typescript
public cluster: CloudCluster;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L803">property run</a>
</h3>

```typescript
public run: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L801">property taskDefinition</a>
</h3>

```typescript
public taskDefinition: aws.ecs.TaskDefinition;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Timer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L95">class Timer</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L99">constructor</a>
</h3>

```typescript
new Timer(name: string, scheduleExpression: string, handler: timer.Action, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L99">property function</a>
</h3>

```typescript
public function: Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L97">property rule</a>
</h3>

```typescript
public rule: aws.cloudwatch.EventRule;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L96">property scheduleExpression</a>
</h3>

```typescript
public scheduleExpression: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L98">property target</a>
</h3>

```typescript
public target: aws.cloudwatch.EventTarget;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/topic.ts#L21">property name</a>
</h3>

```typescript
private name: string;
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="apigatewayAssumeRolePolicyDocument">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L790">const apigatewayAssumeRolePolicyDocument</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L792">let Statement</a>
</h3>

```typescript
let Statement: { ... }[] =  [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "apigateway.amazonaws.com",
            },
            "Action": "sts:AssumeRole",
        },
    ];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L791">let Version</a>
</h3>

```typescript
let Version: string = "2012-10-17";
```

<h2 class="pdoc-module-header" id="buildImageCache">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L188">const buildImageCache</a>
</h2>

```typescript
const buildImageCache: Map<string, Output<string>> =  new Map<string, pulumi.Output<string>>();
```

<h2 class="pdoc-module-header" id="consistentRead">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L29">const consistentRead</a>
</h2>

```typescript
const consistentRead: true = true;
```

<h2 class="pdoc-module-header" id="repositories">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L175">const repositories</a>
</h2>

```typescript
const repositories: Map<string, Repository> =  new Map<string, aws.ecr.Repository>();
```

<h2 class="pdoc-module-header" id="stageName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L859">const stageName</a>
</h2>

```typescript
const stageName: stage = "stage";
```

<h2 class="pdoc-module-header" id="taskRolePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L392">const taskRolePolicy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L394">let Statement</a>
</h3>

```typescript
let Statement: { ... }[] =  [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "ecs-tasks.amazonaws.com",
            },
            "Effect": "Allow",
            "Sid": "",
        },
    ];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L393">let Version</a>
</h3>

```typescript
let Version: string = "2012-10-17";
```

<h2 class="pdoc-module-header" id="thisShape">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/index.ts#L43">const thisShape</a>
</h2>

```typescript
const thisShape: "/Users/luke/go/src/github.com/pulumi/pulumi-cloud/aws/index" =  undefined as any;
```

<h2 class="pdoc-module-header" id="volumeNames">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L730">const volumeNames</a>
</h2>

```typescript
const volumeNames: Set<string> =  new Set<string>();
```

<h2 class="pdoc-module-header" id="apiGatewayToRequestResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L860">function apiGatewayToRequestResponse</a>
</h2>

```typescript
apiGatewayToRequestResponse(ev: APIGatewayRequest, body: Buffer, cb: { ... }): RequestResponse
```

<h2 class="pdoc-module-header" id="apply">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L27">function apply</a>
</h2>

```typescript
apply<T,U>(val: Record<string, T>, func: { ... }): Record<string, U>
```

<h2 class="pdoc-module-header" id="buildAndPushImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L40">function buildAndPushImage</a>
</h2>

```typescript
buildAndPushImage(imageName: string, container: cloud.Container, repositoryUrl: pulumi.Input<string>, logResource: pulumi.Resource, connectToRegistry: { ... }): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="buildImageAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L131">function buildImageAsync</a>
</h2>

```typescript
buildImageAsync(imageName: string, container: cloud.Container, logResource: pulumi.Resource, cacheFrom: Promise<string[] | undefined>): Promise<BuildResult>
```

<h2 class="pdoc-module-header" id="computeContainerDefinitions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L322">function computeContainerDefinitions</a>
</h2>

```typescript
computeContainerDefinitions(containers: cloud.Containers, ports: ExposedPorts | undefined, logGroup: aws.cloudwatch.LogGroup): pulumi.Output<aws.ecs.ContainerDefinition[]>
```

<h2 class="pdoc-module-header" id="computeImage">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L202">function computeImage</a>
</h2>

```typescript
computeImage(imageName: string, container: cloud.Container, ports: ExposedPorts | undefined, repository: aws.ecr.Repository | undefined): pulumi.Output<ImageOptions>
```

<h2 class="pdoc-module-header" id="createBaseSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L625">function createBaseSpec</a>
</h2>

```typescript
createBaseSpec(apiName: string): SwaggerSpec
```

<h2 class="pdoc-module-header" id="createLoadBalancer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L39">function createLoadBalancer</a>
</h2>

```typescript
createLoadBalancer(parent: pulumi.Resource, cluster: CloudCluster, serviceName: string, containerName: string, portMapping: cloud.ContainerPort, network: CloudNetwork): ContainerPortLoadBalancer
```

<h2 class="pdoc-module-header" id="createPathSpecLambda">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L634">function createPathSpecLambda</a>
</h2>

```typescript
createPathSpecLambda(lambda: aws.lambda.Function): SwaggerOperationAsync
```

<h2 class="pdoc-module-header" id="createPathSpecObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L705">function createPathSpecObject</a>
</h2>

```typescript
createPathSpecObject(bucket: aws.s3.Bucket, key: string, role: aws.iam.Role, pathParameter?: undefined | string): SwaggerOperationAsync
```

<h2 class="pdoc-module-header" id="createPathSpecProxy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L649">function createPathSpecProxy</a>
</h2>

```typescript
createPathSpecProxy(target: string | pulumi.Output<cloud.Endpoint>, vpcLink: aws.apigateway.VpcLink | undefined, useProxyPathParameter: boolean): SwaggerOperationAsync
```

<h2 class="pdoc-module-header" id="createScheduledEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/timer.ts#L139">function createScheduledEvent</a>
</h2>

```typescript
createScheduledEvent(name: string, scheduleExpression: string, handler: timer.Action, opts?: pulumi.ResourceOptions): void
```

<h2 class="pdoc-module-header" id="createSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L49">function createSubscription</a>
</h2>

```typescript
createSubscription(resName: string, topic: aws.sns.Topic, handler: { ... }): aws.sns.TopicSubscription
```

<h2 class="pdoc-module-header" id="createSwaggerString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L504">function createSwaggerString</a>
</h2>

```typescript
createSwaggerString(spec: SwaggerSpec): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="createTaskDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L449">function createTaskDefinition</a>
</h2>

```typescript
createTaskDefinition(parent: pulumi.Resource, name: string, containers: cloud.Containers, ports?: ExposedPorts): TaskDefinition
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

<h2 class="pdoc-module-header" id="dockerBuild">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L208">function dockerBuild</a>
</h2>

```typescript
dockerBuild(imageName: string, build: cloud.ContainerBuild, cacheFrom: Promise<string[] | undefined>, target?: undefined | string): Promise<void>
```

<h2 class="pdoc-module-header" id="getEndpointHelper">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L695">function getEndpointHelper</a>
</h2>

```typescript
getEndpointHelper(endpoints: Endpoints, containerName: string | undefined, containerPort: number | undefined): Endpoint
```

<h2 class="pdoc-module-header" id="getEndpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L718">function getEndpoints</a>
</h2>

```typescript
getEndpoints(ports: ExposedPorts): pulumi.Output<Endpoints>
```

<h2 class="pdoc-module-header" id="getExecutionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L430">function getExecutionRole</a>
</h2>

```typescript
getExecutionRole(): aws.iam.Role
```

<h2 class="pdoc-module-header" id="getImageName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L141">function getImageName</a>
</h2>

```typescript
getImageName(container: cloud.Container): string
```

<h2 class="pdoc-module-header" id="getOrCreateRepository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L178">function getOrCreateRepository</a>
</h2>

```typescript
getOrCreateRepository(imageName: string): aws.ecr.Repository
```

<h2 class="pdoc-module-header" id="getTaskRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L408">function getTaskRole</a>
</h2>

```typescript
getTaskRole(): aws.iam.Role
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

<h2 class="pdoc-module-header" id="isCloudDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L60">function isCloudDomain</a>
</h2>

```typescript
isCloudDomain(domain: Domain): boolean
```

<h2 class="pdoc-module-header" id="liftResource">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L38">function liftResource</a>
</h2>

```typescript
liftResource<T>(resource: T): pulumi.Output<T>
```

<h2 class="pdoc-module-header" id="localStageImageName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L127">function localStageImageName</a>
</h2>

```typescript
localStageImageName(imageName: string, stage: string): string
```

<h2 class="pdoc-module-header" id="loginToRegistry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L243">function loginToRegistry</a>
</h2>

```typescript
loginToRegistry(registry: Registry): Promise<void>
```

<h2 class="pdoc-module-header" id="makeServiceEnvName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L191">function makeServiceEnvName</a>
</h2>

```typescript
makeServiceEnvName(service: string): string
```

<h2 class="pdoc-module-header" id="parseDockerEngineUpdatesFromBuffer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L281">function parseDockerEngineUpdatesFromBuffer</a>
</h2>

```typescript
parseDockerEngineUpdatesFromBuffer(buffer: Buffer): any[]
```

<h2 class="pdoc-module-header" id="placementConstraintsForHost">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L549">function placementConstraintsForHost</a>
</h2>

```typescript
placementConstraintsForHost(host: cloud.HostProperties | undefined): undefined | { ... }[]
```

<h2 class="pdoc-module-header" id="pullCacheAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L93">function pullCacheAsync</a>
</h2>

```typescript
pullCacheAsync(imageName: string, cacheFrom: cloud.CacheFrom, login: { ... }, repositoryUrl: Promise<string>, logResource: pulumi.Resource): Promise<string[] | undefined>
```

<h2 class="pdoc-module-header" id="pulumiKeyTypeToDynamoKeyType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/table.ts#L20">function pulumiKeyTypeToDynamoKeyType</a>
</h2>

```typescript
pulumiKeyTypeToDynamoKeyType(keyType: cloud.PrimaryKeyType): string
```

<h2 class="pdoc-module-header" id="pushImageAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L259">function pushImageAsync</a>
</h2>

```typescript
pushImageAsync(imageName: string, repositoryUrl: string, tag?: undefined | string): Promise<void>
```

<h2 class="pdoc-module-header" id="runCLICommand">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L303">function runCLICommand</a>
</h2>

```typescript
runCLICommand(cmd: string, args: string[], returnStdout?: undefined | true | false, stdin?: undefined | string): Promise<CommandResult>
```

<h2 class="pdoc-module-header" id="safeS3BucketName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L949">function safeS3BucketName</a>
</h2>

```typescript
safeS3BucketName(apiName: string): string
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/utils.ts#L19">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="swaggerMethod">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L773">function swaggerMethod</a>
</h2>

```typescript
swaggerMethod(method: string): string
```

<h2 class="pdoc-module-header" id="taskMemoryAndCPUForContainers">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L499">function taskMemoryAndCPUForContainers</a>
</h2>

```typescript
taskMemoryAndCPUForContainers(defs: aws.ecs.ContainerDefinition[]): { ... }
```

<h2 class="pdoc-module-header" id="APIGatewayIdentity">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L833">interface APIGatewayIdentity</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L835">property accountId</a>
</h3>

```typescript
accountId?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L838">property apiKey</a>
</h3>

```typescript
apiKey?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L837">property caller</a>
</h3>

```typescript
caller?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L841">property cognitoAuthenticationProvider</a>
</h3>

```typescript
cognitoAuthenticationProvider?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L840">property cognitoAuthenticationType</a>
</h3>

```typescript
cognitoAuthenticationType?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L836">property cognitoIdentityId</a>
</h3>

```typescript
cognitoIdentityId?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L834">property cognitoIdentityPoolId</a>
</h3>

```typescript
cognitoIdentityPoolId?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L839">property sourceIp</a>
</h3>

```typescript
sourceIp?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L844">property user</a>
</h3>

```typescript
user?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L843">property userAgent</a>
</h3>

```typescript
userAgent?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L842">property userArn</a>
</h3>

```typescript
userArn?: undefined | string;
```

<h2 class="pdoc-module-header" id="APIGatewayRequest">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L804">interface APIGatewayRequest</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L818">property body</a>
</h3>

```typescript
body: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L813">property headers</a>
</h3>

```typescript
headers: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L807">property httpMethod</a>
</h3>

```typescript
httpMethod: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L819">property isBase64Encoded</a>
</h3>

```typescript
isBase64Encoded: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L806">property path</a>
</h3>

```typescript
path: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L815">property pathParameters</a>
</h3>

```typescript
pathParameters: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L814">property queryStringParameters</a>
</h3>

```typescript
queryStringParameters: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L817">property requestContext</a>
</h3>

```typescript
requestContext: APIGatewayRequestContext;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L805">property resource</a>
</h3>

```typescript
resource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L816">property stageVariables</a>
</h3>

```typescript
stageVariables: { ... };
```

<h2 class="pdoc-module-header" id="APIGatewayRequestContext">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L822">interface APIGatewayRequestContext</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L823">property accountId</a>
</h3>

```typescript
accountId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L830">property apiId</a>
</h3>

```typescript
apiId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L829">property httpMethod</a>
</h3>

```typescript
httpMethod: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L827">property identity</a>
</h3>

```typescript
identity: APIGatewayIdentity;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L826">property requestId</a>
</h3>

```typescript
requestId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L824">property resourceId</a>
</h3>

```typescript
resourceId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L828">property resourcePath</a>
</h3>

```typescript
resourcePath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L825">property stage</a>
</h3>

```typescript
stage: string;
```

<h2 class="pdoc-module-header" id="APIGatewayResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L847">interface APIGatewayResponse</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L851">property body</a>
</h3>

```typescript
body: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L850">property headers</a>
</h3>

```typescript
headers?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L848">property isBase64Encoded</a>
</h3>

```typescript
isBase64Encoded?: undefined | true | false;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L849">property statusCode</a>
</h3>

```typescript
statusCode: number;
```

<h2 class="pdoc-module-header" id="AWSDomain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L51">interface AWSDomain</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L53">property certificateArn</a>
</h3>

```typescript
certificateArn: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L52">property domainName</a>
</h3>

```typescript
domainName: string;
```

<h2 class="pdoc-module-header" id="ApigatewayIntegration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L576">interface ApigatewayIntegration</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L579">property connectionId</a>
</h3>

```typescript
connectionId?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L573">property connectionType</a>
</h3>

```typescript
connectionType?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L578">property credentials</a>
</h3>

```typescript
credentials?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L570">property httpMethod</a>
</h3>

```typescript
httpMethod: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L569">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L568">property requestParameters</a>
</h3>

```typescript
requestParameters?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L572">property responses</a>
</h3>

```typescript
responses?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L571">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L577">property uri</a>
</h3>

```typescript
uri: string;
```

<h2 class="pdoc-module-header" id="ApigatewayIntegrationAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L582">interface ApigatewayIntegrationAsync</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L585">property connectionId</a>
</h3>

```typescript
connectionId?: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L573">property connectionType</a>
</h3>

```typescript
connectionType?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L584">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L570">property httpMethod</a>
</h3>

```typescript
httpMethod: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L569">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L568">property requestParameters</a>
</h3>

```typescript
requestParameters?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L572">property responses</a>
</h3>

```typescript
responses?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L571">property type</a>
</h3>

```typescript
type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L583">property uri</a>
</h3>

```typescript
uri: pulumi.Output<string>;
```

<h2 class="pdoc-module-header" id="ApigatewayIntegrationBase">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L567">interface ApigatewayIntegrationBase</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L573">property connectionType</a>
</h3>

```typescript
connectionType?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L570">property httpMethod</a>
</h3>

```typescript
httpMethod: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L569">property passthroughBehavior</a>
</h3>

```typescript
passthroughBehavior?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L568">property requestParameters</a>
</h3>

```typescript
requestParameters?: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L572">property responses</a>
</h3>

```typescript
responses?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L571">property type</a>
</h3>

```typescript
type: string;
```

<h2 class="pdoc-module-header" id="BuildResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L33">interface BuildResult</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L34">property digest</a>
</h3>

```typescript
digest: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L35">property stages</a>
</h3>

```typescript
stages: string[];
```

<h2 class="pdoc-module-header" id="CommandResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L294">interface CommandResult</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L295">property code</a>
</h3>

```typescript
code: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L296">property stdout</a>
</h3>

```typescript
stdout?: undefined | string;
```

<h2 class="pdoc-module-header" id="ContainerPortLoadBalancer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L31">interface ContainerPortLoadBalancer</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L32">property loadBalancer</a>
</h3>

```typescript
loadBalancer: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L34">property protocol</a>
</h3>

```typescript
protocol: cloud.ContainerProtocol;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L33">property targetGroup</a>
</h3>

```typescript
targetGroup: aws.elasticloadbalancingv2.TargetGroup;
```

<h2 class="pdoc-module-header" id="Endpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L572">interface Endpoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L232">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L573">property loadBalancer</a>
</h3>

```typescript
loadBalancer: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/node_modules/@pulumi/cloud/service.d.ts#L233">property port</a>
</h3>

```typescript
port: number;
```

<h2 class="pdoc-module-header" id="ExposedPort">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L565">interface ExposedPort</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L566">property host</a>
</h3>

```typescript
host: aws.elasticloadbalancingv2.LoadBalancer;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L567">property hostPort</a>
</h3>

```typescript
hostPort: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L568">property hostProtocol</a>
</h3>

```typescript
hostProtocol: cloud.ContainerProtocol;
```

<h2 class="pdoc-module-header" id="ExposedPorts">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L559">interface ExposedPorts</a>
</h2>
<h2 class="pdoc-module-header" id="ImageOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L195">interface ImageOptions</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L197">property environment</a>
</h3>

```typescript
environment: Record<string, string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L196">property image</a>
</h3>

```typescript
image: string;
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

<h2 class="pdoc-module-header" id="Registry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L27">interface Registry</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L30">property password</a>
</h3>

```typescript
password: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L28">property registry</a>
</h3>

```typescript
registry: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L29">property username</a>
</h3>

```typescript
username: string;
```

<h2 class="pdoc-module-header" id="RequestResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L854">interface RequestResponse</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L855">property req</a>
</h3>

```typescript
req: cloud.Request;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L856">property res</a>
</h3>

```typescript
res: cloud.Response;
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

<h2 class="pdoc-module-header" id="SNSEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L18">interface SNSEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L19">property Records</a>
</h3>

```typescript
Records: SNSRecord[];
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

<h2 class="pdoc-module-header" id="SNSRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L22">interface SNSRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L25">property EventSource</a>
</h3>

```typescript
EventSource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L24">property EventSubscriptionArn</a>
</h3>

```typescript
EventSubscriptionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L23">property EventVersion</a>
</h3>

```typescript
EventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/sns.ts#L26">property Sns</a>
</h3>

```typescript
Sns: SNSItem;
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

<h2 class="pdoc-module-header" id="SwaggerAPIGatewayIntegrationResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L620">interface SwaggerAPIGatewayIntegrationResponse</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L622">property responseParameters</a>
</h3>

```typescript
responseParameters?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L621">property statusCode</a>
</h3>

```typescript
statusCode: string;
```

<h2 class="pdoc-module-header" id="SwaggerHeader">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L610">interface SwaggerHeader</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L612">property items</a>
</h3>

```typescript
items?: SwaggerItems;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L611">property type</a>
</h3>

```typescript
type: string | number | integer | boolean | array;
```

<h2 class="pdoc-module-header" id="SwaggerInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L562">interface SwaggerInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L563">property title</a>
</h3>

```typescript
title: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L564">property version</a>
</h3>

```typescript
version: string;
```

<h2 class="pdoc-module-header" id="SwaggerItems">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L615">interface SwaggerItems</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L617">property items</a>
</h3>

```typescript
items?: SwaggerItems;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L616">property type</a>
</h3>

```typescript
type: string | number | integer | boolean | array;
```

<h2 class="pdoc-module-header" id="SwaggerOperation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L594">interface SwaggerOperation</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L595">property parameters</a>
</h3>

```typescript
parameters?: any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L596">property responses</a>
</h3>

```typescript
responses?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L597">property x-amazon-apigateway-integration</a>
</h3>

```typescript
x-amazon-apigateway-integration: ApigatewayIntegration;
```

<h2 class="pdoc-module-header" id="SwaggerOperationAsync">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L588">interface SwaggerOperationAsync</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L589">property parameters</a>
</h3>

```typescript
parameters?: any[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L590">property responses</a>
</h3>

```typescript
responses?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L591">property x-amazon-apigateway-integration</a>
</h3>

```typescript
x-amazon-apigateway-integration: ApigatewayIntegrationAsync;
```

<h2 class="pdoc-module-header" id="SwaggerResponse">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L600">interface SwaggerResponse</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L601">property description</a>
</h3>

```typescript
description: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L603">property headers</a>
</h3>

```typescript
headers?: undefined | { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L602">property schema</a>
</h3>

```typescript
schema?: SwaggerSchema;
```

<h2 class="pdoc-module-header" id="SwaggerSchema">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L606">interface SwaggerSchema</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L607">property type</a>
</h3>

```typescript
type: string;
```

<h2 class="pdoc-module-header" id="SwaggerSpec">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L495">interface SwaggerSpec</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L497">property info</a>
</h3>

```typescript
info: SwaggerInfo;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L498">property paths</a>
</h3>

```typescript
paths: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L496">property swagger</a>
</h3>

```typescript
swagger: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L499">property x-amazon-apigateway-binary-media-types</a>
</h3>

```typescript
x-amazon-apigateway-binary-media-types?: string[];
```

<h2 class="pdoc-module-header" id="TaskDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L443">interface TaskDefinition</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L445">property logGroup</a>
</h3>

```typescript
logGroup: aws.cloudwatch.LogGroup;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L444">property task</a>
</h3>

```typescript
task: aws.ecs.TaskDefinition;
```

<h2 class="pdoc-module-header" id="Volume">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L732">interface Volume</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L734">method getHostPath</a>
</h3>

```typescript
getHostPath(): any
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L733">method getVolumeName</a>
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

<h2 class="pdoc-module-header" id="apiShape">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/index.ts#L42">let apiShape</a>
</h2>

```typescript
let apiShape: "/Users/luke/go/src/github.com/pulumi/pulumi-cloud/aws/node_modules/@pulumi/cloud/types" =  undefined as any;
```

<h2 class="pdoc-module-header" id="cachedDockerVersionString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L23">let cachedDockerVersionString</a>
</h2>

```typescript
let cachedDockerVersionString: string | undefined;
```

<h2 class="pdoc-module-header" id="dockerPasswordStdin">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/docker.ts#L24">let dockerPasswordStdin</a>
</h2>

```typescript
let dockerPasswordStdin: boolean = false;
```

<h2 class="pdoc-module-header" id="executionRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L429">let executionRole</a>
</h2>

```typescript
let executionRole: aws.iam.Role | undefined;
```

<h2 class="pdoc-module-header" id="taskRole">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L407">let taskRole</a>
</h2>

```typescript
let taskRole: aws.iam.Role | undefined;
```

<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L57">type Domain</a>
</h2>

```typescript
type Domain = cloud.Domain | AWSDomain;
```

<h2 class="pdoc-module-header" id="Endpoints">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/service.ts#L576">type Endpoints</a>
</h2>

```typescript
type Endpoints = { ... };
```

<h2 class="pdoc-module-header" id="HttpEndpoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/api.ts#L956">type HttpEndpoint</a>
</h2>

```typescript
type HttpEndpoint = API;
```

