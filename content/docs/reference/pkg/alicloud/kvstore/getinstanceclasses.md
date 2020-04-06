
---
title: "GetInstanceClasses"
block_external_search_index: true
---



This data source provides the KVStore instance classes resource available info of Alibaba Cloud.

> **NOTE:** Available in v1.49.0+

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/kvstore_instance_classes.html.markdown.





## Using GetInstanceClasses

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getInstanceClasses<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/kvstore/#GetInstanceClassesArgs">GetInstanceClassesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/kvstore/#GetInstanceClassesResult">GetInstanceClassesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_instance_classes(</span>architecture=None<span class="p">, </span>edition_type=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>instance_charge_type=None<span class="p">, </span>node_type=None<span class="p">, </span>output_file=None<span class="p">, </span>package_type=None<span class="p">, </span>performance_type=None<span class="p">, </span>series_type=None<span class="p">, </span>shard_number=None<span class="p">, </span>sorted_by=None<span class="p">, </span>storage_type=None<span class="p">, </span>zone_id=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupInstanceClasses<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/kvstore?tab=doc#LookupInstanceClassesArgs">LookupInstanceClassesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/kvstore?tab=doc#LookupInstanceClassesResult">LookupInstanceClassesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetInstanceClasses </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Kvstore.GetInstanceClassesResult.html">GetInstanceClassesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.KVStore.GetInstanceClassesArgs.html">GetInstanceClassesArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance system architecture required by the user. Valid values: `standard`, `cluster` and `rwsplit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance edition type required by the user. Valid values: `Community` and `Enterprise`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter the results by charge type. Valid values: `PrePaid` and `PostPaid`. Default to `PrePaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance node type required by the user. Valid values: `double`, `single`, `readone`, `readthree` and `readfive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance series type required by the user. Valid values: `enhanced_performance_type` and `hybrid_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of shard.Valid values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the KVStore instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The KVStore instance system architecture required by the user. Valid values: `standard`, `cluster` and `rwsplit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The KVStore instance edition type required by the user. Valid values: `Community` and `Enterprise`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Filter the results by charge type. Valid values: `PrePaid` and `PostPaid`. Default to `PrePaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The KVStore instance node type required by the user. Valid values: `double`, `single`, `readone`, `readthree` and `readfive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The KVStore instance series type required by the user. Valid values: `enhanced_performance_type` and `hybrid_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of shard.Valid values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the KVStore instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance system architecture required by the user. Valid values: `standard`, `cluster` and `rwsplit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance edition type required by the user. Valid values: `Community` and `Enterprise`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Filter the results by charge type. Valid values: `PrePaid` and `PostPaid`. Default to `PrePaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance node type required by the user. Valid values: `double`, `single`, `readone`, `readthree` and `readfive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KVStore instance series type required by the user. Valid values: `enhanced_performance_type` and `hybrid_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of shard.Valid values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the KVStore instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The KVStore instance system architecture required by the user. Valid values: `standard`, `cluster` and `rwsplit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The KVStore instance edition type required by the user. Valid values: `Community` and `Enterprise`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `Redis`, `Memcache`. Default to `Redis`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database version required by the user. Value options of Redis can refer to the latest docs [detail info](https://www.alibabacloud.com/help/doc-detail/60873.htm) `EngineVersion`. Value of Memcache should be empty.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Filter the results by charge type. Valid values: `PrePaid` and `PostPaid`. Default to `PrePaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The KVStore instance node type required by the user. Valid values: `double`, `single`, `readone`, `readthree` and `readfive`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>package_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>performance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>series_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The KVStore instance series type required by the user. Valid values: `enhanced_performance_type` and `hybrid_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shard_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of shard.Valid values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sorted_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.68.0. 
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the KVStore instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetInstanceClasses Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Classes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceclassesclass">List&lt;Get<wbr>Instance<wbr>Classes<wbr>Class&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes when the `sorted_by` is "Price". include:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Classes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Classes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceclassesclass">[]Get<wbr>Instance<wbr>Classes<wbr>Class</a></span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes when the `sorted_by` is "Price". include:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Classes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>classes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceclassesclass">Get<wbr>Instance<wbr>Classes<wbr>Class[]</a></span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes when the `sorted_by` is "Price". include:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>edition<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Classes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>package<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>performance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>series<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shard<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sorted<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>architecture</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>classes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getinstanceclassesclass">List[Get<wbr>Instance<wbr>Classes<wbr>Class]</a></span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes when the `sorted_by` is "Price". include:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>edition_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>classes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of KVStore available instance classes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>package_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;package_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>performance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;performance_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>series_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shard_<wbr>number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sorted_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}<p class="property-message">Deprecated: {{% md %}}The parameter &#39;storage_type&#39; has been deprecated from 1.68.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Instance<wbr>Classes<wbr>Class</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetInstanceClassesClass">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/kvstore?tab=doc#GetInstanceClassesClass">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}KVStore available instance class.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}KVStore available instance class.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}KVStore available instance class.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}KVStore available instance class.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







