---
title: Package @pulumi/gcp
---


Node.js:

```javascript
var gcp = require("@pulumi/gcp");
```

ES6 modules:

```typescript
import * as gcp from "@pulumi/gcp";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Provider">class Provider</a>
* <a href="#ProviderArgs">interface ProviderArgs</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts">provider.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>

* <a href="bigquery">bigquery</a>
* <a href="bigtable">bigtable</a>
* <a href="cloudbuild">cloudbuild</a>
* <a href="cloudfunctions">cloudfunctions</a>
* <a href="compute">compute</a>
* <a href="config">config</a>
* <a href="container">container</a>
* <a href="dataflow">dataflow</a>
* <a href="dataproc">dataproc</a>
* <a href="dns">dns</a>
* <a href="endpoints">endpoints</a>
* <a href="folder">folder</a>
* <a href="kms">kms</a>
* <a href="logging">logging</a>
* <a href="organizations">organizations</a>
* <a href="projects">projects</a>
* <a href="pubsub">pubsub</a>
* <a href="redis">redis</a>
* <a href="resourcemanager">resourcemanager</a>
* <a href="runtimeconfig">runtimeconfig</a>
* <a href="serverless">serverless</a>
* <a href="serviceAccount">serviceAccount</a>
* <a href="sourcerepo">sourcerepo</a>
* <a href="spanner">spanner</a>
* <a href="sql">sql</a>
* <a href="storage">storage</a>

<h2 class="pdoc-module-header" id="Provider">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L9">class Provider</a>
</h2>

The provider type for the google package

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L9">constructor</a>
</h3>

```typescript
new Provider(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions)
```


Create a Provider resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProviderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L33">interface ProviderArgs</a>
</h2>

The set of arguments for constructing a Provider resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L34">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L35">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L36">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/provider.ts#L37">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```

