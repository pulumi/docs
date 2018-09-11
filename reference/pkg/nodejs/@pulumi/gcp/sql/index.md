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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L12">class Database</a>
</h2>

Creates a new Google SQL Database on a Google SQL Database Instance. For more information, see
the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/databases).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L57">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L32">property charset</a>
</h3>

```typescript
public charset: pulumi.Output<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L40">property collation</a>
</h3>

```typescript
public collation: pulumi.Output<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L44">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L53">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L57">property selfLink</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L16">class DatabaseInstance</a>
</h2>

Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

~> **NOTE on `google_sql_database_instance`:** - Second-generation instances include a
default 'root'@'%' user with no password. This user will be deleted by Terraform on
instance creation. You should use `google_sql_user` to define a custom user with
a restricted host and strong password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L90">constructor</a>
</h3>

```typescript
new DatabaseInstance(name: string, args: DatabaseInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DatabaseInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseInstanceState): DatabaseInstance
```


Get an existing DatabaseInstance resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L32">property connectionName</a>
</h3>

```typescript
public connectionName: pulumi.Output<string>;
```


The connection name of the instance to be used in connection strings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L40">property databaseVersion</a>
</h3>

```typescript
public databaseVersion: pulumi.Output<string | undefined>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L46">property firstIpAddress</a>
</h3>

```typescript
public firstIpAddress: pulumi.Output<string>;
```


The first IPv4 address of the addresses assigned. This is
is to support accessing the [first address in the list in a terraform output](https://github.com/terraform-providers/terraform-provider-google/issues/912)
when the resource is configured with a `count`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L47">property ipAddresses</a>
</h3>

```typescript
public ipAddresses: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L53">property masterInstanceName</a>
</h3>

```typescript
public masterInstanceName: pulumi.Output<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to [one week](https://cloud.google.com/sql/docs/delete-instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L65">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L75">property region</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L80">property replicaConfiguration</a>
</h3>

```typescript
public replicaConfiguration: pulumi.Output<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L84">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L85">property serverCaCert</a>
</h3>

```typescript
public serverCaCert: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L90">property settings</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L14">class User</a>
</h2>

Creates a new Google SQL User on a Google SQL User Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/users).

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html). Passwords will not be retrieved when running
"terraform import".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L51">constructor</a>
</h3>

```typescript
new User(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState): User
```


Get an existing User resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L32">property host</a>
</h3>

```typescript
public host: pulumi.Output<string | undefined>;
```


The host the user can connect from. This is only supported
for MySQL instances. Don't set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L37">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L46">property password</a>
</h3>

```typescript
public password: pulumi.Output<string | undefined>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L51">property project</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L135">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L143">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L151">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L155">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L164">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L209">interface DatabaseInstanceArgs</a>
</h2>

The set of arguments for constructing a DatabaseInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L217">property databaseVersion</a>
</h3>

```typescript
databaseVersion?: pulumi.Input<string>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L223">property masterInstanceName</a>
</h3>

```typescript
masterInstanceName?: pulumi.Input<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L230">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to [one week](https://cloud.google.com/sql/docs/delete-instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L235">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L245">property region</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L250">property replicaConfiguration</a>
</h3>

```typescript
replicaConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L255">property settings</a>
</h3>

```typescript
settings: pulumi.Input<{ ... }>;
```


The settings to use for the database. The
configuration is detailed below.

<h2 class="pdoc-module-header" id="DatabaseInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L141">interface DatabaseInstanceState</a>
</h2>

Input properties used for looking up and filtering DatabaseInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L145">property connectionName</a>
</h3>

```typescript
connectionName?: pulumi.Input<string>;
```


The connection name of the instance to be used in connection strings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L153">property databaseVersion</a>
</h3>

```typescript
databaseVersion?: pulumi.Input<string>;
```


The MySQL version to
use. Can be `MYSQL_5_6`, `MYSQL_5_7` or `POSTGRES_9_6` for second-generation
instances, or `MYSQL_5_5` or `MYSQL_5_6` for first-generation instances.
See [Second Generation Capabilities](https://cloud.google.com/sql/docs/1st-2nd-gen-differences)
for more information. `POSTGRES_9_6` support is in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L159">property firstIpAddress</a>
</h3>

```typescript
firstIpAddress?: pulumi.Input<string>;
```


The first IPv4 address of the addresses assigned. This is
is to support accessing the [first address in the list in a terraform output](https://github.com/terraform-providers/terraform-provider-google/issues/912)
when the resource is configured with a `count`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L160">property ipAddresses</a>
</h3>

```typescript
ipAddresses?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L166">property masterInstanceName</a>
</h3>

```typescript
masterInstanceName?: pulumi.Input<string>;
```


The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to [one week](https://cloud.google.com/sql/docs/delete-instance).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L178">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L188">property region</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L193">property replicaConfiguration</a>
</h3>

```typescript
replicaConfiguration?: pulumi.Input<{ ... }>;
```


The configuration for replication. The
configuration is detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L197">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L198">property serverCaCert</a>
</h3>

```typescript
serverCaCert?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/databaseInstance.ts#L203">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }>;
```


The settings to use for the database. The
configuration is detailed below.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L96">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L104">property charset</a>
</h3>

```typescript
charset?: pulumi.Input<string>;
```


The charset value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Character Set Support](https://www.postgresql.org/docs/9.6/static/multibyte.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `charset` support; they only support a value of `UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L112">property collation</a>
</h3>

```typescript
collation?: pulumi.Input<string>;
```


The collation value. See MySQL's
[Supported Character Sets and Collations](https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html)
and Postgres' [Collation Support](https://www.postgresql.org/docs/9.6/static/collation.html)
for more details and supported values. Postgres databases are in [Beta](https://www.terraform.io/docs/providers/google/index.html#beta-features),
and have limited `collation` support; they only support a value of `en_US.UTF8` at creation time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L116">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of containing instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L125">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/database.ts#L129">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L119">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L125">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```


The host the user can connect from. This is only supported
for MySQL instances. Don't set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L130">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L139">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L144">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L88">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L94">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```


The host the user can connect from. This is only supported
for MySQL instances. Don't set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L99">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the Cloud SQL instance. Changing this
forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the user. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L108">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password for the user. Can be updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/sql/user.ts#L113">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

