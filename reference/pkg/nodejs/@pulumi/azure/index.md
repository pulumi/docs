---
title: Package @pulumi/azure
---


Node.js:

```javascript
var azure = require("@pulumi/azure");
```

ES6 modules:

```typescript
import * as azure from "@pulumi/azure";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Provider">class Provider</a>
* <a href="#getEnv">function getEnv</a>
* <a href="#getEnvBoolean">function getEnvBoolean</a>
* <a href="#getEnvNumber">function getEnvNumber</a>
* <a href="#requireWithDefault">function requireWithDefault</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts">provider.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/utilities.ts">utilities.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="ad">ad</a>
* <a href="apimanagement">apimanagement</a>
* <a href="appinsights">appinsights</a>
* <a href="appservice">appservice</a>
* <a href="automation">automation</a>
* <a href="autoscale">autoscale</a>
* <a href="cdn">cdn</a>
* <a href="cognitive">cognitive</a>
* <a href="compute">compute</a>
* <a href="config">config</a>
* <a href="containerservice">containerservice</a>
* <a href="core">core</a>
* <a href="cosmosdb">cosmosdb</a>
* <a href="databricks">databricks</a>
* <a href="datalake">datalake</a>
* <a href="devtest">devtest</a>
* <a href="dns">dns</a>
* <a href="eventhub">eventhub</a>
* <a href="iot">iot</a>
* <a href="keyvault">keyvault</a>
* <a href="lb">lb</a>
* <a href="logicapps">logicapps</a>
* <a href="managementgroups">managementgroups</a>
* <a href="managementresource">managementresource</a>
* <a href="monitoring">monitoring</a>
* <a href="msi">msi</a>
* <a href="mysql">mysql</a>
* <a href="network">network</a>
* <a href="notificationhub">notificationhub</a>
* <a href="operationalinsights">operationalinsights</a>
* <a href="policy">policy</a>
* <a href="postgresql">postgresql</a>
* <a href="recoveryservices">recoveryservices</a>
* <a href="redis">redis</a>
* <a href="relay">relay</a>
* <a href="role">role</a>
* <a href="scheduler">scheduler</a>
* <a href="search">search</a>
* <a href="securitycenter">securitycenter</a>
* <a href="servicefabric">servicefabric</a>
* <a href="sql">sql</a>
* <a href="storage">storage</a>
* <a href="trafficmanager">trafficmanager</a>

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L10">class Provider</a>
</h2>

The provider type for the azurerm package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L10">constructor</a>
</h3>

```typescript
new Provider(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getEnv">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/utilities.ts#L7">function getEnv</a>
</h2>

```typescript
getEnv(vars: string[]): string | undefined
```

<h2 class="pdoc-module-header" id="getEnvBoolean">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/utilities.ts#L17">function getEnvBoolean</a>
</h2>

```typescript
getEnvBoolean(vars: string[]): boolean | undefined
```

<h2 class="pdoc-module-header" id="getEnvNumber">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/utilities.ts#L32">function getEnvNumber</a>
</h2>

```typescript
getEnvNumber(vars: string[]): number | undefined
```

<h2 class="pdoc-module-header" id="requireWithDefault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/utilities.ts#L43">function requireWithDefault</a>
</h2>

```typescript
requireWithDefault<T>(req: { ... }, def: T | undefined): T
```

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L39">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L40">property clientId</a>
</h3>

```typescript
clientId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L41">property clientSecret</a>
</h3>

```typescript
clientSecret?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L42">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L43">property msiEndpoint</a>
</h3>

```typescript
msiEndpoint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L44">property skipCredentialsValidation</a>
</h3>

```typescript
skipCredentialsValidation?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L45">property skipProviderRegistration</a>
</h3>

```typescript
skipProviderRegistration?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L46">property subscriptionId</a>
</h3>

```typescript
subscriptionId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L47">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/provider.ts#L48">property useMsi</a>
</h3>

```typescript
useMsi?: pulumi.Input<boolean>;
```

