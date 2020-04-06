
---
title: "KubernetesAutoscaler"
block_external_search_index: true
---



This resource will help you to manager cluster-autoscaler in Kubernetes Cluster. 

> **NOTE:** The scaling group must use CentOS7 or AliyunLinux2 as base image.

> **NOTE:** The cluster-autoscaler can only use the same size of instanceTypes in one scaling group. 

> **NOTE:** Add Policy to RAM role of the node to deploy cluster-autoscaler if you need.

> **NOTE:** Available in 1.65.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cs_kubernetes_autoscaler.html.markdown.



## Create a KubernetesAutoscaler Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cs/#KubernetesAutoscaler">KubernetesAutoscaler</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cs/#KubernetesAutoscalerArgs">KubernetesAutoscalerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">KubernetesAutoscaler</span><span class="p">(resource_name, opts=None, </span>cluster_id=None<span class="p">, </span>cool_down_duration=None<span class="p">, </span>defer_scale_in_duration=None<span class="p">, </span>nodepools=None<span class="p">, </span>utilization=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewKubernetesAutoscaler<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscalerArgs">KubernetesAutoscalerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscaler">KubernetesAutoscaler</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cs.KubernetesAutoscaler.html">KubernetesAutoscaler</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.CS.KubernetesAutoscalerArgs.html">KubernetesAutoscalerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List&lt;Kubernetes<wbr>Autoscaler<wbr>Nodepool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">[]Kubernetes<wbr>Autoscaler<wbr>Nodepool</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">Kubernetes<wbr>Autoscaler<wbr>Nodepool[]?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cool_<wbr>down_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defer_<wbr>scale_<wbr>in_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List[Kubernetes<wbr>Autoscaler<wbr>Nodepool]</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## KubernetesAutoscaler Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List&lt;Kubernetes<wbr>Autoscaler<wbr>Nodepool&gt;?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">[]Kubernetes<wbr>Autoscaler<wbr>Nodepool</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">Kubernetes<wbr>Autoscaler<wbr>Nodepool[]?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cool_<wbr>down_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defer_<wbr>scale_<wbr>in_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List[Kubernetes<wbr>Autoscaler<wbr>Nodepool]</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing KubernetesAutoscaler Resource

Get an existing KubernetesAutoscaler resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cs/#KubernetesAutoscalerState">KubernetesAutoscalerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/cs/#KubernetesAutoscaler">KubernetesAutoscaler</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cluster_id=None<span class="p">, </span>cool_down_duration=None<span class="p">, </span>defer_scale_in_duration=None<span class="p">, </span>nodepools=None<span class="p">, </span>utilization=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetKubernetesAutoscaler<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscalerState">KubernetesAutoscalerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscaler">KubernetesAutoscaler</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cs.KubernetesAutoscaler.html">KubernetesAutoscaler</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Cs.KubernetesAutoscalerState.html">KubernetesAutoscalerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List&lt;Kubernetes<wbr>Autoscaler<wbr>Nodepool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">[]Kubernetes<wbr>Autoscaler<wbr>Nodepool</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cool<wbr>Down<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defer<wbr>Scale<wbr>In<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">Kubernetes<wbr>Autoscaler<wbr>Nodepool[]?</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of kubernetes cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cool_<wbr>down_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cool_down_duration option of cluster-autoscaler.  
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defer_<wbr>scale_<wbr>in_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The defer_scale_in_duration option of cluster-autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nodepools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#kubernetesautoscalernodepool">List[Kubernetes<wbr>Autoscaler<wbr>Nodepool]</a></span>
    </dt>
    <dd>{{% md %}}
* `nodepools.id` - (Required) The scaling group id of the groups configured for cluster-autoscaler.
* `nodepools.taints` - (Required) The taints for the nodes in scaling group.
* `nodepools.labels` - (Required) The labels for the nodes in scaling group.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The utilization option of cluster-autoscaler.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Kubernetes<wbr>Autoscaler<wbr>Nodepool</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#KubernetesAutoscalerNodepool">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#KubernetesAutoscalerNodepool">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscalerNodepoolArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/cs?tab=doc#KubernetesAutoscalerNodepoolOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

