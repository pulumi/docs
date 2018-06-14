---
title: Module eventhub
---

<a href="../index.html">@pulumi/azure</a> &gt; eventhub

<h2 class="pdoc-module-header">Index</h2>

* <a href="#EventGridTopic">class EventGridTopic</a>
* <a href="#EventHub">class EventHub</a>
* <a href="#EventHubAuthorizationRule">class EventHubAuthorizationRule</a>
* <a href="#EventHubConsumerGroup">class EventHubConsumerGroup</a>
* <a href="#EventHubNamespace">class EventHubNamespace</a>
* <a href="#Namespace">class Namespace</a>
* <a href="#Queue">class Queue</a>
* <a href="#Subscription">class Subscription</a>
* <a href="#SubscriptionRule">class SubscriptionRule</a>
* <a href="#Topic">class Topic</a>
* <a href="#TopicAuthorizationRule">class TopicAuthorizationRule</a>
* <a href="#getEventhubNamespace">function getEventhubNamespace</a>
* <a href="#EventGridTopicArgs">interface EventGridTopicArgs</a>
* <a href="#EventGridTopicState">interface EventGridTopicState</a>
* <a href="#EventHubArgs">interface EventHubArgs</a>
* <a href="#EventHubAuthorizationRuleArgs">interface EventHubAuthorizationRuleArgs</a>
* <a href="#EventHubAuthorizationRuleState">interface EventHubAuthorizationRuleState</a>
* <a href="#EventHubConsumerGroupArgs">interface EventHubConsumerGroupArgs</a>
* <a href="#EventHubConsumerGroupState">interface EventHubConsumerGroupState</a>
* <a href="#EventHubNamespaceArgs">interface EventHubNamespaceArgs</a>
* <a href="#EventHubNamespaceState">interface EventHubNamespaceState</a>
* <a href="#EventHubState">interface EventHubState</a>
* <a href="#GetEventhubNamespaceArgs">interface GetEventhubNamespaceArgs</a>
* <a href="#GetEventhubNamespaceResult">interface GetEventhubNamespaceResult</a>
* <a href="#NamespaceArgs">interface NamespaceArgs</a>
* <a href="#NamespaceState">interface NamespaceState</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#SubscriptionArgs">interface SubscriptionArgs</a>
* <a href="#SubscriptionRuleArgs">interface SubscriptionRuleArgs</a>
* <a href="#SubscriptionRuleState">interface SubscriptionRuleState</a>
* <a href="#SubscriptionState">interface SubscriptionState</a>
* <a href="#TopicArgs">interface TopicArgs</a>
* <a href="#TopicAuthorizationRuleArgs">interface TopicAuthorizationRuleArgs</a>
* <a href="#TopicAuthorizationRuleState">interface TopicAuthorizationRuleState</a>
* <a href="#TopicState">interface TopicState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts">eventhub/eventGridTopic.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts">eventhub/eventHub.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts">eventhub/eventHubAuthorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts">eventhub/eventHubConsumerGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts">eventhub/eventHubNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts">eventhub/getEventhubNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts">eventhub/namespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts">eventhub/queue.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts">eventhub/subscription.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts">eventhub/subscriptionRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts">eventhub/topic.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts">eventhub/topicAuthorizationRule.ts</a> 


<h2 class="pdoc-module-header" id="EventGridTopic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L11">class EventGridTopic</a>
</h2>

Manages an EventGrid Topic

~> **Note:** at this time EventGrid Topic's are only available in a limited number of regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L51">constructor</a>
</h3>

```typescript
new EventGridTopic(name: string, args: EventGridTopicArgs, opts?: pulumi.ResourceOptions)
```


Create a EventGridTopic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventGridTopicState): EventGridTopic
```


Get an existing EventGridTopic resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L27">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The Endpoint associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L31">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L39">property primaryAccessKey</a>
</h3>

```typescript
public primaryAccessKey: pulumi.Output<string>;
```


The Primary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L43">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L47">property secondaryAccessKey</a>
</h3>

```typescript
public secondaryAccessKey: pulumi.Output<string>;
```


The Secondary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L51">property tags</a>
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

<h2 class="pdoc-module-header" id="EventHub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L9">class EventHub</a>
</h2>

Manages a new Event Hubs as a nested resource within a Event Hubs namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L50">constructor</a>
</h3>

```typescript
new EventHub(name: string, args: EventHubArgs, opts?: pulumi.ResourceOptions)
```


Create a EventHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubState): EventHub
```


Get an existing EventHub resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L25">property captureDescription</a>
</h3>

```typescript
public captureDescription: pulumi.Output<{ ... } | undefined>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L30">property messageRetention</a>
</h3>

```typescript
public messageRetention: pulumi.Output<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The Name of the Destination where the capture should take place. At this time the only supported value is `EventHubArchive.AzureBlockBlob`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L38">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L42">property partitionCount</a>
</h3>

```typescript
public partitionCount: pulumi.Output<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L46">property partitionIds</a>
</h3>

```typescript
public partitionIds: pulumi.Output<string[]>;
```


The identifiers for partitions created for Event Hubs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventHubAuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L9">class EventHubAuthorizationRule</a>
</h2>

Manages a new Event Hubs authorization Rule within an Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L66">constructor</a>
</h3>

```typescript
new EventHubAuthorizationRule(name: string, args: EventHubAuthorizationRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a EventHubAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubAuthorizationRuleState): EventHubAuthorizationRule
```


Get an existing EventHubAuthorizationRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L25">property eventhubName</a>
</h3>

```typescript
public eventhubName: pulumi.Output<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L29">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L34">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L42">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L46">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L50">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L58">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L62">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L66">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventHubConsumerGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L9">class EventHubConsumerGroup</a>
</h2>

Manages a new Event Hubs Consumer Group as a nested resource within an Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L42">constructor</a>
</h3>

```typescript
new EventHubConsumerGroup(name: string, args: EventHubConsumerGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a EventHubConsumerGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubConsumerGroupState): EventHubConsumerGroup
```


Get an existing EventHubConsumerGroup resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L25">property eventhubName</a>
</h3>

```typescript
public eventhubName: pulumi.Output<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L34">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L42">property userMetadata</a>
</h3>

```typescript
public userMetadata: pulumi.Output<string | undefined>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L9">class EventHubNamespace</a>
</h2>

Create an EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L71">constructor</a>
</h3>

```typescript
new EventHubNamespace(name: string, args: EventHubNamespaceArgs, opts?: pulumi.ResourceOptions)
```


Create a EventHubNamespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubNamespaceState): EventHubNamespace
```


Get an existing EventHubNamespace resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L25">property autoInflateEnabled</a>
</h3>

```typescript
public autoInflateEnabled: pulumi.Output<boolean | undefined>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L29">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number | undefined>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L34">property defaultPrimaryConnectionString</a>
</h3>

```typescript
public defaultPrimaryConnectionString: pulumi.Output<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L38">property defaultPrimaryKey</a>
</h3>

```typescript
public defaultPrimaryKey: pulumi.Output<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L43">property defaultSecondaryConnectionString</a>
</h3>

```typescript
public defaultSecondaryConnectionString: pulumi.Output<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L47">property defaultSecondaryKey</a>
</h3>

```typescript
public defaultSecondaryKey: pulumi.Output<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L51">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L55">property maximumThroughputUnits</a>
</h3>

```typescript
public maximumThroughputUnits: pulumi.Output<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L59">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L63">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L67">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L71">property tags</a>
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

<h2 class="pdoc-module-header" id="Namespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L9">class Namespace</a>
</h2>

Create a ServiceBus Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L65">constructor</a>
</h3>

```typescript
new Namespace(name: string, args: NamespaceArgs, opts?: pulumi.ResourceOptions)
```


Create a Namespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceState): Namespace
```


Get an existing Namespace resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L25">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number | undefined>;
```


Specifies the capacity of a Premium namespace. Can be 1, 2 or 4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L30">property defaultPrimaryConnectionString</a>
</h3>

```typescript
public defaultPrimaryConnectionString: pulumi.Output<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L34">property defaultPrimaryKey</a>
</h3>

```typescript
public defaultPrimaryKey: pulumi.Output<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L39">property defaultSecondaryConnectionString</a>
</h3>

```typescript
public defaultSecondaryConnectionString: pulumi.Output<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L43">property defaultSecondaryKey</a>
</h3>

```typescript
public defaultSecondaryKey: pulumi.Output<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L47">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L57">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L61">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L65">property tags</a>
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

<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L9">class Queue</a>
</h2>

Create and manage a ServiceBus Queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L95">constructor</a>
</h3>

```typescript
new Queue(name: string, args: QueueArgs, opts?: pulumi.ResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L27">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The idle interval after which the
Queue is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L28">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
public deadLetteringOnMessageExpiration: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L34">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The TTL of messages sent to this queue. This is the default value
used when TTL is not set on message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L39">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
public duplicateDetectionHistoryTimeWindow: pulumi.Output<string>;
```


The duration during which
duplicates can be detected. Default value is 10 minutes. Provided in the [TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L40">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L47">property enableExpress</a>
</h3>

```typescript
public enableExpress: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L54">property enablePartitioning</a>
</h3>

```typescript
public enablePartitioning: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L59">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L63">property lockDuration</a>
</h3>

```typescript
public lockDuration: pulumi.Output<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L69">property maxSizeInMegabytes</a>
</h3>

```typescript
public maxSizeInMegabytes: pulumi.Output<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L79">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L85">property requiresDuplicateDetection</a>
</h3>

```typescript
public requiresDuplicateDetection: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L89">property requiresSession</a>
</h3>

```typescript
public requiresSession: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L94">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L95">property supportOrdering</a>
</h3>

```typescript
public supportOrdering: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Subscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L9">class Subscription</a>
</h2>

Create a ServiceBus Subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L90">constructor</a>
</h3>

```typescript
new Subscription(name: string, args: SubscriptionArgs, opts?: pulumi.ResourceOptions)
```


Create a Subscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionState): Subscription
```


Get an existing Subscription resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L27">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
[TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L28">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
public deadLetteringOnFilterEvaluationExceptions: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L34">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
public deadLetteringOnMessageExpiration: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L40">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L45">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L50">property forwardTo</a>
</h3>

```typescript
public forwardTo: pulumi.Output<string | undefined>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L55">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L60">property lockDuration</a>
</h3>

```typescript
public lockDuration: pulumi.Output<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L64">property maxDeliveryCount</a>
</h3>

```typescript
public maxDeliveryCount: pulumi.Output<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L69">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L74">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L80">property requiresSession</a>
</h3>

```typescript
public requiresSession: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L85">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L90">property topicName</a>
</h3>

```typescript
public topicName: pulumi.Output<string>;
```


The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L9">class SubscriptionRule</a>
</h2>

Create a ServiceBus Subscription Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L57">constructor</a>
</h3>

```typescript
new SubscriptionRule(name: string, args: SubscriptionRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a SubscriptionRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionRuleState): SubscriptionRule
```


Get an existing SubscriptionRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L25">property action</a>
</h3>

```typescript
public action: pulumi.Output<string | undefined>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L29">property correlationFilter</a>
</h3>

```typescript
public correlationFilter: pulumi.Output<{ ... } | undefined>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L33">property filterType</a>
</h3>

```typescript
public filterType: pulumi.Output<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L41">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L49">property sqlFilter</a>
</h3>

```typescript
public sqlFilter: pulumi.Output<string | undefined>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L53">property subscriptionName</a>
</h3>

```typescript
public subscriptionName: pulumi.Output<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L57">property topicName</a>
</h3>

```typescript
public topicName: pulumi.Output<string>;
```


The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L11">class Topic</a>
</h2>

Create a ServiceBus Topic.

**Note** Topics can only be created in Namespaces with an SKU of `standard` or higher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L99">constructor</a>
</h3>

```typescript
new Topic(name: string, args: TopicArgs, opts?: pulumi.ResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicState): Topic
```


Get an existing Topic resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L29">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The idle interval after which the
Topic is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L35">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The TTL of messages sent to this topic if no
TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L40">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
public duplicateDetectionHistoryTimeWindow: pulumi.Output<string>;
```


The duration during which
duplicates can be detected. Provided in the [TimeSpan](#timespan-format) format. Defaults to 10 minutes (`00:10:00`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L45">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L51">property enableExpress</a>
</h3>

```typescript
public enableExpress: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L52">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
public enableFilteringMessagesBeforePublishing: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L58">property enablePartitioning</a>
</h3>

```typescript
public enablePartitioning: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L63">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L69">property maxSizeInMegabytes</a>
</h3>

```typescript
public maxSizeInMegabytes: pulumi.Output<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L79">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L85">property requiresDuplicateDetection</a>
</h3>

```typescript
public requiresDuplicateDetection: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L90">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L94">property status</a>
</h3>

```typescript
public status: pulumi.Output<string | undefined>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L99">property supportOrdering</a>
</h3>

```typescript
public supportOrdering: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicAuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L9">class TopicAuthorizationRule</a>
</h2>

Manages a new ServiceBus Topic authorization Rule within a ServiceBus Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L65">constructor</a>
</h3>

```typescript
new TopicAuthorizationRule(name: string, args: TopicAuthorizationRuleArgs, opts?: pulumi.ResourceOptions)
```


Create a TopicAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicAuthorizationRuleState): TopicAuthorizationRule
```


Get an existing TopicAuthorizationRule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L25">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Listen to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L29">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Manage to the ServiceBus Topic? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the erviceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L37">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L41">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L45">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L49">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L53">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L57">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L61">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Send to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L65">property topicName</a>
</h3>

```typescript
public topicName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getEventhubNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L9">function getEventhubNamespace</a>
</h2>

```typescript
getEventhubNamespace(args: GetEventhubNamespaceArgs): Promise<GetEventhubNamespaceResult>
```


Use this data source to obtain information about an EventHub Namespace.

<h2 class="pdoc-module-header" id="EventGridTopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L129">interface EventGridTopicArgs</a>
</h2>

The set of arguments for constructing a EventGridTopic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L133">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L141">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L145">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventGridTopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L95">interface EventGridTopicState</a>
</h2>

Input properties used for looking up and filtering EventGridTopic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L99">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The Endpoint associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L103">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L111">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey?: pulumi.Input<string>;
```


The Primary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L115">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L119">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey?: pulumi.Input<string>;
```


The Secondary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L137">interface EventHubArgs</a>
</h2>

The set of arguments for constructing a EventHub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L141">property captureDescription</a>
</h3>

```typescript
captureDescription?: pulumi.Input<{ ... }>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L142">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L146">property messageRetention</a>
</h3>

```typescript
messageRetention: pulumi.Input<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Destination where the capture should take place. At this time the only supported value is `EventHubArchive.AzureBlockBlob`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L154">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L158">property partitionCount</a>
</h3>

```typescript
partitionCount: pulumi.Input<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L162">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="EventHubAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L174">interface EventHubAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a EventHubAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L178">property eventhubName</a>
</h3>

```typescript
eventhubName: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L182">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L183">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L187">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L195">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L199">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L203">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L123">interface EventHubAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering EventHubAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L127">property eventhubName</a>
</h3>

```typescript
eventhubName?: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L131">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L132">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L136">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L144">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L148">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L152">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L156">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L160">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L164">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L168">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubConsumerGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L114">interface EventHubConsumerGroupArgs</a>
</h2>

The set of arguments for constructing a EventHubConsumerGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L118">property eventhubName</a>
</h3>

```typescript
eventhubName: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L119">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L123">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L127">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L135">property userMetadata</a>
</h3>

```typescript
userMetadata?: pulumi.Input<string>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubConsumerGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L87">interface EventHubConsumerGroupState</a>
</h2>

Input properties used for looking up and filtering EventHubConsumerGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L91">property eventhubName</a>
</h3>

```typescript
eventhubName?: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L92">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L96">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L100">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L108">property userMetadata</a>
</h3>

```typescript
userMetadata?: pulumi.Input<string>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L184">interface EventHubNamespaceArgs</a>
</h2>

The set of arguments for constructing a EventHubNamespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L188">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled?: pulumi.Input<boolean>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L192">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L196">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L200">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits?: pulumi.Input<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L204">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L208">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L212">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L216">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubNamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L128">interface EventHubNamespaceState</a>
</h2>

Input properties used for looking up and filtering EventHubNamespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L132">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled?: pulumi.Input<boolean>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L136">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L141">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString?: pulumi.Input<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L145">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey?: pulumi.Input<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L150">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString?: pulumi.Input<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L154">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey?: pulumi.Input<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L158">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L162">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits?: pulumi.Input<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L166">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L170">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L174">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L102">interface EventHubState</a>
</h2>

Input properties used for looking up and filtering EventHub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L106">property captureDescription</a>
</h3>

```typescript
captureDescription?: pulumi.Input<{ ... }>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L107">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L111">property messageRetention</a>
</h3>

```typescript
messageRetention?: pulumi.Input<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The Name of the Destination where the capture should take place. At this time the only supported value is `EventHubArchive.AzureBlockBlob`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L119">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L123">property partitionCount</a>
</h3>

```typescript
partitionCount?: pulumi.Input<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L127">property partitionIds</a>
</h3>

```typescript
partitionIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The identifiers for partitions created for Event Hubs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetEventhubNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L19">interface GetEventhubNamespaceArgs</a>
</h2>

A collection of arguments for invoking getEventhubNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The Name of the Resource Group where the EventHub Namespace exists.

<h2 class="pdoc-module-header" id="GetEventhubNamespaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L33">interface GetEventhubNamespaceResult</a>
</h2>

A collection of values returned by getEventhubNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L37">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled: boolean;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L41">property capacity</a>
</h3>

```typescript
capacity: number;
```


The Capacity / Throughput Units for a `Standard` SKU namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L46">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString: string;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L50">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey: string;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L55">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString: string;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L59">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey: string;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L63">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the EventHub Namespace exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L67">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits: number;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L71">property sku</a>
</h3>

```typescript
sku: string;
```


Defines which tier to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L75">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the EventHub Namespace.

<h2 class="pdoc-module-header" id="NamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L168">interface NamespaceArgs</a>
</h2>

The set of arguments for constructing a Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L172">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the capacity of a Premium namespace. Can be 1, 2 or 4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L176">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L181">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L186">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L190">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L194">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L118">interface NamespaceState</a>
</h2>

Input properties used for looking up and filtering Namespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L122">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the capacity of a Premium namespace. Can be 1, 2 or 4.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L127">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString?: pulumi.Input<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L131">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey?: pulumi.Input<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L136">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString?: pulumi.Input<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L140">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey?: pulumi.Input<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L144">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L154">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L158">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L162">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L237">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L243">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Queue is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L244">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L250">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this queue. This is the default value
used when TTL is not set on message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L255">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The duration during which
duplicates can be detected. Default value is 10 minutes. Provided in the [TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L256">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L263">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L270">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L275">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L279">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L285">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L290">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L295">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L301">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L305">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L310">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L311">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L157">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L163">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Queue is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L164">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L170">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this queue. This is the default value
used when TTL is not set on message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L175">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The duration during which
duplicates can be detected. Default value is 10 minutes. Provided in the [TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L176">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L183">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L190">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L195">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L199">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L205">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L210">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L215">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L221">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L225">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L230">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L231">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="SubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L229">interface SubscriptionArgs</a>
</h2>

The set of arguments for constructing a Subscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L235">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
[TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L236">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
deadLetteringOnFilterEvaluationExceptions?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L242">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L248">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L253">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L258">property forwardTo</a>
</h3>

```typescript
forwardTo?: pulumi.Input<string>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L263">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L268">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L272">property maxDeliveryCount</a>
</h3>

```typescript
maxDeliveryCount: pulumi.Input<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L277">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L282">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L288">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L293">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L298">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L156">interface SubscriptionRuleArgs</a>
</h2>

The set of arguments for constructing a SubscriptionRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L160">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L164">property correlationFilter</a>
</h3>

```typescript
correlationFilter?: pulumi.Input<{ ... }>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L168">property filterType</a>
</h3>

```typescript
filterType: pulumi.Input<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L172">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L176">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L180">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L184">property sqlFilter</a>
</h3>

```typescript
sqlFilter?: pulumi.Input<string>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L188">property subscriptionName</a>
</h3>

```typescript
subscriptionName: pulumi.Input<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L192">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L114">interface SubscriptionRuleState</a>
</h2>

Input properties used for looking up and filtering SubscriptionRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L118">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L122">property correlationFilter</a>
</h3>

```typescript
correlationFilter?: pulumi.Input<{ ... }>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L126">property filterType</a>
</h3>

```typescript
filterType?: pulumi.Input<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L134">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L138">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L142">property sqlFilter</a>
</h3>

```typescript
sqlFilter?: pulumi.Input<string>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L146">property subscriptionName</a>
</h3>

```typescript
subscriptionName?: pulumi.Input<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L150">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L154">interface SubscriptionState</a>
</h2>

Input properties used for looking up and filtering Subscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L160">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
[TimeSpan](#timespan-format) format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L161">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
deadLetteringOnFilterEvaluationExceptions?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L167">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L173">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L178">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L183">property forwardTo</a>
</h3>

```typescript
forwardTo?: pulumi.Input<string>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L188">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L193">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L197">property maxDeliveryCount</a>
</h3>

```typescript
maxDeliveryCount?: pulumi.Input<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L207">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L213">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L218">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L223">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L241">interface TopicArgs</a>
</h2>

The set of arguments for constructing a Topic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L247">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Topic is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L253">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this topic if no
TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L258">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The duration during which
duplicates can be detected. Provided in the [TimeSpan](#timespan-format) format. Defaults to 10 minutes (`00:10:00`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L263">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L269">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L270">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
enableFilteringMessagesBeforePublishing?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L276">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L281">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L287">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L292">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L297">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L303">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L308">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L312">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L317">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

<h2 class="pdoc-module-header" id="TopicAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L170">interface TopicAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a TopicAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L174">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L178">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the ServiceBus Topic? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the erviceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L186">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L190">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L194">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L198">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L120">interface TopicAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering TopicAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L124">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L128">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the ServiceBus Topic? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L132">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the erviceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L136">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L140">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L144">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L148">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L152">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L156">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L160">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the ServiceBus Topic? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L164">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L159">interface TopicState</a>
</h2>

Input properties used for looking up and filtering Topic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L165">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Topic is automatically deleted, minimum of 5 minutes. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L171">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this topic if no
TTL value is set on the message itself. Provided in the [TimeSpan](#timespan-format)
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L176">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The duration during which
duplicates can be detected. Provided in the [TimeSpan](#timespan-format) format. Defaults to 10 minutes (`00:10:00`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L181">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L187">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L188">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
enableFilteringMessagesBeforePublishing?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L194">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L199">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L205">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L210">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L215">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L221">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L226">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L230">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L235">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

