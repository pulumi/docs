
---
title: "Instance"
block_external_search_index: true
---

A Google Cloud Redis instance.


To get more information about Instance, see:

* [API documentation](https://cloud.google.com/memorystore/docs/redis/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/memorystore/docs/redis/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/redis_instance.html.markdown.



## Create a Instance Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/redis/#Instance">Instance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/redis/#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Instance</span><span class="p">(resource_name, opts=None, </span>alternative_location_id=None<span class="p">, </span>authorized_network=None<span class="p">, </span>connect_mode=None<span class="p">, </span>display_name=None<span class="p">, </span>labels=None<span class="p">, </span>location_id=None<span class="p">, </span>memory_size_gb=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>redis_configs=None<span class="p">, </span>redis_version=None<span class="p">, </span>region=None<span class="p">, </span>reserved_ip_range=None<span class="p">, </span>tier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/redis?tab=doc#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/redis?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Redis.Instance.html">Instance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Redis.InstanceArgs.html">InstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
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
        <span>redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative_<wbr>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>memory_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
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
        <span>redis_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redis_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved_<wbr>ip_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Instance Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>alternative_<wbr>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authorized_<wbr>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connect_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>current_<wbr>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>memory_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>redis_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>redis_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>reserved_<wbr>ip_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Instance Resource

Get an existing Instance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/redis/#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/redis/#Instance">Instance</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>alternative_location_id=None<span class="p">, </span>authorized_network=None<span class="p">, </span>connect_mode=None<span class="p">, </span>create_time=None<span class="p">, </span>current_location_id=None<span class="p">, </span>display_name=None<span class="p">, </span>host=None<span class="p">, </span>labels=None<span class="p">, </span>location_id=None<span class="p">, </span>memory_size_gb=None<span class="p">, </span>name=None<span class="p">, </span>port=None<span class="p">, </span>project=None<span class="p">, </span>redis_configs=None<span class="p">, </span>redis_version=None<span class="p">, </span>region=None<span class="p">, </span>reserved_ip_range=None<span class="p">, </span>tier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/redis?tab=doc#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/redis?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Redis.Instance.html">Instance</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Redis.InstanceState.html">InstanceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Host</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>Redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current<wbr>Location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>redis<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redis<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved<wbr>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alternative_<wbr>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Only applicable to STANDARD_HA tier which protects the instance against zonal failures by provisioning it across two
zones. If provided, it must be a different zone from the one provided in [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The full name of the Google Compute Engine network to which the instance is connected. If left unspecified, the default
network will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The connection mode of the Redis instance. Can be either 'DIRECT_PEERING' or 'PRIVATE_SERVICE_ACCESS'. The default
connect mode if not provided is 'DIRECT_PEERING'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>current_<wbr>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
[locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
[alternativeLocationId] and can change after a failover event.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An arbitrary and optional user-provided name for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>host</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Resource labels to represent user provided metadata.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone where the instance will be provisioned. If not provided, the service will choose a zone for the instance. For
STANDARD_HA tier, instances will be created across two zones for protection against zonal failures. If
[alternativeLocationId] is also provided, it must be different from [locationId].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Redis memory size in GiB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the instance or a fully qualified identifier for the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port number of the exposed Redis endpoint.
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
        <span>redis_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Redis configuration parameters, according to http://redis.io/topics/config. Please check Memorystore documentation for
the list of supported parameters:
https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>redis_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values
are: - REDIS_4_0 for Redis 4.0 compatibility - REDIS_3_2 for Redis 3.2 compatibility
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Redis region of the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>reserved_<wbr>ip_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The CIDR range of internal addresses that are reserved for this instance. If not provided, the service will choose an
unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be unique and non-overlapping with existing
subnets in an authorized network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service tier of the instance. Must be one of these values: - BASIC: standalone instance - STANDARD_HA: highly
available primary/replica instances
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
