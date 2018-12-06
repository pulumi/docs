---
title: Module sns
---

<a href="../index.html">@pulumi/aws</a> &gt; sns

<h2 class="pdoc-module-header">Index</h2>

* <a href="#PlatformApplication">class PlatformApplication</a>
* <a href="#SmsPreferences">class SmsPreferences</a>
* <a href="#Topic">class Topic</a>
* <a href="#TopicEventSubscription">class TopicEventSubscription</a>
* <a href="#TopicPolicy">class TopicPolicy</a>
* <a href="#TopicSubscription">class TopicSubscription</a>
* <a href="#getTopic">function getTopic</a>
* <a href="#GetTopicArgs">interface GetTopicArgs</a>
* <a href="#GetTopicResult">interface GetTopicResult</a>
* <a href="#PlatformApplicationArgs">interface PlatformApplicationArgs</a>
* <a href="#PlatformApplicationState">interface PlatformApplicationState</a>
* <a href="#SNSItem">interface SNSItem</a>
* <a href="#SNSMessageAttribute">interface SNSMessageAttribute</a>
* <a href="#SmsPreferencesArgs">interface SmsPreferencesArgs</a>
* <a href="#SmsPreferencesState">interface SmsPreferencesState</a>
* <a href="#TopicArgs">interface TopicArgs</a>
* <a href="#TopicEvent">interface TopicEvent</a>
* <a href="#TopicPolicyArgs">interface TopicPolicyArgs</a>
* <a href="#TopicPolicyState">interface TopicPolicyState</a>
* <a href="#TopicRecord">interface TopicRecord</a>
* <a href="#TopicState">interface TopicState</a>
* <a href="#TopicSubscriptionArgs">interface TopicSubscriptionArgs</a>
* <a href="#TopicSubscriptionState">interface TopicSubscriptionState</a>
* <a href="#TopicEventHandler">type TopicEventHandler</a>
* <a href="#TopicEventSubscriptionArgs">type TopicEventSubscriptionArgs</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts">sns/getTopic.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts">sns/platformApplication.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts">sns/smsPreferences.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts">sns/snsMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts">sns/topic.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts">sns/topicPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts">sns/topicSubscription.ts</a> 


<h2 class="pdoc-module-header" id="PlatformApplication">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L10">class PlatformApplication</a>
</h2>

Provides an SNS platform application resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L70">constructor</a>
</h3>

```typescript
new PlatformApplication(name: string, args: PlatformApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PlatformApplication resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PlatformApplicationState): PlatformApplication
```


Get an existing PlatformApplication resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L26">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L30">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
public eventDeliveryFailureTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L34">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
public eventEndpointCreatedTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L38">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
public eventEndpointDeletedTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L42">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
public eventEndpointUpdatedTopicArn: pulumi.Output<string | undefined>;
```


SNS Topic triggered when an existing platform endpoint is changed from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L46">property failureFeedbackRoleArn</a>
</h3>

```typescript
public failureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L54">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L58">property platformCredential</a>
</h3>

```typescript
public platformCredential: pulumi.Output<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L62">property platformPrincipal</a>
</h3>

```typescript
public platformPrincipal: pulumi.Output<string | undefined>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L66">property successFeedbackRoleArn</a>
</h3>

```typescript
public successFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L70">property successFeedbackSampleRate</a>
</h3>

```typescript
public successFeedbackSampleRate: pulumi.Output<string | undefined>;
```


The percentage of success to sample (0-100)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SmsPreferences">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L10">class SmsPreferences</a>
</h2>

Provides a way to set SNS SMS preferences.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L46">constructor</a>
</h3>

```typescript
new SmsPreferences(name: string, args?: SmsPreferencesArgs, opts?: pulumi.CustomResourceOptions)
```


Create a SmsPreferences resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SmsPreferencesState): SmsPreferences
```


Get an existing SmsPreferences resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L26">property defaultSenderId</a>
</h3>

```typescript
public defaultSenderId: pulumi.Output<string | undefined>;
```


A string, such as your business brand, that is displayed as the sender on the receiving device.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L30">property defaultSmsType</a>
</h3>

```typescript
public defaultSmsType: pulumi.Output<string | undefined>;
```


The type of SMS message that you will send by default. Possible values are: Promotional, Transactional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L34">property deliveryStatusIamRoleArn</a>
</h3>

```typescript
public deliveryStatusIamRoleArn: pulumi.Output<string | undefined>;
```


The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L38">property deliveryStatusSuccessSamplingRate</a>
</h3>

```typescript
public deliveryStatusSuccessSamplingRate: pulumi.Output<string | undefined>;
```


The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L42">property monthlySpendLimit</a>
</h3>

```typescript
public monthlySpendLimit: pulumi.Output<string | undefined>;
```


The maximum amount in USD that you are willing to spend each month to send SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L46">property usageReportS3Bucket</a>
</h3>

```typescript
public usageReportS3Bucket: pulumi.Output<string | undefined>;
```


The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.

<h2 class="pdoc-module-header" id="Topic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L12">class Topic</a>
</h2>

Provides an SNS topic resource

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L100">constructor</a>
</h3>

```typescript
new Topic(name: string, args?: TopicArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Topic resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicState): Topic
```


Get an existing Topic resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L28">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
public applicationFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L32">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
public applicationSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L36">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
public applicationSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L40">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<ARN>;
```


The ARN of the SNS topic, as a more obvious property (clone of id)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L44">property deliveryPolicy</a>
</h3>

```typescript
public deliveryPolicy: pulumi.Output<string | undefined>;
```


The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L48">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string | undefined>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L52">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
public httpFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L56">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
public httpSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L60">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
public httpSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L64">property kmsMasterKeyId</a>
</h3>

```typescript
public kmsMasterKeyId: pulumi.Output<string | undefined>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L68">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
public lambdaFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L72">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
public lambdaSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L76">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
public lambdaSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L80">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L84">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L88">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L92">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
public sqsFailureFeedbackRoleArn: pulumi.Output<string | undefined>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L96">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
public sqsSuccessFeedbackRoleArn: pulumi.Output<string | undefined>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L100">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
public sqsSuccessFeedbackSampleRate: pulumi.Output<number | undefined>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L58">class TopicEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L64">constructor</a>
</h3>

```typescript
public new TopicEventSubscription(name: string, topic: topic.Topic, handler: TopicEventHandler, args: TopicEventSubscriptionArgs, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L227">property func</a>
</h3>

```typescript
public func: LambdaFunction;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L226">property permission</a>
</h3>

```typescript
public permission: permission.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L64">property subscription</a>
</h3>

```typescript
public subscription: topicSubscription.TopicSubscription;
```


The underlying sns object created for the subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L59">property topic</a>
</h3>

```typescript
public topic: topic.Topic;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L12">class TopicPolicy</a>
</h2>

Provides an SNS topic policy resource

~> **NOTE:** If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future terraform plans to differ. To avoid this problem, just specify the full ARN, e.g. `arn:aws:iam::123456789012:root`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L32">constructor</a>
</h3>

```typescript
new TopicPolicy(name: string, args: TopicPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicPolicyState): TopicPolicy
```


Get an existing TopicPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L32">property policy</a>
</h3>

```typescript
public policy: pulumi.Output<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L23">class TopicSubscription</a>
</h2>

  Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.
This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will
probably be SQS queues.

~> **NOTE:** If the SNS topic and SQS queue are in different AWS regions, it is important for the "aws_sns_topic_subscription" to use an AWS provider that is in the same region of the SNS topic. If the "aws_sns_topic_subscription" is using a provider with a different region than the SNS topic, terraform will fail to create the subscription.

~> **NOTE:** Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the "aws_sns_topic_subscription" to use the AWS provider of the account with the SQS queue. If "aws_sns_topic_subscription" is using a Provider with a different account than the SNS topic, terraform creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.

~> **NOTE:** If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L71">constructor</a>
</h3>

```typescript
new TopicSubscription(name: string, args: TopicSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TopicSubscription resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L32">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TopicSubscriptionState): TopicSubscription
```


Get an existing TopicSubscription resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L39">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the subscription stored as a more user-friendly property

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L43">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
public confirmationTimeoutInMinutes: pulumi.Output<number | undefined>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L47">property deliveryPolicy</a>
</h3>

```typescript
public deliveryPolicy: pulumi.Output<string | undefined>;
```


JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L51">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L55">property endpointAutoConfirms</a>
</h3>

```typescript
public endpointAutoConfirms: pulumi.Output<boolean | undefined>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L59">property filterPolicy</a>
</h3>

```typescript
public filterPolicy: pulumi.Output<string | undefined>;
```


JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L63">property protocol</a>
</h3>

```typescript
public protocol: pulumi.Output<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L67">property rawMessageDelivery</a>
</h3>

```typescript
public rawMessageDelivery: pulumi.Output<boolean | undefined>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L71">property topic</a>
</h3>

```typescript
public topic: pulumi.Output<Topic>;
```


The ARN of the SNS topic to subscribe to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getTopic">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L12">function getTopic</a>
</h2>

```typescript
getTopic(args: GetTopicArgs, opts?: pulumi.InvokeOptions): Promise<GetTopicResult>
```


Use this data source to get the ARN of a topic in AWS Simple Notification
Service (SNS). By using this data source, you can reference SNS topics
without having to hard code the ARNs as input.

<h2 class="pdoc-module-header" id="GetTopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L21">interface GetTopicArgs</a>
</h2>

A collection of arguments for invoking getTopic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The friendly name of the topic to match.

<h2 class="pdoc-module-header" id="GetTopicResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L31">interface GetTopicResult</a>
</h2>

A collection of values returned by getTopic.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```


Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/getTopic.ts#L39">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="PlatformApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L178">interface PlatformApplicationArgs</a>
</h2>

The set of arguments for constructing a PlatformApplication resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L182">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
eventDeliveryFailureTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L186">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
eventEndpointCreatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L190">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
eventEndpointDeletedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L194">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
eventEndpointUpdatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is changed from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L198">property failureFeedbackRoleArn</a>
</h3>

```typescript
failureFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L206">property platform</a>
</h3>

```typescript
platform: pulumi.Input<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L210">property platformCredential</a>
</h3>

```typescript
platformCredential: pulumi.Input<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L214">property platformPrincipal</a>
</h3>

```typescript
platformPrincipal?: pulumi.Input<string>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L218">property successFeedbackRoleArn</a>
</h3>

```typescript
successFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L222">property successFeedbackSampleRate</a>
</h3>

```typescript
successFeedbackSampleRate?: pulumi.Input<string>;
```


The percentage of success to sample (0-100)

<h2 class="pdoc-module-header" id="PlatformApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L124">interface PlatformApplicationState</a>
</h2>

Input properties used for looking up and filtering PlatformApplication resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L128">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L132">property eventDeliveryFailureTopicArn</a>
</h3>

```typescript
eventDeliveryFailureTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L136">property eventEndpointCreatedTopicArn</a>
</h3>

```typescript
eventEndpointCreatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when a new platform endpoint is added to your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L140">property eventEndpointDeletedTopicArn</a>
</h3>

```typescript
eventEndpointDeletedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L144">property eventEndpointUpdatedTopicArn</a>
</h3>

```typescript
eventEndpointUpdatedTopicArn?: pulumi.Input<string>;
```


SNS Topic triggered when an existing platform endpoint is changed from your platform application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L148">property failureFeedbackRoleArn</a>
</h3>

```typescript
failureFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive failure feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L152">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS platform application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L156">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```


The platform that the app is registered with. See [Platform][1] for supported platforms.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L160">property platformCredential</a>
</h3>

```typescript
platformCredential?: pulumi.Input<string>;
```


Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L164">property platformPrincipal</a>
</h3>

```typescript
platformPrincipal?: pulumi.Input<string>;
```


Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L168">property successFeedbackRoleArn</a>
</h3>

```typescript
successFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/platformApplication.ts#L172">property successFeedbackSampleRate</a>
</h3>

```typescript
successFeedbackSampleRate?: pulumi.Input<string>;
```


The percentage of success to sample (0-100)

<h2 class="pdoc-module-header" id="SNSItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L31">interface SNSItem</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L37">property Message</a>
</h3>

```typescript
Message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L38">property MessageAttributes</a>
</h3>

```typescript
MessageAttributes: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L36">property MessageId</a>
</h3>

```typescript
MessageId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L34">property Signature</a>
</h3>

```typescript
Signature: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L32">property SignatureVersion</a>
</h3>

```typescript
SignatureVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L35">property SigningCertUrl</a>
</h3>

```typescript
SigningCertUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L42">property Subject</a>
</h3>

```typescript
Subject: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L33">property Timestamp</a>
</h3>

```typescript
Timestamp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L41">property TopicArn</a>
</h3>

```typescript
TopicArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L39">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L40">property UnsubscribeUrl</a>
</h3>

```typescript
UnsubscribeUrl: string;
```

<h2 class="pdoc-module-header" id="SNSMessageAttribute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L45">interface SNSMessageAttribute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L46">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L47">property Value</a>
</h3>

```typescript
Value: string;
```

<h2 class="pdoc-module-header" id="SmsPreferencesArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L112">interface SmsPreferencesArgs</a>
</h2>

The set of arguments for constructing a SmsPreferences resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L116">property defaultSenderId</a>
</h3>

```typescript
defaultSenderId?: pulumi.Input<string>;
```


A string, such as your business brand, that is displayed as the sender on the receiving device.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L120">property defaultSmsType</a>
</h3>

```typescript
defaultSmsType?: pulumi.Input<string>;
```


The type of SMS message that you will send by default. Possible values are: Promotional, Transactional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L124">property deliveryStatusIamRoleArn</a>
</h3>

```typescript
deliveryStatusIamRoleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L128">property deliveryStatusSuccessSamplingRate</a>
</h3>

```typescript
deliveryStatusSuccessSamplingRate?: pulumi.Input<string>;
```


The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L132">property monthlySpendLimit</a>
</h3>

```typescript
monthlySpendLimit?: pulumi.Input<string>;
```


The maximum amount in USD that you are willing to spend each month to send SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L136">property usageReportS3Bucket</a>
</h3>

```typescript
usageReportS3Bucket?: pulumi.Input<string>;
```


The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.

<h2 class="pdoc-module-header" id="SmsPreferencesState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L82">interface SmsPreferencesState</a>
</h2>

Input properties used for looking up and filtering SmsPreferences resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L86">property defaultSenderId</a>
</h3>

```typescript
defaultSenderId?: pulumi.Input<string>;
```


A string, such as your business brand, that is displayed as the sender on the receiving device.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L90">property defaultSmsType</a>
</h3>

```typescript
defaultSmsType?: pulumi.Input<string>;
```


The type of SMS message that you will send by default. Possible values are: Promotional, Transactional

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L94">property deliveryStatusIamRoleArn</a>
</h3>

```typescript
deliveryStatusIamRoleArn?: pulumi.Input<string>;
```


The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L98">property deliveryStatusSuccessSamplingRate</a>
</h3>

```typescript
deliveryStatusSuccessSamplingRate?: pulumi.Input<string>;
```


The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L102">property monthlySpendLimit</a>
</h3>

```typescript
monthlySpendLimit?: pulumi.Input<string>;
```


The maximum amount in USD that you are willing to spend each month to send SMS messages.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/smsPreferences.ts#L106">property usageReportS3Bucket</a>
</h3>

```typescript
usageReportS3Bucket?: pulumi.Input<string>;
```


The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.

<h2 class="pdoc-module-header" id="TopicArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L244">interface TopicArgs</a>
</h2>

The set of arguments for constructing a Topic resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L248">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
applicationFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L252">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
applicationSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L256">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
applicationSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L260">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L264">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L268">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
httpFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L272">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
httpSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L276">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
httpSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L280">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L284">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
lambdaFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L288">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
lambdaSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L292">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
lambdaSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L296">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L300">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L304">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L308">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
sqsFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L312">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
sqsSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L316">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
sqsSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h2 class="pdoc-module-header" id="TopicEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L20">interface TopicEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L21">property Records</a>
</h3>

```typescript
Records: TopicRecord[];
```

<h2 class="pdoc-module-header" id="TopicPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L80">interface TopicPolicyArgs</a>
</h2>

The set of arguments for constructing a TopicPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L84">property arn</a>
</h3>

```typescript
arn: pulumi.Input<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L88">property policy</a>
</h3>

```typescript
policy: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h2 class="pdoc-module-header" id="TopicPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L66">interface TopicPolicyState</a>
</h2>

Input properties used for looking up and filtering TopicPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L70">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicPolicy.ts#L74">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h2 class="pdoc-module-header" id="TopicRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L24">interface TopicRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L27">property EventSource</a>
</h3>

```typescript
EventSource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L26">property EventSubscriptionArn</a>
</h3>

```typescript
EventSubscriptionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L25">property EventVersion</a>
</h3>

```typescript
EventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L28">property Sns</a>
</h3>

```typescript
Sns: SNSItem;
```

<h2 class="pdoc-module-header" id="TopicState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L162">interface TopicState</a>
</h2>

Input properties used for looking up and filtering Topic resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L166">property applicationFailureFeedbackRoleArn</a>
</h3>

```typescript
applicationFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L170">property applicationSuccessFeedbackRoleArn</a>
</h3>

```typescript
applicationSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L174">property applicationSuccessFeedbackSampleRate</a>
</h3>

```typescript
applicationSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L178">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<ARN>;
```


The ARN of the SNS topic, as a more obvious property (clone of id)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L182">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L186">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The display name for the SNS topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L190">property httpFailureFeedbackRoleArn</a>
</h3>

```typescript
httpFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L194">property httpSuccessFeedbackRoleArn</a>
</h3>

```typescript
httpSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L198">property httpSuccessFeedbackSampleRate</a>
</h3>

```typescript
httpSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L202">property kmsMasterKeyId</a>
</h3>

```typescript
kmsMasterKeyId?: pulumi.Input<string>;
```


The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L206">property lambdaFailureFeedbackRoleArn</a>
</h3>

```typescript
lambdaFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L210">property lambdaSuccessFeedbackRoleArn</a>
</h3>

```typescript
lambdaSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L214">property lambdaSuccessFeedbackSampleRate</a>
</h3>

```typescript
lambdaSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L218">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The friendly name for the SNS topic. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L222">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The friendly name for the SNS topic. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L226">property policy</a>
</h3>

```typescript
policy?: pulumi.Input<string>;
```


The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L230">property sqsFailureFeedbackRoleArn</a>
</h3>

```typescript
sqsFailureFeedbackRoleArn?: pulumi.Input<string>;
```


IAM role for failure feedback

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L234">property sqsSuccessFeedbackRoleArn</a>
</h3>

```typescript
sqsSuccessFeedbackRoleArn?: pulumi.Input<string>;
```


The IAM role permitted to receive success feedback for this topic

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topic.ts#L238">property sqsSuccessFeedbackSampleRate</a>
</h3>

```typescript
sqsSuccessFeedbackSampleRate?: pulumi.Input<number>;
```


Percentage of success to sample

<h2 class="pdoc-module-header" id="TopicSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L164">interface TopicSubscriptionArgs</a>
</h2>

The set of arguments for constructing a TopicSubscription resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L168">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
confirmationTimeoutInMinutes?: pulumi.Input<number>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L172">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L176">property endpoint</a>
</h3>

```typescript
endpoint: pulumi.Input<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L180">property endpointAutoConfirms</a>
</h3>

```typescript
endpointAutoConfirms?: pulumi.Input<boolean>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L184">property filterPolicy</a>
</h3>

```typescript
filterPolicy?: pulumi.Input<string>;
```


JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L188">property protocol</a>
</h3>

```typescript
protocol: pulumi.Input<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L192">property rawMessageDelivery</a>
</h3>

```typescript
rawMessageDelivery?: pulumi.Input<boolean>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L196">property topic</a>
</h3>

```typescript
topic: pulumi.Input<Topic>;
```


The ARN of the SNS topic to subscribe to

<h2 class="pdoc-module-header" id="TopicSubscriptionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L122">interface TopicSubscriptionState</a>
</h2>

Input properties used for looking up and filtering TopicSubscription resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L126">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the subscription stored as a more user-friendly property

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L130">property confirmationTimeoutInMinutes</a>
</h3>

```typescript
confirmationTimeoutInMinutes?: pulumi.Input<number>;
```


Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L134">property deliveryPolicy</a>
</h3>

```typescript
deliveryPolicy?: pulumi.Input<string>;
```


JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L138">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint to send data to, the contents will vary with the protocol. (see below for more information)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L142">property endpointAutoConfirms</a>
</h3>

```typescript
endpointAutoConfirms?: pulumi.Input<boolean>;
```


Boolean indicating whether the end point is capable of [auto confirming subscription](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare) e.g., PagerDuty (default is false)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L146">property filterPolicy</a>
</h3>

```typescript
filterPolicy?: pulumi.Input<string>;
```


JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the [SNS docs](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html) for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L150">property protocol</a>
</h3>

```typescript
protocol?: pulumi.Input<string>;
```


The protocol to use. The possible values for this are: `sqs`, `sms`, `lambda`, `application`. (`http` or `https` are partially supported, see below) (`email` is option but unsupported, see below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L154">property rawMessageDelivery</a>
</h3>

```typescript
rawMessageDelivery?: pulumi.Input<boolean>;
```


Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/topicSubscription.ts#L158">property topic</a>
</h3>

```typescript
topic?: pulumi.Input<Topic>;
```


The ARN of the SNS topic to subscribe to

<h2 class="pdoc-module-header" id="TopicEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L50">type TopicEventHandler</a>
</h2>

```typescript
type TopicEventHandler = lambda.EventHandler<TopicEvent, void>;
```

<h2 class="pdoc-module-header" id="TopicEventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/sns/snsMixins.ts#L56">type TopicEventSubscriptionArgs</a>
</h2>

```typescript
type TopicEventSubscriptionArgs = { ... };
```


Arguments to control the topic subscription.  Currently empty, but still defined in case of
future need.

