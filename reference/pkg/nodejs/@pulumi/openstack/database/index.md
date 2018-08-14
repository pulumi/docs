---
title: Module database
---

<a href="../index.html">@pulumi/openstack</a> &gt; database

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Configuration">class Configuration</a>
* <a href="#Database">class Database</a>
* <a href="#Instance">class Instance</a>
* <a href="#User">class User</a>
* <a href="#ConfigurationArgs">interface ConfigurationArgs</a>
* <a href="#ConfigurationState">interface ConfigurationState</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#UserArgs">interface UserArgs</a>
* <a href="#UserState">interface UserState</a>

<a href="/database/configuration.ts">database/configuration.ts</a> <a href="/database/database.ts">database/database.ts</a> <a href="/database/instance.ts">database/instance.ts</a> <a href="/database/user.ts">database/user.ts</a> 


<h2 class="pdoc-module-header" id="Configuration">
<a class="pdoc-member-name" href="/database/configuration.ts#L9">class Configuration</a>
</h2>

Manages a V1 DB configuration resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L43">constructor</a>
</h3>

```typescript
new Configuration(name: string, args: ConfigurationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Configuration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState): Configuration
```


Get an existing Configuration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L25">property configurations</a>
</h3>

```typescript
public configurations: pulumi.Output<{ ... }[] | undefined>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L30">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


Description of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Configuration parameter name. Changing this creates a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L43">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="/database/database.ts#L9">class Database</a>
</h2>

Manages a V1 DB database resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L33">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L25">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L33">property region</a>
</h3>

```typescript
public region: pulumi.Output<string | undefined>;
```


Openstack region resource is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="/database/instance.ts#L9">class Instance</a>
</h2>

Manages a V1 DB instance resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L66">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L26">property configurationId</a>
</h3>

```typescript
public configurationId: pulumi.Output<string | undefined>;
```


Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L31">property databases</a>
</h3>

```typescript
public databases: pulumi.Output<{ ... }[] | undefined>;
```


An array of database name, charset and collate. The database
object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L36">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L41">property flavorId</a>
</h3>

```typescript
public flavorId: pulumi.Output<string>;
```


The flavor ID of the desired flavor for the instance.
Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Database to be created on new instance. Changing this creates a
new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L52">property networks</a>
</h3>

```typescript
public networks: pulumi.Output<{ ... }[] | undefined>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L57">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L61">property size</a>
</h3>

```typescript
public size: pulumi.Output<number>;
```


Specifies the volume size in GB. Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L66">property users</a>
</h3>

```typescript
public users: pulumi.Output<{ ... }[] | undefined>;
```


An array of username, password, host and databases. The user
object structure is documented below.

<h2 class="pdoc-module-header" id="User">
<a class="pdoc-member-name" href="/database/user.ts#L9">class User</a>
</h2>

Manages a V1 DB user resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L39">constructor</a>
</h3>

```typescript
new User(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState): User
```


Get an existing User resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L25">property databases</a>
</h3>

```typescript
public databases: pulumi.Output<string[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L26">property host</a>
</h3>

```typescript
public host: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L27">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L35">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L39">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


Openstack region resource is created in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigurationArgs">
<a class="pdoc-member-name" href="/database/configuration.ts#L114">interface ConfigurationArgs</a>
</h2>

The set of arguments for constructing a Configuration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L118">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L123">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L127">property description</a>
</h3>

```typescript
description: pulumi.Input<string>;
```


Description of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Configuration parameter name. Changing this creates a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L136">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h2 class="pdoc-module-header" id="ConfigurationState">
<a class="pdoc-member-name" href="/database/configuration.ts#L86">interface ConfigurationState</a>
</h2>

Input properties used for looking up and filtering Configuration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L90">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L95">property datastore</a>
</h3>

```typescript
datastore?: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Configuration parameter name. Changing this creates a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L108">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="/database/database.ts#L84">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L88">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L92">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L96">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="/database/database.ts#L66">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L70">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L74">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L78">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="/database/instance.ts#L168">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L173">property configurationId</a>
</h3>

```typescript
configurationId?: pulumi.Input<string>;
```


Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L178">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of database name, charset and collate. The database
object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L183">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L188">property flavorId</a>
</h3>

```typescript
flavorId?: pulumi.Input<string>;
```


The flavor ID of the desired flavor for the instance.
Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L193">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Database to be created on new instance. Changing this creates a
new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L199">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L204">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L208">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


Specifies the volume size in GB. Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L213">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of username, password, host and databases. The user
object structure is documented below.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="/database/instance.ts#L117">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L122">property configurationId</a>
</h3>

```typescript
configurationId?: pulumi.Input<string>;
```


Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L127">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of database name, charset and collate. The database
object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L132">property datastore</a>
</h3>

```typescript
datastore?: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L137">property flavorId</a>
</h3>

```typescript
flavorId?: pulumi.Input<string>;
```


The flavor ID of the desired flavor for the instance.
Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Database to be created on new instance. Changing this creates a
new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L148">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L153">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L157">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Specifies the volume size in GB. Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L162">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of username, password, host and databases. The user
object structure is documented below.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="/database/user.ts#L108">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L112">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L113">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L114">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L122">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L126">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="/database/user.ts#L84">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L88">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L89">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L90">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L98">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L102">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

