---
title: Module dns
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ARecord">class ARecord</a>
* <a href="#AaaaRecord">class AaaaRecord</a>
* <a href="#CNameRecord">class CNameRecord</a>
* <a href="#MxRecord">class MxRecord</a>
* <a href="#NsRecord">class NsRecord</a>
* <a href="#PtrRecord">class PtrRecord</a>
* <a href="#SrvRecord">class SrvRecord</a>
* <a href="#TxtRecord">class TxtRecord</a>
* <a href="#Zone">class Zone</a>
* <a href="#getZone">function getZone</a>
* <a href="#ARecordArgs">interface ARecordArgs</a>
* <a href="#ARecordState">interface ARecordState</a>
* <a href="#AaaaRecordArgs">interface AaaaRecordArgs</a>
* <a href="#AaaaRecordState">interface AaaaRecordState</a>
* <a href="#CNameRecordArgs">interface CNameRecordArgs</a>
* <a href="#CNameRecordState">interface CNameRecordState</a>
* <a href="#GetZoneArgs">interface GetZoneArgs</a>
* <a href="#GetZoneResult">interface GetZoneResult</a>
* <a href="#MxRecordArgs">interface MxRecordArgs</a>
* <a href="#MxRecordState">interface MxRecordState</a>
* <a href="#NsRecordArgs">interface NsRecordArgs</a>
* <a href="#NsRecordState">interface NsRecordState</a>
* <a href="#PtrRecordArgs">interface PtrRecordArgs</a>
* <a href="#PtrRecordState">interface PtrRecordState</a>
* <a href="#SrvRecordArgs">interface SrvRecordArgs</a>
* <a href="#SrvRecordState">interface SrvRecordState</a>
* <a href="#TxtRecordArgs">interface TxtRecordArgs</a>
* <a href="#TxtRecordState">interface TxtRecordState</a>
* <a href="#ZoneArgs">interface ZoneArgs</a>
* <a href="#ZoneState">interface ZoneState</a>

<a href="/dns/aRecord.ts">dns/aRecord.ts</a> <a href="/dns/aaaaRecord.ts">dns/aaaaRecord.ts</a> <a href="/dns/cNameRecord.ts">dns/cNameRecord.ts</a> <a href="/dns/getZone.ts">dns/getZone.ts</a> <a href="/dns/mxRecord.ts">dns/mxRecord.ts</a> <a href="/dns/nsRecord.ts">dns/nsRecord.ts</a> <a href="/dns/ptrRecord.ts">dns/ptrRecord.ts</a> <a href="/dns/srvRecord.ts">dns/srvRecord.ts</a> <a href="/dns/txtRecord.ts">dns/txtRecord.ts</a> <a href="/dns/zone.ts">dns/zone.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="ARecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L9">class ARecord</a>
</h2>

Enables you to manage DNS A Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L42">constructor</a>
</h3>

```typescript
new ARecord(name: string, args: ARecordArgs, opts?: pulumi.ResourceOptions)
```


Create a ARecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ARecord(name: string, state?: ARecordState, opts?: pulumi.ResourceOptions)
```


Create a ARecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ARecordState): ARecord
```


Get an existing ARecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L38">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L42">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L9">class AaaaRecord</a>
</h2>

Enables you to manage DNS AAAA Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L42">constructor</a>
</h3>

```typescript
new AaaaRecord(name: string, args: AaaaRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a AaaaRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new AaaaRecord(name: string, state?: AaaaRecordState, opts?: pulumi.ResourceOptions)
```


Create a AaaaRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AaaaRecordState): AaaaRecord
```


Get an existing AaaaRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L38">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L42">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L9">class CNameRecord</a>
</h2>

Enables you to manage DNS CNAME Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L42">constructor</a>
</h3>

```typescript
new CNameRecord(name: string, args: CNameRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a CNameRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new CNameRecord(name: string, state?: CNameRecordState, opts?: pulumi.ResourceOptions)
```


Create a CNameRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CNameRecordState): CNameRecord
```


Get an existing CNameRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L29">property record</a>
</h3>

```typescript
public record: pulumi.Output<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L38">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L42">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="MxRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L9">class MxRecord</a>
</h2>

Enables you to manage DNS MX Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L45">constructor</a>
</h3>

```typescript
new MxRecord(name: string, args: MxRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a MxRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new MxRecord(name: string, state?: MxRecordState, opts?: pulumi.ResourceOptions)
```


Create a MxRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MxRecordState): MxRecord
```


Get an existing MxRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L41">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L45">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L9">class NsRecord</a>
</h2>

Enables you to manage DNS NS Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L45">constructor</a>
</h3>

```typescript
new NsRecord(name: string, args: NsRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a NsRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new NsRecord(name: string, state?: NsRecordState, opts?: pulumi.ResourceOptions)
```


Create a NsRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NsRecordState): NsRecord
```


Get an existing NsRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L41">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L45">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L9">class PtrRecord</a>
</h2>

Enables you to manage DNS PTR Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L45">constructor</a>
</h3>

```typescript
new PtrRecord(name: string, args: PtrRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a PtrRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new PtrRecord(name: string, state?: PtrRecordState, opts?: pulumi.ResourceOptions)
```


Create a PtrRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PtrRecordState): PtrRecord
```


Get an existing PtrRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L41">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L45">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L9">class SrvRecord</a>
</h2>

Enables you to manage DNS SRV Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L45">constructor</a>
</h3>

```typescript
new SrvRecord(name: string, args: SrvRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a SrvRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new SrvRecord(name: string, state?: SrvRecordState, opts?: pulumi.ResourceOptions)
```


Create a SrvRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SrvRecordState): SrvRecord
```


Get an existing SrvRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L41">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L45">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L9">class TxtRecord</a>
</h2>

Enables you to manage DNS TXT Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L45">constructor</a>
</h3>

```typescript
new TxtRecord(name: string, args: TxtRecordArgs, opts?: pulumi.ResourceOptions)
```


Create a TxtRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new TxtRecord(name: string, state?: TxtRecordState, opts?: pulumi.ResourceOptions)
```


Create a TxtRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TxtRecordState): TxtRecord
```


Get an existing TxtRecord resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L29">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L41">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L45">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="Zone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L9">class Zone</a>
</h2>

Enables you to manage DNS zones within Azure DNS. These zones are hosted on Azure's name servers to which you can delegate the zone from the parent domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L45">constructor</a>
</h3>

```typescript
new Zone(name: string, args: ZoneArgs, opts?: pulumi.ResourceOptions)
```


Create a Zone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Zone(name: string, state?: ZoneState, opts?: pulumi.ResourceOptions)
```


Create a Zone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState): Zone
```


Get an existing Zone resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L25">property maxNumberOfRecordSets</a>
</h3>

```typescript
public maxNumberOfRecordSets: pulumi.Output<string>;
```


(Optional) Maximum number of Records in the zone. Defaults to `1000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L33">property nameServers</a>
</h3>

```typescript
public nameServers: pulumi.Output<string[]>;
```


(Optional) A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L37">property numberOfRecordSets</a>
</h3>

```typescript
public numberOfRecordSets: pulumi.Output<string>;
```


(Optional) The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L45">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L9">function getZone</a>
</h2>

```typescript
getZone(args: GetZoneArgs): Promise<GetZoneResult>
```


Use this data source to obtain information about a DNS Zone.

<h2 class="pdoc-module-header" id="ARecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L119">interface ARecordArgs</a>
</h2>

The set of arguments for constructing a ARecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L127">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L136">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L140">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ARecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L92">interface ARecordState</a>
</h2>

Input properties used for looking up and filtering ARecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L100">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L108">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L109">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aRecord.ts#L113">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L119">interface AaaaRecordArgs</a>
</h2>

The set of arguments for constructing a AaaaRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L127">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L136">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L140">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L92">interface AaaaRecordState</a>
</h2>

Input properties used for looking up and filtering AaaaRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L100">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L108">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L109">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/aaaaRecord.ts#L113">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L119">interface CNameRecordArgs</a>
</h2>

The set of arguments for constructing a CNameRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L127">property record</a>
</h3>

```typescript
record: pulumi.Input<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L136">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L140">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L92">interface CNameRecordState</a>
</h2>

Input properties used for looking up and filtering CNameRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L100">property record</a>
</h3>

```typescript
record?: pulumi.Input<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L108">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L109">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/cNameRecord.ts#L113">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L19">interface GetZoneArgs</a>
</h2>

A collection of arguments for invoking getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the DNS Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The Name of the Resource Group where the DNS Zone exists.

<h2 class="pdoc-module-header" id="GetZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L33">interface GetZoneResult</a>
</h2>

A collection of values returned by getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L37">property maxNumberOfRecordSets</a>
</h3>

```typescript
maxNumberOfRecordSets: string;
```


Maximum number of Records in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L41">property nameServers</a>
</h3>

```typescript
nameServers: string[];
```


A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L45">property numberOfRecordSets</a>
</h3>

```typescript
numberOfRecordSets: string;
```


The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/getZone.ts#L49">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the EventHub Namespace.

<h2 class="pdoc-module-header" id="MxRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L125">interface MxRecordArgs</a>
</h2>

The set of arguments for constructing a MxRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L133">property records</a>
</h3>

```typescript
records: pulumi.Input<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L145">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L149">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="MxRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L95">interface MxRecordState</a>
</h2>

Input properties used for looking up and filtering MxRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L103">property records</a>
</h3>

```typescript
records?: pulumi.Input<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L115">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/mxRecord.ts#L119">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L125">interface NsRecordArgs</a>
</h2>

The set of arguments for constructing a NsRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L133">property records</a>
</h3>

```typescript
records: pulumi.Input<{ ... }[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L145">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L149">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L95">interface NsRecordState</a>
</h2>

Input properties used for looking up and filtering NsRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L103">property records</a>
</h3>

```typescript
records?: pulumi.Input<{ ... }[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L115">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/nsRecord.ts#L119">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L125">interface PtrRecordArgs</a>
</h2>

The set of arguments for constructing a PtrRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L133">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L145">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L149">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L95">interface PtrRecordState</a>
</h2>

Input properties used for looking up and filtering PtrRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L103">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L115">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/ptrRecord.ts#L119">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L125">interface SrvRecordArgs</a>
</h2>

The set of arguments for constructing a SrvRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L133">property records</a>
</h3>

```typescript
records: pulumi.Input<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L145">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L149">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L95">interface SrvRecordState</a>
</h2>

Input properties used for looking up and filtering SrvRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L103">property records</a>
</h3>

```typescript
records?: pulumi.Input<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L115">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/srvRecord.ts#L119">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L125">interface TxtRecordArgs</a>
</h2>

The set of arguments for constructing a TxtRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L133">property records</a>
</h3>

```typescript
records: pulumi.Input<{ ... }[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L145">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L149">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L95">interface TxtRecordState</a>
</h2>

Input properties used for looking up and filtering TxtRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L99">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L103">property records</a>
</h3>

```typescript
records?: pulumi.Input<{ ... }[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L115">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/txtRecord.ts#L119">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L116">interface ZoneArgs</a>
</h2>

The set of arguments for constructing a Zone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L124">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ZoneState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L86">interface ZoneState</a>
</h2>

Input properties used for looking up and filtering Zone resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L90">property maxNumberOfRecordSets</a>
</h3>

```typescript
maxNumberOfRecordSets?: pulumi.Input<string>;
```


(Optional) Maximum number of Records in the zone. Defaults to `1000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L98">property nameServers</a>
</h3>

```typescript
nameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


(Optional) A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L102">property numberOfRecordSets</a>
</h3>

```typescript
numberOfRecordSets?: pulumi.Input<string>;
```


(Optional) The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/dns/zone.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

