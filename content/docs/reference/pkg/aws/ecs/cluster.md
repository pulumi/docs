
---
title: "Cluster"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an ECS cluster.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const foo = new aws.ecs.Cluster("foo", {});
```

## setting

The `setting` configuration block supports the following:

* `name` - (Required) Name of the setting to manage. Valid values: `containerInsights`.
* `value` -  (Required) The value to assign to the setting. Value values are `enabled` and `disabled`.

## default_capacity_provider_strategy

The `default_capacity_provider_strategy` configuration block supports the following:

* `capacity_provider` - (Required) The short name of the capacity provider.
* `weight` - (Optional) The relative percentage of the total number of launched tasks that should use the specified capacity provider.
* `base` - (Optional) The number of tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecs_cluster.html.markdown.



## Create a Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>capacity_providers=None<span class="p">, </span>default_capacity_provider_strategies=None<span class="p">, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterArgs.html">ClusterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Cluster resource with the given unique name, arguments, and options.

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
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Setting<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">[]Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">[]Cluster<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">ecs.<wbr>Cluster<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">capacity_<wbr>providers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>capacity_<wbr>provider_<wbr>strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List[Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List[Cluster<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
    
    </tbody>
</table>


{{% /lang %}}







## Cluster Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Setting&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">[]Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy</a></code>
            </td>
            <td class="align-top">{{% md %}} The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">[]Cluster<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">ecs.<wbr>Cluster<wbr>Setting[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity_<wbr>providers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>capacity_<wbr>provider_<wbr>strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List[Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy]</a></code>
            </td>
            <td class="align-top">{{% md %}} The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List[Cluster<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ecs/#Cluster">Cluster</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>capacity_providers=None<span class="p">, </span>default_capacity_provider_strategies=None<span class="p">, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List&lt;Pulumi.<wbr>Aws.<wbr>Ecs.<wbr>Cluster<wbr>Setting<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">[]Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">[]Cluster<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Providers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Capacity<wbr>Provider<wbr>Strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">ecs.<wbr>Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">ecs.<wbr>Cluster<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
The Amazon Resource Name (ARN) that identifies the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity_<wbr>providers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of short names of one or more capacity providers to associate with the cluster. Valid values also include `FARGATE` and `FARGATE_SPOT`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>capacity_<wbr>provider_<wbr>strategies</td>
            <td class="align-top">
                
                <code><a href="#clusterdefaultcapacityproviderstrategy">List[Cluster<wbr>Default<wbr>Capacity<wbr>Provider<wbr>Strategy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The capacity provider strategy to use by default for the cluster. Can be one or more.  Defined below.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#clustersetting">List[Cluster<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
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
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClusterDefaultCapacityProviderStrategy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterDefaultCapacityProviderStrategy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterDefaultCapacityProviderStrategy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterDefaultCapacityProviderStrategyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterDefaultCapacityProviderStrategyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterDefaultCapacityProviderStrategyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterDefaultCapacityProviderStrategy.html">output</a> API doc for this type.
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
            <td class="align-top">Base</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weight</td>
            <td class="align-top">
                
                <code>int?</code>
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
            <td class="align-top">Base</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weight</td>
            <td class="align-top">
                
                <code>*int</code>
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
            <td class="align-top">base</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Provider</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weight</td>
            <td class="align-top">
                
                <code>number?</code>
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
            <td class="align-top">base</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Provider</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weight</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterSetting
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterSetting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterSetting">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterSettingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ecs?tab=doc#ClusterSettingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterSettingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ecs.ClusterSetting.html">output</a> API doc for this type.
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
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
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







