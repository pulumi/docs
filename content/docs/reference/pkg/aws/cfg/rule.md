
---
title: "Rule"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an AWS Config Rule.

> **Note:** Config Rule requires an existing [Configuration Recorder](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html) to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

## Example Usage

### AWS Managed Rules

AWS managed rules can be used by setting the source owner to `AWS` and the source identifier to the name of the managed rule. More information about AWS managed rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const role = new aws.iam.Role("r", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
`,
});
const foo = new aws.cfg.Recorder("foo", {
    roleArn: role.arn,
});
const rule = new aws.cfg.Rule("r", {
    source: {
        owner: "AWS",
        sourceIdentifier: "S3_BUCKET_VERSIONING_ENABLED",
    },
}, {dependsOn: [foo]});
const rolePolicy = new aws.iam.RolePolicy("p", {
    policy: `{
  "Version": "2012-10-17",
  "Statement": [
  	{
  		"Action": "config:Put*",
  		"Effect": "Allow",
  		"Resource": "*"

  	}
  ]
}
`,
    role: role.id,
});
```

### Custom Rules

Custom rules can be used by setting the source owner to `CUSTOM_LAMBDA` and the source identifier to the Amazon Resource Name (ARN) of the Lambda Function. The AWS Config service must have permissions to invoke the Lambda Function, e.g. via the [`aws.lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html). More information about custom rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleRecorder = new aws.cfg.Recorder("example", {});
const exampleFunction = new aws.lambda.Function("example", {});
const examplePermission = new aws.lambda.Permission("example", {
    action: "lambda:InvokeFunction",
    function: exampleFunction.arn,
    principal: "config.amazonaws.com",
});
const exampleRule = new aws.cfg.Rule("example", {
    source: {
        owner: "CUSTOM_LAMBDA",
        sourceIdentifier: exampleFunction.arn,
    },
}, {dependsOn: [exampleRecorder, examplePermission]});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/config_config_rule.html.markdown.



## Create a Rule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#Rule">Rule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#RuleArgs">RuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Rule</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>input_parameters=None<span class="p">, </span>maximum_execution_frequency=None<span class="p">, </span>name=None<span class="p">, </span>scope=None<span class="p">, </span>source=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleArgs">RuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#Rule">Rule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.Rule.html">Rule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleArgs.html">RuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Rule resource with the given unique name, arguments, and options.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Scope<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Source<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">*cfg.<wbr>Rule<wbr>Scope</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">cfg.<wbr>Rule<wbr>Scope?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>parameters</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>execution_<wbr>frequency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Dict[rule_<wbr>scope]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Dict[rule_<wbr>source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Rule Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Scope?</a></code>
            </td>
            <td class="align-top">{{% md %}} Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
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
            <td class="align-top">{{% md %}} The ARN of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">*cfg.<wbr>Rule<wbr>Scope</a></code>
            </td>
            <td class="align-top">{{% md %}} Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
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
            <td class="align-top">{{% md %}} The ARN of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">cfg.<wbr>Rule<wbr>Scope?</a></code>
            </td>
            <td class="align-top">{{% md %}} Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
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
            <td class="align-top">{{% md %}} The ARN of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>parameters</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>execution_<wbr>frequency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Dict[rule_<wbr>scope]</a></code>
            </td>
            <td class="align-top">{{% md %}} Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Dict[rule_<wbr>source]</a></code>
            </td>
            <td class="align-top">{{% md %}} Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Rule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#RuleState">RuleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#Rule">Rule</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>input_parameters=None<span class="p">, </span>maximum_execution_frequency=None<span class="p">, </span>name=None<span class="p">, </span>rule_id=None<span class="p">, </span>scope=None<span class="p">, </span>source=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleState">RuleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#Rule">Rule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.Rule.html">Rule</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleState.html">RuleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Rule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the config rule
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
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Scope<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
The ARN of the config rule
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
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">*cfg.<wbr>Rule<wbr>Scope</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">*cfg.<wbr>Rule<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
The ARN of the config rule
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
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Parameters</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">cfg.<wbr>Rule<wbr>Scope?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">cfg.<wbr>Rule<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
The ARN of the config rule
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
Description of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>parameters</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A string in JSON format that is passed to the AWS Config rule Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>execution_<wbr>frequency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
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
The name of the rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the config rule
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code><a href="#rulescope">Dict[rule_<wbr>scope]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Scope defines which resources can trigger an evaluation for the rule as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source</td>
            <td class="align-top">
                
                <code><a href="#rulesource">Dict[rule_<wbr>source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### RuleScope
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RuleScope">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RuleScope">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleScopeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleScopeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleScopeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleScope.html">output</a> API doc for this type.
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
            <td class="align-top">Compliance<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compliance<wbr>Resource<wbr>Types</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
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
            <td class="align-top">Compliance<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compliance<wbr>Resource<wbr>Types</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Value</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
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
            <td class="align-top">compliance<wbr>Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compliance<wbr>Resource<wbr>Types</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag<wbr>Value</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
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
            <td class="align-top">compliance_<wbr>resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compliance_<wbr>resource_<wbr>types</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of resource types of only those AWS resources that you want to trigger an
evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag key that is applied to only those AWS resources that you want you
want to trigger an evaluation for the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag_<wbr>value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RuleSource
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RuleSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RuleSource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleSourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleSourceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleSource.html">output</a> API doc for this type.
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
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the [`aws.lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#rulesourcesourcedetail">List&lt;Pulumi.<wbr>Aws.<wbr>Cfg.<wbr>Rule<wbr>Source<wbr>Source<wbr>Detail<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the [`arn` attribute of the `aws.lambda.Function` resource](https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn).
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
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the [`aws.lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#rulesourcesourcedetail">[]cfg.<wbr>Rule<wbr>Source<wbr>Source<wbr>Detail</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the [`arn` attribute of the `aws.lambda.Function` resource](https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn).
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
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the [`aws.lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Details</td>
            <td class="align-top">
                
                <code><a href="#rulesourcesourcedetail">cfg.<wbr>Rule<wbr>Source<wbr>Source<wbr>Detail[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the [`arn` attribute of the `aws.lambda.Function` resource](https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn).
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
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the [`aws.lambda.Permission` resource](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>details</td>
            <td class="align-top">
                
                <code><a href="#rulesourcesourcedetail">List[rule_<wbr>source_<wbr>source_<wbr>detail]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the [`arn` attribute of the `aws.lambda.Function` resource](https://www.terraform.io/docs/providers/aws/r/lambda_function.html#arn).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### RuleSourceSourceDetail
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#RuleSourceSourceDetail">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#RuleSourceSourceDetail">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleSourceSourceDetailArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#RuleSourceSourceDetailOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleSourceSourceDetailArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.RuleSourceSourceDetail.html">output</a> API doc for this type.
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
            <td class="align-top">Event<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Message<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
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
            <td class="align-top">Event<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Message<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
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
            <td class="align-top">event<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum<wbr>Execution<wbr>Frequency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">message<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
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
            <td class="align-top">event_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The source of the event, such as an AWS service, that triggers AWS Config
to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maximum_<wbr>execution_<wbr>frequency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">message_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







