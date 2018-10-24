---
title: Module monitoring
---

<a href="../index.html">@pulumi/gcp</a> &gt; monitoring

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AlertPolicy">class AlertPolicy</a>
* <a href="#AlertPolicyArgs">interface AlertPolicyArgs</a>
* <a href="#AlertPolicyState">interface AlertPolicyState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts">monitoring/alertPolicy.ts</a> 


<h2 class="pdoc-module-header" id="AlertPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L7">class AlertPolicy</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L28">constructor</a>
</h3>

```typescript
new AlertPolicy(name: string, args: AlertPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AlertPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L16">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertPolicyState): AlertPolicy
```


Get an existing AlertPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L20">property combiner</a>
</h3>

```typescript
public combiner: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L21">property conditions</a>
</h3>

```typescript
public conditions: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L22">property creationRecord</a>
</h3>

```typescript
public creationRecord: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L23">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L24">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L25">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L27">property notificationChannels</a>
</h3>

```typescript
public notificationChannels: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L28">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AlertPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L97">interface AlertPolicyArgs</a>
</h2>

The set of arguments for constructing a AlertPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L98">property combiner</a>
</h3>

```typescript
combiner: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L99">property conditions</a>
</h3>

```typescript
conditions: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L100">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L101">property enabled</a>
</h3>

```typescript
enabled: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L102">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L103">property notificationChannels</a>
</h3>

```typescript
notificationChannels?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L104">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="AlertPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L82">interface AlertPolicyState</a>
</h2>

Input properties used for looking up and filtering AlertPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L83">property combiner</a>
</h3>

```typescript
combiner?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L84">property conditions</a>
</h3>

```typescript
conditions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L85">property creationRecord</a>
</h3>

```typescript
creationRecord?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L86">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L87">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L88">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L90">property notificationChannels</a>
</h3>

```typescript
notificationChannels?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/monitoring/alertPolicy.ts#L91">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

