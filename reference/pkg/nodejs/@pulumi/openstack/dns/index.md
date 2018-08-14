---
title: Module dns
---

<a href="../index.html">@pulumi/openstack</a> &gt; dns

<h2 class="pdoc-module-header">Index</h2>

* <a href="#RecordSet">class RecordSet</a>
* <a href="#Zone">class Zone</a>
* <a href="#getDnsZone">function getDnsZone</a>
* <a href="#GetDnsZoneArgs">interface GetDnsZoneArgs</a>
* <a href="#GetDnsZoneResult">interface GetDnsZoneResult</a>
* <a href="#RecordSetArgs">interface RecordSetArgs</a>
* <a href="#RecordSetState">interface RecordSetState</a>
* <a href="#ZoneArgs">interface ZoneArgs</a>
* <a href="#ZoneState">interface ZoneState</a>

<a href="/dns/getDnsZone.ts">dns/getDnsZone.ts</a> <a href="/dns/recordSet.ts">dns/recordSet.ts</a> <a href="/dns/zone.ts">dns/zone.ts</a> 


<h2 class="pdoc-module-header" id="RecordSet">
<a class="pdoc-member-name" href="/dns/recordSet.ts#L9">class RecordSet</a>
</h2>

Manages a DNS record set in the OpenStack DNS Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L59">constructor</a>
</h3>

```typescript
new RecordSet(name: string, args: RecordSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RecordSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordSetState): RecordSet
```


Get an existing RecordSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/dns/recordSet.ts#L25">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the record set. Note the `.` at the end of the name.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L34">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[] | undefined>;
```


An array of DNS records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L40">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 DNS client.
If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L44">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The time to live (TTL) of the record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L49">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of record set. Examples: "A", "MX".
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L54">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options. Changing this creates a
new record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L59">property zoneId</a>
</h3>

```typescript
public zoneId: pulumi.Output<string>;
```


The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.

<h2 class="pdoc-module-header" id="Zone">
<a class="pdoc-member-name" href="/dns/zone.ts#L9">class Zone</a>
</h2>

Manages a DNS zone in the OpenStack DNS Service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L65">constructor</a>
</h3>

```typescript
new Zone(name: string, args?: ZoneArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Zone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState): Zone
```


Get an existing Zone resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="/dns/zone.ts#L26">property attributes</a>
</h3>

```typescript
public attributes: pulumi.Output<{ ... } | undefined>;
```


Attributes for the DNS Service scheduler.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L34">property email</a>
</h3>

```typescript
public email: pulumi.Output<string | undefined>;
```


The email contact for the zone record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L39">property masters</a>
</h3>

```typescript
public masters: pulumi.Output<string[] | undefined>;
```


An array of master DNS servers. For when `type` is
`SECONDARY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the zone. Note the `.` at the end of the name.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L51">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L55">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The time to live (TTL) of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L60">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of zone. Can either be `PRIMARY` or `SECONDARY`.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L65">property valueSpecs</a>
</h3>

```typescript
public valueSpecs: pulumi.Output<{ ... } | undefined>;
```


Map of additional options. Changing this creates a
new zone.

<h2 class="pdoc-module-header" id="getDnsZone">
<a class="pdoc-member-name" href="/dns/getDnsZone.ts#L9">function getDnsZone</a>
</h2>

```typescript
getDnsZone(args?: GetDnsZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetDnsZoneResult>
```


Use this data source to get the ID of an available OpenStack DNS zone.

<h2 class="pdoc-module-header" id="GetDnsZoneArgs">
<a class="pdoc-member-name" href="/dns/getDnsZone.ts#L34">interface GetDnsZoneArgs</a>
</h2>

A collection of arguments for invoking getDnsZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L35">property attributes</a>
</h3>

```typescript
attributes?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L36">property createdAt</a>
</h3>

```typescript
createdAt?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L40">property description</a>
</h3>

```typescript
description?: string;
```


A description of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L44">property email</a>
</h3>

```typescript
email?: string;
```


The email contact for the zone record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L45">property masters</a>
</h3>

```typescript
masters?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L49">property name</a>
</h3>

```typescript
name?: string;
```


The name of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L50">property poolId</a>
</h3>

```typescript
poolId?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L51">property projectId</a>
</h3>

```typescript
projectId?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L57">property region</a>
</h3>

```typescript
region?: string;
```


The region in which to obtain the V2 DNS client.
A DNS client is needed to retrieve zone ids. If omitted, the
`region` argument of the provider is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L58">property serial</a>
</h3>

```typescript
serial?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L62">property status</a>
</h3>

```typescript
status?: string;
```


The zone's status.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L63">property transferredAt</a>
</h3>

```typescript
transferredAt?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L67">property ttl</a>
</h3>

```typescript
ttl?: number;
```


The time to live (TTL) of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L71">property type</a>
</h3>

```typescript
type?: string;
```


The type of the zone. Can either be `PRIMARY` or `SECONDARY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L72">property updatedAt</a>
</h3>

```typescript
updatedAt?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L73">property version</a>
</h3>

```typescript
version?: number;
```

<h2 class="pdoc-module-header" id="GetDnsZoneResult">
<a class="pdoc-member-name" href="/dns/getDnsZone.ts#L79">interface GetDnsZoneResult</a>
</h2>

A collection of values returned by getDnsZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L83">property attributes</a>
</h3>

```typescript
attributes: { ... };
```


Attributes of the DNS Service scheduler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L87">property createdAt</a>
</h3>

```typescript
createdAt: string;
```


The time the zone was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L123">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L91">property masters</a>
</h3>

```typescript
masters: string[];
```


An array of master DNS servers. When `type` is  `SECONDARY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L95">property poolId</a>
</h3>

```typescript
poolId: string;
```


The ID of the pool hosting the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L99">property projectId</a>
</h3>

```typescript
projectId: string;
```


The project ID that owns the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L103">property region</a>
</h3>

```typescript
region: string;
```


See Argument Reference above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L107">property serial</a>
</h3>

```typescript
serial: number;
```


The serial number of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L111">property transferredAt</a>
</h3>

```typescript
transferredAt: string;
```


The time the zone was transferred.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L115">property updatedAt</a>
</h3>

```typescript
updatedAt: string;
```


The time the zone was last updated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/getDnsZone.ts#L119">property version</a>
</h3>

```typescript
version: number;
```


The version of the zone.

<h2 class="pdoc-module-header" id="RecordSetArgs">
<a class="pdoc-member-name" href="/dns/recordSet.ts#L146">interface RecordSetArgs</a>
</h2>

The set of arguments for constructing a RecordSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L150">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the record set. Note the `.` at the end of the name.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L159">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of DNS records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L165">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 DNS client.
If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L169">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The time to live (TTL) of the record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L174">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of record set. Examples: "A", "MX".
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L179">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options. Changing this creates a
new record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L184">property zoneId</a>
</h3>

```typescript
zoneId: pulumi.Input<string>;
```


The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.

<h2 class="pdoc-module-header" id="RecordSetState">
<a class="pdoc-member-name" href="/dns/recordSet.ts#L102">interface RecordSetState</a>
</h2>

Input properties used for looking up and filtering RecordSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the record set. Note the `.` at the end of the name.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L115">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of DNS records.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L121">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 DNS client.
If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L125">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The time to live (TTL) of the record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L130">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of record set. Examples: "A", "MX".
Changing this creates a new DNS  record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L135">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options. Changing this creates a
new record set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/recordSet.ts#L140">property zoneId</a>
</h3>

```typescript
zoneId?: pulumi.Input<string>;
```


The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.

<h2 class="pdoc-module-header" id="ZoneArgs">
<a class="pdoc-member-name" href="/dns/zone.ts#L157">interface ZoneArgs</a>
</h2>

The set of arguments for constructing a Zone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L162">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Attributes for the DNS Service scheduler.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L166">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L170">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The email contact for the zone record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L175">property masters</a>
</h3>

```typescript
masters?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of master DNS servers. For when `type` is
`SECONDARY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L180">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the zone. Note the `.` at the end of the name.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L187">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L191">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The time to live (TTL) of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L196">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of zone. Can either be `PRIMARY` or `SECONDARY`.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L201">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options. Changing this creates a
new zone.

<h2 class="pdoc-module-header" id="ZoneState">
<a class="pdoc-member-name" href="/dns/zone.ts#L107">interface ZoneState</a>
</h2>

Input properties used for looking up and filtering Zone resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L112">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }>;
```


Attributes for the DNS Service scheduler.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L120">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


The email contact for the zone record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L125">property masters</a>
</h3>

```typescript
masters?: pulumi.Input<pulumi.Input<string>[]>;
```


An array of master DNS servers. For when `type` is
`SECONDARY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the zone. Note the `.` at the end of the name.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L137">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L141">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The time to live (TTL) of the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L146">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of zone. Can either be `PRIMARY` or `SECONDARY`.
Changing this creates a new zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="/dns/zone.ts#L151">property valueSpecs</a>
</h3>

```typescript
valueSpecs?: pulumi.Input<{ ... }>;
```


Map of additional options. Changing this creates a
new zone.

