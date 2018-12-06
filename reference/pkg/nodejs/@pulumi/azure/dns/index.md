---
title: Module dns
---

<a href="../index.html">@pulumi/azure</a> &gt; dns

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ARecord">class ARecord</a>
* <a href="#AaaaRecord">class AaaaRecord</a>
* <a href="#CNameRecord">class CNameRecord</a>
* <a href="#CaaRecord">class CaaRecord</a>
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
* <a href="#CaaRecordArgs">interface CaaRecordArgs</a>
* <a href="#CaaRecordState">interface CaaRecordState</a>
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

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts">dns/aRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts">dns/aaaaRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts">dns/cNameRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts">dns/caaRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts">dns/getZone.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts">dns/mxRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts">dns/nsRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts">dns/ptrRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts">dns/srvRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts">dns/txtRecord.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts">dns/zone.ts</a> 


<h2 class="pdoc-module-header" id="ARecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L10">class ARecord</a>
</h2>

Enables you to manage DNS A Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L43">constructor</a>
</h3>

```typescript
new ARecord(name: string, args: ARecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ARecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ARecordState): ARecord
```


Get an existing ARecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L39">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L43">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L10">class AaaaRecord</a>
</h2>

Enables you to manage DNS AAAA Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L43">constructor</a>
</h3>

```typescript
new AaaaRecord(name: string, args: AaaaRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AaaaRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AaaaRecordState): AaaaRecord
```


Get an existing AaaaRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L39">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L43">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L10">class CNameRecord</a>
</h2>

Enables you to manage DNS CNAME Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L43">constructor</a>
</h3>

```typescript
new CNameRecord(name: string, args: CNameRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CNameRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CNameRecordState): CNameRecord
```


Get an existing CNameRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L30">property record</a>
</h3>

```typescript
public record: pulumi.Output<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L39">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L43">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CaaRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L10">class CaaRecord</a>
</h2>

Enables you to manage DNS CAA Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L46">constructor</a>
</h3>

```typescript
new CaaRecord(name: string, args: CaaRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CaaRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CaaRecordState): CaaRecord
```


Get an existing CaaRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS CAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the CAA record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L42">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L46">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="MxRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L10">class MxRecord</a>
</h2>

Enables you to manage DNS MX Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L46">constructor</a>
</h3>

```typescript
new MxRecord(name: string, args: MxRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MxRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MxRecordState): MxRecord
```


Get an existing MxRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the MX record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L42">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L46">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L10">class NsRecord</a>
</h2>

Enables you to manage DNS NS Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L50">constructor</a>
</h3>

```typescript
new NsRecord(name: string, args: NsRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NsRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NsRecordState): NsRecord
```


Get an existing NsRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L30">property record</a>
</h3>

```typescript
public record: pulumi.Output<{ ... }[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L34">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L42">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L46">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L50">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L10">class PtrRecord</a>
</h2>

Enables you to manage DNS PTR Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L46">constructor</a>
</h3>

```typescript
new PtrRecord(name: string, args: PtrRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PtrRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PtrRecordState): PtrRecord
```


Get an existing PtrRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<string[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L42">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L46">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L10">class SrvRecord</a>
</h2>

Enables you to manage DNS SRV Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L46">constructor</a>
</h3>

```typescript
new SrvRecord(name: string, args: SrvRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SrvRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SrvRecordState): SrvRecord
```


Get an existing SrvRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L42">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L46">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L10">class TxtRecord</a>
</h2>

Enables you to manage DNS TXT Records within Azure DNS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L46">constructor</a>
</h3>

```typescript
new TxtRecord(name: string, args: TxtRecordArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TxtRecord resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TxtRecordState): TxtRecord
```


Get an existing TxtRecord resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L30">property records</a>
</h3>

```typescript
public records: pulumi.Output<{ ... }[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L38">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L42">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L46">property zoneName</a>
</h3>

```typescript
public zoneName: pulumi.Output<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="Zone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L10">class Zone</a>
</h2>

Enables you to manage DNS zones within Azure DNS. These zones are hosted on Azure's name servers to which you can delegate the zone from the parent domain.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L58">constructor</a>
</h3>

```typescript
new Zone(name: string, args: ZoneArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Zone resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ZoneState): Zone
```


Get an existing Zone resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L26">property maxNumberOfRecordSets</a>
</h3>

```typescript
public maxNumberOfRecordSets: pulumi.Output<string>;
```


(Optional) Maximum number of Records in the zone. Defaults to `1000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L34">property nameServers</a>
</h3>

```typescript
public nameServers: pulumi.Output<string[]>;
```


(Optional) A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L38">property numberOfRecordSets</a>
</h3>

```typescript
public numberOfRecordSets: pulumi.Output<string>;
```


(Optional) The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L42">property registrationVirtualNetworkIds</a>
</h3>

```typescript
public registrationVirtualNetworkIds: pulumi.Output<string[] | undefined>;
```


A list of Virtual Network ID's that register hostnames in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L46">property resolutionVirtualNetworkIds</a>
</h3>

```typescript
public resolutionVirtualNetworkIds: pulumi.Output<string[] | undefined>;
```


A list of Virtual Network ID's that resolve records in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L54">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L58">property zoneType</a>
</h3>

```typescript
public zoneType: pulumi.Output<string | undefined>;
```


Specifies the type of this DNS zone. Possible values are `Public` or `Private` (Defaults to `Public`).

<h2 class="pdoc-module-header" id="getZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L10">function getZone</a>
</h2>

```typescript
getZone(args: GetZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetZoneResult>
```


Use this data source to access information about an existing DNS Zone.

<h2 class="pdoc-module-header" id="ARecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L118">interface ARecordArgs</a>
</h2>

The set of arguments for constructing a ARecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L126">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L135">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L139">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ARecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L91">interface ARecordState</a>
</h2>

Input properties used for looking up and filtering ARecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS A Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L99">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv4 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L107">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L108">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aRecord.ts#L112">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L118">interface AaaaRecordArgs</a>
</h2>

The set of arguments for constructing a AaaaRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L126">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L135">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L139">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="AaaaRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L91">interface AaaaRecordState</a>
</h2>

Input properties used for looking up and filtering AaaaRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS AAAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L99">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of IPv6 Addresses.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L107">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L108">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/aaaaRecord.ts#L112">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L118">interface CNameRecordArgs</a>
</h2>

The set of arguments for constructing a CNameRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L126">property record</a>
</h3>

```typescript
record: pulumi.Input<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L135">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L139">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CNameRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L91">interface CNameRecordState</a>
</h2>

Input properties used for looking up and filtering CNameRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L95">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CNAME Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L99">property record</a>
</h3>

```typescript
record?: pulumi.Input<string>;
```


The target of the CNAME.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L103">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L107">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L108">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/cNameRecord.ts#L112">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CaaRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L124">interface CaaRecordArgs</a>
</h2>

The set of arguments for constructing a CaaRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L132">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the CAA record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L144">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L148">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="CaaRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L94">interface CaaRecordState</a>
</h2>

Input properties used for looking up and filtering CaaRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS CAA Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L102">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the CAA record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L114">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/caaRecord.ts#L118">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L20">interface GetZoneArgs</a>
</h2>

A collection of arguments for invoking getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the DNS Zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L30">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: string;
```


The Name of the Resource Group where the DNS Zone exists.
If the Name of the Resource Group is not provided, the first DNS Zone from the list of DNS Zones
in your subscription that matches `name` will be returned.

<h2 class="pdoc-module-header" id="GetZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L36">interface GetZoneResult</a>
</h2>

A collection of values returned by getZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L69">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L40">property maxNumberOfRecordSets</a>
</h3>

```typescript
maxNumberOfRecordSets: string;
```


Maximum number of Records in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L44">property nameServers</a>
</h3>

```typescript
nameServers: string[];
```


A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L48">property numberOfRecordSets</a>
</h3>

```typescript
numberOfRecordSets: string;
```


The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L52">property registrationVirtualNetworkIds</a>
</h3>

```typescript
registrationVirtualNetworkIds: string[];
```


A list of Virtual Network ID's that register hostnames in this DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L56">property resolutionVirtualNetworkIds</a>
</h3>

```typescript
resolutionVirtualNetworkIds: string[];
```


A list of Virtual Network ID's that resolve records in this DNS zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L57">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L61">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/getZone.ts#L65">property zoneType</a>
</h3>

```typescript
zoneType: string;
```


The type of this DNS zone, such as `Public` or `Private`.

<h2 class="pdoc-module-header" id="MxRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L124">interface MxRecordArgs</a>
</h2>

The set of arguments for constructing a MxRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L132">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the MX record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L144">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L148">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="MxRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L94">interface MxRecordState</a>
</h2>

Input properties used for looking up and filtering MxRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS MX Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L102">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the MX record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L114">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/mxRecord.ts#L118">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L131">interface NsRecordArgs</a>
</h2>

The set of arguments for constructing a NsRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L139">property record</a>
</h3>

```typescript
record?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L143">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L147">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L151">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L155">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L159">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="NsRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L97">interface NsRecordState</a>
</h2>

Input properties used for looking up and filtering NsRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS NS Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L105">property record</a>
</h3>

```typescript
record?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the NS record. Each `record` block supports fields documented below. This field has been deprecated and will be removed in a future release.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L109">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of values that make up the NS record. *WARNING*: Either `records` or `record` is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L113">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L117">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L121">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/nsRecord.ts#L125">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L124">interface PtrRecordArgs</a>
</h2>

The set of arguments for constructing a PtrRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L132">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<string>[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L144">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L148">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="PtrRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L94">interface PtrRecordState</a>
</h2>

Input properties used for looking up and filtering PtrRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS PTR Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L102">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<string>[]>;
```


List of Fully Qualified Domain Names.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L114">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/ptrRecord.ts#L118">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L124">interface SrvRecordArgs</a>
</h2>

The set of arguments for constructing a SrvRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L132">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L144">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L148">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SrvRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L94">interface SrvRecordState</a>
</h2>

Input properties used for looking up and filtering SrvRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS SRV Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L102">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the SRV record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L114">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/srvRecord.ts#L118">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecordArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L124">interface TxtRecordArgs</a>
</h2>

The set of arguments for constructing a TxtRecord resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L132">property records</a>
</h3>

```typescript
records: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L136">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L140">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L144">property ttl</a>
</h3>

```typescript
ttl: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L148">property zoneName</a>
</h3>

```typescript
zoneName: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TxtRecordState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L94">interface TxtRecordState</a>
</h2>

Input properties used for looking up and filtering TxtRecord resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS TXT Record.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L102">property records</a>
</h3>

```typescript
records?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A list of values that make up the txt record. Each `record` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L106">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L110">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L114">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<number>;
```


The Time To Live (TTL) of the DNS record in seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/txtRecord.ts#L118">property zoneName</a>
</h3>

```typescript
zoneName?: pulumi.Input<string>;
```


Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L145">interface ZoneArgs</a>
</h2>

The set of arguments for constructing a Zone resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L153">property registrationVirtualNetworkIds</a>
</h3>

```typescript
registrationVirtualNetworkIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Network ID's that register hostnames in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L157">property resolutionVirtualNetworkIds</a>
</h3>

```typescript
resolutionVirtualNetworkIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Network ID's that resolve records in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L161">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L165">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L169">property zoneType</a>
</h3>

```typescript
zoneType?: pulumi.Input<string>;
```


Specifies the type of this DNS zone. Possible values are `Public` or `Private` (Defaults to `Public`).

<h2 class="pdoc-module-header" id="ZoneState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L103">interface ZoneState</a>
</h2>

Input properties used for looking up and filtering Zone resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L107">property maxNumberOfRecordSets</a>
</h3>

```typescript
maxNumberOfRecordSets?: pulumi.Input<string>;
```


(Optional) Maximum number of Records in the zone. Defaults to `1000`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the DNS Zone. Must be a valid domain name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L115">property nameServers</a>
</h3>

```typescript
nameServers?: pulumi.Input<pulumi.Input<string>[]>;
```


(Optional) A list of values that make up the NS record for the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L119">property numberOfRecordSets</a>
</h3>

```typescript
numberOfRecordSets?: pulumi.Input<string>;
```


(Optional) The number of records already in the zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L123">property registrationVirtualNetworkIds</a>
</h3>

```typescript
registrationVirtualNetworkIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Network ID's that register hostnames in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L127">property resolutionVirtualNetworkIds</a>
</h3>

```typescript
resolutionVirtualNetworkIds?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of Virtual Network ID's that resolve records in this DNS zone. This field can only be set when `zone_type` is set to `Private`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


Specifies the resource group where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/dns/zone.ts#L139">property zoneType</a>
</h3>

```typescript
zoneType?: pulumi.Input<string>;
```


Specifies the type of this DNS zone. Possible values are `Public` or `Private` (Defaults to `Public`).

