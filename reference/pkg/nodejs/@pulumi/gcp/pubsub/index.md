---
title: Module pubsub
---

<a href="../index.html">@pulumi/gcp</a> &gt; pubsub

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Subscription">class Subscription</a>
* <a href="#SubscriptionIAMBinding">class SubscriptionIAMBinding</a>
* <a href="#SubscriptionIAMMember">class SubscriptionIAMMember</a>
* <a href="#SubscriptionIAMPolicy">class SubscriptionIAMPolicy</a>
* <a href="#Topic">class Topic</a>
* <a href="#TopicIAMBinding">class TopicIAMBinding</a>
* <a href="#TopicIAMMember">class TopicIAMMember</a>
* <a href="#TopicIAMPolicy">class TopicIAMPolicy</a>
* <a href="#SubscriptionArgs">interface SubscriptionArgs</a>
* <a href="#SubscriptionIAMBindingArgs">interface SubscriptionIAMBindingArgs</a>
* <a href="#SubscriptionIAMBindingState">interface SubscriptionIAMBindingState</a>
* <a href="#SubscriptionIAMMemberArgs">interface SubscriptionIAMMemberArgs</a>
* <a href="#SubscriptionIAMMemberState">interface SubscriptionIAMMemberState</a>
* <a href="#SubscriptionIAMPolicyArgs">interface SubscriptionIAMPolicyArgs</a>
* <a href="#SubscriptionIAMPolicyState">interface SubscriptionIAMPolicyState</a>
* <a href="#SubscriptionState">interface SubscriptionState</a>
* <a href="#TopicArgs">interface TopicArgs</a>
* <a href="#TopicIAMBindingArgs">interface TopicIAMBindingArgs</a>
* <a href="#TopicIAMBindingState">interface TopicIAMBindingState</a>
* <a href="#TopicIAMMemberArgs">interface TopicIAMMemberArgs</a>
* <a href="#TopicIAMMemberState">interface TopicIAMMemberState</a>
* <a href="#TopicIAMPolicyArgs">interface TopicIAMPolicyArgs</a>
* <a href="#TopicIAMPolicyState">interface TopicIAMPolicyState</a>
* <a href="#TopicState">interface TopicState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts">pubsub/subscription.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts">pubsub/subscriptionIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts">pubsub/subscriptionIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts">pubsub/subscriptionIAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts">pubsub/topic.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts">pubsub/topicIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts">pubsub/topicIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts">pubsub/topicIAMPolicy.ts</a> 


<h2 class="pdoc-module-header" id="Subscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L13">class Subscription</a>
</h2>

Creates a subscription in Google's pubsub queueing system. For more information see
[the official documentation](https://cloud.google.com/pubsub/docs) and
[API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L55">constructor</a>
</h3>

```typescript
new Subscription(name: string, args: SubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Subscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionState): Subscription
```


Get an existing Subscription resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L31">property ackDeadlineSeconds</a>
</h3>

```typescript
public ackDeadlineSeconds: pulumi.Output<number>;
```


The maximum number of seconds a
subscriber has to acknowledge a received message, otherwise the message is
redelivered. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by pubsub.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L40">property path</a>
</h3>

```typescript
public path: pulumi.Output<string>;
```


Path of the subscription in the format `projects/{project}/subscriptions/{sub}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L45">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L50">property pushConfig</a>
</h3>

```typescript
public pushConfig: pulumi.Output<{ ... } | undefined>;
```


Block configuration for push options. More
configuration options are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L55">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<string>;
```


The topic name or id to bind this subscription to, required by pubsub.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L18">class SubscriptionIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:

* `google_pubsub_subscription_iam_policy`: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.
* `google_pubsub_subscription_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.
* `google_pubsub_subscription_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.

~> **Note:** `google_pubsub_subscription_iam_policy` **cannot** be used in conjunction with `google_pubsub_subscription_iam_binding` and `google_pubsub_subscription_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_subscription_iam_binding` resources **can be** used in conjunction with `google_pubsub_subscription_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L50">constructor</a>
</h3>

```typescript
new SubscriptionIAMBinding(name: string, args: SubscriptionIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubscriptionIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionIAMBindingState): SubscriptionIAMBinding
```


Get an existing SubscriptionIAMBinding resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L35">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L40">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L46">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L50">property subscription</a>
</h3>

```typescript
public subscription: pulumi.Output<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L18">class SubscriptionIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:

* `google_pubsub_subscription_iam_policy`: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.
* `google_pubsub_subscription_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.
* `google_pubsub_subscription_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.

~> **Note:** `google_pubsub_subscription_iam_policy` **cannot** be used in conjunction with `google_pubsub_subscription_iam_binding` and `google_pubsub_subscription_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_subscription_iam_binding` resources **can be** used in conjunction with `google_pubsub_subscription_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L50">constructor</a>
</h3>

```typescript
new SubscriptionIAMMember(name: string, args: SubscriptionIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubscriptionIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionIAMMemberState): SubscriptionIAMMember
```


Get an existing SubscriptionIAMMember resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L35">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L40">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L46">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L50">property subscription</a>
</h3>

```typescript
public subscription: pulumi.Output<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L18">class SubscriptionIAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:

* `google_pubsub_subscription_iam_policy`: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.
* `google_pubsub_subscription_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.
* `google_pubsub_subscription_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.

~> **Note:** `google_pubsub_subscription_iam_policy` **cannot** be used in conjunction with `google_pubsub_subscription_iam_binding` and `google_pubsub_subscription_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_subscription_iam_binding` resources **can be** used in conjunction with `google_pubsub_subscription_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L48">constructor</a>
</h3>

```typescript
new SubscriptionIAMPolicy(name: string, args: SubscriptionIAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SubscriptionIAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubscriptionIAMPolicyState): SubscriptionIAMPolicy
```


Get an existing SubscriptionIAMPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L39">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L44">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L48">property subscription</a>
</h3>

```typescript
public subscription: pulumi.Output<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L13">class Topic</a>
</h2>

Creates a topic in Google's pubsub queueing system. For more information see
[the official documentation](https://cloud.google.com/pubsub/docs) and
[API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L35">constructor</a>
</h3>

```typescript
new Topic(name: string, args?: TopicArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicState): Topic
```


Get an existing Topic resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the pubsub topic.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L35">property project</a>
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

<h2 class="pdoc-module-header" id="TopicIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L18">class TopicIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:

* `google_pubsub_topic_iam_policy`: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.
* `google_pubsub_topic_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.
* `google_pubsub_topic_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.

~> **Note:** `google_pubsub_topic_iam_policy` **cannot** be used in conjunction with `google_pubsub_topic_iam_binding` and `google_pubsub_topic_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_topic_iam_binding` resources **can be** used in conjunction with `google_pubsub_topic_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L50">constructor</a>
</h3>

```typescript
new TopicIAMBinding(name: string, args: TopicIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicIAMBindingState): TopicIAMBinding
```


Get an existing TopicIAMBinding resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L35">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L40">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L46">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L50">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<string>;
```


The topic name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L18">class TopicIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:

* `google_pubsub_topic_iam_policy`: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.
* `google_pubsub_topic_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.
* `google_pubsub_topic_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.

~> **Note:** `google_pubsub_topic_iam_policy` **cannot** be used in conjunction with `google_pubsub_topic_iam_binding` and `google_pubsub_topic_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_topic_iam_binding` resources **can be** used in conjunction with `google_pubsub_topic_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L50">constructor</a>
</h3>

```typescript
new TopicIAMMember(name: string, args: TopicIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicIAMMemberState): TopicIAMMember
```


Get an existing TopicIAMMember resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L35">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L40">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L46">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L50">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<string>;
```


The topic name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L18">class TopicIAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for pubsub topic. Each of these resources serves a different use case:

* `google_pubsub_topic_iam_policy`: Authoritative. Sets the IAM policy for the topic and replaces any existing policy already attached.
* `google_pubsub_topic_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the topic are preserved.
* `google_pubsub_topic_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the topic are preserved.

~> **Note:** `google_pubsub_topic_iam_policy` **cannot** be used in conjunction with `google_pubsub_topic_iam_binding` and `google_pubsub_topic_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_pubsub_topic_iam_binding` resources **can be** used in conjunction with `google_pubsub_topic_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L48">constructor</a>
</h3>

```typescript
new TopicIAMPolicy(name: string, args: TopicIAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicIAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicIAMPolicyState): TopicIAMPolicy
```


Get an existing TopicIAMPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L34">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L39">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L44">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L48">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<string>;
```


The topic name or id to bind to attach IAM policy to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L130">interface SubscriptionArgs</a>
</h2>

The set of arguments for constructing a Subscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L136">property ackDeadlineSeconds</a>
</h3>

```typescript
ackDeadlineSeconds?: pulumi.Input<number>;
```


The maximum number of seconds a
subscriber has to acknowledge a received message, otherwise the message is
redelivered. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by pubsub.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L146">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L151">property pushConfig</a>
</h3>

```typescript
pushConfig?: pulumi.Input<{ ... }>;
```


Block configuration for push options. More
configuration options are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L156">property topic</a>
</h3>

```typescript
topic: pulumi.Input<string>;
```


The topic name or id to bind this subscription to, required by pubsub.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="SubscriptionIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L119">interface SubscriptionIAMBindingArgs</a>
</h2>

The set of arguments for constructing a SubscriptionIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L120">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L125">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L131">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L135">property subscription</a>
</h3>

```typescript
subscription: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L93">interface SubscriptionIAMBindingState</a>
</h2>

Input properties used for looking up and filtering SubscriptionIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L97">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L98">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L103">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L109">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMBinding.ts#L113">property subscription</a>
</h3>

```typescript
subscription?: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L119">interface SubscriptionIAMMemberArgs</a>
</h2>

The set of arguments for constructing a SubscriptionIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L120">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L125">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L131">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L135">property subscription</a>
</h3>

```typescript
subscription: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L93">interface SubscriptionIAMMemberState</a>
</h2>

Input properties used for looking up and filtering SubscriptionIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L97">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L98">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L103">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L109">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_subscription_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMMember.ts#L113">property subscription</a>
</h3>

```typescript
subscription?: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L110">interface SubscriptionIAMPolicyArgs</a>
</h2>

The set of arguments for constructing a SubscriptionIAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L115">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L120">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L124">property subscription</a>
</h3>

```typescript
subscription: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionIAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L86">interface SubscriptionIAMPolicyState</a>
</h2>

Input properties used for looking up and filtering SubscriptionIAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L90">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the subscription's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L95">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L100">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscriptionIAMPolicy.ts#L104">property subscription</a>
</h3>

```typescript
subscription?: pulumi.Input<string>;
```


The subscription name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="SubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L94">interface SubscriptionState</a>
</h2>

Input properties used for looking up and filtering Subscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L100">property ackDeadlineSeconds</a>
</h3>

```typescript
ackDeadlineSeconds?: pulumi.Input<number>;
```


The maximum number of seconds a
subscriber has to acknowledge a received message, otherwise the message is
redelivered. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by pubsub.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L109">property path</a>
</h3>

```typescript
path?: pulumi.Input<string>;
```


Path of the subscription in the format `projects/{project}/subscriptions/{sub}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L114">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L119">property pushConfig</a>
</h3>

```typescript
pushConfig?: pulumi.Input<{ ... }>;
```


Block configuration for push options. More
configuration options are detailed below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/subscription.ts#L124">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<string>;
```


The topic name or id to bind this subscription to, required by pubsub.
Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="TopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L79">interface TopicArgs</a>
</h2>

The set of arguments for constructing a Topic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the pubsub topic.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L89">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="TopicIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L119">interface TopicIAMBindingArgs</a>
</h2>

The set of arguments for constructing a TopicIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L120">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L125">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L131">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L135">property topic</a>
</h3>

```typescript
topic: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L93">interface TopicIAMBindingState</a>
</h2>

Input properties used for looking up and filtering TopicIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L97">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L98">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L103">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L109">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMBinding.ts#L113">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L119">interface TopicIAMMemberArgs</a>
</h2>

The set of arguments for constructing a TopicIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L120">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L125">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L131">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L135">property topic</a>
</h3>

```typescript
topic: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L93">interface TopicIAMMemberState</a>
</h2>

Input properties used for looking up and filtering TopicIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L97">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L98">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L103">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L109">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_pubsub_topic_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMMember.ts#L113">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L110">interface TopicIAMPolicyArgs</a>
</h2>

The set of arguments for constructing a TopicIAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L115">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L120">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L124">property topic</a>
</h3>

```typescript
topic: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicIAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L86">interface TopicIAMPolicyState</a>
</h2>

Input properties used for looking up and filtering TopicIAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L90">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the topic's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L95">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L100">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topicIAMPolicy.ts#L104">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<string>;
```


The topic name or id to bind to attach IAM policy to.

<h2 class="pdoc-module-header" id="TopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L63">interface TopicState</a>
</h2>

Input properties used for looking up and filtering Topic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L68">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the pubsub topic.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/pubsub/topic.ts#L73">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

