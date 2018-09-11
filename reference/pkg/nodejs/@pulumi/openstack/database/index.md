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
<a class="pdoc-member-name" href="/database/configuration.ts#L10">class Configuration</a>
</h2>

Manages a V1 DB configuration resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L44">constructor</a>
</h3>

```typescript
new Configuration(name: string, args: ConfigurationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Configuration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/database/configuration.ts#L26">property configurations</a>
</h3>

```typescript
public configurations: pulumi.Output<{ ... }[] | undefined>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L31">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L35">property description</a>
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
<a class="pdoc-child-name" href="/database/configuration.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L44">property region</a>
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
<a class="pdoc-member-name" href="/database/database.ts#L10">class Database</a>
</h2>

Manages a V1 DB database resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L34">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/database/database.ts#L26">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L34">property region</a>
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
<a class="pdoc-member-name" href="/database/instance.ts#L10">class Instance</a>
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
<a class="pdoc-child-name" href="/database/instance.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/database/instance.ts#L27">property configurationId</a>
</h3>

```typescript
public configurationId: pulumi.Output<string | undefined>;
```


Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L32">property databases</a>
</h3>

```typescript
public databases: pulumi.Output<{ ... }[] | undefined>;
```


An array of database name, charset and collate. The database
object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L37">property datastore</a>
</h3>

```typescript
public datastore: pulumi.Output<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L42">property flavorId</a>
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


A unique name for the resource.

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
<a class="pdoc-member-name" href="/database/user.ts#L10">class User</a>
</h2>

Manages a V1 DB user resource within OpenStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L40">constructor</a>
</h3>

```typescript
new User(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
```


Create a User resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="/database/user.ts#L26">property databases</a>
</h3>

```typescript
public databases: pulumi.Output<string[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L27">property host</a>
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
<a class="pdoc-child-name" href="/database/user.ts#L28">property instanceId</a>
</h3>

```typescript
public instanceId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L36">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L40">property region</a>
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
<a class="pdoc-member-name" href="/database/configuration.ts#L115">interface ConfigurationArgs</a>
</h2>

The set of arguments for constructing a Configuration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L119">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L124">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L128">property description</a>
</h3>

```typescript
description: pulumi.Input<string>;
```


Description of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L137">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h2 class="pdoc-module-header" id="ConfigurationState">
<a class="pdoc-member-name" href="/database/configuration.ts#L87">interface ConfigurationState</a>
</h2>

Input properties used for looking up and filtering Configuration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L91">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L96">property datastore</a>
</h3>

```typescript
datastore?: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L100">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/configuration.ts#L109">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="/database/database.ts#L85">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L89">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L97">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="/database/database.ts#L67">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L71">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```


The ID for the database instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/database.ts#L79">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="/database/instance.ts#L167">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L172">property configurationId</a>
</h3>

```typescript
configurationId?: pulumi.Input<string>;
```


Configuration ID to be attached to the instance. Database instance
will be rebooted when configuration is detached.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L177">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of database name, charset and collate. The database
object structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L182">property datastore</a>
</h3>

```typescript
datastore: pulumi.Input<{ ... }>;
```


An array of database engine type and version. The datastore
object structure is documented below. Changing this creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L187">property flavorId</a>
</h3>

```typescript
flavorId?: pulumi.Input<string>;
```


The flavor ID of the desired flavor for the instance.
Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L197">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L202">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L206">property size</a>
</h3>

```typescript
size: pulumi.Input<number>;
```


Specifies the volume size in GB. Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L211">property users</a>
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
<a class="pdoc-child-name" href="/database/instance.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L147">property networks</a>
</h3>

```typescript
networks?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of one or more networks to attach to the
instance. The network object structure is documented below. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L152">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to create the db instance. Changing this
creates a new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L156">property size</a>
</h3>

```typescript
size?: pulumi.Input<number>;
```


Specifies the volume size in GB. Changing this creates new instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/instance.ts#L161">property users</a>
</h3>

```typescript
users?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An array of username, password, host and databases. The user
object structure is documented below.

<h2 class="pdoc-module-header" id="UserArgs">
<a class="pdoc-member-name" href="/database/user.ts#L109">interface UserArgs</a>
</h2>

The set of arguments for constructing a User resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L113">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L114">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L115">property instanceId</a>
</h3>

```typescript
instanceId: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L123">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L127">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


Openstack region resource is created in.

<h2 class="pdoc-module-header" id="UserState">
<a class="pdoc-member-name" href="/database/user.ts#L85">interface UserState</a>
</h2>

Input properties used for looking up and filtering User resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L89">property databases</a>
</h3>

```typescript
databases?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of database user should have access to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L90">property host</a>
</h3>

```typescript
host?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L91">property instanceId</a>
</h3>

```typescript
instanceId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L99">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


User's password.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/database/user.ts#L103">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Openstack region resource is created in.

