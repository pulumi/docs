---
title: Module sql
---

<a href="../index.html">@pulumi/gcp</a> &gt; sql

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Database">class Database</a>
* <a href="#DatabaseInstance">class DatabaseInstance</a>
* <a href="#User">class User</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseInstanceArgs">interface DatabaseInstanceArgs</a>
* <a href="#DatabaseInstanceState">interface DatabaseInstanceState</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#UserArgs">interface UserArgs</a>
* <a href="#UserState">interface UserState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts">sql/database.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts">sql/databaseInstance.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts">sql/user.ts</a> 


<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L11">class Database</a>
</h2>

Creates a new Google SQL Database on a Google SQL Database Instance. For more information, see
the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/databases).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L56">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L31">property charset</a>
</h3>

```typescript
public charset: pulumi.Output<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L39">property collation</a>
</h3>

```typescript
public collation: pulumi.Output<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L43">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L47">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L52">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L56">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L15">class DatabaseInstance</a>
</h2>

Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

~> **NOTE on `google_sql_database_instance`:** - Second-generation instances include a
default 'root'@'%' user with no password. This user will be deleted by Terraform on
instance creation. You should use `google_sql_user` to define a custom user with
a restricted host and strong password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L86">constructor</a>
</h3>

```typescript
new DatabaseInstance(name: string, args: DatabaseInstanceArgs, opts?: pulumi.ResourceOptions)
```


Create a DatabaseInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseInstanceState): DatabaseInstance
```


Get an existing DatabaseInstance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L31">property connectionName</a>
</h3>

```typescript
public connectionName: pulumi.Output<string>;
```


The connection name of the instance to be used in connection strings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L39">property databaseVersion</a>
</h3>

```typescript
public databaseVersion: pulumi.Output<string | undefined>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L45">property firstIpAddress</a>
</h3>

```typescript
public firstIpAddress: pulumi.Output<string>;
```


The first IPv4 address of the addresses assigned. This is
is to support accessing the [first address in the list in a terraform output](https://github.com/terraform-providers/terraform-provider-google/issues/912)
when the resource is configured with a `count`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L46">property ipAddresses</a>
</h3>

```typescript
public ipAddresses: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L52">property masterInstanceName</a>
</h3>

```typescript
public masterInstanceName: pulumi.Output<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L56">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A name for this whitelist entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L61">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L71">property region</a>
</h3>

```typescript
public region: pulumi.Output<string | undefined>;
```


The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the `region` argument for this resource, make sure you understand this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L76">property replicaConfiguration</a>
</h3>

```typescript
public replicaConfiguration: pulumi.Output<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L80">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L81">property serverCaCert</a>
</h3>

```typescript
public serverCaCert: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L86">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }>;
```


The settings to use for the database. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="User">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L13">class User</a>
</h2>

Creates a new Google SQL User on a Google SQL User Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/users).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html). Passwords will not be retrieved when running
"terraform import".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L50">constructor</a>
</h3>

```typescript
new User(name: string, args: UserArgs, opts?: pulumi.ResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState): User
```


Get an existing User resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L31">property host</a>
</h3>

```typescript
public host: pulumi.Output<string | undefined>;
```


The host the user can connect from. This is only supported
for first generation SQL instances. Don't set this field for second generation
SQL instances. Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L36">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L45">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L134">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L142">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L150">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L154">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L163">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L202">interface DatabaseInstanceArgs</a>
</h2>

The set of arguments for constructing a DatabaseInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L210">property databaseVersion</a>
</h3>

```typescript
databaseVersion?: pulumi.Input<string>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L216">property masterInstanceName</a>
</h3>

```typescript
masterInstanceName?: pulumi.Input<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L220">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for this whitelist entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L225">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L235">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the `region` argument for this resource, make sure you understand this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L240">property replicaConfiguration</a>
</h3>

```typescript
replicaConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L245">property settings</a>
</h3>

```typescript
settings: pulumi.Input<{ ... }>;
```


The settings to use for the database. The
configuration is detailed below.

<h2 class="pdoc-module-header" id="DatabaseInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L137">interface DatabaseInstanceState</a>
</h2>

Input properties used for looking up and filtering DatabaseInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L141">property connectionName</a>
</h3>

```typescript
connectionName?: pulumi.Input<string>;
```


The connection name of the instance to be used in connection strings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L149">property databaseVersion</a>
</h3>

```typescript
databaseVersion?: pulumi.Input<string>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L155">property firstIpAddress</a>
</h3>

```typescript
firstIpAddress?: pulumi.Input<string>;
```


The first IPv4 address of the addresses assigned. This is
is to support accessing the [first address in the list in a terraform output](https://github.com/terraform-providers/terraform-provider-google/issues/912)
when the resource is configured with a `count`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L156">property ipAddresses</a>
</h3>

```typescript
ipAddresses?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L162">property masterInstanceName</a>
</h3>

```typescript
masterInstanceName?: pulumi.Input<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L166">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A name for this whitelist entry.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L171">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L181">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances *and* for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the `region` argument for this resource, make sure you understand this.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L186">property replicaConfiguration</a>
</h3>

```typescript
replicaConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L190">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L191">property serverCaCert</a>
</h3>

```typescript
serverCaCert?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L196">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }>;
```


The settings to use for the database. The
configuration is detailed below.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L95">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L103">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L111">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L115">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L124">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L128">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L118">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L124">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```


The host the user can connect from. This is only supported
for first generation SQL instances. Don't set this field for second generation
SQL instances. Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L129">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L134">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L138">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L143">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L87">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L93">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```


The host the user can connect from. This is only supported
for first generation SQL instances. Don't set this field for second generation
SQL instances. Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L98">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L107">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L112">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

