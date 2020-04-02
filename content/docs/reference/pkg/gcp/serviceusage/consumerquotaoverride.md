
---
title: "ConsumerQuotaOverride"
block_external_search_index: true
---

A consumer override is applied to the consumer on its own authority to limit its own quota usage.
Consumer overrides cannot be used to grant more quota than would be allowed by admin overrides,
producer overrides, or the default limit of the service.

To get more information about ConsumerQuotaOverride, see:

* How-to Guides
    * [Getting Started](https://cloud.google.com/service-usage/docs/getting-started)
    * [REST API documentation](https://cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.consumerOverrides)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_usage_consumer_quota_override.html.markdown.



## Create a ConsumerQuotaOverride Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/serviceusage/#ConsumerQuotaOverride">ConsumerQuotaOverride</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/serviceusage/#ConsumerQuotaOverrideArgs">ConsumerQuotaOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ConsumerQuotaOverride</span><span class="p">(resource_name, opts=None, </span>dimensions=None<span class="p">, </span>force=None<span class="p">, </span>limit=None<span class="p">, </span>metric=None<span class="p">, </span>override_value=None<span class="p">, </span>project=None<span class="p">, </span>service=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewConsumerQuotaOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/serviceusage?tab=doc#ConsumerQuotaOverrideArgs">ConsumerQuotaOverrideArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/serviceusage?tab=doc#ConsumerQuotaOverride">ConsumerQuotaOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Serviceusage.ConsumerQuotaOverride.html">ConsumerQuotaOverride</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.ServiceUsage.ConsumerQuotaOverrideArgs.html">ConsumerQuotaOverrideArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>override_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ConsumerQuotaOverride Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ConsumerQuotaOverride Resource

Get an existing ConsumerQuotaOverride resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/serviceusage/#ConsumerQuotaOverrideState">ConsumerQuotaOverrideState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/serviceusage/#ConsumerQuotaOverride">ConsumerQuotaOverride</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>dimensions=None<span class="p">, </span>force=None<span class="p">, </span>limit=None<span class="p">, </span>metric=None<span class="p">, </span>name=None<span class="p">, </span>override_value=None<span class="p">, </span>project=None<span class="p">, </span>service=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetConsumerQuotaOverride<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/serviceusage?tab=doc#ConsumerQuotaOverrideState">ConsumerQuotaOverrideState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/serviceusage?tab=doc#ConsumerQuotaOverride">ConsumerQuotaOverride</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Serviceusage.ConsumerQuotaOverride.html">ConsumerQuotaOverride</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Serviceusage.ConsumerQuotaOverrideState.html">ConsumerQuotaOverrideState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>dimensions</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If the new quota would decrease the existing quota by more than 10%, the request is rejected. If 'force' is 'true', that
safety check is ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The limit on the metric, e.g. '/project/region'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The metric that should be limited, e.g. 'compute.googleapis.com/cpus'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The server-generated name of the quota override.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service that the metrics belong to, e.g. 'compute.googleapis.com'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
