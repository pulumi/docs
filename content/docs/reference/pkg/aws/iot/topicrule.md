
---
title: "TopicRule"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const mytopic = new aws.sns.Topic("mytopic", {});
const role = new aws.iam.Role("role", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "iot.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
`,
});
const rule = new aws.iot.TopicRule("rule", {
    description: "Example rule",
    enabled: true,
    sns: {
        messageFormat: "RAW",
        roleArn: role.arn,
        targetArn: mytopic.arn,
    },
    sql: "SELECT * FROM 'topic/test'",
    sqlVersion: "2015-10-08",
});
const iamPolicyForLambda = new aws.iam.RolePolicy("iam_policy_for_lambda", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "sns:Publish"
        ],
        "Resource": "${mytopic.arn}"
    }
  ]
}
`,
    role: role.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_topic_rule.html.markdown.



## Create a TopicRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iot/#TopicRule">TopicRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iot/#TopicRuleArgs">TopicRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">TopicRule</span><span class="p">(resource_name, opts=None, </span>cloudwatch_alarm=None<span class="p">, </span>cloudwatch_metric=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb=None<span class="p">, </span>elasticsearch=None<span class="p">, </span>enabled=None<span class="p">, </span>firehose=None<span class="p">, </span>kinesis=None<span class="p">, </span>lambda_=None<span class="p">, </span>name=None<span class="p">, </span>republish=None<span class="p">, </span>s3=None<span class="p">, </span>sns=None<span class="p">, </span>sql=None<span class="p">, </span>sql_version=None<span class="p">, </span>sqs=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTopicRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleArgs">TopicRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRule">TopicRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRule.html">TopicRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleArgs.html">TopicRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a TopicRule resource with the given unique name, arguments, and options.

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
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Firehose<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Kinesis<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Lambda<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Republish<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>S3Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sns<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sqs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">*iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">*iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">*iot.<wbr>Topic<wbr>Rule<wbr>Firehose</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">*iot.<wbr>Topic<wbr>Rule<wbr>Kinesis</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">*iot.<wbr>Topic<wbr>Rule<wbr>Lambda</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">*iot.<wbr>Topic<wbr>Rule<wbr>Republish</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">*iot.<wbr>Topic<wbr>Rule<wbr>S3</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">*iot.<wbr>Topic<wbr>Rule<wbr>Sns</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">*iot.<wbr>Topic<wbr>Rule<wbr>Sqs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">iot.<wbr>Topic<wbr>Rule<wbr>Firehose?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">iot.<wbr>Topic<wbr>Rule<wbr>Kinesis?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">iot.<wbr>Topic<wbr>Rule<wbr>Lambda?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">iot.<wbr>Topic<wbr>Rule<wbr>Republish?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">iot.<wbr>Topic<wbr>Rule<wbr>S3?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">iot.<wbr>Topic<wbr>Rule<wbr>Sns?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">iot.<wbr>Topic<wbr>Rule<wbr>Sqs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">cloudwatch_<wbr>alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Dict[Topic<wbr>Rule<wbr>Dynamodb]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Dict[Topic<wbr>Rule<wbr>Elasticsearch]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Dict[Topic<wbr>Rule<wbr>Firehose]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Dict[Topic<wbr>Rule<wbr>Kinesis]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Dict[Topic<wbr>Rule<wbr>Lambda]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Dict[Topic<wbr>Rule<wbr>Republish]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Dict[Topic<wbr>Rule<wbr>S3]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Dict[Topic<wbr>Rule<wbr>Sns]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Dict[Topic<wbr>Rule<wbr>Sqs]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## TopicRule Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Firehose?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Kinesis?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Lambda?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Republish?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>S3?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sns?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sqs?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">*iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">*iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">*iot.<wbr>Topic<wbr>Rule<wbr>Firehose</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">*iot.<wbr>Topic<wbr>Rule<wbr>Kinesis</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">*iot.<wbr>Topic<wbr>Rule<wbr>Lambda</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">*iot.<wbr>Topic<wbr>Rule<wbr>Republish</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">*iot.<wbr>Topic<wbr>Rule<wbr>S3</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">*iot.<wbr>Topic<wbr>Rule<wbr>Sns</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">*iot.<wbr>Topic<wbr>Rule<wbr>Sqs</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">iot.<wbr>Topic<wbr>Rule<wbr>Firehose?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">iot.<wbr>Topic<wbr>Rule<wbr>Kinesis?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">iot.<wbr>Topic<wbr>Rule<wbr>Lambda?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">iot.<wbr>Topic<wbr>Rule<wbr>Republish?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">iot.<wbr>Topic<wbr>Rule<wbr>S3?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">iot.<wbr>Topic<wbr>Rule<wbr>Sns?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">iot.<wbr>Topic<wbr>Rule<wbr>Sqs?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Dict[Topic<wbr>Rule<wbr>Dynamodb]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Dict[Topic<wbr>Rule<wbr>Elasticsearch]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Dict[Topic<wbr>Rule<wbr>Firehose]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Dict[Topic<wbr>Rule<wbr>Kinesis]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Dict[Topic<wbr>Rule<wbr>Lambda]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Dict[Topic<wbr>Rule<wbr>Republish]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Dict[Topic<wbr>Rule<wbr>S3]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Dict[Topic<wbr>Rule<wbr>Sns]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Dict[Topic<wbr>Rule<wbr>Sqs]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing TopicRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iot/#TopicRuleState">TopicRuleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/iot/#TopicRule">TopicRule</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>cloudwatch_alarm=None<span class="p">, </span>cloudwatch_metric=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb=None<span class="p">, </span>elasticsearch=None<span class="p">, </span>enabled=None<span class="p">, </span>firehose=None<span class="p">, </span>kinesis=None<span class="p">, </span>lambda_=None<span class="p">, </span>name=None<span class="p">, </span>republish=None<span class="p">, </span>s3=None<span class="p">, </span>sns=None<span class="p">, </span>sql=None<span class="p">, </span>sql_version=None<span class="p">, </span>sqs=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTopicRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleState">TopicRuleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRule">TopicRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRule.html">TopicRule</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleState.html">TopicRuleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing TopicRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Firehose<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Kinesis<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Lambda<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Republish<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>S3Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sns<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Pulumi.<wbr>Aws.<wbr>Iot.<wbr>Topic<wbr>Rule<wbr>Sqs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">*iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">*iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">*iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">*iot.<wbr>Topic<wbr>Rule<wbr>Firehose</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">*iot.<wbr>Topic<wbr>Rule<wbr>Kinesis</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">*iot.<wbr>Topic<wbr>Rule<wbr>Lambda</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">*iot.<wbr>Topic<wbr>Rule<wbr>Republish</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">*iot.<wbr>Topic<wbr>Rule<wbr>S3</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">*iot.<wbr>Topic<wbr>Rule<wbr>Sns</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sql<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">*iot.<wbr>Topic<wbr>Rule<wbr>Sqs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch<wbr>Metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">iot.<wbr>Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">iot.<wbr>Topic<wbr>Rule<wbr>Dynamodb?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">iot.<wbr>Topic<wbr>Rule<wbr>Elasticsearch?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">iot.<wbr>Topic<wbr>Rule<wbr>Firehose?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">iot.<wbr>Topic<wbr>Rule<wbr>Kinesis?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">iot.<wbr>Topic<wbr>Rule<wbr>Lambda?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">iot.<wbr>Topic<wbr>Rule<wbr>Republish?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">iot.<wbr>Topic<wbr>Rule<wbr>S3?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">iot.<wbr>Topic<wbr>Rule<wbr>Sns?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">iot.<wbr>Topic<wbr>Rule<wbr>Sqs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the topic rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>alarm</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchalarm">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Alarm]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cloudwatch_<wbr>metric</td>
            <td class="align-top">
                
                <code><a href="#topicrulecloudwatchmetric">Dict[Topic<wbr>Rule<wbr>Cloudwatch<wbr>Metric]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb</td>
            <td class="align-top">
                
                <code><a href="#topicruledynamodb">Dict[Topic<wbr>Rule<wbr>Dynamodb]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch</td>
            <td class="align-top">
                
                <code><a href="#topicruleelasticsearch">Dict[Topic<wbr>Rule<wbr>Elasticsearch]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the rule is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">firehose</td>
            <td class="align-top">
                
                <code><a href="#topicrulefirehose">Dict[Topic<wbr>Rule<wbr>Firehose]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis</td>
            <td class="align-top">
                
                <code><a href="#topicrulekinesis">Dict[Topic<wbr>Rule<wbr>Kinesis]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_</td>
            <td class="align-top">
                
                <code><a href="#topicrulelambda">Dict[Topic<wbr>Rule<wbr>Lambda]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">republish</td>
            <td class="align-top">
                
                <code><a href="#topicrulerepublish">Dict[Topic<wbr>Rule<wbr>Republish]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3</td>
            <td class="align-top">
                
                <code><a href="#topicrules3">Dict[Topic<wbr>Rule<wbr>S3]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sns</td>
            <td class="align-top">
                
                <code><a href="#topicrulesns">Dict[Topic<wbr>Rule<wbr>Sns]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sql_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the SQL rules engine to use when evaluating the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs</td>
            <td class="align-top">
                
                <code><a href="#topicrulesqs">Dict[Topic<wbr>Rule<wbr>Sqs]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### TopicRuleCloudwatchAlarm
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleCloudwatchAlarm">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleCloudwatchAlarm">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleCloudwatchAlarmArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleCloudwatchAlarmOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleCloudwatchAlarmArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleCloudwatchAlarm.html">output</a> API doc for this type.
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
            <td class="align-top">Alarm<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch alarm name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Reason</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The reason for the alarm change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
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
            <td class="align-top">Alarm<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch alarm name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Reason</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The reason for the alarm change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
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
            <td class="align-top">alarm<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch alarm name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state<wbr>Reason</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The reason for the alarm change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
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
            <td class="align-top">alarm<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch alarm name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state<wbr>Reason</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The reason for the alarm change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleCloudwatchMetric
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleCloudwatchMetric">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleCloudwatchMetric">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleCloudwatchMetricArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleCloudwatchMetricOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleCloudwatchMetricArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleCloudwatchMetric.html">output</a> API doc for this type.
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
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric namespace name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Timestamp</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric namespace name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Timestamp</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric namespace name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Timestamp</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Unit</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">metric_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Namespace</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric namespace name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Timestamp</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An optional Unix timestamp (http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Unit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric unit (supported units can be found here: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The CloudWatch metric value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleDynamodb
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleDynamodb">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleDynamodb">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleDynamodbArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleDynamodbOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleDynamodbArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleDynamodb.html">output</a> API doc for this type.
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
            <td class="align-top">Hash<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hash key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload<wbr>Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action payload.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the DynamoDB table.
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
            <td class="align-top">Hash<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hash key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload<wbr>Field</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action payload.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the DynamoDB table.
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
            <td class="align-top">hash<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hash key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload<wbr>Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action payload.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the DynamoDB table.
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
            <td class="align-top">hash<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hash key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The hash key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload<wbr>Field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action payload.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key type. Valid values are &#34;STRING&#34; or &#34;NUMBER&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key<wbr>Value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The range key value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the DynamoDB table.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleElasticsearch
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleElasticsearch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleElasticsearch">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleElasticsearchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleElasticsearchOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleElasticsearchArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleElasticsearch.html">output</a> API doc for this type.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The endpoint of your Elasticsearch domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier for the document you are storing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index where you want to store your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of document you are storing.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The endpoint of your Elasticsearch domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier for the document you are storing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Index</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index where you want to store your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of document you are storing.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The endpoint of your Elasticsearch domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier for the document you are storing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index where you want to store your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of document you are storing.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The endpoint of your Elasticsearch domain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The unique identifier for the document you are storing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">index</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Elasticsearch index where you want to store your data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of document you are storing.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleFirehose
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleFirehose">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleFirehose">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleFirehoseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleFirehoseOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleFirehoseArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleFirehose.html">output</a> API doc for this type.
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
            <td class="align-top">Delivery<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The delivery stream name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Separator</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A character separator that is used to separate records written to the Firehose stream. Valid values are: &#39;\n&#39; (newline), &#39;\t&#39; (tab), &#39;\r\n&#39; (Windows newline), &#39;,&#39; (comma).
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
            <td class="align-top">Delivery<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The delivery stream name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Separator</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A character separator that is used to separate records written to the Firehose stream. Valid values are: &#39;\n&#39; (newline), &#39;\t&#39; (tab), &#39;\r\n&#39; (Windows newline), &#39;,&#39; (comma).
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
            <td class="align-top">delivery<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The delivery stream name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">separator</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A character separator that is used to separate records written to the Firehose stream. Valid values are: &#39;\n&#39; (newline), &#39;\t&#39; (tab), &#39;\r\n&#39; (Windows newline), &#39;,&#39; (comma).
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
            <td class="align-top">delivery<wbr>Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The delivery stream name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">separator</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A character separator that is used to separate records written to the Firehose stream. Valid values are: &#39;\n&#39; (newline), &#39;\t&#39; (tab), &#39;\r\n&#39; (Windows newline), &#39;,&#39; (comma).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleKinesis
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleKinesis">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleKinesis">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleKinesisArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleKinesisOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleKinesisArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleKinesis.html">output</a> API doc for this type.
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
            <td class="align-top">Partition<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The partition key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the Amazon Kinesis stream.
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
            <td class="align-top">Partition<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The partition key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the Amazon Kinesis stream.
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
            <td class="align-top">partition<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The partition key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the Amazon Kinesis stream.
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
            <td class="align-top">partition<wbr>Key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The partition key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the Amazon Kinesis stream.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleLambda
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleLambda">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleLambda">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleLambdaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleLambdaOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleLambdaArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleLambda.html">output</a> API doc for this type.
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function.
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function.
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
            <td class="align-top">function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function.
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
            <td class="align-top">function_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleRepublish
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleRepublish">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleRepublish">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleRepublishArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleRepublishOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleRepublishArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleRepublish.html">output</a> API doc for this type.
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
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the MQTT topic the message should be republished to.
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
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Topic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the MQTT topic the message should be republished to.
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
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the MQTT topic the message should be republished to.
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
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">topic</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the MQTT topic the message should be republished to.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleS3
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleS3">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleS3">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleS3Args">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleS3Output">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleS3Args.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleS3.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The object key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The object key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The object key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
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
            <td class="align-top">bucket_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon S3 bucket name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The object key.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleSns
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleSns">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleSns">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleSnsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleSnsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleSnsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleSns.html">output</a> API doc for this type.
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
            <td class="align-top">Message<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message format of the message to publish. Accepted values are &#34;JSON&#34; and &#34;RAW&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic.
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
            <td class="align-top">Message<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message format of the message to publish. Accepted values are &#34;JSON&#34; and &#34;RAW&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic.
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
            <td class="align-top">message<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message format of the message to publish. Accepted values are &#34;JSON&#34; and &#34;RAW&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic.
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
            <td class="align-top">message<wbr>Format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message format of the message to publish. Accepted values are &#34;JSON&#34; and &#34;RAW&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the SNS topic.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TopicRuleSqs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TopicRuleSqs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TopicRuleSqs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleSqsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/iot?tab=doc#TopicRuleSqsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleSqsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Iot.TopicRuleSqs.html">output</a> API doc for this type.
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
            <td class="align-top">Queue<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The URL of the Amazon SQS queue.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Base64</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether to use Base64 encoding.
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
            <td class="align-top">Queue<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The URL of the Amazon SQS queue.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Base64</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether to use Base64 encoding.
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
            <td class="align-top">queue<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The URL of the Amazon SQS queue.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Base64</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether to use Base64 encoding.
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
            <td class="align-top">queue_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The URL of the Amazon SQS queue.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the IAM role that grants access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Base64</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies whether to use Base64 encoding.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







