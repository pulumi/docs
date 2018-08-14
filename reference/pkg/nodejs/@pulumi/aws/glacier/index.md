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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L9">class Alias</a>
</h2>

Provides a Gamelift Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L37">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L29">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L37">property routingStrategy</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L9">class Build</a>
</h2>

Provides an Gamelift Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L37">constructor</a>
</h3>

```typescript
new Build(name: string, args: BuildArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Build resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L25">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L29">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L33">property storageLocation</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L37">property version</a>
</h3>

```typescript
public version: pulumi.Output<string | undefined>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="Detector">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L11">class Detector</a>
</h2>

Provides a resource to manage a GuardDuty detector.

~> **NOTE:** Deleting this resource is equivalent to "disabling" GuardDuty for an AWS region, which removes all existing findings. You can set the `enable` attribute to `false` to instead "suspend" monitoring and feedback reporting while keeping existing data. See the [Suspending or Disabling Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L31">constructor</a>
</h3>

```typescript
new Detector(name: string, args?: DetectorArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Detector resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L27">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L31">property enable</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L9">class Fleet</a>
</h2>

Provides a Gamelift Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L66">constructor</a>
</h3>

```typescript
new Fleet(name: string, args: FleetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Fleet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L29">property buildId</a>
</h3>

```typescript
public buildId: pulumi.Output<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L37">property ec2InboundPermissions</a>
</h3>

```typescript
public ec2InboundPermissions: pulumi.Output<{ ... }[] | undefined>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L41">property ec2InstanceType</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L42">property logPaths</a>
</h3>

```typescript
public logPaths: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L46">property metricGroups</a>
</h3>

```typescript
public metricGroups: pulumi.Output<string[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L54">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
public newGameSessionProtectionPolicy: pulumi.Output<string | undefined>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L58">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L62">property resourceCreationLimitPolicy</a>
</h3>

```typescript
public resourceCreationLimitPolicy: pulumi.Output<{ ... } | undefined>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L66">property runtimeConfiguration</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L11">class IPSet</a>
</h2>

Provides a resource to manage a GuardDuty IPSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage IPSets. IPSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-ip-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L43">constructor</a>
</h3>

```typescript
new IPSet(name: string, args: IPSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IPSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L27">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L31">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L35">property format</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L39">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L43">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L11">class Member</a>
</h2>

Provides a resource to manage a GuardDuty member.

~> **NOTE:** Currently after using this resource, you must manually accept member account invitations before GuardDuty will begin sending cross-account events. More information for how to accomplish this via the AWS Console or API can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html). Terraform implementation of the member acceptance resource can be tracked in [Github](https://github.com/terraform-providers/terraform-provider-aws/issues/2489).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L51">constructor</a>
</h3>

```typescript
new Member(name: string, args: MemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Member resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L27">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L31">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L35">property disableEmailNotification</a>
</h3>

```typescript
public disableEmailNotification: pulumi.Output<boolean | undefined>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L39">property email</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L43">property invitationMessage</a>
</h3>

```typescript
public invitationMessage: pulumi.Output<string | undefined>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L47">property invite</a>
</h3>

```typescript
public invite: pulumi.Output<boolean | undefined>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L51">property relationshipStatus</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L11">class ThreatIntelSet</a>
</h2>

Provides a resource to manage a GuardDuty ThreatIntelSet.

~> **Note:** Currently in GuardDuty, users from member accounts cannot upload and further manage ThreatIntelSets. ThreatIntelSets that are uploaded by the master account are imposed on GuardDuty functionality in its member accounts. See the [GuardDuty API Documentation](https://docs.aws.amazon.com/guardduty/latest/ug/create-threat-intel-set.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L43">constructor</a>
</h3>

```typescript
new ThreatIntelSet(name: string, args: ThreatIntelSetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ThreatIntelSet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L27">property activate</a>
</h3>

```typescript
public activate: pulumi.Output<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L31">property detectorId</a>
</h3>

```typescript
public detectorId: pulumi.Output<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L35">property format</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L39">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L43">property name</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L13">class Vault</a>
</h2>

Provides a Glacier Vault Resource. You can refer to the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html) for a full explanation of the Glacier Vault functionality

~> **NOTE:** When removing a Glacier Vault, the Vault must be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L50">constructor</a>
</h3>

```typescript
new Vault(name: string, args?: VaultArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L30">property accessPolicy</a>
</h3>

```typescript
public accessPolicy: pulumi.Output<string | undefined>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L34">property arn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L38">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The URI of the vault that was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L42">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L46">property notifications</a>
</h3>

```typescript
public notifications: pulumi.Output<{ ... }[] | undefined>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L50">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L94">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L106">property routingStrategy</a>
</h3>

```typescript
routingStrategy: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L72">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L76">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L80">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/alias.ts#L88">property routingStrategy</a>
</h3>

```typescript
routingStrategy?: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="BuildArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L97">interface BuildArgs</a>
</h2>

The set of arguments for constructing a Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L105">property operatingSystem</a>
</h3>

```typescript
operatingSystem: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L109">property storageLocation</a>
</h3>

```typescript
storageLocation: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L113">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="BuildState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L75">interface BuildState</a>
</h2>

Input properties used for looking up and filtering Build resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L79">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L83">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L87">property storageLocation</a>
</h3>

```typescript
storageLocation?: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/build.ts#L91">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="DetectorArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L73">interface DetectorArgs</a>
</h2>

The set of arguments for constructing a Detector resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L77">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="DetectorState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L59">interface DetectorState</a>
</h2>

Input properties used for looking up and filtering Detector resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L63">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The AWS account ID of the GuardDuty detector

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/detector.ts#L67">property enable</a>
</h3>

```typescript
enable?: pulumi.Input<boolean>;
```


Enable monitoring and feedback reporting. Setting to `false` is equivalent to "suspending" GuardDuty. Defaults to `true`.

<h2 class="pdoc-module-header" id="FleetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L171">interface FleetArgs</a>
</h2>

The set of arguments for constructing a Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L175">property buildId</a>
</h3>

```typescript
buildId: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L179">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L183">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L187">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L191">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L195">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L199">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L203">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L207">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="FleetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L120">interface FleetState</a>
</h2>

Input properties used for looking up and filtering Fleet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L124">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L128">property buildId</a>
</h3>

```typescript
buildId?: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L136">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L140">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType?: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L141">property logPaths</a>
</h3>

```typescript
logPaths?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L145">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L153">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L157">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L161">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/fleet.ts#L165">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="IPSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L115">interface IPSetArgs</a>
</h2>

The set of arguments for constructing a IPSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L119">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L123">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L127">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L131">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="IPSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L89">interface IPSetState</a>
</h2>

Input properties used for looking up and filtering IPSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L93">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L97">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L101">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the IPSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L105">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the IPSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/iPSet.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the IPSet.

<h2 class="pdoc-module-header" id="MemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L132">interface MemberArgs</a>
</h2>

The set of arguments for constructing a Member resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L136">property accountId</a>
</h3>

```typescript
accountId: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L140">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L144">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L148">property email</a>
</h3>

```typescript
email: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L152">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L156">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h2 class="pdoc-module-header" id="MemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L98">interface MemberState</a>
</h2>

Input properties used for looking up and filtering Member resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L102">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


AWS account ID for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L106">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty account where you want to create member accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L110">property disableEmailNotification</a>
</h3>

```typescript
disableEmailNotification?: pulumi.Input<boolean>;
```


Boolean whether an email notification is sent to the accounts. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L114">property email</a>
</h3>

```typescript
email?: pulumi.Input<string>;
```


Email address for member account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L118">property invitationMessage</a>
</h3>

```typescript
invitationMessage?: pulumi.Input<string>;
```


Message for invitation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L122">property invite</a>
</h3>

```typescript
invite?: pulumi.Input<boolean>;
```


Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/member.ts#L126">property relationshipStatus</a>
</h3>

```typescript
relationshipStatus?: pulumi.Input<string>;
```


The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).

<h2 class="pdoc-module-header" id="ThreatIntelSetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L115">interface ThreatIntelSetArgs</a>
</h2>

The set of arguments for constructing a ThreatIntelSet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L119">property activate</a>
</h3>

```typescript
activate: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L123">property detectorId</a>
</h3>

```typescript
detectorId: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L127">property format</a>
</h3>

```typescript
format: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L131">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

<h2 class="pdoc-module-header" id="ThreatIntelSetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L89">interface ThreatIntelSetState</a>
</h2>

Input properties used for looking up and filtering ThreatIntelSet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L93">property activate</a>
</h3>

```typescript
activate?: pulumi.Input<boolean>;
```


Specifies whether GuardDuty is to start using the uploaded ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L97">property detectorId</a>
</h3>

```typescript
detectorId?: pulumi.Input<string>;
```


The detector ID of the GuardDuty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L101">property format</a>
</h3>

```typescript
format?: pulumi.Input<string>;
```


The format of the file that contains the ThreatIntelSet. Valid values: `TXT` | `STIX` | `OTX_CSV` | `ALIEN_VAULT` | `PROOF_POINT` | `FIRE_EYE`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L105">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the file that contains the ThreatIntelSet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/threatIntelSet.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name to identify the ThreatIntelSet.

<h2 class="pdoc-module-header" id="VaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L117">interface VaultArgs</a>
</h2>

The set of arguments for constructing a Vault resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L122">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L130">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VaultState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L86">interface VaultState</a>
</h2>

Input properties used for looking up and filtering Vault resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L91">property accessPolicy</a>
</h3>

```typescript
accessPolicy?: pulumi.Input<string>;
```


The policy document. This is a JSON formatted string.
The heredoc syntax or `file` function is helpful here. Use the [Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html) for more information on Glacier Vault Policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L95">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L99">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The URI of the vault that was created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Vault. Names can be between 1 and 255 characters long and the valid characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L107">property notifications</a>
</h3>

```typescript
notifications?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The notifications for the Vault. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glacier/vault.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

