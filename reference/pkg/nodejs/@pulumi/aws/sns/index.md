---
title: Module sns
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#PlatformApplication">class PlatformApplication</a>
* <a href="#Topic">class Topic</a>
* <a href="#TopicPolicy">class TopicPolicy</a>
* <a href="#TopicSubscription">class TopicSubscription</a>
* <a href="#getTopic">function getTopic</a>
* <a href="#GetTopicArgs">interface GetTopicArgs</a>
* <a href="#GetTopicResult">interface GetTopicResult</a>
* <a href="#PlatformApplicationArgs">interface PlatformApplicationArgs</a>
* <a href="#PlatformApplicationState">interface PlatformApplicationState</a>
* <a href="#TopicArgs">interface TopicArgs</a>
* <a href="#TopicPolicyArgs">interface TopicPolicyArgs</a>
* <a href="#TopicPolicyState">interface TopicPolicyState</a>
* <a href="#TopicState">interface TopicState</a>
* <a href="#TopicSubscriptionArgs">interface TopicSubscriptionArgs</a>
* <a href="#TopicSubscriptionState">interface TopicSubscriptionState</a>

<a href="/sns/getTopic.ts">sns/getTopic.ts</a> <a href="/sns/platformApplication.ts">sns/platformApplication.ts</a> <a href="/sns/topic.ts">sns/topic.ts</a> <a href="/sns/topicPolicy.ts">sns/topicPolicy.ts</a> <a href="/sns/topicSubscription.ts">sns/topicSubscription.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="PlatformApplication">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L9">class PlatformApplication</a>
</h2>

Provides an SNS platform application resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L66">constructor</a>
</h3>

```typescript
new PlatformApplication(name: string, args: PlatformApplicationArgs, opts?: pulumi.ResourceOptions)
```


Create a PlatformApplication resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new PlatformApplication(name: string, state?: PlatformApplicationState, opts?: pulumi.ResourceOptions)
```


Create a PlatformApplication resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlatformApplicationState): PlatformApplication
```


Get an existing PlatformApplication resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L29">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
public eventDeliveryFailureTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L33">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
public eventEndpointCreatedTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L37">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
public eventEndpointDeletedTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L38">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
public eventEndpointUpdatedTopicArn: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L42">property failureFeedbackRoleArn</a>
</h3>

```typescript
public failureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L50">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L54">property platformCredential</a>
</h3>

```typescript
public platformCredential: pulumi.Output<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L58">property platformPrincipal</a>
</h3>

```typescript
public platformPrincipal: pulumi.Output<string | undefined>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L62">property successFeedbackRoleArn</a>
</h3>

```typescript
public successFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L66">property successFeedbackSampleRate</a>
</h3>

```typescript
public successFeedbackSampleRate: pulumi.Output<string | undefined>;
```


The percentage of success to sample (0-100)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L11">class Topic</a>
</h2>

Provides an SNS topic resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L95">constructor</a>
</h3>

```typescript
new Topic(name: string, args?: TopicArgs, opts?: pulumi.ResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Topic(name: string, state?: TopicState, opts?: pulumi.ResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicState): Topic
```


Get an existing Topic resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L27">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
public applicationFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L31">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
public applicationSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L35">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
public applicationSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L39">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<ARN>;
```


The ARN of the SNS topic, as a more obvious property (clone of id)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L43">property deliveryPolicy</a>
</h3>

```typescript
public deliveryPolicy: pulumi.Output<string | undefined>;
```


The SNS delivery policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L47">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string | undefined>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L51">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
public httpFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L55">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
public httpSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L59">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
public httpSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L63">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
public lambdaFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L67">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
public lambdaSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L71">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
public lambdaSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L79">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L83">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The fully-formed AWS policy as JSON

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L87">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
public sqsFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L91">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
public sqsSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L95">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
public sqsSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L11">class TopicPolicy</a>
</h2>

Provides an SNS topic policy resource

~> **NOTE:** If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future terraform plans to differ. To avoid this problem, just specify the full ARN, e.g. `arn:aws:iam::123456789012:root`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L31">constructor</a>
</h3>

```typescript
new TopicPolicy(name: string, args: TopicPolicyArgs, opts?: pulumi.ResourceOptions)
```


Create a TopicPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new TopicPolicy(name: string, state?: TopicPolicyState, opts?: pulumi.ResourceOptions)
```


Create a TopicPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicPolicyState): TopicPolicy
```


Get an existing TopicPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L31">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The fully-formed AWS policy as JSON

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L22">class TopicSubscription</a>
</h2>

  Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.
This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will
probably be SQS queues.

~> **NOTE:** If SNS topic and SQS queue are in different AWS regions it is important to place the "aws_sns_topic_subscription" into the terraform configuration of the region with the SQS queue. If "aws_sns_topic_subscription" is placed in the terraform configuration of the region with the SNS topic terraform will fail to create the subscription.

~> **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts but the same region it is important to place the "aws_sns_topic_subscription" into the terraform configuration of the account with the SQS queue. If "aws_sns_topic_subscription" is placed in the terraform configuration of the account with the SNS topic terraform creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L67">constructor</a>
</h3>

```typescript
new TopicSubscription(name: string, args: TopicSubscriptionArgs, opts?: pulumi.ResourceOptions)
```


Create a TopicSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new TopicSubscription(name: string, state?: TopicSubscriptionState, opts?: pulumi.ResourceOptions)
```


Create a TopicSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L31">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicSubscriptionState): TopicSubscription
```


Get an existing TopicSubscription resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L38">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the subscription stored as a more user-friendly property

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L42">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
public confirmationTimeoutInMinutes: pulumi.Output<number | undefined>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L43">property deliveryPolicy</a>
</h3>

```typescript
public deliveryPolicy: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L47">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L51">property endpointAutoConfirms</a>
</h3>

```typescript
public endpointAutoConfirms: pulumi.Output<boolean | undefined>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L55">property filterPolicy</a>
</h3>

```typescript
public filterPolicy: pulumi.Output<string | undefined>;
```


The text of a filter policy to the topic subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L59">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L63">property rawMessageDelivery</a>
</h3>

```typescript
public rawMessageDelivery: pulumi.Output<boolean | undefined>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L67">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<Topic>;
```


The ARN of the SNS topic to subscribe to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getTopic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/getTopic.ts#L11">function getTopic</a>
</h2>

```typescript
getTopic(args: GetTopicArgs): Promise<GetTopicResult>
```


Use this data source to get the ARN of a topic in AWS Simple Notification
Service (SNS). By using this data source, you can reference SNS topics
without having to hard code the ARNs as input.

<h2 class="pdoc-module-header" id="GetTopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/getTopic.ts#L20">interface GetTopicArgs</a>
</h2>

A collection of arguments for invoking getTopic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/getTopic.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The friendly name of the topic to match.

<h2 class="pdoc-module-header" id="GetTopicResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/getTopic.ts#L30">interface GetTopicResult</a>
</h2>

A collection of values returned by getTopic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/getTopic.ts#L34">property arn</a>
</h3>

```typescript
arn: string;
```


Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.

<h2 class="pdoc-module-header" id="PlatformApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L173">interface PlatformApplicationArgs</a>
</h2>

The set of arguments for constructing a PlatformApplication resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L177">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
eventDeliveryFailureTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L181">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
eventEndpointCreatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L185">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
eventEndpointDeletedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L186">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
eventEndpointUpdatedTopicArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L190">property failureFeedbackRoleArn</a>
</h3>

```typescript
failureFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L198">property platform</a>
</h3>

```typescript
platform: pulumi.Input<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L202">property platformCredential</a>
</h3>

```typescript
platformCredential: pulumi.Input<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L206">property platformPrincipal</a>
</h3>

```typescript
platformPrincipal?: pulumi.Input<string>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L210">property successFeedbackRoleArn</a>
</h3>

```typescript
successFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L214">property successFeedbackSampleRate</a>
</h3>

```typescript
successFeedbackSampleRate?: pulumi.Input<string>;
```


The percentage of success to sample (0-100)

<h2 class="pdoc-module-header" id="PlatformApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L122">interface PlatformApplicationState</a>
</h2>

Input properties used for looking up and filtering PlatformApplication resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L126">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L130">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
eventDeliveryFailureTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L134">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
eventEndpointCreatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L138">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
eventEndpointDeletedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L139">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
eventEndpointUpdatedTopicArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L143">property failureFeedbackRoleArn</a>
</h3>

```typescript
failureFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L151">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L155">property platformCredential</a>
</h3>

```typescript
platformCredential?: pulumi.Input<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L159">property platformPrincipal</a>
</h3>

```typescript
platformPrincipal?: pulumi.Input<string>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L163">property successFeedbackRoleArn</a>
</h3>

```typescript
successFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/platformApplication.ts#L167">property successFeedbackSampleRate</a>
</h3>

```typescript
successFeedbackSampleRate?: pulumi.Input<string>;
```


The percentage of success to sample (0-100)

<h2 class="pdoc-module-header" id="TopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L235">interface TopicArgs</a>
</h2>

The set of arguments for constructing a Topic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L239">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
applicationFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L243">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
applicationSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L247">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
applicationSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L251">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


The SNS delivery policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L255">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L259">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
httpFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L263">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
httpSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L267">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
httpSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L271">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
lambdaFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L275">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
lambdaSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L279">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
lambdaSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L283">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L287">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L291">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L295">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
sqsFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L299">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
sqsSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L303">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
sqsSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h2 class="pdoc-module-header" id="TopicPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L81">interface TopicPolicyArgs</a>
</h2>

The set of arguments for constructing a TopicPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L85">property arn</a>
</h3>

```typescript
arn: pulumi.Input<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L89">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON

<h2 class="pdoc-module-header" id="TopicPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L67">interface TopicPolicyState</a>
</h2>

Input properties used for looking up and filtering TopicPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L71">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicPolicy.ts#L75">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON

<h2 class="pdoc-module-header" id="TopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L157">interface TopicState</a>
</h2>

Input properties used for looking up and filtering Topic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L161">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
applicationFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L165">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
applicationSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L169">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
applicationSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L173">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<ARN>;
```


The ARN of the SNS topic, as a more obvious property (clone of id)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L177">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


The SNS delivery policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L181">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L185">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
httpFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L189">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
httpSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L193">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
httpSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L197">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
lambdaFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L201">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
lambdaSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L205">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
lambdaSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L209">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L213">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L217">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L221">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
sqsFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L225">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
sqsSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topic.ts#L229">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
sqsSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h2 class="pdoc-module-header" id="TopicSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L159">interface TopicSubscriptionArgs</a>
</h2>

The set of arguments for constructing a TopicSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L163">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
confirmationTimeoutInMinutes?: pulumi.Input<number>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L164">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L168">property endpoint</a>
</h3>

```typescript
endpoint: pulumi.Input<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L172">property endpointAutoConfirms</a>
</h3>

```typescript
endpointAutoConfirms?: pulumi.Input<boolean>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L176">property filterPolicy</a>
</h3>

```typescript
filterPolicy?: pulumi.Input<string>;
```


The text of a filter policy to the topic subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L180">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L184">property rawMessageDelivery</a>
</h3>

```typescript
rawMessageDelivery?: pulumi.Input<boolean>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L188">property topic</a>
</h3>

```typescript
topic: pulumi.Input<Topic>;
```


The ARN of the SNS topic to subscribe to

<h2 class="pdoc-module-header" id="TopicSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L120">interface TopicSubscriptionState</a>
</h2>

Input properties used for looking up and filtering TopicSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L124">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the subscription stored as a more user-friendly property

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L128">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
confirmationTimeoutInMinutes?: pulumi.Input<number>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L129">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L133">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L137">property endpointAutoConfirms</a>
</h3>

```typescript
endpointAutoConfirms?: pulumi.Input<boolean>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L141">property filterPolicy</a>
</h3>

```typescript
filterPolicy?: pulumi.Input<string>;
```


The text of a filter policy to the topic subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L145">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L149">property rawMessageDelivery</a>
</h3>

```typescript
rawMessageDelivery?: pulumi.Input<boolean>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/sns/topicSubscription.ts#L153">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<Topic>;
```


The ARN of the SNS topic to subscribe to

