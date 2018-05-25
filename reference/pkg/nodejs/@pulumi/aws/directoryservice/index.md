---
title: Module directoryservice
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Directory">class Directory</a>
* <a href="#DirectoryArgs">interface DirectoryArgs</a>
* <a href="#DirectoryState">interface DirectoryState</a>

<a href="/directoryservice/directory.ts">directoryservice/directory.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Directory">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L12">class Directory</a>
</h2>

Provides a Simple or Managed Microsoft directory in AWS Directory Service.

~> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L84">constructor</a>
</h3>

```typescript
new Directory(name: string, args: DirectoryArgs, opts?: pulumi.ResourceOptions)
```


Create a Directory resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Directory(name: string, state?: DirectoryState, opts?: pulumi.ResourceOptions)
```


Create a Directory resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DirectoryState): Directory
```


Get an existing Directory resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L28">property accessUrl</a>
</h3>

```typescript
public accessUrl: pulumi.Output<string>;
```


The access URL for the directory, such as `http://alias.awsapps.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L32">property alias</a>
</h3>

```typescript
public alias: pulumi.Output<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L36">property connectSettings</a>
</h3>

```typescript
public connectSettings: pulumi.Output<{ ... } | undefined>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L40">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L44">property dnsIpAddresses</a>
</h3>

```typescript
public dnsIpAddresses: pulumi.Output<string[]>;
```


A list of IP addresses of the DNS servers for the directory or connector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L48">property edition</a>
</h3>

```typescript
public edition: pulumi.Output<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L52">property enableSso</a>
</h3>

```typescript
public enableSso: pulumi.Output<boolean | undefined>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L56">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L60">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L64">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L68">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L72">property size</a>
</h3>

```typescript
public size: pulumi.Output<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L76">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L80">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L84">property vpcSettings</a>
</h3>

```typescript
public vpcSettings: pulumi.Output<{ ... } | undefined>;
```


VPC related information about the directory. Fields documented below.

<h2 class="pdoc-module-header" id="DirectoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L209">interface DirectoryArgs</a>
</h2>

The set of arguments for constructing a Directory resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L213">property alias</a>
</h3>

```typescript
alias?: pulumi.Input<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L217">property connectSettings</a>
</h3>

```typescript
connectSettings?: pulumi.Input<{ ... }>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L221">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L225">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L229">property enableSso</a>
</h3>

```typescript
enableSso?: pulumi.Input<boolean>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L233">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L237">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L241">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L245">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L249">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L253">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L257">property vpcSettings</a>
</h3>

```typescript
vpcSettings?: pulumi.Input<{ ... }>;
```


VPC related information about the directory. Fields documented below.

<h2 class="pdoc-module-header" id="DirectoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L143">interface DirectoryState</a>
</h2>

Input properties used for looking up and filtering Directory resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L147">property accessUrl</a>
</h3>

```typescript
accessUrl?: pulumi.Input<string>;
```


The access URL for the directory, such as `http://alias.awsapps.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L151">property alias</a>
</h3>

```typescript
alias?: pulumi.Input<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L155">property connectSettings</a>
</h3>

```typescript
connectSettings?: pulumi.Input<{ ... }>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L159">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L163">property dnsIpAddresses</a>
</h3>

```typescript
dnsIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IP addresses of the DNS servers for the directory or connector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L167">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L171">property enableSso</a>
</h3>

```typescript
enableSso?: pulumi.Input<boolean>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L175">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L179">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L183">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L187">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L191">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L195">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L199">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/directoryservice/directory.ts#L203">property vpcSettings</a>
</h3>

```typescript
vpcSettings?: pulumi.Input<{ ... }>;
```


VPC related information about the directory. Fields documented below.

