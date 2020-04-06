
---
title: "GetScalingConfigurations"
block_external_search_index: true
---



This data source provides available scaling configuration resources. 

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/ess_scaling_configurations.html.markdown.





## Using GetScalingConfigurations

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getScalingConfigurations<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#GetScalingConfigurationsArgs">GetScalingConfigurationsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#GetScalingConfigurationsResult">GetScalingConfigurationsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_scaling_configurations(</span>ids=None<span class="p">, </span>name_regex=None<span class="p">, </span>output_file=None<span class="p">, </span>scaling_group_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupScalingConfigurations<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#LookupScalingConfigurationsArgs">LookupScalingConfigurationsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#LookupScalingConfigurationsResult">LookupScalingConfigurationsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetScalingConfigurations </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.GetScalingConfigurationsResult.html">GetScalingConfigurationsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.GetScalingConfigurationsArgs.html">GetScalingConfigurationsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter resulting scaling configurations by name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter resulting scaling configurations by name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter resulting scaling configurations by name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration IDs.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter resulting scaling configurations by name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetScalingConfigurations Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfiguration">List&lt;Get<wbr>Scaling<wbr>Configurations<wbr>Configuration&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of scaling rules. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfiguration">[]Get<wbr>Scaling<wbr>Configurations<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A list of scaling rules. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfiguration">Get<wbr>Scaling<wbr>Configurations<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}A list of scaling rules. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfiguration">List[Get<wbr>Scaling<wbr>Configurations<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A list of scaling rules. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of scaling configuration names.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the scaling group.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Scaling<wbr>Configurations<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetScalingConfigurationsConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#GetScalingConfigurationsConfiguration">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation time of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfigurationdatadisk">List&lt;Get<wbr>Scaling<wbr>Configurations<wbr>Configuration<wbr>Data<wbr>Disk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Data disks of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Image ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internet charge type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Max<wbr>Bandwidth<wbr>In</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth in of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Max<wbr>Bandwidth<wbr>Out</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lifecycle<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lifecycle state of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security group ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>System<wbr>Disk<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}System disk category of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>System<wbr>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}System disk size of the scaling configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation time of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfigurationdatadisk">[]Get<wbr>Scaling<wbr>Configurations<wbr>Configuration<wbr>Data<wbr>Disk</a></span>
    </dt>
    <dd>{{% md %}}Data disks of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Image ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internet charge type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Max<wbr>Bandwidth<wbr>In</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth in of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Internet<wbr>Max<wbr>Bandwidth<wbr>Out</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lifecycle<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lifecycle state of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security group ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>System<wbr>Disk<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}System disk category of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>System<wbr>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}System disk size of the scaling configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creation time of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>data<wbr>Disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfigurationdatadisk">Get<wbr>Scaling<wbr>Configurations<wbr>Configuration<wbr>Data<wbr>Disk[]</a></span>
    </dt>
    <dd>{{% md %}}Data disks of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the scaling rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Image ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Internet charge type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet<wbr>Max<wbr>Bandwidth<wbr>In</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth in of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet<wbr>Max<wbr>Bandwidth<wbr>Out</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lifecycle<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Lifecycle state of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scaling<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Security group ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>system<wbr>Disk<wbr>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}System disk category of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>system<wbr>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}System disk size of the scaling configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creation time of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>data_<wbr>disks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getscalingconfigurationsconfigurationdatadisk">List[Get<wbr>Scaling<wbr>Configurations<wbr>Configuration<wbr>Data<wbr>Disk]</a></span>
    </dt>
    <dd>{{% md %}}Data disks of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the scaling rule.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Image ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Internet charge type of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet_<wbr>max_<wbr>bandwidth_<wbr>in</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth in of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>internet_<wbr>max_<wbr>bandwidth_<wbr>out</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Internet max bandwidth of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lifecycle<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Lifecycle state of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scaling_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Scaling group id the scaling configurations belong to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Security group ID of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>system_<wbr>disk_<wbr>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}System disk category of the scaling configuration.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>system_<wbr>disk_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}System disk size of the scaling configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Scaling<wbr>Configurations<wbr>Configuration<wbr>Data<wbr>Disk</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetScalingConfigurationsConfigurationDataDisk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#GetScalingConfigurationsConfigurationDataDisk">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Category of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>With<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Delete_with_instance attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Device attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Category</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Category of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>With<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Delete_with_instance attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Device attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Category of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>With<wbr>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Delete_with_instance attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Device attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>category</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Category of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>with_<wbr>instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Delete_with_instance attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>device</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Device attribute of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Size of data disk.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







