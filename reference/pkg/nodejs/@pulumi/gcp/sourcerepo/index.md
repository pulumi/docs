---
title: Module sourcerepo
---

<a href="../index.html">@pulumi/gcp</a> &gt; sourcerepo

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Repository">class Repository</a>
* <a href="#RepositoryArgs">interface RepositoryArgs</a>
* <a href="#RepositoryState">interface RepositoryState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts">sourcerepo/repository.ts</a> 


<h2 class="pdoc-module-header" id="Repository">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L11">class Repository</a>
</h2>

For more information, see [the official
documentation](https://cloud.google.com/source-repositories/) and
[API](https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L40">constructor</a>
</h3>

```typescript
new Repository(name: string, args?: RepositoryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Repository resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryState): Repository
```


Get an existing Repository resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L27">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the repository that will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L32">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L36">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


The size of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L40">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The url to clone the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="RepositoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L95">interface RepositoryArgs</a>
</h2>

The set of arguments for constructing a Repository resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the repository that will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L104">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="RepositoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L72">interface RepositoryState</a>
</h2>

Input properties used for looking up and filtering Repository resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the repository that will be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L81">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L85">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


The size of the repository.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sourcerepo/repository.ts#L89">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The url to clone the repository.

