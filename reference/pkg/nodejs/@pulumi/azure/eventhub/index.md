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
* <a href="#EventHubNamespaceAuthorizationRule">class EventHubNamespaceAuthorizationRule</a>
* <a href="#Namespace">class Namespace</a>
* <a href="#NamespaceAuthorizationRule">class NamespaceAuthorizationRule</a>
* <a href="#Queue">class Queue</a>
* <a href="#QueueAuthorizationRule">class QueueAuthorizationRule</a>
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
* <a href="#EventHubNamespaceAuthorizationRuleArgs">interface EventHubNamespaceAuthorizationRuleArgs</a>
* <a href="#EventHubNamespaceAuthorizationRuleState">interface EventHubNamespaceAuthorizationRuleState</a>
* <a href="#EventHubNamespaceState">interface EventHubNamespaceState</a>
* <a href="#EventHubState">interface EventHubState</a>
* <a href="#GetEventhubNamespaceArgs">interface GetEventhubNamespaceArgs</a>
* <a href="#GetEventhubNamespaceResult">interface GetEventhubNamespaceResult</a>
* <a href="#NamespaceArgs">interface NamespaceArgs</a>
* <a href="#NamespaceAuthorizationRuleArgs">interface NamespaceAuthorizationRuleArgs</a>
* <a href="#NamespaceAuthorizationRuleState">interface NamespaceAuthorizationRuleState</a>
* <a href="#NamespaceState">interface NamespaceState</a>
* <a href="#QueueArgs">interface QueueArgs</a>
* <a href="#QueueAuthorizationRuleArgs">interface QueueAuthorizationRuleArgs</a>
* <a href="#QueueAuthorizationRuleState">interface QueueAuthorizationRuleState</a>
* <a href="#QueueState">interface QueueState</a>
* <a href="#SubscriptionArgs">interface SubscriptionArgs</a>
* <a href="#SubscriptionRuleArgs">interface SubscriptionRuleArgs</a>
* <a href="#SubscriptionRuleState">interface SubscriptionRuleState</a>
* <a href="#SubscriptionState">interface SubscriptionState</a>
* <a href="#TopicArgs">interface TopicArgs</a>
* <a href="#TopicAuthorizationRuleArgs">interface TopicAuthorizationRuleArgs</a>
* <a href="#TopicAuthorizationRuleState">interface TopicAuthorizationRuleState</a>
* <a href="#TopicState">interface TopicState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts">eventhub/eventGridTopic.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts">eventhub/eventHub.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts">eventhub/eventHubAuthorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts">eventhub/eventHubConsumerGroup.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts">eventhub/eventHubNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts">eventhub/eventHubNamespaceAuthorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts">eventhub/getEventhubNamespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts">eventhub/namespace.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts">eventhub/namespaceAuthorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts">eventhub/queue.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts">eventhub/queueAuthorizationRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts">eventhub/subscription.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts">eventhub/subscriptionRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts">eventhub/topic.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts">eventhub/topicAuthorizationRule.ts</a> 


<h2 class="pdoc-module-header" id="EventGridTopic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L12">class EventGridTopic</a>
</h2>

Manages an EventGrid Topic

~> **Note:** at this time EventGrid Topic's are only available in a limited number of regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L52">constructor</a>
</h3>

```typescript
new EventGridTopic(name: string, args: EventGridTopicArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventGridTopic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventGridTopicState): EventGridTopic
```


Get an existing EventGridTopic resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L28">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The Endpoint associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L32">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L40">property primaryAccessKey</a>
</h3>

```typescript
public primaryAccessKey: pulumi.Output<string>;
```


The Primary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L44">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L48">property secondaryAccessKey</a>
</h3>

```typescript
public secondaryAccessKey: pulumi.Output<string>;
```


The Secondary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L52">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L10">class EventHub</a>
</h2>

Manages a Event Hubs as a nested resource within a Event Hubs namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L51">constructor</a>
</h3>

```typescript
new EventHub(name: string, args: EventHubArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubState): EventHub
```


Get an existing EventHub resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L26">property captureDescription</a>
</h3>

```typescript
public captureDescription: pulumi.Output<{ ... } | undefined>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L27">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L31">property messageRetention</a>
</h3>

```typescript
public messageRetention: pulumi.Output<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L39">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L43">property partitionCount</a>
</h3>

```typescript
public partitionCount: pulumi.Output<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L47">property partitionIds</a>
</h3>

```typescript
public partitionIds: pulumi.Output<string[]>;
```


The identifiers for partitions created for Event Hubs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L51">property resourceGroupName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L10">class EventHubAuthorizationRule</a>
</h2>

Manages a Event Hubs authorization Rule within an Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L67">constructor</a>
</h3>

```typescript
new EventHubAuthorizationRule(name: string, args: EventHubAuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventHubAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubAuthorizationRuleState): EventHubAuthorizationRule
```


Get an existing EventHubAuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L26">property eventhubName</a>
</h3>

```typescript
public eventhubName: pulumi.Output<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L30">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L31">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L35">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L43">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L47">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L51">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L55">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L59">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L63">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L67">property send</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L10">class EventHubConsumerGroup</a>
</h2>

Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L43">constructor</a>
</h3>

```typescript
new EventHubConsumerGroup(name: string, args: EventHubConsumerGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventHubConsumerGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubConsumerGroupState): EventHubConsumerGroup
```


Get an existing EventHubConsumerGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L26">property eventhubName</a>
</h3>

```typescript
public eventhubName: pulumi.Output<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L27">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L35">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L39">property resourceGroupName</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L43">property userMetadata</a>
</h3>

```typescript
public userMetadata: pulumi.Output<string | undefined>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubNamespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L10">class EventHubNamespace</a>
</h2>

Manage an EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L72">constructor</a>
</h3>

```typescript
new EventHubNamespace(name: string, args: EventHubNamespaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventHubNamespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubNamespaceState): EventHubNamespace
```


Get an existing EventHubNamespace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L26">property autoInflateEnabled</a>
</h3>

```typescript
public autoInflateEnabled: pulumi.Output<boolean | undefined>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L30">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number | undefined>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L35">property defaultPrimaryConnectionString</a>
</h3>

```typescript
public defaultPrimaryConnectionString: pulumi.Output<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L39">property defaultPrimaryKey</a>
</h3>

```typescript
public defaultPrimaryKey: pulumi.Output<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L44">property defaultSecondaryConnectionString</a>
</h3>

```typescript
public defaultSecondaryConnectionString: pulumi.Output<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L48">property defaultSecondaryKey</a>
</h3>

```typescript
public defaultSecondaryKey: pulumi.Output<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L52">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L56">property maximumThroughputUnits</a>
</h3>

```typescript
public maximumThroughputUnits: pulumi.Output<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L60">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L64">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L68">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L72">property tags</a>
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

<h2 class="pdoc-module-header" id="EventHubNamespaceAuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L10">class EventHubNamespaceAuthorizationRule</a>
</h2>

Manages an Authorization Rule for an Event Hub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L63">constructor</a>
</h3>

```typescript
new EventHubNamespaceAuthorizationRule(name: string, args: EventHubNamespaceAuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventHubNamespaceAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventHubNamespaceAuthorizationRuleState): EventHubNamespaceAuthorizationRule
```


Get an existing EventHubNamespaceAuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L26">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L27">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L31">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L39">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L43">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L47">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L51">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L55">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L59">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L63">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Namespace">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L10">class Namespace</a>
</h2>

Manage a ServiceBus Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L66">constructor</a>
</h3>

```typescript
new Namespace(name: string, args: NamespaceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Namespace resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceState): Namespace
```


Get an existing Namespace resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L26">property capacity</a>
</h3>

```typescript
public capacity: pulumi.Output<number | undefined>;
```


Specifies the capacity, can only be set when `sku` is `Premium` namespace. Can be `1`, `2` or `4`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L31">property defaultPrimaryConnectionString</a>
</h3>

```typescript
public defaultPrimaryConnectionString: pulumi.Output<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L35">property defaultPrimaryKey</a>
</h3>

```typescript
public defaultPrimaryKey: pulumi.Output<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L40">property defaultSecondaryConnectionString</a>
</h3>

```typescript
public defaultSecondaryConnectionString: pulumi.Output<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L44">property defaultSecondaryKey</a>
</h3>

```typescript
public defaultSecondaryKey: pulumi.Output<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L48">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L62">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L66">property tags</a>
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

<h2 class="pdoc-module-header" id="NamespaceAuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L10">class NamespaceAuthorizationRule</a>
</h2>

Manages a ServiceBus Namespace authorization Rule within a ServiceBus.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L62">constructor</a>
</h3>

```typescript
new NamespaceAuthorizationRule(name: string, args: NamespaceAuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NamespaceAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NamespaceAuthorizationRuleState): NamespaceAuthorizationRule
```


Get an existing NamespaceAuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L26">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L30">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L38">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L42">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L46">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L54">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L58">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L62">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Queue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L10">class Queue</a>
</h2>

Manage and manage a ServiceBus Queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L100">constructor</a>
</h3>

```typescript
new Queue(name: string, args: QueueArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Queue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueState): Queue
```


Get an existing Queue resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L27">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L31">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
public deadLetteringOnMessageExpiration: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L36">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L41">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
public duplicateDetectionHistoryTimeWindow: pulumi.Output<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L42">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L49">property enableExpress</a>
</h3>

```typescript
public enableExpress: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L56">property enablePartitioning</a>
</h3>

```typescript
public enablePartitioning: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L61">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L65">property lockDuration</a>
</h3>

```typescript
public lockDuration: pulumi.Output<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L71">property maxSizeInMegabytes</a>
</h3>

```typescript
public maxSizeInMegabytes: pulumi.Output<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L76">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L81">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L87">property requiresDuplicateDetection</a>
</h3>

```typescript
public requiresDuplicateDetection: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L94">property requiresSession</a>
</h3>

```typescript
public requiresSession: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L99">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L100">property supportOrdering</a>
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

<h2 class="pdoc-module-header" id="QueueAuthorizationRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L10">class QueueAuthorizationRule</a>
</h2>

Manages an Authorization Rule for a ServiceBus Queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L66">constructor</a>
</h3>

```typescript
new QueueAuthorizationRule(name: string, args: QueueAuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a QueueAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QueueAuthorizationRuleState): QueueAuthorizationRule
```


Get an existing QueueAuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L26">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L30">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L38">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L42">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L46">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L50">property queueName</a>
</h3>

```typescript
public queueName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L58">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L62">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L66">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Subscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L10">class Subscription</a>
</h2>

Manage a ServiceBus Subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L91">constructor</a>
</h3>

```typescript
new Subscription(name: string, args: SubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionState): Subscription
```


Get an existing Subscription resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L28">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L29">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
public deadLetteringOnFilterEvaluationExceptions: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L35">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
public deadLetteringOnMessageExpiration: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L41">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L46">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L51">property forwardTo</a>
</h3>

```typescript
public forwardTo: pulumi.Output<string | undefined>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L56">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L61">property lockDuration</a>
</h3>

```typescript
public lockDuration: pulumi.Output<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L65">property maxDeliveryCount</a>
</h3>

```typescript
public maxDeliveryCount: pulumi.Output<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L70">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L75">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L81">property requiresSession</a>
</h3>

```typescript
public requiresSession: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L86">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L91">property topicName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L10">class SubscriptionRule</a>
</h2>

Manage a ServiceBus Subscription Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L58">constructor</a>
</h3>

```typescript
new SubscriptionRule(name: string, args: SubscriptionRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubscriptionRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionRuleState): SubscriptionRule
```


Get an existing SubscriptionRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L26">property action</a>
</h3>

```typescript
public action: pulumi.Output<string | undefined>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L30">property correlationFilter</a>
</h3>

```typescript
public correlationFilter: pulumi.Output<{ ... } | undefined>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L34">property filterType</a>
</h3>

```typescript
public filterType: pulumi.Output<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L42">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L50">property sqlFilter</a>
</h3>

```typescript
public sqlFilter: pulumi.Output<string | undefined>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L54">property subscriptionName</a>
</h3>

```typescript
public subscriptionName: pulumi.Output<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L58">property topicName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L12">class Topic</a>
</h2>

Manage a ServiceBus Topic.

**Note** Topics can only be created in Namespaces with an SKU of `standard` or higher.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L98">constructor</a>
</h3>

```typescript
new Topic(name: string, args: TopicArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicState): Topic
```


Get an existing Topic resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L29">property autoDeleteOnIdle</a>
</h3>

```typescript
public autoDeleteOnIdle: pulumi.Output<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L34">property defaultMessageTtl</a>
</h3>

```typescript
public defaultMessageTtl: pulumi.Output<string>;
```


The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L39">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
public duplicateDetectionHistoryTimeWindow: pulumi.Output<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L44">property enableBatchedOperations</a>
</h3>

```typescript
public enableBatchedOperations: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L50">property enableExpress</a>
</h3>

```typescript
public enableExpress: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L51">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
public enableFilteringMessagesBeforePublishing: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L57">property enablePartitioning</a>
</h3>

```typescript
public enablePartitioning: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L62">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L68">property maxSizeInMegabytes</a>
</h3>

```typescript
public maxSizeInMegabytes: pulumi.Output<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L73">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L78">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L84">property requiresDuplicateDetection</a>
</h3>

```typescript
public requiresDuplicateDetection: pulumi.Output<boolean | undefined>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L89">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L93">property status</a>
</h3>

```typescript
public status: pulumi.Output<string | undefined>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L98">property supportOrdering</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L10">class TopicAuthorizationRule</a>
</h2>

Manages a ServiceBus Topic authorization Rule within a ServiceBus Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L66">constructor</a>
</h3>

```typescript
new TopicAuthorizationRule(name: string, args: TopicAuthorizationRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicAuthorizationRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicAuthorizationRuleState): TopicAuthorizationRule
```


Get an existing TopicAuthorizationRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L26">property listen</a>
</h3>

```typescript
public listen: pulumi.Output<boolean | undefined>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L30">property manage</a>
</h3>

```typescript
public manage: pulumi.Output<boolean | undefined>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L38">property namespaceName</a>
</h3>

```typescript
public namespaceName: pulumi.Output<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L42">property primaryConnectionString</a>
</h3>

```typescript
public primaryConnectionString: pulumi.Output<string>;
```


The Primary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L46">property primaryKey</a>
</h3>

```typescript
public primaryKey: pulumi.Output<string>;
```


The Primary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L50">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L54">property secondaryConnectionString</a>
</h3>

```typescript
public secondaryConnectionString: pulumi.Output<string>;
```


The Secondary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L58">property secondaryKey</a>
</h3>

```typescript
public secondaryKey: pulumi.Output<string>;
```


The Secondary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L62">property send</a>
</h3>

```typescript
public send: pulumi.Output<boolean | undefined>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L66">property topicName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L10">function getEventhubNamespace</a>
</h2>

```typescript
getEventhubNamespace(args: GetEventhubNamespaceArgs, opts?: pulumi.InvokeOptions): Promise<GetEventhubNamespaceResult>
```


Use this data source to obtain information about an EventHub Namespace.

<h2 class="pdoc-module-header" id="EventGridTopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L130">interface EventGridTopicArgs</a>
</h2>

The set of arguments for constructing a EventGridTopic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L134">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L142">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L146">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventGridTopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L96">interface EventGridTopicState</a>
</h2>

Input properties used for looking up and filtering EventGridTopic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L100">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The Endpoint associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L104">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L112">property primaryAccessKey</a>
</h3>

```typescript
primaryAccessKey?: pulumi.Input<string>;
```


The Primary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L116">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L120">property secondaryAccessKey</a>
</h3>

```typescript
secondaryAccessKey?: pulumi.Input<string>;
```


The Secondary Shared Access Key associated with the EventGrid Topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventGridTopic.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L138">interface EventHubArgs</a>
</h2>

The set of arguments for constructing a EventHub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L142">property captureDescription</a>
</h3>

```typescript
captureDescription?: pulumi.Input<{ ... }>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L143">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L147">property messageRetention</a>
</h3>

```typescript
messageRetention: pulumi.Input<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L151">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L155">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L159">property partitionCount</a>
</h3>

```typescript
partitionCount: pulumi.Input<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L163">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="EventHubAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L175">interface EventHubAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a EventHubAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L179">property eventhubName</a>
</h3>

```typescript
eventhubName: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L183">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L184">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L188">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L196">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L204">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L124">interface EventHubAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering EventHubAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L128">property eventhubName</a>
</h3>

```typescript
eventhubName?: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L132">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L133">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L137">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L145">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L149">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L153">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L157">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L161">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L165">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the Event Hubs authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubAuthorizationRule.ts#L169">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubConsumerGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L115">interface EventHubConsumerGroupArgs</a>
</h2>

The set of arguments for constructing a EventHubConsumerGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L119">property eventhubName</a>
</h3>

```typescript
eventhubName: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L120">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L128">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L132">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L136">property userMetadata</a>
</h3>

```typescript
userMetadata?: pulumi.Input<string>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubConsumerGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L88">interface EventHubConsumerGroupState</a>
</h2>

Input properties used for looking up and filtering EventHubConsumerGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L92">property eventhubName</a>
</h3>

```typescript
eventhubName?: pulumi.Input<string>;
```


Specifies the name of the EventHub. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L93">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L101">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L105">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubConsumerGroup.ts#L109">property userMetadata</a>
</h3>

```typescript
userMetadata?: pulumi.Input<string>;
```


Specifies the user metadata.

<h2 class="pdoc-module-header" id="EventHubNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L185">interface EventHubNamespaceArgs</a>
</h2>

The set of arguments for constructing a EventHubNamespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L189">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled?: pulumi.Input<boolean>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L193">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L197">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L201">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits?: pulumi.Input<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L205">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L209">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L213">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L217">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubNamespaceAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L162">interface EventHubNamespaceAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a EventHubNamespaceAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L166">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L167">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L171">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L175">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L179">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L183">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L187">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubNamespaceAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L115">interface EventHubNamespaceAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering EventHubNamespaceAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L119">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L120">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L124">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L132">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L136">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L140">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L148">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L152">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespaceAuthorizationRule.ts#L156">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h2 class="pdoc-module-header" id="EventHubNamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L129">interface EventHubNamespaceState</a>
</h2>

Input properties used for looking up and filtering EventHubNamespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L133">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled?: pulumi.Input<boolean>;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L137">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L142">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString?: pulumi.Input<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L146">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey?: pulumi.Input<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L151">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString?: pulumi.Input<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L155">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey?: pulumi.Input<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L159">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L163">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits?: pulumi.Input<number>;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L167">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L171">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L175">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Defines which tier to use. Valid options are `Basic` and `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHubNamespace.ts#L179">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="EventHubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L103">interface EventHubState</a>
</h2>

Input properties used for looking up and filtering EventHub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L107">property captureDescription</a>
</h3>

```typescript
captureDescription?: pulumi.Input<{ ... }>;
```


A `capture_description` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L108">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L112">property messageRetention</a>
</h3>

```typescript
messageRetention?: pulumi.Input<number>;
```


Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L120">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L124">property partitionCount</a>
</h3>

```typescript
partitionCount?: pulumi.Input<number>;
```


Specifies the current number of shards on the Event Hub.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L128">property partitionIds</a>
</h3>

```typescript
partitionIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The identifiers for partitions created for Event Hubs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/eventHub.ts#L132">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="GetEventhubNamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L20">interface GetEventhubNamespaceArgs</a>
</h2>

A collection of arguments for invoking getEventhubNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the EventHub Namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where the EventHub Namespace exists.

<h2 class="pdoc-module-header" id="GetEventhubNamespaceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L34">interface GetEventhubNamespaceResult</a>
</h2>

A collection of values returned by getEventhubNamespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L38">property autoInflateEnabled</a>
</h3>

```typescript
autoInflateEnabled: boolean;
```


Is Auto Inflate enabled for the EventHub Namespace?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L42">property capacity</a>
</h3>

```typescript
capacity: number;
```


The Capacity / Throughput Units for a `Standard` SKU namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L47">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString: string;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L51">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey: string;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L56">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString: string;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L60">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey: string;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L80">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L64">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the EventHub Namespace exists

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L68">property maximumThroughputUnits</a>
</h3>

```typescript
maximumThroughputUnits: number;
```


Specifies the maximum number of throughput units when Auto Inflate is Enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L72">property sku</a>
</h3>

```typescript
sku: string;
```


Defines which tier to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/getEventhubNamespace.ts#L76">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the EventHub Namespace.

<h2 class="pdoc-module-header" id="NamespaceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L169">interface NamespaceArgs</a>
</h2>

The set of arguments for constructing a Namespace resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L173">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the capacity, can only be set when `sku` is `Premium` namespace. Can be `1`, `2` or `4`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L177">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L187">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L191">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L195">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="NamespaceAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L158">interface NamespaceAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a NamespaceAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L162">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L166">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L174">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L178">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L182">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h2 class="pdoc-module-header" id="NamespaceAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L112">interface NamespaceAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering NamespaceAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L116">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L120">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L124">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L128">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L132">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L136">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L140">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L144">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L148">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the ServiceBus Namespace authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespaceAuthorizationRule.ts#L152">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h2 class="pdoc-module-header" id="NamespaceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L119">interface NamespaceState</a>
</h2>

Input properties used for looking up and filtering Namespace resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L123">property capacity</a>
</h3>

```typescript
capacity?: pulumi.Input<number>;
```


Specifies the capacity, can only be set when `sku` is `Premium` namespace. Can be `1`, `2` or `4`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L128">property defaultPrimaryConnectionString</a>
</h3>

```typescript
defaultPrimaryConnectionString?: pulumi.Input<string>;
```


The primary connection string for the authorization
rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L132">property defaultPrimaryKey</a>
</h3>

```typescript
defaultPrimaryKey?: pulumi.Input<string>;
```


The primary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L137">property defaultSecondaryConnectionString</a>
</h3>

```typescript
defaultSecondaryConnectionString?: pulumi.Input<string>;
```


The secondary connection string for the
authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L141">property defaultSecondaryKey</a>
</h3>

```typescript
defaultSecondaryKey?: pulumi.Input<string>;
```


The secondary access key for the authorization rule `RootManageSharedAccessKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L145">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L155">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L159">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Defines which tier to use. Options are basic, standard or premium.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/namespace.ts#L163">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="QueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L246">interface QueueArgs</a>
</h2>

The set of arguments for constructing a Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L251">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L255">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L260">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L265">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L266">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L273">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L280">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L285">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L289">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L295">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L300">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L305">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L311">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L318">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L323">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L324">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="QueueAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L171">interface QueueAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a QueueAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L175">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L179">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L187">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L191">property queueName</a>
</h3>

```typescript
queueName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L195">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L199">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to `false`.

<h2 class="pdoc-module-header" id="QueueAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L121">interface QueueAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering QueueAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L125">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L129">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L137">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L141">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L145">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L149">property queueName</a>
</h3>

```typescript
queueName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L153">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L157">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L161">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the Authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queueAuthorizationRule.ts#L165">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to `false`.

<h2 class="pdoc-module-header" id="QueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L162">interface QueueState</a>
</h2>

Input properties used for looking up and filtering Queue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L167">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L171">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L176">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L181">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L182">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L189">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L196">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L201">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L205">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L211">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L221">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L227">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L234">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L239">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/queue.ts#L240">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```

<h2 class="pdoc-module-header" id="SubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L230">interface SubscriptionArgs</a>
</h2>

The set of arguments for constructing a Subscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L236">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L237">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
deadLetteringOnFilterEvaluationExceptions?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L243">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L249">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L254">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L259">property forwardTo</a>
</h3>

```typescript
forwardTo?: pulumi.Input<string>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L264">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L269">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L273">property maxDeliveryCount</a>
</h3>

```typescript
maxDeliveryCount: pulumi.Input<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L278">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L283">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L289">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L294">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L299">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L157">interface SubscriptionRuleArgs</a>
</h2>

The set of arguments for constructing a SubscriptionRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L161">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L165">property correlationFilter</a>
</h3>

```typescript
correlationFilter?: pulumi.Input<{ ... }>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L169">property filterType</a>
</h3>

```typescript
filterType: pulumi.Input<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L173">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L177">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L181">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L185">property sqlFilter</a>
</h3>

```typescript
sqlFilter?: pulumi.Input<string>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L189">property subscriptionName</a>
</h3>

```typescript
subscriptionName: pulumi.Input<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L193">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L115">interface SubscriptionRuleState</a>
</h2>

Input properties used for looking up and filtering SubscriptionRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L119">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L123">property correlationFilter</a>
</h3>

```typescript
correlationFilter?: pulumi.Input<{ ... }>;
```


A `correlation_filter` block as documented below to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L127">property filterType</a>
</h3>

```typescript
filterType?: pulumi.Input<string>;
```


Type of filter to be applied to a BrokeredMessage. Possible values are `SqlFilter` and `CorrelationFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L135">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L139">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L143">property sqlFilter</a>
</h3>

```typescript
sqlFilter?: pulumi.Input<string>;
```


Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when `filter_type` is set to `SqlFilter`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L147">property subscriptionName</a>
</h3>

```typescript
subscriptionName?: pulumi.Input<string>;
```


The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscriptionRule.ts#L151">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L155">interface SubscriptionState</a>
</h2>

Input properties used for looking up and filtering Subscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L161">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L162">property deadLetteringOnFilterEvaluationExceptions</a>
</h3>

```typescript
deadLetteringOnFilterEvaluationExceptions?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L168">property deadLetteringOnMessageExpiration</a>
</h3>

```typescript
deadLetteringOnMessageExpiration?: pulumi.Input<boolean>;
```


Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L174">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L179">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L184">property forwardTo</a>
</h3>

```typescript
forwardTo?: pulumi.Input<string>;
```


The name of a Queue or Topic to automatically forward
messages to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L189">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L194">property lockDuration</a>
</h3>

```typescript
lockDuration?: pulumi.Input<string>;
```


The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L198">property maxDeliveryCount</a>
</h3>

```typescript
maxDeliveryCount?: pulumi.Input<number>;
```


The maximum number of deliveries.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L203">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L208">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L214">property requiresSession</a>
</h3>

```typescript
requiresSession?: pulumi.Input<boolean>;
```


Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L219">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/subscription.ts#L224">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L238">interface TopicArgs</a>
</h2>

The set of arguments for constructing a Topic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L243">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L248">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L253">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L258">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L264">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L265">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
enableFilteringMessagesBeforePublishing?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L271">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L276">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L282">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L287">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L292">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L298">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L303">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L307">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L312">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

<h2 class="pdoc-module-header" id="TopicAuthorizationRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L171">interface TopicAuthorizationRuleArgs</a>
</h2>

The set of arguments for constructing a TopicAuthorizationRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L175">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L179">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L183">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L187">property namespaceName</a>
</h3>

```typescript
namespaceName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L191">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L195">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L199">property topicName</a>
</h3>

```typescript
topicName: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicAuthorizationRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L121">interface TopicAuthorizationRuleState</a>
</h2>

Input properties used for looking up and filtering TopicAuthorizationRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L125">property listen</a>
</h3>

```typescript
listen?: pulumi.Input<boolean>;
```


Grants listen access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L129">property manage</a>
</h3>

```typescript
manage?: pulumi.Input<boolean>;
```


Grants manage access to this this Authorization Rule. When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L137">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L141">property primaryConnectionString</a>
</h3>

```typescript
primaryConnectionString?: pulumi.Input<string>;
```


The Primary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L145">property primaryKey</a>
</h3>

```typescript
primaryKey?: pulumi.Input<string>;
```


The Primary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L149">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L153">property secondaryConnectionString</a>
</h3>

```typescript
secondaryConnectionString?: pulumi.Input<string>;
```


The Secondary Connection String for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L157">property secondaryKey</a>
</h3>

```typescript
secondaryKey?: pulumi.Input<string>;
```


The Secondary Key for the ServiceBus Topic authorization Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L161">property send</a>
</h3>

```typescript
send?: pulumi.Input<boolean>;
```


Grants send access to this this Authorization Rule. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topicAuthorizationRule.ts#L165">property topicName</a>
</h3>

```typescript
topicName?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L158">interface TopicState</a>
</h2>

Input properties used for looking up and filtering Topic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L163">property autoDeleteOnIdle</a>
</h3>

```typescript
autoDeleteOnIdle?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L168">property defaultMessageTtl</a>
</h3>

```typescript
defaultMessageTtl?: pulumi.Input<string>;
```


The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L173">property duplicateDetectionHistoryTimeWindow</a>
</h3>

```typescript
duplicateDetectionHistoryTimeWindow?: pulumi.Input<string>;
```


The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (`PT10M`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L178">property enableBatchedOperations</a>
</h3>

```typescript
enableBatchedOperations?: pulumi.Input<boolean>;
```


Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L184">property enableExpress</a>
</h3>

```typescript
enableExpress?: pulumi.Input<boolean>;
```


Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L185">property enableFilteringMessagesBeforePublishing</a>
</h3>

```typescript
enableFilteringMessagesBeforePublishing?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L191">property enablePartitioning</a>
</h3>

```typescript
enablePartitioning?: pulumi.Input<boolean>;
```


Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L196">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L202">property maxSizeInMegabytes</a>
</h3>

```typescript
maxSizeInMegabytes?: pulumi.Input<number>;
```


Integer value which controls the size of
memory allocated for the topic. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L207">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L212">property namespaceName</a>
</h3>

```typescript
namespaceName?: pulumi.Input<string>;
```


The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L218">property requiresDuplicateDetection</a>
</h3>

```typescript
requiresDuplicateDetection?: pulumi.Input<boolean>;
```


Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L223">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L227">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The Status of the Service Bus Topic. Acceptable values are `Active` or `Disabled`. Defaults to `Active`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/eventhub/topic.ts#L232">property supportOrdering</a>
</h3>

```typescript
supportOrdering?: pulumi.Input<boolean>;
```


Boolean flag which controls whether the Topic
supports ordering. Defaults to false.

