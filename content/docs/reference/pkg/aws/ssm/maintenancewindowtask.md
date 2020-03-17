
---
title: "MaintenanceWindowTask"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an SSM Maintenance Window Task resource

## Example Usage

### Automation Tasks

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ssm.MaintenanceWindowTask("example", {
    maxConcurrency: "2",
    maxErrors: "1",
    priority: 1,
    serviceRoleArn: aws_iam_role_example.arn,
    targets: [{
        key: "InstanceIds",
        values: [aws_instance_example.id],
    }],
    taskArn: "AWS-RestartEC2Instance",
    taskInvocationParameters: {
        automationParameters: {
            documentVersion: "$LATEST",
            parameters: [{
                name: "InstanceId",
                values: [aws_instance_example.id],
            }],
        },
    },
    taskType: "AUTOMATION",
    windowId: aws_ssm_maintenance_window_example.id,
});
```

### Lambda Tasks

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ssm.MaintenanceWindowTask("example", {
    maxConcurrency: "2",
    maxErrors: "1",
    priority: 1,
    serviceRoleArn: aws_iam_role_example.arn,
    targets: [{
        key: "InstanceIds",
        values: [aws_instance_example.id],
    }],
    taskArn: aws_lambda_function_example.arn,
    taskInvocationParameters: {
        lambdaParameters: {
            clientContext: Buffer.from("{\"key1\":\"value1\"}").toString("base64"),
            payload: "{\"key1\":\"value1\"}",
        },
    },
    taskType: "LAMBDA",
    windowId: aws_ssm_maintenance_window_example.id,
});
```

### Run Command Tasks

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ssm.MaintenanceWindowTask("example", {
    maxConcurrency: "2",
    maxErrors: "1",
    priority: 1,
    serviceRoleArn: aws_iam_role_example.arn,
    targets: [{
        key: "InstanceIds",
        values: [aws_instance_example.id],
    }],
    taskArn: "AWS-RunShellScript",
    taskInvocationParameters: {
        runCommandParameters: {
            notificationConfig: {
                notificationArn: aws_sns_topic_example.arn,
                notificationEvents: ["All"],
                notificationType: ["Command"],
            },
            outputS3Bucket: aws_s3_bucket_example.bucket,
            outputS3KeyPrefix: "output",
            parameters: [{
                name: "commands",
                values: ["date"],
            }],
            serviceRoleArn: aws_iam_role_example.arn,
            timeoutSeconds: 600,
        },
    },
    taskType: "RUN_COMMAND",
    windowId: aws_ssm_maintenance_window_example.id,
});
```

### Step Function Tasks

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ssm.MaintenanceWindowTask("example", {
    maxConcurrency: "2",
    maxErrors: "1",
    priority: 1,
    serviceRoleArn: aws_iam_role_example.arn,
    targets: [{
        key: "InstanceIds",
        values: [aws_instance_example.id],
    }],
    taskArn: aws_sfn_activity_example.id,
    taskInvocationParameters: {
        stepFunctionsParameters: {
            input: "{\"key1\":\"value1\"}",
            name: "example",
        },
    },
    taskType: "STEP_FUNCTIONS",
    windowId: aws_ssm_maintenance_window_example.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_task.html.markdown.



## Create a MaintenanceWindowTask Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTask">MaintenanceWindowTask</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTaskArgs">MaintenanceWindowTaskArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MaintenanceWindowTask</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>logging_info=None<span class="p">, </span>max_concurrency=None<span class="p">, </span>max_errors=None<span class="p">, </span>name=None<span class="p">, </span>priority=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>targets=None<span class="p">, </span>task_arn=None<span class="p">, </span>task_invocation_parameters=None<span class="p">, </span>task_parameters=None<span class="p">, </span>task_type=None<span class="p">, </span>window_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMaintenanceWindowTask<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskArgs">MaintenanceWindowTaskArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTask">MaintenanceWindowTask</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTask.html">MaintenanceWindowTask</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskArgs.html">MaintenanceWindowTaskArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a MaintenanceWindowTask resource with the given unique name, arguments, and options.

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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Dict[maintenance_<wbr>window_<wbr>task_<wbr>logging_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>concurrency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>errors</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List[maintenance_<wbr>window_<wbr>task_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>invocation_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the task with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## MaintenanceWindowTask Output Properties

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of errors allowed before this task stops being scheduled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the task with.
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
            <td class="align-top">{{% md %}} The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of errors allowed before this task stops being scheduled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the task with.
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
            <td class="align-top">{{% md %}} The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of errors allowed before this task stops being scheduled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the task with.
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
            <td class="align-top">{{% md %}} The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Dict[maintenance_<wbr>window_<wbr>task_<wbr>logging_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>concurrency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>errors</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum number of errors allowed before this task stops being scheduled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List[maintenance_<wbr>window_<wbr>task_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>invocation_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the task with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing MaintenanceWindowTask Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTaskState">MaintenanceWindowTaskState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTask">MaintenanceWindowTask</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>logging_info=None<span class="p">, </span>max_concurrency=None<span class="p">, </span>max_errors=None<span class="p">, </span>name=None<span class="p">, </span>priority=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>targets=None<span class="p">, </span>task_arn=None<span class="p">, </span>task_invocation_parameters=None<span class="p">, </span>task_parameters=None<span class="p">, </span>task_type=None<span class="p">, </span>window_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMaintenanceWindowTask<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskState">MaintenanceWindowTaskState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTask">MaintenanceWindowTask</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTask.html">MaintenanceWindowTask</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskState.html">MaintenanceWindowTaskState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing MaintenanceWindowTask resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Errors</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Logging<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Concurrency</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Errors</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Target[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Invocation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the task with.
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
The description of the maintenance window task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasklogginginfo">Dict[maintenance_<wbr>window_<wbr>task_<wbr>logging_<wbr>info]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about an Amazon S3 bucket to write instance-level logs to. Use `task_invocation_parameters` configuration block `run_command_parameters` configuration block `output_s3_*` arguments instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>concurrency</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of targets this task can be run for in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>errors</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum number of errors allowed before this task stops being scheduled.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktarget">List[maintenance_<wbr>window_<wbr>task_<wbr>target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the task to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>invocation_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for task execution. This argument is conflict with `task_parameters` and `logging_info`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskparameter">List[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A structure containing information about parameters required by the particular `task_arn`. Use `parameter` configuration blocks under the `task_invocation_parameters` configuration block instead. Conflicts with `task_invocation_parameters`. Documented below.
 {{% /md %}}

            use &#39;task_invocation_parameters&#39; argument instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of task being registered. The only allowed value is `RUN_COMMAND`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the task with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### MaintenanceWindowTaskLoggingInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskLoggingInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskLoggingInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskLoggingInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskLoggingInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskLoggingInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskLoggingInfo.html">output</a> API doc for this type.
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
            <td class="align-top">S3Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">S3Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">S3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">s3Bucket<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3Region</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">s3_<wbr>bucket_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">s3_<wbr>region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTarget.html">output</a> API doc for this type.
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
The array of strings.
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
The array of strings.
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
The array of strings.
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
The array of strings.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParameters
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParameters">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParameters.html">output</a> API doc for this type.
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
            <td class="align-top">Automation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for an AUTOMATION task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameterslambdaparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Lambda<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a LAMBDA task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a RUN_COMMAND task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Functions<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersstepfunctionsparameters">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Step<wbr>Functions<wbr>Parameters<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a STEP_FUNCTIONS task type. Documented below.
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
            <td class="align-top">Automation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for an AUTOMATION task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameterslambdaparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Lambda<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a LAMBDA task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Run<wbr>Command<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a RUN_COMMAND task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Functions<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersstepfunctionsparameters">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Step<wbr>Functions<wbr>Parameters</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a STEP_FUNCTIONS task type. Documented below.
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
            <td class="align-top">automation<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for an AUTOMATION task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameterslambdaparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Lambda<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a LAMBDA task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run<wbr>Command<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a RUN_COMMAND task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step<wbr>Functions<wbr>Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersstepfunctionsparameters">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Step<wbr>Functions<wbr>Parameters?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a STEP_FUNCTIONS task type. Documented below.
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
            <td class="align-top">automation_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>automation_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for an AUTOMATION task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparameterslambdaparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>lambda_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a LAMBDA task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">run_<wbr>command_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>run_<wbr>command_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a RUN_COMMAND task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step_<wbr>functions_<wbr>parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersstepfunctionsparameters">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>step_<wbr>functions_<wbr>parameters]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for a STEP_FUNCTIONS task type. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersAutomationParameters
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersAutomationParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersAutomationParameters">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersAutomationParameters.html">output</a> API doc for this type.
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
            <td class="align-top">Document<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of an Automation document to use during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparametersparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
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
            <td class="align-top">Document<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of an Automation document to use during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparametersparameter">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
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
            <td class="align-top">document<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of an Automation document to use during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparametersparameter">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Automation<wbr>Parameters<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
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
            <td class="align-top">document_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of an Automation document to use during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersautomationparametersparameter">List[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>automation_<wbr>parameters_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersAutomationParametersParameter.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersLambdaParameters
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersLambdaParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersLambdaParameters">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersLambdaParametersOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersLambdaParametersArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersLambdaParameters.html">output</a> API doc for this type.
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
            <td class="align-top">Client<wbr>Context</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Pass client-specific information to the Lambda function that you are invoking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
JSON to provide to your Lambda function as input.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify a Lambda function version or alias name.
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
            <td class="align-top">Client<wbr>Context</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Pass client-specific information to the Lambda function that you are invoking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Payload</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
JSON to provide to your Lambda function as input.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Qualifier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify a Lambda function version or alias name.
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
            <td class="align-top">client<wbr>Context</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Pass client-specific information to the Lambda function that you are invoking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
JSON to provide to your Lambda function as input.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify a Lambda function version or alias name.
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
            <td class="align-top">client_<wbr>context</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Pass client-specific information to the Lambda function that you are invoking.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">payload</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
JSON to provide to your Lambda function as input.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">qualifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify a Lambda function version or alias name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParameters.html">output</a> API doc for this type.
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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the command(s) to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Document<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Document<wbr>Hash<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersnotificationconfig">Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Notification<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>S3Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket subfolder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersparameter">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Parameter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Seconds</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this time is reached and the command has not already started executing, it doesn&#39;t run.
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
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the command(s) to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Document<wbr>Hash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Document<wbr>Hash<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersnotificationconfig">*ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Notification<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>S3Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket subfolder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersparameter">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Parameter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout<wbr>Seconds</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this time is reached and the command has not already started executing, it doesn&#39;t run.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the command(s) to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">document<wbr>Hash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">document<wbr>Hash<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersnotificationconfig">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Notification<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>S3Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>S3Key<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket subfolder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersparameter">ssm.<wbr>Maintenance<wbr>Window<wbr>Task<wbr>Task<wbr>Invocation<wbr>Parameters<wbr>Run<wbr>Command<wbr>Parameters<wbr>Parameter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout<wbr>Seconds</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this time is reached and the command has not already started executing, it doesn&#39;t run.
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
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about the command(s) to execute.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">document_<wbr>hash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">document_<wbr>hash_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersnotificationconfig">Dict[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>run_<wbr>command_<wbr>parameters_<wbr>notification_<wbr>config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configurations for sending notifications about command status changes on a per-instance basis. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>s3_<wbr>bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Amazon S3 bucket.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>s3_<wbr>key_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon S3 bucket subfolder.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtasktaskinvocationparametersruncommandparametersparameter">List[maintenance_<wbr>window_<wbr>task_<wbr>task_<wbr>invocation_<wbr>parameters_<wbr>run_<wbr>command_<wbr>parameters_<wbr>parameter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The parameters for the RUN_COMMAND task execution. Documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role to assume during task execution.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout_<wbr>seconds</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this time is reached and the command has not already started executing, it doesn&#39;t run.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersNotificationConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Notification<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Events</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
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
            <td class="align-top">Notification<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Events</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
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
            <td class="align-top">notification<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Events</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
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
            <td class="align-top">notification_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) for a Simple Notification Service (SNS) topic. Run Command pushes notifications about command status changes to this topic.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>events</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The different events for which you can receive notifications. Valid values: `All`, `InProgress`, `Success`, `TimedOut`, `Cancelled`, and `Failed`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When specified with `Command`, receive notification when the status of a command changes. When specified with `Invocation`, for commands sent to multiple instances, receive notification on a per-instance basis when the status of a command changes. Valid values: `Command` and `Invocation`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersRunCommandParametersParameter.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParametersArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskInvocationParametersStepFunctionsParameters.html">output</a> API doc for this type.
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
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inputs for the STEP_FUNCTION task.
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
The parameter name.
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
            <td class="align-top">Input</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inputs for the STEP_FUNCTION task.
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
The parameter name.
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
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inputs for the STEP_FUNCTION task.
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
The parameter name.
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
            <td class="align-top">input</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The inputs for the STEP_FUNCTION task.
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
The parameter name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### MaintenanceWindowTaskTaskParameter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTaskTaskParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTaskTaskParameter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTaskTaskParameterOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskParameterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTaskTaskParameter.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The parameter name.
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
The array of strings.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







