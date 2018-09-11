---
title: Module directoryservice
---

<a href="../index.html">@pulumi/aws</a> &gt; directoryservice

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ConditionalForwader">class ConditionalForwader</a>
* <a href="#Directory">class Directory</a>
* <a href="#ConditionalForwaderArgs">interface ConditionalForwaderArgs</a>
* <a href="#ConditionalForwaderState">interface ConditionalForwaderState</a>
* <a href="#DirectoryArgs">interface DirectoryArgs</a>
* <a href="#DirectoryState">interface DirectoryState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts">directoryservice/conditionalForwader.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts">directoryservice/directory.ts</a> 


<h2 class="pdoc-module-header" id="ConditionalForwader">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L10">class ConditionalForwader</a>
</h2>

Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L34">constructor</a>
</h3>

```typescript
new ConditionalForwader(name: string, args: ConditionalForwaderArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ConditionalForwader resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConditionalForwaderState): ConditionalForwader
```


Get an existing ConditionalForwader resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L26">property directoryId</a>
</h3>

```typescript
public directoryId: pulumi.Output<string>;
```


The id of directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L30">property dnsIps</a>
</h3>

```typescript
public dnsIps: pulumi.Output<string[]>;
```


A list of forwarder IP addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L34">property remoteDomainName</a>
</h3>

```typescript
public remoteDomainName: pulumi.Output<string>;
```


The fully qualified domain name of the remote domain for which forwarders will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Directory">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L15">class Directory</a>
</h2>

Provides a Simple or Managed Microsoft directory in AWS Directory Service.

~> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L87">constructor</a>
</h3>

```typescript
new Directory(name: string, args: DirectoryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Directory resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DirectoryState): Directory
```


Get an existing Directory resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L31">property accessUrl</a>
</h3>

```typescript
public accessUrl: pulumi.Output<string>;
```


The access URL for the directory, such as `http://alias.awsapps.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L35">property alias</a>
</h3>

```typescript
public alias: pulumi.Output<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L39">property connectSettings</a>
</h3>

```typescript
public connectSettings: pulumi.Output<{ ... } | undefined>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L43">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L47">property dnsIpAddresses</a>
</h3>

```typescript
public dnsIpAddresses: pulumi.Output<string[]>;
```


A list of IP addresses of the DNS servers for the directory or connector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L51">property edition</a>
</h3>

```typescript
public edition: pulumi.Output<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L55">property enableSso</a>
</h3>

```typescript
public enableSso: pulumi.Output<boolean | undefined>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L63">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L67">property securityGroupId</a>
</h3>

```typescript
public securityGroupId: pulumi.Output<string>;
```


The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L71">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L75">property size</a>
</h3>

```typescript
public size: pulumi.Output<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L79">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L83">property type</a>
</h3>

```typescript
public type: pulumi.Output<string | undefined>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L87">property vpcSettings</a>
</h3>

```typescript
public vpcSettings: pulumi.Output<{ ... } | undefined>;
```


VPC related information about the directory. Fields documented below.

<h2 class="pdoc-module-header" id="ConditionalForwaderArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L91">interface ConditionalForwaderArgs</a>
</h2>

The set of arguments for constructing a ConditionalForwader resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L95">property directoryId</a>
</h3>

```typescript
directoryId: pulumi.Input<string>;
```


The id of directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L99">property dnsIps</a>
</h3>

```typescript
dnsIps: pulumi.Input<pulumi.Input<string>[]>;
```


A list of forwarder IP addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L103">property remoteDomainName</a>
</h3>

```typescript
remoteDomainName: pulumi.Input<string>;
```


The fully qualified domain name of the remote domain for which forwarders will be used.

<h2 class="pdoc-module-header" id="ConditionalForwaderState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L73">interface ConditionalForwaderState</a>
</h2>

Input properties used for looking up and filtering ConditionalForwader resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L77">property directoryId</a>
</h3>

```typescript
directoryId?: pulumi.Input<string>;
```


The id of directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L81">property dnsIps</a>
</h3>

```typescript
dnsIps?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of forwarder IP addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/conditionalForwader.ts#L85">property remoteDomainName</a>
</h3>

```typescript
remoteDomainName?: pulumi.Input<string>;
```


The fully qualified domain name of the remote domain for which forwarders will be used.

<h2 class="pdoc-module-header" id="DirectoryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L210">interface DirectoryArgs</a>
</h2>

The set of arguments for constructing a Directory resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L214">property alias</a>
</h3>

```typescript
alias?: pulumi.Input<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L218">property connectSettings</a>
</h3>

```typescript
connectSettings?: pulumi.Input<{ ... }>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L222">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L226">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L230">property enableSso</a>
</h3>

```typescript
enableSso?: pulumi.Input<boolean>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L234">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L238">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L242">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L246">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L250">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L254">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L258">property vpcSettings</a>
</h3>

```typescript
vpcSettings?: pulumi.Input<{ ... }>;
```


VPC related information about the directory. Fields documented below.

<h2 class="pdoc-module-header" id="DirectoryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L144">interface DirectoryState</a>
</h2>

Input properties used for looking up and filtering Directory resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L148">property accessUrl</a>
</h3>

```typescript
accessUrl?: pulumi.Input<string>;
```


The access URL for the directory, such as `http://alias.awsapps.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L152">property alias</a>
</h3>

```typescript
alias?: pulumi.Input<string>;
```


The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L156">property connectSettings</a>
</h3>

```typescript
connectSettings?: pulumi.Input<{ ... }>;
```


Connector related information about the directory. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L160">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description for the directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L164">property dnsIpAddresses</a>
</h3>

```typescript
dnsIpAddresses?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of IP addresses of the DNS servers for the directory or connector.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L168">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L172">property enableSso</a>
</h3>

```typescript
enableSso?: pulumi.Input<boolean>;
```


Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L176">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The fully qualified name for the directory, such as `corp.example.com`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L180">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the directory administrator or connector user.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L184">property securityGroupId</a>
</h3>

```typescript
securityGroupId?: pulumi.Input<string>;
```


The ID of the security group created by the directory (`SimpleAD` or `MicrosoftAD` only).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L188">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


The short name of the directory, such as `CORP`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L192">property size</a>
</h3>

```typescript
size?: pulumi.Input<string>;
```


The size of the directory (`Small` or `Large` are accepted values).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L196">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L200">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/directoryservice/directory.ts#L204">property vpcSettings</a>
</h3>

```typescript
vpcSettings?: pulumi.Input<{ ... }>;
```


VPC related information about the directory. Fields documented below.

