---
title: Module postgresql
---

<a href="../index.html">@pulumi/azure</a> &gt; postgresql

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

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts">postgresql/configuration.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts">postgresql/database.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts">postgresql/firewallRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts">postgresql/server.ts</a> 


<h2 class="pdoc-module-header" id="Configuration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L10">class Configuration</a>
</h2>

Sets a PostgreSQL Configuration value on a PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L38">constructor</a>
</h3>

```typescript
new Configuration(name: string, args: ConfigurationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Configuration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState): Configuration
```


Get an existing Configuration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L30">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L34">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L38">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.

<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L10">class Database</a>
</h2>

Manages a PostgreSQL Database within a PostgreSQL Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L43">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L26">property charset</a>
</h3>

```typescript
public charset: pulumi.Output<string>;
```


Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L30">property collation</a>
</h3>

```typescript
public collation: pulumi.Output<string>;
```


Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L39">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L43">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FirewallRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L10">class FirewallRule</a>
</h2>

Manages a Firewall Rule for a PostgreSQL Server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L43">constructor</a>
</h3>

```typescript
new FirewallRule(name: string, args: FirewallRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FirewallRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallRuleState): FirewallRule
```


Get an existing FirewallRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L26">property endIpAddress</a>
</h3>

```typescript
public endIpAddress: pulumi.Output<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L35">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L39">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L43">property startIpAddress</a>
</h3>

```typescript
public startIpAddress: pulumi.Output<string>;
```


Specifies the Charset for the PostgreSQL Database. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Server">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L10">class Server</a>
</h2>

Create a PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L66">constructor</a>
</h3>

```typescript
new Server(name: string, args: ServerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Server resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState): Server
```


Get an existing Server resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L26">property administratorLogin</a>
</h3>

```typescript
public administratorLogin: pulumi.Output<string>;
```


The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L30">property administratorLoginPassword</a>
</h3>

```typescript
public administratorLoginPassword: pulumi.Output<string>;
```


The Password associated with the `administrator_login` for the PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L34">property fqdn</a>
</h3>

```typescript
public fqdn: pulumi.Output<string>;
```


The FQDN of the PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L38">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L50">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L54">property sslEnforcement</a>
</h3>

```typescript
public sslEnforcement: pulumi.Output<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enabled` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L58">property storageProfile</a>
</h3>

```typescript
public storageProfile: pulumi.Output<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L62">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L66">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


Specifies the version of PostgreSQL to use. Valid values are `9.5`, `9.6`, and `10.0`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L101">interface ConfigurationArgs</a>
</h2>

The set of arguments for constructing a Configuration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L109">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L113">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L117">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.

<h2 class="pdoc-module-header" id="ConfigurationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L79">interface ConfigurationState</a>
</h2>

Input properties used for looking up and filtering Configuration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L87">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L91">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/configuration.ts#L95">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L116">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L120">property charset</a>
</h3>

```typescript
charset: pulumi.Input<string>;
```


Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L124">property collation</a>
</h3>

```typescript
collation: pulumi.Input<string>;
```


Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L133">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L137">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L89">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L93">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](https://www.postgresql.org/docs/current/static/multibyte.html). Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L97">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](https://www.postgresql.org/docs/current/static/collation.html). Note that Microsoft uses different [notation](https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx) - en-US instead of en_US. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS). Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/database.ts#L110">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FirewallRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L116">interface FirewallRuleArgs</a>
</h2>

The set of arguments for constructing a FirewallRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L120">property endIpAddress</a>
</h3>

```typescript
endIpAddress: pulumi.Input<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L125">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L129">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L133">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L137">property startIpAddress</a>
</h3>

```typescript
startIpAddress: pulumi.Input<string>;
```


Specifies the Charset for the PostgreSQL Database. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="FirewallRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L89">interface FirewallRuleState</a>
</h2>

Input properties used for looking up and filtering FirewallRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L93">property endIpAddress</a>
</h3>

```typescript
endIpAddress?: pulumi.Input<string>;
```


Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L106">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/firewallRule.ts#L110">property startIpAddress</a>
</h3>

```typescript
startIpAddress?: pulumi.Input<string>;
```


Specifies the Charset for the PostgreSQL Database. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L186">interface ServerArgs</a>
</h2>

The set of arguments for constructing a Server resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L190">property administratorLogin</a>
</h3>

```typescript
administratorLogin: pulumi.Input<string>;
```


The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L194">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword: pulumi.Input<string>;
```


The Password associated with the `administrator_login` for the PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L198">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L206">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L210">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L214">property sslEnforcement</a>
</h3>

```typescript
sslEnforcement: pulumi.Input<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enabled` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L218">property storageProfile</a>
</h3>

```typescript
storageProfile: pulumi.Input<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L222">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L226">property version</a>
</h3>

```typescript
version: pulumi.Input<string>;
```


Specifies the version of PostgreSQL to use. Valid values are `9.5`, `9.6`, and `10.0`. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L136">interface ServerState</a>
</h2>

Input properties used for looking up and filtering Server resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L140">property administratorLogin</a>
</h3>

```typescript
administratorLogin?: pulumi.Input<string>;
```


The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L144">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword?: pulumi.Input<string>;
```


The Password associated with the `administrator_login` for the PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L148">property fqdn</a>
</h3>

```typescript
fqdn?: pulumi.Input<string>;
```


The FQDN of the PostgreSQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L152">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the `tier` + `family` + `cores` pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L160">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L164">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L168">property sslEnforcement</a>
</h3>

```typescript
sslEnforcement?: pulumi.Input<string>;
```


Specifies if SSL should be enforced on connections. Possible values are `Enabled` and `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L172">property storageProfile</a>
</h3>

```typescript
storageProfile?: pulumi.Input<{ ... }>;
```


A `storage_profile` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L176">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/postgresql/server.ts#L180">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Specifies the version of PostgreSQL to use. Valid values are `9.5`, `9.6`, and `10.0`. Changing this forces a new resource to be created.

