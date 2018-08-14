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
* <a href="#ProviderArgs">interface ProviderArgs</a>

<a href="/provider.ts">provider.ts</a> 

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
<a class="pdoc-member-name" href="/provider.ts#L9">class Provider</a>
</h2>

The provider type for the openstack package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L9">constructor</a>
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

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="/provider.ts#L52">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L56">property authUrl</a>
</h3>

```typescript
authUrl?: pulumi.Input<string>;
```


The Identity authentication URL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L60">property cacertFile</a>
</h3>

```typescript
cacertFile?: pulumi.Input<string>;
```


A Custom CA certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L64">property cert</a>
</h3>

```typescript
cert?: pulumi.Input<string>;
```


A client certificate to authenticate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L68">property cloud</a>
</h3>

```typescript
cloud?: pulumi.Input<string>;
```


An entry in a `clouds.yaml` file to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L72">property defaultDomain</a>
</h3>

```typescript
defaultDomain?: pulumi.Input<string>;
```


The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L76">property domainId</a>
</h3>

```typescript
domainId?: pulumi.Input<string>;
```


The ID of the Domain to scope to (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L80">property domainName</a>
</h3>

```typescript
domainName?: pulumi.Input<string>;
```


The name of the Domain to scope to (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L81">property endpointType</a>
</h3>

```typescript
endpointType?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L85">property insecure</a>
</h3>

```typescript
insecure?: pulumi.Input<boolean>;
```


Trust self-signed certificates.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L89">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


A client private key to authenticate with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L93">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


Password to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L97">property projectDomainId</a>
</h3>

```typescript
projectDomainId?: pulumi.Input<string>;
```


The ID of the domain where the proejct resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L101">property projectDomainName</a>
</h3>

```typescript
projectDomainName?: pulumi.Input<string>;
```


The name of the domain where the project resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L105">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The OpenStack region to connect to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L109">property swauth</a>
</h3>

```typescript
swauth?: pulumi.Input<boolean>;
```


Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L113">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L117">property tenantName</a>
</h3>

```typescript
tenantName?: pulumi.Input<string>;
```


The name of the Tenant (Identity v2) or Project (Identity v3) to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L121">property token</a>
</h3>

```typescript
token?: pulumi.Input<string>;
```


Authentication token to use as an alternative to username/password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L126">property useOctavia</a>
</h3>

```typescript
useOctavia?: pulumi.Input<boolean>;
```


If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service
(Neutron).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L130">property userDomainId</a>
</h3>

```typescript
userDomainId?: pulumi.Input<string>;
```


The ID of the domain where the user resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L134">property userDomainName</a>
</h3>

```typescript
userDomainName?: pulumi.Input<string>;
```


The name of the domain where the user resides (Identity v3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L138">property userId</a>
</h3>

```typescript
userId?: pulumi.Input<string>;
```


Username to login with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/provider.ts#L142">property userName</a>
</h3>

```typescript
userName?: pulumi.Input<string>;
```


Username to login with.

