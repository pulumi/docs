---
title: Module athena
---

<a href="../index.html">@pulumi/aws</a> &gt; athena

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Database">class Database</a>
* <a href="#NamedQuery">class NamedQuery</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#NamedQueryArgs">interface NamedQueryArgs</a>
* <a href="#NamedQueryState">interface NamedQueryState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts">athena/database.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts">athena/namedQuery.ts</a> 


<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L10">class Database</a>
</h2>

Provides an Athena database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L38">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L26">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


Name of s3 bucket to save the results of the query execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L30">property encryptionConfiguration</a>
</h3>

```typescript
public encryptionConfiguration: pulumi.Output<{ ... } | undefined>;
```


The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `encryption_configuration` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L34">property forceDestroy</a>
</h3>

```typescript
public forceDestroy: pulumi.Output<boolean | undefined>;
```


A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the database to create.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="NamedQuery">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L10">class NamedQuery</a>
</h2>

Provides an Athena Named Query resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L38">constructor</a>
</h3>

```typescript
new NamedQuery(name: string, args: NamedQueryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NamedQuery resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamedQueryState): NamedQuery
```


Get an existing NamedQuery resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L26">property database</a>
</h3>

```typescript
public database: pulumi.Output<string>;
```


The database to which the query belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A brief explanation of the query. Maximum length of 1024.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The plain language name for the query. Maximum length of 128.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L38">property query</a>
</h3>

```typescript
public query: pulumi.Output<string>;
```


The text of the query itself. In other words, all query statements. Maximum length of 262144.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L95">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L99">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string>;
```


Name of s3 bucket to save the results of the query execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L103">property encryptionConfiguration</a>
</h3>

```typescript
encryptionConfiguration?: pulumi.Input<{ ... }>;
```


The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `encryption_configuration` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L107">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the database to create.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L73">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L77">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string>;
```


Name of s3 bucket to save the results of the query execution.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L81">property encryptionConfiguration</a>
</h3>

```typescript
encryptionConfiguration?: pulumi.Input<{ ... }>;
```


The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `encryption_configuration` block is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L85">property forceDestroy</a>
</h3>

```typescript
forceDestroy?: pulumi.Input<boolean>;
```


A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/database.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the database to create.

<h2 class="pdoc-module-header" id="NamedQueryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L98">interface NamedQueryArgs</a>
</h2>

The set of arguments for constructing a NamedQuery resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L102">property database</a>
</h3>

```typescript
database: pulumi.Input<string>;
```


The database to which the query belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief explanation of the query. Maximum length of 1024.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The plain language name for the query. Maximum length of 128.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L114">property query</a>
</h3>

```typescript
query: pulumi.Input<string>;
```


The text of the query itself. In other words, all query statements. Maximum length of 262144.

<h2 class="pdoc-module-header" id="NamedQueryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L76">interface NamedQueryState</a>
</h2>

Input properties used for looking up and filtering NamedQuery resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L80">property database</a>
</h3>

```typescript
database?: pulumi.Input<string>;
```


The database to which the query belongs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L84">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A brief explanation of the query. Maximum length of 1024.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The plain language name for the query. Maximum length of 128.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/athena/namedQuery.ts#L92">property query</a>
</h3>

```typescript
query?: pulumi.Input<string>;
```


The text of the query itself. In other words, all query statements. Maximum length of 262144.

