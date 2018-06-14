---
title: Module mysql
---

<a href="../index.html">@pulumi/azure</a> &gt; mysql

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Configuration">class Configuration</a>
* <a href="#Database">class Database</a>
* <a href="#FirewallRule">class FirewallRule</a>
* <a href="#Server">class Server</a>
* <a href="#ConfigurationArgs">interface ConfigurationArgs</a>
* <a href="#ConfigurationState">interface ConfigurationState</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#FirewallRuleArgs">interface FirewallRuleArgs</a>
* <a href="#FirewallRuleState">interface FirewallRuleState</a>
* <a href="#ServerArgs">interface ServerArgs</a>
* <a href="#ServerState">interface ServerState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts">mysql/configuration.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts">mysql/database.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts">mysql/firewallRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts">mysql/server.ts</a> 


<h2 class="pdoc-module-header" id="Configuration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L9">class Configuration</a>
</h2>

Sets a MySQL Configuration value on a MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L37">constructor</a>
</h3>

```typescript
new Configuration(name: string, args: ConfigurationArgs, opts?: pulumi.ResourceOptions)
```


Create a Configuration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState): Configuration
```


Get an existing Configuration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the MySQL Configuration, which needs [to be a valid MySQL configuration name](https://dev.mysql.com/doc/refman/5.7/en/server-configuration.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L29">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L33">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L37">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


Specifies the value of the MySQL Configuration. See the MySQL documentation for valid values.

<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L9">class Database</a>
</h2>

Manages a MySQL Database within a MySQL Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L41">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L25">property charset</a>
</h3>

```typescript
public charset: pulumi.Output<string>;
```


Specifies the Charset for the MySQL Database, which needs [to be a valid MySQL Charset](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L29">property collation</a>
</h3>

```typescript
public collation: pulumi.Output<string>;
```


Specifies the Collation for the MySQL Database, which needs [to be a valid MySQL Collation](https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the MySQL Database, which needs [to be a valid MySQL identifier](https://dev.mysql.com/doc/refman/5.7/en/identifiers.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L37">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L41">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FirewallRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L9">class FirewallRule</a>
</h2>

Manages a Firewall Rule for a MySQL Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L41">constructor</a>
</h3>

```typescript
new FirewallRule(name: string, args: FirewallRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a FirewallRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallRuleState): FirewallRule
```


Get an existing FirewallRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L25">property endIpAddress</a>
</h3>

```typescript
public endIpAddress: pulumi.Output<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L37">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L41">property startIpAddress</a>
</h3>

```typescript
public startIpAddress: pulumi.Output<string>;
```


Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Server">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L9">class Server</a>
</h2>

Manages a MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L65">constructor</a>
</h3>

```typescript
new Server(name: string, args: ServerArgs, opts?: pulumi.ResourceOptions)
```


Create a Server resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState): Server
```


Get an existing Server resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L25">property administratorLogin</a>
</h3>

```typescript
public administratorLogin: pulumi.Output<string>;
```


The Administrator Login for the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L29">property administratorLoginPassword</a>
</h3>

```typescript
public administratorLoginPassword: pulumi.Output<string>;
```


The Password associated with the `administrator_login` for the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L33">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L37">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the SKU Name for this MySQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L49">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L53">property sslEnforcement</a>
</h3>

```typescript
public sslEnforcement: pulumi.Output<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enforced` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L57">property storageProfile</a>
</h3>

```typescript
public storageProfile: pulumi.Output<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L61">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L65">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


Specifies the version of MySQL to use. Valid values are `5.6` and `5.7`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L100">interface ConfigurationArgs</a>
</h2>

The set of arguments for constructing a Configuration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Configuration, which needs [to be a valid MySQL configuration name](https://dev.mysql.com/doc/refman/5.7/en/server-configuration.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L108">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L112">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L116">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


Specifies the value of the MySQL Configuration. See the MySQL documentation for valid values.

<h2 class="pdoc-module-header" id="ConfigurationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L78">interface ConfigurationState</a>
</h2>

Input properties used for looking up and filtering Configuration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L82">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Configuration, which needs [to be a valid MySQL configuration name](https://dev.mysql.com/doc/refman/5.7/en/server-configuration.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L86">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L90">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/configuration.ts#L94">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


Specifies the value of the MySQL Configuration. See the MySQL documentation for valid values.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L113">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L117">property charset</a>
</h3>

```typescript
charset: pulumi.Input<string>;
```


Specifies the Charset for the MySQL Database, which needs [to be a valid MySQL Charset](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L121">property collation</a>
</h3>

```typescript
collation: pulumi.Input<string>;
```


Specifies the Collation for the MySQL Database, which needs [to be a valid MySQL Collation](https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Database, which needs [to be a valid MySQL identifier](https://dev.mysql.com/doc/refman/5.7/en/identifiers.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L129">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L133">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L87">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L91">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


Specifies the Charset for the MySQL Database, which needs [to be a valid MySQL Charset](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L95">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


Specifies the Collation for the MySQL Database, which needs [to be a valid MySQL Collation](https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Database, which needs [to be a valid MySQL identifier](https://dev.mysql.com/doc/refman/5.7/en/identifiers.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/database.ts#L107">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FirewallRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L113">interface FirewallRuleArgs</a>
</h2>

The set of arguments for constructing a FirewallRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L117">property endIpAddress</a>
</h3>

```typescript
endIpAddress: pulumi.Input<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L125">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L129">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L133">property startIpAddress</a>
</h3>

```typescript
startIpAddress: pulumi.Input<string>;
```


Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FirewallRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L87">interface FirewallRuleState</a>
</h2>

Input properties used for looking up and filtering FirewallRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L91">property endIpAddress</a>
</h3>

```typescript
endIpAddress?: pulumi.Input<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the MySQL Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L99">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the MySQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L103">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/firewallRule.ts#L107">property startIpAddress</a>
</h3>

```typescript
startIpAddress?: pulumi.Input<string>;
```


Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L185">interface ServerArgs</a>
</h2>

The set of arguments for constructing a Server resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L189">property administratorLogin</a>
</h3>

```typescript
administratorLogin: pulumi.Input<string>;
```


The Administrator Login for the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L193">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword: pulumi.Input<string>;
```


The Password associated with the `administrator_login` for the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L197">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L201">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the SKU Name for this MySQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L205">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L209">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L213">property sslEnforcement</a>
</h3>

```typescript
sslEnforcement: pulumi.Input<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enforced` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L217">property storageProfile</a>
</h3>

```typescript
storageProfile: pulumi.Input<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L221">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L225">property version</a>
</h3>

```typescript
version: pulumi.Input<string>;
```


Specifies the version of MySQL to use. Valid values are `5.6` and `5.7`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L135">interface ServerState</a>
</h2>

Input properties used for looking up and filtering Server resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L139">property administratorLogin</a>
</h3>

```typescript
administratorLogin?: pulumi.Input<string>;
```


The Administrator Login for the MySQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L143">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword?: pulumi.Input<string>;
```


The Password associated with the `administrator_login` for the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L147">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L151">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the SKU Name for this MySQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/mysql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L159">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the MySQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L163">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L167">property sslEnforcement</a>
</h3>

```typescript
sslEnforcement?: pulumi.Input<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enforced` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L171">property storageProfile</a>
</h3>

```typescript
storageProfile?: pulumi.Input<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L175">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/mysql/server.ts#L179">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Specifies the version of MySQL to use. Valid values are `5.6` and `5.7`. Changing this forces a new resource to be created.

