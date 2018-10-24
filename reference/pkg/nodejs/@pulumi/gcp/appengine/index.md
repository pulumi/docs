---
title: Module appengine
---

<a href="../index.html">@pulumi/gcp</a> &gt; appengine

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Application">class Application</a>
* <a href="#ApplicationArgs">interface ApplicationArgs</a>
* <a href="#ApplicationState">interface ApplicationState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts">appengine/application.ts</a> 


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L15">class Application</a>
</h2>

Allows creation and management of an App Engine application.

~> App Engine applications cannot be deleted once they're created; you have to delete the
   entire project to delete the application. Terraform will report the application has been
   successfully deleted; this is a limitation of Terraform, and will go away in the future.
   Terraform is not able to delete App Engine applications.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L69">constructor</a>
</h3>

```typescript
new Application(name: string, args: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState): Application
```


Get an existing Application resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L31">property authDomain</a>
</h3>

```typescript
public authDomain: pulumi.Output<string>;
```


The domain to authenticate users with when using App Engine's User API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L35">property codeBucket</a>
</h3>

```typescript
public codeBucket: pulumi.Output<string>;
```


The GCS bucket code is being stored in for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L39">property defaultBucket</a>
</h3>

```typescript
public defaultBucket: pulumi.Output<string>;
```


The GCS bucket content is being stored in for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L43">property defaultHostname</a>
</h3>

```typescript
public defaultHostname: pulumi.Output<string>;
```


The default hostname for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L47">property featureSettings</a>
</h3>

```typescript
public featureSettings: pulumi.Output<{ ... }>;
```


A block of optional settings to configure specific App Engine features:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L51">property gcrDomain</a>
</h3>

```typescript
public gcrDomain: pulumi.Output<string>;
```


The GCR domain used for storing managed Docker images for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L56">property locationId</a>
</h3>

```typescript
public locationId: pulumi.Output<string>;
```


The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Unique name of the app, usually `apps/{PROJECT_ID}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L61">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L65">property servingStatus</a>
</h3>

```typescript
public servingStatus: pulumi.Output<string>;
```


The serving status of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L69">property urlDispatchRules</a>
</h3>

```typescript
public urlDispatchRules: pulumi.Output<{ ... }[]>;
```


A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L166">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L170">property authDomain</a>
</h3>

```typescript
authDomain?: pulumi.Input<string>;
```


The domain to authenticate users with when using App Engine's User API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L174">property featureSettings</a>
</h3>

```typescript
featureSettings?: pulumi.Input<{ ... }>;
```


A block of optional settings to configure specific App Engine features:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L179">property locationId</a>
</h3>

```typescript
locationId: pulumi.Input<string>;
```


The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L180">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L184">property servingStatus</a>
</h3>

```typescript
servingStatus?: pulumi.Input<string>;
```


The serving status of the app.

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L118">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L122">property authDomain</a>
</h3>

```typescript
authDomain?: pulumi.Input<string>;
```


The domain to authenticate users with when using App Engine's User API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L126">property codeBucket</a>
</h3>

```typescript
codeBucket?: pulumi.Input<string>;
```


The GCS bucket code is being stored in for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L130">property defaultBucket</a>
</h3>

```typescript
defaultBucket?: pulumi.Input<string>;
```


The GCS bucket content is being stored in for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L134">property defaultHostname</a>
</h3>

```typescript
defaultHostname?: pulumi.Input<string>;
```


The default hostname for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L138">property featureSettings</a>
</h3>

```typescript
featureSettings?: pulumi.Input<{ ... }>;
```


A block of optional settings to configure specific App Engine features:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L142">property gcrDomain</a>
</h3>

```typescript
gcrDomain?: pulumi.Input<string>;
```


The GCR domain used for storing managed Docker images for this app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L147">property locationId</a>
</h3>

```typescript
locationId?: pulumi.Input<string>;
```


The [location](https://cloud.google.com/appengine/docs/locations)
to serve the app from.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Unique name of the app, usually `apps/{PROJECT_ID}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L152">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L156">property servingStatus</a>
</h3>

```typescript
servingStatus?: pulumi.Input<string>;
```


The serving status of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/appengine/application.ts#L160">property urlDispatchRules</a>
</h3>

```typescript
urlDispatchRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of dispatch rule blocks. Each block has a `domain`, `path`, and `service` field.

