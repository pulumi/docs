---
title: Module glacier
---

<a href="../index.html">@pulumi/aws</a> &gt; glacier

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Alias">class Alias</a>
* <a href="#Build">class Build</a>
* <a href="#Detector">class Detector</a>
* <a href="#Fleet">class Fleet</a>
* <a href="#IPSet">class IPSet</a>
* <a href="#Member">class Member</a>
* <a href="#ThreatIntelSet">class ThreatIntelSet</a>
* <a href="#Vault">class Vault</a>
* <a href="#AliasArgs">interface AliasArgs</a>
* <a href="#AliasState">interface AliasState</a>
* <a href="#BuildArgs">interface BuildArgs</a>
* <a href="#BuildState">interface BuildState</a>
* <a href="#DetectorArgs">interface DetectorArgs</a>
* <a href="#DetectorState">interface DetectorState</a>
* <a href="#FleetArgs">interface FleetArgs</a>
* <a href="#FleetState">interface FleetState</a>
* <a href="#IPSetArgs">interface IPSetArgs</a>
* <a href="#IPSetState">interface IPSetState</a>
* <a href="#MemberArgs">interface MemberArgs</a>
* <a href="#MemberState">interface MemberState</a>
* <a href="#ThreatIntelSetArgs">interface ThreatIntelSetArgs</a>
* <a href="#ThreatIntelSetState">interface ThreatIntelSetState</a>
* <a href="#VaultArgs">interface VaultArgs</a>
* <a href="#VaultState">interface VaultState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts">glacier/alias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts">glacier/build.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts">glacier/detector.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts">glacier/fleet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts">glacier/iPSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts">glacier/member.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts">glacier/threatIntelSet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts">glacier/vault.ts</a> 


<h2 class="pdoc-module-header" id="Alias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L10">class Alias</a>
</h2>

Provides a Gamelift Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L38">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AliasState): Alias
```


Get an existing Alias resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L38">property routingStrategy</a>
</h3>

```typescript
public routingStrategy: pulumi.Output<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Build">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L10">class Build</a>
</h2>

Provides an Gamelift Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L38">constructor</a>
</h3>

```typescript
new Build(name: string, args: BuildArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Build resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BuildState): Build
```


Get an existing Build resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L30">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L34">property storageLocation</a>
</h3>

```typescript
public storageLocation: pulumi.Output<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L38">property version</a>
</h3>

```typescript
public version: pulumi.Output<string | undefined>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="Detector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L12">class Detector</a>
</h2>

Provides a resource to manage a GuardDuty detector.

~> **NOTE:** Deleting this resource is equivalent to "disabling" GuardDuty for an AWS region, which removes all existing findings. You can set the `enable` attribute to `false` to instead "suspend" monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L32">constructor</a>
</h3>

```typescript
new Detector(name: string, args?: DetectorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Detector resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DetectorState): Detector
```


Get an existing Detector resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L28">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L32">property enable</a>
</h3>

```typescript
public enable: pulumi.Output<boolean | undefined>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Fleet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L10">class Fleet</a>
</h2>

Provides a Gamelift Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L67">constructor</a>
</h3>

```typescript
new Fleet(name: string, args: FleetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Fleet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FleetState): Fleet
```


Get an existing Fleet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L30">property buildId</a>
</h3>

```typescript
public buildId: pulumi.Output<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L38">property ec2InboundPermissions</a>
</h3>

```typescript
public ec2InboundPermissions: pulumi.Output<{ ... }[] | undefined>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L42">property ec2InstanceType</a>
</h3>

```typescript
public ec2InstanceType: pulumi.Output<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L43">property logPaths</a>
</h3>

```typescript
public logPaths: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L47">property metricGroups</a>
</h3>

```typescript
public metricGroups: pulumi.Output<string[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L55">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
public newGameSessionProtectionPolicy: pulumi.Output<string | undefined>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L59">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L63">property resourceCreationLimitPolicy</a>
</h3>

```typescript
public resourceCreationLimitPolicy: pulumi.Output<{ ... } | undefined>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L67">property runtimeConfiguration</a>
</h3>

```typescript
public runtimeConfiguration: pulumi.Output<{ ... } | undefined>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IPSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L12">class IPSet</a>
</h2>

Provides a resource to manage a GuardDuty IPSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L44">constructor</a>
</h3>

```typescript
new IPSet(name: string, args: IPSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IPSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IPSetState): IPSet
```


Get an existing IPSet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L28">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L36">property format</a>
</h3>

```typescript
public format: pulumi.Output<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name to identify the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Member">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L12">class Member</a>
</h2>

Provides a resource to manage a GuardDuty member.

~> **NOTE:** Currently after using this resource, you must manually accept member account invitations before GuardDuty will begin sending cross-account events. More information for how to accomplish this via the AWS Console or API can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html). Terraform implementation of the member acceptance resource can be tracked in [Github](https://github.com/terraform-providers/terraform-provider-aws/issues/2489).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L52">constructor</a>
</h3>

```typescript
new Member(name: string, args: MemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Member resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberState): Member
```


Get an existing Member resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L28">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L36">property disableEmailNotification</a>
</h3>

```typescript
public disableEmailNotification: pulumi.Output<boolean | undefined>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L40">property email</a>
</h3>

```typescript
public email: pulumi.Output<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L44">property invitationMessage</a>
</h3>

```typescript
public invitationMessage: pulumi.Output<string | undefined>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L48">property invite</a>
</h3>

```typescript
public invite: pulumi.Output<boolean | undefined>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L52">property relationshipStatus</a>
</h3>

```typescript
public relationshipStatus: pulumi.Output<string>;
```


The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ThreatIntelSet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L12">class ThreatIntelSet</a>
</h2>

Provides a resource to manage a GuardDuty ThreatIntelSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L44">constructor</a>
</h3>

```typescript
new ThreatIntelSet(name: string, args: ThreatIntelSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ThreatIntelSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThreatIntelSetState): ThreatIntelSet
```


Get an existing ThreatIntelSet resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L28">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L32">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L36">property format</a>
</h3>

```typescript
public format: pulumi.Output<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L40">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name to identify the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Vault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L14">class Vault</a>
</h2>

Provides a Glacier Vault Resource. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html) for a full explanation of the Glacier Vault functionality

~> **NOTE:** When removing a Glacier Vault, the Vault must be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L51">constructor</a>
</h3>

```typescript
new Vault(name: string, args?: VaultArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultState): Vault
```


Get an existing Vault resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L31">property accessPolicy</a>
</h3>

```typescript
public accessPolicy: pulumi.Output<string | undefined>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L35">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L39">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the vault that was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L43">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L47">property notifications</a>
</h3>

```typescript
public notifications: pulumi.Output<{ ... }[] | undefined>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L51">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L95">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L107">property routingStrategy</a>
</h3>

```typescript
routingStrategy: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L73">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L81">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L89">property routingStrategy</a>
</h3>

```typescript
routingStrategy?: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="BuildArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L98">interface BuildArgs</a>
</h2>

The set of arguments for constructing a Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L106">property operatingSystem</a>
</h3>

```typescript
operatingSystem: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L110">property storageLocation</a>
</h3>

```typescript
storageLocation: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L114">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="BuildState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L76">interface BuildState</a>
</h2>

Input properties used for looking up and filtering Build resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L84">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L88">property storageLocation</a>
</h3>

```typescript
storageLocation?: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L92">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="DetectorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L74">interface DetectorArgs</a>
</h2>

The set of arguments for constructing a Detector resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L78">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="DetectorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L60">interface DetectorState</a>
</h2>

Input properties used for looking up and filtering Detector resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L64">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L68">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="FleetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L172">interface FleetArgs</a>
</h2>

The set of arguments for constructing a Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L176">property buildId</a>
</h3>

```typescript
buildId: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L180">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L184">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L188">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L192">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L196">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L200">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L204">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L208">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="FleetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L121">interface FleetState</a>
</h2>

Input properties used for looking up and filtering Fleet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L125">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L129">property buildId</a>
</h3>

```typescript
buildId?: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L137">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L141">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType?: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L142">property logPaths</a>
</h3>

```typescript
logPaths?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L146">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L154">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L158">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L162">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L166">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="IPSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L116">interface IPSetArgs</a>
</h2>

The set of arguments for constructing a IPSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L120">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L124">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L128">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="IPSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L90">interface IPSetState</a>
</h2>

Input properties used for looking up and filtering IPSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L94">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L98">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L102">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L106">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="MemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L133">interface MemberArgs</a>
</h2>

The set of arguments for constructing a Member resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L137">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L141">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L145">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L149">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L153">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L157">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h2 class="pdoc-module-header" id="MemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L99">interface MemberState</a>
</h2>

Input properties used for looking up and filtering Member resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L103">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L107">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L111">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L115">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L119">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L123">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L127">property relationshipStatus</a>
</h3>

```typescript
relationshipStatus?: pulumi.Input<string>;
```


The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).

<h2 class="pdoc-module-header" id="ThreatIntelSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L116">interface ThreatIntelSetArgs</a>
</h2>

The set of arguments for constructing a ThreatIntelSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L120">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L124">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L128">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L132">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

<h2 class="pdoc-module-header" id="ThreatIntelSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L90">interface ThreatIntelSetState</a>
</h2>

Input properties used for looking up and filtering ThreatIntelSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L94">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L98">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L102">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L106">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

<h2 class="pdoc-module-header" id="VaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L118">interface VaultArgs</a>
</h2>

The set of arguments for constructing a Vault resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L123">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L131">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VaultState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L87">interface VaultState</a>
</h2>

Input properties used for looking up and filtering Vault resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L92">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L96">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L100">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the vault that was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L108">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L112">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

