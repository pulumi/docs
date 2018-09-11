---
title: Package @pulumi/openstack
---


Node.js:

```javascript
var openstack = require("@pulumi/openstack");
```

ES6 modules:

```typescript
import * as openstack from "@pulumi/openstack";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Provider">class Provider</a>
* <a href="#getEnv">function getEnv</a>
* <a href="#getEnvBoolean">function getEnvBoolean</a>
* <a href="#getEnvNumber">function getEnvNumber</a>
* <a href="#requireWithDefault">function requireWithDefault</a>
* <a href="#unwrap">function unwrap</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>

<a href="/provider.ts">provider.ts</a> <a href="/utilities.ts">utilities.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="blockstorage">blockstorage</a>
* <a href="compute">compute</a>
* <a href="config">config</a>
* <a href="database">database</a>
* <a href="dns">dns</a>
* <a href="firewall">firewall</a>
* <a href="identity">identity</a>
* <a href="images">images</a>
* <a href="loadbalancer">loadbalancer</a>
* <a href="networking">networking</a>
* <a href="objectstorage">objectstorage</a>
* <a href="vpnaas">vpnaas</a>

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="/provider.ts#L10">class Provider</a>
</h2>

The provider type for the openstack package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L10">constructor</a>
</h3>

```typescript
new Provider(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getEnv">
<a class="pdoc-member-name" href="/utilities.ts#L7">function getEnv</a>
</h2>

```typescript
getEnv(vars: string[]): string | undefined
```

<h2 class="pdoc-module-header" id="getEnvBoolean">
<a class="pdoc-member-name" href="/utilities.ts#L17">function getEnvBoolean</a>
</h2>

```typescript
getEnvBoolean(vars: string[]): boolean | undefined
```

<h2 class="pdoc-module-header" id="getEnvNumber">
<a class="pdoc-member-name" href="/utilities.ts#L32">function getEnvNumber</a>
</h2>

```typescript
getEnvNumber(vars: string[]): number | undefined
```

<h2 class="pdoc-module-header" id="requireWithDefault">
<a class="pdoc-member-name" href="/utilities.ts#L43">function requireWithDefault</a>
</h2>

```typescript
requireWithDefault<T>(req: { ... }, def: T | undefined): T
```

<h2 class="pdoc-module-header" id="unwrap">
<a class="pdoc-member-name" href="/utilities.ts#L54">function unwrap</a>
</h2>

```typescript
unwrap(val: pulumi.Input<any>): pulumi.Output<any>
```

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="/provider.ts#L53">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L57">property authUrl</a>
</h3>

```typescript
authUrl?: pulumi.Input<string>;
```


The Identity authentication URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L61">property cacertFile</a>
</h3>

```typescript
cacertFile?: pulumi.Input<string>;
```


A Custom CA certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L65">property cert</a>
</h3>

```typescript
cert?: pulumi.Input<string>;
```


A client certificate to authenticate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L69">property cloud</a>
</h3>

```typescript
cloud?: pulumi.Input<string>;
```


An entry in a `clouds.yaml` file to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L73">property defaultDomain</a>
</h3>

```typescript
defaultDomain?: pulumi.Input<string>;
```


The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L77">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The ID of the Domain to scope to (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L81">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The name of the Domain to scope to (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L82">property endpointType</a>
</h3>

```typescript
endpointType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L86">property insecure</a>
</h3>

```typescript
insecure?: pulumi.Input<boolean>;
```


Trust self-signed certificates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L90">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


A client private key to authenticate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L94">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


Password to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L98">property projectDomainId</a>
</h3>

```typescript
projectDomainId?: pulumi.Input<string>;
```


The ID of the domain where the proejct resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L102">property projectDomainName</a>
</h3>

```typescript
projectDomainName?: pulumi.Input<string>;
```


The name of the domain where the project resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L106">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The OpenStack region to connect to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L110">property swauth</a>
</h3>

```typescript
swauth?: pulumi.Input<boolean>;
```


Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L114">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L118">property tenantName</a>
</h3>

```typescript
tenantName?: pulumi.Input<string>;
```


The name of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L122">property token</a>
</h3>

```typescript
token?: pulumi.Input<string>;
```


Authentication token to use as an alternative to username/password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L127">property useOctavia</a>
</h3>

```typescript
useOctavia?: pulumi.Input<boolean>;
```


If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service
(Neutron).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L131">property userDomainId</a>
</h3>

```typescript
userDomainId?: pulumi.Input<string>;
```


The ID of the domain where the user resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L135">property userDomainName</a>
</h3>

```typescript
userDomainName?: pulumi.Input<string>;
```


The name of the domain where the user resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L139">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```


Username to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L143">property userName</a>
</h3>

```typescript
userName?: pulumi.Input<string>;
```


Username to login with.

