
---
title: "EventTarget"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a CloudWatch Event Target resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const console = new aws.cloudwatch.EventRule("console", {
    description: "Capture all EC2 scaling events",
    eventPattern: `{
  "source": [
    "aws.autoscaling"
  ],
  "detail-type": [
    "EC2 Instance Launch Successful",
    "EC2 Instance Terminate Successful",
    "EC2 Instance Launch Unsuccessful",
    "EC2 Instance Terminate Unsuccessful"
  ]
}
`,
});
const testStream = new aws.kinesis.Stream("test_stream", {
    shardCount: 1,
});
const yada = new aws.cloudwatch.EventTarget("yada", {
    arn: testStream.arn,
    rule: console.name,
    runCommandTargets: [
        {
            key: "tag:Name",
            values: ["FooBar"],
        },
        {
            key: "InstanceIds",
            values: ["i-162058cd308bffec2"],
        },
    ],
});
```

## Example SSM Document Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ssmLifecycleTrust = aws.iam.getPolicyDocument({
    statements: [{
        actions: ["sts:AssumeRole"],
        principals: [{
            identifiers: ["events.amazonaws.com"],
            type: "Service",
        }],
    }],
});
const stopInstance = new aws.ssm.Document("stop_instance", {
    content: `  {
    "schemaVersion": "1.2",
    "description": "Stop an instance",
    "parameters": {

    },
    "runtimeConfig": {
      "aws:runShellScript": {
        "properties": [
          {
            "id": "0.aws:runShellScript",
            "runCommand": ["halt"]
          }
        ]
      }
    }
  }
`,
    documentType: "Command",
});
const ssmLifecyclePolicyDocument = stopInstance.arn.apply(arn => aws.iam.getPolicyDocument({
    statements: [
        {
            actions: ["ssm:SendCommand"],
            conditions: [{
                test: "StringEquals",
                values: ["*"],
                variable: "ec2:ResourceTag/Terminate",
            }],
            effect: "Allow",
            resources: ["arn:aws:ec2:eu-west-1:1234567890:instance/*"],
        },
        {
            actions: ["ssm:SendCommand"],
            effect: "Allow",
            resources: [arn],
        },
    ],
}));
const ssmLifecycleRole = new aws.iam.Role("ssm_lifecycle", {
    assumeRolePolicy: ssmLifecycleTrust.json,
});
const ssmLifecyclePolicy = new aws.iam.Policy("ssm_lifecycle", {
    policy: ssmLifecyclePolicyDocument.json,
});
const stopInstancesEventRule = new aws.cloudwatch.EventRule("stop_instances", {
    description: "Stop instances nightly",
    scheduleExpression: "cron(0 0 * * ? *)",
});
const stopInstancesEventTarget = new aws.cloudwatch.EventTarget("stop_instances", {
    arn: stopInstance.arn,
    roleArn: ssmLifecycleRole.arn,
    rule: stopInstancesEventRule.name,
    runCommandTargets: [{
        key: "tag:Terminate",
        values: ["midnight"],
    }],
});
```

## Example RunCommand Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const stopInstancesEventRule = new aws.cloudwatch.EventRule("stop_instances", {
    description: "Stop instances nightly",
    scheduleExpression: "cron(0 0 * * ? *)",
});
const stopInstancesEventTarget = new aws.cloudwatch.EventTarget("stop_instances", {
    arn: `arn:aws:ssm:${var_aws_region}::document/AWS-RunShellScript`,
    input: "{\"commands\":[\"halt\"]}",
    roleArn: aws_iam_role_ssm_lifecycle.arn,
    rule: stopInstancesEventRule.name,
    runCommandTargets: [{
        key: "tag:Terminate",
        values: ["midnight"],
    }],
});
```

## Example ECS Run Task with Role and Task Override Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ecsEvents = new aws.iam.Role("ecs_events", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
`,
});
const ecsEventsRunTaskWithAnyRole = new aws.iam.RolePolicy("ecs_events_run_task_with_any_role", {
    policy: aws_ecs_task_definition_task_name.arn.apply(arn => `{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ecs:RunTask",
            "Resource": "${arn.replace(/:\d+$/, ":*")}"
        }
    ]
}
`),
    role: ecsEvents.id,
});
const ecsScheduledTask = new aws.cloudwatch.EventTarget("ecs_scheduled_task", {
    arn: aws_ecs_cluster_cluster_name.arn,
    ecsTarget: {
        taskCount: 1,
        taskDefinitionArn: aws_ecs_task_definition_task_name.arn,
    },
    input: `{
  "containerOverrides": [
    {
      "name": "name-of-container-to-override",
      "command": ["bin/console", "scheduled-task"]
    }
  ]
}
`,
    roleArn: ecsEvents.arn,
    rule: aws_cloudwatch_event_rule_every_hour.name,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudwatch_event_target.html.markdown.



## Create a EventTarget Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudwatch/#EventTarget">EventTarget</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudwatch/#EventTargetArgs">EventTargetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">EventTarget</span><span class="p">(resource_name, opts=None, </span>arn=None<span class="p">, </span>batch_target=None<span class="p">, </span>ecs_target=None<span class="p">, </span>input=None<span class="p">, </span>input_path=None<span class="p">, </span>input_transformer=None<span class="p">, </span>kinesis_target=None<span class="p">, </span>role_arn=None<span class="p">, </span>rule=None<span class="p">, </span>run_command_targets=None<span class="p">, </span>sqs_target=None<span class="p">, </span>target_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewEventTarget<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetArgs">EventTargetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTarget">EventTarget</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTarget.html">EventTarget</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetArgs.html">EventTargetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a EventTarget resource with the given unique name, arguments, and options.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">*cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">[]cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
 (Required)
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Dict[event_<wbr>target_<wbr>batch_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Dict[event_<wbr>target_<wbr>ecs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Dict[event_<wbr>target_<wbr>input_<wbr>transformer]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Dict[event_<wbr>target_<wbr>kinesis_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run_<wbr>command_<wbr>targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List[event_<wbr>target_<wbr>run_<wbr>command_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Dict[event_<wbr>target_<wbr>sqs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## EventTarget Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The unique target assignment ID.  If missing, will generate a random, unique id.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">*cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">[]cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The unique target assignment ID.  If missing, will generate a random, unique id.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The unique target assignment ID.  If missing, will generate a random, unique id.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Dict[event_<wbr>target_<wbr>batch_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Dict[event_<wbr>target_<wbr>ecs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Dict[event_<wbr>target_<wbr>input_<wbr>transformer]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Dict[event_<wbr>target_<wbr>kinesis_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run_<wbr>command_<wbr>targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List[event_<wbr>target_<wbr>run_<wbr>command_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Dict[event_<wbr>target_<wbr>sqs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The unique target assignment ID.  If missing, will generate a random, unique id.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing EventTarget Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudwatch/#EventTargetState">EventTargetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cloudwatch/#EventTarget">EventTarget</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>batch_target=None<span class="p">, </span>ecs_target=None<span class="p">, </span>input=None<span class="p">, </span>input_path=None<span class="p">, </span>input_transformer=None<span class="p">, </span>kinesis_target=None<span class="p">, </span>role_arn=None<span class="p">, </span>rule=None<span class="p">, </span>run_command_targets=None<span class="p">, </span>sqs_target=None<span class="p">, </span>target_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetEventTarget<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetState">EventTargetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTarget">EventTarget</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTarget.html">EventTarget</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetState.html">EventTargetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing EventTarget resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List&lt;Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">*cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">[]cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">*cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Batch<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">cloudwatch.<wbr>Event<wbr>Target<wbr>Input<wbr>Transformer?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Kinesis<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run<wbr>Command<wbr>Targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Run<wbr>Command<wbr>Target[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">cloudwatch.<wbr>Event<wbr>Target<wbr>Sqs<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
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
The Amazon Resource Name (ARN) associated of the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">batch_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetbatchtarget">Dict[event_<wbr>target_<wbr>batch_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Batch Job. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ecs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstarget">Dict[event_<wbr>target_<wbr>ecs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon ECS Task. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Valid JSON text passed to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The value of the [JSONPath](http://goessner.net/articles/JsonPath/)
that is used for extracting part of the matched event when passing it to the target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>transformer</td>
            <td class="align-top">
                
                <code><a href="#eventtargetinputtransformer">Dict[event_<wbr>target_<wbr>input_<wbr>transformer]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are providing a custom input to a target based on certain event data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kinesis_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetkinesistarget">Dict[event_<wbr>target_<wbr>kinesis_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon Kinesis Stream. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. Required if `ecs_target` is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the rule you want to add targets to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run_<wbr>command_<wbr>targets</td>
            <td class="align-top">
                
                <code><a href="#eventtargetruncommandtarget">List[event_<wbr>target_<wbr>run_<wbr>command_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke Amazon EC2 Run Command. Documented below. A maximum of 5 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sqs_<wbr>target</td>
            <td class="align-top">
                
                <code><a href="#eventtargetsqstarget">Dict[event_<wbr>target_<wbr>sqs_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Parameters used when you are using the rule to invoke an Amazon SQS Queue. Documented below. A maximum of 1 are allowed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unique target assignment ID.  If missing, will generate a random, unique id.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### EventTargetBatchTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetBatchTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetBatchTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetBatchTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetBatchTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetBatchTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetBatchTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Array<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Attempts</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name to use for this execution of the job, if the target is an AWS Batch job.
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
            <td class="align-top">Array<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Attempts</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Job<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name to use for this execution of the job, if the target is an AWS Batch job.
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
            <td class="align-top">array<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job<wbr>Attempts</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name to use for this execution of the job, if the target is an AWS Batch job.
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
            <td class="align-top">array_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job_<wbr>attempts</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of times to attempt to retry, if the job fails. Valid values are 1 to 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job_<wbr>definition</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">job_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name to use for this execution of the job, if the target is an AWS Batch job.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetEcsTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetEcsTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetEcsTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetEcsTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetEcsTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetEcsTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetEcsTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ECS task group for the task. The maximum length is 255 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstargetnetworkconfiguration">Pulumi.<wbr>Aws.<wbr>Cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target<wbr>Network<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of tasks to create based on the TaskDefinition. The default is 1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition to use if the event target is an Amazon ECS cluster.
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
            <td class="align-top">Group</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ECS task group for the task. The maximum length is 255 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstargetnetworkconfiguration">*cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target<wbr>Network<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of tasks to create based on the TaskDefinition. The default is 1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition to use if the event target is an Amazon ECS cluster.
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
            <td class="align-top">group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ECS task group for the task. The maximum length is 255 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstargetnetworkconfiguration">cloudwatch.<wbr>Event<wbr>Target<wbr>Ecs<wbr>Target<wbr>Network<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of tasks to create based on the TaskDefinition. The default is 1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Definition<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition to use if the event target is an Amazon ECS cluster.
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
            <td class="align-top">group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies an ECS task group for the task. The maximum length is 255 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. Valid values are EC2 or FARGATE.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#eventtargetecstargetnetworkconfiguration">Dict[event_<wbr>target_<wbr>ecs_<wbr>target_<wbr>network_<wbr>configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Use this if the ECS task uses the awsvpc network mode. This specifies the VPC subnets and security groups associated with the task, and whether a public IP address is to be used. Required if launch_type is FARGATE because the awsvpc mode is required for Fargate tasks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. This is used only if LaunchType is FARGATE. For more information about valid platform versions, see [AWS Fargate Platform Versions](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of tasks to create based on the TaskDefinition. The default is 1.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>definition_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition to use if the event target is an Amazon ECS cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetEcsTargetNetworkConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetEcsTargetNetworkConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetEcsTargetNetworkConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetEcsTargetNetworkConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetEcsTargetNetworkConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetEcsTargetNetworkConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetEcsTargetNetworkConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Assign<wbr>Public<wbr>Ip</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnets associated with the task or service.
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
            <td class="align-top">Assign<wbr>Public<wbr>Ip</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnets associated with the task or service.
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
            <td class="align-top">assign<wbr>Public<wbr>Ip</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnets associated with the task or service.
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
            <td class="align-top">assign_<wbr>public_<wbr>ip</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Assign a public IP address to the ENI (Fargate launch type only). Valid values are `true` or `false`. Default `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The subnets associated with the task or service.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetInputTransformer
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetInputTransformer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetInputTransformer">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetInputTransformerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetInputTransformerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetInputTransformerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetInputTransformer.html">output</a> API doc for this type.
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
            <td class="align-top">Input<wbr>Paths</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key value pairs specified in the form of JSONPath (for example, time = $.time)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Structure containing the template body.
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
            <td class="align-top">Input<wbr>Paths</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key value pairs specified in the form of JSONPath (for example, time = $.time)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Structure containing the template body.
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
            <td class="align-top">input<wbr>Paths</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key value pairs specified in the form of JSONPath (for example, time = $.time)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Structure containing the template body.
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
            <td class="align-top">input_<wbr>paths</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key value pairs specified in the form of JSONPath (for example, time = $.time)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Structure containing the template body.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetKinesisTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetKinesisTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetKinesisTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetKinesisTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetKinesisTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetKinesisTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetKinesisTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Partition<wbr>Key<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The JSON path to be extracted from the event and used as the partition key.
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
            <td class="align-top">Partition<wbr>Key<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The JSON path to be extracted from the event and used as the partition key.
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
            <td class="align-top">partition<wbr>Key<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The JSON path to be extracted from the event and used as the partition key.
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
            <td class="align-top">partition_<wbr>key_<wbr>path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The JSON path to be extracted from the event and used as the partition key.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetRunCommandTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetRunCommandTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetRunCommandTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetRunCommandTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetRunCommandTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetRunCommandTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetRunCommandTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `tag:tag-key` or `InstanceIds`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `tag:tag-key` or `InstanceIds`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `tag:tag-key` or `InstanceIds`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Can be either `tag:tag-key` or `InstanceIds`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
If Key is `tag:tag-key`, Values is a list of tag values. If Key is `InstanceIds`, Values is a list of Amazon EC2 instance IDs.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EventTargetSqsTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EventTargetSqsTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EventTargetSqsTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetSqsTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cloudwatch?tab=doc#EventTargetSqsTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetSqsTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cloudwatch.EventTargetSqsTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Message<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The FIFO message group ID to use as the target.
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
            <td class="align-top">Message<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The FIFO message group ID to use as the target.
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
            <td class="align-top">message<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The FIFO message group ID to use as the target.
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
            <td class="align-top">message_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The FIFO message group ID to use as the target.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







