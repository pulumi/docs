---
title: Package @pulumi/aws-serverless
---


Node.js:

```javascript
var aws-serverless = require("@pulumi/aws-serverless");
```

ES6 modules:

```typescript
import * as aws-serverless from "@pulumi/aws-serverless";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#BucketEventSubscription">class BucketEventSubscription</a>
* <a href="#TopicEventSubscription">class TopicEventSubscription</a>
* <a href="#defaultComputePolicies">const defaultComputePolicies</a>
* <a href="#createLambdaFunction">function createLambdaFunction</a>
* <a href="#mapObject">function mapObject</a>
* <a href="#onDelete">function onDelete</a>
* <a href="#onEvent">function onEvent</a>
* <a href="#onPut">function onPut</a>
* <a href="#outputFromObject">function outputFromObject</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#subscribe">function subscribe</a>
* <a href="#BucketEvent">interface BucketEvent</a>
* <a href="#BucketRecord">interface BucketRecord</a>
* <a href="#BucketSubscriptionArgs">interface BucketSubscriptionArgs</a>
* <a href="#SNSItem">interface SNSItem</a>
* <a href="#SNSMessageAttribute">interface SNSMessageAttribute</a>
* <a href="#SimpleBucketSubscriptionArgs">interface SimpleBucketSubscriptionArgs</a>
* <a href="#SubscriptionInfo">interface SubscriptionInfo</a>
* <a href="#TopicEvent">interface TopicEvent</a>
* <a href="#TopicRecord">interface TopicRecord</a>
* <a href="#bucketSubscriptionInfos">let bucketSubscriptionInfos</a>
* <a href="#BucketDeleteArgs">type BucketDeleteArgs</a>
* <a href="#BucketEventHandler">type BucketEventHandler</a>
* <a href="#BucketPutArgs">type BucketPutArgs</a>
* <a href="#Callback">type Callback</a>
* <a href="#Diff">type Diff</a>
* <a href="#Handler">type Handler</a>
* <a href="#Omit">type Omit</a>
* <a href="#TopicEventHandler">type TopicEventHandler</a>
* <a href="#TopicSubscriptionArgs">type TopicSubscriptionArgs</a>

<a href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts">bucket.ts</a> <a href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/function.ts">function.ts</a> <a href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts">topic.ts</a> <a href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts">utils.ts</a> 


<h2 class="pdoc-module-header" id="BucketEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L163">class BucketEventSubscription</a>
</h2>

A component corresponding to a single underlying aws.s3.BucketNotification created for a bucket.
Note: due to the AWS requirement that all notifications for a bucket be defined at once, the
actual aws.s3.BucketNotification instances will only be created once the pulumi program runs to
completion and all subscriptions have been heard about.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L163">constructor</a>
</h3>

```typescript
public new BucketEventSubscription(name: string, bucket: s3.Bucket, func: lambda.Function, args: BucketSubscriptionArgs, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L100">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/subscription.ts#L23">property func</a>
</h3>

```typescript
public func: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/subscription.ts#L22">property permission</a>
</h3>

```typescript
public permission: lambda.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TopicEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L72">class TopicEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L76">constructor</a>
</h3>

```typescript
public new TopicEventSubscription(name: string, topic: sns.Topic, func: lambda.Function, args: TopicSubscriptionArgs, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L100">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/subscription.ts#L23">property func</a>
</h3>

```typescript
public func: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/subscription.ts#L22">property permission</a>
</h3>

```typescript
public permission: lambda.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L76">property subscription</a>
</h3>

```typescript
public subscription: sns.TopicSubscription;
```


The underlying sns object created for the subscription.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="defaultComputePolicies">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L127">const defaultComputePolicies</a>
</h2>

```typescript
const defaultComputePolicies: string[] =  [
    aws.iam.AWSLambdaFullAccess,                 // Provides wide access to "serverless" services (Dynamo, S3, etc.)
    aws.iam.AmazonEC2ContainerServiceFullAccess, // Required for lambda compute to be able to run Tasks
];
```

<h2 class="pdoc-module-header" id="createLambdaFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/function.ts#L38">function createLambdaFunction</a>
</h2>

```typescript
createLambdaFunction<E,R>(name: string, handler: Handler<E, R>, opts?: ResourceOptions): aws.lambda.Function
```

<h2 class="pdoc-module-header" id="mapObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts#L27">function mapObject</a>
</h2>

```typescript
mapObject<T,U>(obj: Record<string, T>, func: { ... }): Record<string, U>
```

<h2 class="pdoc-module-header" id="onDelete">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L113">function onDelete</a>
</h2>

```typescript
onDelete(name: string, bucket: s3.Bucket, handler: BucketEventHandler, args?: BucketDeleteArgs, opts?: pulumi.ResourceOptions): BucketEventSubscription
```

<h2 class="pdoc-module-header" id="onEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L138">function onEvent</a>
</h2>

```typescript
onEvent(name: string, bucket: s3.Bucket, handler: BucketEventHandler, args: BucketSubscriptionArgs, opts?: pulumi.ResourceOptions): BucketEventSubscription
```


Creates a new subscription to the given bucket using the lambda provided, along with optional
options to control the behavior of the subscription.  This function should be used when full
control over the subscription is wanted, and other helpers (like onPut/onDelete) are not
sufficient.

<h2 class="pdoc-module-header" id="onPut">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L99">function onPut</a>
</h2>

```typescript
onPut(name: string, bucket: s3.Bucket, handler: BucketEventHandler, args?: BucketPutArgs, opts?: pulumi.ResourceOptions): BucketEventSubscription
```

<h2 class="pdoc-module-header" id="outputFromObject">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts#L37">function outputFromObject</a>
</h2>

```typescript
outputFromObject<T,U>(obj: Record<string, T>, func: { ... }): pulumi.Output<Record<string, U>>
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts#L19">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="subscribe">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L63">function subscribe</a>
</h2>

```typescript
subscribe(name: string, topic: sns.Topic, handler: TopicEventHandler, args?: TopicSubscriptionArgs, opts?: pulumi.ResourceOptions): TopicEventSubscription
```


Creates a new subscription to the given topic using the lambda provided, along with optional
options to control the behavior of the subscription.

<h2 class="pdoc-module-header" id="BucketEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L55">interface BucketEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L56">property Records</a>
</h3>

```typescript
Records?: BucketRecord[];
```

<h2 class="pdoc-module-header" id="BucketRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L59">interface BucketRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L62">property awsRegion</a>
</h3>

```typescript
awsRegion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L64">property eventName</a>
</h3>

```typescript
eventName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L61">property eventSource</a>
</h3>

```typescript
eventSource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L63">property eventTime</a>
</h3>

```typescript
eventTime: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L60">property eventVersion</a>
</h3>

```typescript
eventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L68">property requestParameters</a>
</h3>

```typescript
requestParameters: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L71">property responseElements</a>
</h3>

```typescript
responseElements: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L75">property s3</a>
</h3>

```typescript
s3: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L65">property userIdentity</a>
</h3>

```typescript
userIdentity: { ... };
```

<h2 class="pdoc-module-header" id="BucketSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L33">interface BucketSubscriptionArgs</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L37">property events</a>
</h3>

```typescript
events: string[];
```


Events to subscribe to. For example: "s3:ObjectCreated:*".  Cannot be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L29">property filterPrefix</a>
</h3>

```typescript
filterPrefix?: undefined | string;
```


An optional prefix or suffix to filter down notifications.  See
aws.s3.BucketNotification.lambdaFunctions for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L30">property filterSuffix</a>
</h3>

```typescript
filterSuffix?: undefined | string;
```

<h2 class="pdoc-module-header" id="SNSItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L32">interface SNSItem</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L38">property Message</a>
</h3>

```typescript
Message: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L39">property MessageAttributes</a>
</h3>

```typescript
MessageAttributes: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L37">property MessageId</a>
</h3>

```typescript
MessageId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L35">property Signature</a>
</h3>

```typescript
Signature: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L33">property SignatureVersion</a>
</h3>

```typescript
SignatureVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L36">property SigningCertUrl</a>
</h3>

```typescript
SigningCertUrl: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L43">property Subject</a>
</h3>

```typescript
Subject: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L34">property Timestamp</a>
</h3>

```typescript
Timestamp: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L42">property TopicArn</a>
</h3>

```typescript
TopicArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L40">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L41">property UnsubscribeUrl</a>
</h3>

```typescript
UnsubscribeUrl: string;
```

<h2 class="pdoc-module-header" id="SNSMessageAttribute">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L46">interface SNSMessageAttribute</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L47">property Type</a>
</h3>

```typescript
Type: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L48">property Value</a>
</h3>

```typescript
Value: string;
```

<h2 class="pdoc-module-header" id="SimpleBucketSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L24">interface SimpleBucketSubscriptionArgs</a>
</h2>

Arguments to help customize a notification subscription for a bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L29">property filterPrefix</a>
</h3>

```typescript
filterPrefix?: undefined | string;
```


An optional prefix or suffix to filter down notifications.  See
aws.s3.BucketNotification.lambdaFunctions for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L30">property filterSuffix</a>
</h3>

```typescript
filterSuffix?: undefined | string;
```

<h2 class="pdoc-module-header" id="SubscriptionInfo">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L146">interface SubscriptionInfo</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L148">property events</a>
</h3>

```typescript
events: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L149">property filterPrefix</a>
</h3>

```typescript
filterPrefix?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L150">property filterSuffix</a>
</h3>

```typescript
filterSuffix?: undefined | string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L151">property lambdaFunctionArn</a>
</h3>

```typescript
lambdaFunctionArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L147">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L152">property permission</a>
</h3>

```typescript
permission: aws.lambda.Permission;
```

<h2 class="pdoc-module-header" id="TopicEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L21">interface TopicEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L22">property Records</a>
</h3>

```typescript
Records: TopicRecord[];
```

<h2 class="pdoc-module-header" id="TopicRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L25">interface TopicRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L28">property EventSource</a>
</h3>

```typescript
EventSource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L27">property EventSubscriptionArn</a>
</h3>

```typescript
EventSubscriptionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L26">property EventVersion</a>
</h3>

```typescript
EventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L29">property Sns</a>
</h3>

```typescript
Sns: SNSItem;
```

<h2 class="pdoc-module-header" id="bucketSubscriptionInfos">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L155">let bucketSubscriptionInfos</a>
</h2>

```typescript
let bucketSubscriptionInfos: Map<Bucket, SubscriptionInfo[]> =  new Map<s3.Bucket, SubscriptionInfo[]>();
```

<h2 class="pdoc-module-header" id="BucketDeleteArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L52">type BucketDeleteArgs</a>
</h2>

```typescript
type BucketDeleteArgs = SimpleBucketSubscriptionArgs;
```


Arguments to specifically control a subscription to 'delete' notifications on a bucket.
Specifically, 'events' should not be provided as they will be assumed to be "s3:ObjectRemoved:*".
If different events are desired, the 'subscribe' function should be used instead.

<h2 class="pdoc-module-header" id="BucketEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L97">type BucketEventHandler</a>
</h2>

```typescript
type BucketEventHandler = Handler<BucketEvent, void>;
```

<h2 class="pdoc-module-header" id="BucketPutArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/bucket.ts#L45">type BucketPutArgs</a>
</h2>

```typescript
type BucketPutArgs = SimpleBucketSubscriptionArgs;
```


Arguments to specifically control a subscription to 'put' notifications on a bucket.
Specifically, 'events' should not be provided as they will be assumed to be "s3:ObjectCreated:*".
If different events are desired, the 'subscribe' function should be used instead.

<h2 class="pdoc-module-header" id="Callback">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/function.ts#L26">type Callback</a>
</h2>

```typescript
type Callback = { ... };
```


A synchronous or asynchronous function that can be converted into an AWS lambda.  Async callbacks
are only supported with an AWS lambda runtime of 8.10 or higher.  On those runtimes a Promise can
be returned, 'callback' parameter can be ignored, and AWS will appropriately handle things. For
AWS lambda pre-8.10, a synchronous function must be provided.  The synchronous function should
return nothing, and should instead invoke 'callback' when complete.

<h2 class="pdoc-module-header" id="Diff">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts#L44">type Diff</a>
</h2>

```typescript
type Diff = ({ [P in T]: P; } & { [P in U]: never; } & { [x: string]: never; })[T];
```

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/function.ts#L32">type Handler</a>
</h2>

```typescript
type Handler = Callback<E, R> | aws.lambda.Function;
```


Handler represents the appropriate type for functions that can take either an AWS lambda function
instance, or a JS function object that will then be used to create the AWS lambda function.

<h2 class="pdoc-module-header" id="Omit">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/utils.ts#L45">type Omit</a>
</h2>

```typescript
type Omit = Pick<T, Diff<keyof T, K>>;
```

<h2 class="pdoc-module-header" id="TopicEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L51">type TopicEventHandler</a>
</h2>

```typescript
type TopicEventHandler = Handler<TopicEvent, void>;
```

<h2 class="pdoc-module-header" id="TopicSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs/topic.ts#L57">type TopicSubscriptionArgs</a>
</h2>

```typescript
type TopicSubscriptionArgs = { ... };
```


Arguments to control the topic subscription.  Currently empty, but still defined in case of
future need.

