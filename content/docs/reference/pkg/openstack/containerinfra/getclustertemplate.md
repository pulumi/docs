
---
title: "GetClusterTemplate"
block_external_search_index: true
---



Use this data source to get the ID of an available OpenStack Magnum cluster
template.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const clustertemplate1 = openstack.containerinfra.getClusterTemplate({
    name: "clustertemplate_1",
});
```

{{% /example %}}
{{% /examples %}}





## Using GetClusterTemplate

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getClusterTemplate<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/containerinfra/#GetClusterTemplateArgs">GetClusterTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/containerinfra/#GetClusterTemplateResult">GetClusterTemplateResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_cluster_template(</span>name=None<span class="p">, </span>region=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupClusterTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/containerinfra?tab=doc#LookupClusterTemplateArgs">LookupClusterTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/containerinfra?tab=doc#LookupClusterTemplateResult">LookupClusterTemplateResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetClusterTemplate </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Containerinfra.GetClusterTemplateResult.html">GetClusterTemplateResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.OpenStack.ContainerInfra.GetClusterTemplateArgs.html">GetClusterTemplateArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the cluster template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 Container Infra
client.
If omitted, the `region` argument of the provider is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the cluster template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 Container Infra
client.
If omitted, the `region` argument of the provider is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the cluster template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 Container Infra
client.
If omitted, the `region` argument of the provider is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the cluster template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V1 Container Infra
client.
If omitted, the `region` argument of the provider is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetClusterTemplate Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Apiserver<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The API server port for the Container Orchestration
Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Distro</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The distro for the cluster (fedora-atomic, coreos, etc.).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Coe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Container Orchestration Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Nameserver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the DNS nameserver that is used in nodes of the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Docker<wbr>Storage<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Docker<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size (in GB) of the Docker volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the external network that will be used for
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fixed<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The fixed network that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fixed<wbr>Subnet</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}=The fixed subnet that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Floating<wbr>Ip<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should create IP
floating IP for every node or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTP requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTPS requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The reference to an image that is used for nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insecure<wbr>Registry</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The insecure registry URL for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Keypair<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Compute service SSH keypair.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing additional properties
of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the master nodes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Lb<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should has a
loadbalancer for master nodes or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver for the container network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of IP addresses that shouldn't be used in
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The project of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether cluster template should be public.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether Docker registry is enabled in the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The server type for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the TLS should be disabled in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The user of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Volume<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver that is used for the volumes of the
cluster nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Apiserver<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The API server port for the Container Orchestration
Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Distro</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The distro for the cluster (fedora-atomic, coreos, etc.).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Coe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Container Orchestration Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Nameserver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the DNS nameserver that is used in nodes of the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Docker<wbr>Storage<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Docker<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size (in GB) of the Docker volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the external network that will be used for
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fixed<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The fixed network that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fixed<wbr>Subnet</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}=The fixed subnet that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Floating<wbr>Ip<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should create IP
floating IP for every node or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTP requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTPS requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The reference to an image that is used for nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Insecure<wbr>Registry</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The insecure registry URL for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Keypair<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Compute service SSH keypair.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing additional properties
of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the master nodes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Lb<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should has a
loadbalancer for master nodes or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver for the container network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of IP addresses that shouldn't be used in
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The project of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether cluster template should be public.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether Docker registry is enabled in the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The server type for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tls<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the TLS should be disabled in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The user of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Volume<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver that is used for the volumes of the
cluster nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>apiserver<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The API server port for the Container Orchestration
Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Distro</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The distro for the cluster (fedora-atomic, coreos, etc.).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>coe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Container Orchestration Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Nameserver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Address of the DNS nameserver that is used in nodes of the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>docker<wbr>Storage<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>docker<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size (in GB) of the Docker volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the external network that will be used for
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fixed<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The fixed network that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fixed<wbr>Subnet</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}=The fixed subnet that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>floating<wbr>Ip<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should create IP
floating IP for every node or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTP requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTPS requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The reference to an image that is used for nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insecure<wbr>Registry</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The insecure registry URL for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>keypair<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Compute service SSH keypair.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing additional properties
of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the master nodes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Lb<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should has a
loadbalancer for master nodes or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver for the container network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no<wbr>Proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of IP addresses that shouldn't be used in
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The project of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether cluster template should be public.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>registry<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether Docker registry is enabled in the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The server type for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls<wbr>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the TLS should be disabled in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated<wbr>At</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The user of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>volume<wbr>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver that is used for the volumes of the
cluster nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>apiserver_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The API server port for the Container Orchestration
Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>distro</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The distro for the cluster (fedora-atomic, coreos, etc.).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>coe</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Container Orchestration Engine for this cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>created_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>nameserver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Address of the DNS nameserver that is used in nodes of the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>docker_<wbr>storage_<wbr>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>docker_<wbr>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size (in GB) of the Docker volume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the external network that will be used for
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fixed_<wbr>network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The fixed network that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fixed_<wbr>subnet</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}=The fixed subnet that will be attached to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>floating_<wbr>ip_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should create IP
floating IP for every node or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTP requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https_<wbr>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The address of a proxy for receiving all HTTPS requests and
relay them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The reference to an image that is used for nodes of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>insecure_<wbr>registry</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The insecure registry URL for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>keypair_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Compute service SSH keypair.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}The list of key value pairs representing additional properties
of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>flavor</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The flavor for the master nodes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>lb_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether created cluster should has a
loadbalancer for master nodes or not.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver for the container network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no_<wbr>proxy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of IP addresses that shouldn't be used in
the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The project of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether cluster template should be public.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}See Argument Reference above.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>registry_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether Docker registry is enabled in the
cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The server type for the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tls_<wbr>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether the TLS should be disabled in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>updated_<wbr>at</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The time at which cluster template was updated.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The user of the cluster template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>volume_<wbr>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the driver that is used for the volumes of the
cluster nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







