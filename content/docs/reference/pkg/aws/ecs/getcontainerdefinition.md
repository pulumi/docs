
---
title: "GetContainerDefinition"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

The ECS container definition data source allows access to details of
a specific container within an AWS ECS service.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ecs_mongo = aws_ecs_task_definition_mongo.id.apply(id => aws.ecs.getContainerDefinition({
    containerName: "mongodb",
    taskDefinition: id,
}));
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ecs_container_definition.html.markdown.





## Using GetContainerDefinition

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getContainerDefinition<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#GetContainerDefinitionArgs">GetContainerDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#GetContainerDefinitionResult">GetContainerDefinitionResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_container_definition(</span>container_name=None<span class="p">, </span>task_definition=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupContainerDefinition<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#LookupContainerDefinitionArgs">LookupContainerDefinitionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#LookupContainerDefinitionResult">LookupContainerDefinitionResult</a></span>, error)</span></code></pre></div>


<div class="highlight">
<pre class="chroma">
<code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetContainerDefinition </span><span class="p">{</span>
    <span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.GetContainerDefinitionResult.html">Pulumi.Aws.Ecs.GetContainerDefinitionResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.GetContainerDefinitionArgs.html">GetContainerDefinitionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span>
<span class="p">}</span></code></pre>
</div>



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
            <td class="align-top">Container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition which contains the container
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
The name of the container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition which contains the container
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
The name of the container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition which contains the container
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
The name of the container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>definition</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the task definition which contains the container
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetContainerDefinition Result

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
            <td class="align-top">Container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The CPU limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Networking</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicator if networking is disabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Docker<wbr>Labels</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Set docker labels
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The environment in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The docker image in use, including the digest
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Digest</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The digest of the docker image in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The memory limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Reservation</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">Container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The CPU limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Networking</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicator if networking is disabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Docker<wbr>Labels</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} Set docker labels
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Environment</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} The environment in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The docker image in use, including the digest
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Digest</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The digest of the docker image in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The memory limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Memory<wbr>Reservation</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">container<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The CPU limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Networking</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Indicator if networking is disabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">docker<wbr>Labels</td>
            <td class="align-top">
                
                <code>{[key: string]: string}</code>
            </td>
            <td class="align-top">{{% md %}} Set docker labels
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>{[key: string]: string}</code>
            </td>
            <td class="align-top">{{% md %}} The environment in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The docker image in use, including the digest
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Digest</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The digest of the docker image in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The memory limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory<wbr>Reservation</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task<wbr>Definition</td>
            <td class="align-top">
                
                <code>string</code>
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
            <td class="align-top">container_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The CPU limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable_<wbr>networking</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicator if networking is disabled
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">docker_<wbr>labels</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} Set docker labels
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">environment</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} The environment in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The docker image in use, including the digest
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>digest</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The digest of the docker image in use
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The memory limit for this container definition
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">memory_<wbr>reservation</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">task_<wbr>definition</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







