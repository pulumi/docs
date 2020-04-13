
---
title: "HorizontalPodAutoscaler"
block_external_search_index: true
---



HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified.


## Create a HorizontalPodAutoscaler Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/autoscaling/v2beta1/#HorizontalPodAutoscaler">HorizontalPodAutoscaler</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/autoscaling/v2beta1/#HorizontalPodAutoscalerArgs">HorizontalPodAutoscalerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">HorizontalPodAutoscaler</span><span class="p">(resource_name, opts=None, </span>metadata=None<span class="p">, </span>spec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewHorizontalPodAutoscaler<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscalerArgs">HorizontalPodAutoscalerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscaler">HorizontalPodAutoscaler</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Autoscaling.V2Beta1.HorizontalPodAutoscaler.html">HorizontalPodAutoscaler</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Kubernetes/Pulumi.Kubernetes.Autoscaling.V2Beta1.HorizontalPodAutoscalerArgs.html">HorizontalPodAutoscalerArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">*Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Dict[Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## HorizontalPodAutoscaler Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerstatus">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}status is the current information about the autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">*Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerstatus">*Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}status is the current information about the autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Object<wbr>Meta?</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec?</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerstatus">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}status is the current information about the autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmeta">Dict[Object<wbr>Meta]</a></span>
    </dt>
    <dd>{{% md %}}metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerspec">Dict[Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalerstatus">Dict[Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}status is the current information about the autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}












## Supporting Types

<h4>Cross<wbr>Version<wbr>Object<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#CrossVersionObjectReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#CrossVersionObjectReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#CrossVersionObjectReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#CrossVersionObjectReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>External<wbr>Metric<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ExternalMetricSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ExternalMetricSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ExternalMetricSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ExternalMetricSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>External<wbr>Metric<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ExternalMetricStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ExternalMetricStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of metric averaged over autoscaled pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of a metric used for autoscaling in metric system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of metric averaged over autoscaled pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of a metric used for autoscaling in metric system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of metric averaged over autoscaled pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of a metric used for autoscaling in metric system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of metric averaged over autoscaled pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of a metric used for autoscaling in metric system.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}metricSelector is used to identify a specific time series within a given metric.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HorizontalPodAutoscalerCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscalerConditionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}lastTransitionTime is the last time the condition transitioned from one status to another{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}message is a human-readable explanation containing details about the transition{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}reason is the reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}status is the status of the condition (True, False, Unknown){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type describes the current condition{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}lastTransitionTime is the last time the condition transitioned from one status to another{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}message is a human-readable explanation containing details about the transition{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}reason is the reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}status is the status of the condition (True, False, Unknown){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}type describes the current condition{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}lastTransitionTime is the last time the condition transitioned from one status to another{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}message is a human-readable explanation containing details about the transition{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}reason is the reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}status is the status of the condition (True, False, Unknown){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type describes the current condition{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Transition<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}lastTransitionTime is the last time the condition transitioned from one status to another{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}message is a human-readable explanation containing details about the transition{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reason</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}reason is the reason for the condition's last transition.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}status is the status of the condition (True, False, Unknown){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}type describes the current condition{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#HorizontalPodAutoscalerSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HorizontalPodAutoscalerSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscalerSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscalerSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricspec">List&lt;Metric<wbr>Spec<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>Target<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricspec">[]Metric<wbr>Spec</a></span>
    </dt>
    <dd>{{% md %}}metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scale<wbr>Target<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">*Cross<wbr>Version<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricspec">Metric<wbr>Spec[]?</a></span>
    </dt>
    <dd>{{% md %}}metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale<wbr>Target<wbr>Ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricspec">List[Metric<wbr>Spec]</a></span>
    </dt>
    <dd>{{% md %}}metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scale_<wbr>target_<wbr>ref</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Dict[Cross<wbr>Version<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#HorizontalPodAutoscalerStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#HorizontalPodAutoscalerStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalercondition">List&lt;Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Condition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricstatus">List&lt;Metric<wbr>Status<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}currentMetrics is the last read state of the metrics used by this autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Scale<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}observedGeneration is the most recent generation observed by this autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalercondition">[]Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricstatus">[]Metric<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}currentMetrics is the last read state of the metrics used by this autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Scale<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}observedGeneration is the most recent generation observed by this autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalercondition">Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Condition[]?</a></span>
    </dt>
    <dd>{{% md %}}conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricstatus">Metric<wbr>Status[]?</a></span>
    </dt>
    <dd>{{% md %}}currentMetrics is the last read state of the metrics used by this autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired<wbr>Replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Scale<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>observed<wbr>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}observedGeneration is the most recent generation observed by this autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#horizontalpodautoscalercondition">List[Horizontal<wbr>Pod<wbr>Autoscaler<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current_<wbr>metrics</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#metricstatus">List[Metric<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}currentMetrics is the last read state of the metrics used by this autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired_<wbr>replicas</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>scale_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>observed_<wbr>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}observedGeneration is the most recent generation observed by this autoscaler.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Label<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LabelSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LabelSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">List&lt;Label<wbr>Selector<wbr>Requirement<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">Label<wbr>Selector<wbr>Requirement</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">Label<wbr>Selector<wbr>Requirement[]?</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>expressions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselectorrequirement">List[Label<wbr>Selector<wbr>Requirement]</a></span>
    </dt>
    <dd>{{% md %}}matchExpressions is a list of label selector requirements. The requirements are ANDed.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Label<wbr>Selector<wbr>Requirement</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#LabelSelectorRequirement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#LabelSelectorRequirement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorRequirementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#LabelSelectorRequirementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}key is the label key that the selector applies to.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Managed<wbr>Fields<wbr>Entry</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ManagedFieldsEntry">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ManagedFieldsEntry">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ManagedFieldsEntryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ManagedFieldsEntryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;?</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fields<wbr>V1</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>manager</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Manager is an identifier of the workflow managing these fields.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Metric<wbr>Spec</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#MetricSpec">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#MetricSpec">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#MetricSpecArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#MetricSpecOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricsource">External<wbr>Metric<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricsource">Object<wbr>Metric<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricsource">Pods<wbr>Metric<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricsource">Resource<wbr>Metric<wbr>Source<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricsource">*External<wbr>Metric<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricsource">*Object<wbr>Metric<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricsource">*Pods<wbr>Metric<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricsource">*Resource<wbr>Metric<wbr>Source</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricsource">External<wbr>Metric<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricsource">Object<wbr>Metric<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricsource">Pods<wbr>Metric<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricsource">Resource<wbr>Metric<wbr>Source?</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricsource">Dict[External<wbr>Metric<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricsource">Dict[Object<wbr>Metric<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricsource">Dict[Pods<wbr>Metric<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricsource">Dict[Resource<wbr>Metric<wbr>Source]</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It should be one of "Object", "Pods" or "Resource", each mapping to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Metric<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#MetricStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#MetricStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricstatus">External<wbr>Metric<wbr>Status<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricstatus">Object<wbr>Metric<wbr>Status<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricstatus">Pods<wbr>Metric<wbr>Status<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricstatus">Resource<wbr>Metric<wbr>Status<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricstatus">*External<wbr>Metric<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricstatus">*Object<wbr>Metric<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricstatus">*Pods<wbr>Metric<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricstatus">*Resource<wbr>Metric<wbr>Status</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricstatus">External<wbr>Metric<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricstatus">Object<wbr>Metric<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricstatus">Pods<wbr>Metric<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricstatus">Resource<wbr>Metric<wbr>Status?</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#externalmetricstatus">Dict[External<wbr>Metric<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#objectmetricstatus">Dict[Object<wbr>Metric<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pods</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#podsmetricstatus">Dict[Pods<wbr>Metric<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resourcemetricstatus">Dict[Resource<wbr>Metric<wbr>Status]</a></span>
    </dt>
    <dd>{{% md %}}resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}type is the type of metric source.  It will be one of "Object", "Pods" or "Resource", each corresponds to a matching field in the object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Object<wbr>Meta</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ObjectMeta">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectMeta">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ObjectMetaArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#ObjectMetaOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;?</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;?</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">List&lt;Managed<wbr>Fields<wbr>Entry<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">List&lt;Owner<wbr>Reference<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">Managed<wbr>Fields<wbr>Entry</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">Owner<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Grace<wbr>Period<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">Managed<wbr>Fields<wbr>Entry[]?</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner<wbr>References</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">Owner<wbr>Reference[]?</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>grace_<wbr>period_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deletion_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.

Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>finalizers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generate_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.

If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).

Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed_<wbr>fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#managedfieldsentry">List[Managed<wbr>Fields<wbr>Entry]</a></span>
    </dt>
    <dd>{{% md %}}ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Namespace defines the space within each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.

Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner_<wbr>references</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#ownerreference">List[Owner<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.

Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SelfLink is a URL representing this object. Populated by the system. Read-only.

DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.

Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Object<wbr>Metric<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ObjectMetricSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectMetricSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ObjectMetricSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ObjectMetricSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}averageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}averageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">*Cross<wbr>Version<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}averageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity).{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}averageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Dict[Cross<wbr>Version<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}targetValue is the target value of the metric (as a quantity).{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Object<wbr>Metric<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ObjectMetricStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ObjectMetricStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}averageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the ObjectMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}averageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the ObjectMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">*Cross<wbr>Version<wbr>Object<wbr>Reference</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}averageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the ObjectMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Cross<wbr>Version<wbr>Object<wbr>Reference?</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}averageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}currentValue is the current value of the metric (as a quantity).{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the ObjectMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#crossversionobjectreference">Dict[Cross<wbr>Version<wbr>Object<wbr>Reference]</a></span>
    </dt>
    <dd>{{% md %}}target is the described Kubernetes object.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Owner<wbr>Reference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#OwnerReference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#OwnerReference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#OwnerReferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/meta/v1?tab=doc#OwnerReferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>block<wbr>Owner<wbr>Deletion</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If true, this reference points to the managing controller.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pods<wbr>Metric<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#PodsMetricSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodsMetricSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#PodsMetricSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#PodsMetricSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Pods<wbr>Metric<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#PodsMetricStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#PodsMetricStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the PodsMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the PodsMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Label<wbr>Selector?</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the PodsMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity){{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}metricName is the name of the metric in question{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#labelselector">Dict[Label<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the PodsMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Resource<wbr>Metric<wbr>Source</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#ResourceMetricSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ResourceMetricSource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ResourceMetricSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ResourceMetricSourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type.{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Resource<wbr>Metric<wbr>Status</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/kubernetes/types/output/#ResourceMetricStatus">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-kubernetes/sdk/go/kubernetes/autoscaling/v2beta1?tab=doc#ResourceMetricStatusOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type. It will always be set, regardless of the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type. It will always be set, regardless of the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type. It will always be set, regardless of the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Utilization</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Average<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the "pods" metric source type. It will always be set, regardless of the corresponding metric specification.{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name is the name of the resource in question.{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-kubernetes">https://github.com/pulumi/pulumi-kubernetes</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

