
---
title: "BucketNotification"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Manages a S3 Bucket Notification Configuration. For additional information, see the [Configuring S3 Event Notifications section in the Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html).

> **NOTE:** S3 Buckets only support a single notification configuration. Declaring multiple `aws.s3.BucketNotification` resources to the same S3 Bucket will cause a perpetual difference in configuration. See the example "Trigger multiple Lambda functions" for an option.

## Example Usage

### Add notification configuration to SNS Topic

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {});
const topic = new aws.sns.Topic("topic", {
    policy: pulumi.interpolate`{
    "Version":"2012-10-17",
    "Statement":[{
        "Effect": "Allow",
        "Principal": {"AWS":"*"},
        "Action": "SNS:Publish",
        "Resource": "arn:aws:sns:*:*:s3-event-notification-topic",
        "Condition":{
            "ArnLike":{"aws:SourceArn":"${bucket.arn}"}
        }
    }]
}
`,
});
const bucketNotification = new aws.s3.BucketNotification("bucket_notification", {
    bucket: bucket.id,
    topics: [{
        events: ["s3:ObjectCreated:*"],
        filterSuffix: ".log",
        topicArn: topic.arn,
    }],
});
```

### Add notification configuration to SQS Queue

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {});
const queue = new aws.sqs.Queue("queue", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "sqs:SendMessage",
	  "Resource": "arn:aws:sqs:*:*:s3-event-notification-queue",
      "Condition": {
        "ArnEquals": { "aws:SourceArn": "${bucket.arn}" }
      }
    }
  ]
}
`,
});
const bucketNotification = new aws.s3.BucketNotification("bucket_notification", {
    bucket: bucket.id,
    queues: [{
        events: ["s3:ObjectCreated:*"],
        filterSuffix: ".log",
        queueArn: queue.arn,
    }],
});
```

### Add multiple notification configurations to SQS Queue

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket", {});
const queue = new aws.sqs.Queue("queue", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "sqs:SendMessage",
	  "Resource": "arn:aws:sqs:*:*:s3-event-notification-queue",
      "Condition": {
        "ArnEquals": { "aws:SourceArn": "${bucket.arn}" }
      }
    }
  ]
}
`,
});
const bucketNotification = new aws.s3.BucketNotification("bucket_notification", {
    bucket: bucket.id,
    queues: [
        {
            events: ["s3:ObjectCreated:*"],
            filterPrefix: "images/",
            id: "image-upload-event",
            queueArn: queue.arn,
        },
        {
            events: ["s3:ObjectCreated:*"],
            filterPrefix: "videos/",
            id: "video-upload-event",
            queueArn: queue.arn,
        },
    ],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_notification.html.markdown.



## Create a BucketNotification Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketNotification">BucketNotification</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#BucketNotificationArgs">BucketNotificationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BucketNotification</span><span class="p">(resource_name, id, opts=None, </span>bucket=None<span class="p">, </span>lambda_functions=None<span class="p">, </span>queues=None<span class="p">, </span>topics=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBucketNotification<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationArgs">BucketNotificationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotification">BucketNotification</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotification.html">BucketNotification</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationArgs.html">BucketNotificationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a BucketNotification resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Queue<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Topic<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">[]s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">[]s3.<wbr>Bucket<wbr>Notification<wbr>Queue</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">[]s3.<wbr>Bucket<wbr>Notification<wbr>Topic</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">s3.<wbr>Bucket<wbr>Notification<wbr>Queue[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">s3.<wbr>Bucket<wbr>Notification<wbr>Topic[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">list[bucket_<wbr>notification_<wbr>lambda_<wbr>function]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">list[bucket_<wbr>notification_<wbr>queue]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">list[bucket_<wbr>notification_<wbr>topic]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## BucketNotification Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Queue&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Topic&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">[]s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function</a></code>
            </td>
            <td class="align-top">{{% md %}} Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">[]s3.<wbr>Bucket<wbr>Notification<wbr>Queue</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">[]s3.<wbr>Bucket<wbr>Notification<wbr>Topic</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">s3.<wbr>Bucket<wbr>Notification<wbr>Queue[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">s3.<wbr>Bucket<wbr>Notification<wbr>Topic[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">list[bucket_<wbr>notification_<wbr>lambda_<wbr>function]</a></code>
            </td>
            <td class="align-top">{{% md %}} Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">list[bucket_<wbr>notification_<wbr>queue]</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">list[bucket_<wbr>notification_<wbr>topic]</a></code>
            </td>
            <td class="align-top">{{% md %}} The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing BucketNotification Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BucketNotificationState, opts?: pulumi.CustomResourceOptions): BucketNotification;
```

```python
def get(resource_name, id, opts=None, bucket=None, lambda_<wbr>functions=None, queues=None, topics=None)
```

```go
func GetBucketNotification(ctx *pulumi.Context, name string, id pulumi.IDInput, state *BucketNotificationState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static BucketNotification Get(string name, Input<string> id, BucketNotificationState? state = null, CustomResourceOptions? options = null);
```

Get an existing BucketNotification resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Queue<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">List&lt;Pulumi.<wbr>Aws.<wbr>S3.<wbr>Bucket<wbr>Notification<wbr>Topic<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">[]s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">[]s3.<wbr>Bucket<wbr>Notification<wbr>Queue</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">[]s3.<wbr>Bucket<wbr>Notification<wbr>Topic</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">s3.<wbr>Bucket<wbr>Notification<wbr>Lambda<wbr>Function[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">s3.<wbr>Bucket<wbr>Notification<wbr>Queue[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">s3.<wbr>Bucket<wbr>Notification<wbr>Topic[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket to put notification configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>functions</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationlambdafunction">list[bucket_<wbr>notification_<wbr>lambda_<wbr>function]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure notifications to a Lambda Function (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationqueue">list[bucket_<wbr>notification_<wbr>queue]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SQS Queue (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topics</td>
            <td class="align-top">
                
                <code><a href="#bucketnotificationtopic">list[bucket_<wbr>notification_<wbr>topic]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The notification configuration to SNS Topic (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### BucketNotificationLambdaFunction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketNotificationLambdaFunction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketNotificationLambdaFunction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationLambdaFunctionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationLambdaFunctionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationLambdaFunctionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationLambdaFunction.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies Amazon Lambda function ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies Amazon Lambda function ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies Amazon Lambda function ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>suffix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>function_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies Amazon Lambda function ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketNotificationQueue
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketNotificationQueue">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketNotificationQueue">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationQueueArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationQueueOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationQueueArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationQueue.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queue<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SQS queue ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queue<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SQS queue ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queue<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SQS queue ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>suffix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queue_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SQS queue ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BucketNotificationTopic
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BucketNotificationTopic">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BucketNotificationTopic">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationTopicArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#BucketNotificationTopicOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationTopicArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.BucketNotificationTopic.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SNS topic ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SNS topic ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SNS topic ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">events</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name prefix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filter_<wbr>suffix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies object key name suffix.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies unique identifier for each of the notification configurations.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies Amazon SNS topic ARN.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







