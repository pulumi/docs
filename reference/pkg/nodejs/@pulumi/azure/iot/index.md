---
title: Module iot
---

<a href="../index.html">@pulumi/azure</a> &gt; iot

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ConsumerGroup">class ConsumerGroup</a>
* <a href="#IoTHub">class IoTHub</a>
* <a href="#ConsumerGroupArgs">interface ConsumerGroupArgs</a>
* <a href="#ConsumerGroupState">interface ConsumerGroupState</a>
* <a href="#IoTHubArgs">interface IoTHubArgs</a>
* <a href="#IoTHubState">interface IoTHubState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts">iot/consumerGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts">iot/ioTHub.ts</a> 


<h2 class="pdoc-module-header" id="ConsumerGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L10">class ConsumerGroup</a>
</h2>

Manages a Consumer Group within an IotHub

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L38">constructor</a>
</h3>

```typescript
new ConsumerGroup(name: string, args: ConsumerGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ConsumerGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConsumerGroupState): ConsumerGroup
```


Get an existing ConsumerGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L26">property eventhubEndpointName</a>
</h3>

```typescript
public eventhubEndpointName: pulumi.Output<string>;
```


The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L30">property iothubName</a>
</h3>

```typescript
public iothubName: pulumi.Output<string>;
```


The name of the IoT Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of this Consumer Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IoTHub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L10">class IoTHub</a>
</h2>

Manages an IotHub

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L75">constructor</a>
</h3>

```typescript
new IoTHub(name: string, args: IoTHubArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IoTHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IoTHubState): IoTHub
```


Get an existing IoTHub resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L26">property endpoints</a>
</h3>

```typescript
public endpoints: pulumi.Output<{ ... }[] | undefined>;
```


An `endpoint` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L30">property eventHubEventsEndpoint</a>
</h3>

```typescript
public eventHubEventsEndpoint: pulumi.Output<string>;
```


The EventHub compatible endpoint for events data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L34">property eventHubEventsPath</a>
</h3>

```typescript
public eventHubEventsPath: pulumi.Output<string>;
```


The EventHub compatible path for events data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L38">property eventHubOperationsEndpoint</a>
</h3>

```typescript
public eventHubOperationsEndpoint: pulumi.Output<string>;
```


The EventHub compatible endpoint for operational data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L42">property eventHubOperationsPath</a>
</h3>

```typescript
public eventHubOperationsPath: pulumi.Output<string>;
```


The EventHub compatible path for operational data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L46">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L50">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L62">property routes</a>
</h3>

```typescript
public routes: pulumi.Output<{ ... }[] | undefined>;
```


A `route` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L66">property sharedAccessPolicies</a>
</h3>

```typescript
public sharedAccessPolicies: pulumi.Output<{ ... }[]>;
```


One or more `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L70">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L74">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L75">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConsumerGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L101">interface ConsumerGroupArgs</a>
</h2>

The set of arguments for constructing a ConsumerGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L105">property eventhubEndpointName</a>
</h3>

```typescript
eventhubEndpointName: pulumi.Input<string>;
```


The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L109">property iothubName</a>
</h3>

```typescript
iothubName: pulumi.Input<string>;
```


The name of the IoT Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of this Consumer Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L117">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="ConsumerGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L79">interface ConsumerGroupState</a>
</h2>

Input properties used for looking up and filtering ConsumerGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L83">property eventhubEndpointName</a>
</h3>

```typescript
eventhubEndpointName?: pulumi.Input<string>;
```


The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L87">property iothubName</a>
</h3>

```typescript
iothubName?: pulumi.Input<string>;
```


The name of the IoT Hub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of this Consumer Group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/consumerGroup.ts#L95">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="IoTHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L195">interface IoTHubArgs</a>
</h2>

The set of arguments for constructing a IoTHub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L199">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `endpoint` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L203">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L207">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L211">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L215">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `route` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L219">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L223">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="IoTHubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L136">interface IoTHubState</a>
</h2>

Input properties used for looking up and filtering IoTHub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L140">property endpoints</a>
</h3>

```typescript
endpoints?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An `endpoint` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L144">property eventHubEventsEndpoint</a>
</h3>

```typescript
eventHubEventsEndpoint?: pulumi.Input<string>;
```


The EventHub compatible endpoint for events data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L148">property eventHubEventsPath</a>
</h3>

```typescript
eventHubEventsPath?: pulumi.Input<string>;
```


The EventHub compatible path for events data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L152">property eventHubOperationsEndpoint</a>
</h3>

```typescript
eventHubOperationsEndpoint?: pulumi.Input<string>;
```


The EventHub compatible endpoint for operational data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L156">property eventHubOperationsPath</a>
</h3>

```typescript
eventHubOperationsPath?: pulumi.Input<string>;
```


The EventHub compatible path for operational data

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L160">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L164">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L168">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L172">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L176">property routes</a>
</h3>

```typescript
routes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


A `route` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L180">property sharedAccessPolicies</a>
</h3>

```typescript
sharedAccessPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L184">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L188">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L189">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

