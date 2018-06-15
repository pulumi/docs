---
title: Module dns
---

<a href="../index.html">@pulumi/gcp</a> &gt; dns

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ManagedZone">class ManagedZone</a>
* <a href="#RecordSet">class RecordSet</a>
* <a href="#getManagedZone">function getManagedZone</a>
* <a href="#GetManagedZoneArgs">interface GetManagedZoneArgs</a>
* <a href="#GetManagedZoneResult">interface GetManagedZoneResult</a>
* <a href="#ManagedZoneArgs">interface ManagedZoneArgs</a>
* <a href="#ManagedZoneState">interface ManagedZoneState</a>
* <a href="#RecordSetArgs">interface RecordSetArgs</a>
* <a href="#RecordSetState">interface RecordSetState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts">dns/getManagedZone.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts">dns/managedZone.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts">dns/recordSet.ts</a> 


<h2 class="pdoc-module-header" id="ManagedZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L10">class ManagedZone</a>
</h2>

Manages a zone within Google Cloud DNS. For more information see [the official documentation](https://cloud.google.com/dns/zones/) and
[API](https://cloud.google.com/dns/api/v1/managedZones).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L46">constructor</a>
</h3>

```typescript
new ManagedZone(name: string, args: ManagedZoneArgs, opts?: pulumi.ResourceOptions)
```


Create a ManagedZone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagedZoneState): ManagedZone
```


Get an existing ManagedZone resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A textual description field. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L30">property dnsName</a>
</h3>

```typescript
public dnsName: pulumi.Output<string>;
```


The fully qualified DNS name of this zone, e.g. `terraform.io.`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L41">property nameServers</a>
</h3>

```typescript
public nameServers: pulumi.Output<string[]>;
```


The list of nameservers that will be authoritative for this
domain. Use NS records to redirect from your DNS provider to these names,
thus making Google Cloud DNS authoritative for this zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L46">property project</a>
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

<h2 class="pdoc-module-header" id="RecordSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L16">class RecordSet</a>
</h2>

Manages a set of DNS records within Google Cloud DNS. For more information see [the official documentation](https://cloud.google.com/dns/records/) and
[API](https://cloud.google.com/dns/api/v1/resourceRecordSets).

~> **Note:** The Google Cloud DNS API requires NS records be present at all
times. To accommodate this, when creating NS records, the default records
Google automatically creates will be silently overwritten.  Also, when
destroying NS records, Terraform will not actually remove NS records, but will
report that it did.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L55">constructor</a>
</h3>

```typescript
new RecordSet(name: string, args: RecordSetArgs, opts?: pulumi.ResourceOptions)
```


Create a RecordSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordSetState): RecordSet
```


Get an existing RecordSet resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L33">property managedZone</a>
</h3>

```typescript
public managedZone: pulumi.Output<string>;
```


The name of the zone in which this record set will
reside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The DNS name this record set will apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L42">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L47">property rrdatas</a>
</h3>

```typescript
public rrdatas: pulumi.Output<string[]>;
```


The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding `\"` if you don't want your string to get split on spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L51">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The time-to-live of this record set (seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L55">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The DNS record set type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getManagedZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L29">function getManagedZone</a>
</h2>

```typescript
getManagedZone(args: GetManagedZoneArgs): Promise<GetManagedZoneResult>
```


Provides access to a zone's attributes within Google Cloud DNS.
For more information see
[the official documentation](https://cloud.google.com/dns/zones/)
and
[API](https://cloud.google.com/dns/api/v1/managedZones).

```hcl
data "google_dns_managed_zone" "env_dns_zone" {
  name        = "qa-zone"
}

resource "google_dns_record_set" "dns" {
  name = "my-address.${data.google_dns_managed_zone.env_dns_zone.dns_name}"
  type = "TXT"
  ttl  = 300

  managed_zone = "${data.google_dns_managed_zone.env_dns_zone.name}"

  rrdatas = ["test"]
}
```

<h2 class="pdoc-module-header" id="GetManagedZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L39">interface GetManagedZoneArgs</a>
</h2>

A collection of arguments for invoking getManagedZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L43">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


A unique name for the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L47">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project for the Google Cloud DNS zone.

<h2 class="pdoc-module-header" id="GetManagedZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L53">interface GetManagedZoneResult</a>
</h2>

A collection of values returned by getManagedZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L57">property description</a>
</h3>

```typescript
description: string;
```


A textual description field.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L61">property dnsName</a>
</h3>

```typescript
dnsName: string;
```


The fully qualified DNS name of this zone, e.g. `terraform.io.`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/getManagedZone.ts#L67">property nameServers</a>
</h3>

```typescript
nameServers: string[];
```


The list of nameservers that will be authoritative for this
domain. Use NS records to redirect from your DNS provider to these names,
thus making Google Cloud DNS authoritative for this zone.

<h2 class="pdoc-module-header" id="ManagedZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L113">interface ManagedZoneArgs</a>
</h2>

The set of arguments for constructing a ManagedZone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L117">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description field. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L121">property dnsName</a>
</h3>

```typescript
dnsName: pulumi.Input<string>;
```


The fully qualified DNS name of this zone, e.g. `terraform.io.`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L131">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="ManagedZoneState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L83">interface ManagedZoneState</a>
</h2>

Input properties used for looking up and filtering ManagedZone resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L87">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A textual description field. Defaults to 'Managed by Terraform'.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L91">property dnsName</a>
</h3>

```typescript
dnsName?: pulumi.Input<string>;
```


The fully qualified DNS name of this zone, e.g. `terraform.io.`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by GCE.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L102">property nameServers</a>
</h3>

```typescript
nameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of nameservers that will be authoritative for this
domain. Use NS records to redirect from your DNS provider to these names,
thus making Google Cloud DNS authoritative for this zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/managedZone.ts#L107">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="RecordSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L136">interface RecordSetArgs</a>
</h2>

The set of arguments for constructing a RecordSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L141">property managedZone</a>
</h3>

```typescript
managedZone: pulumi.Input<string>;
```


The name of the zone in which this record set will
reside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The DNS name this record set will apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L150">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L155">property rrdatas</a>
</h3>

```typescript
rrdatas: pulumi.Input<pulumi.Input<string>[]>;
```


The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding `\"` if you don't want your string to get split on spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L159">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The time-to-live of this record set (seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L163">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The DNS record set type.

<h2 class="pdoc-module-header" id="RecordSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L103">interface RecordSetState</a>
</h2>

Input properties used for looking up and filtering RecordSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L108">property managedZone</a>
</h3>

```typescript
managedZone?: pulumi.Input<string>;
```


The name of the zone in which this record set will
reside.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The DNS name this record set will apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L117">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L122">property rrdatas</a>
</h3>

```typescript
rrdatas?: pulumi.Input<pulumi.Input<string>[]>;
```


The string data for the records in this record set
whose meaning depends on the DNS type. For TXT record, if the string data contains spaces, add surrounding `\"` if you don't want your string to get split on spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L126">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The time-to-live of this record set (seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dns/recordSet.ts#L130">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The DNS record set type.

