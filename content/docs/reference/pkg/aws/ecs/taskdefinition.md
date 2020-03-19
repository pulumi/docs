
---
title: "TaskDefinition"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages a revision of an ECS task definition to be used in `aws.ecs.Service`.

## Example Usage

### With AppMesh Proxy

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const service = new aws.ecs.TaskDefinition("service", {
    containerDefinitions: fs.readFileSync("task-definitions/service.json", "utf-8"),
    family: "service",
    proxyConfiguration: {
        containerName: "applicationContainerName",
        properties: {
            AppPorts: "8080",
            EgressIgnoredIPs: "169.254.170.2,169.254.169.254",
            IgnoredUID: "1337",
            ProxyEgressPort: 15001,
            ProxyIngressPort: 15000,
        },
        type: "APPMESH",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecs_task_definition.html.markdown.



## Create a TaskDefinition Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#TaskDefinition">TaskDefinition</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#TaskDefinitionArgs">TaskDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">TaskDefinition</span><span class="p">(resource_name, opts=None, </span>container_definitions=None<span class="p">, </span>cpu=None<span class="p">, </span>execution_role_arn=None<span class="p">, </span>family=None<span class="p">, </span>ipc_mode=None<span class="p">, </span>memory=None<span class="p">, </span>network_mode=None<span class="p">, </span>pid_mode=None<span class="p">, </span>placement_constraints=None<span class="p">, </span>proxy_configuration=None<span class="p">, </span>requires_compatibilities=None<span class="p">, </span>tags=None<span class="p">, </span>task_role_arn=None<span class="p">, </span>volumes=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTaskDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionArgs">TaskDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinition">TaskDefinition</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinition.html">TaskDefinition</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionArgs.html">TaskDefinitionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a TaskDefinition resource with the given unique name, arguments, and options.

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
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">[]ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">*ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">[]ecs.<wbr>Task<wbr>Definition<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
            <td class="align-top">container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">ecs.<wbr>Task<wbr>Definition<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
            <td class="align-top">container_<wbr>definitions</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List[Task<wbr>Definition<wbr>Placement<wbr>Constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Dict[Task<wbr>Definition<wbr>Proxy<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires_<wbr>compatibilities</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List[Task<wbr>Definition<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## TaskDefinition Output Properties

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
            <td class="align-top">{{% md %}} Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The revision of the task in a particular family.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Volume&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of volume blocks that containers in your task may use.
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
            <td class="align-top">{{% md %}} Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">[]ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">*ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The revision of the task in a particular family.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">[]ecs.<wbr>Task<wbr>Definition<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of volume blocks that containers in your task may use.
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
            <td class="align-top">{{% md %}} Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The revision of the task in a particular family.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">ecs.<wbr>Task<wbr>Definition<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of volume blocks that containers in your task may use.
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
            <td class="align-top">{{% md %}} Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container_<wbr>definitions</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List[Task<wbr>Definition<wbr>Placement<wbr>Constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Dict[Task<wbr>Definition<wbr>Proxy<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires_<wbr>compatibilities</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The revision of the task in a particular family.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List[Task<wbr>Definition<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of volume blocks that containers in your task may use.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing TaskDefinition Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#TaskDefinitionState">TaskDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#TaskDefinition">TaskDefinition</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>container_definitions=None<span class="p">, </span>cpu=None<span class="p">, </span>execution_role_arn=None<span class="p">, </span>family=None<span class="p">, </span>ipc_mode=None<span class="p">, </span>memory=None<span class="p">, </span>network_mode=None<span class="p">, </span>pid_mode=None<span class="p">, </span>placement_constraints=None<span class="p">, </span>proxy_configuration=None<span class="p">, </span>requires_compatibilities=None<span class="p">, </span>revision=None<span class="p">, </span>tags=None<span class="p">, </span>task_role_arn=None<span class="p">, </span>volumes=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTaskDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionState">TaskDefinitionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinition">TaskDefinition</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinition.html">TaskDefinition</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionState.html">TaskDefinitionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing TaskDefinition resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The revision of the task in a particular family.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Family</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">[]ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">*ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The revision of the task in a particular family.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">[]ecs.<wbr>Task<wbr>Definition<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container<wbr>Definitions</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">ecs.<wbr>Task<wbr>Definition<wbr>Placement<wbr>Constraint[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">ecs.<wbr>Task<wbr>Definition<wbr>Proxy<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires<wbr>Compatibilities</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The revision of the task in a particular family.
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
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">ecs.<wbr>Task<wbr>Definition<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
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
Full ARN of the Task Definition (including both `family` and `revision`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">container_<wbr>definitions</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">execution_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">family</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for your task definition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipc_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IPC resource namespace to be used for the containers in the task The valid values are `host`, `task`, and `none`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pid_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The process namespace to use for the containers in the task. The valid values are `host` and `task`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>constraints</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionplacementconstraint">List[Task<wbr>Definition<wbr>Placement<wbr>Constraint]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of placement constraints rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionproxyconfiguration">Dict[Task<wbr>Definition<wbr>Proxy<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy configuration details for the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requires_<wbr>compatibilities</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The revision of the task in a particular family.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volumes</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolume">List[Task<wbr>Definition<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of volume blocks that containers in your task may use.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### TaskDefinitionPlacementConstraint
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TaskDefinitionPlacementConstraint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TaskDefinitionPlacementConstraint">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionPlacementConstraintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionPlacementConstraintOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionPlacementConstraintArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionPlacementConstraint.html">output</a> API doc for this type.
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
            <td class="align-top">Expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster Query Language expression to apply to the constraint.
For more information, see [Cluster Query Language in the Amazon EC2 Container
Service Developer
Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
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
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">Expression</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster Query Language expression to apply to the constraint.
For more information, see [Cluster Query Language in the Amazon EC2 Container
Service Developer
Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
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
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">expression</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster Query Language expression to apply to the constraint.
For more information, see [Cluster Query Language in the Amazon EC2 Container
Service Developer
Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
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
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">expression</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Cluster Query Language expression to apply to the constraint.
For more information, see [Cluster Query Language in the Amazon EC2 Container
Service Developer
Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html).
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
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TaskDefinitionProxyConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TaskDefinitionProxyConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TaskDefinitionProxyConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionProxyConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionProxyConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionProxyConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionProxyConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the container that will serve as the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">Container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the container that will serve as the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the container that will serve as the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
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
            <td class="align-top">container_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the container that will serve as the App Mesh proxy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of network configuration parameters to provide the Container Network Interface (CNI) plugin, specified a key-value mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The proxy type. The default value is `APPMESH`. The only supported value is `APPMESH`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TaskDefinitionVolume
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TaskDefinitionVolume">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TaskDefinitionVolume">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolumeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolume.html">output</a> API doc for this type.
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
            <td class="align-top">Docker<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumedockervolumeconfiguration">Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Docker<wbr>Volume<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a docker volume
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Efs<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumeefsvolumeconfiguration">Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Efs<wbr>Volume<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a EFS volume. Can be used only with an EC2 type task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the volume. This name is referenced in the `sourceVolume`
parameter of container definition in the `mountPoints` section.
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
            <td class="align-top">Docker<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumedockervolumeconfiguration">*ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Docker<wbr>Volume<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a docker volume
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Efs<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumeefsvolumeconfiguration">*ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Efs<wbr>Volume<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a EFS volume. Can be used only with an EC2 type task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the volume. This name is referenced in the `sourceVolume`
parameter of container definition in the `mountPoints` section.
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
            <td class="align-top">docker<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumedockervolumeconfiguration">ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Docker<wbr>Volume<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a docker volume
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">efs<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumeefsvolumeconfiguration">ecs.<wbr>Task<wbr>Definition<wbr>Volume<wbr>Efs<wbr>Volume<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a EFS volume. Can be used only with an EC2 type task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the volume. This name is referenced in the `sourceVolume`
parameter of container definition in the `mountPoints` section.
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
            <td class="align-top">docker<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumedockervolumeconfiguration">Dict[Task<wbr>Definition<wbr>Volume<wbr>Docker<wbr>Volume<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a docker volume
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">efs<wbr>Volume<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#taskdefinitionvolumeefsvolumeconfiguration">Dict[Task<wbr>Definition<wbr>Volume<wbr>Efs<wbr>Volume<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Used to configure a EFS volume. Can be used only with an EC2 type task.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path on the host container instance that is presented to the container. If not set, ECS will create a nonpersistent data volume that starts empty and is deleted after the task has finished.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the volume. This name is referenced in the `sourceVolume`
parameter of container definition in the `mountPoints` section.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TaskDefinitionVolumeDockerVolumeConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TaskDefinitionVolumeDockerVolumeConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TaskDefinitionVolumeDockerVolumeConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeDockerVolumeConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeDockerVolumeConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolumeDockerVolumeConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolumeDockerVolumeConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Autoprovision</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Driver</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Driver<wbr>Opts</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of Docker driver specific options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of custom metadata to add to your Docker volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
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
            <td class="align-top">Autoprovision</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Driver</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Driver<wbr>Opts</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of Docker driver specific options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of custom metadata to add to your Docker volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
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
            <td class="align-top">autoprovision</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">driver</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">driver<wbr>Opts</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of Docker driver specific options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of custom metadata to add to your Docker volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
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
            <td class="align-top">autoprovision</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If this value is `true`, the Docker volume is created if it does not already exist. *Note*: This field is only used if the scope is `shared`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">driver</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Docker volume driver to use. The driver value must match the driver name provided by Docker because it is used for task placement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">driver<wbr>Opts</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of Docker driver specific options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of custom metadata to add to your Docker volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The scope for the Docker volume, which determines its lifecycle, either `task` or `shared`.  Docker volumes that are scoped to a `task` are automatically provisioned when the task starts and destroyed when the task stops. Docker volumes that are `scoped` as shared persist after the task stops.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TaskDefinitionVolumeEfsVolumeConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TaskDefinitionVolumeEfsVolumeConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TaskDefinitionVolumeEfsVolumeConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeEfsVolumeConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#TaskDefinitionVolumeEfsVolumeConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolumeEfsVolumeConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.TaskDefinitionVolumeEfsVolumeConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">File<wbr>System<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the EFS File System.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Directory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to mount on the host
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
            <td class="align-top">File<wbr>System<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the EFS File System.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Directory</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to mount on the host
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
            <td class="align-top">file<wbr>System<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the EFS File System.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Directory</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to mount on the host
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
            <td class="align-top">file_<wbr>system_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the EFS File System.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Directory</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The path to mount on the host
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







