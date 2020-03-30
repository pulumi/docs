
---
title: "GetCache"
block_external_search_index: true
---

Use this data source to access information about an existing Redis Cache

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/redis_cache.html.markdown.





## Using GetCache

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getCache<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/redis/#GetCacheArgs">GetCacheArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/redis/#GetCacheResult">GetCacheResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_cache(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>zones=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupCache<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/redis?tab=doc#LookupCacheArgs">LookupCacheArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/redis?tab=doc#LookupCacheResult">LookupCacheResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetCache </span><span class="p">{</span><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Redis.GetCacheResult.html">GetCacheResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Redis.Inputs.GetCacheArgs.html">GetCacheArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis cache
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group the Redis cache instance is located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis cache
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group the Redis cache instance is located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis cache
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group the Redis cache instance is located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Redis cache
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group the Redis cache instance is located in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetCache Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the Redis Cache deployed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Non<wbr>Ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the SSL port is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Family</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU family/pricing group used. Possible values are `C` (for Basic/Standard SKU family) and `P` (for `Premium`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname of the Redis Instance
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
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the Redis Cache.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Minimum<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The minimum TLS version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Patch<wbr>Schedules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcachepatchschedule">List&lt;Get<wbr>Cache<wbr>Patch<wbr>Schedule&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of `patch_schedule` blocks as defined below - only available for Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The non-SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The primary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Static<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redis<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcacheredisconfiguration">List&lt;Get<wbr>Cache<wbr>Redis<wbr>Configuration&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `redis_configuration` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secondary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shard<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU of Redis used. Possible values are `Basic`, `Standard` and `Premium`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The size of the Redis Cache deployed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Non<wbr>Ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the SSL port is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Family</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU family/pricing group used. Possible values are `C` (for Basic/Standard SKU family) and `P` (for `Premium`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname of the Redis Instance
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
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the Redis Cache.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Minimum<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The minimum TLS version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Patch<wbr>Schedules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcachepatchschedule">[]Get<wbr>Cache<wbr>Patch<wbr>Schedule</a></span>
    </dt>
    <dd>{{% md %}}A list of `patch_schedule` blocks as defined below - only available for Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The non-SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Primary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The primary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Static<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redis<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcacheredisconfiguration">[]Get<wbr>Cache<wbr>Redis<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A `redis_configuration` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Secondary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secondary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shard<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU of Redis used. Possible values are `Basic`, `Standard` and `Premium`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The size of the Redis Cache deployed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Non<wbr>Ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the SSL port is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>family</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU family/pricing group used. Possible values are `C` (for Basic/Standard SKU family) and `P` (for `Premium`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Hostname of the Redis Instance
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
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location of the Redis Cache.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>minimum<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The minimum TLS version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>patch<wbr>Schedules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcachepatchschedule">Get<wbr>Cache<wbr>Patch<wbr>Schedule[]</a></span>
    </dt>
    <dd>{{% md %}}A list of `patch_schedule` blocks as defined below - only available for Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The non-SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Primary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The primary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Static<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redis<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcacheredisconfiguration">Get<wbr>Cache<wbr>Redis<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}A `redis_configuration` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary<wbr>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Secondary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The secondary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shard<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SKU of Redis used. Possible values are `Basic`, `Standard` and `Premium`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssl<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size of the Redis Cache deployed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>non_<wbr>ssl_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the SSL port is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>family</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SKU family/pricing group used. Possible values are `C` (for Basic/Standard SKU family) and `P` (for `Premium`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Hostname of the Redis Instance
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
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location of the Redis Cache.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>minimum_<wbr>tls_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The minimum TLS version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>patch_<wbr>schedules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcachepatchschedule">List[Get<wbr>Cache<wbr>Patch<wbr>Schedule]</a></span>
    </dt>
    <dd>{{% md %}}A list of `patch_schedule` blocks as defined below - only available for Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The non-SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary_<wbr>access_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Primary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>primary_<wbr>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The primary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>static_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redis_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getcacheredisconfiguration">List[Get<wbr>Cache<wbr>Redis<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A `redis_configuration` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary_<wbr>access_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Secondary Access Key for the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>secondary_<wbr>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secondary connection string of the Redis Instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shard_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SKU of Redis used. Possible values are `Basic`, `Standard` and `Premium`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssl_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The SSL Port of the Redis Instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zones</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

#### Get&lt;wbr&gt;Cache&lt;wbr&gt;Patch&lt;wbr&gt;Schedule
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetCachePatchSchedule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/redis?tab=doc#GetCachePatchSchedule">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Day<wbr>Of<wbr>Week</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Weekday name for the patch item
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Hour<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Start Hour for maintenance in UTC
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Day<wbr>Of<wbr>Week</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Weekday name for the patch item
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Hour<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Start Hour for maintenance in UTC
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>day<wbr>Of<wbr>Week</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}the Weekday name for the patch item
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Hour<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Start Hour for maintenance in UTC
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>day<wbr>Of<wbr>Week</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the Weekday name for the patch item
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Hour<wbr>Utc</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Start Hour for maintenance in UTC
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





#### Get&lt;wbr&gt;Cache&lt;wbr&gt;Redis&lt;wbr&gt;Configuration
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetCacheRedisConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/redis?tab=doc#GetCacheRedisConfiguration">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Storage<wbr>Connection<wbr>String0</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Storage<wbr>Connection<wbr>String1</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if authentication is enabled
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxclients</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxfragmentationmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Value in megabytes reserved to accommodate for memory fragmentation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Delta</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max-memory delta for this Redis instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How Redis will select what to remove when `maxmemory` is reached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The value in megabytes reserved for non-cache usage e.g. failover
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Notify<wbr>Keyspace<wbr>Events</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Backup Enabled? Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Backup Frequency in Minutes. Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Max<wbr>Snapshot<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of snapshots that can be created as a backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Storage<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Connection String to the Storage Account. Only supported for Premium SKU's.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Storage<wbr>Connection<wbr>String0</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Aof<wbr>Storage<wbr>Connection<wbr>String1</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if authentication is enabled
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxclients</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxfragmentationmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Value in megabytes reserved to accommodate for memory fragmentation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Delta</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max-memory delta for this Redis instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How Redis will select what to remove when `maxmemory` is reached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maxmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The value in megabytes reserved for non-cache usage e.g. failover
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Notify<wbr>Keyspace<wbr>Events</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Backup Enabled? Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Backup Frequency in Minutes. Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Backup<wbr>Max<wbr>Snapshot<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of snapshots that can be created as a backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rdb<wbr>Storage<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Connection String to the Storage Account. Only supported for Premium SKU's.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Storage<wbr>Connection<wbr>String0</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Storage<wbr>Connection<wbr>String1</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies if authentication is enabled
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxclients</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxfragmentationmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Value in megabytes reserved to accommodate for memory fragmentation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Delta</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max-memory delta for this Redis instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How Redis will select what to remove when `maxmemory` is reached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The value in megabytes reserved for non-cache usage e.g. failover
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>notify<wbr>Keyspace<wbr>Events</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is Backup Enabled? Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Backup Frequency in Minutes. Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Max<wbr>Snapshot<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of snapshots that can be created as a backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Storage<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Connection String to the Storage Account. Only supported for Premium SKU's.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Storage<wbr>Connection<wbr>String0</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>aof<wbr>Storage<wbr>Connection<wbr>String1</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Authentication</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if authentication is enabled
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxclients</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxfragmentationmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Value in megabytes reserved to accommodate for memory fragmentation.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Delta</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max-memory delta for this Redis instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How Redis will select what to remove when `maxmemory` is reached.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maxmemory<wbr>Reserved</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The value in megabytes reserved for non-cache usage e.g. failover
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>notify<wbr>Keyspace<wbr>Events</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is Backup Enabled? Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Backup Frequency in Minutes. Only supported on Premium SKU's.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Backup<wbr>Max<wbr>Snapshot<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of snapshots that can be created as a backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rdb<wbr>Storage<wbr>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Connection String to the Storage Account. Only supported for Premium SKU's.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







