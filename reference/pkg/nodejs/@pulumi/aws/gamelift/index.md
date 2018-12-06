---
title: Module gamelift
---

<a href="../index.html">@pulumi/aws</a> &gt; gamelift

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Alias">class Alias</a>
* <a href="#Build">class Build</a>
* <a href="#Fleet">class Fleet</a>
* <a href="#GameSessionQueue">class GameSessionQueue</a>
* <a href="#AliasArgs">interface AliasArgs</a>
* <a href="#AliasState">interface AliasState</a>
* <a href="#BuildArgs">interface BuildArgs</a>
* <a href="#BuildState">interface BuildState</a>
* <a href="#FleetArgs">interface FleetArgs</a>
* <a href="#FleetState">interface FleetState</a>
* <a href="#GameSessionQueueArgs">interface GameSessionQueueArgs</a>
* <a href="#GameSessionQueueState">interface GameSessionQueueState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts">gamelift/alias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts">gamelift/build.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts">gamelift/fleet.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts">gamelift/gameSessionQueue.ts</a> 


<h2 class="pdoc-module-header" id="Alias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L10">class Alias</a>
</h2>

Provides a Gamelift Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L38">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L30">property description</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L38">property routingStrategy</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L10">class Build</a>
</h2>

Provides an Gamelift Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L38">constructor</a>
</h3>

```typescript
new Build(name: string, args: BuildArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Build resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L26">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L30">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L34">property storageLocation</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L38">property version</a>
</h3>

```typescript
public version: pulumi.Output<string | undefined>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="Fleet">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L10">class Fleet</a>
</h2>

Provides a Gamelift Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L67">constructor</a>
</h3>

```typescript
new Fleet(name: string, args: FleetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Fleet resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L30">property buildId</a>
</h3>

```typescript
public buildId: pulumi.Output<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L38">property ec2InboundPermissions</a>
</h3>

```typescript
public ec2InboundPermissions: pulumi.Output<{ ... }[] | undefined>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L42">property ec2InstanceType</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L43">property logPaths</a>
</h3>

```typescript
public logPaths: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L47">property metricGroups</a>
</h3>

```typescript
public metricGroups: pulumi.Output<string[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L55">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
public newGameSessionProtectionPolicy: pulumi.Output<string | undefined>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L59">property operatingSystem</a>
</h3>

```typescript
public operatingSystem: pulumi.Output<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L63">property resourceCreationLimitPolicy</a>
</h3>

```typescript
public resourceCreationLimitPolicy: pulumi.Output<{ ... } | undefined>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L67">property runtimeConfiguration</a>
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

<h2 class="pdoc-module-header" id="GameSessionQueue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L10">class GameSessionQueue</a>
</h2>

Provides an Gamelift Game Session Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L42">constructor</a>
</h3>

```typescript
new GameSessionQueue(name: string, args?: GameSessionQueueArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GameSessionQueue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GameSessionQueueState): GameSessionQueue
```


Get an existing GameSessionQueue resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Game Session Queue ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L30">property destinations</a>
</h3>

```typescript
public destinations: pulumi.Output<string[] | undefined>;
```


List of fleet/alias ARNs used by session queue for placing game sessions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the session queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L38">property playerLatencyPolicies</a>
</h3>

```typescript
public playerLatencyPolicies: pulumi.Output<{ ... }[] | undefined>;
```


One or more policies used to choose fleet based on player latency. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L42">property timeoutInSeconds</a>
</h3>

```typescript
public timeoutInSeconds: pulumi.Output<number | undefined>;
```


Maximum time a game session request can remain in the queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L95">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L107">property routingStrategy</a>
</h3>

```typescript
routingStrategy: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L73">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L77">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Alias ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L81">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/alias.ts#L89">property routingStrategy</a>
</h3>

```typescript
routingStrategy?: pulumi.Input<{ ... }>;
```


Specifies the fleet and/or routing type to use for the alias.

<h2 class="pdoc-module-header" id="BuildArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L98">interface BuildArgs</a>
</h2>

The set of arguments for constructing a Build resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L102">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L106">property operatingSystem</a>
</h3>

```typescript
operatingSystem: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L110">property storageLocation</a>
</h3>

```typescript
storageLocation: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L114">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="BuildState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L76">interface BuildState</a>
</h2>

Input properties used for looking up and filtering Build resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L80">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the build

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L84">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system that the game server binaries are built to run on. e.g. `WINDOWS_2012` or `AMAZON_LINUX`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L88">property storageLocation</a>
</h3>

```typescript
storageLocation?: pulumi.Input<{ ... }>;
```


Information indicating where your game build files are stored. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/build.ts#L92">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Version that is associated with this build.

<h2 class="pdoc-module-header" id="FleetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L172">interface FleetArgs</a>
</h2>

The set of arguments for constructing a Fleet resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L176">property buildId</a>
</h3>

```typescript
buildId: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L180">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L184">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L188">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L192">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L196">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L200">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L204">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L208">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="FleetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L121">interface FleetState</a>
</h2>

Input properties used for looking up and filtering Fleet resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L125">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Fleet ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L129">property buildId</a>
</h3>

```typescript
buildId?: pulumi.Input<string>;
```


ID of the Gamelift Build to be deployed on the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Human-readable description of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L137">property ec2InboundPermissions</a>
</h3>

```typescript
ec2InboundPermissions?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L141">property ec2InstanceType</a>
</h3>

```typescript
ec2InstanceType?: pulumi.Input<string>;
```


Name of an EC2 instance type. e.g. `t2.micro`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L142">property logPaths</a>
</h3>

```typescript
logPaths?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L146">property metricGroups</a>
</h3>

```typescript
metricGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the fleet.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L154">property newGameSessionProtectionPolicy</a>
</h3>

```typescript
newGameSessionProtectionPolicy?: pulumi.Input<string>;
```


Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L158">property operatingSystem</a>
</h3>

```typescript
operatingSystem?: pulumi.Input<string>;
```


Operating system of the fleet's computing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L162">property resourceCreationLimitPolicy</a>
</h3>

```typescript
resourceCreationLimitPolicy?: pulumi.Input<{ ... }>;
```


Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/fleet.ts#L166">property runtimeConfiguration</a>
</h3>

```typescript
runtimeConfiguration?: pulumi.Input<{ ... }>;
```


Instructions for launching server processes on each instance in the fleet. See below.

<h2 class="pdoc-module-header" id="GameSessionQueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L102">interface GameSessionQueueArgs</a>
</h2>

The set of arguments for constructing a GameSessionQueue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L106">property destinations</a>
</h3>

```typescript
destinations?: pulumi.Input<pulumi.Input<string>[]>;
```


List of fleet/alias ARNs used by session queue for placing game sessions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the session queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L114">property playerLatencyPolicies</a>
</h3>

```typescript
playerLatencyPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more policies used to choose fleet based on player latency. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L118">property timeoutInSeconds</a>
</h3>

```typescript
timeoutInSeconds?: pulumi.Input<number>;
```


Maximum time a game session request can remain in the queue.

<h2 class="pdoc-module-header" id="GameSessionQueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L76">interface GameSessionQueueState</a>
</h2>

Input properties used for looking up and filtering GameSessionQueue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L80">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Game Session Queue ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L84">property destinations</a>
</h3>

```typescript
destinations?: pulumi.Input<pulumi.Input<string>[]>;
```


List of fleet/alias ARNs used by session queue for placing game sessions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the session queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L92">property playerLatencyPolicies</a>
</h3>

```typescript
playerLatencyPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more policies used to choose fleet based on player latency. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/gamelift/gameSessionQueue.ts#L96">property timeoutInSeconds</a>
</h3>

```typescript
timeoutInSeconds?: pulumi.Input<number>;
```


Maximum time a game session request can remain in the queue.

