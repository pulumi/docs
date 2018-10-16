---
title: Package @pulumi/kubernetes
---


Node.js:

```javascript
var kubernetes = require("@pulumi/kubernetes");
```

ES6 modules:

```typescript
import * as kubernetes from "@pulumi/kubernetes";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Provider">class Provider</a>
* <a href="#fetch">function fetch</a>
* <a href="#quotePath">function quotePath</a>
* <a href="#quoteWindowsPath">function quoteWindowsPath</a>
* <a href="#FetchOpts">interface FetchOpts</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>

<a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts">helm.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/path.ts">path.ts</a> <a href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts">provider.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="admissionregistration">admissionregistration</a>
* <a href="apiextensions">apiextensions</a>
* <a href="apiregistration">apiregistration</a>
* <a href="apps">apps</a>
* <a href="authentication">authentication</a>
* <a href="authorization">authorization</a>
* <a href="autoscaling">autoscaling</a>
* <a href="batch">batch</a>
* <a href="certificates">certificates</a>
* <a href="core">core</a>
* <a href="events">events</a>
* <a href="extensions">extensions</a>
* <a href="meta">meta</a>
* <a href="networking">networking</a>
* <a href="pkg">pkg</a>
* <a href="policy">policy</a>
* <a href="rbac">rbac</a>
* <a href="scheduling">scheduling</a>
* <a href="settings">settings</a>
* <a href="storage">storage</a>
* <a href="tests">tests</a>
* <a href="types">types</a>
* <a href="v2">v2</a>
* <a href="yaml">yaml</a>

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1412">class Provider</a>
</h2>

The provider type for the kubernetes package.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1412">constructor</a>
</h3>

```typescript
new Provider(name: string, args: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="fetch">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L224">function fetch</a>
</h2>

```typescript
fetch(chart: string, opts?: FetchOpts): void
```

<h2 class="pdoc-module-header" id="quotePath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/path.ts#L3">function quotePath</a>
</h2>

```typescript
quotePath(path: string): string
```

<h2 class="pdoc-module-header" id="quoteWindowsPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/path.ts#L11">function quoteWindowsPath</a>
</h2>

```typescript
quoteWindowsPath(path: string): string
```

<h2 class="pdoc-module-header" id="FetchOpts">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L163">interface FetchOpts</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L168">property caFile</a>
</h3>

```typescript
caFile?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L171">property certFile</a>
</h3>

```typescript
certFile?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L178">property destination</a>
</h3>

```typescript
destination?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L201">property devel</a>
</h3>

```typescript
devel?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L197">property home</a>
</h3>

```typescript
home?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L174">property keyFile</a>
</h3>

```typescript
keyFile?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L181">property keyring</a>
</h3>

```typescript
keyring?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L184">property password</a>
</h3>

```typescript
password?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L204">property prov</a>
</h3>

```typescript
prov?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L187">property repo</a>
</h3>

```typescript
repo?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L207">property untar</a>
</h3>

```typescript
untar?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L191">property untardir</a>
</h3>

```typescript
untardir?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L194">property username</a>
</h3>

```typescript
username?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L210">property verify</a>
</h3>

```typescript
verify?: undefined | false | true;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/helm.ts#L165">property version</a>
</h3>

```typescript
version?: undefined | string;
```

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1434">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1438">property cluster</a>
</h3>

```typescript
cluster?: pulumi.Input<string>;
```


If present, the name of the kubeconfig cluster to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1442">property context</a>
</h3>

```typescript
context?: pulumi.Input<string>;
```


If present, the name of the kubeconfig context to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1446">property kubeconfig</a>
</h3>

```typescript
kubeconfig?: pulumi.Input<string>;
```


The contents of a kubeconfig file. If this is set, this config will be used instead of $KUBECONFIG.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs/provider.ts#L1450">property namespace</a>
</h3>

```typescript
namespace?: pulumi.Input<string>;
```


If present, the namespace scope to use.

