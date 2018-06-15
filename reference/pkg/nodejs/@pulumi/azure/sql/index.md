---
title: Module sql
---

<a href="../index.html">@pulumi/azure</a> &gt; sql

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ActiveDirectoryAdministrator">class ActiveDirectoryAdministrator</a>
* <a href="#Database">class Database</a>
* <a href="#ElasticPool">class ElasticPool</a>
* <a href="#FirewallRule">class FirewallRule</a>
* <a href="#SqlServer">class SqlServer</a>
* <a href="#VirtualNetworkRule">class VirtualNetworkRule</a>
* <a href="#ActiveDirectoryAdministratorArgs">interface ActiveDirectoryAdministratorArgs</a>
* <a href="#ActiveDirectoryAdministratorState">interface ActiveDirectoryAdministratorState</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#ElasticPoolArgs">interface ElasticPoolArgs</a>
* <a href="#ElasticPoolState">interface ElasticPoolState</a>
* <a href="#FirewallRuleArgs">interface FirewallRuleArgs</a>
* <a href="#FirewallRuleState">interface FirewallRuleState</a>
* <a href="#SqlServerArgs">interface SqlServerArgs</a>
* <a href="#SqlServerState">interface SqlServerState</a>
* <a href="#VirtualNetworkRuleArgs">interface VirtualNetworkRuleArgs</a>
* <a href="#VirtualNetworkRuleState">interface VirtualNetworkRuleState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts">sql/activeDirectoryAdministrator.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts">sql/database.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts">sql/elasticPool.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts">sql/firewallRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts">sql/sqlServer.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts">sql/virtualNetworkRule.ts</a> 


<h2 class="pdoc-module-header" id="ActiveDirectoryAdministrator">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L9">class ActiveDirectoryAdministrator</a>
</h2>

Allows you to set a user or group as the AD administrator for an Azure SQL server

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L41">constructor</a>
</h3>

```typescript
new ActiveDirectoryAdministrator(name: string, args: ActiveDirectoryAdministratorArgs, opts?: pulumi.ResourceOptions)
```


Create a ActiveDirectoryAdministrator resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActiveDirectoryAdministratorState): ActiveDirectoryAdministrator
```


Get an existing ActiveDirectoryAdministrator resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L25">property login</a>
</h3>

```typescript
public login: pulumi.Output<string>;
```


The login name of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L29">property objectId</a>
</h3>

```typescript
public objectId: pulumi.Output<string>;
```


The ID of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group for the SQL server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L37">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L41">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The Azure Tenant ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L9">class Database</a>
</h2>

Allows you to manage an Azure SQL Database

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L88">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L25">property collation</a>
</h3>

```typescript
public collation: pulumi.Output<string>;
```


The name of the collation. Applies only if `create_mode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L29">property createMode</a>
</h3>

```typescript
public createMode: pulumi.Output<string | undefined>;
```


Specifies the type of database to create. Defaults to `Default`. See below for the accepted values/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L30">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L34">property defaultSecondaryLocation</a>
</h3>

```typescript
public defaultSecondaryLocation: pulumi.Output<string>;
```


The default secondary location of the SQL Database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L38">property edition</a>
</h3>

```typescript
public edition: pulumi.Output<string>;
```


The edition of the database to be created. Applies only if `create_mode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, or `DataWarehouse`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L42">property elasticPoolName</a>
</h3>

```typescript
public elasticPoolName: pulumi.Output<string>;
```


The name of the elastic database pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L43">property encryption</a>
</h3>

```typescript
public encryption: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L47">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L51">property maxSizeBytes</a>
</h3>

```typescript
public maxSizeBytes: pulumi.Output<string>;
```


The maximum size that the database can grow to. Applies only if `create_mode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L60">property requestedServiceObjectiveId</a>
</h3>

```typescript
public requestedServiceObjectiveId: pulumi.Output<string>;
```


Use `requested_service_objective_id` or `requested_service_objective_name` to set the performance level for the database.
Valid values are: `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L64">property requestedServiceObjectiveName</a>
</h3>

```typescript
public requestedServiceObjectiveName: pulumi.Output<string>;
```


Use `requested_service_objective_name` or `requested_service_objective_id` to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L68">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L72">property restorePointInTime</a>
</h3>

```typescript
public restorePointInTime: pulumi.Output<string>;
```


The point in time for the restore. Only applies if `create_mode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L76">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


The name of the SQL Server on which to create the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L80">property sourceDatabaseDeletionDate</a>
</h3>

```typescript
public sourceDatabaseDeletionDate: pulumi.Output<string>;
```


The deletion date time of the source database. Only applies to deleted databases where `create_mode` is `PointInTimeRestore`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L84">property sourceDatabaseId</a>
</h3>

```typescript
public sourceDatabaseId: pulumi.Output<string>;
```


The URI of the source database if `create_mode` value is not `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L88">property tags</a>
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

<h2 class="pdoc-module-header" id="ElasticPool">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L9">class ElasticPool</a>
</h2>

Allows you to manage an Azure SQL Elastic Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L65">constructor</a>
</h3>

```typescript
new ElasticPool(name: string, args: ElasticPoolArgs, opts?: pulumi.ResourceOptions)
```


Create a ElasticPool resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ElasticPoolState): ElasticPool
```


Get an existing ElasticPool resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L25">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


The creation date of the SQL Elastic Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L29">property dbDtuMax</a>
</h3>

```typescript
public dbDtuMax: pulumi.Output<number>;
```


The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L33">property dbDtuMin</a>
</h3>

```typescript
public dbDtuMin: pulumi.Output<number>;
```


The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L37">property dtu</a>
</h3>

```typescript
public dtu: pulumi.Output<number>;
```


The total shared DTU for the elastic pool. Valid values depend on the `edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L41">property edition</a>
</h3>

```typescript
public edition: pulumi.Output<string>;
```


The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L45">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L53">property poolSize</a>
</h3>

```typescript
public poolSize: pulumi.Output<number>;
```


The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `edition` and `dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `edition` and `dtu`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L57">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L61">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L65">property tags</a>
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

<h2 class="pdoc-module-header" id="FirewallRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L9">class FirewallRule</a>
</h2>

Allows you to manage an Azure SQL Firewall Rule

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L42">constructor</a>
</h3>

```typescript
new FirewallRule(name: string, args: FirewallRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a FirewallRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L25">property endIpAddress</a>
</h3>

```typescript
public endIpAddress: pulumi.Output<string>;
```


The ending IP address to allow through the firewall for this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the sql server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L38">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


The name of the SQL Server on which to create the Firewall Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L42">property startIpAddress</a>
</h3>

```typescript
public startIpAddress: pulumi.Output<string>;
```


The starting IP address to allow through the firewall for this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SqlServer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L12">class SqlServer</a>
</h2>

Manages a SQL Azure Database Server.

~> **Note:** All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L56">constructor</a>
</h3>

```typescript
new SqlServer(name: string, args: SqlServerArgs, opts?: pulumi.ResourceOptions)
```


Create a SqlServer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SqlServerState): SqlServer
```


Get an existing SqlServer resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L28">property administratorLogin</a>
</h3>

```typescript
public administratorLogin: pulumi.Output<string>;
```


The administrator login name for the new server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L32">property administratorLoginPassword</a>
</h3>

```typescript
public administratorLoginPassword: pulumi.Output<string>;
```


The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L36">property fullyQualifiedDomainName</a>
</h3>

```typescript
public fullyQualifiedDomainName: pulumi.Output<string>;
```


The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the SQL Server. This needs to be globally unique within Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L48">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the SQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L52">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L56">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).

<h2 class="pdoc-module-header" id="VirtualNetworkRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L9">class VirtualNetworkRule</a>
</h2>

Allows you to add, update, or remove an Azure SQL server to a subnet of a virtual network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L41">constructor</a>
</h3>

```typescript
new VirtualNetworkRule(name: string, args: VirtualNetworkRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a VirtualNetworkRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VirtualNetworkRuleState): VirtualNetworkRule
```


Get an existing VirtualNetworkRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L25">property ignoreMissingVnetServiceEndpoint</a>
</h3>

```typescript
public ignoreMissingVnetServiceEndpoint: pulumi.Output<boolean | undefined>;
```


Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L37">property serverName</a>
</h3>

```typescript
public serverName: pulumi.Output<string>;
```


The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L41">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


The ID of the subnet that the SQL server will be connected to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ActiveDirectoryAdministratorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L116">interface ActiveDirectoryAdministratorArgs</a>
</h2>

The set of arguments for constructing a ActiveDirectoryAdministrator resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L120">property login</a>
</h3>

```typescript
login: pulumi.Input<string>;
```


The login name of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L124">property objectId</a>
</h3>

```typescript
objectId: pulumi.Input<string>;
```


The ID of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L128">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group for the SQL server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L132">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L136">property tenantId</a>
</h3>

```typescript
tenantId: pulumi.Input<string>;
```


The Azure Tenant ID

<h2 class="pdoc-module-header" id="ActiveDirectoryAdministratorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L90">interface ActiveDirectoryAdministratorState</a>
</h2>

Input properties used for looking up and filtering ActiveDirectoryAdministrator resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L94">property login</a>
</h3>

```typescript
login?: pulumi.Input<string>;
```


The login name of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L98">property objectId</a>
</h3>

```typescript
objectId?: pulumi.Input<string>;
```


The ID of the principal to set as the server administrator

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L102">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group for the SQL server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L106">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/activeDirectoryAdministrator.ts#L110">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The Azure Tenant ID

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L230">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L234">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The name of the collation. Applies only if `create_mode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L238">property createMode</a>
</h3>

```typescript
createMode?: pulumi.Input<string>;
```


Specifies the type of database to create. Defaults to `Default`. See below for the accepted values/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L242">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The edition of the database to be created. Applies only if `create_mode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, or `DataWarehouse`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L246">property elasticPoolName</a>
</h3>

```typescript
elasticPoolName?: pulumi.Input<string>;
```


The name of the elastic database pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L250">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L254">property maxSizeBytes</a>
</h3>

```typescript
maxSizeBytes?: pulumi.Input<string>;
```


The maximum size that the database can grow to. Applies only if `create_mode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L258">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L263">property requestedServiceObjectiveId</a>
</h3>

```typescript
requestedServiceObjectiveId?: pulumi.Input<string>;
```


Use `requested_service_objective_id` or `requested_service_objective_name` to set the performance level for the database.
Valid values are: `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L267">property requestedServiceObjectiveName</a>
</h3>

```typescript
requestedServiceObjectiveName?: pulumi.Input<string>;
```


Use `requested_service_objective_name` or `requested_service_objective_id` to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L271">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L275">property restorePointInTime</a>
</h3>

```typescript
restorePointInTime?: pulumi.Input<string>;
```


The point in time for the restore. Only applies if `create_mode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L279">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


The name of the SQL Server on which to create the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L283">property sourceDatabaseDeletionDate</a>
</h3>

```typescript
sourceDatabaseDeletionDate?: pulumi.Input<string>;
```


The deletion date time of the source database. Only applies to deleted databases where `create_mode` is `PointInTimeRestore`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L287">property sourceDatabaseId</a>
</h3>

```typescript
sourceDatabaseId?: pulumi.Input<string>;
```


The URI of the source database if `create_mode` value is not `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L291">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L157">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L161">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The name of the collation. Applies only if `create_mode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L165">property createMode</a>
</h3>

```typescript
createMode?: pulumi.Input<string>;
```


Specifies the type of database to create. Defaults to `Default`. See below for the accepted values/

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L166">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L170">property defaultSecondaryLocation</a>
</h3>

```typescript
defaultSecondaryLocation?: pulumi.Input<string>;
```


The default secondary location of the SQL Database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L174">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The edition of the database to be created. Applies only if `create_mode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, or `DataWarehouse`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L178">property elasticPoolName</a>
</h3>

```typescript
elasticPoolName?: pulumi.Input<string>;
```


The name of the elastic database pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L179">property encryption</a>
</h3>

```typescript
encryption?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L183">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L187">property maxSizeBytes</a>
</h3>

```typescript
maxSizeBytes?: pulumi.Input<string>;
```


The maximum size that the database can grow to. Applies only if `create_mode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L196">property requestedServiceObjectiveId</a>
</h3>

```typescript
requestedServiceObjectiveId?: pulumi.Input<string>;
```


Use `requested_service_objective_id` or `requested_service_objective_name` to set the performance level for the database.
Valid values are: `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L200">property requestedServiceObjectiveName</a>
</h3>

```typescript
requestedServiceObjectiveName?: pulumi.Input<string>;
```


Use `requested_service_objective_name` or `requested_service_objective_id` to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L204">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L208">property restorePointInTime</a>
</h3>

```typescript
restorePointInTime?: pulumi.Input<string>;
```


The point in time for the restore. Only applies if `create_mode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L212">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


The name of the SQL Server on which to create the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L216">property sourceDatabaseDeletionDate</a>
</h3>

```typescript
sourceDatabaseDeletionDate?: pulumi.Input<string>;
```


The deletion date time of the source database. Only applies to deleted databases where `create_mode` is `PointInTimeRestore`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L220">property sourceDatabaseId</a>
</h3>

```typescript
sourceDatabaseId?: pulumi.Input<string>;
```


The URI of the source database if `create_mode` value is not `Default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/database.ts#L224">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ElasticPoolArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L176">interface ElasticPoolArgs</a>
</h2>

The set of arguments for constructing a ElasticPool resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L180">property dbDtuMax</a>
</h3>

```typescript
dbDtuMax?: pulumi.Input<number>;
```


The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L184">property dbDtuMin</a>
</h3>

```typescript
dbDtuMin?: pulumi.Input<number>;
```


The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L188">property dtu</a>
</h3>

```typescript
dtu: pulumi.Input<number>;
```


The total shared DTU for the elastic pool. Valid values depend on the `edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L192">property edition</a>
</h3>

```typescript
edition: pulumi.Input<string>;
```


The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L196">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L200">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L204">property poolSize</a>
</h3>

```typescript
poolSize?: pulumi.Input<number>;
```


The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `edition` and `dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `edition` and `dtu`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L208">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L212">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ElasticPoolState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L126">interface ElasticPoolState</a>
</h2>

Input properties used for looking up and filtering ElasticPool resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L130">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


The creation date of the SQL Elastic Pool.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L134">property dbDtuMax</a>
</h3>

```typescript
dbDtuMax?: pulumi.Input<number>;
```


The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L138">property dbDtuMin</a>
</h3>

```typescript
dbDtuMin?: pulumi.Input<number>;
```


The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L142">property dtu</a>
</h3>

```typescript
dtu?: pulumi.Input<number>;
```


The total shared DTU for the elastic pool. Valid values depend on the `edition` which has been defined. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for valid combinations.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L146">property edition</a>
</h3>

```typescript
edition?: pulumi.Input<string>;
```


The edition of the elastic pool to be created. Valid values are `Basic`, `Standard`, and `Premium`. Refer to [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus) for details. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L150">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L158">property poolSize</a>
</h3>

```typescript
poolSize?: pulumi.Input<number>;
```


The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of `edition` and `dtu` and the limits documented in [Azure SQL Database Service Tiers](https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus). If not defined when creating an elastic pool, the value is set to the size implied by `edition` and `dtu`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L162">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L166">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/elasticPool.ts#L170">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="FirewallRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L115">interface FirewallRuleArgs</a>
</h2>

The set of arguments for constructing a FirewallRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L119">property endIpAddress</a>
</h3>

```typescript
endIpAddress: pulumi.Input<string>;
```


The ending IP address to allow through the firewall for this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L128">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the sql server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L132">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


The name of the SQL Server on which to create the Firewall Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L136">property startIpAddress</a>
</h3>

```typescript
startIpAddress: pulumi.Input<string>;
```


The starting IP address to allow through the firewall for this rule.

<h2 class="pdoc-module-header" id="FirewallRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L88">interface FirewallRuleState</a>
</h2>

Input properties used for looking up and filtering FirewallRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L92">property endIpAddress</a>
</h3>

```typescript
endIpAddress?: pulumi.Input<string>;
```


The ending IP address to allow through the firewall for this rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L101">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the sql server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L105">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


The name of the SQL Server on which to create the Firewall Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/firewallRule.ts#L109">property startIpAddress</a>
</h3>

```typescript
startIpAddress?: pulumi.Input<string>;
```


The starting IP address to allow through the firewall for this rule.

<h2 class="pdoc-module-header" id="SqlServerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L149">interface SqlServerArgs</a>
</h2>

The set of arguments for constructing a SqlServer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L153">property administratorLogin</a>
</h3>

```typescript
administratorLogin: pulumi.Input<string>;
```


The administrator login name for the new server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L157">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword: pulumi.Input<string>;
```


The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L161">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L165">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SQL Server. This needs to be globally unique within Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L169">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the SQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L173">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L177">property version</a>
</h3>

```typescript
version: pulumi.Input<string>;
```


The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).

<h2 class="pdoc-module-header" id="SqlServerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L111">interface SqlServerState</a>
</h2>

Input properties used for looking up and filtering SqlServer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L115">property administratorLogin</a>
</h3>

```typescript
administratorLogin?: pulumi.Input<string>;
```


The administrator login name for the new server. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L119">property administratorLoginPassword</a>
</h3>

```typescript
administratorLoginPassword?: pulumi.Input<string>;
```


The password associated with the `administrator_login` user. Needs to comply with Azure's [Password Policy](https://msdn.microsoft.com/library/ms161959.aspx)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L123">property fullyQualifiedDomainName</a>
</h3>

```typescript
fullyQualifiedDomainName?: pulumi.Input<string>;
```


The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L127">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SQL Server. This needs to be globally unique within Azure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L135">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the SQL Server.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/sqlServer.ts#L143">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).

<h2 class="pdoc-module-header" id="VirtualNetworkRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L110">interface VirtualNetworkRuleArgs</a>
</h2>

The set of arguments for constructing a VirtualNetworkRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L114">property ignoreMissingVnetServiceEndpoint</a>
</h3>

```typescript
ignoreMissingVnetServiceEndpoint?: pulumi.Input<boolean>;
```


Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L122">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L126">property serverName</a>
</h3>

```typescript
serverName: pulumi.Input<string>;
```


The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L130">property subnetId</a>
</h3>

```typescript
subnetId: pulumi.Input<string>;
```


The ID of the subnet that the SQL server will be connected to.

<h2 class="pdoc-module-header" id="VirtualNetworkRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L84">interface VirtualNetworkRuleState</a>
</h2>

Input properties used for looking up and filtering VirtualNetworkRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L88">property ignoreMissingVnetServiceEndpoint</a>
</h3>

```typescript
ignoreMissingVnetServiceEndpoint?: pulumi.Input<boolean>;
```


Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L92">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L96">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L100">property serverName</a>
</h3>

```typescript
serverName?: pulumi.Input<string>;
```


The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/sql/virtualNetworkRule.ts#L104">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


The ID of the subnet that the SQL server will be connected to.

